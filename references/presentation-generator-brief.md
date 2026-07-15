# Presentation Generator Brief

Create this brief only after the analysis blueprint, quality checks, evidence, and claim set pass the required review stage. It is a delivery specification, not a place to perform new analysis.

## Generator Contract

- Use only stakeholder-eligible claims from `analysis-manifest.json`.
- Preserve claim wording, posture, population, period, grain, denominator, coverage, uncertainty, fingerprints, and caveats.
- Use only canonical result tables or approved evidence references.
- Do not calculate, interpolate, merge, or infer missing results.
- Do not introduce recommendations without decision lineage.
- Follow the user's template, brand, language, and exact business or interface terminology.
- Follow `synthesis-and-visualisation.md` for chart selection, measurement cards, wording review, and rendered QA.

## Brief Header

```text
Analysis ID and manifest path:
Audience and analytics literacy:
Decision or learning objective:
Selected framing and evidence ceiling:
Primary and secondary problem types:
Risk and review status:
Approved claim IDs:
Period, timezone, population, and grain:
Template, brand, language, and terminology inputs:
Visualisation guide and live-catalogue status:
Required delivery format:
```

## Narrative Architecture

Do not use a fixed number of slides. Include only sections required by the blueprint and audience.

A typical sequence may contain:

1. Title, audience, date, and review posture.
2. Concise context required to understand population, process, scope, and measurement.
3. Executive summary with decision-relevant approved claims and implications.
4. Analysis sections ordered by context, decision, diagnostic, and problem-type logic.
5. Recommendations or tests supported by evidence.
6. Measurement, methods, caveats, validation, or appendix material when useful.

Do not create a context chapter when context adds no interpretive or decision value. Preserve mixed-analysis branch boundaries.

## Per-Slide Specification

Repeat for every slide:

```text
Slide ID:
Question ID:
Claim IDs:
Slide function: context | finding | comparison | explanation | recommendation | method | appendix
Audience question answered:
Message title:
Evidence and claim posture:
Body copy:
Decision implication:
Required caveats:
Result/data reference:
Metric IDs and fingerprint hashes:
Visual ID and type:
Measurement card:
Source context or screenshot reference:
Speaker notes:
Dependencies:
```

Titles should state the supported message. Do not use a conclusion title for assumed, unresolved, or needs-validation evidence.

## Visual Specification

For every chart or analytical visual, include:

```text
Communication function:
Data structure and metric shape:
Candidate charts:
Selected chart and rationale:
Variety role: tie_breaker | structure_required | not_applicable
Rejected alternatives, when non-obvious:
Population, denominator, coverage, and unit:
Period and temporal scope:
Sample size and uncertainty:
Expected domain and zero/missing treatment:
Colour, sorting, and annotation rules:
Live catalogue checked or fallback note:
Rendered QA status:
```

Do not add a chart to fill space. Use a table, annotated screenshot, diagram, or concise text when it communicates the evidence more honestly.

## Data Blocks

Provide exact plotted values in a structured table for every chart:

```md
| category | value | denominator | coverage | unit | sample_size | lower_bound | upper_bound | metric_id |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
```

Preserve expected zero and missing categories. Distinguish `0`, `not applicable`, `not measured`, and `missing`.

## Recommendations

For every recommendation, include:

```text
Recommendation ID and decision supported:
Supporting claim IDs and posture:
Hypothesis and expected mechanism:
Target population:
Proposed action:
Expected learning or outcome:
Success metrics and guardrails:
Experiment or implementation requirement:
Owner and revisit condition:
```

Frame observational findings as hypotheses, validations, or tests when causal impact is not established.

## Audience And Language

- Write for the audience's analytics literacy.
- Define population and rates before comparing them.
- Use exact business and interface labels where confusion is possible.
- Keep technical source names in methods or notes unless needed.
- Explain caveats as limits on interpretation, not defensive footnotes.
- Prefer direct sentences and concrete verbs.
- Remove generic, inflated, repetitive, or formulaic AI-style wording.
- Keep detailed lineage and formulas in notes or appendices.

Record wording review:

```text
Language and audience:
Terminology source:
Plain-language review:
Fact/interpretation/recommendation separation:
Analytics-naive readback result:
Open wording issues:
```

## Design Direction

Record template, brand assets, fonts, palette, chart palette, highlight rule, footer, screenshot treatment, density, whitespace, and accessibility requirements. If no design system is supplied, use a restrained, readable business presentation without imitating an unavailable brand.

## Final QA Record

```text
Claim set frozen at:
Slide plan approved by:
Data-to-chart check:
Measurement-card check:
Wording and terminology review:
Rendered visual inspection:
Audience-naive review:
Technical review:
Stale dependency check:
Template and brand check:
Caveat check:
Unverified items:
Final status: draft | ready_for_review | approved | approved_with_caveats | rejected | superseded
```

The artifact cannot be approved while an analytical slide depends on a non-approved claim, missing measurement context, incompatible fingerprint, blocking quality check, failed visual decision, or stale artifact.
