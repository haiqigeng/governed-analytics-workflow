# Governed Analytics Workflow

An instruction-first AI agent skill for running analytics work as a governed, traceable, human-reviewed process.

The workflow helps an AI agent turn a business question into structured analytics artifacts: risk triage, intake, framing, data readiness, bounded execution, quality review, reproducibility packet, human approval, stakeholder output, and durable context updates.

## Why This Exists

AI agents can speed up analytics work, but they can also make unsupported claims look polished. This skill is designed to keep the useful speed while preserving reviewability.

Core principle:

```text
AI agents produce evidence, checks, drafts, and packets. Humans approve meaning, risk, and decisions.
```

## What's Included

```text
governed-analytics-workflow/
  SKILL.md               Core workflow instructions for AI agents
  AGENT_PROMPT.md        Copy-paste prompt for agents that do not auto-discover skills
  agents/openai.yaml     Optional Codex/OpenAI UI metadata
  README.md              Human-readable project overview
  CHANGELOG.md           Release history
```

## Use With Codex

Copy this folder to your Codex skills directory:

```text
~/.codex/skills/governed-analytics-workflow
```

Then invoke it:

```text
Use $governed-analytics-workflow to run this analysis interactively.
```

## Use With Claude Code, Gemini, Or Other Agents

Give the agent access to `SKILL.md`, or paste the content of `AGENT_PROMPT.md`.

Example:

```text
Read `SKILL.md` and use it as your operating process for this analytics analysis.

My analysis request is:
Analyze how visitors scroll on programme pages and whether key content should move higher.

Available context:
GA4/BigQuery events include page_view, scroll events, device category, traffic channel, and CTA clicks.
```

The agent should start with a short triage snapshot and ask only the next necessary question.

## Workflow Summary

```text
Triage risk and decision
-> create intake
-> frame scope and metrics
-> check data readiness
-> draft analysis plan
-> execute bounded worker tasks
-> validate and quality review
-> generate reproducibility packet
-> ask for human approval
-> produce stakeholder output
-> update durable context
-> define follow-up monitoring or experiment
```

## Expected Outputs

The workflow can produce artifacts such as:

- `analytics-intake.md`
- `analysis-framing.md`
- `readiness-assessment.md`
- `analysis-plan.md`
- `worker-result-packets.md`
- `quality-review.md`
- `reproducibility-packet.md`
- `stakeholder-brief.md`
- `decision-log-entry.md`

The most important artifact is the reproducibility packet. It should let a human reviewer recreate or challenge the analysis using the source data, filters, queries, row counts, metric definitions, assumptions, and caveats.

## Example Use Case

Question:

```text
How are visitors scrolling on programme pages, and should key content move higher?
```

Good supported conclusion:

```text
Only 31% of sessions reached the approximate Fees section, suggesting limited measured exposure.
```

Unsupported conclusion to avoid:

```text
Users do not care about fees.
```

## Project Status

Initial private release. The skill is usable as a portable Markdown-based agent workflow and does not require Python, Node.js, or any runtime dependency.

## License

No license has been specified yet. Treat this repository as private/internal unless a license is added.

