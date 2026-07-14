# Governed Analytics Workflow

[![CI](https://github.com/haiqigeng/governed-analytics-workflow/actions/workflows/ci.yml/badge.svg)](https://github.com/haiqigeng/governed-analytics-workflow/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/haiqigeng/governed-analytics-workflow?sort=semver)](https://github.com/haiqigeng/governed-analytics-workflow/releases/latest)
[![License](https://img.shields.io/github/license/haiqigeng/governed-analytics-workflow)](LICENSE)

An adaptive, evidence-governed analytics skill for Codex, Claude Code, Gemini, and other file- and tool-capable AI agents.

## Why It Exists

Analytics requesters often provide more information than the analysis needs: proposed indicators, preferred explanations, desired charts, old analyses, and solution ideas. Those inputs may be useful, but they are not automatically a valid analysis specification.

This skill makes the agent responsible for locating the real decision or learning need before querying data. It then connects that need to a question tree, appropriate analytical methods, reproducible evidence, reviewed claims, honest visualisation, and a decision-ready delivery.

The central rule is:

```text
Business need
-> decision or learning objective
-> question tree
-> evidence
-> reviewed claim
-> stakeholder output or action
```

## Who It Serves

- Analysts interpreting unclear stakeholder briefs
- Product, marketing, digital, revenue, and operations teams
- Teams combining several analytics, qualitative, browser, or business sources
- Decision-support work that needs traceability and review
- Agents producing stakeholder briefs, PowerPoint decks, reproducibility evidence, or follow-up plans

It is not a replacement for business ownership, legal/privacy judgement, causal study design, source permissions, or human approval of consequential decisions.

## Adaptive Workflow

Users see four phases:

1. **Contract:** interpret the need, confirm the question tree, scope, definitions, and evidence limits.
2. **Evidence:** check readiness, execute bounded work, validate, and review claims.
3. **Synthesis:** answer the tree, select visuals, and produce stakeholder output.
4. **Delivery:** document, version durable context, and define follow-up.

Twelve operational checkpoints remain inside those phases. The skill selects a `Light`, `Standard`, or `Deep` discovery mode so a clear low-risk request stays fast while a vague or consequential request receives stronger framing and approval gates.

## Needs Discovery

Before selecting metrics, the agent separates:

- facts and business objectives;
- constraints and output preferences;
- hypotheses and preferred explanations;
- suggested metrics, methods, breakdowns, and solutions;
- uncertainties and missing decisions.

Depending on the case, it applies decision-backward framing, analytical laddering, assumption mapping, stakeholder mapping, evidence-ceiling analysis, alternative framing, minimum-useful-scope review, and a pre-mortem.

The result is a concise framing proposal and a question tree. The requester confirms the real need without having to design grain, metrics, or statistical methods.

## Question Tree

The tree progresses through three states:

```text
Draft -> Confirmed -> Operational
```

Operational leaves contain a problem type, source, grain, metric, method, validation rule, and expected output. Every original request item is mapped to an answered question, supporting context, parked item, rejected assumption, unavailable item, or superseded need.

No query, claim, chart, or recommendation should exist without a path back to the tree.

## Analytical Problem Types

The skill supports six routes:

| Type | Typical answer |
| --- | --- |
| Make predictions | What is likely to happen or which case is likely next? |
| Categorise things | Which class or useful segment does this belong to? |
| Spot something unusual | What departs from an appropriate baseline? |
| Identify themes | Which recurring ideas appear in unstructured evidence? |
| Discover connections | Which variables, behaviours, or entities are associated? |
| Find patterns | What distributions, trends, cohorts, paths, or recurring structures exist? |

One primary type guides the analysis. Secondary types are attached to distinct subquestions. Each playbook defines required inputs, baselines, methods, validation, claim limits, outputs, and follow-up.

## Evidence Governance

Important numbers receive a definition fingerprint containing population, grain, period, scope, filters, numerator, denominator, deduplication, query reference, and run date. Sources receive authority, coverage, freshness, joinability, allowed-use, and forbidden-use records.

Findings move through a controlled lifecycle:

```text
Observation -> Candidate -> Validated -> Approved
                         \-> Rejected
Approved or validated -> Superseded when replaced
```

The promotion point is governed, not every exploratory read or query. High-risk and externally durable claims require human approval. Independent review uses technical, audience, and domain-aware but analysis-naive lenses.

## Visualisation

For stakeholder analyses containing charts, the skill uses [The Data Visualisation Catalogue](https://datavizcatalogue.com/search.html) as the default function-first reference unless the user provides another system.

The live catalogue is consulted once per distinct communication function. Each analytical visual records its claim, data structure, candidate charts, selected chart, required labels, and rendered QA result.

Hard rules reject misleading choices such as:

- exclusive classes displayed as a funnel;
- percentages without a denominator;
- missing zero or expected categories;
- lines across unordered categories;
- part-to-whole charts for overlapping groups;
- incompatible grains or axes;
- visuals that imply unsupported causality.

Specialist analytical diagnostics may override catalogue choices when methodologically required.

## Runtime Artifacts

The canonical run file is `analysis-manifest.json`. The default analysis folder stays small:

```text
analyses/<analysis-id>/
|-- analysis-manifest.json
|-- evidence/
|-- results.md
`-- requested delivery, when needed
```

Plans, reproducibility packets, documentation, changelogs, and presentation briefs are generated only when risk, review, or delivery requires them. One active artifact is maintained per purpose; changed fingerprints mark dependent claims and outputs stale.

Create a run:

```powershell
python scripts/analysis_guard.py init analyses/example-analysis --analysis-id example-analysis
```

Validate before delivery:

```powershell
python scripts/analysis_guard.py validate analyses/example-analysis/analysis-manifest.json --strict
python scripts/analysis_guard.py stale analyses/example-analysis/analysis-manifest.json --fail-on-stale
python scripts/analysis_guard.py scan analyses/example-analysis
```

The runtime utility uses only the Python standard library. The same contracts can be applied manually if Python is unavailable.

## Repository Contents

```text
.
|-- SKILL.md
|-- agents/openai.yaml
|-- references/
|   |-- needs-discovery-and-analysis-contract.md
|   |-- problem-type-playbooks.md
|   |-- evidence-claims-and-review.md
|   |-- synthesis-and-visualisation.md
|   `-- presentation-generator-brief.md
|-- assets/analysis-manifest.template.json
|-- scripts/analysis_guard.py
|-- tools/
|-- tests/
`-- .github/workflows/
```

`tools/`, `tests/`, and repository documentation are not included in the runtime release package.

## Installation

Clone into the skills directory used by your agent:

```powershell
git clone https://github.com/haiqigeng/governed-analytics-workflow.git "$env:USERPROFILE\.codex\skills\governed-analytics-workflow"
```

Alternatively, download the runtime zip from the latest GitHub release and extract the contained `governed-analytics-workflow` folder into the appropriate skills directory.

Restart or reload the agent so it discovers the skill.

## Example Prompts

```text
Use $governed-analytics-workflow to interpret this stakeholder email, propose the real analytical need and question tree, and wait for my framing confirmation.
```

```text
Use $governed-analytics-workflow to investigate an unexpected performance change, preserving the expected baseline and false-positive risks.
```

```text
Use $governed-analytics-workflow to compare observed journeys with an outcome and produce a reviewed stakeholder deck without causal overstatement.
```

## Agent Compatibility

The skill describes operations rather than vendor-specific commands. Codex, Claude Code, Gemini, and other agents can use local equivalents for files, queries, notebooks, APIs, browsers, visualisation, and presentations.

Unavailable tools must be recorded as limitations. The skill contains no client data, credentials, source integration, or machine-specific path.

## Release Checks

Run before contributing or publishing:

```powershell
python tools/check_release.py --tag v1.0.0 --release-notes CHANGELOG.md
python -m unittest discover -s tests -v
python tools/build_skill_package.py --output dist/governed-analytics-workflow-v1.0.0.zip
```

CI validates structure, reference routing, portability, the manifest contract, six problem types, claim promotion, stale dependencies, and chart regressions. Tagged releases build a deterministic runtime archive.

## Privacy And Security

Keep data and generated analysis artifacts outside the repository. Do not commit credentials, client information, private dashboard links, raw exports, personal data, or machine-specific paths. Use the runtime scan before sharing or publishing work.

See [SECURITY.md](SECURITY.md) for reporting guidance.

## License

MIT. See [LICENSE](LICENSE).
