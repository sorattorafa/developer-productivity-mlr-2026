#!/usr/bin/env python3
"""
NotebookLM extraction for the October 2026 search update.

Reuses process_papers.py (same prompts, same output format, same rate limits).
Only the list of sources changes: it is read from update_2026-10_papers.json,
and the full texts are read from pdfs/selecionados/Update_2026-10/<ID>_*.pdf or <ID>_*.txt
(.txt = page text saved from ScienceDirect HTML or gray-literature web pages).
Sources without a file were excluded at full text (EC6) and are skipped;
the reason for each one is in data/master/FULL_TEXT_RETRIEVAL_2026-10.xlsx.
Outputs go to extraction/notebooklm/<ID>_notebooklm.md, as before.
Progress is kept in progress_update_2026-10.json so the original progress file is untouched.

Usage (from extraction/scripts/notebooklm/):
    python process_update.py --mode status
    python process_update.py --mode extract --dry-run
    python process_update.py --mode extract --batch-size 10
    python process_update.py --mode retry --batch-size 5
"""
import asyncio
import json
import sys
from pathlib import Path

import process_papers as pp

HERE = Path(__file__).resolve().parent
LIST_FILE = HERE / "update_2026-10_papers.json"
PDF_DIR = pp.BASE_DIR / "pdfs" / "selecionados" / "Update_2026-10"
pp.PROGRESS_FILE = HERE / "progress_update_2026-10.json"


def load_update_papers():
    items = json.loads(LIST_FILE.read_text(encoding="utf-8"))
    papers = []
    for it in items:
        pdf_path = None
        if PDF_DIR.exists():
            for f in sorted(PDF_DIR.iterdir()):
                if f.name.startswith(f"{it['id']}_"):
                    pdf_path = f
                    break
        if pdf_path is None:
            continue  # EC6: full text not accessible (see FULL_TEXT_RETRIEVAL_2026-10.xlsx)
        papers.append({
            "id": it["id"],
            "title": it["title"],
            "source": "Update 2026-10",
            "source_folder": "Update_2026-10",
            "year": it.get("year"),
            "pdf_path": pdf_path,
            "type": it["type"],
        })
    return papers


pp.load_papers_from_excel = load_update_papers

if __name__ == "__main__":
    pp.main()
