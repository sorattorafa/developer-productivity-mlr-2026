#!/usr/bin/env python3
"""
NotebookLM Paper Processor for MLR
===================================
Processes selected PDFs through Google NotebookLM to generate structured
summaries for triangulation with Claude-generated summaries.

Usage:
    python process_papers.py --mode extract --dry-run
    python process_papers.py --mode extract --batch-size 5
    python process_papers.py --mode extract --start-from P0030
    python process_papers.py --mode extract --only-gl
    python process_papers.py --mode extract --source IEEE
    python process_papers.py --mode sample --sample-size 25

Requirements:
    pip install "notebooklm-py[browser]" openpyxl
    playwright install chromium
    notebooklm login
"""

import asyncio
import argparse
import json
import os
import sys
import random
from pathlib import Path
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[3]
PDFS_DIR = BASE_DIR / "pdfs" / "selecionados"
EXCEL_PATH = BASE_DIR / "data" / "master" / "MLR_Final_Consolidated.xlsx"
OUTPUT_DIR = BASE_DIR / "extraction" / "notebooklm"
PROGRESS_FILE = Path(__file__).parent / "progress.json"

# Rate limit: wait between papers to avoid hitting Google's limits
DELAY_BETWEEN_PAPERS = 30  # seconds
DELAY_BETWEEN_BATCHES = 120  # seconds

def _set_delay(value):
    global DELAY_BETWEEN_PAPERS
    DELAY_BETWEEN_PAPERS = value

# ============================================================
# EXTRACTION PROMPT (mirrors the Claude structured summary format)
# ============================================================

EXTRACTION_PROMPT = """Analyze this research paper and extract a structured summary in the EXACT format below.
Use Portuguese for section headers but English for technical terms when appropriate.
Be precise and factual — only include information explicitly stated in the paper.

Format your response EXACTLY as follows:

# {PAPER_ID} — {TITLE}

**Decisao: INCLUIDO | Qualidade: {SCORE}/5**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | {PAPER_ID} |
| **Autores** | [list all authors] |
| **Ano** | [publication year] |
| **Venue** | [journal/conference name] |
| **DOI** | [DOI if available] |
| **Tipo** | [Conference paper / Journal article / Book chapter / Technical report / etc.] |
| **Metodo** | [Research method: Survey, Case study, Experiment, Mixed methods, Repository mining, Literature review, Qualitative, Quantitative, etc.] |
| **Amostra** | [Sample size and description] |
| **Contexto** | [Industry, OSS, Academic, Mixed — with details] |
| **Modo de trabalho** | [Remote, Hybrid, On-site, Not specified] |
| **Metodologia** | [Agile, DevOps, Waterfall, Mixed, Not specified] |

---

## Objetivo

[One paragraph describing the paper's main objective]

---

## Questoes de Pesquisa

[List each research question if any, prefixed with RQ1, RQ2, etc.]

---

## Metricas e Instrumentos de Avaliacao

[List ALL metrics mentioned in the paper with their definitions, how they are collected, and whether they are validated. Use a table format:]

| Metrica | Categoria | Nivel | Como Coletada | Validada |
|---------|-----------|-------|---------------|----------|
| [name]  | [category: Productivity, Quality, Collaboration, Satisfaction, Activity, Delivery, DevEx, etc.] | [Individual/Team/Organization] | [method] | [Yes/No/Partial] |

---

## Frameworks e Metricas

### Frameworks Referenciados
[List all frameworks mentioned: DORA, SPACE, DevEx, GQM, HEART, OKR, etc.]
- For each, indicate if it is REFERENCED (cited/discussed) or APPLIED (used as measurement instrument)

### Frameworks Propostos
[If the paper proposes a new framework, describe it]

---

## Fatores que Influenciam Produtividade

### Fatores Positivos
| Fator | Categoria |
|-------|-----------|
| [factor] | [Technical/Organizational/Human/Process] |

### Fatores Negativos
| Fator | Categoria |
|-------|-----------|
| [factor] | [Technical/Organizational/Human/Process] |

---

## Papel da IA e Automacao

| Campo | Valor |
|-------|-------|
| Usa IA/ML? | [Yes/No — describe if yes] |
| Automacao de coleta? | [Yes/No — describe if yes] |
| Impacto de IA na produtividade? | [Describe findings if applicable] |

---

## Resultados Principais

[Bullet points of key findings, with specific numbers when available]

---

## Desafios do Uso das Metricas

[List challenges and anti-patterns identified in the paper]

---

## Avaliacao de Qualidade Metodologica

| Criterio | Pontuacao (0-2) |
|----------|----------------|
| Objetivo claramente definido | [0-2] |
| Metodologia adequada ao objetivo | [0-2] |
| Amostra/contexto descrito adequadamente | [0-2] |
| Ameacas a validade discutidas | [0-2] |
| Resultados com evidencia suficiente | [0-2] |
| Contribuicao clara para pratica ou teoria | [0-2] |
| **TOTAL** | **[sum]/12** |

---

## Limitacoes

[List the paper's stated limitations]

---

## Contribuicao Principal

[One paragraph summarizing the key contribution]

---

*Extraido via NotebookLM em {DATE} para MLR: Software Developer Metrics in Practice*
"""

GL_EXTRACTION_PROMPT = """Analyze this grey literature source and extract a structured summary in the EXACT format below.
Grey literature includes blog posts, industry reports, white papers, and practitioner guides.
Use Portuguese for section headers but English for technical terms.
Be precise — only include information explicitly stated in the source.

Format your response EXACTLY as follows:

# {PAPER_ID} — {TITLE}

**Decisao: INCLUIDO | Qualidade GL: {SCORE}/6**

---

## Dados Bibliograficos

| Campo | Valor |
|-------|-------|
| **ID** | {PAPER_ID} |
| **Autor/Organizacao** | [author or organization] |
| **Data** | [publication date] |
| **Tipo** | [Blog post / Industry report / White paper / Guide / etc.] |
| **URL** | [URL if available] |

---

## Resumo

[2-3 paragraph summary of the content]

---

## Frameworks Mencionados

[List all frameworks: DORA, SPACE, DevEx, etc. — indicate if discussed, recommended, or critiqued]

---

## Metricas Mencionadas

[List all specific metrics mentioned with context]

---

## Insights para Praticantes

[Key takeaways and recommendations]

---

## Avaliacao de Qualidade GL (Garousi et al.)

| Criterio | Pontuacao (0-1) |
|----------|----------------|
| Autoridade do autor/organizacao | [0-1] |
| Descricao de metodologia | [0-1] |
| Data de publicacao | [0-1] |
| Objetividade (vies comercial) | [0-1] |
| Referencias citadas | [0-1] |
| Contribuicao nova | [0-1] |
| **TOTAL** | **[sum]/6** |

---

*Extraido via NotebookLM em {DATE} para MLR: Software Developer Metrics in Practice*
"""


# ============================================================
# PAPER LOADING
# ============================================================

def load_papers_from_excel():
    """Load all included papers from the consolidated spreadsheet."""
    import openpyxl

    wb = openpyxl.load_workbook(str(EXCEL_PATH), data_only=True)
    papers = []

    # Academic papers
    ws = wb["Included Papers"]
    for row in range(2, ws.max_row + 1):
        pid = ws.cell(row, 1).value
        title = ws.cell(row, 2).value
        source = ws.cell(row, 7).value
        pdf_rel = ws.cell(row, 28).value
        notes = ws.cell(row, 26).value or ""
        year = ws.cell(row, 4).value

        if "DESCARTADO" in str(notes).upper():
            continue

        # Map source to folder name
        source_folder = {
            "IEEE Xplore": "IEEE",
            "ACM Digital Library": "ACM",
            "Google Scholar": "Google_Scholar",
            "Scopus": "Scopus",
            "Springer Nature": "Springer_Nature",
            "Snowballing": "Snowballing",
        }.get(source, source or "Unknown")

        # Find PDF in selecionados
        pdf_path = None
        folder = PDFS_DIR / source_folder
        if folder.exists():
            for f in folder.iterdir():
                if f.name.startswith(f"{pid}_"):
                    pdf_path = f
                    break

        papers.append({
            "id": pid,
            "title": title or "Unknown",
            "source": source,
            "source_folder": source_folder,
            "year": year,
            "pdf_path": pdf_path,
            "type": "academic",
        })

    # Grey literature
    ws_gl = wb["Grey Literature"]
    for row in range(2, ws_gl.max_row + 1):
        gid = ws_gl.cell(row, 1).value
        title = ws_gl.cell(row, 2).value
        decision = ws_gl.cell(row, 12).value
        filename = ws_gl.cell(row, 11).value

        if not (decision and "INCLUIDO" in str(decision).upper()):
            continue

        pdf_path = None
        gl_folder = PDFS_DIR / "Grey_Literature"
        if gl_folder.exists():
            for f in gl_folder.iterdir():
                if f.name.startswith(f"{gid}_"):
                    pdf_path = f
                    break

        papers.append({
            "id": gid,
            "title": title or "Unknown",
            "source": "Grey Literature",
            "source_folder": "Grey_Literature",
            "year": None,
            "pdf_path": pdf_path,
            "type": "grey",
        })

    wb.close()
    return papers


# ============================================================
# PROGRESS TRACKING
# ============================================================

def load_progress():
    """Load processing progress from file."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": [], "failed": [], "skipped": []}


def save_progress(progress):
    """Save processing progress to file."""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


# ============================================================
# NOTEBOOKLM PROCESSING
# ============================================================

async def process_single_paper(client, paper, progress):
    """Process a single paper through NotebookLM."""
    pid = paper["id"]
    title = paper["title"]
    pdf_path = paper["pdf_path"]

    if not pdf_path or not pdf_path.exists():
        print(f"  SKIP {pid}: PDF not found")
        progress["skipped"].append({"id": pid, "reason": "PDF not found"})
        save_progress(progress)
        return False

    output_file = OUTPUT_DIR / f"{pid}_notebooklm.md"
    if output_file.exists():
        print(f"  SKIP {pid}: Already processed")
        return True

    print(f"  Processing {pid}: {title[:60]}...")

    try:
        # Create a dedicated notebook for this paper
        nb = await client.notebooks.create(f"MLR-{pid}")
        print(f"    Created notebook: {nb.id}")

        # Upload the PDF
        source = await client.sources.add_file(
            nb.id, str(pdf_path), wait=True, wait_timeout=180
        )
        print(f"    Source added: {source.id if hasattr(source, 'id') else 'ok'}")

        # Build the extraction prompt
        date_str = datetime.now().strftime("%B %Y")
        if paper["type"] == "grey":
            prompt = GL_EXTRACTION_PROMPT.replace("{PAPER_ID}", pid)
            prompt = prompt.replace("{TITLE}", title)
            prompt = prompt.replace("{SCORE}", "?")
            prompt = prompt.replace("{DATE}", date_str)
        else:
            prompt = EXTRACTION_PROMPT.replace("{PAPER_ID}", pid)
            prompt = prompt.replace("{TITLE}", title)
            prompt = prompt.replace("{SCORE}", "?")
            prompt = prompt.replace("{DATE}", date_str)

        # Query NotebookLM
        result = await client.chat.ask(nb.id, prompt)
        answer = result.answer if hasattr(result, "answer") else str(result)

        # Save the output
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(answer)

        print(f"    Saved: {output_file.name} ({len(answer)} chars)")

        # Clean up — delete the notebook to avoid clutter
        try:
            await client.notebooks.delete(nb.id)
            print(f"    Notebook deleted")
        except Exception:
            print(f"    Warning: Could not delete notebook")

        progress["completed"].append({
            "id": pid,
            "timestamp": datetime.now().isoformat(),
            "output_chars": len(answer),
        })
        save_progress(progress)
        return True

    except Exception as e:
        error_msg = str(e)
        print(f"    ERROR: {error_msg}")
        progress["failed"].append({
            "id": pid,
            "timestamp": datetime.now().isoformat(),
            "error": error_msg,
        })
        save_progress(progress)
        return False


async def run_extraction(papers, args):
    """Run the extraction pipeline."""
    progress = load_progress()
    completed_ids = {p["id"] for p in progress["completed"]}

    # Filter papers
    pending = [p for p in papers if p["id"] not in completed_ids]

    if args.start_from:
        found = False
        filtered = []
        for p in pending:
            if p["id"] == args.start_from:
                found = True
            if found:
                filtered.append(p)
        pending = filtered
        if not found:
            print(f"ERROR: Paper {args.start_from} not found in pending list")
            return

    if args.source:
        pending = [p for p in pending if p["source_folder"] == args.source]

    if args.only_gl:
        pending = [p for p in pending if p["type"] == "grey"]
    elif args.only_academic:
        pending = [p for p in pending if p["type"] == "academic"]

    total = len(pending)
    print(f"\nPapers to process: {total}")
    print(f"Already completed: {len(completed_ids)}")
    print(f"Batch size: {args.batch_size}")
    print()

    if args.dry_run:
        print("DRY RUN — would process:")
        for i, p in enumerate(pending[:args.batch_size], 1):
            has_pdf = "OK" if p["pdf_path"] and p["pdf_path"].exists() else "MISSING"
            print(f"  {i}. {p['id']} [{p['source_folder']}] [{has_pdf}] {p['title'][:60]}")
        print(f"\n  ... and {max(0, total - args.batch_size)} more")
        return

    from notebooklm import NotebookLMClient
    async with await NotebookLMClient.from_storage() as client:
        processed = 0
        for i, paper in enumerate(pending):
            if processed >= args.batch_size:
                print(f"\nBatch limit reached ({args.batch_size}). Run again to continue.")
                break

            print(f"\n[{processed+1}/{min(total, args.batch_size)}] ", end="")
            success = await process_single_paper(client, paper, progress)

            if success:
                processed += 1

            # Rate limiting
            if i < len(pending) - 1 and processed < args.batch_size:
                wait = DELAY_BETWEEN_PAPERS
                if processed > 0 and processed % 10 == 0:
                    wait = DELAY_BETWEEN_BATCHES
                    print(f"\n  Batch pause: waiting {wait}s...")
                else:
                    print(f"    Waiting {wait}s...")
                await asyncio.sleep(wait)

    # Summary
    progress = load_progress()
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"  Completed: {len(progress['completed'])}")
    print(f"  Failed:    {len(progress['failed'])}")
    print(f"  Skipped:   {len(progress['skipped'])}")
    print(f"{'='*60}")


# ============================================================
# SAMPLE MODE
# ============================================================

async def run_sample(papers, args):
    """Run extraction on a stratified random sample for validation."""
    academic = [p for p in papers if p["type"] == "academic"]

    # Stratify by period
    pre = [p for p in academic if p["year"] and int(p["year"]) <= 2019]
    pan = [p for p in academic if p["year"] and 2020 <= int(p["year"]) <= 2021]
    post = [p for p in academic if p["year"] and int(p["year"]) >= 2022]

    sample_size = args.sample_size
    # Proportional allocation
    n_pre = max(1, round(sample_size * len(pre) / len(academic)))
    n_pan = max(1, round(sample_size * len(pan) / len(academic)))
    n_post = sample_size - n_pre - n_pan

    random.seed(42)  # Reproducible
    sample = (
        random.sample(pre, min(n_pre, len(pre)))
        + random.sample(pan, min(n_pan, len(pan)))
        + random.sample(post, min(n_post, len(post)))
    )

    # Add a few GL sources
    gl = [p for p in papers if p["type"] == "grey"]
    gl_sample = random.sample(gl, min(5, len(gl)))
    sample.extend(gl_sample)

    print(f"Stratified sample ({len(sample)} papers):")
    print(f"  Pre-pandemic: {n_pre}")
    print(f"  Pandemic:     {n_pan}")
    print(f"  Post-pandemic: {n_post}")
    print(f"  Grey lit:     {len(gl_sample)}")
    print()

    for p in sample:
        has_pdf = "OK" if p["pdf_path"] and p["pdf_path"].exists() else "MISSING"
        print(f"  {p['id']} [{p['source_folder']}] [{has_pdf}] {p['title'][:60]}")

    if args.dry_run:
        print("\nDRY RUN — use without --dry-run to process")
        # Save sample list for reference
        sample_file = Path(__file__).parent / "sample_list.json"
        with open(sample_file, "w") as f:
            json.dump([{"id": p["id"], "type": p["type"], "title": p["title"]}
                       for p in sample], f, indent=2)
        print(f"Sample list saved to: {sample_file}")
        return

    # Process sample
    args.batch_size = len(sample)
    # Override pending list with sample only
    from notebooklm import NotebookLMClient

    progress = load_progress()

    async with await NotebookLMClient.from_storage() as client:
        for i, paper in enumerate(sample):
            print(f"\n[{i+1}/{len(sample)}] ", end="")
            await process_single_paper(client, paper, progress)
            if i < len(sample) - 1:
                await asyncio.sleep(DELAY_BETWEEN_PAPERS)


# ============================================================
# STATUS
# ============================================================

def show_status(papers):
    """Show current processing status."""
    progress = load_progress()
    completed_ids = {p["id"] for p in progress["completed"]}
    failed_ids = {p["id"] for p in progress["failed"]}

    academic = [p for p in papers if p["type"] == "academic"]
    grey = [p for p in papers if p["type"] == "grey"]

    ac_done = sum(1 for p in academic if p["id"] in completed_ids)
    gl_done = sum(1 for p in grey if p["id"] in completed_ids)

    print(f"{'='*60}")
    print(f"PROCESSING STATUS")
    print(f"{'='*60}")
    print(f"Academic:  {ac_done}/{len(academic)} completed")
    print(f"Grey Lit:  {gl_done}/{len(grey)} completed")
    print(f"Total:     {ac_done + gl_done}/{len(papers)} completed")
    print(f"Failed:    {len(failed_ids)}")
    print()

    if failed_ids:
        print("Failed papers:")
        for p in progress["failed"]:
            print(f"  {p['id']}: {p['error'][:80]}")
        print()

    # By source
    from collections import Counter
    done_by_source = Counter()
    total_by_source = Counter()
    for p in papers:
        total_by_source[p["source_folder"]] += 1
        if p["id"] in completed_ids:
            done_by_source[p["source_folder"]] += 1

    print("By source:")
    for src in sorted(total_by_source):
        print(f"  {src:20s}: {done_by_source[src]:3d}/{total_by_source[src]:3d}")


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Process MLR papers through NotebookLM"
    )
    parser.add_argument(
        "--mode",
        choices=["extract", "sample", "status", "retry"],
        default="status",
        help="Processing mode",
    )
    parser.add_argument("--batch-size", type=int, default=10,
                        help="Papers per batch (default: 10)")
    parser.add_argument("--sample-size", type=int, default=25,
                        help="Sample size for validation (default: 25)")
    parser.add_argument("--start-from", type=str, default=None,
                        help="Start from specific paper ID")
    parser.add_argument("--source", type=str, default=None,
                        help="Filter by source folder (IEEE, ACM, etc.)")
    parser.add_argument("--only-gl", action="store_true",
                        help="Only process grey literature")
    parser.add_argument("--only-academic", action="store_true",
                        help="Only process academic papers")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be processed without doing it")
    parser.add_argument("--delay", type=int, default=None,
                        help=f"Delay between papers in seconds (default: {DELAY_BETWEEN_PAPERS})")

    args = parser.parse_args()

    if args.delay is not None:
        _set_delay(args.delay)

    print("Loading papers from spreadsheet...")
    papers = load_papers_from_excel()
    print(f"Loaded {len(papers)} papers ({sum(1 for p in papers if p['type']=='academic')} academic, "
          f"{sum(1 for p in papers if p['type']=='grey')} grey lit)")

    # Check PDFs
    with_pdf = sum(1 for p in papers if p["pdf_path"] and p["pdf_path"].exists())
    print(f"PDFs available: {with_pdf}/{len(papers)}")

    if args.mode == "status":
        show_status(papers)
    elif args.mode == "extract":
        asyncio.run(run_extraction(papers, args))
    elif args.mode == "sample":
        asyncio.run(run_sample(papers, args))
    elif args.mode == "retry":
        # Reset failed papers so they can be retried
        progress = load_progress()
        failed_ids = {p["id"] for p in progress["failed"]}
        progress["failed"] = []
        save_progress(progress)
        print(f"Reset {len(failed_ids)} failed papers for retry")
        asyncio.run(run_extraction(papers, args))


if __name__ == "__main__":
    main()
