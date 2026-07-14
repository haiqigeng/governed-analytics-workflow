---
name: governed-analytics-workflow
description: Run an adaptive, governed analytics workflow for vague, metric-led, multi-source, or consequential business, product, marketing, digital, revenue, and operations questions. Use when an AI agent must discover the real decision need, build a question tree, select methods by analytical problem type, verify source semantics and readiness, execute reproducible work, govern claim promotion, and create reviewed stakeholder outputs such as PowerPoint briefs. Designed for Codex, Claude Code, Gemini, and other file- and tool-capable agents.
---

# Governed Analytics Workflow

Turn unclear requests into decision-relevant, reproducible analysis. Treat requesters as authorities on business context and constraints, not automatically on analytical design. Agents may propose framing, methods, interpretations, and actions; humans approve consequential meaning and decisions.

## Non-Negotiable Rules

- Interpret the request before selecting metrics or querying data.
- Treat requested metrics, breakdowns, methods, explanations, and charts as candidates unless they are explicit constraints.
- Build a question tree and map every operation, claim, and stakeholder visual to it.
- Use one primary analytical problem type and secondary types only for distinct subquestions.
- Scale ceremony to ambiguity and risk. Do not require approval for every exploratory read or query.
- Gate promotion from observation to stakeholder claim.
- Give every important metric a definition fingerprint and every source an authority record.
- Validate business and interface meaning, not only technical field existence.
- Do not generalize sample, browser, qualitative, or single-page evidence beyond its representativeness.
- Keep association, prediction, and causal claims separate.
- Let presentation workers communicate approved claims; they may not create new analytical results.
- Version reviewed context and mark replaced claims or artifacts `superseded`; never silently overwrite them.
- If access or evidence is insufficient, narrow the question or report readiness instead of fabricating an answer.

## Start Behaviour

Read the request and supplied context before asking questions. Choose an internal needs-discovery mode:

- `Light`: clear, low-risk, single-question work.
- `Standard`: partial ambiguity, several questions, or a medium-risk decision.
- `Deep`: vague, contradictory, metric- or solution-led, multi-stakeholder, causal, or high-impact work.

Show only the four phases, not a twelve-item wall of process:

```text
1. Contract - interpret the need, confirm the question tree, scope, definitions, and evidence limits
2. Evidence - check readiness, execute bounded work, validate, and review claims
3. Synthesis - answer the tree, choose visuals, and produce stakeholder output
4. Delivery - document, version context, and define follow-up
```

For `Standard` or `Deep` work, begin with a concise framing proposal:

```text
What I believe the business needs:
Decision or learning objective:
Proposed core questions:
What I am treating as hypotheses:
What I recommend parking or reframing:
Primary and secondary problem types:
Decision needed:
```

Do not ask the user to design grain, methods, or metrics from scratch. Recommend them and ask only for corrections or decisions that materially change the work. For `Light` work, keep the same reasoning internal and proceed when the framing is unambiguous.

## Reference Router

- Read [needs-discovery-and-analysis-contract.md](references/needs-discovery-and-analysis-contract.md) before framing `Standard` or `Deep` work, or whenever a request is long, unclear, metric-led, solution-led, or internally inconsistent.
- Read [problem-type-playbooks.md](references/problem-type-playbooks.md) after drafting the question tree and before approving methods or validation.
- Read [evidence-claims-and-review.md](references/evidence-claims-and-review.md) before source mapping, execution, claim promotion, independent review, or durable-context updates.
- Read [synthesis-and-visualisation.md](references/synthesis-and-visualisation.md) before narrative design, chart selection, or stakeholder-output generation.
- Read [presentation-generator-brief.md](references/presentation-generator-brief.md) when a deck, PowerPoint, or external presentation handoff is requested.

## Four Phases And Twelve Checkpoints

The four phases are the user-facing model. The twelve checkpoints are the operational contract and may be combined only when risk and complexity allow.

| Phase | Checkpoint | Required outcome |
| --- | --- | --- |
| Contract | 1. Interpret the request | Decomposed request, inferred need, decision or learning objective, discovery mode |
| Contract | 2. Build and confirm the question tree | Core/supporting questions, coverage map, problem types, parked items |
| Contract | 3. Check data readiness | Source authority, semantics, grain, fingerprints, representativeness, evidence ceiling |
| Contract | 4. Approve the analysis contract | Scope, methods, validation, outputs, risk gates, definition of done |
| Evidence | 5. Execute bounded work | Reproducible operations and structured result packets |
| Evidence | 6. Validate results and candidate claims | Complete domains, compatible definitions, claim posture, caveats |
| Evidence | 7. Assemble reproducibility evidence | Queries/code, results, row counts, lineage, decisions, limitations |
| Evidence | 8. Review and promote claims | Independent review and risk-appropriate approval |
| Synthesis | 9. Produce stakeholder output | Question-led narrative using only approved claims and chart decisions |
| Delivery | 10. Document delivery and changes | Active outputs, generated review views, change history, stale/superseded state |
| Delivery | 11. Update durable context | Versioned reviewed facts, definitions, owners, validity dates, superseded entries |
| Delivery | 12. Define follow-up | Monitoring, validation, experiment, refresh, or no follow-up with rationale |

## Phase 1: Contract

### 1. Interpret The Request

Separate facts, objectives, constraints, hypotheses, suggested metrics, suggested methods, suggested solutions, output preferences, and uncertainties. Infer what decision or learning objective the work should support. Use decision-backward reasoning and the answer-to-action test: if different answers would not change a decision or learning outcome, the item is probably supporting context.

For complex work, use the conditional methods in the needs-discovery reference: analytical laddering, assumption mapping, alternative framing, stakeholder mapping, evidence-ceiling analysis, minimum-useful-scope review, and a pre-mortem. These are internal tools, not a questionnaire to impose on the user.

### 2. Build And Confirm The Question Tree

Create a draft tree with one decision root, a small set of core questions, and supporting or diagnostic leaves. Classify each leaf as `core`, `supporting`, `diagnostic`, `optional`, `duplicate`, `misleading`, `unavailable`, or `out_of_scope`.

Assign one of these types to each accepted analytical leaf:

```text
make_predictions
categorise_things
spot_unusual
identify_themes
discover_connections
find_patterns
```

Maintain request coverage so every material item is answered, supporting, parked, rejected, or unavailable. Confirm the concise tree for `Standard` and `Deep` work. Then operationalize accepted leaves with source, grain, metric, method, validation, and expected-output mappings.

### 3. Check Data Readiness

Create a source-authority record for every source and a definition fingerprint for every important metric. Verify source semantics, identifiers, coverage, freshness, time logic, access/PII constraints, availability denominators, and joinability. Record allowed and forbidden source uses.

Apply a representativeness gate before turning sampled evidence into a population statement. Browser inspection can validate visible wording, interaction outcomes, geometry, and instrumentation behaviour; it does not by itself establish aggregate prevalence or impact.

Apply problem-type readiness checks. If the evidence cannot support the requested claim, reframe to the strongest defensible answer. For medium/high-risk work, pause for a decision when the evidence ceiling materially changes the business interpretation.

### 4. Approve The Analysis Contract

The contract must identify:

```text
decision or learning objective
audience and owner
risk and needs-discovery mode
confirmed question tree and problem types
population, exclusions, period, timezone, and grain
source authority and metric fingerprints
methods, comparisons, validation, and claim limits
expected artifacts and presentation inputs
definition of done and approval gates
```

For medium/high-risk work, ask for contract approval before material execution. For low-risk work, record the contract and proceed unless an unresolved choice could change the answer.

## Phase 2: Evidence

### 5. Execute Bounded Work

Every operation must answer a question-tree leaf or a documented validation need. Use reproducible queries, scripts, notebooks, exports, API calls, or browser evidence. Keep exploration separate from promoted claims.

When workers or subagents are available, give them bounded task packets with allowed sources and an output schema. Workers may inspect and calculate; they may not publish, approve claims, update durable context, or take irreversible actions. A single agent may execute the same modes sequentially.

### 6. Validate Results And Candidate Claims

Validate code and result meaning separately. Check filters, joins, grain, full expected domains, zero/start states, denominators, deduplication, sample size, time ordering, availability, missingness, uncertainty, segment composition, representativeness, and causal language.

Promote findings through:

```text
observation -> candidate -> validated -> approved
                         \-> rejected
approved or validated -> superseded when replaced
```

Claims generated from limited evidence may be approved as `directional` only when the limitation remains visible. Source count alone is never a confidence score.

### 7. Assemble Reproducibility Evidence

Maintain claim-to-evidence and decision-lineage mappings in the manifest. Preserve operations, source references, output tables, row counts, fingerprints, validation outcomes, assumptions, caveats, and anonymized examples when allowed. Generate a human-readable reproducibility packet only when risk, review, or the requested delivery requires one.

### 8. Review And Promote Claims

Use independent review lenses:

- technical and methodological correctness;
- target-audience interpretation;
- domain-aware but analysis-naive interpretation.

Where possible, review from a clean context using the contract, evidence packet, proposed claims, and draft output rather than the producer's complete reasoning history. Human approval is required before high-risk or externally durable claims are treated as trusted. Low-risk claims may use an automated promotion path only when fingerprints, evidence, and caveats pass validation.

## Phase 3: Synthesis

### 9. Produce Stakeholder Output

Build the narrative from the confirmed question tree and approved claims, not from the order of the request or a generic slide template. Separate verified facts, interpretation, recommendation, and caveats. Choose depth and structure according to the problem type and audience.

Freeze the claim set and slide architecture before generating a deck for medium/high-risk work. Every analytical slide must reference approved claim IDs and canonical result data. Apply The Data Visualisation Catalogue, chart-decision, hard-rejection, specialist-chart, wording, and rendered-QA rules in the synthesis reference. User-provided templates, brand guides, and visualization systems override default styling, not evidence rules.

## Phase 4: Delivery

### 10. Document Delivery And Changes

Keep one active version of each deliverable. Mark replaced outputs `superseded`. Generate review packets, documentation, or changelog views from the canonical manifest instead of maintaining duplicate truths. When a fingerprint, source mapping, or claim changes, mark dependent artifacts `stale` until regenerated and reviewed.

### 11. Update Durable Context

Update durable context only with reviewed knowledge. Append versions with old/new value or definition, validity window, run date, owner, reviewer, reason, and source analysis ID. Never overwrite history silently. Store pointers to the analysis manifest rather than copying facts into multiple homes.

### 12. Define Follow-Up

Choose the follow-up that fits the problem type: monitoring, model drift/recalibration, label review, anomaly-threshold review, qualitative refresh, validation study, controlled experiment, measurement improvement, or no follow-up. Name the owner, success criteria, guardrails, and revisit condition when applicable.

## Canonical Run Artifacts

Use `analyses/<analysis_id>/` unless the user provides another location. Start from `assets/analysis-manifest.template.json` or run:

```text
python scripts/analysis_guard.py init analyses/<analysis_id> --analysis-id <analysis_id>
```

The canonical source of truth is `analysis-manifest.json`. Keep raw or derived evidence under `evidence/`. Add `results.md` and the requested delivery format when useful. Generate `analysis-plan.md`, `reproducibility-packet.md`, `analysis-documentation.md`, or `analysis-changelog.md` only when human review, risk, or delivery needs justify them.

Use stable IDs for decisions, questions, sources, metrics, evidence, claims, visuals, and artifacts. Run the guard before stakeholder delivery:

```text
python scripts/analysis_guard.py validate analyses/<analysis_id>/analysis-manifest.json --strict
python scripts/analysis_guard.py stale analyses/<analysis_id>/analysis-manifest.json
python scripts/analysis_guard.py scan analyses/<analysis_id>
```

If the utility is unavailable, apply the same checks manually and record that automated validation was not performed.

## Agent And Tool Portability

Use local equivalents for files, queries, notebooks, APIs, browsers, charts, and presentations. Do not require a particular vendor, agent, MCP server, operating system, or analytics platform. When a capability is missing, preserve the contract and evidence format, mark the limitation, and offer the strongest feasible path.

Never copy credentials, client data, prior analysis results, or machine-specific absolute paths into the reusable skill. Keep generated work visible in the user's chosen workspace and access-controlled where needed.
