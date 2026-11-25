#!/usr/bin/env python3
"""Recount of every corpus-derived number in main.tex for the search update 2026-10.

Reads the master (human-coded (H) columns), the metric inventory, the challenge recoding and the vendor file, and
computes each figure twice: for the original corpus only (Stream = "Original search", to check against the numbers
now in main.tex) and for the integrated corpus (all streams). Writes recount_2026-10.json.

Usage: python3 recount_2026_10.py MASTER INVENTORY_CSV VENDORS_CSV CHALLENGES_DIR OUT_JSON
"""
import csv, json, re, statistics, sys
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter
from pathlib import Path
import openpyxl
from scipy.stats import fisher_exact, chi2_contingency

MASTER, INV, VEND, CHDIR, OUT = sys.argv[1:6]
wb = openpyxl.load_workbook(MASTER, read_only=True, data_only=True)
IP = [r for r in list(wb["Included Papers"].iter_rows(values_only=True))[1:] if str(r[30]).strip() == "Include"]
GL = [r for r in list(wb["Grey Literature"].iter_rows(values_only=True))[1:] if str(r[19]).strip() == "Include"]

yes = lambda v: str(v).strip().lower() in ("yes", "y", "true", "1")
# percentages round half up, as in the article (5/16 = 31.3%); Python's round() rounds half to even
pct = lambda n, d: float((Decimal(100) * n / d).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)) if d else 0.0
hu = lambda n, d: int((Decimal(100) * n / d).quantize(Decimal("1"), rounding=ROUND_HALF_UP)) if d else 0
P3 = ("2016-2019", "2020-2022", "2023-2026")


def period(y):
    y = int(str(y)[:4])
    return P3[0] if y <= 2019 else P3[1] if y <= 2022 else P3[2]


# academic columns (0-based): 0 id, 3 year, 4 venue, 12 sample, 32 study type, 34 context, 35 DORA, 36 SPACE, 37 AI,
# 38..46 nine categories, 50 remote, 53 quality, 54 strength, 55 stream
AC = dict(dora=35, space=36, devex=44, ai=37, remote=50, q=53, strength=54, stream=55, year=3)
CATS_A = {"Productivity/Performance": 38, "Quality": 39, "Collaboration": 40, "Satisfaction/Wellbeing": 41,
          "Activity/Code": 42, "Delivery Performance": 43, "DevEx Dimensions": 44, "Agile/Process": 45,
          "Survey/Perceptual": 46}
# grey columns (0-based): 4 year, 7 tier, 22 DORA, 23 SPACE, 24 AI, 25..33 categories, 37 remote, 40 quality,
# 41..43 mentioned, 44..46 level, 47 stream
GC = dict(dora=22, space=23, devex=31, ai=24, remote=37, q=40, stream=47, year=4)
CATS_G = {k: v - 13 for k, v in CATS_A.items()}
LVL = {"DORA": (41, 44), "SPACE": (42, 45), "DevEx": (43, 46)}
vendor = {r["id"].strip(): r["vendor"].strip() in ("1", "yes", "true") for r in csv.DictReader(open(VEND))}
CH = {p.stem: json.load(open(p)) for p in Path(CHDIR).glob("*.json")}


def ctx_bucket(t):
    s = str(t or "").strip().lower()
    if re.match(r"(oss\b|open[- ]source)", s):
        return "OSS"
    if re.match(r"(mixed|academic/industry|academic/mixed)", s) or ("academic" in s[:30] and "+ industry" in s):
        return "Mixed"
    if re.match(r"academic", s):
        return "Academic/secondary"
    if re.match(r"(not reported|public data|practitioner/industry framework|controlled online lab)", s):
        return "Other/not specified"
    return "Industry"


def venue_type(v):
    s = str(v or "").lower()
    if "workshop" in s and "workshop and conference" not in s:  # CCWC is a conference
        return "Workshop"
    if "thesis" in s:
        return "Thesis"
    # update rows carry abbreviated or truncated venue names (e.g. "ACM Trans. Softw. Eng. Methodol.",
    # "Information and Software ...", "Communications of the ..."); D1 rows: "Queue (ACM)", "<journal> (MDPI)"
    if re.search(r"(journal|jurnal|transactions|trans\. softw|communications of the|ieee software|computing surveys|"
                 r"science china|acmqueue|frontiers in|acm queue|\bqueue \(acm\)|\(mdpi\)|information and software|e-informatica)", s) \
            or s.startswith("empirical software"):
        return "Journal"
    return "Conference"


def method(st):
    b = str(st).split(" (")[0].strip()
    return {"Other": "Conceptual / Other", "Review-Secondary": "Review / Secondary",
            "Qualitative-Interviews": "Qualitative / Interviews", "Experiment": "Controlled Experiment",
            "Quasi-experiment": "Quasi-Experiment", "Repository mining": "Repository Mining",
            "Mixed methods": "Mixed Methods", "Case study": "Case Study"}.get(b, b)


def num(v):
    m = re.search(r"(\d[\d.,]*)", str(v or ""))
    return int(m.group(1).replace(".", "").replace(",", "")) if m else None


def compute(ip, gl):
    na, ng = len(ip), len(gl)
    o = {"n_academic": na, "n_grey": ng, "n_total": na + ng,
         "share_academic": pct(na, na + ng), "share_grey": pct(ng, na + ng)}
    # periods
    pa = Counter(period(r[3]) for r in ip)
    pg = Counter(period(r[4]) for r in gl)
    o["period_academic"] = {p: pa[p] for p in P3}
    o["period_grey"] = {p: pg[p] for p in P3}
    o["post2022_academic_pct"] = pct(pa[P3[2]], na)
    o["post2022_grey_pct"] = pct(pg[P3[2]], ng)
    # tiers
    tier = Counter()
    for r in gl:
        t = str(r[7] or "").lower()
        tier["1st" if "1" in t else "2nd" if "2" in t else "3rd"] += 1
    o["grey_tier"] = dict(tier)
    # framework application academic
    fa = {"DORA": [r for r in ip if yes(r[35])], "SPACE": [r for r in ip if yes(r[36])],
          "DevEx": [r for r in ip if yes(r[44])]}
    o["acad_applied"] = {k: {"n": len(v), "pct": pct(len(v), na)} for k, v in fa.items()}
    o["acad_applied_by_period"] = {k: {p: sum(1 for r in v if period(r[3]) == p) for p in P3} for k, v in fa.items()}
    nfw = [sum(1 for c in (35, 36, 44) if yes(r[c])) for r in ip]
    o["acad_any_framework"] = {"n": sum(1 for x in nfw if x), "pct": pct(sum(1 for x in nfw if x), na),
                               "one": sum(1 for x in nfw if x == 1), "two_plus": sum(1 for x in nfw if x >= 2)}
    nof = [r for r, x in zip(ip, nfw) if x == 0]
    o["acad_no_framework"] = {"n": len(nof),
                              "survey": [sum(1 for r in nof if yes(r[46])), pct(sum(1 for r in nof if yes(r[46])), len(nof))],
                              "satisfaction": [sum(1 for r in nof if yes(r[41])), pct(sum(1 for r in nof if yes(r[41])), len(nof))],
                              "productivity": [sum(1 for r in nof if yes(r[38])), pct(sum(1 for r in nof if yes(r[38])), len(nof))]}
    # AI and remote
    ai_a = [r for r in ip if yes(r[37])]
    o["acad_ai"] = {"n": len(ai_a), "pct": pct(len(ai_a), na),
                    "by_period": {p: sum(1 for r in ai_a if period(r[3]) == p) for p in P3},
                    "post2022_share_of_post2022": pct(sum(1 for r in ai_a if period(r[3]) == P3[2]), pa[P3[2]])}
    ai_g = [r for r in gl if yes(r[24])]
    o["grey_ai"] = {"n": len(ai_g), "pct": pct(len(ai_g), ng)}
    rem = [r for r in ip if yes(r[50])]
    o["acad_remote"] = {"n": len(rem), "by_period": {p: sum(1 for r in rem if period(r[3]) == p) for p in P3},
                        "pct_by_period": {p: pct(sum(1 for r in rem if period(r[3]) == p), pa[p]) for p in P3}}
    # grey engagement
    lv = {}
    for f, (mc, lc) in LVL.items():
        m = sum(1 for r in gl if yes(r[mc]))
        e = sum(1 for r in gl if str(r[lc] or "").strip() == "empirical")
        g = sum(1 for r in gl if str(r[lc] or "").strip() == "guidance")
        lv[f] = {"mentioned": m, "empirical": e, "guidance": g, "referenced_only": m - e - g,
                 "empirical_pct": pct(e, ng), "guidance_pct": pct(g, ng), "ref_only_pct": pct(m - e - g, ng)}
    o["grey_levels"] = lv
    anym = sum(1 for r in gl if any(yes(r[c]) for c in (41, 42, 43)))
    anye = sum(1 for r in gl if any(str(r[c] or "").strip() == "empirical" for c in (44, 45, 46)))
    o["grey_any_mentioned"] = {"n": anym, "pct": pct(anym, ng)}
    o["grey_any_empirical"] = {"n": anye, "pct": pct(anye, ng)}
    tests = {}
    for f in ("DORA", "SPACE", "DevEx"):
        a = len(fa[f]); e = lv[f]["empirical"]
        tests[f] = round(fisher_exact([[a, na - a], [e, ng - e]])[1], 4)
    anya = o["acad_any_framework"]["n"]
    chi2, p, _, _ = chi2_contingency([[anya, na - anya], [anye, ng - anye]])
    tests["any_empirical"] = {"chi2": round(chi2, 2), "p": round(p, 3)}
    o["tests"] = tests
    # categories
    cat = {}
    for k in CATS_A:
        a = sum(1 for r in ip if yes(r[CATS_A[k]])); g = sum(1 for r in gl if yes(r[CATS_G[k]]))
        cat[k] = {"n": a + g, "pct": pct(a + g, na + ng), "acad": a, "acad_pct": pct(a, na), "grey": g, "grey_pct": pct(g, ng)}
    o["categories"] = cat
    rem_all = len(rem) + sum(1 for r in gl if yes(r[37]))
    o["remote_all_pct"] = pct(rem_all, na + ng)
    per_src = [sum(1 for k in CATS_A if yes(r[CATS_A[k]])) for r in ip] + \
              [sum(1 for k in CATS_G if yes(r[CATS_G[k]])) for r in gl]
    o["categories_per_source_mean"] = round(statistics.mean(per_src), 1)
    o["single_category"] = {"n": sum(1 for x in per_src if x == 1), "pct": pct(sum(1 for x in per_src if x == 1), na + ng)}
    # measurement focus by period (academic)
    foc = {}
    for k in ("Satisfaction/Wellbeing", "Activity/Code", "Delivery Performance", "DevEx Dimensions", "Quality", "Collaboration"):
        foc[k] = {p: hu(sum(1 for r in ip if period(r[3]) == p and yes(r[CATS_A[k]])), pa[p]) for p in P3}
    foc["Remote/COVID"] = {p: hu(sum(1 for r in rem if period(r[3]) == p), pa[p]) for p in P3}
    o["focus_by_period_pct"] = foc
    # study characterization
    o["venue_type"] = dict(Counter(venue_type(r[4]) for r in ip))
    o["methods"] = dict(Counter(method(r[32]) for r in ip).most_common())
    o["strength"] = dict(Counter(str(r[54]).split(" (")[0] if not str(r[54]).startswith("substantiated (secondary")
                                 else "substantiated (secondary synthesis)" for r in ip if r[54]))
    kw = ("survey", "interview", "experiment", "questionnaire", "focus", "diary", "case study", "mixed")
    hs = sorted(n for r in ip for n in [num(r[12])] if n is not None and any(w in str(r[33]).lower() for w in kw)
                and "mining" not in str(r[33]).lower() and n < 20000)
    o["human_samples"] = {"n": len(hs), "median": statistics.median(hs) if hs else None,
                          "below30": sum(1 for n in hs if n < 30)}
    o["context"] = dict(Counter(ctx_bucket(r[34]) for r in ip).most_common())
    # quality
    qa = [float(str(r[53]).replace(",", ".")) for r in ip if re.match(r"^[0-9.,]+$", str(r[53]))]
    qg = [float(str(r[40]).replace(",", ".")) for r in gl if re.match(r"^[0-9.,]+$", str(r[40]))]
    o["quality"] = {"acad_mean": round(statistics.mean(qa), 2), "acad_sd": round(statistics.pstdev(qa), 2),
                    "grey_mean": round(statistics.mean(qg), 2), "grey_sd": round(statistics.pstdev(qg), 2)}
    # vendor split (empirical level)
    vend = [r for r in gl if vendor.get(r[0], False)]; ind = [r for r in gl if not vendor.get(r[0], False)]
    vs = {"n_vendor": len(vend), "n_independent": len(ind)}
    for f, (mc, lc) in LVL.items():
        ve = sum(1 for r in vend if str(r[lc] or "").strip() == "empirical")
        ie = sum(1 for r in ind if str(r[lc] or "").strip() == "empirical")
        vs[f] = {"vendor_pct": pct(ve, len(vend)), "independent_pct": pct(ie, len(ind))}
    o["vendor_empirical"] = vs
    # challenges (recoded)
    ch = [r for r in ip if r[0] in CH]
    y = [r for r in ch if CH[r[0]]["reports"] == "Yes"]
    o["challenges"] = {"coded": len(ch), "n": len(y), "pct": pct(len(y), len(ch)),
                       "by_period": {p: [sum(1 for r in y if period(r[3]) == p), pa[p],
                                         pct(sum(1 for r in y if period(r[3]) == p), pa[p])] for p in P3},
                       "themes": dict(Counter(t for r in y for t in CH[r[0]]["themes"]).most_common())}
    return o


def inventory(ids):
    rows = [r for r in list(csv.reader(open(INV)))[1:]]
    out = {}
    canon = [r for r in rows if not r[0].startswith("OTHER")]
    def n(r):
        s = [x for x in r[5].split(";") if x in ids]
        return len(s), sum(1 for x in s if x.startswith("P")), sum(1 for x in s if x.startswith("G"))
    cov = {x for r in rows for x in r[5].split(";") if x in ids}
    out["canonical_9cat"] = sum(1 for r in canon if n(r)[0] > 0)
    out["sources_covered"] = len(cov)
    top = sorted(((r[1], r[0]) + n(r) for r in canon), key=lambda t: -t[2])[:15]
    out["top15"] = top
    byname = {r[1]: n(r) for r in rows}
    for k in ("change failure rate", "mean time to restore", "perceived productivity (self-report)",
              "affect / sentiment", "AI suggestion acceptance / persistence", "deployment frequency",
              "lead time for changes", "satisfaction", "productivity / efficiency score", "flow state / focus time"):
        out[k] = byname.get(k)
    return out


orig_ip = [r for r in IP if r[55] == "Original search"]
orig_gl = [r for r in GL if r[47] == "Original search"]
res = {"original": compute(orig_ip, orig_gl), "integrated": compute(IP, GL)}
res["original"]["inventory"] = inventory({r[0] for r in orig_ip} | {r[0] for r in orig_gl})
res["integrated"]["inventory"] = inventory({r[0] for r in IP} | {r[0] for r in GL})
json.dump(res, open(OUT, "w"), indent=1, ensure_ascii=False, default=str)
print("written", OUT)
