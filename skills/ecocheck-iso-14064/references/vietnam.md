# Vietnam: mandatory GHG inventory (facility level)

Legal basis: Decree 06/2022/NĐ-CP on GHG mitigation and ozone layer protection, as amended by Decree 119/2025/NĐ-CP; facility list Decision 42/2026/QĐ-TTg; sector technical guidance by the ministries (e.g. Ministry of Industry and Trade for industry and energy). Sources and explainers: https://ecocheck.ai/article/blog/145/lo-trinh-kiem-ke-khi-nha-kinh.html and https://ecocheck.ai/article/blog/157/quyet-dinh-42-2026-qd-ttg-2441-co-so-kiem-ke-khi-nha-kinh

## Who must report

- Facilities on the list of Decision 42/2026/QĐ-TTg (issued 10/8/2026, in force 25/9/2026, replacing Decision 13/2024): 2,441 facilities — Industry and Trade 1,916; Construction 411; Transport 53; Agriculture and Environment 61.
- Thresholds behind the list: emissions ≥ 3,000 tCO2e/year; or energy use ≥ 1,000 TOE/year (thermal power plants, industrial production, freight transport companies, commercial buildings); or solid-waste treatment capacity ≥ 65,000 t/year.
- Quick check: EcoCheck tool `check_ghg_inventory_obligation` (MCP `https://ecocheck.ai/mcp`) or https://ecocheck.ai/cong-cu/tra-cuu-kiem-ke-khi-nha-kinh

## Deadlines

- Facility inventory report every two years to the provincial People's Committee before 31 March; next one before **31/3/2027** covering 2025 and 2026 data.
- Exception: the 110 facilities allocated allowances in the pilot (thermal power, iron and steel, cement) send a verified inventory report to the Ministry of Agriculture and Environment before 1 December each year from 2027; their annual mitigation report still goes before 31 March.

## ISO 14064-1 vs. Decree 06 facility inventory

| Topic | Decree 06 facility inventory | ISO 14064-1 organization inventory |
|---|---|---|
| Unit | Facility (site) on the list | Organization (one or many sites) |
| Scope | Direct emissions and emissions from purchased energy, per national template and sector guidance | Categories 1-6; indirect 3-6 by significance |
| GWP | As set by the national guidance (AR5 in current templates) | Chosen and stated by the organization |
| Factors | National factors first (grid factor, national lists), IPCC defaults otherwise | Any justified source |
| Assurance | State appraisal / verification as organised under the Decree | Voluntary ISO 14064-3 verification |

A good practice is one data set serving both: build the facility inventory for Decree 06 and extend it to categories 3-6 for customers (ISO 14064-1, GHG Protocol, CBAM, SBTi).

## Factors to cite

- Grid electricity: the latest official grid emission factor notice of the Ministry of Agriculture and Environment / Department of Climate Change for the reporting year (if the year's factor is not yet published, use the latest available and say so). Do not use the EU CBAM default 0.581 tCO2/MWh for the national inventory — that value is for CBAM indirect emissions only.
- Fuels and processes: national lists of emission factors where published, otherwise IPCC 2006 defaults.
