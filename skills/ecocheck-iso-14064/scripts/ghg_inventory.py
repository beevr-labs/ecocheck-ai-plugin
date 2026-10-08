#!/usr/bin/env python3
"""
GHG inventory calculator (ISO 14064-1 categories + GHG Protocol scopes). Python 3 standard library only.

    python3 ghg_inventory.py activity-data.csv [--gwp AR5|AR6] [--json]

CSV columns (see templates/activity-data.csv):
  site, period, iso_category (1-6), ghg_scope (1-3), source, activity_value, activity_unit,
  factor_co2, factor_ch4, factor_n2o   (kg gas per activity unit, optional)
  factor_other_co2e                    (kg CO2e per activity unit, e.g. refrigerant GWP or a CO2e factor)
  factor_unit, factor_source, biogenic (yes/no: CO2 reported separately), ad_uncertainty_pct, ef_uncertainty_pct, note

Per line: kg CO2e = value x (co2 + ch4 x GWP_CH4 + n2o x GWP_N2O + other_co2e); biogenic lines keep CO2 out
of the totals (reported separately). Uncertainty: line U = sqrt(U_AD^2 + U_EF^2), totals by error propagation.
"""
import argparse
import csv
import json
import math
import sys
from collections import defaultdict

GWP = {"AR5": {"CH4": 28, "N2O": 265}, "AR6": {"CH4": 29.8, "N2O": 273}}
ISO_NAMES = {
    1: "Direct GHG emissions and removals",
    2: "Indirect GHG emissions from imported energy",
    3: "Indirect GHG emissions from transportation",
    4: "Indirect GHG emissions from products used by the organization",
    5: "Indirect GHG emissions associated with the use of products from the organization",
    6: "Indirect GHG emissions from other sources",
}


def num(value):
    value = (value or "").strip().replace(" ", "")
    if not value:
        return 0.0
    if "," in value and "." not in value:
        value = value.replace(",", ".")
    return float(value)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("--gwp", default="AR5", choices=sorted(GWP))
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    g = GWP[args.gwp]

    lines = []
    with open(args.csv, newline="", encoding="utf-8-sig") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            try:
                value = num(row.get("activity_value"))
                co2 = value * num(row.get("factor_co2"))
                ch4 = value * num(row.get("factor_ch4"))
                n2o = value * num(row.get("factor_n2o"))
                other = value * num(row.get("factor_other_co2e"))
            except ValueError as e:
                sys.exit(f"line {i}: {e}")
            biogenic = (row.get("biogenic") or "").strip().lower() in ("yes", "y", "true", "1", "co")
            co2e_fossil = (0 if biogenic else co2) + ch4 * g["CH4"] + n2o * g["N2O"] + other
            u = math.sqrt(num(row.get("ad_uncertainty_pct")) ** 2 + num(row.get("ef_uncertainty_pct")) ** 2)
            lines.append({
                "line": i,
                "site": row.get("site", ""),
                "period": row.get("period", ""),
                "iso_category": int(num(row.get("iso_category")) or 0),
                "scope": int(num(row.get("ghg_scope")) or 0),
                "source": row.get("source", ""),
                "t_co2e": co2e_fossil / 1000,
                "t_co2": (0 if biogenic else co2) / 1000,
                "t_ch4": ch4 / 1000,
                "t_n2o": n2o / 1000,
                "t_other_co2e": other / 1000,
                "t_biogenic_co2": (co2 if biogenic else 0) / 1000,
                "u_pct": u,
                "factor_source": row.get("factor_source", ""),
            })

    by_cat = defaultdict(float)
    by_scope = defaultdict(float)
    var_cat = defaultdict(float)
    for x in lines:
        by_cat[x["iso_category"]] += x["t_co2e"]
        by_scope[x["scope"]] += x["t_co2e"]
        var_cat[x["iso_category"]] += (x["t_co2e"] * x["u_pct"] / 100) ** 2
    total = sum(by_cat.values())
    u_total = math.sqrt(sum(var_cat.values())) / total * 100 if total else 0
    result = {
        "gwp": args.gwp,
        "total_t_co2e": round(total, 3),
        "uncertainty_pct_95": round(u_total, 1),
        "by_iso_category": {c: {"name": ISO_NAMES.get(c, "?"), "t_co2e": round(v, 3), "uncertainty_pct": round(math.sqrt(var_cat[c]) / v * 100, 1) if v else 0} for c, v in sorted(by_cat.items())},
        "by_scope": {f"Scope {s}": round(v, 3) for s, v in sorted(by_scope.items())},
        "category_1_by_gas_t": {
            "CO2": round(sum(x["t_co2"] for x in lines if x["iso_category"] == 1), 3),
            "CH4 (t gas)": round(sum(x["t_ch4"] for x in lines if x["iso_category"] == 1), 6),
            "N2O (t gas)": round(sum(x["t_n2o"] for x in lines if x["iso_category"] == 1), 6),
            "Other (t CO2e, e.g. HFCs)": round(sum(x["t_other_co2e"] for x in lines if x["iso_category"] == 1), 3),
        },
        "biogenic_co2_t_reported_separately": round(sum(x["t_biogenic_co2"] for x in lines), 3),
        "lines": lines,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return
    print(f"GHG inventory ({args.gwp}) - total {total:,.2f} tCO2e, uncertainty +/-{u_total:.1f} % (95 %)\n")
    print(f"{'ISO category':<75} {'tCO2e':>14} {'U %':>7}")
    for c, v in result["by_iso_category"].items():
        print(f"{str(c) + ' ' + v['name']:<75} {v['t_co2e']:>14,.2f} {v['uncertainty_pct']:>7.1f}")
    print()
    for s, v in result["by_scope"].items():
        print(f"{s:<75} {v:>14,.2f}")
    print(f"\nCategory 1 by gas: {result['category_1_by_gas_t']}")
    print(f"Biogenic CO2 (reported separately): {result['biogenic_co2_t_reported_separately']:,.3f} t")
    print(f"\n{'Line':>4} {'Cat':>3} {'Source':<40} {'tCO2e':>12}  Factor source")
    for x in lines:
        print(f"{x['line']:>4} {x['iso_category']:>3} {x['source'][:40]:<40} {x['t_co2e']:>12,.3f}  {x['factor_source'][:60]}")


if __name__ == "__main__":
    main()
