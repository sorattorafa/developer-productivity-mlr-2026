#!/usr/bin/env python3
"""
Merge & Compare Claude vs NotebookLM Structured Summaries
==========================================================
Compares extraction outputs from two independent sources and generates
a concordance report for validation.

Usage:
    python merge_summaries.py --report           # Generate comparison report
    python merge_summaries.py --merge            # Create merged best-of-both summaries
    python merge_summaries.py --stats            # Quick concordance statistics
    python merge_summaries.py --divergences      # Show only divergent fields
"""

import argparse
import os
import re
import json
from pathlib import Path
from collections import Counter, defaultdict

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[3]
CLAUDE_DIR = BASE_DIR / "extraction" / "claude"
NOTEBOOKLM_DIR = Path(__file__).parent / "output"
MERGED_DIR = Path(__file__).parent / "merged"
REPORT_FILE = Path(__file__).parent / "comparison_report.md"

# Fields to compare
FIELDS_TO_EXTRACT = [
    "study_type",       # Tipo (Conference paper, Journal, etc.)
    "method",           # Metodo (Survey, Case study, etc.)
    "context",          # Contexto (Industry, OSS, etc.)
    "work_mode",        # Modo de trabalho
    "frameworks_ref",   # Frameworks referenced
    "frameworks_app",   # Frameworks applied
    "dora_applied",     # Whether DORA was applied
    "space_applied",    # Whether SPACE was applied
    "metrics",          # Metrics mentioned
    "ai_used",          # Whether AI/ML is discussed
    "quality_score",    # Quality assessment total
    "challenges",       # Number of challenges listed
    "factors_positive", # Positive factors count
    "factors_negative", # Negative factors count
]


# ============================================================
# FIELD EXTRACTION FROM MARKDOWN
# ============================================================

def strip_citations(text):
    """Remove NotebookLM-style citation references like [1], [2, 3], [1-4]."""
    return re.sub(r'\s*\[[\d,\s\-]+\]', '', text).strip()


def extract_table_field(text, field_name):
    """Extract a value from a markdown table row: | **Field** | Value |"""
    patterns = [
        rf'\|\s*\*\*{re.escape(field_name)}\*\*\s*\|\s*(.+?)\s*\|',
        rf'\|\s*{re.escape(field_name)}\s*\|\s*(.+?)\s*\|',
    ]
    for pattern in patterns:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            return strip_citations(m.group(1).strip())
    return None


def extract_section(text, header):
    """Extract content under a markdown ## or ### header."""
    # Try ## first, then ###
    for prefix in [r'##', r'###']:
        pattern = rf'{prefix}\s*{re.escape(header)}\s*\n(.*?)(?=\n##|\n###|\Z)'
        m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


def extract_section_fuzzy(text, *keywords):
    """Extract content under a header that contains any of the given keywords."""
    for kw in keywords:
        # Match ##, ###, or #### headers containing the keyword
        pattern = rf'^#{2,4}\s*[^\n]*{re.escape(kw)}[^\n]*\n(.*?)(?=\n#{2,4}\s[^#]|\Z)'
        m = re.search(pattern, text, re.DOTALL | re.IGNORECASE | re.MULTILINE)
        if m:
            return m.group(1).strip()
    return ""


def extract_all_metrics_tables(text):
    """Find ALL tables that look like metric tables anywhere in the document."""
    total_rows = 0
    # Find all table blocks in the document
    table_blocks = re.findall(
        r'(\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n?)*)',
        text, re.MULTILINE
    )
    for block in table_blocks:
        # Check if it looks like a metrics table (has category/level-like columns)
        header_line = block.split('\n')[0].lower()
        metric_headers = ["metrica", "metric", "categoria", "category", "nivel",
                         "level", "coletada", "collected", "validada"]
        if any(h in header_line for h in metric_headers):
            rows = block.strip().split('\n')
            # Subtract header + separator rows
            data_rows = len([r for r in rows[2:] if r.strip().startswith('|')])
            total_rows += data_rows
    return total_rows


def count_table_data_rows(section_text):
    """Count data rows in a markdown table (excludes header and separator rows)."""
    lines = section_text.split('\n')
    data_rows = 0
    in_table = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and '|' in stripped[1:]:
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                # Separator row like |---|---|
                in_table = True
                continue
            if in_table:
                # Check it's not another header
                if not re.match(r'^\|\s*\*\*[A-Z]', stripped):
                    data_rows += 1
                else:
                    # Could be a header row before separator
                    pass
            else:
                # First row before separator = header
                in_table = False
    # Fallback: count rows with | that aren't separator/header
    if data_rows == 0:
        all_rows = re.findall(r'^\|[^-].*\|', section_text, re.MULTILINE)
        # Subtract 1 for the header row
        data_rows = max(0, len(all_rows) - 1)
    return data_rows


def extract_fields(text):
    """Extract comparable fields from a structured summary."""
    fields = {}

    # Study type / Tipo
    fields["study_type"] = extract_table_field(text, "Tipo") or ""

    # Method
    fields["method"] = extract_table_field(text, "Metodo") or ""

    # Context
    fields["context"] = extract_table_field(text, "Contexto") or ""

    # Work mode
    fields["work_mode"] = extract_table_field(text, "Modo de trabalho") or ""

    # Frameworks section — search multiple possible headers
    fw_section = extract_section(text, "Frameworks e Metricas")
    fw_ref_section = extract_section(text, "Frameworks Referenciados")
    fw_prop_section = extract_section(text, "Frameworks Propostos")
    # Also search in C1 section (Claude format)
    c1_section = extract_section_fuzzy(text, "C1", "Frameworks Referenciados/Propostos")

    search_text = " ".join([fw_section, fw_ref_section, fw_prop_section, c1_section])

    # Extract framework names
    framework_keywords = ["DORA", "SPACE", "DevEx", "GQM", "HEART", "OKR",
                          "INVEST", "KPI", "BSC", "Accelerate"]
    found_fw = []
    for fw in framework_keywords:
        if re.search(rf'\b{fw}\b', search_text, re.IGNORECASE):
            found_fw.append(fw)
    fields["frameworks_ref"] = ", ".join(sorted(found_fw)) if found_fw else ""

    # DORA/SPACE applied — check for explicit "APPLIED" markers or Portuguese equivalents
    applied_keywords = ["applied", "aplicado", "aplicou", "instrumento",
                        "utilizado como", "used as", "foco central",
                        "base central", "measurement instrument"]

    def check_framework_applied(fw_name, text_to_search):
        """Check if a specific framework was applied (not just referenced)."""
        # Look for patterns like "DORA: APPLIED" or "DORA (Applied)"
        patterns = [
            rf'\b{fw_name}\b[^.]*?\bAPPLIED\b',
            rf'\b{fw_name}\b[^.]*?\baplicad[oa]\b',
            rf'\b{fw_name}\b[^.]*?\bfoco central\b',
            rf'\b{fw_name}\b[^.]*?\bbase central\b',
            rf'\b{fw_name}\b[^.]*?\bmeasurement instrument\b',
            rf'\b{fw_name}\b[^.]*?\butilizado como\b',
        ]
        for p in patterns:
            if re.search(p, text_to_search, re.IGNORECASE):
                return True
        return False

    fields["dora_applied"] = "Yes" if check_framework_applied("DORA", search_text) else "No"
    fields["space_applied"] = "Yes" if check_framework_applied("SPACE", search_text) else "No"

    # Also check the spreadsheet-style fields (DORA Applied / SPACE Applied columns from Claude)
    dora_field = extract_table_field(text, "DORA Applied") or ""
    space_field = extract_table_field(text, "SPACE Applied") or ""
    if any(w in dora_field.lower() for w in ["sim", "yes"]):
        fields["dora_applied"] = "Yes"
    if any(w in space_field.lower() for w in ["sim", "yes"]):
        fields["space_applied"] = "Yes"

    # Frameworks applied (derived)
    applied_list = []
    if fields["dora_applied"] == "Yes":
        applied_list.append("DORA")
    if fields["space_applied"] == "Yes":
        applied_list.append("SPACE")
    fields["frameworks_app"] = " ".join(applied_list)

    # Metrics — use broad search across entire document for metric tables
    metrics_count = extract_all_metrics_tables(text)
    if metrics_count == 0:
        # Fallback: search specific sections
        metrics_section = extract_section(text, "Metricas e Instrumentos de Avaliacao")
        if not metrics_section:
            metrics_section = extract_section_fuzzy(text, "Metricas Principais", "Metricas Especificas")
        if not metrics_section:
            metrics_section = extract_section_fuzzy(text, "C2", "Metricas")
        metrics_count = count_table_data_rows(metrics_section)
    fields["metrics"] = str(metrics_count)

    # AI
    ai_val = extract_table_field(text, "Usa IA/ML?") or ""
    # Also check "Impacto de IA" field
    ai_impact = extract_table_field(text, "Impacto de IA na produtividade?") or ""
    ai_text = (ai_val + " " + ai_impact).lower()
    # "No" only if explicitly stated as no/nao
    if any(w in ai_val.lower() for w in ["sim", "yes"]):
        fields["ai_used"] = "Yes"
    elif re.match(r'^n[aã]o\b', ai_val.strip().lower()):
        fields["ai_used"] = "No"
    elif "yes" in ai_text or "sim" in ai_text:
        fields["ai_used"] = "Yes"
    else:
        fields["ai_used"] = "No"

    # Quality score — handle **TOTAL** | **11/12 (Alta)** format
    quality_section = extract_section_fuzzy(text, "Avaliacao de Qualidade", "Qualidade Metodologica")
    # Try multiple patterns
    total_patterns = [
        r'\*{0,2}TOTAL\*{0,2}\s*\|\s*\*{0,2}(\d+)\s*/\s*(\d+)',  # **TOTAL** | **11/12
        r'TOTAL[^|]*\|\s*(\d+)/(\d+)',                              # TOTAL | 11/12
        r'TOTAL[^|]*\|\s*\*{1,2}(\d+)/(\d+)',                       # TOTAL | *11/12*
    ]
    fields["quality_score"] = ""
    for pattern in total_patterns:
        m = re.search(pattern, quality_section, re.IGNORECASE)
        if m:
            fields["quality_score"] = f"{m.group(1)}/{m.group(2)}"
            break

    # Challenges count — search multiple section names
    challenges = extract_section_fuzzy(text, "Desafios", "Challenges")
    if not challenges:
        challenges = extract_section_fuzzy(text, "Desafios do Uso")
    # Count numbered items, bullet points, and bold items
    challenge_items = re.findall(r'^\s*(\d+\.\s+|\*\s+|\-\s+)', challenges, re.MULTILINE)
    if not challenge_items:
        # Try counting bold items as challenges
        challenge_items = re.findall(r'\*\*[^*]+\*\*', challenges)
    fields["challenges"] = str(len(challenge_items))

    # Factors — search subsections with multiple name variants
    pos_section = extract_section_fuzzy(text, "Fatores Positivos", "Positive", "D1")
    neg_section = extract_section_fuzzy(text, "Fatores Negativos", "Negative", "D2")

    pos_count = count_table_data_rows(pos_section)
    neg_count = count_table_data_rows(neg_section)

    # If no tables found, count bullet/numbered items
    if pos_count == 0 and pos_section:
        pos_items = re.findall(r'^\s*(\d+\.\s+|\*\s+|\-\s+)', pos_section, re.MULTILINE)
        pos_count = len(pos_items)
    if neg_count == 0 and neg_section:
        neg_items = re.findall(r'^\s*(\d+\.\s+|\*\s+|\-\s+)', neg_section, re.MULTILINE)
        neg_count = len(neg_items)

    fields["factors_positive"] = str(pos_count)
    fields["factors_negative"] = str(neg_count)

    return fields


# ============================================================
# MATCHING FILES
# ============================================================

def find_claude_summary(paper_id):
    """Find the Claude-generated summary for a paper."""
    if not CLAUDE_DIR.exists():
        return None
    for f in CLAUDE_DIR.iterdir():
        if f.name.startswith(paper_id) and f.suffix == ".md":
            return f
    return None


def find_notebooklm_summary(paper_id):
    """Find the NotebookLM-generated summary for a paper."""
    expected = NOTEBOOKLM_DIR / f"{paper_id}_notebooklm.md"
    if expected.exists():
        return expected
    return None


# ============================================================
# COMPARISON
# ============================================================

def normalize(value):
    """Normalize a field value for comparison."""
    if not value:
        return ""
    v = value.lower().strip()
    # Strip any remaining citations
    v = re.sub(r'\s*\[[\d,\s\-]+\]', '', v).strip()
    # Strip bold markers
    v = v.replace("**", "")
    # Normalize common variants
    v = v.replace("conference paper", "conference")
    v = v.replace("journal article", "journal")
    v = v.replace("nao informado", "not specified")
    v = v.replace("nao especificado", "not specified")
    v = v.replace("não informado", "not specified")
    v = v.replace("not informed", "not specified")
    v = v.replace("mixed methods", "mixed")
    v = v.replace("mixed-methods", "mixed")
    v = v.replace("repository mining", "mining")
    v = v.replace("repo mining", "mining")
    # Normalize whitespace
    v = re.sub(r'\s+', ' ', v)
    return v


def normalize_type(value):
    """Normalize study type to canonical forms."""
    v = normalize(value)
    if not v:
        return ""
    # Map to canonical types
    type_map = {
        "conference": "conference",
        "conf paper": "conference",
        "journal": "journal",
        "book chapter": "book chapter",
        "technical report": "technical report",
        "thesis": "thesis",
        "master": "thesis",
        "phd": "thesis",
        "dissertation": "thesis",
        "literature review": "literature review",
        "systematic review": "literature review",
        "slr": "literature review",
        "survey": "survey",
        "preprint": "preprint",
        "arxiv": "preprint",
        "workshop": "workshop",
    }
    for key, canonical in type_map.items():
        if key in v:
            return canonical
    return v


def normalize_method(value):
    """Normalize research method to canonical forms."""
    v = normalize(value)
    if not v:
        return ""
    method_map = {
        "mining": "mining",
        "case study": "case study",
        "experiment": "experiment",
        "rct": "experiment",
        "randomized": "experiment",
        "survey": "survey",
        "questionnaire": "survey",
        "interview": "qualitative",
        "qualitative": "qualitative",
        "quantitative": "quantitative",
        "mixed": "mixed",
        "literature review": "literature review",
        "systematic": "literature review",
        "mlr": "literature review",
        "action research": "action research",
        "design science": "design science",
        "grounded theory": "qualitative",
    }
    for key, canonical in method_map.items():
        if key in v:
            return canonical
    return v


def normalize_context(value):
    """Normalize context to canonical forms."""
    v = normalize(value)
    if not v:
        return ""
    if "oss" in v or "open source" in v or "open-source" in v:
        ctx = "oss"
    elif "industr" in v or "enterprise" in v or "company" in v or "companies" in v:
        ctx = "industry"
    elif "academ" in v or "university" in v:
        ctx = "academic"
    elif "mixed" in v or ("oss" in v and "industr" in v):
        ctx = "mixed"
    else:
        ctx = v
    return ctx


def compare_field(val_claude, val_nlm, field_name):
    """Compare two field values and return concordance status."""
    # Apply field-specific normalization
    if field_name == "study_type":
        nc = normalize_type(val_claude)
        nn = normalize_type(val_nlm)
    elif field_name == "method":
        nc = normalize_method(val_claude)
        nn = normalize_method(val_nlm)
    elif field_name == "context":
        nc = normalize_context(val_claude)
        nn = normalize_context(val_nlm)
    else:
        nc = normalize(val_claude)
        nn = normalize(val_nlm)

    if not nc and not nn:
        return "both_empty"
    if not nc:
        return "only_nlm"
    if not nn:
        return "only_claude"
    if nc == nn:
        return "exact_match"
    # Fuzzy: check if one contains the other
    if nc in nn or nn in nc:
        return "partial_match"
    # For numeric fields, compare first number found
    if field_name in ("metrics", "challenges", "factors_positive", "factors_negative"):
        nc_num = re.search(r'\d+', nc)
        nn_num = re.search(r'\d+', nn)
        if nc_num and nn_num:
            # Within ±2 tolerance for counts (different section parsing can vary)
            diff = abs(int(nc_num.group()) - int(nn_num.group()))
            if diff == 0:
                return "exact_match"
            elif diff <= 2:
                return "partial_match"
    if field_name == "quality_score":
        nc_num = re.search(r'(\d+)/(\d+)', nc)
        nn_num = re.search(r'(\d+)/(\d+)', nn)
        if nc_num and nn_num:
            if nc_num.group(1) == nn_num.group(1):
                return "exact_match"
            elif abs(int(nc_num.group(1)) - int(nn_num.group(1))) <= 1:
                return "partial_match"
    # For binary fields, already handled above
    return "divergent"


def generate_comparison():
    """Generate full comparison between Claude and NotebookLM summaries."""
    # Get all paper IDs that have NotebookLM output
    nlm_files = list(NOTEBOOKLM_DIR.glob("*_notebooklm.md"))
    paper_ids = [f.stem.replace("_notebooklm", "") for f in nlm_files]

    if not paper_ids:
        print("No NotebookLM summaries found in output/")
        return None

    results = []
    for pid in sorted(paper_ids):
        claude_file = find_claude_summary(pid)
        nlm_file = find_notebooklm_summary(pid)

        if not claude_file:
            results.append({"id": pid, "status": "no_claude"})
            continue

        claude_text = claude_file.read_text(encoding="utf-8")
        nlm_text = nlm_file.read_text(encoding="utf-8")

        claude_fields = extract_fields(claude_text)
        nlm_fields = extract_fields(nlm_text)

        comparisons = {}
        for field in FIELDS_TO_EXTRACT:
            vc = claude_fields.get(field, "")
            vn = nlm_fields.get(field, "")
            status = compare_field(vc, vn, field)
            comparisons[field] = {
                "claude": vc,
                "notebooklm": vn,
                "status": status,
            }

        results.append({
            "id": pid,
            "status": "compared",
            "fields": comparisons,
        })

    return results


def compute_stats(results):
    """Compute concordance statistics from comparison results."""
    compared = [r for r in results if r["status"] == "compared"]
    if not compared:
        return None

    field_stats = defaultdict(Counter)
    for r in compared:
        for field, data in r["fields"].items():
            field_stats[field][data["status"]] += 1

    overall = Counter()
    for r in compared:
        for field, data in r["fields"].items():
            overall[data["status"]] += 1

    total_comparisons = sum(overall.values())
    agreement = overall["exact_match"] + overall["partial_match"]
    agreement_rate = agreement / total_comparisons * 100 if total_comparisons > 0 else 0

    return {
        "total_papers": len(compared),
        "total_comparisons": total_comparisons,
        "agreement_rate": agreement_rate,
        "overall": dict(overall),
        "by_field": {k: dict(v) for k, v in field_stats.items()},
    }


# ============================================================
# REPORT GENERATION
# ============================================================

def write_report(results, stats):
    """Write a comparison report in Markdown."""
    compared = [r for r in results if r["status"] == "compared"]

    lines = []
    lines.append("# Claude vs NotebookLM: Comparison Report")
    lines.append(f"\nGenerated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"\nPapers compared: {stats['total_papers']}")
    lines.append(f"Overall agreement rate: **{stats['agreement_rate']:.1f}%**")
    lines.append("")

    # Overall stats
    lines.append("## Overall Concordance")
    lines.append("")
    lines.append("| Status | Count | % |")
    lines.append("|--------|------:|--:|")
    total = stats["total_comparisons"]
    for status in ["exact_match", "partial_match", "divergent", "only_claude", "only_nlm", "both_empty"]:
        count = stats["overall"].get(status, 0)
        pct = count / total * 100 if total > 0 else 0
        lines.append(f"| {status} | {count} | {pct:.1f}% |")
    lines.append("")

    # Per field
    lines.append("## Concordance by Field")
    lines.append("")
    lines.append("| Field | Exact | Partial | Divergent | Agreement |")
    lines.append("|-------|------:|--------:|----------:|----------:|")
    for field in FIELDS_TO_EXTRACT:
        fs = stats["by_field"].get(field, {})
        exact = fs.get("exact_match", 0)
        partial = fs.get("partial_match", 0)
        divergent = fs.get("divergent", 0)
        total_f = exact + partial + divergent
        agree = (exact + partial) / total_f * 100 if total_f > 0 else 0
        lines.append(f"| {field} | {exact} | {partial} | {divergent} | {agree:.0f}% |")
    lines.append("")

    # Divergences detail
    lines.append("## Divergences (Require Manual Review)")
    lines.append("")
    for r in compared:
        divergent_fields = {k: v for k, v in r["fields"].items()
                          if v["status"] == "divergent"}
        if divergent_fields:
            lines.append(f"### {r['id']}")
            lines.append("")
            lines.append("| Field | Claude | NotebookLM |")
            lines.append("|-------|--------|------------|")
            for field, data in divergent_fields.items():
                c = data["claude"][:50] if data["claude"] else "(empty)"
                n = data["notebooklm"][:50] if data["notebooklm"] else "(empty)"
                lines.append(f"| {field} | {c} | {n} |")
            lines.append("")

    report_text = "\n".join(lines)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_text)

    return report_text


# ============================================================
# MERGE
# ============================================================

def merge_summaries(results):
    """Create merged summaries prioritizing NotebookLM when divergent."""
    MERGED_DIR.mkdir(exist_ok=True)

    compared = [r for r in results if r["status"] == "compared"]
    merged_count = 0

    for r in compared:
        pid = r["id"]
        claude_file = find_claude_summary(pid)
        nlm_file = find_notebooklm_summary(pid)

        if not claude_file or not nlm_file:
            continue

        # Start with Claude summary (more detailed format)
        claude_text = claude_file.read_text(encoding="utf-8")
        nlm_text = nlm_file.read_text(encoding="utf-8")

        # Add comparison metadata at the top
        header = f"<!-- MERGED SUMMARY: {pid} -->\n"
        header += f"<!-- Claude source: {claude_file.name} -->\n"
        header += f"<!-- NotebookLM source: {nlm_file.name} -->\n"

        divergent_fields = {k: v for k, v in r["fields"].items()
                          if v["status"] == "divergent"}

        if divergent_fields:
            header += "<!-- DIVERGENCES FOUND:\n"
            for field, data in divergent_fields.items():
                header += f"  {field}: Claude='{data['claude']}' vs NLM='{data['notebooklm']}'\n"
            header += "-->\n"

        header += "\n"

        # Use Claude as base, append NotebookLM notes at bottom
        merged = header + claude_text
        if divergent_fields:
            merged += "\n\n---\n\n## Notas de Verificacao (NotebookLM)\n\n"
            merged += "Os seguintes campos divergiram entre as duas extracoes:\n\n"
            merged += "| Campo | Claude | NotebookLM |\n"
            merged += "|-------|--------|------------|\n"
            for field, data in divergent_fields.items():
                merged += f"| {field} | {data['claude']} | {data['notebooklm']} |\n"
            merged += "\n**Acao necessaria:** Verificar manualmente no PDF original.\n"

        output_file = MERGED_DIR / f"{pid}_merged.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(merged)
        merged_count += 1

    print(f"Merged {merged_count} summaries to {MERGED_DIR}")
    return merged_count


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Compare and merge Claude vs NotebookLM summaries"
    )
    parser.add_argument("--report", action="store_true",
                        help="Generate full comparison report")
    parser.add_argument("--merge", action="store_true",
                        help="Create merged summaries")
    parser.add_argument("--stats", action="store_true",
                        help="Show concordance statistics")
    parser.add_argument("--divergences", action="store_true",
                        help="Show only divergent fields")

    args = parser.parse_args()

    if not any([args.report, args.merge, args.stats, args.divergences]):
        args.stats = True

    print("Generating comparison...")
    results = generate_comparison()
    if results is None:
        return

    stats = compute_stats(results)
    if stats is None:
        print("No papers could be compared.")
        return

    if args.stats or args.report:
        print(f"\n{'='*60}")
        print(f"CONCORDANCE STATISTICS")
        print(f"{'='*60}")
        print(f"Papers compared:  {stats['total_papers']}")
        print(f"Agreement rate:   {stats['agreement_rate']:.1f}%")
        print()
        print(f"{'Field':25s} {'Exact':>6s} {'Partial':>8s} {'Diverge':>8s} {'Agree%':>7s}")
        print(f"{'-'*25} {'-'*6} {'-'*8} {'-'*8} {'-'*7}")
        for field in FIELDS_TO_EXTRACT:
            fs = stats["by_field"].get(field, {})
            exact = fs.get("exact_match", 0)
            partial = fs.get("partial_match", 0)
            divergent = fs.get("divergent", 0)
            total_f = exact + partial + divergent
            agree = (exact + partial) / total_f * 100 if total_f > 0 else 0
            print(f"{field:25s} {exact:6d} {partial:8d} {divergent:8d} {agree:6.0f}%")

    if args.report:
        report = write_report(results, stats)
        print(f"\nReport saved to: {REPORT_FILE}")

    if args.divergences:
        compared = [r for r in results if r["status"] == "compared"]
        for r in compared:
            divs = {k: v for k, v in r["fields"].items() if v["status"] == "divergent"}
            if divs:
                print(f"\n{r['id']}:")
                for field, data in divs.items():
                    print(f"  {field}: Claude='{data['claude']}' vs NLM='{data['notebooklm']}'")

    if args.merge:
        merge_summaries(results)


if __name__ == "__main__":
    main()
