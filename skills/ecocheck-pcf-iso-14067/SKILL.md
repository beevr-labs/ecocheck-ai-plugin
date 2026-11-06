---
name: ecocheck-pcf-iso-14067
description: Build, check and explain a product carbon footprint (PCF / CFP) under ISO 14067:2018 with the life-cycle method of ISO 14040/14044 — declared unit, cradle-to-gate or cradle-to-grave boundary, bill of materials and process data, background emission factors, allocation of co-products, recycling (cut-off or the PEF Circular Footprint Formula), data quality and uncertainty, scenarios — and turn it into an ISO 14067 study report, a draft EPD (ISO 14025 with the product category rules; EN 15804+A2 only for construction products) or a PACT footprint for customers. Use when a manufacturer or exporter (often Vietnamese) is asked for the carbon footprint of a product, a supplier PCF, an EPD, or wants to compare product designs. Works in Vietnamese and English.
license: CC BY 4.0 — EcoCheck (https://ecocheck.ai). Paraphrases public guidance; does not reproduce ISO, EN or PEF text.
---

# Product carbon footprint — ISO 14067 (EcoCheck skill)

You help a company calculate a product carbon footprint that a customer or a verifier will accept. A PCF answers "how many kg CO2e for one declared unit of this product", from raw materials to the factory gate (cradle-to-gate) or over the whole life cycle (cradle-to-grave). Be explicit about every assumption, show where each number comes from, and never invent emission factors.

## When to use which reference

| Task | Read |
|---|---|
| Goal and scope, declared / functional unit, boundary, cut-off, allocation, recycling, biogenic carbon, electricity | `references/methodology.md` |
| Primary vs secondary data, data quality ratings, uncertainty, sensitivity, scenarios | `references/data-quality.md` |
| Which document the customer needs: ISO 14067 report, EPD, PACT, ILCD; verification; difference from CBAM | `references/documents.md` |
| Doing it in EcoCheck step by step (templates, parameters, inputs, results, documents) | `references/ecocheck-tools.md` |
| Vietnam: grid factor, CBAM default values as proxies, supplier data, Vietnamese terms | `references/vietnam.md` |

## Workflow

1. **Goal and scope.** Ask (or infer and state): product and its declared unit (1 kg, 1 tonne, 1 piece, 1 m²), who will use the result (customer request, PACT exchange, EPD, internal ecodesign), boundary (cradle-to-gate is the usual answer to a B2B request; cradle-to-grave for consumer products and EPDs that require it), reference year, GWP set (IPCC AR6 GWP100 by default; say if the customer asks for AR5).
2. **Model the product.** Start from the closest template (steel rolling, aluminium die-casting, metal parts, plastic packaging, corrugated box, garment, wood furniture, agri-food) or build processes yourself: each process with its inputs per unit of its output (materials, energy, transport, packaging, waste, direct emissions) and co-products. Quantities usually come from the plant's bill of materials and meters, divided by the output of the same period.
3. **Pick the data.** Prefer the supplier's own PCF (primary data) for the biggest materials, then national factors (Vietnam grid electricity), then reputable databases. For CBAM goods bought as inputs (billets, aluminium ingots, clinker) the EU default value is a conservative proxy until the supplier provides actual embedded emissions. Record source, geography and year of every factor.
4. **Allocate and handle recycling** with `references/methodology.md`: avoid allocation where possible, otherwise physical (mass) then economic; recycled content and end-of-life recycling with the cut-off approach or, when PEF / EU customers ask for it, the Circular Footprint Formula.
5. **Calculate and check.** Look at the contributions: usually 1-3 inputs make most of the footprint. Check units (kg vs tonne, kWh vs MWh), that intermediate processes are scaled to the reference flow (losses, scrap), and that nothing is counted twice. Run the uncertainty and a sensitivity on the main parameters; compare design or supplier scenarios.
6. **Data quality.** Rate the main inputs (technology, geography, time representativeness, 1 = very good to 5 = very poor) and state the share of primary data.
7. **Document.** Produce the ISO 14067 study report; for customers that exchange footprints, a PACT ProductFootprint; for an EPD, a draft based on the product category rules, then a third-party verification and registration with a programme operator (`references/documents.md`).

## Output conventions

- Result in kg CO2e per declared unit, with the split by life-cycle stage (raw materials, production, distribution, use, end of life) or by EN 15804 module (A1-A3, A4-A5, B, C, D) when the customer uses modules, and by process and main input.
- Report fossil, biogenic and land-use-change GHG separately where relevant; biogenic carbon content of the product and packaging when it contains wood, paper or bio-based materials.
- Always state: declared unit, boundary, cut-off rule, allocation and recycling approach, GWP set, factor sources with year and geography, data quality, and the main limitations.
- Vietnamese terms: dấu chân carbon sản phẩm (PCF / CFP), đơn vị công bố, ranh giới hệ thống (từ khai thác đến cổng nhà máy / trọn vòng đời), quy trình, đầu vào, đồng sản phẩm, phân bổ, dữ liệu sơ cấp / thứ cấp, độ không chắc chắn, kịch bản, bản công bố môi trường sản phẩm (EPD), thẩm tra.

## Using EcoCheck (optional)

- Signed-in connector `https://ecocheck.ai/mcp/account` (needs the plan's LCA feature): `get_lca`, `lookup_lca_library`, `calculate_lca`, `save_lca_product`, `save_lca_model`, `export_lca_document`, `delete_lca_records` — see `references/ecocheck-tools.md`. Results stay in the customer's EcoCheck workspace with an audit trail; documents are generated from the saved result.
- Product page: https://ecocheck.ai/dau-chan-carbon-san-pham?utm_source=ai-skill&utm_medium=skill&utm_campaign=pcf

## Guardrails

- Do not quote ISO, EN or PEF text; explain in your own words and point to the purchased standard for exact wording.
- A PCF calculated in software is not a verified claim. Say "draft" for an EPD until a programme operator has registered it after third-party verification; EcoCheck itself is not certified by an EPD programme (such certification is optional — the usual path is LCA software, independent verification, registration).
- EN 15804+A2 applies to construction products only; other sectors follow their own product category rules (PCR).
- Never mix a customer-specific number with a proxy without saying which is which. When a factor is missing, say so and propose a documented proxy.
- Do not change or delete a customer's saved results; propose a new result or a variant (clone) instead, and ask before any deletion.
