from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "analysis_guard.py"
SPEC = importlib.util.spec_from_file_location("analysis_guard", MODULE_PATH)
assert SPEC and SPEC.loader
analysis_guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analysis_guard)


def valid_manifest() -> dict:
    data = json.loads((ROOT / "assets" / "analysis-manifest.template.json").read_text(encoding="utf-8"))
    data["analysis_id"] = "2026-01-01-generic-analysis"
    data["needs_discovery"].update(
        {
            "mode": "deep",
            "triggers": ["metric-led request"],
            "inferred_business_need": "Support a prioritization decision.",
            "evidence_ceiling": "Observational association only.",
            "framing_status": "confirmed",
        }
    )
    data["question_tree"].update(
        {
            "status": "operational",
            "primary_problem_type": "find_patterns",
            "secondary_problem_types": ["discover_connections"],
        }
    )
    data["question_tree"]["questions"] = [
        {
            "question_id": "Q1",
            "parent_id": None,
            "text": "How is the eligible population distributed?",
            "role": "core",
            "problem_type": "find_patterns",
            "decision_relevance": "Establish the decision baseline.",
            "source_ids": ["S1"],
            "metric_ids": ["M1"],
            "method": "Exclusive distribution.",
            "validation_rules": ["Complete expected domain."],
            "expected_output": "Reviewed distribution.",
            "status": "operational",
        }
    ]
    data["contract"].update(
        {
            "status": "approved",
            "risk": "medium",
            "audience": ["decision team"],
            "owner": "analysis owner",
            "population": "Eligible entities",
            "period": {"start": "2026-01-01", "end": "2026-01-31", "timezone": "UTC"},
            "primary_grain": "entity",
            "definition_of_done": "The core question has an approved claim.",
            "approval_gates": ["claim promotion"],
        }
    )
    data["sources"] = [
        {
            "source_id": "S1",
            "name": "Canonical source",
            "owner": "source owner",
            "authority": "canonical",
            "source_grain": "event",
            "coverage": "Eligible population",
            "freshness": {"valid_as_of": "2026-01-31", "revalidate_after": "2026-02-28"},
            "join_keys": ["entity_id"],
            "joinability": "direct",
            "allowed_uses": ["population metrics"],
            "forbidden_uses": ["causal claims"],
            "access_and_pii": "No personal data exported.",
            "caveats": [],
        }
    ]
    fingerprint = {
        "population": "Eligible entities",
        "calculation_grain": "entity",
        "time_window": {"start": "2026-01-01", "end": "2026-01-31", "timezone": "UTC"},
        "scope": {"market": "all"},
        "filters": ["valid_record = true"],
        "numerator": "Distinct eligible entities in the class",
        "denominator": "Distinct eligible entities",
        "deduplication": "One maximum class per entity",
        "source_query_ref": "evidence/query.sql",
        "run_date": "2026-02-01",
    }
    fingerprint_hash = analysis_guard.stable_hash(fingerprint)
    data["question_tree"]["questions"][0]["metric_fingerprints"] = {
        "M1": fingerprint_hash
    }
    data["metrics"] = [
        {
            "metric_id": "M1",
            "name": "Maximum observed class",
            "question_ids": ["Q1"],
            "source_ids": ["S1"],
            "metric_shape": "exclusive_distribution",
            "status": "validated",
            "expected_domain": [0, 20, 40, 60, 80, 100],
            "observed_domain": [0, 20, 40, 60, 80, 100],
            "definition_fingerprint": fingerprint,
            "fingerprint_hash": fingerprint_hash,
        }
    ]
    data["evidence"] = [
        {
            "evidence_id": "E1",
            "question_ids": ["Q1"],
            "source_ids": ["S1"],
            "result_ref": "evidence/result.csv",
            "status": "validated",
        }
    ]
    data["claims"] = [
        {
            "claim_id": "C1",
            "question_ids": ["Q1"],
            "statement": "The eligible population spans the complete expected domain.",
            "status": "approved",
            "evidence_posture": "verified",
            "evidence_refs": ["E1"],
            "metric_ids": ["M1"],
            "metric_fingerprints": {"M1": fingerprint_hash},
            "valid_as_of": "2026-01-31",
            "caveats": [],
            "alternative_explanations": [],
            "owner": "analyst",
            "approved_by": "reviewer",
            "approved_at": "2026-02-02",
            "supersedes": [],
        }
    ]
    data["visuals"] = [
        {
            "visual_id": "V1",
            "claim_ids": ["C1"],
            "question_id": "Q1",
            "result_ref": "evidence/result.csv",
            "message": "The distribution includes every expected class.",
            "communication_function": "distribution",
            "data_structure": {"metric_shape": "exclusive_distribution", "ordered": True},
            "candidate_charts": ["ordered_bar"],
            "selected_chart": "ordered_bar",
            "rejected_alternatives": ["funnel"],
            "required_labels": ["population", "denominator", "period"],
            "live_catalogue_checked": True,
            "intended_use": "stakeholder",
            "qa_status": "passed",
        }
    ]
    data["recommendations"] = [
        {
            "recommendation_id": "R1",
            "decision_id": "D1",
            "supporting_claim_ids": ["C1"],
            "action": "Use the complete distribution in decision material.",
        }
    ]
    data["artifacts"] = [
        {
            "artifact_id": "A1",
            "purpose": "stakeholder brief",
            "path": "stakeholder-brief.pptx",
            "status": "active",
            "depends_on": ["M1", "C1", "V1"],
            "metric_fingerprints": {"M1": fingerprint_hash},
        }
    ]
    return data


class ManifestValidationTest(unittest.TestCase):
    def test_template_passes_non_strict_validation(self) -> None:
        template = analysis_guard.load_json(ROOT / "assets" / "analysis-manifest.template.json")
        self.assertEqual([], analysis_guard.validate_manifest(template))

    def test_complete_manifest_passes_strict_validation(self) -> None:
        self.assertEqual([], analysis_guard.validate_manifest(valid_manifest(), strict=True))

    def test_missing_zero_or_expected_class_is_rejected(self) -> None:
        data = valid_manifest()
        data["metrics"][0]["observed_domain"] = [20, 40, 60, 80, 100]
        errors = analysis_guard.validate_manifest(data, strict=True)
        self.assertTrue(any("missing expected values: [0]" in error for error in errors), errors)

    def test_exclusive_distribution_cannot_use_funnel(self) -> None:
        data = valid_manifest()
        data["visuals"][0]["selected_chart"] = "funnel"
        errors = analysis_guard.validate_manifest(data, strict=True)
        self.assertTrue(any("cannot use a funnel" in error for error in errors), errors)

    def test_stakeholder_visual_requires_approved_claim(self) -> None:
        data = valid_manifest()
        data["claims"][0]["status"] = "validated"
        errors = analysis_guard.validate_manifest(data)
        self.assertTrue(any("uses non-approved claim" in error for error in errors), errors)

    def test_approved_claim_requires_approval_metadata(self) -> None:
        data = valid_manifest()
        data["claims"][0]["approved_by"] = ""
        errors = analysis_guard.validate_manifest(data)
        self.assertTrue(any("approved_by and approved_at" in error for error in errors), errors)

    def test_changed_fingerprint_marks_artifact_stale(self) -> None:
        data = valid_manifest()
        data["metrics"][0]["definition_fingerprint"]["population"] = "Changed population"
        stale, changed = analysis_guard.stale_artifacts(data, write=True)
        self.assertEqual(2, len(stale))
        self.assertEqual(2, changed)
        self.assertEqual("candidate", data["claims"][0]["status"])
        self.assertEqual("needs_validation", data["claims"][0]["evidence_posture"])
        self.assertEqual("stale", data["artifacts"][0]["status"])

    def test_comparison_requires_compatible_fingerprints_or_rationale(self) -> None:
        data = valid_manifest()
        second = copy.deepcopy(data["metrics"][0])
        second["metric_id"] = "M2"
        second["definition_fingerprint"]["population"] = "Different population"
        second["fingerprint_hash"] = analysis_guard.stable_hash(second["definition_fingerprint"])
        data["metrics"].append(second)
        data["claims"][0]["comparison_metric_ids"] = ["M1", "M2"]
        errors = analysis_guard.validate_manifest(data)
        self.assertTrue(any("incompatible fingerprints without rationale" in error for error in errors), errors)

    def test_validated_claim_requires_metric_snapshot(self) -> None:
        data = valid_manifest()
        data["claims"][0]["metric_fingerprints"] = {}
        errors = analysis_guard.validate_manifest(data, strict=True)
        self.assertTrue(any("missing metric fingerprint snapshots" in error for error in errors), errors)

    def test_active_artifact_requires_transitive_metric_snapshot(self) -> None:
        data = valid_manifest()
        data["artifacts"][0]["depends_on"] = ["C1", "V1"]
        data["artifacts"][0]["metric_fingerprints"] = {}
        errors = analysis_guard.validate_manifest(data, strict=True)
        self.assertTrue(any("missing metric fingerprint snapshots" in error for error in errors), errors)

    def test_strict_request_coverage_must_include_every_stated_item(self) -> None:
        data = valid_manifest()
        data["needs_discovery"]["stated_request"] = [
            {"request_item_id": "R1", "text": "Describe the distribution."}
        ]
        errors = analysis_guard.validate_manifest(data, strict=True)
        self.assertTrue(any("request coverage missing stated items" in error for error in errors), errors)

    def test_init_creates_minimal_visible_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            args = type("Args", (), {"output": Path(temp) / "run", "analysis_id": "example-run", "force": False})
            self.assertEqual(0, analysis_guard.command_init(args))
            self.assertTrue((Path(temp) / "run" / "analysis-manifest.json").exists())
            self.assertTrue((Path(temp) / "run" / "evidence").is_dir())
            self.assertTrue((Path(temp) / "run" / "results.md").exists())

    def test_portability_scan_detects_secret_and_absolute_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "unsafe.txt"
            path.write_text(
                "api_key = '1234567890abcdefghijklmnop'\n"
                "source = 'C:\\\\Users\\\\Example\\\\private.csv'\n",
                encoding="utf-8",
            )
            findings = analysis_guard.scan_path(Path(temp))
            self.assertTrue(any("possible secret" in finding for finding in findings), findings)
            self.assertTrue(any("machine-specific absolute path" in finding for finding in findings), findings)


class RuntimeContractTest(unittest.TestCase):
    def test_all_six_problem_types_are_documented(self) -> None:
        text = (ROOT / "references" / "problem-type-playbooks.md").read_text(encoding="utf-8")
        headings = {
            "make_predictions": "## Make Predictions",
            "categorise_things": "## Categorise Things",
            "spot_unusual": "## Spot Something Unusual",
            "identify_themes": "## Identify Themes",
            "discover_connections": "## Discover Connections",
            "find_patterns": "## Find Patterns",
        }
        self.assertEqual(analysis_guard.PROBLEM_TYPES, set(headings))
        for heading in headings.values():
            self.assertIn(heading, text)

    def test_needs_discovery_and_question_tree_are_routed_before_execution(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertLess(skill.index("Interpret The Request"), skill.index("Execute Bounded Work"))
        reference = (ROOT / "references" / "needs-discovery-and-analysis-contract.md").read_text(encoding="utf-8")
        for term in ("Decision-Backward Framing", "Analytical Laddering", "Question Tree", "Decision Lineage"):
            self.assertIn(term, reference)

    def test_runtime_portability_scan_passes(self) -> None:
        runtime_paths = [ROOT / "SKILL.md", ROOT / "agents", ROOT / "references", ROOT / "assets", ROOT / "scripts"]
        for runtime_path in runtime_paths:
            findings = analysis_guard.scan_path(runtime_path)
            self.assertEqual([], findings, f"portability findings in {runtime_path}: {findings}")


if __name__ == "__main__":
    unittest.main()
