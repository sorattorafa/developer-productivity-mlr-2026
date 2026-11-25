#!/usr/bin/env python3
"""
Claude vs NotebookLM comparison for the October 2026 search update.

Reads the two extraction forms for each source of the update
(extraction/claude/<ID>.md and extraction/notebooklm/<ID>_notebooklm.md),
compares the fields used in the original comparison (comparison_report.md),
and writes:
  - extraction/comparison_report_update_2026-10.md   (summary + divergences)
  - extraction/comparison_update_2026-10.xlsx        (one row per source x field,
                                                       with a column for the reviewer's resolution)

The comparison is an audit aid. The reviewer resolves divergences against the full text.

Usage (from the project root):
    python3 extraction/scripts/compare_update_2026-10.py
"""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXT = ROOT / "extraction"
LIST = EXT / "scripts" / "notebooklm" / "update_2026-10_papers.json"
OUT_MD = EXT / "comparison_report_update_2026-10.md"
OUT_XLSX = EXT / "comparison_update_2026-10.xlsx"

FRAMEWORKS = {
    "DORA": r"\bDORA\b|DevOps Research|Accelerate metrics|four key metrics",
    "SPACE": r"\bSPACE\b",
    "DevEx": r"\bDevEx\b|Developer Experience framework|DX Core 4|Core 4",
    "GQM": r"\bGQM\b|Goal[- ]Question[- ]Metric",
    "HEART": r"\bHEART\b",
    "OKR": r"\bOKRs?\b",
    "Flow (Flow Framework)": r"Flow Framework|Flow Metrics",
    "TAM/UTAUT": r"\bTAM\b|\bUTAUT",
    "ISO 25010": r"25010",
    "COCOMO/FPA": r"COCOMO|Function Point",
    "AI Measurement Framework (DX)": r"AI Measurement Framework",
}

STOP = set("a o e de da do das dos em para por com sem na no nas nos um uma the of and in on for to with by from as at or an is are not nao".split())


def read(p):
    return p.read_text(encoding="utf-8", errors="ignore") if p.exists() else ""


def section(text, title):
    m = re.search(r"^##+\s*" + re.escape(title) + r"[^\n]*\n(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def table_value(text, field):
    m = re.search(r"^\|\s*\*{0,2}" + re.escape(field) + r"\*{0,2}\s*\|\s*(.*?)\s*\|\s*$", text, re.M)
    if not m:
        return ""
    v = re.sub(r"\[\d+(?:[-,\s]+\d+)*\]", "", m.group(1))  # drop NotebookLM citation markers
    v = v.replace("**", "").strip()
    return "" if v.lower().startswith(("nao reportado", "not reported", "not specified", "n/a")) and len(v) < 25 else v


def score(text):
    m = re.search(r"Qualidade(?: GL)?:\s*([\d.,]+)\s*/\s*(\d+)", text)
    head = f"{m.group(1)}/{m.group(2)}" if m else ""
    t = re.search(r"\*\*TOTAL\*\*\s*\|\s*\*\*\s*([\d.,]+)\s*/\s*(\d+)", text)
    total = f"{t.group(1)}/{t.group(2)}" if t else ""
    return head, total


def frameworks(text, kind):
    sec = section(text, "Frameworks e Metricas") if kind == "academic" else section(text, "Frameworks Mencionados")
    found, applied = set(), set()
    for name, pat in FRAMEWORKS.items():
        for line in sec.splitlines():
            if re.search(pat, line, re.I):
                found.add(name)
                if re.search(r"APPLIED|APLICAD", line) and not re.search(r"NOT APPLIED|NAO APLICAD", line, re.I):
                    applied.add(name)
    return found, applied


def metrics(text, kind):
    if kind == "academic":
        sec = section(text, "Metricas e Instrumentos de Avaliacao")
        names = []
        for line in sec.splitlines():
            if line.startswith("|") and not re.match(r"^\|\s*(Metrica|-{3,})", line):
                cell = line.strip("|").split("|")[0]
                names.append(cell)
    else:
        sec = section(text, "Metricas Mencionadas")
        names = [re.sub(r"^[-*\d.\s]+", "", l).split(":")[0].split(" — ")[0] for l in sec.splitlines() if re.match(r"^\s*([-*]|\d+\.)\s", l)]
    out = set()
    for n in names:
        n = re.sub(r"\[\d+(?:[-,\s]+\d+)*\]|\*|`|\(.*?\)", "", n).strip().lower()
        n = re.sub(r"[^a-z0-9 /%-]", " ", n)
        n = re.sub(r"\s+", " ", n).strip()
        if len(n) > 2:
            out.add(n)
    return out


def ai_used(text):
    v = table_value(text, "Usa IA/ML?")
    if not v:
        return ""
    return "Yes" if re.match(r"\s*(yes|sim)", v, re.I) else ("No" if re.match(r"\s*(no|nao)", v, re.I) else v[:40])


def toks(s):
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2}


def cmp_text(a, b):
    if not a and not b:
        return "both_empty"
    if not a:
        return "only_nlm"
    if not b:
        return "only_claude"
    ta, tb = toks(a), toks(b)
    if not ta or not tb:
        return "exact_match" if a.strip().lower() == b.strip().lower() else "divergent"
    j = len(ta & tb) / len(ta | tb)
    if j >= 0.6 or a.strip().lower() == b.strip().lower():
        return "exact_match"
    if j >= 0.2 or ta <= tb or tb <= ta:
        return "partial_match"
    return "divergent"


def cmp_set(a, b):
    if not a and not b:
        return "both_empty"
    if not a:
        return "only_nlm"
    if not b:
        return "only_claude"
    if a == b:
        return "exact_match"
    return "partial_match" if a & b else "divergent"


def cmp_flag(a, b):
    if not a and not b:
        return "both_empty"
    if not a:
        return "only_nlm"
    if not b:
        return "only_claude"
    return "exact_match" if a == b else "divergent"


def cmp_score(a, b, tol):
    if not a and not b:
        return "both_empty"
    if not a:
        return "only_nlm"
    if not b:
        return "only_claude"
    fa = float(a.split("/")[0].replace(",", "."))
    fb = float(b.split("/")[0].replace(",", "."))
    if fa == fb:
        return "exact_match"
    return "partial_match" if abs(fa - fb) <= tol else "divergent"


def fuzzy_overlap(a, b):
    """metric names: count a name as shared when its tokens overlap >= 50% with some name of the other side."""
    shared = 0
    for x in a:
        tx = toks(x)
        if any(tx and (len(tx & toks(y)) / max(1, min(len(tx), len(toks(y))))) >= 0.5 for y in b):
            shared += 1
    return shared


def main():
    items = json.loads(LIST.read_text(encoding="utf-8"))
    rows, summary, per_source = [], {}, []
    for it in items:
        pid = it["id"]
        kind = "grey" if it["type"].lower().startswith(("grey", "gl", "gray")) or pid.startswith("G") else "academic"
        c = read(EXT / "claude" / f"{pid}.md")
        n = read(EXT / "notebooklm" / f"{pid}_notebooklm.md")
        if not c and not n:
            continue  # EC6: no full text, not extracted
        fields = []
        if kind == "academic":
            for f, key in [("Tipo", "study_type"), ("Metodo", "method"), ("Amostra", "sample"), ("Contexto", "context"),
                           ("Modo de trabalho", "work_mode"), ("Metodologia", "process")]:
                a, b = table_value(c, f), table_value(n, f)
                fields.append((key, a, b, cmp_text(a, b)))
        else:
            for f, key in [("Tipo", "gl_type"), ("Data", "date"), ("Autor/Organizacao", "author")]:
                a, b = table_value(c, f), table_value(n, f)
                fields.append((key, a, b, cmp_text(a, b)))
        fa, aa = frameworks(c, kind)
        fb, ab = frameworks(n, kind)
        fields.append(("frameworks_ref", ", ".join(sorted(fa)), ", ".join(sorted(fb)), cmp_set(fa, fb)))
        if kind == "academic":
            fields.append(("frameworks_app", ", ".join(sorted(aa)), ", ".join(sorted(ab)), cmp_set(aa, ab)))
            for fw, key in [("DORA", "dora_applied"), ("SPACE", "space_applied"), ("DevEx", "devex_applied")]:
                a = "Yes" if fw in aa else "No"
                b = "Yes" if fw in ab else "No"
                fields.append((key, a, b, "exact_match" if a == b else "divergent"))
            a, b = ai_used(c), ai_used(n)
            fields.append(("ai_used", a, b, cmp_flag(a, b)))
        ma, mb = metrics(c, kind), metrics(n, kind)
        sh = fuzzy_overlap(ma, mb)
        mstat = "both_empty" if not ma and not mb else ("only_nlm" if not ma else ("only_claude" if not mb else
                ("exact_match" if sh >= 0.6 * max(len(ma), len(mb)) else ("partial_match" if sh else "divergent"))))
        fields.append(("metrics", f"{len(ma)} metrics", f"{len(mb)} metrics ({sh} in common)", mstat))
        ha, ta = score(c)
        hb, tb = score(n)
        if kind == "academic":
            fields.append(("quality_total_12", ta, tb, cmp_score(ta, tb, 2)))
        else:
            fields.append(("quality_gl_6", ta or ha, tb or hb, cmp_score(ta or ha, tb or hb, 1)))
        partial_c = "texto parcial" in c.lower()
        for key, a, b, st in fields:
            rows.append([pid, kind, key, a, b, st, "", ""])
            summary.setdefault((kind, key), {}).setdefault(st, 0)
            summary[(kind, key)][st] += 1
        div = [k for k, a, b, st in fields if st in ("divergent",)]
        per_source.append((pid, kind, it["title"], div, partial_c))

    # ---- markdown report
    stats = ["exact_match", "partial_match", "divergent", "only_claude", "only_nlm", "both_empty"]
    L = [f"# Claude vs NotebookLM: search update of October 2026", "",
         f"Generated on {date.today().isoformat()} by `extraction/scripts/compare_update_2026-10.py`.", "",
         f"Sources compared: {len(per_source)} ({sum(1 for p in per_source if p[1]=='academic')} academic, "
         f"{sum(1 for p in per_source if p[1]=='grey')} gray). EC6 sources (full text not retrieved) were not extracted.", "",
         "Same typology as the original report (`comparison_report.md`): exact_match, partial_match, divergent, "
         "only_claude, only_nlm, both_empty. The comparison is automatic and serves as support; the resolution is made by the reviewer against the full text, "
         "in the \"Resolution (reviewer)\" column of `comparison_update_2026-10.xlsx`.", "",
         "Criteria: free text by word overlap (≥60% exact, ≥20% partial); frameworks as a set; "
         "DORA/SPACE/DevEx applied from the APPLIED marks; metrics by overlap of the names; quality with a tolerance of 2/12 (academic) and 1/6 (gray) for partial.", ""]
    tot = {s: 0 for s in stats}
    for v in summary.values():
        for s, k in v.items():
            tot[s] += k
    T = sum(tot.values())
    L += ["## Overall agreement", "", "| Status | n | % |", "|---|--:|--:|"]
    for s in stats:
        L.append(f"| {s} | {tot[s]} | {100*tot[s]/T:.1f}% |")
    for kind in ("academic", "grey"):
        L += ["", f"## Agreement per field, {'academic' if kind=='academic' else 'gray'} sources", "",
              "| Field | " + " | ".join(stats) + " | Agreement (exact+partial) |", "|---|" + "--:|" * (len(stats) + 1)]
        for (k, key), v in summary.items():
            if k != kind:
                continue
            n_ = sum(v.values())
            ok = v.get("exact_match", 0) + v.get("partial_match", 0)
            comparable = n_ - v.get("both_empty", 0)
            L.append(f"| {key} | " + " | ".join(str(v.get(s, 0)) for s in stats) +
                     f" | {100*ok/comparable:.0f}% |" if comparable else f"| {key} | " + " | ".join(str(v.get(s, 0)) for s in stats) + " | — |")
    L += ["", "## Divergences per source (to be resolved during reading)", "",
          "| ID | Type | Divergent fields | Title |", "|---|---|---|---|"]
    for pid, kind, title, div, partial_c in per_source:
        if div:
            L.append(f"| {pid} | {kind} | {', '.join(div)} | {title[:70]} |")
    nodiv = [p[0] for p in per_source if not p[3]]
    L += ["", f"Sources with no divergent field ({len(nodiv)}): {', '.join(nodiv)}", ""]
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- spreadsheet
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook()
    ws = wb.active
    ws.title = "Comparison"
    head = ["ID", "Type", "Field", "Claude", "NotebookLM", "Status", "Resolution (reviewer)", "Note"]
    ws.append(head)
    for r in rows:
        ws.append(r)
    fill = {"divergent": "F8D7DA", "only_claude": "FFF3CD", "only_nlm": "FFF3CD", "partial_match": "E2EFDA"}
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F4E78")
    for row in ws.iter_rows(min_row=2):
        st = row[5].value
        if st in fill:
            row[5].fill = PatternFill("solid", fgColor=fill[st])
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        row[6].fill = PatternFill("solid", fgColor="FFFFE0")
    dv = DataValidation(type="list", formula1='"Claude,NotebookLM,Both,Neither (corrected),N/A"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"G2:G{ws.max_row}")
    for col, w in zip("ABCDEFGH", (8, 9, 16, 55, 55, 13, 18, 30)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    s2 = wb.create_sheet("Summary")
    s2.append(["Type", "Field"] + stats)
    for (k, key), v in summary.items():
        s2.append([k, key] + [v.get(s, 0) for s in stats])
    for c in s2[1]:
        c.font = Font(bold=True)
    wb.save(OUT_XLSX)
    print(f"{len(per_source)} sources, {len(rows)} field comparisons")
    print({s: tot[s] for s in stats})
    print(OUT_MD.relative_to(ROOT), OUT_XLSX.relative_to(ROOT))


if __name__ == "__main__":
    main()
