---
name: governed-analytics-workflow
description: Run an interactive, governed analytics workflow for business, product, marketing, web, revenue, or operations analysis. Use when an AI agent needs to turn a question into traceable analytics work with combined triage/intake, framing, data readiness checks, source mapping, internal bounded work modes, reproducible evidence, human review, PowerPoint brief outputs, final documentation, and durable context updates. Optimized for Codex, Claude Code, Gemini, and other coding or analysis agents.
---

# Governed Analytics Workflow

Use this skill to run analytics work as an interactive, reviewable process. AI agents produce evidence, checks, drafts, and packets; humans approve meaning, risk, and decisions.

## Operating Rules

- Keep internal checklists private; show only user-facing information that helps the user answer, decide, or review.
- Ask the next necessary question or small group of related questions; do not hide important missing fields.
- Make each reply concise: current step, confirmed information, useful gaps, suggested defaults when helpful, and next question(s).
- Scale rigor to risk: lightweight for low-risk questions, full governance for high-risk decisions.
- Prefer structured artifacts over prose-only answers.
- Keep assumptions labeled until reviewed.
- Do not publish a claim unless it has evidence, lineage, and caveat status.
- Generate a reproducibility packet before human approval.
- Document each delivered analysis for future reuse, recheck, and change history.
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

When invoked, do not immediately produce the full workflow. First, read the user's request and respond with a short user-facing triage and intake:

```md
# Triage And Intake

Business question:
Decision to support:
Likely risk:
Audience:
Time window:
Expected output:
Data/context:
What I still need:
```

If important fields are missing, suggest reasonable defaults and ask the user to confirm or change them. Example: "I suggest marketing team as the audience, a PowerPoint brief as the output, and no deadline for this test. Should I use these defaults?"

Then ask one next question or one small group of related questions. If the request already includes enough context, continue to the next workflow step instead of asking.

For low-risk descriptive questions, combine steps where sensible, but still preserve source, metric, and caveat information. For medium or high-risk work, keep the plan approval, reproducibility packet, and human review gates.

Maintain known, unknown, assumed, not-applicable, and next-question fields internally. Do not expose that internal status by default. In conversation, show only the current step, confirmed information, missing user decisions, suggested defaults, and next question(s) when useful. Omit empty or irrelevant sections. Never list internal process instructions such as "I should run the workflow" or "I should show known/unknown fields."

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
```

Classify:

```text
Low risk: descriptive answer, little consequence if wrong.
Medium risk: informs prioritization, design, campaign, or team decision.
High risk: affects budget, customer commitments, compliance, public reporting, compensation, or executive decisions.
```

Example:

```text
Question: How far do users scroll on programme pages?
Risk: Medium
Reason: May influence web redesign and CTA placement.
Required rigor: readiness check, plan, reproducibility packet, human review.
```

Track all fields above internally. Show missing fields only when they require user input or affect the analysis. For low-uncertainty fields, propose defaults and ask the user to confirm or change them.

For vague requests, propose a decision frame:

```text
When you say "scrolling on programme pages", I can frame that as: "Should key content or CTAs move higher on the page?" Is that the decision you want to support?
```

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

Definition of done:
We can say whether key lower-page content is likely receiving limited exposure and what should be tested next.
```

If the user does not know the metric/dimension scope, propose options and explain the consequence. Example: form analysis can be event-level for field interactions, session-level for abandonments, and submission-level for completed contacts.

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

Potential metrics are only hypotheses until mapped to actual source fields or derived logic. Create a metric-source mapping:

```md
| Logical metric | Source event/field | Direct or derived | Metric/dimension scope | Required filters/logic | Availability | Caveat |
| --- | --- | --- | --- | --- | --- | --- |
| form_start_rate | first field_focus after form_view | Derived | session + form | form_start / form_view | Partial | Depends on field tracking |
| submit_success_rate | form_submit_success | Direct | form submission | successes / form views or starts | Ready | Denominator must be approved |
| error_rate | form_validation_error | Direct or derived | event/session | errors / starts | Partial | Field-level errors may be missing |
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
Metric-source mapping:
Validation checks:
Expected artifacts:
Caveats to preserve:
```

Prefer these artifact names when creating files:

```text
analytics-intake.md
analysis-framing.md
readiness-assessment.md
analysis-plan.md
worker-result-packets.md
quality-review.md
reproducibility-packet.md
stakeholder-brief.pptx
analysis-documentation.md
analysis-changelog.md
decision-log-entry.md
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
- sample sizes are sufficient
- segments do not hide key differences
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

Separate facts, interpretation, recommendation, and caveats. When the requested output is a brief, default to an actual PowerPoint deck (`.pptx`) unless the user asks for another format. Use professional slide design, concise text, and visual presentation of the data. If the environment cannot create `.pptx`, state the limitation and provide a slide-by-slide specification as fallback.

```md
# Stakeholder Brief Deck

Required slides:
1. Big title slide with analysis name, audience, date, and caveat status
2. Analytics context: business question, decision, scope, source/readiness, metric definitions
3. Executive summary: 3-5 key findings and recommendation
4+. Analysis pages according to results, one message per slide
Final. Recommendation, measurement plan, caveats, and next step
```

Choose visualizations by communication need: funnel/Sankey for process flow or drop-off; bar or dot plot for categorical comparison; line chart for time trend; heatmap for two-dimensional patterns; table only for precise audit detail; KPI cards only for a few headline numbers. Avoid decorative or complex charts when a simpler comparison is clearer. Use a consistent, restrained palette; highlight only the metric or segment that matters; label axes, denominators, sample sizes, and caveats.

## 10. Document Delivery

After every delivered analysis, create or update human-readable documentation so a future analyst can reuse or recheck the work without reading the conversation.

Include: question, decision, audience, owner, date range, delivery date, final outputs and paths, sources, queries/code, filters, metric definitions, source-mapping notes, key findings, caveats, review status, approver, rejected claims, and superseded claims.

Include an `analysis-changelog.md` section or file. Record material changes made during the analysis: scope changes, source changes, metric or dimension definition changes, query/filter changes, assumption changes, output changes, why they changed, who approved them, and when. If nothing changed after plan approval, write: `Analysis changelog: no material changes after approved plan.`

## 11. Update Durable Context

Update durable context only after review.

Store final decision, reviewed findings, metric definitions, source caveats, excluded interpretations, owner, review date, and superseded facts. Keep one canonical home per fact; when possible, store pointers to source artifacts instead of duplicating definitions across files.

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
- reusing stale metric definitions
- duplicating canonical facts across memory files
- hiding caveats in appendices
- letting the same agent create and approve its own work
- publishing polished prose before evidence review
- updating durable context with unreviewed draft findings
