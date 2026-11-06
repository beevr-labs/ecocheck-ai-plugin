# Methodology of a product carbon footprint (ISO 14067, ISO 14040/14044)

Paraphrased guidance. Consult the purchased standards for exact requirements.

## Goal and scope

- **Goal**: why the footprint is made and for whom (B2B customer request, supplier exchange, EPD, ecodesign, internal). The goal drives the boundary and the data requirements.
- **Declared unit** (cradle-to-gate, no use phase): a quantity of product — 1 kg of resin, 1 tonne of steel coil, 1 corrugated box. **Functional unit** (cradle-to-grave): the service the product delivers over its life — e.g. "packaging and protecting 10 kg of goods during one shipment".
- **Reference flow**: how much product is needed for one declared / functional unit (including losses).
- **Reference year**: the 12-month period the activity data represent; factors should be as close to it as possible.

## System boundary

- **Cradle-to-gate**: raw material extraction, transport to the plant, manufacturing up to the gate (EN 15804 modules A1-A3). The usual answer to a B2B PCF request and the scope of PACT footprints.
- **Cradle-to-grave**: adds distribution (A4), installation (A5), use and maintenance (B1-B7), end of life — demolition, transport, waste processing, disposal (C1-C4). Benefits and loads beyond the system boundary (recycling credits, energy recovery) go to **module D**, reported separately and never netted into the total.
- **Cut-off**: inputs below a small share (commonly 1 % of mass and energy per process, at most 5 % in total) may be left out if documented; never cut off an input known to be significant in emissions (e.g. aluminium, refractory changes in some plants).
- Capital goods (machines, buildings) are usually excluded for B2B footprints; say so.

## Allocation of co-products (ISO 14044 order of preference)

1. Avoid it: divide the process into sub-processes, or expand the system (substitution) when a co-product clearly replaces another product.
2. Physical relationship: by mass, energy content or another physical property that reflects how inputs change with outputs.
3. Other relationship: usually economic value (price × quantity) — use when the co-product has a much lower value per kg (slag, scrap, by-products).
State the method per process and keep shares summing to 100 %.

## Recycling and end of life

- **Cut-off (recycled content) approach**: the product carries the burdens of the recycling process for recycled input; scrap leaving the system leaves without burden or credit. Simple, common in PCF requests and many PCRs.
- **Circular Footprint Formula (PEF / EF 3.1)**: splits burdens and benefits of recycled content and end-of-life recycling between supplier and user with factor A (market situation), quality ratios Qsin/Qp and Qsout/Qp, and the recycled content R1 / recycling rate R2. Required for PEF studies and asked by some EU customers.
- Do not mix approaches within one study.

## Specific topics

- **Electricity** (ISO 14067 asks for the specific treatment of electricity): use the supplier-specific or contractual instrument (green tariff, I-REC, DPPA) only when it meets the quality criteria (no double counting, same market, matching period); otherwise the national grid factor. Report which one was used.
- **Biogenic carbon**: CO2 taken up by wood, paper, bio-based plastics and released at end of life; report biogenic emissions and removals separately; state the biogenic carbon content of the product and packaging (kg C).
- **Land-use change**: direct land-use change emissions for agricultural / forestry inputs where data exist (often within supplier data).
- **GWP**: IPCC AR6 GWP100 is the current default; some customers and programmes still ask for AR5 — state the set. Methane of fossil and biogenic origin have different AR6 values.
- **Transport**: tonne-kilometres = mass transported × distance, with the vehicle type and load factor of the factor used.
- **Packaging** of the product and of purchased inputs is part of the system when within the cut-off rule.

## Common mistakes to check

- Unit slips: kg vs tonne, kWh vs MWh, per-piece factors applied to kg.
- Intermediate processes not scaled to the reference flow (scrap and yield losses ignored).
- Double counting: plant electricity both in a process and in an overhead process; transport inside a supplier's footprint counted again.
- Recycling credits netted into A1-A3 instead of module D.
- Proxy factors from another country or a decade-old dataset used without saying so.
