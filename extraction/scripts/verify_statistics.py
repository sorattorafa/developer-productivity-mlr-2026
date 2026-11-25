#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_statistics.py — Recompute every number reported in the article directly
from the consolidated master spreadsheet, so the results are fully auditable.

Reproduces: corpus counts, framework application (academic vs grey), Fisher exact
and chi-square tests, metric-category frequencies, temporal distribution,
human-subject sample sizes, quality-score means/SD, measurement-challenge counts,
and the vendor / non-vendor sensitivity split.

Usage:
    python3 verify_statistics.py [--master PATH] [--vendors PATH] [--json OUT]

Inputs:
    data/master/MLR_Final_Consolidated.xlsx   (the master; human-coded "(H)" columns)
    data/master/grey_vendor_classification.csv (id,vendor  -> 1 vendor / 0 independent)

Dependencies: openpyxl, scipy, numpy  (see requirements.txt)
"""
import argparse, csv, json, os, re, statistics, sys
from collections import Counter

try:
    import openpyxl
except ImportError:
    sys.exit("Missing dependency: pip install openpyxl")
try:
    from scipy.stats import fisher_exact, chi2_contingency
except ImportError:
    sys.exit("Missing dependency: pip install scipy numpy")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))  # repo root from extraction/scripts/

def yes(v):
    return str(v).strip().lower() in ("yes", "y", "sim", "true", "1")

def year(v):
    try:
        return int(str(v)[:4])
    except Exception:
        return 0

def period(y):
    return "2016-2019" if y <= 2019 else "2020-2022" if y <= 2022 else "2023-2026"

def num(v):
    if v is None:
        return None
    m = re.search(r"(\d[\d.,]*)", str(v))
    return int(m.group(1).replace(".", "").replace(",", "")) if m else None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", default=os.path.join(ROOT, "data", "master", "MLR_Final_Consolidated.xlsx"))
    ap.add_argument("--vendors", default=os.path.join(ROOT, "data", "master", "grey_vendor_classification.csv"))
    ap.add_argument("--json", default=os.path.join(ROOT, "data", "master", "mlr_stats.json"))
    args = ap.parse_args()

    wb = openpyxl.load_workbook(args.master, data_only=True)
    ip, gl = wb["Included Papers"], wb["Grey Literature"]

    # --- included rows (human verdict) ---
    acad = [r for r in range(2, ip.max_row + 1) if str(ip.cell(r, 31).value).strip().lower() == "include"]
    grey = [r for r in range(2, gl.max_row + 1) if str(gl.cell(r, 20).value).strip().lower() == "include"]
    out = {"_metadata": {"source": os.path.basename(args.master),
                         "note": "Recomputed from the human-coded (H) columns of the master."}}

    # --- corpus counts ---
    out["corpus"] = {"academic_included": len(acad), "grey_included": len(grey),
                     "total": len(acad) + len(grey)}

    # --- framework application (H): academic DORA col36 SPACE col37 DevEx col45 ; grey 23/24/32 ---
    def count(rows, co, c):
        return sum(1 for r in rows if yes(co.cell(r, c).value))
    na = len(acad); ng = len(grey)
    fa = {"DORA": count(acad, ip, 36), "SPACE": count(acad, ip, 37), "DevEx": count(acad, ip, 45)}
    fg = {"DORA": count(grey, gl, 23), "SPACE": count(grey, gl, 24), "DevEx": count(grey, gl, 32)}
    out["framework_application"] = {
        "academic": {k: {"n": v, "pct": round(100 * v / na, 1)} for k, v in fa.items()},
        "grey": {k: {"n": v, "pct": round(100 * v / ng, 1)} for k, v in fg.items()},
    }
    any_a = sum(1 for r in acad if any(yes(ip.cell(r, c).value) for c in (36, 37, 45)))
    any_g = sum(1 for r in grey if any(yes(gl.cell(r, c).value) for c in (23, 24, 32)))
    out["framework_application"]["any_academic"] = {"n": any_a, "pct": round(100 * any_a / na, 1)}
    out["framework_application"]["any_grey"] = {"n": any_g, "pct": round(100 * any_g / ng, 1)}

    # --- framework "named" (col15 free-text "Frameworks Mentioned") vs applied ---
    def named(rows, co, fw):
        n = 0
        for r in rows:
            t = str(co.cell(r, 15).value or "").lower()
            if fw == "DORA" and "dora" in t:
                n += 1
            elif fw == "SPACE" and re.search(r"\bspace\b", t):
                n += 1
            elif fw == "DevEx" and ("devex" in t or "dev-x" in t or "developer experience" in t):
                n += 1
        return n
    out["framework_named_vs_applied"] = {
        "_note": "named = framework appears in the free-text 'Frameworks Mentioned' field (col 15); "
                 "applied = operationalized as the measurement instrument (human-coded).",
        "academic": {fw: {"named": named(acad, ip, fw), "applied": fa[fw]} for fw in ("DORA", "SPACE", "DevEx")},
        "grey": {fw: {"named": named(grey, gl, fw), "applied": fg[fw]} for fw in ("DORA", "SPACE", "DevEx")},
    }

    # --- statistical tests ---
    # DORA: academic (yes/no) vs grey (yes/no)
    dora = [[fa["DORA"], na - fa["DORA"]], [fg["DORA"], ng - fg["DORA"]]]
    _, p_dora = fisher_exact(dora)
    # any framework: academic vs grey
    anyf = [[any_a, na - any_a], [any_g, ng - any_g]]
    chi2, p_any, _, _ = chi2_contingency(anyf)
    out["tests"] = {
        "DORA_academic_vs_grey": {"table": dora, "fisher_p": p_dora},
        "any_framework_academic_vs_grey": {"table": anyf, "chi2": round(chi2, 1), "p": p_any},
    }

    # --- metric categories over all 124 (academic 39-47 + remote 51 ; grey 26-34 mapped) ---
    cats_ac = {"Productivity/performance": 39, "Quality": 40, "Collaboration": 41,
               "Satisfaction/well-being": 42, "Activity/code": 43, "Delivery performance": 44,
               "DevEx dimensions": 45, "Agile/process": 46, "Survey/perceptual": 47,
               "Remote/COVID": 51}
    cats_gl = {"Productivity/performance": 26, "Quality": 27, "Collaboration": 28,
               "Satisfaction/well-being": 29, "Activity/code": 30, "Delivery performance": 31,
               "DevEx dimensions": 32, "Agile/process": 33, "Survey/perceptual": 34,
               "Remote/COVID": 38}
    metric = {}
    for name in cats_ac:
        c = count(acad, ip, cats_ac[name]) + count(grey, gl, cats_gl[name])
        metric[name] = {"n": c, "pct": round(100 * c / (na + ng), 1)}
    out["metric_categories_all"] = dict(sorted(metric.items(), key=lambda x: -x[1]["n"]))
    ncats = [sum(1 for c in list(cats_ac.values())[:9] if yes(ip.cell(r, c).value)) for r in acad]
    out["metric_categories_per_academic_source"] = {"mean_of_9": round(statistics.mean(ncats), 1),
                                                     "distribution": dict(sorted(Counter(ncats).items()))}

    # --- temporal distribution ---
    pa = Counter(period(year(ip.cell(r, 4).value)) for r in acad)
    pg = Counter(period(year(gl.cell(r, 5).value)) for r in grey)
    out["temporal"] = {"academic": {p: pa.get(p, 0) for p in ("2016-2019", "2020-2022", "2023-2026")},
                       "grey": {p: pg.get(p, 0) for p in ("2016-2019", "2020-2022", "2023-2026")}}
    # framework application by period (academic)
    fw_per = {}
    for fwname, c in (("DORA", 36), ("SPACE", 37), ("DevEx", 45)):
        fw_per[fwname] = {p: sum(1 for r in acad if yes(ip.cell(r, c).value) and period(year(ip.cell(r, 4).value)) == p)
                          for p in ("2016-2019", "2020-2022", "2023-2026")}
    out["framework_by_period_academic"] = fw_per

    # --- human-subject sample sizes ---
    human = []
    for r in acad:
        meth = str(ip.cell(r, 34).value).lower(); n = num(ip.cell(r, 13).value)
        if n is None:
            continue
        if any(w in meth for w in ("survey", "interview", "experiment", "questionnaire",
                                   "focus", "diary", "case study", "mixed")) and "mining" not in meth and n < 20000:
            human.append(n)
    hs = sorted(human)
    out["sample_sizes_human"] = {"n_studies": len(human), "median": hs[len(hs) // 2] if hs else None,
                                 "sum": sum(human),
                                 "bins": dict(Counter("1-30" if n <= 30 else "31-100" if n <= 100 else
                                                      "101-500" if n <= 500 else "501-2000" if n <= 2000 else "2000+"
                                                      for n in human))}

    # --- quality scores ---
    def qstats(rows, co, c):
        vals = [float(str(co.cell(r, c).value).replace(",", "."))
                for r in rows if co.cell(r, c).value is not None
                and re.match(r"^[0-9.,]+$", str(co.cell(r, c).value))]
        return {"n": len(vals), "mean": round(statistics.mean(vals), 2),
                "sd": round(statistics.pstdev(vals), 2) if len(vals) > 1 else 0.0}
    out["quality"] = {"academic_dyba_1_5": qstats(acad, ip, 54), "grey_aacods_1_6": qstats(grey, gl, 41)}

    # --- vendor / non-vendor sensitivity (grey) ---
    if os.path.exists(args.vendors):
        vmap = {}
        with open(args.vendors, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                vmap[row["id"].strip()] = row["vendor"].strip() in ("1", "yes", "true")
        vend = [r for r in grey if vmap.get(str(gl.cell(r, 1).value).strip(), False)]
        indep = [r for r in grey if not vmap.get(str(gl.cell(r, 1).value).strip(), False)]
        out["vendor_sensitivity"] = {"n_vendor": len(vend), "n_independent": len(indep)}
        for fwname, c in (("DORA", 23), ("SPACE", 24), ("DevEx", 32)):
            out["vendor_sensitivity"][fwname] = {
                "vendor_pct": round(100 * count(vend, gl, c) / len(vend), 1) if vend else None,
                "independent_pct": round(100 * count(indep, gl, c) / len(indep), 1) if indep else None}
    else:
        out["vendor_sensitivity"] = {"note": f"classification file not found: {args.vendors}"}

    # --- write + print ---

    # --- grey engagement levels (Mentioned (H) + Applied Level (H)) ---
    name2col = {str(gl.cell(1, c).value): c for c in range(1, gl.max_column + 1)}
    lv = {f: name2col.get(f + " Applied Level (H)") for f in ("DORA", "SPACE", "DevEx")}
    mn = {f: name2col.get(f + " Mentioned (H)") for f in ("DORA", "SPACE", "DevEx")}
    if all(lv.values()) and all(mn.values()):
        levels = {f: {"empirical": 0, "guidance": 0, "referenced_only": 0, "mentioned": 0} for f in lv}
        any_emp, any_men = set(), set()
        for r in grey:
            gid = str(gl.cell(r, 1).value).strip()
            for f in lv:
                m = yes(gl.cell(r, mn[f]).value)
                l = str(gl.cell(r, lv[f]).value or "").strip()
                if m:
                    levels[f]["mentioned"] += 1
                    any_men.add(gid)
                if l == "empirical":
                    levels[f]["empirical"] += 1
                    any_emp.add(gid)
                elif l == "guidance":
                    levels[f]["guidance"] += 1
                elif m:
                    levels[f]["referenced_only"] += 1
        out["grey_engagement_levels"] = levels
        out["grey_any_mentioned"] = {"n": len(any_men), "pct": round(100 * len(any_men) / ng, 1)}
        out["grey_any_empirical"] = {"n": len(any_emp), "pct": round(100 * len(any_emp) / ng, 1)}
        tests_e = {}
        for f in lv:
            ge = levels[f]["empirical"]
            _, pv = fisher_exact([[fa[f], na - fa[f]], [ge, ng - ge]])
            tests_e[f] = {"acad_applied": fa[f], "grey_empirical": ge, "fisher_p": round(pv, 4)}
        chi2e, pve, _, _ = chi2_contingency([[any_a, na - any_a], [len(any_emp), ng - len(any_emp)]])
        tests_e["any_empirical"] = {"acad": any_a, "grey": len(any_emp), "chi2": round(chi2e, 2), "p": round(pve, 3)}
        out["tests_empirical"] = tests_e

    with open(args.json, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    p = out
    print("=" * 64)
    print("MLR — recomputed statistics (from master)")
    print("=" * 64)
    print(f"Corpus: {p['corpus']['academic_included']} academic + {p['corpus']['grey_included']} grey "
          f"= {p['corpus']['total']}")
    fa_ = p["framework_application"]["academic"]; fg_ = p["framework_application"]["grey"]
    print(f"DORA  applied: academic {fa_['DORA']['n']} ({fa_['DORA']['pct']}%)  | grey {fg_['DORA']['n']} ({fg_['DORA']['pct']}%)")
    print(f"SPACE applied: academic {fa_['SPACE']['n']} ({fa_['SPACE']['pct']}%) | grey {fg_['SPACE']['n']} ({fg_['SPACE']['pct']}%)")
    print(f"DevEx applied: academic {fa_['DevEx']['n']} ({fa_['DevEx']['pct']}%) | grey {fg_['DevEx']['n']} ({fg_['DevEx']['pct']}%)")
    nv = p["framework_named_vs_applied"]["academic"]
    print(f"Named/applied (academic): DORA {nv['DORA']['named']}/{nv['DORA']['applied']}  "
          f"SPACE {nv['SPACE']['named']}/{nv['SPACE']['applied']}  DevEx {nv['DevEx']['named']}/{nv['DevEx']['applied']}")
    print(f"Any framework: academic {p['framework_application']['any_academic']['pct']}% | "
          f"grey {p['framework_application']['any_grey']['pct']}%")
    print(f"Fisher (DORA acad vs grey) p = {p['tests']['DORA_academic_vs_grey']['fisher_p']:.2e}")
    print(f"Chi2 (any framework)      = {p['tests']['any_framework_academic_vs_grey']['chi2']}, "
          f"p = {p['tests']['any_framework_academic_vs_grey']['p']:.2e}")
    print(f"Quality academic mean {p['quality']['academic_dyba_1_5']['mean']} "
          f"(SD {p['quality']['academic_dyba_1_5']['sd']}) | grey {p['quality']['grey_aacods_1_6']['mean']} "
          f"(SD {p['quality']['grey_aacods_1_6']['sd']})")
    print(f"Human-subject samples: {p['sample_sizes_human']['n_studies']} studies, "
          f"median {p['sample_sizes_human']['median']}")
    print(f"Temporal academic: {p['temporal']['academic']}")
    if "n_vendor" in p["vendor_sensitivity"]:
        v = p["vendor_sensitivity"]
        print(f"Vendor split: {v['n_vendor']} vendor / {v['n_independent']} independent | "
              f"DORA {v['DORA']['vendor_pct']}% vs {v['DORA']['independent_pct']}%")
    print("=" * 64)
    print(f"JSON written to {args.json}")

if __name__ == "__main__":
    main()
