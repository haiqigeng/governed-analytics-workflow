# Contributing

Thanks for improving Governed Analytics Workflow.

This repository is designed to make AI-assisted analytics work more decision-relevant,
traceable, reviewable, and reproducible. Contributions should strengthen needs
discovery, analytical reasoning, source mapping, metric clarity, evidence handling,
review gates, or stakeholder delivery quality.

## Guidelines

- Keep examples generic. Do not include client data, private business context,
  internal metrics, confidential screenshots, or personal data.
- Preserve the workflow's bias toward evidence, explicit assumptions, and human
  review before high-stakes outputs.
- Keep instructions portable across AI coding agents where possible.
- Keep `SKILL.md` lean and route detailed behaviour through focused references.
- Update `README.md`, `CHANGELOG.md`, tests, and agent metadata when changing the workflow contract.
- Prefer small, reviewable changes over broad rewrites.

## Validation

Run before opening a pull request:

```powershell
python tools/check_release.py --release-notes CHANGELOG.md
python -m unittest discover -s tests -v
python tools/build_skill_package.py --output dist/governed-analytics-workflow-test.zip
```

Add a regression test when correcting a framing, fingerprint, claim-promotion,
visualisation, portability, or artifact-dependency failure.

## Pull Requests

Before opening a pull request:

- Explain what analytics risk or workflow gap the change addresses.
- Note any new review gate, output artifact, dependency, or required tool.
- Check that examples remain domain-neutral and safe to publish.
- Explain whether the change affects runtime-package compatibility or existing manifests.
