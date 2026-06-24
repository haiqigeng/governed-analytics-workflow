# Governed Analytics Workflow

An interactive, reviewable analytics workflow for AI-assisted business analysis.

This repository contains a Codex skill that helps an analyst or AI agent turn a vague business question into a traceable analysis process with scoped metrics, data readiness checks, reproducible evidence, human review, and stakeholder-ready outputs.

The core idea is simple: do not let polished claims outrun the evidence. The workflow keeps assumptions, caveats, metric definitions, source mapping, and review status visible from intake through delivery.

## What It Is For

Use this workflow when analytics work needs more structure than a quick answer, especially when the result may inform:

- product, marketing, revenue, operations, or digital decisions
- prioritization or roadmap choices
- executive or stakeholder presentations
- metric definitions, source mapping, or readiness checks
- follow-up experiments, monitoring, or measurement plans

It is designed for Codex, Claude Code, Gemini, and other coding or analysis agents that can inspect files, run queries or scripts, create artifacts, and collaborate with a human reviewer.

## What It Does

The workflow guides an agent through:

1. Triage and intake
2. Scope, metric, and grain framing
3. Data readiness assessment
4. Analysis plan creation
5. Bounded execution
6. Quality review
7. Reproducibility packet generation
8. Human approval
9. Stakeholder output creation
10. Delivery documentation
11. Durable context updates
12. Follow-up monitoring or experiment planning

For low-risk descriptive work, steps can be combined. For medium- or high-risk decisions, the workflow preserves explicit review gates before trusted output is produced.

## Repository Contents

```text
.
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- dataviz-catalogue-selection.md
    `-- presentation-generator-brief.md
```

- `SKILL.md` contains the full workflow instructions.
- `agents/openai.yaml` provides agent metadata and a default prompt.
- `references/presentation-generator-brief.md` defines the handoff format for stakeholder decks.
- `references/dataviz-catalogue-selection.md` provides chart-selection guidance based on The Data Visualisation Catalogue.

## Installation

Clone or copy this repository into your Codex skills directory:

```powershell
git clone https://github.com/HQ-Guillaume/governed-analytics-workflow.git "$env:USERPROFILE\.codex\skills\governed-analytics-workflow"
```

Restart Codex after installation so the skill is discovered.

You can then invoke it by name:

```text
Use $governed-analytics-workflow to run a traceable analytics analysis.
```

## Example Prompts

```text
Use $governed-analytics-workflow to analyze why trial-to-paid conversion dropped last month and produce a stakeholder brief.
```

```text
Use $governed-analytics-workflow to check whether our onboarding funnel data is ready for an executive decision.
```

```text
Use $governed-analytics-workflow to compare campaign performance by channel, preserving caveats and source mapping.
```

## Expected Outputs

When artifacts are produced, the workflow stores them under an analysis-specific folder such as:

```text
analyses/2026-06-24-conversion-drop-summary/
```

Common artifacts include:

- `analytics-intake.md`
- `analysis-framing.md`
- `readiness-assessment.md`
- `analysis-plan.md`
- `worker-result-packets.md`
- `quality-review.md`
- `reproducibility-packet.md`
- `presentation-generator-brief.md`
- `stakeholder-brief.pptx`
- `analysis-documentation.md`
- `analysis-changelog.md`
- `decision-log-entry.md`

Generated analysis folders are intentionally ignored by Git so local data, drafts, and outputs are not committed by default.

## Governance Principles

The workflow is built around a few strict rules:

- Claims must map back to evidence, source fields, transformations, and caveats.
- Metric grain and calculation grain must be explicit before rates, funnels, or rankings are trusted.
- Readiness gaps are documented instead of papered over.
- Medium- and high-risk work requires human review before stakeholder output is treated as approved.
- Caveats must travel with the output, not hide in an appendix.
- Durable context is updated only after review.

## Review Status Labels

Artifacts and claims use clear status labels:

- `Draft`
- `Ready for review`
- `Approved`
- `Approved with caveats`
- `Rejected`
- `Superseded`

Claims may also be labeled:

- `Verified`
- `Directional`
- `Assumed`
- `Needs validation`
- `Rejected`
- `Superseded`

## Presentation Support

If the expected output is a stakeholder brief, the workflow creates a `presentation-generator-brief.md` and, where tooling allows, a PowerPoint deck.

It uses The Data Visualisation Catalogue as the default chart-selection reference unless the user provides another visual guide, deck template, brand guide, or preferred chart style.

## Data And Privacy Notes

This repository does not include company data, credentials, or data-source integrations. The workflow uses whatever files, notebooks, queries, dashboards, or connectors are available in the working environment.

Keep raw data access-controlled. Prefer reproducible queries, output tables, and anonymized samples over exporting personal or sensitive records.

## License

No license has been specified yet. Add one before redistributing or accepting external contributions.
