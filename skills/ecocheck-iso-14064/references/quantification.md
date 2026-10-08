# Quantification

## Core formula

Emissions (t gas) = Activity data × Emission factor (with consistent units)
tCO2e = Σ gases (t gas × GWP)

Per line keep: source, period, activity value + unit, factor value + unit + reference, gas split, GWP set, result.

## GWP (100-year)

| Gas | AR5 | AR6 |
|---|---|---|
| CO2 | 1 | 1 |
| CH4 (fossil) | 28 | 29.8 |
| CH4 (non-fossil) | 28 | 27.0 |
| N2O | 265 | 273 |
| SF6 | 23,500 | 24,300 |
| HFC-134a | 1,300 | 1,530 |
| HFC-32 | 677 | 771 |
| R-410A (blend 50 % HFC-32 / 50 % HFC-125) | 1,924 (blend; 2,088 is the AR4 value often quoted) | 2,256 (blend) |
| R-404A (44 % HFC-125 / 52 % HFC-143a / 4 % HFC-134a) | 3,943 | 4,728 |
| R-407C (23 % HFC-32 / 25 % HFC-125 / 52 % HFC-134a) | 1,624 | 1,908 |
| R-22 (HCFC-22) | 1,760 | 1,960 |

Use one set for the whole inventory and the base year. Vietnam's Decree 06 reporting and EU CBAM use AR5. HCFCs (R-22) are Montreal-Protocol gases: many programmes report them separately or exclude them — state your choice.

## Combustion (IPCC 2006 approach)

Energy (TJ) = fuel quantity × density (if volume) × net calorific value (NCV)
CO2 (t) = Energy (TJ) × EF_CO2 (t/TJ) × oxidation factor (1.0 by IPCC 2006 default)
CH4, N2O: Energy × EF per technology.

IPCC 2006 defaults (stationary, energy industries / manufacturing):

| Fuel | NCV (TJ/Gg) | EF CO2 (t/TJ) | Typical density |
|---|---|---|---|
| Diesel / gas oil (DO) | 43.0 | 74.1 | 0.82-0.845 kg/L |
| Residual fuel oil (FO) | 40.4 | 77.4 | 0.94-0.98 kg/L |
| LPG | 47.3 | 63.1 | 0.51-0.54 kg/L (liquid) |
| Motor gasoline | 44.3 | 69.3 | 0.74 kg/L |
| Natural gas | 48.0 | 56.1 | per supplier (Nm³ → GJ from invoice) |
| Anthracite | 26.7 | 98.3 | — |
| Other bituminous coal | 25.8 | 94.6 | — |

Prefer supplier or national values when available (e.g. coal NCV from lab analysis). Worked example: 1,250 L diesel × 0.82 kg/L = 1.025 t = 0.001025 Gg × 43.0 TJ/Gg = 0.0441 TJ × 74.1 = 3.27 tCO2 (+ small CH4 / N2O).

## Purchased electricity (category 2)

tCO2e = kWh × grid emission factor (tCO2/MWh) / 1000. Use the latest grid factor officially published for Vietnam (Ministry of Agriculture and Environment / Department of Climate Change notice) for the reporting year or the most recent available — cite the notice. Report location-based; a market-based figure only with valid contractual instruments (I-REC, PPA with certificates).

## Refrigerants and SF6 (mass balance)

Emissions (kg) = top-ups during the year + (capacity of retired units − recovered) − capacity of new units charged at the factory (simplified: kg recharged = kg leaked). × GWP.

## Process emissions (examples)

- Limestone calcination: t CaCO3 × 0.440 tCO2/t.
- Clinker: t clinker × CaO/MgO-based factor (≈ 0.52-0.53 tCO2/t clinker by default).
- Wastewater CH4: organic load (COD) × Bo × MCF − recovered CH4.

## Spend-based and average-data (categories 3-6)

tCO2e = spend × EEIO factor (kgCO2e per currency unit, price year corrected) or mass × cradle-to-gate factor. Label them as lower quality and plan supplier-specific data for large items.

## Biogenic CO2 and removals

Report biogenic CO2 (biomass, biogas) separately from category 1 totals; CH4 / N2O from biomass combustion stay in category 1. Report removals separately (never net them silently against emissions).

## Rounding

Calculate with full precision; round only in the report (t CO2e to 2 decimals or whole tonnes). Totals must equal the sum of the rounded table only within rounding.
