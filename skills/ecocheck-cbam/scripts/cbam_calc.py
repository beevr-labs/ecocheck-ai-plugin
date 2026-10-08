#!/usr/bin/env python3
"""
EU CBAM offline calculator (EcoCheck skill). Python 3 standard library only.

  python3 cbam_calc.py scope   <cn_code>
  python3 cbam_calc.py default <cn_code> [--country VN] [--year 2026] [--variant GREY|WHITE]
  python3 cbam_calc.py cost    <cn_code> --tonnes 12000 [--country VN] [--year 2026] [--actual-see 1.9] [--price 82.32]
  python3 cbam_calc.py see     <input.json>

Data: ../references/default-values-vn.csv (Implementing Regulation (EU) 2025/2621 as corrected by 2026/1740;
VN, ZZ = other countries, XX = Annex IV) and ../references/benchmarks.csv (2025/2620 Annex, columns A/B).
Same rules as the EcoCheck MCP tools (https://ecocheck.ai/mcp). Indicative only — not a CBAM declaration.

`see` input.json example:
{
  "good": {"cn_code": "72083900", "activity_level_t": 12000, "category_direct_only": true},
  "source_streams": [{"name": "LPG furnace", "method": "combustion", "quantity": 1150, "ncv_tj_per_unit": 0.0473, "ef_t_per_tj": 63.1, "oxidation": 1}],
  "electricity_mwh": 9800, "grid_ef": 0.581,
  "precursors": [{"cn_code": "72071114", "tonnes": 12400, "country": "VN", "see_direct": null, "verified": false}],
  "year": 2026
}
"""
import argparse
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "references")
CBAM_FACTOR = {2026: 0.975, 2027: 0.95, 2028: 0.9, 2029: 0.775, 2030: 0.515, 2031: 0.39, 2032: 0.265, 2033: 0.14}
LATEST_PRICE = (82.32, "2026-Q3 (published 2026-10-05)")
EU_EEA_CH = set("AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE IS LI NO CH".split())


def rng(a, b):
    return [str(i) for i in range(a, b + 1)]


CATEGORIES = [
    ("CALCINED_CLAY", "Calcined clay", ["25070080"], [], False),
    ("CEMENT_CLINKER", "Cement clinker", ["25231000"], [], False),
    ("CEMENT", "Cement", ["25232100", "25232900", "25239000"], [], False),
    ("ALUMINOUS_CEMENT", "Aluminous cement", ["25233000"], [], False),
    ("NITRIC_ACID", "Nitric acid", ["28080000"], [], False),
    ("AMMONIA", "Ammonia", ["2814"], [], False),
    ("UREA", "Urea", ["310210"], [], False),
    ("MIXED_FERTILISERS", "Mixed fertilisers", ["28342100", "3102", "3105"], ["310210", "31056000"], False),
    ("HYDROGEN", "Hydrogen", ["28041000"], [], True),
    ("SINTERED_ORE", "Sintered ore", ["26011200"], [], False),
    ("PIG_IRON", "Pig iron", ["7201"], [], True),
    ("FERRO_MANGANESE", "Ferro-manganese", ["720211", "720219"], [], True),
    ("FERRO_CHROMIUM", "Ferro-chromium", ["720241", "720249"], [], True),
    ("FERRO_NICKEL", "Ferro-nickel", ["720260"], [], True),
    ("DRI", "Direct reduced iron", ["7203"], [], True),
    ("CRUDE_STEEL", "Crude steel", ["7206", "7207", "7218", "7224"], [], True),
    ("IRON_STEEL_PRODUCTS", "Iron or steel products", ["7205"] + rng(7208, 7217) + rng(7219, 7223) + rng(7225, 7229) + rng(7301, 7311) + ["7318", "7326"], [], True),
    ("UNWROUGHT_ALUMINIUM", "Unwrought aluminium", ["7601"], [], True),
    ("ALUMINIUM_PRODUCTS", "Aluminium products", rng(7603, 7614) + ["7616"], [], True),
]
FERTILISERS = {"NITRIC_ACID", "AMMONIA", "UREA", "MIXED_FERTILISERS"}


def norm(cn):
    return str(cn or "").replace(" ", "").replace(".", "")


def category(cn):
    cn = norm(cn)
    if len(cn) != 8 or not cn.isdigit():
        return None
    best = None
    for code, name, prefixes, excl, direct_only in CATEGORIES:
        if any(cn.startswith(e) for e in excl):
            continue
        for p in prefixes:
            if cn.startswith(p) and (best is None or len(p) > best[0]):
                best = (len(p), {"code": code, "name": name, "direct_only": direct_only})
    return best[1] if best else None


def fnum(v):
    return None if v in (None, "") else float(v)


def load_defaults():
    rows = {}
    with open(os.path.join(REF, "default-values-vn.csv"), newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.setdefault(r["country"], []).append({**r, "see_direct": fnum(r["see_direct"]), "see_indirect": fnum(r["see_indirect"]), "see_total": float(r["see_total"])})
    return rows


def load_benchmarks():
    out = {}
    with open(os.path.join(REF, "benchmarks.csv"), newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out.setdefault(r["cn_code"], []).append((r["route"] or None, fnum(r["bmg_column_a"]), fnum(r["bmg_column_b"])))
    return out


DEFAULTS = load_defaults()
BENCH = load_benchmarks()


def find_in(country, cn, variant=""):
    rows = [r for r in DEFAULTS.get(country, []) if cn.startswith(r["cn_code"])]
    if not rows:
        return None
    longest = max(len(r["cn_code"]) for r in rows)
    best = [r for r in rows if len(r["cn_code"]) == longest]
    for want in ((variant or "").upper(), "GREY", ""):
        for r in best:
            if r["variant"] == want:
                return r
    return best[0]


def lookup_default(cn, country="VN", variant=""):
    cn, c = norm(cn), (country or "").upper()
    if not c or c == "XX":
        return find_in("XX", cn, variant)
    return find_in(c, cn, variant) or find_in("ZZ", cn, variant)


def candidates(cn, country="VN"):
    cn, c = norm(cn), (country or "").upper()
    pools = [c, "ZZ"] if c and c != "XX" else ["XX"]
    for n in (6, 4):
        p = cn[:n]
        out = [r for pool in pools for r in DEFAULTS.get(pool, []) if r["cn_code"].startswith(p) or p.startswith(r["cn_code"])]
        if out:
            seen, uniq = set(), []
            for r in out:
                if r["cn_code"] + r["variant"] not in seen:
                    seen.add(r["cn_code"] + r["variant"])
                    uniq.append(r)
            return uniq[:15]
    return []


def markup(year, cat):
    if cat and cat["code"] in FERTILISERS:
        return 0.01
    return 0.1 if year <= 2026 else 0.2 if year == 2027 else 0.3


def see_of_row(row, cat):
    if cat and cat["direct_only"] and row["see_direct"] is not None:
        return row["see_direct"]
    return row["see_total"]


def default_value(cn, country="VN", year=2026, variant=""):
    cat = category(cn)
    row = lookup_default(cn, country, variant)
    if not row:
        return {"cn_code": norm(cn), "category": cat, "value": None, "candidates": [{k: r[k] for k in ("country", "cn_code", "variant", "see_total", "description")} for r in candidates(cn, country)] if cat else []}
    m = markup(year, cat)
    return {"cn_code": norm(cn), "category": cat, "row": row, "markup": m, "see_used": see_of_row(row, cat), "see_with_markup": round(see_of_row(row, cat) * (1 + m), 5)}


def benchmark(cn, route, year):
    rows = [r for r in BENCH.get(norm(cn), []) if r[2] is not None]
    if any(r[0] in ("1", "2") for r in rows):
        rows = [r for r in rows if r[0] == ("1" if year <= 2027 else "2")]
    else:
        wanted = [x.strip() for x in str(route or "").split("/") if x.strip()]
        matching = [r for r in rows if r[0] in wanted]
        rows = matching or rows
    return max(rows, key=lambda r: r[2]) if rows else None


def cost(cn, tonnes, country="VN", year=2026, actual_see=None, price=None, variant=""):
    cat = category(cn)
    if not cat:
        return {"cn_code": norm(cn), "in_scope": False}
    dv = default_value(cn, country, year, variant)
    if dv.get("value", 0) is None and actual_see is None:
        return dv
    see = actual_see if actual_see is not None else dv["see_with_markup"]
    bm = benchmark(cn, dv.get("row", {}).get("route"), year)
    sefa = bm[2] * CBAM_FACTOR.get(year, 0 if year > 2033 else 1) * 1.0 if bm else 0.0
    p = price or LATEST_PRICE[0]
    certs = max(0.0, see - sefa) * tonnes
    return {
        "cn_code": norm(cn), "category": cat["name"], "tonnes": tonnes, "year": year,
        "basis": "actual SEE" if actual_see is not None else f"default {see_of_row(dv['row'], cat)} + {int(dv['markup'] * 100)} % mark-up",
        "see_used": see, "embedded_t": round(see * tonnes, 2),
        "benchmark": {"route": bm[0], "bmg_column_b": bm[2]} if bm else None,
        "sefa": round(sefa, 5), "faa_t": round(sefa * tonnes, 2),
        "certificates": round(certs, 2), "price_eur": p, "price_basis": "given" if price else LATEST_PRICE[1],
        "cost_eur": round(certs * p), "cost_per_tonne_eur": round(certs * p / tonnes, 2),
    }


def see(inp):
    year = int(inp.get("year", 2026))
    good = inp["good"]
    al = float(good["activity_level_t"])
    direct = 0.0
    for s in inp.get("source_streams", []):
        m = s.get("method", "combustion")
        if m == "combustion":
            e = s["quantity"] * s["ncv_tj_per_unit"] * s["ef_t_per_tj"] * s.get("oxidation", 1) * (1 - s.get("biomass_fraction", 0))
        elif m == "process":
            e = s["quantity"] * s["ef_t_per_t"] * s.get("conversion", 1)
        elif m == "mass_balance":
            e = 3.664 * s["quantity"] * s["carbon_content"] * (-1 if s.get("direction") == "OUT" else 1)
        else:
            e = s["tonnes_co2e"]
        s["emissions_t"] = round(e, 3)
        direct += e
    indirect = float(inp.get("electricity_mwh", 0)) * float(inp.get("grid_ef", 0.581))
    pre_dir, pre_ind, used_default = 0.0, 0.0, 0.0
    for p in inp.get("precursors", []):
        c = (p.get("country") or "").upper()
        if c in EU_EEA_CH:
            p["see_used"] = 0.0
        elif p.get("verified") and p.get("see_direct") is not None:
            p["see_used"] = float(p["see_direct"])
            pre_ind += float(p.get("see_indirect_carried") or 0) * p["tonnes"]
        else:
            dv = default_value(p["cn_code"], c or "XX", year)
            if dv.get("value", 0) is None:
                sys.exit(f"precursor {p['cn_code']}: no default value; candidates: {[x['cn_code'] for x in dv['candidates']]}")
            p["see_used"] = dv["see_with_markup"]
            used_default += p["see_used"] * p["tonnes"]
        pre_dir += p["see_used"] * p["tonnes"]
    see_dir = (direct + pre_dir) / al
    see_ind = (indirect + pre_ind) / al
    total = see_dir if good.get("category_direct_only", True) else see_dir + see_ind
    ee = total * al
    dv = default_value(good["cn_code"], "VN", year)
    return {
        "direct_installation_t": round(direct, 2), "indirect_installation_t": round(indirect, 2),
        "precursors_t": round(pre_dir, 2), "see_direct": round(see_dir, 5), "see_indirect": round(see_ind, 5),
        "see_total": round(total, 5), "indirect_counted": not good.get("category_direct_only", True),
        "default_value_share": round(used_default / ee, 3) if ee else None,
        "default_for_comparison": dv.get("see_with_markup"),
        "source_streams": inp.get("source_streams", []), "precursors": inp.get("precursors", []),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("scope", "default", "cost"):
        s = sub.add_parser(name)
        s.add_argument("cn_code")
        s.add_argument("--country", default="VN")
        s.add_argument("--year", type=int, default=2026)
        s.add_argument("--variant", default="")
        if name == "cost":
            s.add_argument("--tonnes", type=float, required=True)
            s.add_argument("--actual-see", type=float)
            s.add_argument("--price", type=float)
    s = sub.add_parser("see")
    s.add_argument("input")
    a = ap.parse_args()
    if a.cmd == "scope":
        cat = category(a.cn_code)
        out = {"cn_code": norm(a.cn_code), "in_scope": bool(cat) and a.country.upper() not in EU_EEA_CH, "category": cat}
        if cat:
            out["default_value"] = default_value(a.cn_code, a.country, a.year, a.variant)
    elif a.cmd == "default":
        out = default_value(a.cn_code, a.country, a.year, a.variant)
    elif a.cmd == "cost":
        out = cost(a.cn_code, a.tonnes, a.country, a.year, a.actual_see, a.price, a.variant)
    else:
        with open(a.input, encoding="utf-8") as f:
            out = see(json.load(f))
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
