"""Prepare source-specific UN36 credit/format guards and a qualified closure proposal.

Does not edit receiving sources, the shared inventory, or canonical assessments.
"""
from pathlib import Path
import csv
import datetime as dt
import hashlib
import json

WORK = Path(__file__).resolve().parents[2]
OUT = WORK / "audit_sign"
LABEL = "cdp:st:C.2.UN.36"
NOW = dt.datetime.now(dt.timezone.utc).isoformat()
WHO = "GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (not separately exposed), S6_SERIES_GRIND/sign_theorem_audit"

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def write(name, value):
    p = OUT / name
    p.write_text(json.dumps(value, indent=2) + "\n")
    return {"path": str(p.relative_to(WORK)), "sha256": sha(p)}

source_rows = [
    {
        "key": "Hatcher2002",
        "path": str(WORK / "audit_corrections/primary_sources/Hatcher2002_author_07.pdf"),
        "url": "https://pi.math.cornell.edu/~hatcher/AT/AT.pdf",
        "locator": "Theorem 3.44, printed pp.254–255 (PDF pp.263–264); Section 3.G, printed pp.321–322 (PDF pp.330–331).",
        "actual_reading": "Read the full theorem and relative cap-duality argument and the integral chain-transfer definition. Proposition 3G.1 was also read, but its field-valued invariant averaging is not the integral input used here.",
        "exact_application": "Z_i is a closed oriented real four-manifold. D_i is compact and locally contractible: a sufficiently small complex-curve neighbourhood is a finite collection of normalized branch discs with their marked origins identified, and isolated points are contractible. The relative cap isomorphism H_2(Z_i,Z_i minus D_i;Z) -> H^2(D_i;Z) identifies the map from H_2(Z_i;Z) with restriction of Poincare duality. Evaluation on the fundamental class of each curve C is exactly intersection with C. Thus its kernel, modulo torsion, is the stated K_i; every class there is represented by a finite, hence compact, cycle in the complement. For the actual cover w^(m_i)=u, x=s^(N/m_i)/w, the sum of all lifts is the integral chain transfer for total degree m_i, including a disconnected covering. Holomorphic local charts preserve orientation, and each transverse intersection has exactly m_i lifts, yielding the multiplicity factor. These source maps supply Steps 2 and 4; the whole-disc horizontal transport and the resulting Psi are proved in the receiving argument.",
    },
    {
        "key": "HuybrechtsK3Draft",
        "path": str(OUT / "primary_sources/Huybrechts_K3Global_author_08.pdf"),
        "url": "https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf",
        "locator": "Author prepublication draft, Chapter 1, Section 3.3, pp.16–17; Proposition 3.5 and equation (3.4), p.17. PDF and printed page numbers agree at these loci.",
        "actual_reading": "Read pp.13–18, including the full proposition and its proof. The exact cited input is the integral K3 lattice and signature (3,19) for a complex K3 surface. No publisher-edition pagination is inferred.",
        "exact_application": "The component minimal model in Step 10 is a complex K3 surface, so its oriented integral middle form is E8(-1)^2 plus U^3 and has negative index 19. Each actual point blowup adds the exceptional class of square -1 through the blowup map described in the Peters entry. The previously proved inequality max(b2minus-r,0)<=3 then gives r>=16+n for the chosen n-fold blowup resolution. The source is credited for the K3 lattice; the receiving boundary-rank inequality is separately proved.",
    },
    {
        "key": "Peters1990",
        "path": str(OUT / "primary_sources/Peters_surfaces_author_08.pdf"),
        "url": "https://cpeters1.win.tue.nl/ConfsAndSchools/Canada/surface.pdf",
        "locator": "Author lecture PDF, Chapter 1, Section 1, pp.5–6 (Noether and signature formulas); Section 2, p.8 (point blowup and intersection-signature change); Section 3, p.9 (Enriques invariants). The title page identifies the June 1990 Canadian Mathematical Society meeting.",
        "actual_reading": "Read the title page and the displayed formula pages, the complete point-blowup paragraph on p.8, and the surface definitions on p.9. These are the current 35-page author PDF's page numbers; no older published pp.87–88 are claimed opened in this reading.",
        "exact_application": "For an Enriques surface, b1=pg=0 and torsion canonical class give chi(O)=1 and c1^2=0. Noether's identity gives c2=e=12, hence b2=10; the signature formula gives -8, hence inertia (1,9). UN33 supplies q=pg=0, e=12 and K^2=0 for the receiving properly elliptic chi(O)=1 case, to which the same explicit signature calculation applies. For a point blowup pi, cohomological pullback pi^* and the exceptional divisor E give the orthogonal splitting with E^2=-1; Poincare duality carries this splitting to the homology pairing used in UN36. Iteration adds n negative directions, so the receiving negative-index bound gives r>=6+n. This reading does not replace UN33's own elliptic-fibre argument.",
    },
]
for row in source_rows:
    row["sha256"] = sha(row["path"])
    row["bytes"] = Path(row["path"]).stat().st_size

source_receipt = {
    "date_utc": NOW,
    "label": LABEL,
    "reviewer": WHO,
    "exposure": "These are source openings and exact receiving applications after the printed UN36 proof was read. They are not a new before-reading derivation.",
    "sources": source_rows,
    "imported_inputs": [
        {"label": "cdp:st:C.2.UN.11", "used_conclusion": "After the stated base change, N=U_1-I has square zero and rank at most two.", "source_event_ids": ["ce:37e8a8fa968d8f7b758a", "ce:5889574116f80dcf20ad", "S6_SERIES_GRIND_sign_source_ACampo1975_UN11"], "locators": "A'Campo 1975 Theorem 1 p.235, Section 2 pp.237–243, and Section 3 pp.243–245; current exact local covering/Lefschetz reading pp.237–238 and243–244. UN11's full proper-analytic argument and its exposure qualifications remain separate."},
        {"label": "cdp:st:C.2.UN.33", "used_conclusion": "For the relevant properly elliptic component, chi(O)=1 implies q=pg=0, e=12 and K^2=0.", "source_event_ids": ["ce:799347f5ec4ec7b4a9fe", "ce:ce3ab30303bdf5404e77", "ce:def8537b9d75032f3af7", "ce:grind-sign:b4d5e984f4f1de61"], "locators": "Ulmer–Urzua arXiv:2002.01906v2 Sections 2.2–2.3 pp.5–6; Kodaira 1963 II Theorem 6.2 pp.564–566, Section 8(iv), (11) p.585 and(12) pp.585–586, at the retained reproduced-original scope. Current UN33 all-twelve-step and eleven-row comparison remains its own event."},
    ],
    "bounded_credit_verdict": "Classical duality, integral transfer, K3/Enriques signatures and point-blowup formulas receive explicit primary credit through the actual maps used. Retain UN36's complete compact-core, full-multiplicity, simultaneous-transport and monodromy-invariant lattice proof. No worldwide priority or literature-absence claim is made. The historical generic found_elsewhere entry had no positive cited_opened_inputs; this receipt supplies concrete positive inputs without representing that old empty field as an actual opening.",
}
source_meta = write("UN36_primary_source_application_08.json", source_receipt)

body_path = WORK / "parts/II.body.linked.tex"
body = body_path.read_text()
start = body.index("\\label{" + LABEL + "}")
end = body.index("\\label{cdp:st:C.2.UN.38}", start)
block = body[start:end]
old_record = next(x for x in block.splitlines() if x.startswith("\\StatementRecord{"))
new_record = old_record[:-1] + r"; \cite[Theorem~3.44, pp.~254--255; \S3.G, p.~321]{Hatcher2002}; \cite[Chapter~1, Proposition~3.5, p.~17]{HuybrechtsK3Draft}; \cite[Chapter~1, \S1, pp.~5--6; \S2, p.~8; \S3, p.~9]{Peters1990}" + "}"
guards = [
    {"old_text": old_record, "new_text": new_record, "reason": "Add the exact positive classical inputs to the uses/source record."},
    {"old_text": "Poincar\\'e--Alexander duality and the relative\nhomology sequence give the exact map", "new_text": "Poincar\\'e--Alexander duality\n\\cite[Theorem~3.44, pp.~254--255]{Hatcher2002}\nand the relative homology sequence give the exact map", "reason": "Credit the precise compact-subset relative cap-duality theorem used by the intersection map."},
    {"old_text": "integral covering transfer and is a chain\nmap. For two transverse compact cycles,", "new_text": "integral covering transfer\n\\cite[\\S3.G, p.~321]{Hatcher2002}\nand is a chain map. For two transverse compact cycles,", "reason": "Credit the actual integral sum-of-lifts chain map, preserving the receiving intersection argument and disconnected-cover scope."},
    {"old_text": "signature $(3,19)$; $n$ point blowups\nadd $n$ orthogonal classes of square\n$-1$. For Enriques surfaces the\nsignature is $(1,9)$.", "new_text": "signature $(3,19)$\n\\cite[Chapter~1, Proposition~3.5, p.~17]{HuybrechtsK3Draft};\n$n$ point blowups add $n$ orthogonal classes of square $-1$.\nThe point-blowup splitting, and the Enriques invariants\nand signature formula giving signature $(1,9)$, are recorded in\n\\cite[Chapter~1, \\S1, pp.~5--6; \\S2, p.~8; \\S3, p.~9]{Peters1990}.", "reason": "Credit the exact K3 and Enriques signature and blowup inputs. The printed application to properly elliptic components still names UN33 and keeps its computation."},
]
for guard in guards:
    assert block.count(guard["old_text"]) == 1
    assert body.count(guard["old_text"]) == 1
    guard.update(label=LABEL, expected_count=1)
guard_meta = write("UN36_primary_credit_guards_08.json", {"date_utc": NOW, "target": "parts/II.body.linked.tex", "target_sha256": sha(body_path), "guards": guards, "scope": "Citation/credit additions only. No mathematical hypothesis, assertion, formula or proof map changes. New cited pages must be inspected after rebuilding; the complete pre-credit build28 row is already actually viewed.", "source_receipt": source_meta})

with (WORK / "S6_SERIES_GRIND_inventory.csv").open() as f:
    inventory = next(r for r in csv.DictReader(f) if r["label"] == LABEL)
values = {
    "credited_to": "Hatcher 2002 Theorem3.44 pp254–255 and Section3.G p321 supply compact-subset relative cap duality and integral covering transfer. Huybrechts author K3 draft Chapter1 Proposition3.5 p17 supplies the K3 lattice/signature. Peters author Compact Complex Surfaces Chapter1 Sections1–3 pp5–6,8–9 supplies Noether/signature identities, point-blowup splitting and Enriques invariants. UN11 supplies the actual square-zero monodromy statement; UN33 supplies the properly elliptic chi(O)=1 invariants. UN36 retains its full compact-core/multiplicity/whole-disc transport and invariant-lattice argument.",
    "literature_searches": "Fresh primary openings and complete exact application maps are recorded in audit_sign/UN36_primary_source_application_08.json, with URLs, SHA256 hashes and actual page scopes. Hatcher Theorem3.44 and its proof and the integral transfer definition were read; Huybrechts pp13–18 include the K3 lattice proof; Peters current35-page author PDF pp5–6,8–9 provides the stated formulas. These source readings occurred after receiving-proof exposure. Historical attached-corpus searches and their bounded scopes remain in notes; no unavailable historical search file or full source-corpus replay is claimed.",
    "source_credit_verdict": "Concrete classical inputs are credited at their exact hypotheses and maps. The full receiving compact-core/lattice proposition remains proved in the paper. No new worldwide novelty, priority or exhaustive literature-absence assertion is made. The earlier generic found_elsewhere.cited_opened_inputs field was empty; the current positive-source receipt supplies the needed explicit credit.",
    "credit_transport": "For each actual normalization resolution Z_i, relative cap duality identifies H2(Z_i,Z_i minus D_i;Z) with H2-cohomology of D_i, and the map from H2(Z_i;Z) evaluates as intersection with every curve component. Its torsion-free kernel is the stated K_i. The literal root equations w^(m_i)=u and x=s^(N/m_i)/w give total covering degree m_i, and summing all lifted singular chains yields intersection scaling by m_i. The receiving two real horizontal flows then put every compact transferred cycle in one nearby torus over the whole small disc, giving Psi and its monodromy-invariant image. Huybrechts gives K3 inertia(3,19); Peters' actual blowdown pullback plus exceptional class adds one orthogonal(-1) per point. Enriques c1^2=0,pg=b1=0 give e12,b2=10,signature-8, hence(1,9); UN33 supplies the same stated numerical inputs for the relevant elliptic case. The receiving negative-index inequalities give boundary ranks16+n and6+n. The current rational wedge certificate is identified with the printed rank-two basis by column order(1,4,2,3) and last-column factor(-epsilon).",
    "literature_disposition": "Retain the complete receiving proposition and proof with explicit classical input credit. Its original full multiplicities, disconnected root covers, simultaneous compact transport, actual monodromy invariants and chosen boundary lattices remain visible. Imported UN11/UN33 inputs retain their separately recorded proof and source scopes; UN36 completion does not close either input row.",
}
source_updates = [{"field": k, "old_value": inventory.get(k, ""), "new_value": v} for k, v in values.items()]
evidence = json.loads((OUT / "II_95_exact_evidence_map_07.json").read_text())["records"][LABEL]
event_by_id = {r["event_id"]: r for r in evidence["events"]}
assessment_before = json.loads((OUT / "row_assessments.json").read_text())[LABEL]
assessment = {
    "confidence_state": "complete printed proof comparison with the retained whole statement-first route and exact current certificates",
    "confidence_line": "All eleven compact-core, integral root-transfer, simultaneous whole-disc transport, monodromy-invariant pairing, radical/index and signature steps have been compared. Retained ce:bfb7cdbb11ddbf06ace6 records the full written statement-only derivation and complete comparison. Current ce:grind-sign:b2506aaf2828c696 compares all eleven steps after the current compact-core/transfer derivation. Exact current rational code checks all four oriented exterior-square forms and explicitly matches the printed basis. The current source and complete four-page visual receipts supply their own distinct scopes.",
    "independent_routes": "Retained ce:bfb7cdbb11ddbf06ace6: complete written statement-only derivation in 011_cover_constraints_prederivations.md and full receiving comparison in 012_cover_constraints_comparison.md; the retained event and completed-row gate are the available provenance, because the named historical files are absent from the supplied bundle. Retained ce:4e4144588e40ff5d2bf0: all four rational nullspaces and congruence signatures. Current ce:grind-sign:b2506aaf2828c696: every printed step compared, with a separately stated compact-core/transfer prereading scope; this current event is not promoted to a fresh full unexposed proof. Current ce:grind-sign:c632f73ecb76f7d157fc: independently authored four-case rational wedge certificate, geometric transfer outside the code's scope. All current checks use the same GPT-6 Astra model family; no added model-family independence is claimed.",
    "remaining_risk": "The UN36 mathematical, current-computation and concrete-source-application gates are closed at the stated imported-input scope. Citation guards still await root integration and changed-page QA; keep canonical completion pending until those exact format/layout steps are accepted. UN11 square-zero monodromy and UN33 elliptic invariants retain their own proof, reading-order and literature scopes. This row closure makes no broader main-theorem or novelty claim.",
    "format_check": "Current code guard integrated in build28; full current statement and all eleven steps actually read. The additional four primary-credit-only guards are prepared in UN36_primary_credit_guards_08.json and remain unapplied by this agent.",
    "layout_check": "Actual build28 visual PASS on all of UN36, pages452–455; exact PDF SHA7680ec1a1448c61848d94e394ae21ca78d23867dea1dc8aee32a28e0271e6453. Receipt II_build28_visual_QA_08.json identifies every inspected image/hash and separately the changed main-outline pages13–14. This whole-row inspection predates the pending citation-only additions.",
    "completion_state": "pending primary-credit guard integration and changed-page QA",
}
proposal = {
    "date_utc": NOW, "label": LABEL, "reviewer": WHO,
    "guarded_source_updates": source_updates,
    "exact_retained_before_reading_event": event_by_id["ce:bfb7cdbb11ddbf06ace6"],
    "retained_completed_row_gate": evidence["retained_explicit_three_check_gates"],
    "evidence": [source_meta, guard_meta, {"path": "audit_sign/II_build28_visual_QA_08.json", "sha256": sha(OUT / "II_build28_visual_QA_08.json")}, {"path": "audit_sign/UN36_current_certificate_guard_08.json", "sha256": sha(OUT / "UN36_current_certificate_guard_08.json")}],
    "assessment_before": assessment_before,
    "assessment_proposal": assessment,
    "completion_recommendation": "Accept the exact mathematical/source/computational record now. After root integrates the four citation-only guards and their changed pages pass actual QA, update this row alone to done. No canonical assessment or shared source is changed by this proposal.",
}
write("UN36_source_completion_proposal_08.json", proposal)

md = """# UN36: exact source application and whole-row completion proposal

The complete current statement and all eleven proof steps agree with the recorded receiving comparison. The current four-case rational certificate supplies every displayed oriented invariant form and an explicit unimodular change from its saved basis to the printed basis. Build28 pages452–455, containing the entire statement and proof, were actually viewed and pass. Four precise citation-only guards remain for root integration and subsequent changed-page inspection.

## Reading order and retained scope

The retained event `ce:bfb7cdbb11ddbf06ace6` expressly records a complete written statement-only derivation followed by the complete proof comparison. Its row gate says the prereading scope is complete. The named historical prederivation/comparison files are absent from the supplied archive; this report retains the exact receipt and does not claim to reopen those files. The current full eleven-step comparison is `ce:grind-sign:b2506aaf2828c696`; its independently derived preliminary scope is compact-core/transfer, so that current event is not a fresh whole-proof blind route. The current wedge event is `ce:grind-sign:c632f73ecb76f7d157fc`. The four exact forms were also computed in the retained event `ce:4e4144588e40ff5d2bf0`.

## Positive primary credit and actual maps

**Hatcher.** Theorem3.44, printed pp254–255, gives compact-subset relative cap duality. Here each `Z_i` is a closed oriented four-manifold and its compact curve/point subset `D_i` is locally contractible. The natural cap-duality square takes the map out of `H_2(Z_i)` to restriction of its Poincare dual on `D_i`. Evaluation on every irreducible curve is its intersection number. Since `H^2(D_i;Z)` is free on these curves, torsion maps to zero and the stated lattice consists of integral classes lifted from the complement. A finite singular-chain representative has compact support there.

Hatcher Section3.G, p321, defines the integral transfer as the sum of all lifts, commuting with boundary. UN36 uses the actual root equations `w^(m_i)=u`, `x=s^(N/m_i)/w`; the collection of sheets has total degree `m_i`, including the disconnected case. Each transverse intersection has `m_i` orientation-preserving lifts. This proves the exact multiplicity factor. The receiving horizontal-flow construction then embeds the compact representatives into one nearby fibre over the whole disc; the sources are not credited with that additional construction.

**Huybrechts.** The author draft Chapter1, Proposition3.5 and equation(3.4), p17, gives the complex K3 lattice and signature(3,19). The full proof was read at the author-draft pagination, including pp16–17. Applying the already proved negative-index inequality to the actual n-fold point-blowup resolution yields the printed bound16+n.

**Peters.** The current author lecture PDF Chapter1 Section1 pp5–6 gives Noether's identity and the signature formula; Section2 p8 gives the point-blowup splitting; Section3 p9 gives the Enriques invariants. For an Enriques surface, `pg=b1=0` and torsion canonical class give `chi(O)=1`, `c1^2=0`, then `e=12`, `b2=10` and signature−8, hence inertia(1,9). The properly elliptic case uses the separately proved UN33 invariants before applying the same formula. The actual blowdown map supplies the cohomological pullback summand, and its exceptional divisor is orthogonal of square−1; Poincare duality gives the corresponding homology splitting. Iteration and the receiving negative-index inequality give6+n. The cited PDF has35pages; these citations do not assert a different published pagination.

## Imported results and remaining gate

UN11 supplies square-zero monodromy and rank at most two, with its own exact A'Campo/analytic hypotheses and exposure record. UN33 supplies the stated elliptic `q`, `pg`, `e` and canonical-square calculation, with its own Kodaira/Ulmer–Urzua source maps. Neither imported row receives fresh whole-proof credit from this UN36 report.

The historical generic `found_elsewhere.cited_opened_inputs` entry was empty. The accompanying source-field update replaces its generic prose by these actual positive inputs and preserves only the recorded historical bounded searches. It makes no worldwide novelty or absence claim. Retain the complete receiving compact-core/lattice proof.

The remaining publication task is exact: integrate the four primary-credit guards, inspect their rebuilt pages, then accept the row-specific completion recommendation. No shared source, inventory or canonical assessment was edited here.
"""
(OUT / "UN36_source_completion_report_08.md").write_text(md)

events_path = OUT / "CHECK_EVENTS_additions.tsv"
with events_path.open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields, events = reader.fieldnames, list(reader)
new_events = [
    {"statement_id": LABEL, "date": NOW, "who": WHO, "type": "used and rechecked in this run", "outcome": "Opened Hatcher Theorem3.44 pp254–255 and Section3.G pp321–322, Huybrechts author K3 draft Chapter1 Proposition3.5 p17 with proof, and Peters author lecture Chapter1 pp5–6,8–9. Exact compact-subset cap/intersection, all-sheet integral transfer, K3/Enriques signature and actual blowdown-pullback/exceptional-class application maps are recorded in UN36_primary_source_application_08.json with URLs and hashes. This is post-receiving source application, not a fresh before-reading proof or whole imported UN11/UN33 proof check.", "event_id": "S6_SERIES_GRIND_sign_UN36_primary_sources_08", "phase": "current"},
    {"statement_id": LABEL, "date": NOW, "who": WHO, "type": "used and rechecked in this run", "outcome": "Actually viewed the entire current build28 UN36 statement/proof on pages452–455. All displayed maps, four-form table, matrix and the current certificate's explicit basis adapter are legible; paths wrap within margins. Exact PDFSHA7680ec1a1448c61848d94e394ae21ca78d23867dea1dc8aee32a28e0271e6453 and image hashes are in II_build28_visual_QA_08.json. This visual receipt predates the separate proposed primary-citation additions and is not a new mathematical derivation.", "event_id": "S6_SERIES_GRIND_sign_UN36_build28_layout_08", "phase": "current"},
]
ids = {r["event_id"] for r in events}
events.extend(r for r in new_events if r["event_id"] not in ids)
with events_path.open("w") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader(); writer.writerows(events)
print(json.dumps({"source": source_meta, "guards": guard_meta, "proposal_sha256": sha(OUT / "UN36_source_completion_proposal_08.json"), "events": len(events)}, indent=2))
