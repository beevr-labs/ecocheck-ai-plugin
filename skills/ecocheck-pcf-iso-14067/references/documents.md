# Which document the customer needs

| Request | Document | Standard / format | Verification |
|---|---|---|---|
| "Send us the carbon footprint of product X" | PCF value + short method note, or the full **ISO 14067 CFP study report** | ISO 14067 (method of ISO 14040/14044) | optional; critical review or third-party verification if the customer asks or the claim is public |
| Supplier footprint exchange through software (PACT network, buyer portals) | **PACT ProductFootprint** (JSON, PACT Methodology / Technical Specification v3) | cradle-to-gate, FINAL result, primary-data share and data quality indicators | per buyer; verification statement optional |
| Environmental Product Declaration | **EPD** (draft from the LCA, then verified and registered) | ISO 14025 (2026 edition) + the product category rules (PCR) of the programme; EN 15804+A2 for **construction products only** | mandatory independent third-party verification by the programme operator (e.g. International EPD System, IBU, EPD Norge) |
| Upload to an EPD programme / EPD hub | **ILCD+EPD** data set (ILCD format with EPD extensions) | programme's technical rules | as for the EPD |
| EU CBAM | not a PCF: **specific embedded emissions** of the installation per CN code (EU Regulation 2025/2547) | CBAM methodology | accredited CBAM verifier (from 2026) |

## ISO 14067 CFP study report — content to include

Goal and scope (declared / functional unit, boundary, cut-off, reference year), the product system diagram, data sources and quality with the share of primary data, allocation and recycling choices, electricity treatment, GWP set, results by stage / process / gas with biogenic carbon reported separately, uncertainty and sensitivity, interpretation (hotspots, limitations, improvement options), and, if verified, the verification statement.

## EPD — the usual path

1. Pick the programme operator and its PCR for the product (or EN 15804+A2 + c-PCR for construction products).
2. Run the LCA in software with the plant's data (the software does not need to be certified by the programme; that certification is optional).
3. Prepare the background report and the draft EPD from the LCA.
4. Independent verification (the verifier asks for the plant's source records).
5. Registration and publication by the programme operator (fees per programme).

## PCF vs CBAM

A CBAM value covers only the installation's direct (and for some goods indirect) emissions plus precursors, under EU rules, per tonne of a CN code. A PCF covers the whole supply chain of the product (materials, energy, transport, packaging…) per declared unit, under ISO 14067. A CBAM value of a purchased good (billet, ingot, clinker) can feed a PCF as the emission factor of that input — not the other way round.
