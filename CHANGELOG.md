# Changelog

## 1.0.0 - 2026-07-15

### Why This Release Matters

The workflow now treats needs discovery and analytical reasoning as first-class work. It no longer assumes that a stakeholder's questions, indicators, methods, or preferred explanations form a valid analysis specification.

### What Changed

- Replaced the visible twelve-step launch with four adaptive phases while preserving twelve operational checkpoints.
- Added `Light`, `Standard`, and `Deep` needs-discovery modes.
- Added request decomposition, decision-backward framing, analytical laddering, assumption mapping, alternative framing, stakeholder mapping, evidence-ceiling analysis, minimum-useful scope, and pre-mortems.
- Added draft, confirmed, and operational question trees with request coverage and decision lineage.
- Added playbooks for prediction, categorisation, anomaly detection, theme identification, connection discovery, and pattern finding.
- Added source-authority records, metric definition fingerprints, semantic validation, availability rules, temporal eligibility, and representativeness gates.
- Added observation-to-approved claim promotion, independent review lenses, versioned durable context, and stale dependency handling.
- Added a function-first live Data Visualisation Catalogue gate, hard chart rejection rules, specialist-chart exceptions, and rendered output QA.
- Restricted presentation generation to approved claims and canonical results.
- Replaced the large default artifact list with a canonical JSON manifest and conditional review views.
- Added the zero-dependency `analysis_guard.py` utility for scaffolding, validation, fingerprinting, stale checks, and portability scans.
- Added deterministic runtime packaging, CI, release automation, and behavioral regression tests.
- Updated repository documentation and agent metadata for the v1 workflow.

### What Users Should Do

- Start new analyses from `assets/analysis-manifest.template.json` or `analysis_guard.py init`.
- Confirm the inferred need and question tree before material execution for ambiguous or consequential work.
- Run strict manifest, stale dependency, and portability checks before stakeholder delivery.
- Treat existing pre-1.0 analysis folders as legacy artifacts; migrate only when they need to be reopened or republished.

### Validation

- System skill validation.
- Python compilation for runtime and release utilities.
- Unit tests for strict manifests, all six problem types, question-tree routing, approved-claim enforcement, expected-domain completeness, exclusive-distribution chart rejection, stale fingerprints, portability scanning, and deterministic packaging.
- Runtime scan for client-specific terms, secrets, and machine-specific absolute paths.
- Clean repository and release-package checks.

### Known Limits

- The guard validates governance structure and selected semantic invariants; it cannot prove that an external query, statistical model, or business interpretation is correct.
- Live chart-catalogue consultation, source access, browser inspection, and rendered PowerPoint QA still depend on available tools.
- Existing analyses are not automatically migrated to the v1 manifest.

## 0.3.4 - 2026-06-14

- Removed residual analysis-specific examples and kept the reusable skill generic.

## 0.3.3 - 2026-06-14

- Hardened analyst orientation, grain checks, and delivery handoff.

## 0.3.2 - 2026-06-14

- Added Data Visualisation Catalogue guidance.

## Earlier Releases

- `0.1.0` through `0.3.1` established the original twelve-step governed workflow, presentation handoff, documentation, and readiness checks.
