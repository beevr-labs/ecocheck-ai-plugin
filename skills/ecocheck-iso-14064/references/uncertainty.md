# Uncertainty and data quality

## Quantitative (IPCC approach 1, error propagation)

For a product (activity × factor): U_line = sqrt(U_AD² + U_EF²) (U as % at 95 % confidence).
For a sum of lines: U_total = sqrt(Σ (U_i × E_i)²) / Σ E_i.

Indicative uncertainties when no better information exists:

| Item | Typical U (95 %) |
|---|---|
| Revenue-grade electricity meter / EVN bill | ±1-2 % |
| Fuel by invoice / calibrated flow meter | ±2-5 % |
| Fuel by estimate (runtime × rating) | ±10-25 % |
| IPCC default CO2 factor (fossil fuels) | ±2-7 % |
| IPCC default CH4 / N2O factors | ±50-150 % |
| Refrigerant top-ups from service records | ±10-30 % |
| Grid emission factor (national) | ±5-10 % |
| Spend-based factors | ±50 % or more |

`scripts/ghg_inventory.py` computes line and total uncertainty when the CSV has `ad_uncertainty_pct` and `ef_uncertainty_pct` columns.

## Qualitative data-quality scoring

Score each line 1-5 on: data source (measured / invoiced / estimated), factor specificity (site / national / IPCC / spend), temporal fit, completeness. Report the weighted average and the main improvement actions.

## Statement in the report

Give the total uncertainty (e.g. "±4.8 % at 95 % confidence, dominated by refrigerant data and Scope 3 spend-based lines"), the method, and how it will be reduced next year.
