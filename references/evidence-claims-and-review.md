# Evidence, Claims, And Review

Use this reference to govern source roles, metric compatibility, bounded execution, claim promotion, independent review, artifact freshness, and durable context.

## Source Authority

Create one record per source:

```json
{
  "source_id": "S1",
  "name": "",
  "owner": "",
  "authority": "canonical | supporting | illustrative | experimental",
  "source_grain": "",
  "coverage": "",
  "freshness": {"valid_as_of": "", "revalidate_after": ""},
  "join_keys": [],
  "joinability": "direct | aggregate_only | none | unknown",
  "allowed_uses": [],
  "forbidden_uses": [],
  "access_and_pii": "",
  "caveats": []
}
```

Multiple sources do not become compatible because they describe the same topic. Never divide, join, or compare across sources until grain, population, period, identifiers, and authority permit it.

## Semantic Validation

Technical availability is not business validity. For every important event, field, status, interaction, or category:

1. Inspect the source dictionary and observed values.
2. Verify visible or operational behaviour when relevant.
3. Map technical signals to one business/user outcome.
4. Identify multiple signals for the same outcome and one signal with multiple meanings.
5. Preserve technical mappings in evidence; use recognizable business wording in stakeholder output.

Browser inspection may establish wording, interaction result, page geometry, or instrumentation behaviour. It cannot establish aggregate reach, prevalence, or effect without population evidence.

## Definition Fingerprints

Every decision metric needs:

```json
{
  "population": "",
  "calculation_grain": "",
  "time_window": {"start": "", "end": "", "timezone": ""},
  "scope": {},
  "filters": [],
  "numerator": "",
  "denominator": "",
  "deduplication": "",
  "source_query_ref": "",
  "run_date": ""
}
```

Add `expected_domain` and `observed_domain` for buckets, stages, statuses, ratings, categories, or ordered values. Include zero/start states when part of the population. Add `metric_shape` such as `exclusive_distribution`, `cumulative_reach`, `rate`, `intensity`, `trend`, or `model_metric`.

Fingerprint compatibility is required before comparison. At minimum align population, calculation grain, time window, scope, filters that define eligibility, and outcome definition. Explain intentional differences rather than hiding them.

## Representativeness Gate

Before generalizing sampled evidence, record:

```text
target population
sampling frame and selection method
sample size and coverage
important variants or archetypes
devices, periods, or contexts represented
known exclusions
claim scope supported by the sample
```

Use `illustrative` when evidence demonstrates a possible behaviour but cannot estimate prevalence. Use `directional` when coverage supports a cautious pattern but not a population estimate. Never multiply a directional geometry/sample observation by an aggregate rate to manufacture precision.

## Availability And Temporal Eligibility

- Use eligible denominators for optional content, products, features, or journeys.
- If availability cannot be measured, report raw usage and the denominator limitation; do not call it an interaction rate for all entities.
- Prove event order before describing behaviour as pre-outcome.
- Exclude or separately describe outcomes that precede the required exposure.
- Keep full-period descriptive behaviour separate from pre-outcome contribution-oriented comparisons.

## Bounded Work Packets

Task packet:

```json
{
  "task_id": "T1",
  "question_ids": ["Q1"],
  "objective": "",
  "allowed_source_ids": ["S1"],
  "allowed_operations": [],
  "required_output_schema": {},
  "validation_rules": [],
  "prohibited_actions": ["publish", "approve_claim", "update_durable_context"]
}
```

Result packet:

```json
{
  "task_id": "T1",
  "question_ids": ["Q1"],
  "source_refs": [],
  "operations": [],
  "result_refs": [],
  "row_counts": {},
  "metric_ids": [],
  "candidate_claims": [],
  "assumptions": [],
  "caveats": [],
  "validation_results": [],
  "status": "draft"
}
```

Workers cannot publish, approve their own claims, change source-of-truth definitions, or update durable context.

## Claim Lifecycle

```text
observation: captured result not yet interpreted or validated
candidate: potentially useful statement awaiting validation
validated: evidence, fingerprint, and claim posture passed review
approved: authorized for the intended stakeholder use
rejected: checked and unsupported or misleading
superseded: replaced by a newer definition, result, or review decision
```

Claim record:

```json
{
  "claim_id": "C1",
  "question_ids": ["Q1"],
  "statement": "",
  "status": "candidate",
  "evidence_posture": "verified | directional | assumed | needs_validation",
  "evidence_refs": [],
  "metric_ids": [],
  "valid_as_of": "",
  "caveats": [],
  "alternative_explanations": [],
  "owner": "",
  "approved_by": "",
  "approved_at": "",
  "supersedes": []
}
```

Tag evidence posture when the claim enters the system, not only during final review. More source references do not automatically increase confidence; source authority, compatibility, design, and directness matter.

## Promotion Gates

| Transition | Minimum requirement |
| --- | --- |
| Observation -> Candidate | Decision relevance and question linkage |
| Candidate -> Validated | Evidence refs, compatible fingerprints, validation results, caveats, claim ceiling |
| Validated -> Approved | Intended audience/use, risk-appropriate reviewer, visible caveats |
| Any active state -> Superseded | Replacement pointer and change reason |

`Light` low-risk work may promote validated claims without a separate human meeting when all automated/manual checks pass and intended use remains low consequence. High-risk, externally durable, public, compliance, compensation, budget, or executive claims require human approval.

## Quality Review

### Technical Lens

- code/query correctness and reproducibility;
- source authority and freshness;
- filters, joins, grain, time, and deduplication;
- full domains, zero states, denominators, and missingness;
- sample size, uncertainty, model/type-specific validation;
- semantic and temporal validity;
- claim-to-evidence traceability.

### Audience Lens

- understandable population, measure, unit, and period;
- no unexplained percentages or technical labels;
- caveats visible where interpretation occurs;
- chart and wording do not imply a stronger claim;
- decision implication is clear without hiding uncertainty.

### Domain-Aware, Analysis-Naive Lens

- assumptions a close analyst may have stopped noticing;
- mismatch with business process or interface behaviour;
- plausible alternative explanations;
- missing context a knowledgeable new reader would need.

Prefer an independent reviewer or clean-context pass. Supply the contract, evidence packet, claim register, and output brief. Do not bias the reviewer with the intended verdict.

## Artifact Dependencies And Staleness

Artifacts declare dependencies on question, metric, claim, visual, and evidence IDs plus the current fingerprint hashes of decision metrics. When an upstream definition or status changes:

1. mark dependent claims `needs_validation` or `superseded` as appropriate;
2. mark dependent artifacts `stale`;
3. regenerate only affected outputs;
4. review before restoring `active` status.

Keep one active artifact per purpose. Retain old versions only when they support audit or comparison, with explicit superseded status.

## Versioned Durable Context

Store only reviewed knowledge. Each update records:

```text
context key
old value or definition
new value or definition
validity/data window
run date
source analysis and claim IDs
owner and reviewer
change reason
status
```

Prefer pointers to the canonical analysis manifest. Do not copy definitions into several files that can drift independently.

## Privacy And Access

- Keep raw sources access-controlled.
- Use anonymized examples unless authorized identifiers are necessary.
- Never place credentials or secrets in manifests, evidence, logs, decks, repositories, or durable context.
- Record access limitations and evidence not inspected.
- Run the portability/secret scan before sharing or publishing artifacts.
