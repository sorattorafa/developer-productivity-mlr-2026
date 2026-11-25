#!/usr/bin/env python3
"""Scan grey full texts for DORA/SPACE/DevEx mentions -> candidate list for human validation.
Output: data/validation/grey_mentions_candidates.xlsx (one row per source x framework hit,
with context snippets). Zero-hit sources listed on a second sheet.
"""
import os, re, glob
import openpyxl
from openpyxl import Workbook

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MASTER = os.path.join(ROOT, "data", "master", "MLR_Final_Consolidated.xlsx")
PDF_DIRS = [os.path.join(ROOT, "pdfs", "grey_literature"),
            os.path.join(ROOT, "pdfs", "selecionados", "Grey_Literature")]

PATTERNS = {
    "DORA":  re.compile(r"\bDORA\b"),
    "SPACE": re.compile(r"\bSPACE\b"),           # all-caps only; validar contexto
    "DevEx": re.compile(r"\bDev[Ee]x\b"),
}

def load_text(gid):
    cands = []
    for d in PDF_DIRS:
        cands += glob.glob(os.path.join(d, f"{gid}_*")) + glob.glob(os.path.join(d, f"*{gid}*"))
    for f in sorted(set(cands)):
        if f.lower().endswith(".txt"):
            try: return open(f, encoding="utf-8", errors="ignore").read(), os.path.basename(f)
            except OSError: pass
    for f in sorted(set(cands)):
        if f.lower().endswith(".pdf"):
            try:
                import pdfplumber
                with pdfplumber.open(f) as pdf:
                    return "\n".join((p.extract_text() or "") for p in pdf.pages), os.path.basename(f)
            except Exception: pass
    return None, None

def snippets(text, rx, n=2, w=90):
    out = []
    for m in rx.finditer(text):
        a, b = max(0, m.start()-w), min(len(text), m.end()+w)
        out.append(" ".join(text[a:b].split()))
        if len(out) >= n: break
    return out

wb = openpyxl.load_workbook(MASTER, read_only=True)
gl = [r for r in list(wb["Grey Literature"].iter_rows(values_only=True))[1:] if str(r[19]).strip() == "Include"]
Y = lambda v: str(v).strip().lower().startswith("yes")

out = Workbook(); ws = out.active; ws.title = "candidates"
ws.append(["G-id", "Title", "Framework", "Hits", "Applied (H)", "Mentioned? [VALIDATE: Yes/No]", "Snippet 1", "Snippet 2", "File"])
ws2 = out.create_sheet("no_text_or_no_hits")
ws2.append(["G-id", "Title", "Status"])

stats = {f: 0 for f in PATTERNS}
for r in gl:
    gid, title = str(r[0]).strip(), str(r[1])[:80]
    applied = {"DORA": Y(r[22]), "SPACE": Y(r[23]), "DevEx": None}
    text, fname = load_text(gid)
    if not text or len(text) < 200:
        ws2.append([gid, title, "NO USABLE TEXT (stub or not found)"]); continue
    any_hit = False
    for fw, rx in PATTERNS.items():
        hits = len(rx.findall(text))
        if hits:
            any_hit = True; stats[fw] += 1
            sn = snippets(text, rx)
            ws.append([gid, title, fw, hits, str(applied[fw]), "", sn[0] if sn else "", sn[1] if len(sn) > 1 else "", fname])
    if not any_hit:
        ws2.append([gid, title, "zero hits for the 3 frameworks"])

dest = os.path.join(ROOT, "data", "validation", "grey_mentions_candidates.xlsx")
out.save(dest)
print("included gray sources:", len(gl))
print("sources with hits per framework:", stats)
print("planilha:", dest)
