# Presentation Generator Brief

Create this brief only after the analysis contract, evidence, and claim set are reviewed at the required risk level. It is a delivery specification, not a place to perform new analysis.

## Generator Contract

- Use only claims with stakeholder-eligible status in `analysis-manifest.json`.
- Preserve claim wording, evidence posture, population, period, units, fingerprints, and caveats.
- Use only canonical result tables or approved evidence references.
- Do not calculate, interpolate, merge, or infer missing results.
- Do not introduce a new recommendation without decision lineage.
- Apply the user's template, brand guide, language, source-visible wording, and visualization system when supplied.
- Follow `synthesis-and-visualisation.md` for chart selection and rendered QA.

## Brief Header

```text
Analysis ID:
Manifest path:
Output audience:
Decision or learning objective:
Primary problem type:
Secondary problem types:
Risk:
Review status:
Approved claim IDs:
Period and timezone:
Population and grain:
Template/brand inputs:
Language and terminology rules:
Visualization guide:
Live catalogue check status:
Required delivery format:
```

## Narrative Architecture

Do not use a fixed number of slides. Include only sections needed by the audience and evidence.

Typical sequence:

1. Title with analysis name, audience, date, and review posture.
2. Concise context covering the decision, scope, population, sources, and definitions necessary to read the findings.
3. Executive summary with the most decision-relevant approved claims and implications.
4. Analysis sections ordered by the confirmed question tree and problem types.
5. Recommendations or next actions only where evidence supports them.
6. Measurement, monitoring, validation, experiment, caveat, or methods appendix when useful.

For mixed analyses, preserve branch boundaries. A descriptive branch should establish the relevant data before an association, prediction, anomaly, category, or theme branch relies on it.

## Per-Slide Specification

Repeat for every slide:

```text
Slide ID:
Question ID:
Claim IDs:
Slide function: context | finding | comparison | explanation | recommendation | method | appendix
Audience question answered:
Message title:
Evidence posture:
Body copy:
Decision implication:
Required caveats:
Result/data reference:
Metric IDs and fingerprint hashes:
Visual ID:
Visual type:
Source context or screenshot reference:
Speaker notes:
Dependencies:
```

Titles should state the supported message, not merely name a metric. Do not use a conclusion title when evidence posture is `assumed` or `needs_validation`.

## Visual Specification

For slides containing a chart or analytical visual, include:

```text
Communication function:
Data structure and metric shape:
Candidate chart types:
Selected chart:
Why it fits:
Rejected alternatives, when non-obvious:
Population and denominator label:
Units and period:
Sample size and uncertainty:
Expected domain and zero state:
Colour/highlight rule:
Annotation rule:
Live catalogue checked:
Rendered QA status:
```

Do not add a chart merely to fill space. Use a table, annotated screenshot, or concise text when it communicates the evidence more honestly.

## Data Blocks

Provide exact plotted values in a structured table for every chart. Example:

```md
| category | value | denominator | unit | sample_size | lower_bound | upper_bound | metric_id |
| --- | ---: | ---: | --- | ---: | ---: | ---: | --- |
| A | 0.31 | 1240 | rate | 1240 | 0.28 | 0.34 | M1 |
```

Preserve expected zero or missing categories. Distinguish `0`, `not applicable`, `not measured`, and `missing`.

## Recommendations

For every recommendation:

```text
Recommendation ID:
Decision supported:
Supporting claim IDs:
Evidence posture:
Proposed action:
Why now:
Expected learning or outcome:
Success metrics:
Guardrails:
Owner:
Revisit condition:
```

Frame observational findings as hypotheses or tests when causal impact is not established.

## Audience And Language

- Use plain language appropriate to the audience's analytics literacy.
- Define population and rates before comparing them.
- Use exact interface or business labels where confusion is possible.
- Avoid technical source names in main slides unless the audience needs them.
- Explain caveats as limits on interpretation, not defensive footnotes.
- Keep detailed lineage, formulas, and technical mappings in notes or appendices.

## Design Direction

Record:

```text
Template file:
Brand assets:
Approved fonts:
Palette:
Chart palette and highlight colour:
Footer/confidentiality:
Image/screenshot treatment:
Density and whitespace expectations:
Accessibility requirements:
```

If no design system is provided, use a restrained, readable business presentation. Do not imitate a brand that was not supplied.

## Final QA Record

```text
Claim set frozen at:
Slide plan approved by:
Data-to-chart check:
Rendered visual inspection:
Audience-naive review:
Technical review:
Stale dependency check:
Template/brand check:
Caveat check:
Unverified items:
Final status: draft | ready_for_review | approved | approved_with_caveats | rejected | superseded
```

The final artifact cannot be `approved` while any analytical slide depends on a non-approved claim, missing evidence reference, incompatible fingerprint, failed visual decision, or stale artifact.
