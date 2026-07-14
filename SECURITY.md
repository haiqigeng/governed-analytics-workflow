# Security Policy

## Supported Versions

Security fixes are considered for the latest public release.

## Reporting A Vulnerability

Please report security issues privately by email or LinkedIn rather than opening
a public issue.

Include:

- the affected file or workflow step;
- a short reproduction or explanation;
- whether personal data, client data, credentials, or confidential analysis
  could be exposed;
- any suggested mitigation.

## Scope

This project is an analytics workflow guide. Security-sensitive areas include
source mapping, uploaded files, manifests, generated analysis packets, stakeholder
outputs, and any instructions that could expose private data or unsupported claims.

Do not publish client data, credentials, private dashboards, raw exports, or
confidential business metrics in issues, examples, tests, or documentation.

Run `python scripts/analysis_guard.py scan <path>` before sharing an analysis
folder and `python tools/check_release.py --release-notes CHANGELOG.md` before
publishing the reusable skill.
