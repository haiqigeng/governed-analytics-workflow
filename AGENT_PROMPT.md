# Agent Launch Prompt

Use this prompt with any AI agent that can read files or accept long instructions.

```text
Read `SKILL.md` in this folder and use it as your operating process for this analytics analysis.

If you cannot read local files, ask me to paste the content of `SKILL.md`.

Run the workflow interactively:
- show each step checklist with known, unknown, assumed, and not-applicable fields
- ask the next necessary question or small group of related questions
- classify risk before doing analysis
- start with a short Triage Snapshot
- frame the decision, scope, metrics, and caveats
- check data readiness before making claims
- map desired metrics to real source events, fields, dimensions, or derived logic
- create an analysis plan before execution
- keep worker outputs structured
- produce a reproducibility packet before human approval
- ask for human approval before producing trusted stakeholder output
- update durable context only after review

Do not fabricate data. If data access is missing or weak, create a readiness assessment and proposed next step.

My analysis request is:
[paste the user/business question here]

Available data, files, dashboards, or context:
[paste links, file paths, table names, screenshots, or notes here]
```
