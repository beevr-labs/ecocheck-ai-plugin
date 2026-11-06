# Doing it in EcoCheck (connector https://ecocheck.ai/mcp/account)

Every tool needs `workspace` (from `list_workspaces`), `inventory_id` and `year_id` (from `get_inventories`). Footprints live in an inventory year; the plan must include the LCA feature (otherwise the tools answer FEATURE_DISABLED). Ids are public ids: products `lcp_…`, processes `lcq_…`, inputs `lce_…`, results `lcr_…`, parameters `lcv_…`, scenarios `lcs_…`, co-products `lck_…`, organization templates `lct_…`.

## Read

| Need | Call |
|---|---|
| Products of the year with their latest result | `get_lca view=products` |
| The model: processes, inputs, parameters, scenarios, issues | `get_lca view=product product_id` |
| Saved results; one result in detail | `get_lca view=results` / `view=result result_id` |
| Rule check of a result (ISO 14067, EN 15804, PEF) | `get_lca view=checks result_id standard` |
| Compare products per declared unit (first = base) | `get_lca view=compare product_ids` |
| Emission factors / unit processes by words; one dataset | `lookup_lca_library kind=factors query` / `kind=dataset key` |
| Templates (built-in and the organization's) | `lookup_lca_library kind=templates` |
| CBAM goods of the year (SEE) to reuse; inventory totals of a facility | `kind=cbam_goods` / `kind=facility_inventory facility_id` |
| Substances for direct site emissions | `kind=elementary_flows query` |

## Build a footprint

1. **Start**: `save_lca_product action=create template=<key> name=…` (built-in: steel-rolling, aluminium-die-casting, metal-parts, plastic-packaging, corrugated-box, garment, wood-furniture, agri-food) or `template_id=lct_…` (organization template), or `data={name, unit, demand_amount, system_boundary, method_gwp}` for an empty model.
2. **Fill the quantities**: a template's quantities are parameters, all 0 in a new product. Read them with `get_lca view=product` (name, unit, meaning) and set them in one call: `save_lca_model entity=parameter data={values:{name: value, …}}`. Parameters shared by every product of the year: `entity=global_parameter`.
3. **Edit the model** (product must be DRAFT): `entity=process` (create / update; `background_key` copies a database unit process as an editable process), `entity=input` (BACKGROUND with a `factor_key` from `lookup_lca_library`, FOREGROUND linking another process, EMISSION of a gas; `input_id` + `background_key` makes a background input editable), `entity=coproduct` (allocation; set `allocation_method` on the process), `entity=derived_input source=facility_inventory | cbam | cff | supplier_pact` (inputs computed from the GHG inventory, CBAM SEE, the Circular Footprint Formula, a supplier PACT footprint).
4. **Check**: `calculate_lca` (nothing saved) → look at `top_contributions`, `per_process`, `data_quality`; `mode=uncertainty` (Monte Carlo), `mode=sensitivity` (each parameter ± delta_pct), `mode=scenarios` after `save_lca_model entity=scenario data={name, values:{…}}`.
5. **Keep**: `save_lca_product action=save_result` (a DRAFT result) or `action=finalise` (FINAL result, model frozen; needed for PACT). `action=reopen` to edit again; `action=clone` for an ecodesign variant; `action=save_template` to reuse the model in other years.
6. **English documents**: `save_lca_product action=update data={doc_en:{product, description, company, facility, address, activity, processes:{lcq_…: "English name"}}}`; EPD resource / waste indicators: `data={epd_declared:{…}}`.
7. **Documents**: `export_lca_document document=report | epd | ilcd | pact` with `result_id` (lang vi / en), or the model as `workbook` (Excel BOM), `jsonld` (openLCA), `simapro`, `ecospold2`; `workbook_template` = blank import template. Importing these files back is done on ecocheck.ai.

## Delete (ask the user first; Full access AI level)

`delete_lca_records entity=product | process | input | coproduct | parameter | scenario | global_parameter | template` with `confirm=true`.

## Worked example (EcoCheck demo)

"Hot-rolled steel coil", template steel-rolling, 1 tonne, cradle-to-gate, AR6, parameters: reheating gas 360 kWh, furnace electricity 15 kWh, billet transport 50 km, billet 1.03 t, rolling electricity 100 kWh, cooling water 1 m³, lubricants 0.5 kg, cutting yield 1.01 t, finishing electricity 5 kWh → about **2,595 kg CO2e per tonne**, of which billets at the Vietnamese CBAM default value ~2,445 kg (94 %): the first improvement is the billet supplier's actual embedded emissions.
