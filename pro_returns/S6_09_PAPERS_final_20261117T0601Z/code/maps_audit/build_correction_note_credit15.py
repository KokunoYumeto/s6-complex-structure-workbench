#!/usr/bin/env python3
"""Build a bounded attribution overlay; never modify sources or inventory."""
from pathlib import Path
import csv
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "deliverables/work/maps_audit"
SOURCE = "sources/correction_note/N_singular_fibre_vanishing_step.tex"
READER = {"model": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro",
          "date": "2026-11-17 UTC", "agent": "/root/maps_audit"}

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def read_json(path):
    return json.loads((ROOT / path).read_text())

mapping_path = "deliverables/work/cdp_audit/working_supplement_mapping.json"
canonical_path = "deliverables/work/cdp_audit/credit_comparison_239.json"
mapping = {r["source_id"]: r for r in read_json(mapping_path)["rows"]
           if r["source_run"] == "CORRECTION_NOTE_20260901"}
canonical = {r["source_id"]: r for r in read_json(canonical_path)}
elsewhere_index = read_json("deliverables/work/cdp_audit/credit_elsewhere_searches_239.json")
corpora = {
    "AC26": ["sources/external/root/AC26_pdf_text.txt"],
    "E26": ["sources/papers/arXiv_2609.38442_Engel_src/S6.tex"],
    "DGKX_v1": ["sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie_src/v5oka_maps_modifications_deformations.tex"],
    "DGKX_v2": ["sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie_src/submited-tams.tex"],
    "elsewhere": [r["path"] for r in elsewhere_index["files"]],
}

# Each description was matched to the complete receiving source and the
# stated actually opened original context, not inferred from keyword hits.
specs = [
    ("lem:torsion-identification", "Torsion is the kernel of restriction to the smooth locus", None,
     ["torsion", "minimal primes", "nonzerodivisor", "smooth locus"],
     "AC26 §10.1, p.85, definition of torsion; Lemma10.3(b), p.87",
     "The same torsion convention and dense-open-support implication are used in AC26. The separate all-reduced-hypersurfaces prime-avoidance lemma is not stated there in this form.", False,
     "Classical coherent-module torsion and prime avoidance, rederived in the correction note; AC26 §10.1 and Lemma10.3(b) for the operative convention and application.",
     "Elementary localization and prime avoidance; no independent full counterpart was identified in the bounded attached-source search.", []),
    ("lem:conormal", "Left exactness of the conormal sequence for a reduced Cartier hypersurface", "A.1.1",
     ["conormal", "reduced hypersurface", "differential", "10.1"],
     "AC26 Setup10.1, p.86, equation(10.1) and the preceding local injectivity calculation",
     "AC26 proves the exact normal-crossing special case by coefficient calculation. The receiving reduced-Cartier formulation includes non-normal-crossing hypersurfaces and proves injectivity at minimal primes.", False,
     "AC26 Setup10.1/equation(10.1) for the normal-crossing case; the general conormal exact sequence and reduced-characteristic-zero injectivity are rederived here.",
     "CDP20 §7, p.692, source lines981–986, displays the conormal sequence. That displayed sequence is valid; the later endpoint inference is the separate issue.", ["CDP2020"]),
    ("prop:filtration", "The conormal/torsion inverse-image filtration", "A.1.1",
     ["conormal", "torsion", "filtration", "kernel"],
     "AC26 Lemma10.3(b), p.87; Theorem10.5 Step2, p.88; §10.4, pp.89–90",
     "The torsion-supported ambient obstruction is explicitly known in AC26. The two short exact sequences through the inverse-image sheaf are an elementary general formulation, not a separately identified full theorem in the opened AC26 scope.", False,
     "AC26 Lemma10.3 and Theorem10.5 for the prior conductor obstruction; elementary inverse-image exactness gives the general filtration, with no priority claim.",
     "CDP20 §7, p.692, supplies the displayed conormal sequence whose quotient-by-torsion step is being audited; the added inverse-image sequences are proved directly.", ["CDP2020"]),
    ("prop:criterion", "Exact kernel-of-connecting-map criterion", "A.1.1",
     ["conormal", "connecting", "torsion", "endpoint"],
     "AC26 Lemma10.3(a)–(c), pp.87–88, and §10.4, pp.89–90",
     "AC26 already identifies a nonzero ambient section with torsion intrinsic image despite the endpoint vanishings. The receiving equality with ker(delta_A) is the explicit general long-exact-sequence formulation of that obstruction.", False,
     "AC26 Lemma10.3 and §10.4 for the prior obstruction; the general ker(delta_A) formula is a direct long-exact-sequence reformulation, not a new claim of discovering the failure.",
     "CDP20 §7, p.692, source lines981–987, is the exact inference under discussion. The correction retains its full global hypotheses separately and does not infer a theorem-level counterexample from the local family.", ["CDP2020"]),
    ("lem:conductor", "Double normal-crossing normalization–conductor square", "A.2.2",
     ["conductor", "Mayer", "normaliz", "normalis"],
     "AC26 Lemma10.2, p.87, equation(10.2), full double- and triple-crossing proof",
     "Exact positive match: the receiving double-crossing sequence and its explicit (a,b,c) map are the double-point special case of AC26 Lemma10.2. Its proof is local and does not use compactness.", True,
     "Alpöge, AC26 Lemma10.2, p.87 (double-point specialization of the printed normalization–conductor sequence). Retain the full explicit local proof without novelty claim.",
     "Standard conductor pullback algebra; the canonical CDP A.2.2 also cites Granger–Schulze for a broader fractional-ideal theorem, which is not required by this elementary double-point row.", []),
    ("prop:conductor-differential", "Nonzero descended conductor differential", None,
     ["conductor", "nowhere", "torsion", "trivialising"],
     "AC26 Lemma10.3(a)–(b), p.87, together with equation(10.3) immediately above",
     "Exact prior mechanism and conclusion: a uniquely descended nonzero ambient differential with zero conductor value and torsion intrinsic image. AC26 states a proper normal-crossing setup; its parts(a)–(b) proof is local/descent-based and uses no compactness. The receiving local clauses remove that unused hypothesis.", False,
     "Alpöge, AC26 Lemma10.3(a)–(b), p.87; local conductor descent and torsion conclusion are already proved there. The no-compactness local formulation is identified explicitly.",
     "The complete proof is merged with WORKING_CDP prop:conductor; no independent novelty is claimed for the conductor differential.", []),
    ("cor:normal-crossing-kernel", "The conductor differential gives a noninjective connecting map", None,
     ["conductor", "connecting", "torsion", "10.3"],
     "AC26 Lemma10.3(a)–(c), pp.87–88; §10.4, pp.89–90",
     "Immediate reformulation of the known nonzero ambient section, combined with the printed general connecting-map criterion. The delta_A notation itself is not attributed to AC26.", False,
     "AC26 Lemma10.3 for the nonzero conductor section; the corollary is its direct consequence under the two endpoint assumptions and the retained exact-sequence criterion.",
     "No full independently named corollary located in the bounded attached-source comparison; its proof is the two-line formal combination printed in the source.", []),
    ("prop:family-geometry", "The proper nodal-cubic times P1 test family", "B1",
     ["nodal cubic", "x\\^2", "normaliz", "normalis"],
     "AC26 Setup10.1, p.86; Lemmas10.2–10.3, p.87",
     "The local normal-crossing models and normalization mechanism are prior material. The specific projective family y²z=x²(x+z)+tz³, rational parametrization and smooth-total-space verification are not found in this opened AC26 scope.", False,
     "The supplied correction note provides the explicit proper test family; AC26 §10.2 supplies the earlier conductor mechanism it instantiates. No claim of exhaustive literature priority is made for the elementary nodal smoothing.",
     "Classical nodal-cubic normalization and the projective smoothing are computed explicitly. Canonical CDP B1 repeats and refines this same supplied family; it is a source concordance, not an independent prior publication.", []),
    ("lem:gluing-bundle", "Non-torsion scalar gluing line bundle on the nodal cubic", None,
     ["gluing", "line bundle", "root of unity", "Pic"],
     "AC26 Lemma10.3(c), pp.87–88",
     "AC26 proves H0(S,A)=0 for a nontrivial line with trivial normalization pullback on a connected compact normal-crossing fibre. The explicit scalar-lambda nodal-curve gluing and tensor-power computation are a classical specialization rederived in the note.", False,
     "Classical line-bundle descent on a nodal curve, with the scalar and tensor powers computed here; AC26 Lemma10.3(c) already supplies the general normalization-trivial H0-vanishing principle.",
     "No full lambda-specific standalone result found in the bounded attached-source search. The printed c=lambda*c calculation is complete and requires no unseen Picard classification theorem.", []),
    ("lem:extending-gluing", "An extending divisor P−O with gluing multiplier 1/3", None,
     ["extending", "gluing", "1/3", "P-O"],
     "AC26 §10.2, pp.86–88, and Theorem10.5 Step1, p.88",
     "AC26 identifies normalization-trivial restrictions of global line bundles for its own compact construction. The specified local cubic sections O and P, divisor P−O, and branch-value ratio1/3 are a different explicit calculation, not found in the opened scope.", False,
     "The correction note's explicit divisor calculation; prior conductor mechanism credited to AC26 Lemma10.3. Extendability on this local proper family is not a compact-CDP counterexample.",
     "No full matching P−O/1/3 construction located in the bounded attached-source searches. Canonical CDP B1 is the internal concordant computation, not independent literature.", []),
    ("thm:nodal-test", "Failure of the unrestricted endpoint implication in a proper local test family", "B1",
     ["nodal cubic", "endpoint", "torsion", "non.torsion"],
     "AC26 Lemma10.3, pp.87–88, Theorem10.5 Step2 p.88, and §10.4 pp.89–90",
     "The conductor-supported failure mechanism is already in AC26. The independent proper nodal-cubic×P1 family and extending local twist provide a distinct complete test, not a theorem-level refutation of CDP20 under compact global hypotheses.", False,
     "AC26 Lemma10.3/§10.4 for the prior obstruction; the correction note for the explicit proper local family and all endpoint calculations. The source itself disclaims priority for the conductor mechanism.",
     "CDP20 §7, p.692, is the exact unrestricted inference tested. Its global Theorem2.2 hypotheses are explicitly not satisfied by this local family. Canonical CDP B1 is an internal refinement of the same source computation.", ["CDP2020"]),
    ("lem:generic-endpoints", "Generic H0/Hn vanishing on a specified analytic Picard parameter space", None,
     ["generic", "semi.continu", "effective divisor", "duality"],
     "AC26 §10.1, pp.85–86, discussion of the CDP strategy; no full parameter-space statement identified",
     "The discussion concerns the CDP strategy, not this precise irreducible reduced parameter space with a Poincaré bundle, dualization stability and two specified negative-divisor twists.", False,
     "Campana–Demailly–Peternell1998 Proposition1.1 and Corollaries1.2–1.3 for the smooth stabilization/generic-vanishing argument; Serre duality and analytic finite-complex semicontinuity. The note makes the parameter-space hypotheses explicit and claims no priority.",
     "CDP98 source lines234–278: full stabilization proof and Corollaries1.2–1.3 read. Only the smooth reduced case needed here is used; the unrestricted nonreduced Proposition1.1 is not silently imported. BS76 ChapterIII Theorems4.1/4.12 provide the opened precise analytic jumping-locus hypotheses; Serre1955 §13 Theorem4 supplies smooth compact duality.", ["CDP1998", "BS76", "Serre1955Duality"]),
    ("thm:corrected-global", "One H2-vanishing twist implies generic vanishing and c3≤0", None,
     ["generic", "Riemann.?Roch", "T_X", "2.4"],
     "AC26 §10.1 pp.85–86 quotes the intact CDP20 Proposition2.4 and distinguishes it from the endpoint inference",
     "AC26 discusses the intact relative hypothesis. The receiving one-absolute-H2-twist formulation is a direct conditional reformulation, not the claimed unconditional vanishing theorem or a new construction.", False,
     "CDP20 Proposition2.4 and CDP98 Corollary1.3 for the surviving strategy; the absolute-H2 formulation follows by explicit Poincaré-family semicontinuity and Hirzebruch–Riemann–Roch. No priority is claimed.",
     "CDP20 source lines327–364: intact relative criterion and the generic-equivalently-one H2 strategy. CDP98 Corollary1.3 supplies H0; Serre duality supplies H3; BS76 finite-complex semicontinuity supplies openness. Atiyah–Singer1963 Theorem3, p427, covers HRR for arbitrary compact complex manifolds; the ch/Td coefficient c3/2 is explicitly derived in the receiving proof.", ["CDP2020", "CDP1998", "BS76", "Serre1955Duality", "AtiyahSinger1963"]),
    ("cor:relative", "The intact R2 direct-image criterion", None,
     ["Riemann.?Roch", "2.4", "Serre", "Leray"],
     "AC26 §10.1, pp.85–86, verbatim discussion of CDP20 Proposition2.4",
     "The intact relative criterion is explicitly reproduced and attributed to CDP20 in AC26. This receiving corollary is a stronger-hypothesis special case of CDP20 Proposition2.4 with a full Leray/positive-curve-twist proof retained.", True,
     "Campana–Demailly–Peternell2020 Proposition2.4, p680; also quoted and distinguished from the faulty endpoint step in AC26 §10.1. The full positive-twist/Leray proof is retained without novelty claim.",
     "Exact positive original match: CDP20 Proposition2.4, source lines331–337, assumes only b2=0 plus algebraic-dimension-one holomorphic reduction; the receiving H1=H2=0 hypothesis is stronger. The conclusion and one relative-vanishing twist agree.", ["CDP2020"]),
    ("prop:relative-local", "Ordinary relative-one-form modules of xy, xyz and s^m charts", None,
     ["relative", "differential", "torsion.free", "multiple"],
     "AC26 Setup10.1 p.86 for normal-crossing chart equations; §5 finite cyclic charts only as geometric context",
     "The chart equations are prior material. The exact ordinary-relative module embeddings, rank/minimal-generator nonfreeness test and cyclic torsion summand are elementary local calculations, not a separately identified full statement in the opened AC26 contexts.", False,
     "Classical Kähler-differential presentations and UFD kernel calculations, rederived in the correction note; AC26 for the normal-crossing and cyclic chart setting. Total-space modules, fibre restrictions and ramified quotients remain explicitly distinguished.",
     "No full counterpart identified in the bounded attached-source searches. The proof computes every map and kernel; no assertion about exterior powers, a ramified quotient, global direct images or Hodge groups is attributed to these local p=1 calculations.", []),
]

source_lines = (ROOT / SOURCE).read_text().splitlines(keepends=True)
context_readings = {
    "AC26": {"file": corpora["AC26"][0], "read_lines": [[5360,5595]],
             "scope": "Primary-PDF text: §10.1, Setup10.1, Lemmas10.2–10.3 with complete proofs, Remark10.4, and Theorem10.5 Steps1–3. Original-PDF prior opening retained in the peer credit context record; this event does not claim a fresh visual opening.",
             "prior_original_opening": "deliverables/work/cdp_audit/credit_context_readings.json#contexts/AC26"},
    "E26": {"file": corpora["E26"][0], "read_lines": [[1480,1570]],
            "scope": "The actual apparent vanishing hits concern integral constructible cohomology and transgression, not the receiving coherent cotangent/endpoint statement.",
            "prior_opened_contexts": "deliverables/work/cdp_audit/credit_context_readings.json#contexts/E26"},
    "DGKX_v1": {"file": corpora["DGKX_v1"][0], "read_lines": [[9440,9492]],
                "scope": "Complete displayed tangent-cohomology theorem and proof; known standard-family tangent dimensions are distinguished from the receiving local test and conditional generic-vanishing results.",
                "prior_opened_contexts": "deliverables/work/cdp_audit/credit_context_readings.json#contexts/DGKX_v1"},
    "DGKX_v2": {"file": corpora["DGKX_v2"][0], "read_lines": [[1644,1691]],
                "scope": "Actual toric-central normalization lemma and full proof; coordinate crossing geometry is related input, not a cotangent-conductor or generic-vanishing theorem. Version2 is searched and credited separately.",
                "prior_opened_contexts": "deliverables/work/cdp_audit/credit_context_readings.json#contexts/DGKX_v2"},
    "CDP1998": {"file": "sources/papers/arXiv_math_9607215_CDP98_src/main.tex", "read_lines": [[224,288]],
                "scope": "Complete Proposition1.1 and Corollaries1.2–1.3 statement/proofs. Only their applicable smooth reduced scope is used."},
    "CDP2020": {"file": "sources/papers/arXiv_1904.11179v2_CDP20_corrigendum_src/main.tex", "read_lines": [[250,364],[976,1012]],
                "scope": "Theorem2.2/Corollary2.3/Proposition2.4 hypotheses, intact strategy and exact §7 endpoint inference. Published page matches rely on the separately opened original record."},
    "HainMatsumoto_attached": {"file": "sources/papers/arXiv_1512.03975_src/main.tex", "read_lines": [[1070,1105]],
                               "scope": "Universal Mixed Elliptic Motives, supplied arXiv:1512.03975 source: the nodal cubic has P1 normalization and its smooth locus is Gm. This is positive classical background, not the receiving specific cubic×P1 endpoint counterexample."},
    "Viaclovsky_combs_attached": {"file": "sources/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex", "read_lines": [[2282,2330]],
                                    "scope": "The P−O hit is a principal C-star bundle on a rational elliptic surface with IV*,III,I1 fibres and a Mordell–Weil generator. It is not the note's local sections [0:1:0],[3:sqrt(36+t):1] or the computed1/3 branch multiplier."},
    "Hain_modular_attached": {"file": "sources/papers/arXiv_1403.6443_src/modular_gps.tex", "read_lines": [[4467,4492]],
                             "scope": "The Hodge-de Rham Theory of Modular Groups: the nodal-cubic hit concerns a logarithmic one-form along the discriminant divisor in a moduli space. It is not the receiving conductor differential on a singular fibre."},
}
for value in context_readings.values():
    value["file_sha256"] = sha(value["file"])
search_records = []
rows = []
source_records = read_json("deliverables/work/cdp_audit/references_verified.json")
if isinstance(source_records, dict):
    source_records = source_records.get("references", source_records.get("records", source_records))
if isinstance(source_records, dict):
    source_records = [dict(key=k, **v) if "key" not in v else v for k,v in source_records.items()]
source_by_key = {r.get("key", r.get("citation_key")): r for r in source_records}
inv_refs_path = "deliverables/work/invariants_arithmetic/references_verified.json"
inv_records = read_json(inv_refs_path)
if isinstance(inv_records, dict):
    inv_records = inv_records.get("references", inv_records.get("records", inv_records))
if isinstance(inv_records, dict):
    inv_records = [dict(key=k, **v) if "key" not in v else v for k,v in inv_records.items()]
for r in inv_records:
    source_by_key[r.get("key", r.get("citation_key"))] = r

for sid, title, alias, terms, ac_locator, ac_relation, ac_full, credit, elsewhere, keys in specs:
    m = mapping[sid]
    first,last = m["source_line_start"],m["source_line_end"]
    proof = "".join(source_lines[first-1:last])
    normalized_proof_hash = hashlib.sha256(proof.rstrip().encode()).hexdigest()
    assert normalized_proof_hash == m["full_statement_and_proof_sha256"], sid
    row = {"source_run": "CORRECTION_NOTE_20260901", "source_id": sid,
           "source_title": title, "source_file": SOURCE, "source_lines": [first,last],
           "source_file_sha256": sha(SOURCE), "actual_source_slice_sha256": hashlib.sha256(proof.encode()).hexdigest(),
           "source_slice_without_trailing_newline_sha256": normalized_proof_hash,
           "existing_mapping_hash_verified": True,
           "existing_mapping_full_statement_and_proof_sha256": m["full_statement_and_proof_sha256"],
           "reader": READER, "paper": "II", "printed_label": m["printed_label"],
           "alias_label": m["alias_label"], "assembly_action": m["assembly_action"],
           "receiving_context_read": "Complete correction-note source lines1–948 read for this attribution event, including all15 statements, full displayed proofs, setup, scope limitations and disclosure. This event does not replace the earlier independent mathematical/source audit.",
           "comparison_method": "Executed per-row whole-file rg queries in all four baselines and43 attached-source files, plus the recorded actual context readings. No claim that every unrelated hit was read or that literature absence is exhaustive.",
           "credited_to": credit, "preserve_historical_checks": True,
           "distinct_proof_current_mapping": {"status": "complete exact source concordance already recorded", "record": mapping_path,
                                              "source_id": sid, "action": m["assembly_action"]},
           "novelty_scope": "Bounded attribution only; no worldwide novelty claim. Positive known inputs are credited even when the receiving statement has broader or different hypotheses."}
    if alias:
        row["canonical_alias_comparison"] = {"source_id": alias, "record": canonical_path,
                                            "record_sha256": sha(canonical_path),
                                            "scope": "The internal canonical statement/proof concordance is preserved; its literature fields are supporting evidence, not copied to unrelated claims."}
    for corpus,files in corpora.items():
        command = ["rg", "-n", "-i", "--no-heading", "--with-filename"]
        for term in terms:
            command.extend(["-e",term])
        command.extend(["--",*files])
        run = subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
        assert run.returncode in (0,1), (sid,corpus,run.stderr)
        record_id = sid+"|"+corpus
        hits=run.stdout.splitlines()
        search_records.append({"id":record_id,"source_id":sid,"corpus":corpus,"terms":terms,
                               "command":command,"exit_code":run.returncode,"hit_line_count":len(hits),
                               "stdout_sha256":hashlib.sha256(run.stdout.encode()).hexdigest(),"hits":hits,
                               "stderr":run.stderr})
        if corpus=="elsewhere":
            opened=[]
            for key in keys:
                assert key in source_by_key,key
                record=source_by_key[key]
                record_file=inv_refs_path if key in ["Serre1955Duality","AtiyahSinger1963"] else "deliverables/work/cdp_audit/references_verified.json"
                opened.append({"citation_key":key,"record_file":record_file,
                               "record_file_sha256":sha(record_file),"preserved_original_reader_record":record,
                               "current_event_scope":"The existing exact original-source opening is reused with its original reader/date, not claimed as a fresh full original proof read."})
            row["found_elsewhere"]={"status":"positive_known_inputs_and_bounded_comparison" if keys or sid=="lem:conductor" else "classical_rederivation_or_internal_source_concordance_with_bounded_search",
                                    "full_statement_found":sid=="cor:relative", "comparison":elsewhere,
                                    "cited_opened_inputs":opened,"search_record":"deliverables/work/maps_audit/correction_note15_credit_search_log.json#"+record_id,
                                    "searched_file_count":len(files),"bounded_absence":"No additional full counterpart was identified within the executed searches and actually read scopes. This is not an exhaustive priority search."}
            if sid in ["prop:family-geometry","lem:gluing-bundle","thm:nodal-test"]:
                row["found_elsewhere"]["related_positive_background"] = {"source":"Hain–Matsumoto, Universal Mixed Elliptic Motives, supplied arXiv:1512.03975 source", "locator":"lines1079–1086", "relation":"Nodal cubic normalization P1 and smooth locus Gm; the specific proper test family, twist and endpoint implication are not asserted there.", "reading_record":"deliverables/work/maps_audit/correction_note15_credit_contexts.json#context_readings/HainMatsumoto_attached"}
            if sid == "lem:extending-gluing":
                row["found_elsewhere"]["specific_hit_disposition"] = {"source":"Viaclovsky supplied combs draft", "locator":"lines2296–2312", "relation":"P−O denotes a line on a different rational elliptic surface, not the note's local1/3 computation.", "reading_record":"deliverables/work/maps_audit/correction_note15_credit_contexts.json#context_readings/Viaclovsky_combs_attached"}
        else:
            positive=corpus=="AC26" and sid not in ["lem:extending-gluing","lem:generic-endpoints","prop:family-geometry","prop:relative-local"]
            row["found_in_"+corpus]={"status":"found_known_input_or_special_case_in_checked_scope" if positive else "full_counterpart_not_identified_in_bounded_checked_scope",
                                      "full_statement_found":ac_full if corpus=="AC26" else False,
                                      "comparison":ac_relation if corpus=="AC26" else "No full matching receiving statement identified in the listed source queries and actual opened contexts; related normal-crossing geometry or cohomology is not equated with this result.",
                                      "positive_or_context_locator":ac_locator if corpus=="AC26" else context_readings[corpus]["scope"],
                                      "terms_searched":terms,"files":[{"path":f,"sha256":sha(f)} for f in files],
                                      "search_record":"deliverables/work/maps_audit/correction_note15_credit_search_log.json#"+record_id,
                                      "actual_context_readings":"deliverables/work/maps_audit/correction_note15_credit_contexts.json#"+corpus}
    rows.append(row)

assert len(rows)==15 and len(search_records)==75
provenance={"note_document_date":"1 September 2026","raw_source_producer_sentence":"The local drafting and audit assistance used OpenAI Codex gpt-5.6-sol, Ultra; no AI system is an author.",
            "producer_date_precision":"The note has a document date; no distinct AI-assistance timestamp is inferred.",
            "source_author_field":"Human author to be supplied","source_producer_locator":"sources/correction_note/N_singular_fibre_vanishing_step.tex, AI-use and authorship disclosure, lines935–943"}
overlay={"reader":READER,"scope":"Attribution and source concordance for the15 CORRECTION_NOTE_20260901 PaperII rows only; no inventory/manuscript/original-source mutation.",
         "source_provenance":provenance,"counts":{"rows":len(rows),"executed_rg_queries":len(search_records),"attached_elsewhere_files":len(corpora['elsewhere']),"rows_with_explicit_credit":sum(bool(r['credited_to']) for r in rows)},
         "rows":rows,"source_checks_preserved":True,
         "historical_notes_policy":"Replace controlling pending credit fields from this overlay. Preserve earlier recorded checks and append the exact existing proof-concordance mapping instead of erasing the earlier pending-comparison note."}
OUT.mkdir(parents=True,exist_ok=True)
for filename,data in [("correction_note15_credit_overlay.json",overlay),
                      ("correction_note15_credit_search_log.json",{"reader":READER,"files":{k:[{"path":p,"sha256":sha(p)} for p in v] for k,v in corpora.items()},"records":search_records}),
                      ("correction_note15_credit_contexts.json",{"reader":READER,"context_readings":context_readings,"full_receiving_source":SOURCE,"source_sha256":sha(SOURCE),"source_read_lines":[1,948]})]:
    (OUT/filename).write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
fields=["source_run","source_id","source_title","source_file","source_lines","paper","printed_label","found_in_AC26","found_in_E26","found_in_DGKX_v1","found_in_DGKX_v2","found_elsewhere","credited_to"]
with (OUT/"correction_note15_credit_overlay.csv").open("w",newline="") as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader()
    for row in rows:
        writer.writerow({k:json.dumps(row[k],ensure_ascii=False) if isinstance(row[k],(dict,list)) else row[k] for k in fields})
print(json.dumps(overlay['counts']))
print(OUT/"correction_note15_credit_overlay.json")
