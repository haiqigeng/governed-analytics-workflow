# Synthesis And Visualisation

Use this reference after evidence review. Synthesis answers the confirmed question tree with approved claims; it does not rescue weak evidence through polished language or visuals.

## Narrative Contract

Build from:

```text
decision or learning objective
-> core question
-> approved claims
-> interpretation within the evidence ceiling
-> recommendation, next action, or remaining uncertainty
```

Do not reproduce the request's metric order. Do not force every analysis into the same deck structure. Let problem type, evidence, audience, and decision determine the sequence.

For medium/high-risk work, freeze these before generating a deck:

- approved claim set and evidence posture;
- narrative order and one message per slide;
- selected supporting tables or figures;
- caveats that must appear on each slide;
- presentation template, brand, language, and audience conventions.

Material changes after freeze mark affected slides and artifacts stale.

## Problem-Type Narrative Biases

| Type | Stakeholder narrative should normally establish |
| --- | --- |
| Make predictions | Decision context, baseline, performance/uncertainty, threshold trade-offs, use limits |
| Categorise things | Category purpose, definitions, coverage, quality/stability, action by class |
| Spot unusual | Expected baseline, detected departures, magnitude/context, investigation priority |
| Identify themes | Corpus/coverage, themes, evidence and exceptions, implications without false prevalence |
| Discover connections | Compatible population, relationship magnitude, robustness, alternatives, no unsupported cause |
| Find patterns | Complete descriptive foundation, important segments/trends, interpretation, next questions/actions |

Mixed analyses should preserve branch boundaries. Do not use one branch's evidence posture to strengthen another.

## Chart-Selection Gate

The default external guide is The Data Visualisation Catalogue:

- Main catalogue: `https://datavizcatalogue.com/index.html`
- Search by function: `https://datavizcatalogue.com/search.html`

For every stakeholder analysis containing charts:

1. Write the exact slide question and approved claim.
2. Identify data structure: variable types, ordering, exclusivity, cumulative/stage logic, time, geography, number of categories/series, sample size, and uncertainty.
3. Select the communication function.
4. If internet access is available, consult the live catalogue once for every distinct function used in the analysis. Open individual chart pages for unfamiliar, complex, or ambiguous choices.
5. Shortlist valid candidates and reject those that misrepresent the data.
6. Choose the simplest valid chart for the audience.
7. Record the decision and required labels.
8. Render and visually inspect the result.

If the live catalogue is unavailable, use this reference and record `live_catalogue_checked: false`. A user-provided visualization system overrides the default catalogue but not statistical integrity or QA.

## Function Map

| Communication need | Function | Common stakeholder choices |
| --- | --- | --- |
| Compare categories or groups | Comparison | Sorted bar, grouped bar, dot plot, small multiples |
| Show a distribution | Distribution | Histogram, box plot, density, ordered exclusive bars |
| Show change over time | Data over time | Line, small multiples, indexed line, area when magnitude matters |
| Show association | Relationship | Scatterplot, heatmap, grouped estimates with intervals |
| Show part of a whole | Proportion | 100% stacked bar, simple stacked bar; pie/donut only for very few parts |
| Show cumulative stage reach | Process or ordered progression | Stepped bars, stage bars, line; funnel only when stages are genuinely nested/sequential |
| Show movement or flow | Movement/flow | Sankey or flow diagram only when paths/transfer are the message |
| Show range or uncertainty | Range | Interval plot, error bars, box plot, forecast band |
| Show hierarchy | Hierarchy | Tree or treemap when nesting is essential |
| Show location | Location | Choropleth, dot/bubble map with normalized measures where required |
| Show text themes | Analysing text | Ranked bars, theme matrix, evidence excerpts; not a standalone word cloud |
| Explain an interface or spatial context | How things work/reference | Annotated screenshot, page map, table, process diagram |

Specialist analytical diagnostics such as calibration, lift, precision-recall, residual, control, or survival plots may override catalogue choices. Explain their use and provide a simpler stakeholder interpretation when needed.

## Visual Decision Record

```json
{
  "visual_id": "V1",
  "claim_ids": ["C1"],
  "question_id": "Q1",
  "result_ref": "",
  "message": "",
  "communication_function": "distribution",
  "data_structure": {
    "metric_shape": "exclusive_distribution",
    "ordered": true,
    "categories_overlap": false,
    "series_count": 1
  },
  "candidate_charts": ["ordered_bar", "histogram"],
  "selected_chart": "ordered_bar",
  "rejected_alternatives": [],
  "required_labels": ["population", "denominator", "period"],
  "live_catalogue_checked": true,
  "qa_status": "pending"
}
```

Detailed rejected-alternative prose is required only for a non-obvious, complex, or disputed choice.

## Hard Rejection Rules

Reject a visual when it:

- presents mutually exclusive classes as sequential funnel stages;
- uses a line to imply continuity between unordered categories;
- uses part-to-whole encoding for overlapping categories;
- omits an expected zero/start state or source-domain value;
- displays a percentage without population and denominator meaning;
- compares incompatible fingerprints, periods, grains, or axes;
- ranks raw volume when the question requires normalized performance;
- hides small samples or uncertainty that changes interpretation;
- implies causality through title, arrows, ordering, or annotation without a causal design;
- uses a complex radial, network, Sankey, treemap, or dual-axis chart when a simpler comparison is clearer;
- turns illustrative browser/qualitative evidence into a population percentage;
- cannot be read by the target audience at rendered size.

## Wording And Source Context

- Use exact user-visible, operational, or approved business vocabulary in main outputs.
- Keep event, field, table, model, and technical taxonomy names in methodology or appendices.
- Define analytical terms in plain language for non-expert audiences.
- Do not call a proxy direct visibility, attention, satisfaction, intent, value, or contribution unless the measurement supports it.
- When interface, document, dashboard, spatial, or workflow context matters, use annotated source views where permitted.

## Presentation Generator Boundary

The presentation worker may:

- select and order approved claims;
- simplify language without changing meaning;
- choose and render approved visual designs;
- apply a template, brand, and audience style;
- surface caveats and decision implications.

It may not:

- calculate or merge new analytical results;
- choose a different population, denominator, period, or grain;
- promote a directional claim to verified;
- turn association into causality;
- omit required caveats;
- invent explanations or recommendations without claim lineage.

## Rendered Output QA

Inspect slides or equivalent rendered pages, not only source code or XML. Check:

- slide order and one-message discipline;
- text fit, font size, contrast, and no overlap;
- title accuracy and evidence posture;
- axes, units, baselines, sorting, periods, sample sizes, and denominators;
- full expected domains and zero states;
- legend and label clarity;
- caveats placed beside the claim they constrain;
- template/brand application;
- source screenshots readable and correctly framed;
- no stale claim, result, or fingerprint dependency;
- visual decision record updated to `passed` or `failed` with notes.

If rendering or visual inspection is impossible, state that limitation and do not claim visual QA passed.
