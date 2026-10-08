# Actual specific embedded emissions (SEE) — Implementing Regulation (EU) 2025/2547

Reporting period: calendar year. GWP AR5 (CO2 1, CH4 28, N2O 265, CF4 6,630, C2F6 11,100). CBAM gases by sector: CO2 everywhere; N2O for nitric acid and some fertilisers; PFCs (CF4, C2F6) for aluminium. CH4 is not a CBAM gas.

## 1. Installation and production processes

- Installation = the site (operator, address, UN/LOCODE, coordinates). Production process = the part of the installation producing one aggregated goods category (e.g. "crude steel", "iron or steel products", "cement clinker", "cement", "ammonia", "unwrought aluminium").
- Activity level AL = tonnes of good produced in the year by the process (all output, not only exports).
- Each CN code exported is assigned to the process producing it.

## 2. Source streams (direct emissions of the installation)

| Method | Formula |
|---|---|
| Combustion | Em (tCO2) = fuel quantity × NCV (TJ/unit) × EF (tCO2/TJ) × oxidation factor × (1 − biomass fraction) |
| Process | Em = activity (t) × EF (tCO2/t) × conversion factor (e.g. CaCO3 → 0.440) |
| Mass balance | Em = Σ 3.664 × activity (t) × carbon content (t C/t), outputs negative |
| Measurement (CEMS) | tonnes of gas measured (mandatory for N2O from nitric acid) |

IPCC 2006 defaults are acceptable when no better data exists (e.g. LPG NCV 0.0473 TJ/t, EF 63.1 tCO2/TJ; diesel NCV 0.0430 TJ/t, EF 74.1; natural gas EF 56.1).

## 3. Attribution to processes (Eq. 55-type balance)

AttrEm_dir(process) = Σ source streams of the process
  + emissions of measurable heat imported − heat exported (Q TJ × heat EF)
  + waste gases imported (V × NCV × 56.1) − waste gases exported (V × NCV × 56.1 × 0.667)
  − emissions of electricity produced on site and exported/used elsewhere.
Negative results are set to 0 (flag them). A waste gas imported from another process must not be entered again as its own combustion source stream.

## 4. Indirect emissions

Em_indir = electricity consumed (MWh) × emission factor. Default factor = Annex II of 2025/2621 (Viet Nam 0.581 tCO2/MWh; other countries per Annex II), or the actual factor of a direct line / physical PPA with evidence.
Indirect emissions are part of embedded emissions **only for non-Annex-II goods**: cement, clinker, calcined clay, aluminous cement, nitric acid, ammonia, urea, mixed fertilisers, sintered ore. For iron and steel (except sinter), aluminium and hydrogen, compute and report indirect emissions but do not add them to SEE.

## 5. Precursors

- Internal precursor (made by another process of the installation): use that process's SEE (compute processes in dependency order; cycles are an error).
- Purchased precursor: actual SEE only when the supplier provides verified data; otherwise the default value of its country of origin (Annex I; "other countries" row when the country has none) **with the mark-up of the year**; EU / EEA / Switzerland origin = 0 (still report the mass).
- Indirect emissions of a precursor are carried only when they count for that precursor's own category (e.g. sinter's indirect emissions are carried into steel; hydrogen's indirect emissions are dropped in ammonia).

## 6. SEE

SEE_dir = (AttrEm_dir + Σ M_precursor × SEE_precursor,dir) / AL
SEE_indir = (AttrEm_indir + Σ M_precursor × SEE_precursor,indir carried) / AL
SEE_total = SEE_dir + SEE_indir (non-Annex-II) or SEE_dir (Annex II)
Round SEE to 5 decimals; totals to whole tonnes in exports.

## 7. Worked example — hot-rolled coil from purchased billets (Viet Nam, 2026)

Rolling mill: 12,000 t hot-rolled coil (CN 7208 39 00), 12,400 t billets bought from a Vietnamese steelmaker without verified data, reheating furnace burns 1,150 t LPG, 9,800 MWh electricity.
- LPG: 1,150 × 0.0473 × 63.1 = 3,432.3 tCO2.
- Billets (CN 7207 11 14, ≤ 130 mm, rolled): VN default 2.35 × 1.10 = 2.585 tCO2/t → 12,400 × 2.585 = 32,054 tCO2.
- SEE_dir = (3,432.3 + 32,054) / 12,000 = 2.957 tCO2e/t. Indirect: 9,800 × 0.581 / 12,000 = 0.474 (reported, not counted: Annex II good).
- Compare: default for 7208 39 00 (VN) = 2.35 → 2.585 with mark-up. The actual SEE is higher here only because the billets use default values: verified billet data from the steelmaker is the biggest lever.

## 8. Default-value share

Share of embedded emissions based on default values = Σ (M × SEE from defaults) / total embedded emissions. Importers and verifiers look at it; keep it low by obtaining verified supplier data.
