# Needs Discovery And Analysis Contract

Use this reference to locate the real analytical need inside vague, lengthy, metric-led, solution-led, or contradictory information. The question tree is the output of needs discovery, not a substitute for it.

## Adaptive Discovery Router

Choose the least intensive mode that can produce a defensible frame.

| Signal | Light | Standard | Deep |
| --- | --- | --- | --- |
| Decision clarity | Clear | Partly stated | Missing, contradictory, or solution-led |
| Questions | One | Several related | Many mixed or competing questions |
| Sources/stakeholders | One or familiar | Several | Multiple grains, owners, or audiences |
| Consequence of error | Low | Medium | High, public, expensive, or hard to reverse |
| Causal/preferred conclusion | Absent | Possible | Explicit or politically consequential |
| User-facing behaviour | Proceed with concise restatement | Show framing proposal | Show framing proposal and require confirmation before material execution |

Record the mode and triggers internally. Do not expose method names unless they help the user review the frame.

## Request Decomposition

Classify material statements before accepting them:

| Class | Treatment |
| --- | --- |
| Observed fact | Preserve with provenance and freshness status |
| Business objective | Use to infer the decision or learning objective |
| Constraint | Treat as binding when explicit and feasible |
| Hypothesis | Test or preserve as unverified; never promote silently |
| Suggested metric | Evaluate construct, grain, denominator, actionability, and availability |
| Suggested method | Treat as a preference unless methodologically required |
| Suggested solution | Separate from the problem; test the need before endorsing the solution |
| Output preference | Preserve unless it conflicts with evidence or safety |
| Uncertainty | Convert to a question, assumption, or readiness gap |

Prior analyses, dashboards, emails, and stakeholder statements are context. They are not automatically current or correct. Record what was inspected and whether it is authoritative, stale, illustrative, or superseded.

## Decision-Backward Framing

Infer or establish:

```text
decision owner
decision or learning objective
available options or actions
decision deadline or revisit condition
cost of being wrong
what different analytical answers would change
```

Apply the answer-to-action test. If result A and result B would lead to the same action and no meaningful learning difference, the question is probably supporting rather than core.

Some analyses are exploratory and have no immediate decision. State a learning objective and what future decision, measurement, or investigation it should enable. Do not invent a false decision merely to fill a template.

## Conditional Discovery Methods

Use only methods triggered by the request.

### Analytical Laddering

Use when indicators or requested outputs are clearer than their purpose. Ask internally why each measure matters until reaching a decision or learning objective. Ask the user only when the ladder ends in materially different plausible needs.

### Assumption And Hypothesis Mapping

For each important assumption, capture:

```text
statement
source or owner
why it matters
evidence needed
alternative explanations
claim ceiling
status
```

### Alternative Framing

Compare internally:

- `literal`: answer the request as written;
- `inferred`: answer the underlying business need;
- `minimum_useful`: answer only what is necessary for the decision or learning objective.

Recommend one. Show alternatives only when choosing among them materially changes scope, timing, risk, or interpretation.

### Stakeholder And Decision Mapping

Identify requester, decision owner, affected teams, technical reviewer, final audience, and conflicting expectations. The requester may supply useful context without being the analytical or decision authority.

### Evidence-Ceiling Test

State the strongest claim the available design and sources can support. Common reframings include:

| Requested language | Defensible observational language |
| --- | --- |
| causes | is associated with; precedes; differs with |
| contributes | participates in the observed path; is associated with the outcome |
| users value | users use, reach, select, repeat, or report |
| content is seen | threshold reached; element exposed when directly instrumented |
| improvement | observed change; causal improvement only with an adequate design |

### Minimum-Useful-Scope Review

Keep questions and breakdowns that are decision-relevant, feasible, non-duplicative, and interpretable. Park requests whose marginal value does not justify added complexity or false precision.

### Pre-Mortem

For complex or consequential work, imagine the delivered analysis was rejected or caused a poor decision. Convert plausible failure reasons into framing, readiness, validation, or presentation requirements.

## Question Tree

### States

- `draft`: inferred from the request and context;
- `confirmed`: reviewed or accepted for the current risk level;
- `operational`: accepted leaves have source, metric, method, validation, and output mappings.

### Levels

```text
Level 0: decision or learning objective
Level 1: core analytical questions
Level 2: analytical subquestions
Level 3: diagnostic and validation questions
```

Keep the user-facing tree concise. A normal complex analysis usually needs two to four core questions. Operational leaves may be more numerous, but every leaf must earn its place.

### Question Roles

Use:

```text
core
supporting
diagnostic
optional
duplicate
misleading
unavailable
out_of_scope
```

Only `core`, `supporting`, and necessary `diagnostic` leaves normally create execution work. Optional branches require a clear marginal benefit. Preserve excluded items in request coverage so they do not disappear silently.

### Operational Leaf Contract

```json
{
  "question_id": "Q1.2",
  "parent_id": "Q1",
  "text": "",
  "role": "supporting",
  "problem_type": "find_patterns",
  "decision_relevance": "",
  "source_ids": [],
  "metric_ids": [],
  "method": "",
  "validation_rules": [],
  "expected_output": "",
  "status": "confirmed"
}
```

### Request Coverage

Map every material request item to one of:

```text
answered_by_question
supporting_context
parked
rejected
unavailable
superseded
```

Record a reason for every item not answered directly.

Give each stated item a stable ID before mapping it:

```json
{
  "stated_request": [
    {"request_item_id": "R1", "text": "Original request or faithful paraphrase"}
  ],
  "coverage": [
    {
      "request_item_id": "R1",
      "disposition": "answered_by_question",
      "question_ids": ["Q1"],
      "reason": ""
    }
  ]
}
```

## Decision Lineage

Maintain this chain:

```text
business need
-> decision or learning objective
-> question
-> problem type and method
-> evidence
-> claim
-> recommendation or next action
```

Use it to reject:

- a metric with no question;
- a query with no analytical or validation purpose;
- a claim with no evidence;
- a chart with no approved claim;
- a recommendation with no supporting claims;
- an unanswered core question presented as complete.

## User-Facing Framing Proposal

For `Standard` or `Deep` work, show:

```text
What I believe the business needs:
Decision or learning objective:
Proposed core questions:
What I am treating as hypotheses:
What I recommend parking or reframing:
Proposed problem types:
Evidence ceiling:
Decision needed:
```

Prefer one recommended frame. Do not make a non-expert requester choose among technical methods.

## Analysis Contract

The confirmed contract should include:

| Area | Required content |
| --- | --- |
| Purpose | Need, decision/learning objective, owner, audience, deadline |
| Discovery | Mode, triggers, request coverage, assumptions, evidence ceiling |
| Questions | Confirmed tree, primary/secondary problem types, definition of done |
| Scope | Population, exclusions, period, timezone, grain, segments |
| Evidence | Source authority, semantic mapping, representativeness, freshness |
| Metrics | Definitions and fingerprints |
| Methods | Operations, comparisons, problem-type validation, claim limits |
| Delivery | Artifacts, presentation inputs, review and approval gates |

Contract changes that affect population, outcome, grain, source authority, metric definition, problem type, method, or claim ceiling are material. Record them and mark dependent work stale.

## Stop Conditions

Pause before material execution when:

- two plausible framings would support different decisions;
- the decision owner or outcome definition is disputed;
- a high-risk claim exceeds the evidence ceiling;
- required data access, identifiers, or grain are unavailable;
- a mandatory constraint conflicts with a defensible analysis.

Otherwise recommend a reasonable default, label it, and continue.
