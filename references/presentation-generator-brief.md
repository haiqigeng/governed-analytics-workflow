# Presentation Generator Brief Template

Use this template when handing an approved analytics result to a dedicated presentation or design generator. Fill every bracketed field or mark it `Not applicable`.

```md
# Presentation Generator Brief

## Goal
Create a professional PowerPoint-style stakeholder brief for:
- Analysis: [analysis title]
- Audience: [audience]
- Decision supported: [decision]
- Desired tone: executive, concise, evidence-led, design-polished
- Output: widescreen 16:9 presentation
- PPT template or example deck: [path/link or Not provided]
- Brand assets/guidelines: [path/link or Not provided]
- Visualization reference guide/site: The Data Visualisation Catalogue (`https://datavizcatalogue.com/index.html`) unless user provides another guide

## Hard Rules
- Do not invent numbers, sources, findings, or recommendations.
- Use the provided PPT template, brand guide, example deck, or visualization reference when available; if not available, state that default presentation rules were used.
- Keep caveats visible on the relevant slides, not hidden only at the end.
- Do not imply a highlighted subset is the full analysis; state when slides focus on selected values, entities, or segments.
- Keep the full source metric domain in the reproducibility packet or appendix when the analysis uses buckets, stages, statuses, ratings, or ordered dimensions.
- Use one main message per slide.
- Use charts only where they clarify the decision.
- Label chart axes, units, denominators, sample sizes, and date range.
- Label ranking denominators and minimum threshold rules.
- Prefer clean business design over decorative illustration.
- Avoid crowded slides, dark backgrounds, heavy gradients, and excessive color.
- Keep source/caveat text readable.

## Visual Direction
- Palette: neutral background, dark text, one primary accent, one positive accent, one warning/accent color.
- Suggested colors: background #F7F9FC, text #172033, primary #2563EB, positive #16A34A, warning #F59E0B, risk #DC2626, grid #D8DEE9.
- Typography: modern sans serif, strong title hierarchy, body text large enough for presentation mode.
- Layout: generous margins, aligned content, consistent slide footer with date range/source/caveat status.
- Template use: [which master/layouts/assets to use, or default generated layout]
- Chart-selection reference: [Data Visualisation Catalogue function and URL, or user-provided guide]

## Required Deck Structure
1. Big title slide
2. Context page with only the important triage/intake elements
3. Executive summary
4. Recommendation, if required
5+. Detailed analysis slides, one per key result
Final, only when useful. Measurement plan, caveats, appendix, or next step

## Slide Specifications

### Slide 1: Big Title
- Title: [analysis title]
- Subtitle: [one-line business context]
- Metadata: [audience], [date range], [review/caveat status]
- Design: confident title page, minimal text, no chart.

### Slide 2: Analytics Context
- Business question: [question]
- Decision supported: [decision]
- Audience: [audience]
- Scope: [included/excluded pages, users, events, time window]
- Data readiness: [source availability, synthetic/demo/real, known limitations]
- Metric definitions: [main metrics and scope/grain]
- Design: structured context blocks using only decision-relevant triage/intake elements; avoid restating the full workflow checklist.

### Slide 3: Executive Summary
- 3 to 5 key findings:
  - [finding 1 with number]
  - [finding 2 with number]
  - [finding 3 with number]
- Decision implication: [what the findings mean for the decision]
- Confidence/caveat status: [verified/directional/needs validation]
- Completeness note: [whether full metric domain and key breakdowns were checked]
- Design: use KPI tiles only for headline metrics; keep detailed evidence for later slides.

### Slide 4: Recommendation
Use only when the analysis requires or supports a recommendation.
- Recommendation: [recommended action]
- Why now: [evidence-based rationale]
- Expected impact: [metric or decision outcome affected]
- Caveat: [what must remain qualified]
- Design: decision-focused, concise, no dense appendix table.

### Slide 5+: Detailed Analysis Slides
Repeat this section for each result.

#### Slide [n]: [result title]
- Main message: [one sentence]
- Catalogue function: [comparison/proportion/relationship/hierarchy/concept/location/part-to-whole/distribution/how-things-work/process/movement-flow/pattern/range/time/text/reference]
- Chart type: [bar/dot/line/funnel/Sankey/heatmap/table/KPI]
- Why this chart: [comparison/trend/drop-off/flow/pattern/audit detail]
- Alternatives considered: [chart types considered from the catalogue]
- Why alternatives were rejected: [readability, data shape, audience, caveat, or decision-fit reason]
- Data:
  | Dimension | Metric | Value | Notes |
  |---|---:|---:|---|
  | [dimension value] | [metric name] | [value] | [notes] |
- Interpretation: [what the viewer should conclude]
- Caveat: [what this does not prove]
- Completeness: [full domain shown, selected subset explained, or not applicable]
- Design notes: [highlighting, labels, ordering, color use]

### Final Slide: Measurement, Caveats, Or Next Step
Use only when useful after the detailed analysis.
- Measurement plan: [success metrics, guardrail metrics, test duration]
- Next step: [owner/action/timing]
- Caveats: [remaining limitations]
- Design: action-focused, no dense appendix table.

## Source And Review Notes
- Sources used: [source names/paths]
- Presentation inputs: [template, brand guide, example deck, visualization guide]
- Reproducibility packet: [path/link]
- Analysis documentation: [path/link]
- Review status: [approved/approved with caveats/rejected/revise scope]
- Approver: [name/team/date]

## Appendix Data
Include only if the generator supports appendices. Keep tables readable and clearly labeled.
```
