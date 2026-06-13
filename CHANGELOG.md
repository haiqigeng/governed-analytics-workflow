# Changelog

## v0.2.3 - 2026-06-14

Per-analysis documentation update.

- Required each delivered analysis to store documentation in its own `analyses/<analysis-id>/` folder.
- Added a stable `analysis_id` convention for run artifacts.
- Clarified that durable context should point to per-analysis documentation instead of absorbing all run details.

## v0.2.2 - 2026-06-14

Final documentation update.

- Added a dedicated delivery documentation step after stakeholder output.
- Added expected `analysis-documentation.md` and `analysis-changelog.md` artifacts.
- Required material changes during an analysis to be documented with what changed, why, approval, and date.

## v0.2.1 - 2026-06-14

Presentation guidance update.

- Standardized stakeholder brief deck structure: title, analytics context, executive summary, result-specific analysis pages, and final recommendation/caveats.
- Added chart selection guidance by analysis purpose, including funnel/flow, bar/dot, line, heatmap, table, and KPI-card use cases.
- Added visual design guidance for restrained colors, clear labels, denominators, sample sizes, and caveats.

## v0.2.0 - 2026-06-14

Workflow refinement release based on an end-to-end contact-form analysis test.

- Combined triage and intake into one user-friendly first step.
- Added suggested defaults for unanswered fields, with user confirmation.
- Clarified analysis scope versus metric/dimension scope.
- Added explicit metric-to-source mapping with direct, derived, partial, and unavailable states.
- Kept bounded worker roles as internal execution modes rather than user-facing narration.
- Made PowerPoint (`.pptx`) the default artifact for stakeholder briefs.
- Updated prompt and README to reflect the refined interaction model.

## v0.1.0 - 2026-06-14

Initial release.

- Added `SKILL.md` with the governed analytics workflow.
- Added `AGENT_PROMPT.md` for agents that do not auto-discover skills.
- Added optional Codex/OpenAI metadata in `agents/openai.yaml`.
- Added human-readable project documentation in `README.md`.
- Added Git line-ending and ignore configuration.
