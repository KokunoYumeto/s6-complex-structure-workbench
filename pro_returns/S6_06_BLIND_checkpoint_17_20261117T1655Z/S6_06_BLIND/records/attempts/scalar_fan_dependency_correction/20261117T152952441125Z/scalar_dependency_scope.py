#!/usr/bin/env python3
"""Retain prior scalar-fan arithmetic with explicit post-audit field scopes.

This postprocessor changes metadata only. It does not recompute a return,
alter source/root/topology data, or edit the master manuscript. Every prior
byte and every changed JSON field is recorded before a mutation.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import os
import re
import tempfile

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "records/attempts/scalar_fan_dependency_correction"
LEDGER = "records/scalar_fan_correction_scope.json"
NOTICE = (
    "Post-checkpoint15 scope correction: P3K.61 disproves the marked "
    "full-plumbing equivariant-product premise used for the old scalar "
    "initial data. Prior all-fan expressions and ranges are withdrawn "
    "return assertions; their symbolic arithmetic is retained. P3K.62 "
    "proves the two initial native comparisons and P3K.64 proves the "
    "canonical physical-vertical-edge fan line only."
)

RULES = {
    "P3K.17": {
        "retained": "Exact local Cox rays, weights, charged cap maps and full parameter units.",
        "withdrawn": ["own_value", "scope"],
        "statement": "The exact local Cox and charged-cap maps are retained; the earlier zero correction for the full OS49 outer normal line and the resulting two-fan equality are withdrawn.",
    },
    "P3K.25": {
        "retained": "Exact whole-I1 torus/shear/Cox maps and independently computed initial reference values.",
        "withdrawn": ["statement"],
        "reference_only": ["indices", "oriented_classes_mod_28"],
        "statement": "The actual scalar shear and local Cox maps are retained. The claimed equality on every physical-vertical-edge fan is withdrawn; the corrected canonical-loop formula is P3K.64.",
    },
    "P3K.29": {
        "retained": "Integral common-exterior topology, meridian and dual bases, variation symmetry, and the exact local frame-change identity.",
        "withdrawn": ["variation_initial", "variation_after_fixed_flop_factor", "nonfixed_relative_n"],
        "statement": "Integral common-exterior topology and local frame identities remain proved. The scalar rank-one initial variation and zero nonfixed derivative inferred from a simultaneous equivariant product are withdrawn.",
    },
    "P3K.31": {
        "retained": "The explicit single-star product-frame arrow, native boundary flop, and complex normal reset in their stated local markings.",
        "withdrawn": ["statement", "K27_class_ranges", "original_loop"],
        "local_only": ["ambient_frame_change", "recurrence"],
        "statement": "The local single-star frame, flop and reset maps are retained. The universal scalar-fan polynomial and numerical ranges based on the withdrawn K29 initial data are not active return results.",
    },
    "P3K.33": {
        "retained": "Actual original/higher parameter, root, cap and cusp endpoint morphisms; the independent reference fixed-star comparison.",
        "withdrawn": ["original_fan_classes", "explicit_nonzero_fan"],
        "reference_only": ["original_pair", "higher_pair"],
        "statement": "The actual shorter original/higher endpoint descent and reference fixed-star result are retained; no simultaneous equivariant whole-plumbing product or universal fan formula is inferred.",
    },
    "P3K.34": {
        "retained": "Component-supported source, line, root, cap and positive-fan page maps, with the independent positive-fan index zero.",
        "withdrawn": ["all_fan", "fixed_k_range", "common_exterior_initial_variation",
                      "common_exterior_initial_derivative", "arbitrary_fan",
                      "primitive_fan_witnesses"],
        "reference_only": ["k_Jin", "ell", "m_relative", "n_relative",
                           "individual_pair", "relative_pair", "index",
                           "normal_pontryagin"],
    },
    "P3K.35": {
        "retained": "Actual finite-root, line, period, cyclic norm and shorter-parameter morphisms, and the independently matched reference fixed-star calculation.",
        "withdrawn": ["all_fan"],
        "reference_only": ["k", "ell", "A"],
        "statement": "All thirty whole-I1 branches have the retained actual shorter endpoint descent. Its reference fixed-star calculation is separate from the withdrawn simultaneous-product and all-fan assertions.",
    },
    "P3K.36": {
        "retained": "The one-u holomorphic endpoint obstruction, actual corrected degree-two family, and independent reference fixed-star result.",
        "withdrawn": ["all_fan_class", "fan_class"],
        "reference_only": ["corrected_pair", "relative_pair", "vertical_fan_class"],
    },
    "P3K.37": {
        "retained": "Actual OS49 component divisor, root character, cap square, cyclic norm and shorter-parameter family morphism.",
        "withdrawn": ["all_fan", "k1_range", "all_k_range", "exact_scalar_example"],
        "reference_only": ["k", "ell", "A", "relative_coordinates"],
        "statement": "The actual OS49 shorter endpoint descent is retained. Its old default-fan zero value and universal fan expression are not active results; the corrected two-fan comparison is handled separately in P3K.65.",
    },
    "P3K.41": {
        "retained": "The marked cap-data comparison, finite kernels, scalar winding and actual reduction to an iterate of the constructed shorter return.",
        "withdrawn": ["all_fan", "fan_formula"],
        "retained_row": True,
    },
    "P3K.43": {
        "retained": "The actual closed marked moving-site family morphism, fixed-scalar triviality and reduction to the constructed shorter scalar return.",
        "withdrawn": ["all_fan", "fan_formula"],
        "retained_row": True,
    },
    "P3K.44": {
        "retained": "The actual component-line cap comparison, fixed-scalar triviality, scalar winding and reduction to an iterate of the constructed OS49 return.",
        "withdrawn": ["all_fan", "fan_formula"],
        "retained_row": True,
    },
}

CERTIFICATES = {
    "code/part3_fourfold/cox_flop.json":
        ("P3K.17", []),
    "code/part3_fourfold/whole_i1_shear.json":
        ("P3K.25", []),
    "code/part3_fourfold/common_exterior_meridians.json":
        ("P3K.29", ["primitive_scalar_cases"]),
    "code/part3_fourfold/common_exterior_frame_recurrence.json":
        ("P3K.31", ["initial_V", "initial_delta", "after_fixed_flop_m",
                    "after_fixed_flop_n", "central_formula", "primitive_cases"]),
    "code/part3_fourfold/original_cox_descent_universal.json":
        ("P3K.33", ["original_fan_formula", "original_KL1_range"]),
    "code/part3/os49_full_framing.json":
        ("P3K.34", ["common_exterior_initial_variation",
                    "common_exterior_initial_derivative", "arbitrary_fan",
                    "fixed_k_range", "primitive_fan_witnesses"]),
    "code/part3_fourfold/weighted_shorter_loop.json":
        ("P3K.35", []),
    "code/part3/liu_rollenske_parameter.json":
        ("P3K.36", ["fan_class"]),
    "code/part3_fourfold/os49_shorter_loop.json":
        ("P3K.37", ["fan_class", "integer_odd_S_form", "k1_fan_residues",
                    "k1_primitive_witnesses", "all_k_fan_residues"]),
    "code/part3/fixed_source_cap_loops.json": ("P3K.41", []),
    "code/part3/moving_order_one_sites.json": ("P3K.43", []),
    "code/part3/os49_cap_loops.json": ("P3K.44", []),
}

JSON_PATHS = [
    "code/part3/results_mapping.json",
    "code/part3_fourfold/results_mapping.json",
    "code/part3/canonical_scalar_catalogue.json",
    "code/part3/os49_full_framing_results_mapping.json",
    "code/part3/liu_rollenske_parameter_results_mapping.json",
    "code/part3/named_loop_coverage_results_mapping.json",
    *CERTIFICATES,
]

def scope_record(sid, rule):
    return {
        "statement": sid,
        "current_claim_status": (
            "Proved in the retained morphism scope; numerical universal fan application withdrawn"
            if rule.get("retained_row") else
            "Compound prior assertion partly withdrawn; listed independent scope retained"
        ),
        "retained_scope": rule["retained"],
        "withdrawn_formula_role": "Historical symbolic arithmetic; not an active return value",
        "ledger": LEDGER,
        "correction_proofs": ["P3K.61", "P3K.62"],
        "canonical_vertical_fan_repair": "P3K.64, with its exact canonical closing scope",
        "negative_OS49_scope": "No negative-fan zero value is retained from K17/K34/K37",
    }

def flag_fields(obj, names, value):
    marks = obj.setdefault("field_scope", {})
    for name in names:
        if name in obj:
            marks[name] = value
    if not marks:
        obj.pop("field_scope", None)

def apply_rule(row, sid, *, certificate=False):
    rule = RULES[sid]
    row["audit_scope_correction"] = scope_record(sid, rule)
    if not certificate and "status" in row:
        row.setdefault("prior_promotion_status", row["status"])
        row["status"] = (
            "Proved (retained actual-morphism scope only)"
            if rule.get("retained_row") else
            "Unresolved compound assertion; independent scope retained"
        )
    if not certificate and "statement" in rule and row.get("statement") != rule["statement"]:
        row.setdefault("superseded_statement", row.get("statement"))
        row["statement"] = rule["statement"]
    withdrawn = [("superseded_statement" if x == "statement" else x)
                 for x in rule.get("withdrawn", [])]
    flag_fields(row, withdrawn,
                "WITHDRAWN_PRIOR_FORMULA_ARITHMETIC; not an active return value")
    flag_fields(row, ["superseded_statement"],
                "HISTORICAL_PRIOR_ASSERTION; replaced by the current scoped statement")
    if "statement" in rule and "field_scope" in row:
        row["field_scope"].pop("statement", None)
    flag_fields(row, rule.get("reference_only", []),
                "REFERENCE_SCOPE_ONLY; no arbitrary-fan or negative-OS49 inference")
    flag_fields(row, rule.get("local_only", []),
                "LOCAL_MAP_ONLY; use actual independently constructed product/initial data")
    if isinstance(row.get("own_value"), dict):
        flag_fields(row["own_value"], rule.get("withdrawn", []),
                    "WITHDRAWN_PRIOR_FORMULA_ARITHMETIC; not an active return value")
        flag_fields(row["own_value"], rule.get("reference_only", []),
                    "REFERENCE_SCOPE_ONLY; no arbitrary-fan or negative-OS49 inference")
    if "audit" in row or "audits" in row:
        row["prior_audit_role"] = (
            "Earlier audit history retained verbatim. Its withdrawn scalar-fan conclusion "
            "is superseded by this field-level correction."
        )

def mutate(path, data):
    # Apply only exact known statement identifiers; source/root data remain untouched.
    def walk(value):
        if isinstance(value, dict):
            sid = value.get("id")
            candidate = value.get("statement")
            if sid not in RULES and isinstance(candidate, str) and candidate in RULES:
                sid = candidate
            if sid in RULES:
                apply_rule(value, sid)
            for k, child in list(value.items()):
                if k not in {"audit_scope_correction", "field_scope"}:
                    walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)
    if path not in CERTIFICATES:
        walk(data)

    if path in CERTIFICATES:
        sid, extra = CERTIFICATES[path]
        apply_rule(data, sid, certificate=True)
        flag_fields(data, extra,
                    "WITHDRAWN_PRIOR_FORMULA_ARITHMETIC; exact algebra does not prove its return application")
        # A numerical/SymPy PASS remains a certificate PASS, never a proof promotion.
        if str(data.get("status", "")).startswith("Proved"):
            data.setdefault("prior_status", data["status"])
            data["status"] = "PASS (retained exact arithmetic; mathematical scope corrected)"
        data["certificate_scope_notice"] = NOTICE
        if sid == "P3K.17" and data.get("scope", "").startswith("Code certifies"):
            data.setdefault("prior_scope", data["scope"])
            data["scope"] = (
                "Exact local matrices and charged cap maps are certified. The prior "
                "complete outer family/collar equality is withdrawn; these matrices "
                "do not evaluate the missing outer normal-line contribution."
            )
        if sid == "P3K.17":
            data.get("field_scope", {}).pop("scope", None)
            data.get("field_scope", {}).pop("closed_correction_monodromy", None)
            flag_fields(data, ["prior_scope"],
                        "HISTORICAL_PRIOR_ASSERTION; full outer comparison withdrawn")
        if sid == "P3K.29":
            for case in data.get("primitive_scalar_cases", []):
                flag_fields(case, ["product_variation_K23", "dual_cycle_variation_v",
                                   "initial_variation", "after_fixed_edge_variation",
                                   "nonfixed_edge_relative_n_before_fixed_edge_flop"],
                            "WITHDRAWN_SCALAR_INITIAL_DATA; topology and meridian matrices retained")
        if sid == "P3K.37":
            flag_fields(data, ["short_pair", "short_index"],
                        "PRIOR_REFERENCE_ARITHMETIC; not an active default-negative-fan result")

    if path == "code/part3/canonical_scalar_catalogue.json":
        data["mathematical_scope_correction"] = {
            "source_root_cap_topology": "Retained",
            "reference_page_chi_H_A": "Retained",
            "all_fan_return_application": "WITHDRAWN_PRIOR_FORMULA_ARITHMETIC",
            "status_PASS_means": "Exact arithmetic checks only; it does not promote the withdrawn return application",
            "canonical_vertical_fan_repair": "P3K.64: A(T_n)=A(T_0)-M*n*(n-1)/2 for lambda=r^M and its exact closing",
            "ledger": LEDGER,
        }
        def flag_catalogue(obj):
            if isinstance(obj, dict):
                if "all_fan" in obj:
                    flag_fields(obj, ["all_fan", "fan_coordinate", "fan_S"],
                                "WITHDRAWN_PRIOR_FORMULA_ARITHMETIC; not an active return result")
                for k, x in list(obj.items()):
                    if k not in {"field_scope", "mathematical_scope_correction"}:
                        flag_catalogue(x)
            elif isinstance(obj, list):
                for x in obj:
                    flag_catalogue(x)
        flag_catalogue(data)
        data["withdrawn_formula_checks"] = [
            x for x in data.get("checks", [])
            if isinstance(x, str) and "all-fan" in x
        ]
        data["withdrawn_formula_checks_role"] = (
            "These are correct symbolic identities of the recorded prior polynomial, "
            "not tests of the missing geometric premise."
        )

    if path == "code/part3/named_loop_coverage_results_mapping.json":
        for row in data.get("fully_compared_rows", []):
            old = row.get("scope", "")
            phrase = "The independently constructed other fans have the separate K33 formula and do not replace that specified fan."
            if phrase in old:
                row.setdefault("prior_scope", old)
                row["scope"] = old.replace(
                    phrase,
                    "Only the specified reference construction is compared here. The old K33 other-fan formula is withdrawn; no value for another fan follows from this row."
                )
        data["audit_scope_correction"] = {
            "retained": "Named reference-family loop morphisms and stated reference values",
            "withdrawn": "The old all-fan K33 side assertion in each scope field",
            "ledger": LEDGER,
        }

    if path == "code/part3/results_mapping.json":
        for row in data.get("prompt_statements_not_separate_csv_rows", []):
            if row.get("statement") == "OS49 IV*+II+I2 component-supported target":
                row.setdefault("superseded_own_value", row["own_value"])
                row.setdefault("superseded_comparison", row["comparison"])
                row["comparison"] = "Exact topology retained; actual two-fan returns corrected by P3K.65"
                row["own_value"] = (
                    "The actual order3k cap topology, complete freeness criterion, and "
                    "noncoprime homology remain proved by F26/F29/F33/F34. For n=+/-1 "
                    "every fixed delta twist gives S6. The positive-diagonal filling "
                    "has index0, class0 and a product mapping torus by the actual "
                    "F31/F32 page and line maps. P3K.65 proves that the negative "
                    "fan has oriented class -3k mod28 for one positive r-loop "
                    "with lambda=r^(3k), and class -k mod28 for one positive "
                    "shorter w-loop with lambda=w^k, w=r^3. The positive fan "
                    "has integer index0 and class0 on both actual parameters. "
                    "Both norm signs and every fixed delta character are retained. "
                    "No negative-fan integer index is assigned. The old K17 "
                    "zero-both assertion is preserved as superseded."
                )
                if "P3K.65" not in row["proof_ids"]:
                    row["proof_ids"].append("P3K.65")
                row["corrected_actual_return_scope"] = {
                    "proof": "P3K.65",
                    "r_parameter": "lambda=r^(3k), one positive r-loop",
                    "w_parameter": "lambda=w^k, w=r^3, one positive w-loop",
                    "negative_fan_classes": {"r": "-3k mod28", "w": "-k mod28"},
                    "positive_fan_integer_index": {"r": 0, "w": 0},
                    "positive_fan_classes": {"r": 0, "w": 0},
                    "negative_fan_integer_index": "UNASSIGNED",
                    "norm_signs": [-1, 1], "delta_character": "Every fixed integer d",
                }
                row["field_scope"] = {
                    "superseded_own_value": "Historical prior compound assertion, not an active result",
                    "superseded_comparison": "Historical prior comparison label",
                }

    return data

def differences(old, new, pointer=""):
    out = []
    if isinstance(old, dict) and isinstance(new, dict):
        for key in sorted(set(old) | set(new)):
            p = pointer + "/" + key.replace("~", "~0").replace("/", "~1")
            if key not in old:
                out.append({"pointer": p, "operation": "add", "old": None, "new": new[key]})
            elif key not in new:
                out.append({"pointer": p, "operation": "remove", "old": old[key], "new": None})
            else:
                out.extend(differences(old[key], new[key], p))
    elif isinstance(old, list) and isinstance(new, list) and len(old) == len(new):
        for i, (a, b) in enumerate(zip(old, new)):
            out.extend(differences(a, b, pointer + "/" + str(i)))
    elif old != new:
        out.append({"pointer": pointer, "operation": "replace", "old": old, "new": new})
    return out

def atomic_write(path, content):
    with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False) as f:
        f.write(content)
        temp = Path(f.name)
    os.replace(temp, path)

def enforce_paths(paths=JSON_PATHS, *, origin="manual field-level audit"):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory = ARCHIVE / stamp
    changes = []
    for rel in paths:
        p = ROOT / rel
        if not p.exists():
            continue
        raw = p.read_bytes()
        old = json.loads(raw)
        new = mutate(rel, copy.deepcopy(old))
        diff = differences(old, new)
        if not diff:
            continue
        backup = directory / rel
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_bytes(raw)
        encoded = json.dumps(new, indent=2, ensure_ascii=False) + "\n"
        atomic_write(p, encoded)
        changes.append({
            "file": rel, "before_sha256": hashlib.sha256(raw).hexdigest(),
            "after_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
            "original": str(backup.relative_to(ROOT)), "field_changes": diff,
        })
    if changes:
        directory.mkdir(parents=True, exist_ok=True)
        record = {
            "utc": datetime.now(timezone.utc).isoformat(), "origin": origin,
            "notice": NOTICE, "main_input_modified": False,
            "changes": changes,
        }
        (directory / "field_changes.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        atomic_write(ROOT / "records/scalar_fan_raw_scope_latest.json",
                     json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return changes

def enforce_tex_paths(paths, *, origin="historical exporter scope restoration"):
    """Restore an already adopted quarantine on a regenerated individual include.

    Never touches notes/part3.tex, the master, or the report. The prior proof
    remains verbatim after the explicit correction notice.
    """
    scope = json.loads((ROOT / LEDGER).read_text())["scope"]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory = ARCHIVE / stamp
    changes = []
    for rel in paths:
        if rel in {"notes/part3.tex", "S6_06_BLIND_paper.tex"}:
            raise ValueError("Root-owned aggregate input must not be edited here")
        p = ROOT / rel
        if not p.exists():
            continue
        old = p.read_text()
        new = old
        replacements = []
        for sid, rule in scope.items():
            if rule["file"] != rel:
                continue
            before = "\\begin{statement}{" + sid + "}{Proved}"
            if before not in new:
                continue
            message = (
                "\\par\\noindent\\textbf{Audit correction, 17 November 2026.} "
                + rule["correction"]
                + " The prior argument is retained below as a superseded compound "
                  "claim; only the explicitly retained scope remains proved. "
                  "See P3K.61--62 and the correction ledger.\n"
            )
            after = ("\\begin{statement}{" + sid
                     + "}{Unresolved; scalar-fan audit correction}\n" + message)
            new = new.replace(before, after, 1)
            replacements.append({"old": before, "new": after})
        if new == old:
            continue
        backup = directory / rel
        backup.parent.mkdir(parents=True, exist_ok=True)
        backup.write_text(old)
        atomic_write(p, new)
        changes.append({
            "file": rel, "original": str(backup.relative_to(ROOT)),
            "before_sha256": hashlib.sha256(old.encode()).hexdigest(),
            "after_sha256": hashlib.sha256(new.encode()).hexdigest(),
            "exact_replacements": replacements,
        })
    if changes:
        (directory / "regenerated_include_scope.json").write_text(json.dumps({
            "utc": datetime.now(timezone.utc).isoformat(), "origin": origin,
            "main_input_modified": False, "changes": changes,
        }, indent=2) + "\n")
    return changes

def postprocess_generated(json_paths, tex_paths=(), *, origin="historical generator"):
    result = enforce_paths(json_paths, origin=origin)
    tex = enforce_tex_paths(tex_paths, origin=origin)
    print("POST-AUDIT SCOPE: prior all-fan arithmetic is withdrawn as a return "
          "assertion; actual source/root/topology/local-map data retain their "
          "listed scopes. JSON changes:", len(result), "include notices:", len(tex))
    return result, tex

if __name__ == "__main__":
    result = enforce_paths()
    print("Applied explicit scalar-fan scope to", len(result), "JSON artifacts; prior bytes and every old→new field preserved.")
