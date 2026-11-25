#!/usr/bin/env python3
"""Verdict-level accuracy of the LLM extractors against the human decision.

Reads the decision line (**Decisao: INCLUIDO/EXCLUIDO ...**) of every extraction file in
extraction/claude/ and extraction/notebooklm/, pairs it with the final human verdict in
data/master/MLR_Final_Consolidated.xlsx (columns 'MY VERDICT - Relevance' of the academic
and grey sheets), and prints TP / TN / FP / FN and accuracy per extractor and corpus,
with the human decision as the oracle (Felizardo et al., 2024).

Definitions at the inclusion level:
  TP = extractor includes and reviewer includes
  TN = extractor excludes and reviewer excludes
  FP = extractor includes and reviewer excludes
  FN = extractor excludes and reviewer includes
Sources without a decision line in the extraction file, or without a final human
Include/Exclude verdict (e.g., reclassified records), are excluded from the pair.

Run from the repository root:  python3 extraction/scripts/verdict_accuracy.py
"""
import re
import unicodedata
from pathlib import Path

import openpyxl

BASE = Path(__file__).resolve().parents[2]
MASTER = BASE / "data" / "master" / "MLR_Final_Consolidated.xlsx"


def extractor_verdicts(folder: Path) -> dict:
    out = {}
    for f in sorted(folder.glob("*.md")):
        m = re.match(r"(P\d{4}|P_NEW_1|G\d{3})", f.name)
        if not m:
            continue
        pid = m.group(1)
        if pid in out:
            continue
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("**Decisao"):
                token = unicodedata.normalize("NFKD", line).upper()
                if "INCLU" in token:
                    out[pid] = "Include"
                elif "EXCLU" in token:
                    out[pid] = "Exclude"
                break
    return out


def human_verdicts() -> dict:
    wb = openpyxl.load_workbook(MASTER, read_only=True, data_only=True)
    out = {}
    for sheet, id_col, verdict_col in (("Included Papers", 0, 30), ("Grey Literature", 0, 19)):
        ws = wb[sheet]
        rows = ws.iter_rows(values_only=True)
        next(rows)
        for r in rows:
            if not r or r[id_col] is None:
                continue
            v = str(r[verdict_col]).strip() if r[verdict_col] else ""
            if v in ("Include", "Exclude"):
                out[str(r[id_col]).strip()] = v
    wb.close()
    return out


def confusion(ai: dict, human: dict, prefix: str):
    tp = tn = fp = fn = 0
    for pid, hv in human.items():
        if not pid.startswith(prefix):
            continue
        av = ai.get(pid)
        if av is None:
            continue
        if av == "Include" and hv == "Include":
            tp += 1
        elif av == "Exclude" and hv == "Exclude":
            tn += 1
        elif av == "Include" and hv == "Exclude":
            fp += 1
        else:
            fn += 1
    return tp, tn, fp, fn


def main():
    human = human_verdicts()
    claude = extractor_verdicts(BASE / "extraction" / "claude")
    nblm = extractor_verdicts(BASE / "extraction" / "notebooklm")
    print(f"{'Corpus / extractor':28} {'TP':>4} {'TN':>4} {'FP':>4} {'FN':>4} {'Accuracy':>9}")
    for name, ai in (("Claude", claude), ("NotebookLM", nblm)):
        for label, prefix in (("Academic", "P"), ("Grey", "G")):
            tp, tn, fp, fn = confusion(ai, human, prefix)
            total = tp + tn + fp + fn
            acc = (tp + tn) / total if total else float("nan")
            print(f"{label + ' - ' + name:28} {tp:>4} {tn:>4} {fp:>4} {fn:>4} {acc:>8.1%}")


if __name__ == "__main__":
    main()
