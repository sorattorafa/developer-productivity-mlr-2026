#!/usr/bin/env python3
"""Framework engagement flow (Sankey): proposal -> referenced (academic | grey)
-> applied empirically / guidance / referenced-only.

Reads the master spreadsheet (Mentioned (H) and Applied Level (H) columns on the
Grey Literature sheet). Academic referenced/applied come from mlr_stats.json.
Output: latex-article/figures/fig_framework_flow.(png|pdf). Requires plotly+kaleido.
"""
import json, os
import openpyxl
import plotly.graph_objects as go

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# D1 recount 2026-10-19 (228 sources): academic cited = Frameworks Mentioned or used as instrument (master),
# used = DORA/SPACE Applied (H) and DevEx Dimensions (H); gray levels from recount_2026-10.json
rc = json.load(open(os.path.join(ROOT, "data", "master", "recount_2026-10.json")))["integrated"]
CITED = {"DORA": 19, "SPACE": 49, "DevEx": 37}
acad = {f: (CITED[f], rc["acad_applied"][f]["n"]) for f in ("DORA", "SPACE", "DevEx")}
lv = rc["grey_levels"]

COL = {"DORA": "#1f77b4", "SPACE": "#ff7f0e", "DevEx": "#2ca02c"}
L = {"DORA": "rgba(31,119,180,0.45)", "SPACE": "rgba(255,127,14,0.45)", "DevEx": "rgba(44,160,44,0.45)"}
GRY, AMB = "rgba(160,160,160,0.45)", "rgba(200,170,90,0.5)"

labels, colors, src, tgt, val, lcol = [], [], [], [], [], []
def node(lbl, c):
    labels.append(lbl); colors.append(c); return len(labels) - 1

for f in ("DORA", "SPACE", "DevEx"):
    an, aa = acad[f]
    gn, ge, gd = lv[f]["mentioned"], lv[f]["empirical"], lv[f]["guidance"]
    gro = gn - ge - gd
    total = an + gn
    n0 = node(f"{f} ({total})<br>proposed in a practitioner venue", COL[f])
    n1 = node(f"cited, academic ({an})", COL[f])
    n2 = node(f"cited, gray ({gn})", COL[f])
    a1 = node(f"used to measure ({aa})", COL[f])
    a2 = node(f"cited only ({an - aa})", "rgba(150,150,150,0.85)")
    g1 = node(f"used to measure ({ge})", COL[f])
    g2 = node(f"guidance or commentary ({gd})", "rgba(190,155,60,0.9)")
    g3 = node(f"cited only ({gro})", "rgba(150,150,150,0.85)")
    src += [n0, n0, n1, n1, n2, n2, n2]
    tgt += [n1, n2, a1, a2, g1, g2, g3]
    val += [an, gn, aa, an - aa, ge, gd, gro]
    lcol += [L[f], L[f], L[f], GRY, L[f], AMB, GRY]

fig = go.Figure(go.Sankey(arrangement="snap",
    node=dict(label=labels, color=colors, pad=12, thickness=15,
              line=dict(color="rgba(0,0,0,0.35)", width=0.6)),
    link=dict(source=src, target=tgt, value=val, color=lcol)))
fig.update_layout(font=dict(family="Georgia, serif", size=13, color="#222"),
                  width=1050, height=700, margin=dict(l=10, r=10, t=10, b=10))
out = os.path.join(ROOT, "latex-article", "figures", "fig_framework_flow")
fig.write_image(out + ".png", scale=2)
fig.write_image(out + ".pdf")
print("written:", out)
