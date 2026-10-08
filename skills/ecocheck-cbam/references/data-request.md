# Producer ↔ EU importer data exchange

## What the EU importer (authorised CBAM declarant) needs per consignment / year

| Item | Detail |
|---|---|
| Installation | Operator name and contact, installation name (English), address, country, UN/LOCODE, coordinates, installation identifier in the CBAM registry if registered |
| Goods | 8-digit CN code, quantity (t), production route |
| Embedded emissions | SEE direct and indirect (tCO2e/t), embedded emissions of the quantity, methodology (actual / default), share based on default values |
| Electricity | Consumption, emission factor and its source (default Annex II or actual with evidence) |
| Precursors | CN codes, quantities, origin, SEE and whether verified or default |
| Carbon price paid | Any carbon price effectively paid in the country of origin (none for Viet Nam's pilot ETS free allocation in 2026) |
| Verification | Verification report by an accredited verifier when actual data is used (from the definitive period) |

## What the operator keeps (monitoring documentation)

Monitoring plan (installation boundary, processes, source streams, methods, data sources), meter calibration, fuel invoices and lab analyses, production records by CN code, precursor purchase records and supplier SEE certificates, electricity bills and contracts, calculation workbook, change log.

## Request template for an upstream supplier (e.g. billets, pig iron, clinker)

> For the [year] deliveries of [product, CN code] (… t), please provide: installation name / address / country; production route; specific embedded emissions direct and indirect (tCO2e/t) under Implementing Regulation (EU) 2025/2547; verification status (verifier, date); electricity emission factor used; precursors used and their SEE. Without verified data we must apply the EU default value with mark-up (2026: +10 %).

## Checklist before sending to the importer

- CN codes match the commercial invoice and customs declaration.
- AL covers the full year's production of each process, not only exports.
- Precursors with default values carry the mark-up of the year; EU-origin precursors are 0.
- Indirect emissions reported but not added for Annex II goods.
- SEE to 5 decimals; units tCO2e per tonne.
