---
name: governed-analytics-workflow
description: Run an interactive, governed analytics workflow for business, product, marketing, web, revenue, or operations analysis. Use when an AI agent needs to turn a question into traceable analytics work with risk triage, framing, data readiness checks, bounded agent tasks, reproducible evidence, human review, stakeholder-ready outputs, and durable context updates. Optimized for Codex, Claude Code, Gemini, and other coding or analysis agents.
---

# Governed Analytics Workflow

Use this skill to run analytics work as an interactive, reviewable process. AI agents produce evidence, checks, drafts, and packets; humans approve meaning, risk, and decisions.

## Operating Rules

- Show the current step checklist with answered, unknown, assumed, and not-applicable fields.
- Ask the next necessary question or small group of related questions; do not hide missing fields.
- Scale rigor to risk: lightweight for low-risk questions, full governance for high-risk decisions.
- Prefer structured artifacts over prose-only answers.
- Keep assumptions labeled until reviewed.
- Do not publish a claim unless it has evidence, lineage, and caveat status.
- Generate a reproducibility packet before human approval.
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

When invoked, do not immediately produce the full workflow. First, read the user's request and respond with:

```md
# Triage Snapshot

Business question:
Decision supported:
Likely risk:
Known data/context:
Missing item blocking the next step:
```

Then ask one next question. If the request already includes enough context, continue to the next workflow step instead of asking.

For low-risk descriptive questions, combine steps where sensible, but still preserve source, metric, and caveat information. For medium or high-risk work, keep the plan approval, reproducibility packet, and human review gates.

At every step, use this compact status pattern:

```md
Known:
Unknown:
Assumed:
Not applicable:
Next question(s):
```

## Interaction Pattern

Proceed in this order:

1. Triage risk and decision.
2. Create intake.
3. Frame scope and metrics.
4. Check data readiness.
5. Draft analysis plan.
6. Execute bounded worker tasks.
7. Validate and quality review.
8. Generate reproducibility packet.
9. Ask for human approval.
10. Produce stakeholder output.
11. Update durable context.
12. Define follow-up monitoring or experiment.

Ask one concise question at each gate. Example:

```text
I can proceed, but the data only supports a directional answer because section impressions are missing. Should I continue with caveats or switch to a tracking-readiness recommendation?
```

## 1. Triage Risk

Ask if unclear:

```text
What decision will this analysis support, and what happens if the answer is wrong?
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

## 2. Intake

Create or update:

```md
# Analytics Intake

Business question:
Decision supported:
Audience:
Deadline:
Risk:
Expected output:
Known context:
```

Show all fields above to the user. Mark missing fields as `Unknown` instead of silently turning them into one hidden follow-up.

For vague requests, propose a decision frame:

```text
When you say "scrolling on programme pages", I can frame that as: "Should key content or CTAs move higher on the page?" Is that the decision you want to support?
```

## 3. Frame The Analysis

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

## 4. Check Data Readiness

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

## 5. Draft The Analysis Plan

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
stakeholder-brief.md
decision-log-entry.md
```

For medium/high-risk work, ask:

```text
Please review this plan before I run or write the analysis. Are the scope, metrics, and caveats correct?
```

## 6. Execute With Bounded Workers

If using one agent, simulate these roles sequentially:

```text
Data profiler: inspect schemas, samples, row counts, freshness, and anomalies.
Execution worker: write/run queries or transformations; return code, results, row counts, caveats.
Readiness checker: validate source compatibility, metric definitions, and metric/dimension scope.
Quality reviewer: check unsupported claims, missing caveats, stale context, wrong filters, and causal overreach.
Writing worker: draft stakeholder language using only reviewed result packets.
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

## 7. Validate And Quality Review

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

## 8. Generate The Reproducibility Packet

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

## 9. Human Review Gate

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

## 10. Produce Stakeholder Output

Separate facts, interpretation, recommendation, and caveats.

```md
# Stakeholder Brief

Question:
Short answer:
Verified findings:
Directional findings:
Recommendation:
Evidence:
Caveats:
Next measurement step:
```

Example:

```md
Short answer:
Most programme-page sessions do not reach lower-page content. The median maximum scroll depth was 50%, and 31% of sessions reached 75%.

Recommendation:
Test moving Fees, Careers, and an Apply/Request Info CTA summary higher on mobile programme pages.

Caveat:
Scroll depth does not prove reading; section exposure is inferred from page layout.
```

## 11. Update Durable Context

Update durable context only after review.

Store final decision, reviewed findings, metric definitions, source caveats, excluded interpretations, owner, review date, and superseded facts. Keep one canonical home per fact; when possible, store pointers to source artifacts instead of duplicating definitions across files.

Example:

```md
# Decision Log Entry

Date:
2026-06-13

Decision:
Recommend testing a shorter mobile programme-page layout with key decision content higher on the page.

Evidence:
programme_scroll_2026_06_13

Valid use:
Directional page exposure analysis.

Do not use for:
Causal claims about user interest in lower-page content.

Status:
Reviewed
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
