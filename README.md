# EcoCheck for Claude — GHG inventory and EU CBAM

EcoCheck is a greenhouse-gas inventory and EU CBAM platform used by Vietnamese manufacturers, exporters and their consultants. This plugin gives Claude two expert skills and the EcoCheck connector, so you can ask in Vietnamese or English:

- “Is CN 7208 39 00 covered by CBAM, and how much would an EU importer pay for 12,000 t in 2026?”
- “Record September data for the rolling mill: electricity 182,400 kWh, diesel 1,250 litres.”
- “Prepare our ISO 14064-1 inventory for 2026 and check which indirect categories are significant.”

## What is inside

| Component | What it does |
|---|---|
| `skills/ecocheck-cbam` | EU CBAM definitive period (2026+): scope by CN code, EU default values and mark-ups (Implementing Regulation (EU) 2025/2621 as corrected by 2026/1740), certificate cost after the free-allocation adjustment (2025/2620 benchmarks), actual specific embedded emissions (SEE) under 2025/2547, data request for suppliers. Includes `scripts/cbam_calc.py` (offline calculator, Python standard library only) and reference CSVs. |
| `skills/ecocheck-iso-14064` | Organization-level GHG inventory under ISO 14064-1:2018 (categories 1–6), mapped to GHG Protocol scopes and to Vietnam's Decree 06/2022 (amended by Decree 119/2025) and Decision 42/2026/QĐ-TTg: boundaries, significance, quantification, base year, uncertainty, report checklist, ISO 14064-3 verification pack. Includes `scripts/ghg_inventory.py` (CSV → tCO2e, standard library only) and a CSV template. |
| `.mcp.json` → `ecocheck` | Remote MCP server `https://ecocheck.ai/mcp/account` (OAuth sign-in with your EcoCheck account). Reads and, if you allow it, updates your own EcoCheck data: organizations, facilities, inventories, activity data, emissions reports, reduction targets, CBAM data, Word report export. |
| `.mcp.json` → `ecocheck-public` | Remote MCP server `https://ecocheck.ai/mcp`, no sign-in: inventory obligation check for Vietnamese facilities, regulations, CBAM scope / default values / cost estimate, quick ISO 14064-1 calculation, emission factors. |

## What it runs, sends and fetches

- The skills are instructions and reference files read by Claude. The two Python scripts run locally only when Claude or you call them; they make **no network calls** and only read the files you pass.
- The `ecocheck` server sends the tool calls Claude makes (for example the activity data you ask it to record) to `https://ecocheck.ai` over HTTPS, after you sign in with OAuth. Access is limited to what your EcoCheck account can see, the scope you approve (read, or read and write) and the AI access level your workspace owner sets. Every call is recorded in your workspace audit log. Your password is never shared with Claude.
- The `ecocheck-public` server receives only the parameters of public tools (for example a CN code or a sector); it needs no account and stores no personal data.
- Nothing else is installed, downloaded or executed.

## Install

Claude Code:

```bash
claude plugin marketplace add beevr-labs/ecocheck-ai-plugin
claude plugin install ecocheck@ecocheck
```

Then run `/mcp` and sign in to `ecocheck`. Without an EcoCheck account the skills and `ecocheck-public` still work.

ChatGPT and Claude (web, desktop): add the connector `https://ecocheck.ai/mcp/account` — see the [documentation](https://ecocheck.ai/ai/docs).

## Links

- Documentation: https://ecocheck.ai/ai/docs
- Privacy policy: https://ecocheck.ai/ai/privacy · Terms: https://ecocheck.ai/ai/terms
- Support: connect@beevr.ai · https://ecocheck.ai/contact
- Vietnamese: https://ecocheck.ai/ai · Skills download: https://ecocheck.ai/cong-cu/ai-skills

License: CC BY 4.0 (see `LICENSE`).
