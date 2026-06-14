---
name: governed-analytics-workflow
description: Run an interactive, governed analytics workflow for business, product, marketing, web, revenue, or operations analysis. Use when an AI agent needs to turn a question into traceable analytics work with combined triage/intake, framing, data readiness checks, source mapping, internal bounded work modes, reproducible evidence, human review, PowerPoint brief outputs, presentation-generator briefs, per-analysis documentation, and durable context updates. Optimized for Codex, Claude Code, Gemini, and other coding or analysis agents.
---

# Governed Analytics Workflow

Use this skill to run analytics work as an interactive, reviewable process. AI agents produce evidence, checks, drafts, and packets; humans approve meaning, risk, and decisions.

## Operating Rules

- Keep internal checklists private; show only user-facing information that helps the user answer, decide, or review.
- At launch, show the user-facing workflow checklist before `# Step 1: Triage And Intake`; keep checklist lines consecutive with no blank lines between bullets.
- Ask the next necessary question or small group of related questions; do not hide important missing fields.
- After the launch checklist, and in every non-launch workflow reply, start the working section with the current step marker: `# Step N: Step Title`, then add `Status:` and `Decision needed:` only when useful.
- Make each reply concise: confirmed information, useful gaps, suggested defaults when helpful, and next question(s).
- Prefer compact checklists over repeated explanatory paragraphs.
- Prefer conversation-first summaries for user decisions; keep complex artifacts in files for audit, but do not make the user open files to understand the current result, caveat, or decision needed.
- Do not use a visible `Next question:` field; ask the next question naturally as the final sentence.
- Scale rigor to risk: lightweight for low-risk questions, full governance for high-risk decisions.
- Prefer structured artifacts over prose-only answers.
- Keep assumptions labeled until reviewed.
- Do not publish a claim unless it has evidence, lineage, and caveat status.
- Generate a reproducibility packet before human approval.
- Document each delivered analysis in its own analysis folder for future reuse, recheck, and change history.
- Give each artifact a clear status line and maintain an artifact index when multiple files are created.
- Store durable context only after review.
- If data access is unavailable, create a readiness assessment and proposed plan instead of fabricating results.

## Core Terms

- Metric/dimension scope, also called grain: the level one row, metric, dimension value, or claim describes. Examples: event, session, user, page, form instance, submission, account.
- Lineage: the trace from a claim back to its source fields, filters, transformations, query/notebook, output table, and caveats.
- Source mapping: the process of matching desired business metrics to actual tables, events, fields, dimensions, or derived logic in the available data.

## Agent Compatibility

Use the local equivalent of each operation.

- Codex: inspect files, run commands, edit notebooks/scripts, and create artifacts in the repo.
- Claude Code: read files, ask concise clarifying questions, propose patches or files, and keep evidence linked.
- Gemini or other agents: use available query/data tools, produce structured outputs, and pause at review gates.

When a tool is unavailable, keep the artifact format and mark the unavailable item explicitly.

## Start Behavior

When invoked, do not produce detailed instructions for every step. First, read the user's request and show the full workflow checklist once. The checklist must appear before `# Step 1: Triage And Intake`, not under it. Keep bullets consecutive with no blank lines; if the host renderer adds too much vertical space to checkbox bullets, use a compact plain-text checklist instead.

```md
# Workflow Checklist
- [ ] 1. Triage and intake (current)
- [ ] 2. Frame scope and metrics
- [ ] 3. Check data readiness
- [ ] 4. Draft analysis plan
- [ ] 5. Execute bounded work
- [ ] 6. Validate and quality review
- [ ] 7. Generate reproducibility packet
- [ ] 8. Ask for human approval
- [ ] 9. Produce stakeholder output
- [ ] 10. Document delivery and analysis changes
- [ ] 11. Update durable context
- [ ] 12. Define follow-up monitoring or experiment
```

Then show the current step title and a short user-facing triage and intake. Do not repeat the roadmap or checklist content inside Step 1.

```md
# Step 1: Triage And Intake

Business question:
Decision to support:
Likely risk:
Audience:
Time window:
Expected output:
Data/context:
```

If important fields are missing, suggest reasonable defaults and ask the user to confirm or change them. Example: "I suggest marketing team as the audience, a PowerPoint brief as the output, and no deadline specified. Should I use these defaults?"

If the expected output includes a PowerPoint, deck, or stakeholder brief, ask whether the user has a PPT template, brand guidelines, example deck, logo/assets, preferred chart style, or visualization reference site to follow. If none are provided, use the default presentation rules and label that as an assumption.

Then ask one next question or one small group of related questions as ordinary prose after the triage fields. Do not introduce it with `Next question:` and do not list the same missing item both as a gap and as the question. If the request already includes enough context, continue to the next workflow step instead of asking.

For low-risk descriptive questions, combine steps where sensible, but still preserve source, metric, and caveat information. For medium or high-risk work, keep the plan approval, reproducibility packet, and human review gates.

Maintain known, unknown, assumed, not-applicable, and next-question fields internally. Do not expose that internal status by default. In conversation, show only the launch checklist once, the current step marker, confirmed information, missing user decisions, suggested defaults, and next question(s) when useful. Omit empty or irrelevant sections. Never list internal process instructions such as "I should run the workflow" or "I should show known/unknown fields."

## Interaction Pattern

Proceed in this order:

1. Triage and intake.
2. Frame scope and metrics.
3. Check data readiness.
4. Draft analysis plan.
5. Execute bounded work.
6. Validate and quality review.
7. Generate reproducibility packet.
8. Ask for human approval.
9. Produce stakeholder output.
10. Document delivery and analysis changes.
11. Update durable context.
12. Define follow-up monitoring or experiment.

Use these exact step names in the user-facing step marker. When a step is complete, move the marker forward in the next workflow reply.

Create a stable `analysis_id` when artifacts are produced, such as `2026-06-14-contact-form-usage`. Store run artifacts under `analyses/<analysis_id>/` unless the user gives another location.

Ask concise grouped questions at each gate. Example:

```text
I can proceed, but the data only supports a directional answer because section impressions are missing. Should I continue with caveats or switch to a tracking-readiness recommendation?
```

## 1. Triage And Intake

Create or update the intake internally:

```md
# Analytics Intake

Business question:
Decision supported:
Audience:
Deadline:
Risk:
Time window:
Expected output:
Known context:
Presentation inputs, if needed:
```

Classify:

```text
Low risk: descriptive answer, little consequence if wrong.
Medium risk: informs prioritization, design, campaign, or team decision.
High risk: affects budget, customer commitments, compliance, public reporting, compensation, or executive decisions.
```

Track all fields above internally. Show missing fields only when they require user input or affect the analysis. For low-uncertainty fields, propose defaults and ask the user to confirm or change them.

For vague requests, propose a decision frame and ask the user to confirm it.

## 2. Frame The Analysis

Define analysis scope, time window, inclusion/exclusion rules, metric/dimension scope (grain), metrics, segments, caveats, and definition of done.

Example:

```md
# Analysis Framing

Population:
Sessions on URLs matching /programmes/*.

Exclusions:
Thank-you, application confirmation, staging, and test URLs.

Time window:
Last 28 complete days.

Metric/dimension scope (grain):
session_id + programme_page_url.

Metrics:
max_scroll_depth, reached_25_pct, reached_50_pct, reached_75_pct, reached_90_pct, cta_click_rate.

Segments:
device category, traffic channel, programme page.

Breakdowns to consider:
entity, geography, channel, cohort, time, device, product/category, top/bottom performers.

Definition of done:
We can say whether key lower-page content is likely receiving limited exposure and what should be tested next.
```

If the user does not know the metric/dimension scope, propose options and explain the consequence. Example: form analysis can be event-level for field interactions, session-level for abandonments, and submission-level for completed contacts.

Before finalizing framing, propose decision-relevant breakdowns instead of only the most obvious aggregate. Default candidates are entity/item, geography, channel/source, cohort, time trend, device/platform, product/category, and top/bottom rankings. Keep only breakdowns that are available, stable enough, and useful for the decision.

## 3. Check Data Readiness

Verify source tables/files, event names, identifiers, page taxonomy, metric definitions, date/timezone logic, freshness, known tracking gaps, and PII/access constraints.

Return:

```md
# Readiness Assessment

Status:
Ready | Partial | Not ready

Available sources:
Missing or weak sources:
Metric caveats:
Recommended next step:
```

Potential metrics are only hypotheses until mapped to actual source fields or derived logic. Create a metric-source mapping.

For every derived metric, specify source grain, calculation grain, numerator, denominator, and deduplication rule. Never calculate a rate by dividing raw event grain directly by visit, visitor, account, or form-instance grain. Normalize to one calculation grain first. Use event-count divided by visit-count only when the metric is explicitly an intensity metric, such as average clicks per visit.

For threshold, stage, bucket, funnel, status, rating, or ordered-dimension metrics, explicitly define the baseline population and include all expected source values in the base result table. Stakeholder outputs may highlight a subset, but the reproducibility packet must show the full domain or explain why values were excluded.

For ranking outputs, rank by normalized rates or decision metrics after applying a minimum denominator threshold. Do not rank by raw volume unless the business question is explicitly about volume.

```md
| Logical metric | Source event/field | Direct or derived | Source grain | Calculation grain | Numerator | Denominator | Deduplication rule | Availability | Caveat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| form_start_rate | first field_focus after form_view | Derived | event | session + form | distinct session + form with start | distinct session + form with view | one start per session + form | Partial | Depends on field tracking |
| submit_success_rate | form_submit_success | Derived | event | form instance | form instances with success | started form instances | one success per form instance | Ready | Denominator must be approved |
| error_presence_rate | form_validation_error | Derived | event | form instance | form instances with at least one error | started form instances | one error flag per form instance | Partial | Field-level errors may be missing |
```

If a dimension or metric does not exist directly, define a derivation recipe and label it `Derived`. If it cannot be derived safely, label it `Unavailable` and recommend tracking changes.

Example:

```md
Status:
Partial

Available sources:
page_view, scroll_25, scroll_50, scroll_75, scroll_90, cta_click

Missing or weak sources:
No section-level impression event.

Metric caveats:
Scroll depth approximates exposure; it does not prove reading.

Recommended next step:
Run directional scroll-depth analysis and recommend section-impression tracking for future work.
```

If readiness is poor and risk is medium or high, stop and ask whether to improve tracking, narrow the question, or proceed with a caveated directional analysis.

## 4. Draft The Analysis Plan

Create a short plan:

```md
# Analysis Plan

Question:
Approved scope:
Queries or operations:
Metrics:
Segments:
Breakdowns and comparisons:
Metric-source mapping with source grain, calculation grain, numerator, denominator, and deduplication rule:
Validation checks:
Expected artifacts:
Caveats to preserve:
Presentation inputs:
```

Prefer these artifact names inside `analyses/<analysis_id>/` when creating files:

```text
analytics-intake.md
analysis-framing.md
readiness-assessment.md
analysis-plan.md
worker-result-packets.md
quality-review.md
reproducibility-packet.md
stakeholder-brief.pptx
presentation-generator-brief.md
analysis-documentation.md
analysis-changelog.md
decision-log-entry.md
```

Each artifact should start with a status value: `Draft`, `Ready for review`, `Approved`, `Approved with caveats`, `Rejected`, or `Superseded`.

When three or more artifacts are created, maintain an artifact index in `analysis-documentation.md`:

```md
| Artifact | Purpose | Status | Review state |
| --- | --- | --- | --- |
| analysis-plan.md | Planned queries, metrics, caveats | Ready for review | Awaiting user approval |
```

For medium/high-risk work, ask:

```text
Please review this plan before I run or write the analysis. Are the scope, metrics, and caveats correct?
```

## 5. Execute With Bounded Work

Use these as internal work modes. If using one agent, simulate them sequentially. Do not expose role handoffs to the user unless asked; show clean artifacts, review points, and final outputs instead.

```text
Data profiler: inspect schemas, samples, row counts, freshness, and anomalies.
Execution worker: write/run queries or transformations; return code, results, row counts, caveats.
Readiness checker: validate source compatibility, metric definitions, and metric/dimension scope.
Quality reviewer: check unsupported claims, missing caveats, stale context, wrong filters, and causal overreach.
Writing worker: draft stakeholder language using only reviewed result packets.
Presentation worker: turn approved findings into a professional deck with charts, tables, caveats, and concise slide text.
Orchestrator: maintain context, route tasks, ask humans at gates, assemble artifacts.
```

Worker outputs must be structured:

```json
{
  "task": "",
  "source_refs": [],
  "operations": [],
  "result_refs": [],
  "key_results": {},
  "row_counts": {},
  "assumptions": [],
  "caveats": [],
  "status": "draft"
}
```

## 6. Validate And Quality Review

Check:

- final numbers exist in source results
- date ranges are consistent
- filters match framing
- joins do not duplicate rows
- metric/dimension scope is correct
- expected metric buckets, stages, statuses, categories, or domain values are all present, or omissions are explained
- denominator, baseline population, and zero/start state are explicit for every rate or funnel metric
- sample sizes are sufficient
- rankings use normalized metrics with minimum denominator thresholds
- segments do not hide key differences
- decision-relevant breakdowns were considered, and unavailable or rejected breakdowns are documented
- assumptions remain labeled
- caveats are carried forward
- causal language is removed unless causal design supports it
- every claim maps to evidence

Reject unsupported language:

```text
Users do not care about fees.
```

Use supported language:

```text
Only 31% of sessions reached the approximate Fees section, suggesting limited measured exposure.
```

## 7. Generate The Reproducibility Packet

Create this before human review:

```md
# Reproducibility Packet

Analysis ID:
Business question:
Decision supported:
Risk:
Time period and timezone:
Included population:
Excluded population:
Source tables or files:
Relevant fields:
Metric definitions:
Metric-source mapping:
Artifact index:
Queries, notebooks, scripts, or dashboard links:
Output tables or files:
Row counts:
Validation checks:
Sample anonymized rows, if allowed:
Claim-to-evidence map:
Assumptions:
Caveats:
PII or access notes:
Reviewer instructions:
```

Use claim-to-evidence mapping:

```md
Claim:
31% of programme-page sessions reached 75% scroll depth.

Evidence:
Output table analytics_sandbox.programme_scroll_result_2026_06_13, row all_devices, column reached_75_pct.

Calculation:
COUNTIF(max_scroll_depth >= 75) / COUNT(*)

Caveat:
75% scroll depth approximates lower-page exposure but does not prove reading.
```

Raw data guidance:

- Link to access-controlled source data.
- Include exact queries or transformation code.
- Include anonymized sample rows when useful.
- Mask or hash user identifiers unless authorized raw rows are required.
- Prefer reproducible output tables over personal-data exports.

## 8. Human Review Gate

Ask for a decision:

```text
Please review the reproducibility packet and choose: Approve, Approve with caveats, Reject, or Revise scope.
```

Reviewer checks:

- Is the business question framed correctly?
- Are the sources, filters, and exclusions appropriate?
- Is the metric/dimension scope correct?
- Can the key numbers be recreated?
- Are claims proportional to evidence?
- Are caveats visible enough?
- Is the recommended action justified?

Do not mark output as trusted until approved.

## 9. Produce Stakeholder Output

Separate facts, interpretation, recommendation, and caveats. When the requested output is a brief, read `references/presentation-generator-brief.md` and create `presentation-generator-brief.md` with slide text, data tables, chart choices, design rules, caveats, and source references. Use it as the handoff for external deck tools and as the specification for any `.pptx` created locally.

When the final artifact should be a brief, default to an actual PowerPoint deck (`.pptx`) unless the user asks for another format. Use professional slide design, concise text, and visual presentation of the data. If the environment cannot create a professional `.pptx`, state the limitation and provide the presentation-generator brief as the primary deliverable.

Before generating any `.pptx`, confirm or record whether there is a user-provided PPT template, brand guide, example deck, logo/assets, preferred chart style, or visualization-reference site. Use provided assets and references when available. If none are available, state that the default deck design and chart-selection rules are being used.

When the user provides a visualization guide, website, or visual vocabulary, use it as the chart-selection reference and cite or name it in `presentation-generator-brief.md`. If the user previously mentioned such a guide but the URL or file is not in current context, ask for it instead of silently falling back to generic chart rules.

Before producing stakeholder output, run a final presentation-readiness check: full metric domains are represented in source tables, selected slide highlights do not imply omitted values do not exist, caveats are visible on relevant slides, and recommendations are separated from verified facts.

```md
# Stakeholder Brief Deck

Required slides:
1. Big title slide with analysis name, audience, date, and caveat status
2. Context page with the important triage/intake elements only: business question, decision supported, audience, scope/time window, source/readiness, key metric definitions, and caveat status
3. Executive summary with 3-5 key findings and the decision implication
4. Recommendation slide, if the analysis requires or supports a recommendation
5+. Detailed analysis pages according to results, one message per slide
Final, only when useful. Measurement plan, caveats, appendix, or next step
```

Choose visualizations by communication need: funnel/Sankey for process flow or drop-off; bar or dot plot for categorical comparison; line chart for time trend; heatmap for two-dimensional patterns; table only for precise audit detail; KPI cards only for a few headline numbers. Avoid decorative or complex charts when a simpler comparison is clearer. Use a consistent, restrained palette; highlight only the metric or segment that matters; label axes, denominators, sample sizes, and caveats.

When source context matters for interpretation, such as page layout, product UX, dashboard screens, maps, or operational workflows, preserve recognizable source context in stakeholder visuals where permitted. Prefer annotated screenshots, crawl captures, or workflow images over abstract charts alone.

## 10. Document Delivery

After every delivered analysis, create or update human-readable documentation so a future analyst can reuse or recheck the work without reading the conversation.

Documentation is per analysis, not a single global file. Store it with that run's artifacts, normally as `analyses/<analysis_id>/analysis-documentation.md` and `analyses/<analysis_id>/analysis-changelog.md`. Use a central index only to point to per-analysis folders.

Include: question, decision, audience, owner, date range, delivery date, final outputs and paths, sources, queries/code, filters, metric definitions, source-mapping notes, key findings, caveats, review status, approver, rejected claims, and superseded claims.

Include an artifact index listing each file, purpose, status, and review state.

Include an `analysis-changelog.md` section or file. Record material changes made during the analysis: scope changes, source changes, metric or dimension definition changes, query/filter changes, assumption changes, output changes, why they changed, who approved them, and when. If nothing changed after plan approval, write: `Analysis changelog: no material changes after approved plan.`

When user feedback or quality review finds a method flaw after output is created, mark affected claims and artifacts as `Superseded`, create or regenerate the corrected artifact, and explain the correction in conversation.

## 11. Update Durable Context

Update durable context only after review.

Store final decision, reviewed findings, metric definitions, source caveats, excluded interpretations, owner, review date, superseded facts, and the `analysis_id`. Keep one canonical home per fact; when possible, store pointers to the per-analysis documentation instead of duplicating definitions across files.

Example:

```md
# Decision Log Entry

Date:
Decision:
Evidence:
Valid use:
Do not use for:
Status:
```

## 12. Follow Up

For recommendations, propose decision owner, next action, success metrics, experiment or monitoring plan, and revisit date.

Example:

```md
Next action:
Run an A/B test with Fees, Careers, and CTA summary moved above detailed curriculum on mobile.

Success metrics:
CTA click rate, application starts, form completion rate, scroll to key sections.

Revisit:
After two complete weeks or when minimum sample size is reached.
```

## Claim Labels

Use:

```text
Verified: directly supported by reviewed data.
Directional: supported but limited by caveats.
Assumed: necessary assumption, not independently verified.
Needs validation: plausible but not ready for decision-making.
Rejected: checked and found unsupported.
Superseded: previously true or used, now replaced.
```

For final analytics outputs, include at minimum: question, decision supported, date range, data sources, metrics, findings, caveats, recommendation or next step, reproducibility reference, and review status.

## Failure Modes

Guard against:

- treating scroll depth, clicks, or engagement as intent without evidence
- mixing events, sessions, users, and pages
- mixing source grains and calculation grains in rate metrics
- omitting expected source buckets, stages, statuses, or categories from base outputs
- using a highlighted subset in slides as if it were the complete analysis
- leaving denominator thresholds unspecified for top/bottom rankings
- ranking entities by raw count when the decision requires rates or normalized metrics
- reusing stale metric definitions
- duplicating canonical facts across memory files
- hiding caveats in appendices
- making the user infer the current workflow step
- letting the same agent create and approve its own work
- publishing polished prose before evidence review
- forcing the user to open audit files to understand the current answer or decision
- updating durable context with unreviewed draft findings
