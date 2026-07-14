#!/usr/bin/env python3
"""Scaffold and validate governed analytics manifests without dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_ROOT / "assets" / "analysis-manifest.template.json"

TOP_LEVEL_KEYS = (
    "schema_version",
    "analysis_id",
    "status",
    "needs_discovery",
    "question_tree",
    "contract",
    "sources",
    "metrics",
    "evidence",
    "claims",
    "visuals",
    "recommendations",
    "artifacts",
    "changes",
    "approvals",
    "durable_context",
)
PROBLEM_TYPES = {
    "make_predictions",
    "categorise_things",
    "spot_unusual",
    "identify_themes",
    "discover_connections",
    "find_patterns",
}
QUESTION_ROLES = {
    "core",
    "supporting",
    "diagnostic",
    "optional",
    "duplicate",
    "misleading",
    "unavailable",
    "out_of_scope",
}
ACTIVE_QUESTION_ROLES = {"core", "supporting", "diagnostic", "optional"}
COVERAGE_DISPOSITIONS = {
    "answered_by_question",
    "supporting_context",
    "parked",
    "rejected",
    "unavailable",
    "superseded",
}
CLAIM_STATUSES = {
    "observation",
    "candidate",
    "validated",
    "approved",
    "rejected",
    "superseded",
}
EVIDENCE_STATUSES = {"observation", "candidate", "validated", "rejected", "superseded"}
EVIDENCE_POSTURES = {"verified", "directional", "assumed", "needs_validation"}
ARTIFACT_STATUSES = {"draft", "active", "stale", "superseded", "rejected"}
NEEDS_MODES = {"light", "standard", "deep"}
CONTRACT_STATUSES = {"draft", "ready_for_review", "approved", "approved_with_caveats", "rejected"}
TREE_STATUSES = {"draft", "confirmed", "operational"}
VISUAL_QA_STATUSES = {"pending", "passed", "failed", "not_possible"}
METRIC_SHAPES = {
    "count",
    "rate",
    "intensity",
    "exclusive_distribution",
    "cumulative_reach",
    "funnel",
    "trend",
    "relationship",
    "range",
    "model_metric",
    "qualitative",
}
STAKEHOLDER_VISUAL_USES = {"stakeholder", "executive", "presentation", "external"}
FINGERPRINT_FIELDS = (
    "population",
    "calculation_grain",
    "time_window",
    "scope",
    "filters",
    "numerator",
    "denominator",
    "deduplication",
    "source_query_ref",
    "run_date",
)
SOURCE_FIELDS = (
    "source_id",
    "name",
    "owner",
    "authority",
    "source_grain",
    "coverage",
    "freshness",
    "join_keys",
    "joinability",
    "allowed_uses",
    "forbidden_uses",
    "access_and_pii",
    "caveats",
)
SECRET_PATTERNS = (
    re.compile(r"(?i)\b(?:api[_-]?key|secret|access[_-]?token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"),
    re.compile(r"\bgh[opusr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\b(?:sk|rk)-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)
ABSOLUTE_PATH_PATTERNS = (
    re.compile(r"(?i)(?<![A-Za-z0-9_])[A-Z]:[\\/]+(?:Users|Documents and Settings)[\\/]+[^\s\"'<>]+"),
    re.compile(r"(?<![A-Za-z0-9_])/(?:home|Users)/+[^\s\"'<>]+"),
)
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
    ".tsv",
    ".sql",
    ".py",
    ".js",
    ".ts",
    ".ps1",
    ".sh",
    ".toml",
}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", "node_modules", "dist"}


class ManifestError(ValueError):
    """Raised when a manifest cannot be loaded."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ManifestError(f"manifest does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    if not isinstance(data, dict):
        raise ManifestError("manifest root must be a JSON object")
    return data


def write_json_atomic(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=path.parent, newline="\n") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
        temp_name = handle.name
    os.replace(temp_name, path)


def stable_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def require_nonempty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def keyed(items: Any, key: str, label: str, errors: list[str]) -> dict[str, dict[str, Any]]:
    if not isinstance(items, list):
        errors.append(f"{label} must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{label}[{index}] must be an object")
            continue
        value = item.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}[{index}] missing {key}")
            continue
        if value in result:
            errors.append(f"duplicate {key}: {value}")
        result[value] = item
    return result


def validate_manifest(data: dict[str, Any], strict: bool = False) -> list[str]:
    errors: list[str] = []
    for key in TOP_LEVEL_KEYS:
        if key not in data:
            errors.append(f"missing top-level key: {key}")

    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    analysis_id = data.get("analysis_id")
    if not isinstance(analysis_id, str) or not analysis_id.strip():
        errors.append("analysis_id must be a non-empty string")
    elif strict and analysis_id == "replace-with-analysis-id":
        errors.append("analysis_id still contains the template placeholder")

    discovery = data.get("needs_discovery", {})
    if not isinstance(discovery, dict):
        errors.append("needs_discovery must be an object")
        discovery = {}
    if discovery.get("mode") not in NEEDS_MODES:
        errors.append(f"invalid needs_discovery.mode: {discovery.get('mode')}")
    if discovery.get("framing_status") not in {"proposed", "confirmed", "revised", "rejected"}:
        errors.append(f"invalid needs_discovery.framing_status: {discovery.get('framing_status')}")
    stated_request = discovery.get("stated_request", [])
    stated_request_ids: list[str] = []
    if not isinstance(stated_request, list):
        errors.append("needs_discovery.stated_request must be a list")
    elif strict:
        for index, item in enumerate(stated_request):
            if not isinstance(item, dict):
                errors.append(f"needs_discovery.stated_request[{index}] must be an object")
                continue
            request_item_id = item.get("request_item_id")
            if not require_nonempty(request_item_id):
                errors.append(f"needs_discovery.stated_request[{index}] missing request_item_id")
            else:
                stated_request_ids.append(str(request_item_id))
            if not require_nonempty(item.get("text")):
                errors.append(f"needs_discovery.stated_request[{index}] missing text")
        for field in ("inferred_business_need", "evidence_ceiling"):
            if not require_nonempty(discovery.get(field)):
                errors.append(f"strict validation requires needs_discovery.{field}")
        if discovery.get("mode") in {"standard", "deep"} and discovery.get("framing_status") not in {"confirmed", "revised"}:
            errors.append("standard/deep work requires confirmed or revised framing under strict validation")

    tree = data.get("question_tree", {})
    if not isinstance(tree, dict):
        errors.append("question_tree must be an object")
        tree = {}
    if tree.get("status") not in TREE_STATUSES:
        errors.append(f"invalid question_tree.status: {tree.get('status')}")
    primary_type = tree.get("primary_problem_type")
    if primary_type not in PROBLEM_TYPES:
        errors.append(f"invalid primary problem type: {primary_type}")
    secondary = tree.get("secondary_problem_types", [])
    if not isinstance(secondary, list) or any(item not in PROBLEM_TYPES for item in secondary):
        errors.append("secondary_problem_types contains an invalid type")
    if primary_type in secondary:
        errors.append("primary problem type must not be repeated as secondary")

    questions = keyed(tree.get("questions", []), "question_id", "question_tree.questions", errors)
    for question_id, question in questions.items():
        role = question.get("role")
        if role not in QUESTION_ROLES:
            errors.append(f"{question_id} has invalid role: {role}")
        problem_type = question.get("problem_type")
        if role in ACTIVE_QUESTION_ROLES and problem_type not in PROBLEM_TYPES:
            errors.append(f"{question_id} has invalid problem_type: {problem_type}")
        parent = question.get("parent_id")
        if parent is not None and parent not in questions:
            errors.append(f"{question_id} references missing parent question: {parent}")
        if parent == question_id:
            errors.append(f"{question_id} cannot be its own parent")
        if strict and role in {"core", "supporting"} and not require_nonempty(question.get("decision_relevance")):
            errors.append(f"{question_id} missing decision_relevance")
    if strict and not any(question.get("role") == "core" for question in questions.values()):
        errors.append("strict validation requires at least one core question")
    coverage = tree.get("coverage", [])
    coverage_ids: list[str] = []
    if not isinstance(coverage, list):
        errors.append("question_tree.coverage must be a list")
    else:
        for index, item in enumerate(coverage):
            if not isinstance(item, dict):
                errors.append(f"question_tree.coverage[{index}] must be an object")
                continue
            request_item_id = item.get("request_item_id")
            if not require_nonempty(request_item_id):
                errors.append(f"question_tree.coverage[{index}] missing request_item_id")
            else:
                coverage_ids.append(str(request_item_id))
            disposition = item.get("disposition")
            if disposition not in COVERAGE_DISPOSITIONS:
                errors.append(f"question_tree.coverage[{index}] has invalid disposition: {disposition}")
            mapped_questions = item.get("question_ids", [])
            for question_id in mapped_questions:
                if question_id not in questions:
                    errors.append(f"question_tree.coverage[{index}] references missing question: {question_id}")
            if disposition not in {"answered_by_question", "supporting_context"} and not require_nonempty(item.get("reason")):
                errors.append(f"question_tree.coverage[{index}] requires a reason for disposition {disposition}")
        for repeated in sorted({value for value in coverage_ids if coverage_ids.count(value) > 1}):
            errors.append(f"duplicate request coverage item: {repeated}")
    if strict and stated_request_ids:
        missing_coverage = sorted(set(stated_request_ids) - set(coverage_ids))
        if missing_coverage:
            errors.append(f"request coverage missing stated items: {missing_coverage}")

    contract = data.get("contract", {})
    if not isinstance(contract, dict):
        errors.append("contract must be an object")
        contract = {}
    if contract.get("status") not in CONTRACT_STATUSES:
        errors.append(f"invalid contract.status: {contract.get('status')}")
    if contract.get("risk") not in {"low", "medium", "high"}:
        errors.append(f"invalid contract.risk: {contract.get('risk')}")
    if strict and contract.get("status") in {"approved", "approved_with_caveats"}:
        for field in ("audience", "owner", "population", "primary_grain", "definition_of_done"):
            if not require_nonempty(contract.get(field)):
                errors.append(f"approved contract missing {field}")
        period = contract.get("period", {})
        if not isinstance(period, dict) or any(not require_nonempty(period.get(field)) for field in ("start", "end", "timezone")):
            errors.append("approved contract requires period start, end, and timezone")
        if contract.get("risk") in {"medium", "high"} and not require_nonempty(contract.get("approval_gates")):
            errors.append("medium/high-risk approved contract requires approval_gates")

    sources = keyed(data.get("sources", []), "source_id", "sources", errors)
    for source_id, source in sources.items():
        missing = [field for field in SOURCE_FIELDS if field not in source]
        if missing:
            errors.append(f"{source_id} missing source fields: {', '.join(missing)}")
        if source.get("authority") not in {"canonical", "supporting", "illustrative", "experimental"}:
            errors.append(f"{source_id} has invalid authority: {source.get('authority')}")
        if source.get("joinability") not in {"direct", "aggregate_only", "none", "unknown"}:
            errors.append(f"{source_id} has invalid joinability: {source.get('joinability')}")

    metrics = keyed(data.get("metrics", []), "metric_id", "metrics", errors)
    metric_hashes: dict[str, str] = {}
    for metric_id, metric in metrics.items():
        for question_id in metric.get("question_ids", []):
            if question_id not in questions:
                errors.append(f"{metric_id} references missing question: {question_id}")
        for source_id in metric.get("source_ids", []):
            if source_id not in sources:
                errors.append(f"{metric_id} references missing source: {source_id}")
        shape = metric.get("metric_shape")
        if shape not in METRIC_SHAPES:
            errors.append(f"{metric_id} has invalid metric_shape: {shape}")
        fingerprint = metric.get("definition_fingerprint")
        if not isinstance(fingerprint, dict):
            errors.append(f"{metric_id} missing definition_fingerprint")
            continue
        if strict or metric.get("status") in {"validated", "approved", "active"}:
            missing = [field for field in FINGERPRINT_FIELDS if not require_nonempty(fingerprint.get(field)) and field not in {"scope", "filters"}]
            if missing:
                errors.append(f"{metric_id} incomplete fingerprint: {', '.join(missing)}")
            time_window = fingerprint.get("time_window", {})
            if not isinstance(time_window, dict) or any(not require_nonempty(time_window.get(field)) for field in ("start", "end", "timezone")):
                errors.append(f"{metric_id} fingerprint requires start, end, and timezone")
        expected = metric.get("expected_domain")
        observed = metric.get("observed_domain")
        if expected is not None:
            if not isinstance(expected, list) or not isinstance(observed, list):
                errors.append(f"{metric_id} expected_domain and observed_domain must both be lists")
            else:
                missing_values = [value for value in expected if value not in observed]
                if missing_values:
                    errors.append(f"{metric_id} observed_domain missing expected values: {missing_values}")
        metric_hashes[metric_id] = stable_hash(fingerprint)
        stored_hash = metric.get("fingerprint_hash")
        if stored_hash and stored_hash != metric_hashes[metric_id]:
            errors.append(f"{metric_id} fingerprint_hash is stale")

    evidence = keyed(data.get("evidence", []), "evidence_id", "evidence", errors)
    for evidence_id, evidence_item in evidence.items():
        status = evidence_item.get("status")
        if status not in EVIDENCE_STATUSES:
            errors.append(f"{evidence_id} has invalid status: {status}")
        for question_id in evidence_item.get("question_ids", []):
            if question_id not in questions:
                errors.append(f"{evidence_id} references missing question: {question_id}")
        for source_id in evidence_item.get("source_ids", []):
            if source_id not in sources:
                errors.append(f"{evidence_id} references missing source: {source_id}")
        if status == "validated" and not require_nonempty(evidence_item.get("result_ref")):
            errors.append(f"{evidence_id} cannot be validated without result_ref")
    claims = keyed(data.get("claims", []), "claim_id", "claims", errors)
    for claim_id, claim in claims.items():
        status = claim.get("status")
        if status not in CLAIM_STATUSES:
            errors.append(f"{claim_id} has invalid status: {status}")
        posture = claim.get("evidence_posture")
        if posture not in EVIDENCE_POSTURES:
            errors.append(f"{claim_id} has invalid evidence_posture: {posture}")
        for question_id in claim.get("question_ids", []):
            if question_id not in questions:
                errors.append(f"{claim_id} references missing question: {question_id}")
        for metric_id in claim.get("metric_ids", []):
            if metric_id not in metrics:
                errors.append(f"{claim_id} references missing metric: {metric_id}")
        for evidence_id in claim.get("evidence_refs", []):
            if evidence_id not in evidence:
                errors.append(f"{claim_id} references missing evidence: {evidence_id}")
        snapshots = claim.get("metric_fingerprints", {})
        if snapshots and not isinstance(snapshots, dict):
            errors.append(f"{claim_id} metric_fingerprints must be an object")
        elif isinstance(snapshots, dict):
            for metric_id, snapshot in snapshots.items():
                if metric_id not in metric_hashes:
                    errors.append(f"{claim_id} snapshots missing metric: {metric_id}")
                elif snapshot != metric_hashes[metric_id] and status not in {"candidate", "rejected", "superseded"}:
                    errors.append(f"{claim_id} has stale metric fingerprint for {metric_id}")
        comparison_ids = claim.get("comparison_metric_ids", [])
        if comparison_ids:
            missing_metrics = [metric_id for metric_id in comparison_ids if metric_id not in metrics]
            if missing_metrics:
                errors.append(f"{claim_id} comparison references missing metrics: {missing_metrics}")
            elif len(comparison_ids) >= 2:
                compatibility_keys = claim.get(
                    "compatibility_keys",
                    [
                        "population",
                        "calculation_grain",
                        "time_window",
                        "scope",
                        "denominator",
                        "deduplication",
                    ],
                )
                baseline = metrics[comparison_ids[0]].get("definition_fingerprint", {})
                mismatches = [
                    key
                    for key in compatibility_keys
                    if any(metrics[metric_id].get("definition_fingerprint", {}).get(key) != baseline.get(key) for metric_id in comparison_ids[1:])
                ]
                if mismatches and not require_nonempty(claim.get("compatibility_rationale")):
                    errors.append(f"{claim_id} compares incompatible fingerprints without rationale: {mismatches}")
        if status in {"validated", "approved"}:
            if not claim.get("evidence_refs"):
                errors.append(f"{claim_id} cannot be {status} without evidence_refs")
            if not claim.get("metric_ids") and posture != "directional":
                errors.append(f"{claim_id} cannot be {status} without metric_ids unless directional")
            if not require_nonempty(claim.get("valid_as_of")):
                errors.append(f"{claim_id} cannot be {status} without valid_as_of")
            missing_snapshots = [
                metric_id
                for metric_id in claim.get("metric_ids", [])
                if metric_id not in snapshots
            ]
            if missing_snapshots:
                errors.append(f"{claim_id} missing metric fingerprint snapshots: {missing_snapshots}")
            unvalidated_evidence = [
                evidence_id
                for evidence_id in claim.get("evidence_refs", [])
                if evidence.get(evidence_id, {}).get("status") != "validated"
            ]
            if unvalidated_evidence:
                errors.append(f"{claim_id} uses evidence that is not validated: {unvalidated_evidence}")
        if status == "approved" and (not require_nonempty(claim.get("approved_by")) or not require_nonempty(claim.get("approved_at"))):
            errors.append(f"{claim_id} cannot be approved without approved_by and approved_at")

    visuals = keyed(data.get("visuals", []), "visual_id", "visuals", errors)
    for visual_id, visual in visuals.items():
        claim_ids = visual.get("claim_ids", [])
        for claim_id in claim_ids:
            if claim_id not in claims:
                errors.append(f"{visual_id} references missing claim: {claim_id}")
        intended_use = visual.get("intended_use", "stakeholder")
        if intended_use in STAKEHOLDER_VISUAL_USES:
            for claim_id in claim_ids:
                if claims.get(claim_id, {}).get("status") != "approved":
                    errors.append(f"{visual_id} stakeholder visual uses non-approved claim: {claim_id}")
        qa_status = visual.get("qa_status")
        if qa_status not in VISUAL_QA_STATUSES:
            errors.append(f"{visual_id} has invalid qa_status: {qa_status}")
        shape = visual.get("data_structure", {}).get("metric_shape") if isinstance(visual.get("data_structure"), dict) else None
        selected = str(visual.get("selected_chart", "")).lower()
        if shape == "exclusive_distribution" and "funnel" in selected:
            errors.append(f"{visual_id} cannot use a funnel for an exclusive distribution")
        ordered = visual.get("data_structure", {}).get("ordered") if isinstance(visual.get("data_structure"), dict) else None
        if ordered is False and "line" in selected:
            errors.append(f"{visual_id} cannot use a line for unordered categories")
        categories_overlap = visual.get("data_structure", {}).get("categories_overlap") if isinstance(visual.get("data_structure"), dict) else None
        if categories_overlap is True and visual.get("communication_function") in {"proportion", "part_to_whole"}:
            errors.append(f"{visual_id} cannot use part-to-whole encoding for overlapping categories")
        if strict and intended_use in STAKEHOLDER_VISUAL_USES:
            for field in ("question_id", "result_ref", "message", "communication_function", "selected_chart"):
                if not require_nonempty(visual.get(field)):
                    errors.append(f"{visual_id} stakeholder visual missing {field}")
            if qa_status != "passed":
                errors.append(f"{visual_id} stakeholder visual has not passed rendered QA")
            if not isinstance(visual.get("live_catalogue_checked"), bool):
                errors.append(f"{visual_id} must record whether the live catalogue was checked")
            elif visual.get("live_catalogue_checked") is False and not require_nonempty(visual.get("catalogue_check_note")):
                errors.append(f"{visual_id} must explain why the live catalogue was not checked")
            if not require_nonempty(visual.get("required_labels")):
                errors.append(f"{visual_id} stakeholder visual missing required_labels")

    recommendations = keyed(data.get("recommendations", []), "recommendation_id", "recommendations", errors)
    for recommendation_id, recommendation in recommendations.items():
        supporting = recommendation.get("supporting_claim_ids", [])
        if not supporting:
            errors.append(f"{recommendation_id} has no supporting_claim_ids")
        for claim_id in supporting:
            if claim_id not in claims:
                errors.append(f"{recommendation_id} references missing claim: {claim_id}")
            elif claims[claim_id].get("status") != "approved":
                errors.append(f"{recommendation_id} uses non-approved claim: {claim_id}")

    artifacts = keyed(data.get("artifacts", []), "artifact_id", "artifacts", errors)
    known_dependencies = set(questions) | set(sources) | set(metrics) | set(evidence) | set(claims) | set(visuals) | set(recommendations)
    for artifact_id, artifact in artifacts.items():
        if artifact.get("status") not in ARTIFACT_STATUSES:
            errors.append(f"{artifact_id} has invalid status: {artifact.get('status')}")
        for dependency in artifact.get("depends_on", []):
            if dependency not in known_dependencies:
                errors.append(f"{artifact_id} references missing dependency: {dependency}")
        snapshots = artifact.get("metric_fingerprints", {})
        if not isinstance(snapshots, dict):
            errors.append(f"{artifact_id} metric_fingerprints must be an object")
        else:
            for metric_id, snapshot in snapshots.items():
                if metric_id not in metric_hashes:
                    errors.append(f"{artifact_id} snapshots missing metric: {metric_id}")
                elif snapshot != metric_hashes[metric_id] and artifact.get("status") not in {"stale", "superseded"}:
                    errors.append(f"{artifact_id} has stale metric fingerprint for {metric_id}")
        required_metric_snapshots = {
            dependency for dependency in artifact.get("depends_on", []) if dependency in metrics
        }
        for dependency in artifact.get("depends_on", []):
            if dependency in claims:
                required_metric_snapshots.update(claims[dependency].get("metric_ids", []))
        if artifact.get("status") == "active":
            missing_snapshots = sorted(required_metric_snapshots - set(snapshots))
            if missing_snapshots:
                errors.append(f"{artifact_id} missing metric fingerprint snapshots: {missing_snapshots}")

    active_purposes: dict[str, list[str]] = {}
    for artifact_id, artifact in artifacts.items():
        if artifact.get("status") == "active" and require_nonempty(artifact.get("purpose")):
            active_purposes.setdefault(str(artifact["purpose"]), []).append(artifact_id)
    for purpose, artifact_ids in active_purposes.items():
        if len(artifact_ids) > 1:
            errors.append(f"multiple active artifacts for purpose {purpose!r}: {artifact_ids}")

    if strict:
        if tree.get("status") != "operational":
            errors.append("strict validation requires an operational question tree")
        for question_id, question in questions.items():
            if question.get("role") in {"core", "supporting"} and question.get("status") not in {"confirmed", "operational", "answered", "unavailable"}:
                errors.append(f"{question_id} is not confirmed or operational under strict validation")
        if contract.get("status") not in {"approved", "approved_with_caveats"}:
            errors.append("strict validation requires an approved contract")

    return errors


def add_fingerprint_hashes(data: dict[str, Any]) -> int:
    changed = 0
    for metric in data.get("metrics", []):
        fingerprint = metric.get("definition_fingerprint")
        if not isinstance(fingerprint, dict):
            continue
        value = stable_hash(fingerprint)
        if metric.get("fingerprint_hash") != value:
            metric["fingerprint_hash"] = value
            changed += 1
    return changed


def stale_artifacts(data: dict[str, Any], write: bool = False) -> tuple[list[str], int]:
    current = {
        metric.get("metric_id"): stable_hash(metric.get("definition_fingerprint"))
        for metric in data.get("metrics", [])
        if metric.get("metric_id") and isinstance(metric.get("definition_fingerprint"), dict)
    }
    stale: list[str] = []
    changed = 0
    for claim in data.get("claims", []):
        snapshots = claim.get("metric_fingerprints", {})
        if not isinstance(snapshots, dict):
            continue
        mismatches = [metric_id for metric_id, value in snapshots.items() if current.get(metric_id) != value]
        if mismatches:
            claim_id = claim.get("claim_id", "<unknown>")
            stale.append(f"{claim_id}: {', '.join(mismatches)}")
            if write and claim.get("status") not in {"candidate", "rejected", "superseded"}:
                claim["status"] = "candidate"
                claim["evidence_posture"] = "needs_validation"
                claim["stale_reason"] = f"metric fingerprint changed: {', '.join(mismatches)}"
                changed += 1
    for artifact in data.get("artifacts", []):
        snapshots = artifact.get("metric_fingerprints", {})
        if not isinstance(snapshots, dict):
            continue
        mismatches = [metric_id for metric_id, value in snapshots.items() if current.get(metric_id) != value]
        if mismatches:
            artifact_id = artifact.get("artifact_id", "<unknown>")
            stale.append(f"{artifact_id}: {', '.join(mismatches)}")
            if write and artifact.get("status") not in {"stale", "superseded"}:
                artifact["status"] = "stale"
                artifact["stale_reason"] = f"metric fingerprint changed: {', '.join(mismatches)}"
                changed += 1
    return stale, changed


def iter_text_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        if root.suffix.lower() in TEXT_SUFFIXES:
            yield root
        return
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def scan_path(root: Path) -> list[str]:
    findings: list[str] = []
    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path}:{line_number}: possible secret")
                    break
            for pattern in ABSOLUTE_PATH_PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path}:{line_number}: machine-specific absolute path")
                    break
    return findings


def command_init(args: argparse.Namespace) -> int:
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "analysis-manifest.json"
    if manifest_path.exists() and not args.force:
        print(f"ERROR: manifest already exists: {manifest_path}", file=sys.stderr)
        return 1
    data = load_json(TEMPLATE)
    data["analysis_id"] = args.analysis_id
    write_json_atomic(manifest_path, data)
    (output / "evidence").mkdir(exist_ok=True)
    results = output / "results.md"
    if not results.exists():
        results.write_text(f"# Results\n\nAnalysis ID: `{args.analysis_id}`\n\nStatus: Draft\n", encoding="utf-8", newline="\n")
    print(f"Created {manifest_path}")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    try:
        data = load_json(args.manifest)
    except ManifestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    errors = validate_manifest(data, strict=args.strict)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Manifest validation: FAIL ({len(errors)} error(s))")
        return 1
    print("Manifest validation: PASS")
    return 0


def command_fingerprint(args: argparse.Namespace) -> int:
    try:
        data = load_json(args.manifest)
    except ManifestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    changed = add_fingerprint_hashes(data)
    if args.write:
        write_json_atomic(args.manifest, data)
    for metric in data.get("metrics", []):
        if metric.get("fingerprint_hash"):
            print(f"{metric.get('metric_id')}: {metric['fingerprint_hash']}")
    print(f"Fingerprint update: {changed} change(s){' written' if args.write else ' calculated'}")
    return 0


def command_stale(args: argparse.Namespace) -> int:
    try:
        data = load_json(args.manifest)
    except ManifestError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    stale, changed = stale_artifacts(data, write=args.write)
    if args.write and changed:
        write_json_atomic(args.manifest, data)
    if stale:
        for item in stale:
            print(f"STALE: {item}")
        print(f"Stale check: FOUND ({len(stale)} artifact(s), {changed} updated)")
        return 1 if args.fail_on_stale else 0
    print("Stale check: PASS")
    return 0


def command_scan(args: argparse.Namespace) -> int:
    findings = scan_path(args.path.resolve())
    if findings:
        for finding in findings:
            print(f"ERROR: {finding}", file=sys.stderr)
        print(f"Portability scan: FAIL ({len(findings)} finding(s))")
        return 1
    print("Portability scan: PASS")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create an analysis folder and manifest")
    init_parser.add_argument("output", type=Path)
    init_parser.add_argument("--analysis-id", required=True)
    init_parser.add_argument("--force", action="store_true")
    init_parser.set_defaults(func=command_init)

    validate_parser = subparsers.add_parser("validate", help="validate manifest structure and governance")
    validate_parser.add_argument("manifest", type=Path)
    validate_parser.add_argument("--strict", action="store_true")
    validate_parser.set_defaults(func=command_validate)

    fingerprint_parser = subparsers.add_parser("fingerprint", help="calculate metric fingerprint hashes")
    fingerprint_parser.add_argument("manifest", type=Path)
    fingerprint_parser.add_argument("--write", action="store_true")
    fingerprint_parser.set_defaults(func=command_fingerprint)

    stale_parser = subparsers.add_parser("stale", help="detect artifacts with changed metric fingerprints")
    stale_parser.add_argument("manifest", type=Path)
    stale_parser.add_argument("--write", action="store_true")
    stale_parser.add_argument("--fail-on-stale", action="store_true")
    stale_parser.set_defaults(func=command_stale)

    scan_parser = subparsers.add_parser("scan", help="scan text files for secrets and machine paths")
    scan_parser.add_argument("path", type=Path)
    scan_parser.set_defaults(func=command_scan)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
