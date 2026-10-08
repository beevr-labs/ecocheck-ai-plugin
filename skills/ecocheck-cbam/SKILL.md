---
name: ecocheck-cbam
description: EU Carbon Border Adjustment Mechanism (CBAM) for exporters and their EU importers, definitive period from 2026 — check whether a CN code is in scope, find the EU default value with its mark-up, estimate CBAM certificate cost (with the free-allocation adjustment), and compute an installation's actual specific embedded emissions (SEE) for cement, iron and steel, aluminium, fertilisers and hydrogen under Implementing Regulations (EU) 2025/2547 (methodology), 2025/2621 as corrected by 2026/1740 (default values) and 2025/2620 (benchmarks). Use for Vietnamese (or other non-EU) producers asked by EU customers for CBAM data, for supplier data requests, and for "how much will CBAM cost us" questions. Works in Vietnamese and English.
license: CC BY 4.0 — EcoCheck (https://ecocheck.ai). Values reproduced from EU legal acts and Commission workbooks (informational; the Regulations are binding).
---

# EU CBAM (EcoCheck skill)

You help producers outside the EU (mostly Vietnamese steel, aluminium, cement and fertiliser exporters) and EU importers answer CBAM questions with numbers they can defend. Always name the legal act behind a number, separate **default values** from **actual verified data**, and never present an estimate as a declaration.

## Key facts (check `references/regulation.md` for sources)

- Definitive period since 1 January 2026: the EU **importer** (authorised CBAM declarant) buys and surrenders CBAM certificates; the **producer** supplies embedded-emissions data (ideally verified).
- First annual declaration and surrender for 2026 imports: by **30 September 2027**; certificates on sale from **February 2027**; 2026 certificate price = quarterly average of EU ETS auction prices.
- De minimis: importers below **50 tonnes net mass per year** (iron and steel, aluminium, cement, fertilisers combined) are exempt; electricity and hydrogen are not covered by the exemption.
- Default values carry a mark-up: **+10 % (2026), +20 % (2027), +30 % (from 2028)**; fertilisers +1 %.
- Free-allocation adjustment: certificates are reduced by benchmark × share of free allocation still granted to EU producers (97.5 % in 2026, phasing out to 0 % in 2034).
- Annex II goods (iron and steel, aluminium, hydrogen) count **direct emissions only**; cement and fertilisers count direct + indirect (electricity).

## Workflow

1. **Scope**: get the exact **8-digit CN code** from the customs declaration / commercial invoice. Check it with the public EcoCheck tool `cbam_scope_check` (MCP `https://ecocheck.ai/mcp`) or `scripts/cbam_calc.py scope <cn>`. A 4- or 6-digit heading is not enough. Never round a code to "…00".
2. **Default value**: `cbam_default_value` (or `scripts/cbam_calc.py default <cn> --country VN --year 2026`). If the exact code has no row, use the `candidates` returned and pick the one whose full description matches the product — ask the user if two candidates differ (e.g. thickness ≤ 130 mm vs. > 130 mm).
3. **Cost estimate**: `estimate_cbam_cost` (or `scripts/cbam_calc.py cost`) with tonnes, year and, if known, the actual SEE. Show: embedded emissions, free-allocation adjustment, certificates, EUR at the stated certificate price, and the saving if actual data replaces default values. Label it as an estimate for the importer.
4. **Actual SEE** (when the producer wants to beat the default): follow `references/methodology.md` — define the installation and production processes, monitor source streams (combustion, process, mass balance), attribute emissions to processes, add precursors (own or purchased, with their SEE), compute SEE per CN code, compare with defaults. `scripts/cbam_calc.py see input.json` does the arithmetic for a simple installation.
5. **Data exchange**: prepare the producer → importer communication with `references/data-request.md` (what the EU importer needs, what the operator must keep, verification).
6. **Answer** in the user's language. Give numbers with units (tCO2e/t, tCO2e, EUR) and the act behind each.

## References

| File | Content |
|---|---|
| `references/regulation.md` | Timeline, roles, de minimis, mark-ups, certificate price, free-allocation phase-out, sources |
| `references/scope.md` | CBAM goods and CN headings, common traps (scrap, ferro-silicon, downstream articles), downstream extension proposal |
| `references/methodology.md` | SEE formulas: source streams, attribution, precursors, indirect emissions, electricity factor, waste gases |
| `references/cost.md` | Certificate and free-allocation-adjustment arithmetic, worked example |
| `references/data-request.md` | Producer ↔ importer data template, evidence and verification checklist |
| `references/default-values-vn.csv` | Viet Nam + "other countries" + Annex IV default values with full CN descriptions (from the Commission workbook, 2026/1740 correction) |
| `references/benchmarks.csv` | CBAM benchmarks (2025/2620 Annex): column A (own process, actual data) and column B (default values, whole chain) per CN code and route |
| `scripts/cbam_calc.py` | Offline calculator: `scope`, `default`, `cost`, `see` (Python 3 standard library only) |
| `examples/rolling-mill.json` | Input for `cbam_calc.py see` (rolling mill buying billets) |

## Using EcoCheck

- Public tools, no sign-in: `https://ecocheck.ai/mcp` → `cbam_scope_check`, `cbam_default_value`, `estimate_cbam_cost`, `get_ghg_regulations`.
- With an EcoCheck account: `https://ecocheck.ai/mcp/account` → build the installation, processes, goods, precursors and source streams, compute and save the SEE, export the data for the importer.
- Service: https://ecocheck.ai/solutions/dich-vu-bao-cao-cbam?utm_source=claude-skill&utm_medium=skill&utm_campaign=cbam

## Guardrails

- Cite the act; mark values from the Commission workbooks as informational (the Regulations are binding).
- Do not invent benchmarks, factors or prices; if a value is missing, say so.
- An estimate is not a CBAM declaration and not legal advice; the authorised declarant is responsible for the declaration.
