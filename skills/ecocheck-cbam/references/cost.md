# CBAM cost arithmetic (indicative, for the EU importer)

1. Embedded emissions EE = mass (t) × SEE (tCO2e/t)
   - SEE = verified actual value from the producer, or the default value (Annex I of 2025/2621 corrected by 2026/1740, country of production; "other countries" row when the country has none; Annex IV when unknown) × (1 + mark-up of the year).
   - Annex II goods (iron and steel, aluminium, hydrogen): direct emissions only.
2. Free-allocation adjustment FAA = mass × SEFA
   - Default values declared: SEFA = BMg (column B "default CBAM benchmark", same production route as the default value; highest if several apply) × CBAM factor of the year × CSCF (1.0 for 2026-2030).
   - Actual data declared: SEFA uses column A (the good's own process) and adds the precursors' SEFA separately — needs the producer's route and precursor data; estimate it with column B if unknown and say so.
3. Certificates = EE − FAA − carbon price effectively paid (converted to tCO2e); never below zero.
4. Cost = certificates × certificate price (2026: quarterly average of EU ETS auctions; latest Q3 2026 = €82.32).

## Worked example — hot-rolled coil, Viet Nam, 2026

CN 7208 39 00, 12,000 t, default value VN 2.35 (route C) → with mark-up 2.585 tCO2e/t.
- EE = 12,000 × 2.585 = 31,020 tCO2e.
- BMg column B, route C = 1.370 → SEFA = 1.370 × 0.975 × 1 = 1.33575 → FAA = 16,029 tCO2e.
- Certificates = 31,020 − 16,029 = 14,991 → at €82.32 ≈ **€1.23 million** (≈ €103 per tonne of steel).
- With verified actual SEE 1.76 (75 % of the default without mark-up): certificates = (1.7625 − 1.33575) × 12,000 = 5,121 → ≈ €0.42 million. Actual data saves ≈ €0.8 million.

## Later years (same goods, default values, same price)

The FAA shrinks (CBAM factor 95 % 2027, 90 % 2028 … 0 % 2034) and the mark-up grows (20 % 2027, 30 % 2028), so the cost per tonne rises steeply: show the user the trend with `scripts/cbam_calc.py cost … --year 2028` or `estimate_cbam_cost` with year.

## Caveats to state

Indicative only; the declarant's actual liability depends on the verified data, the exact CN code and route, the price in the quarter / week of the obligation, and any change of law. Not legal or tax advice.
