"""Record completed current K106/F41/F46 arguments and separate executions."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re

W = Path(__file__).resolve().parents[2]
R = W.parents[1]
A = W / "analysis/IV"
N = R / "sources/newer_night/checkpoint29"
T = W / "code/IV/replay_cp29_k106"
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
checker = "GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)"
events = json.loads((A / "current_check_events.json").read_text())
index = json.loads((W / "analysis/inventory_source_index.json").read_text())
bylabel = {x.get("label"): x for x in index.values() if isinstance(x, dict)}
replay = json.loads((T / "current_results.json").read_text())
assert len(replay["results"]) == 22 and all(x["exit_code"] == 0 for x in replay["results"])
exports = json.loads((A / "checkpoint29_export_manifest.json").read_text())
k106_files = exports[0]["files"]
for f in k106_files:
    assert hashlib.sha256((N / f["path"]).read_bytes()).hexdigest() == f["sha256"]

def locks(label):
    x = bylabel[label]
    text = (R / x["file"]).read_text()
    return {"source_checkpoint": 29, "source_file": x["file"],
            "source_file_sha256": {label: hashlib.sha256((R / x["file"]).read_bytes()).hexdigest()},
            "source_block_sha256": {label: hashlib.sha256(text[x["start"]:x["end"]].encode()).hexdigest()}}

sections = [
    {"scope": "SI3.1–10 and I3P.1–4: full source, genuine point line, finite cap, and end atlases",
     "rederivation": "Substituted v=w²−1 and D=v−2 into the original source and resolved U=Xz,V=Xω. Checked the selected-node coordinates a=z+v/2,b=ω−v/2, the actual square root R_b, K=b+v+2+R_b, x=a−vb/K, y=(bK−(2b+v)a)/4, q=xy, and the displayed contraction inverse. Retained Q=P²R, R−P=s u_s, q_old=R c_q, c_q(0)=1/2, all Miller source/target factors, Theta'_Q(1), and the complete s Delta V_T=P^6 U6 Z^−3 V_pt point arrow with U6(0)=−1. Re-derived h,B and their exact K=hB²,J=hB reindex with inverse h=J²K^−1,B=KJ^−1. The inspected symmetrizing sublattice remains Z times2Z, while every toric construction uses the original lattice. The positive prism determinants and the proper degree-one PL support map give the actual fan. The common4264-cone refinement and zero4402/one4392/infinity4308 four-cone atlases retain protected boundaries, full inverse monomials, finite quotient invariant generators, period units and original volume orders. The finite root has actual height1−t_coll(s)z², invariant norm square and every finite character/full annular cochain."},
    {"scope": "I3C.1–4, FSI.1–5, I3L.1–4 and I3R.1–4: compact and lower relative pairs",
     "rederivation": "Re-derived each normal degree as the negative sum of the three directed coefficient orders and checked the original canonical adjunction. The3422 complete curves,421 ruled surfaces with exactly12 ordinary point blowups,126 interior points and4 interior curves use the actual integral quotient/intersection lattices and full unit arrows. Expanded the weighted Euler/Pontryagin Laurent coefficients independently and inserted M=U^*; the compact pair is(−63,453). Each of the four lower surfaces has128 total source charts across the three subdivisions, with15+6+8=29 chronological blowups and tangent number−87. Its complete B^−j and point-line maps retain P/u_s and the primitive fibre connection. The reference divisor is3F−C1+C2=(3,2,4), of square−6 in the cycle matrix; its retained fibre twists have square and cross pairing zero. The collision-minus-reference normal pairings are(6,−6,6), giving(18,−87) per double and(72,−348) in total."},
    {"scope": "MS3.1–5, MC3.1–6, IC2.1–6: moving star and directed cap Chern numbers",
     "rederivation": "The36 selected charts give the37-ray surface and34 actual ordinary blowups, with three centres on D0 and none on D_infinity. The exact derivative functions F+=V_pt/Z²,F−=p Z²/V_pt give N+=2D0−3D_infinity and N−=−3D0+2D_infinity, hence the positive determinant square−75 and tangent number−102. The full Cox cut C_theta=(alpha Z,(alpha beta)^−1 a,beta c) preserves q; its inverse, Hermitian-ball map and complete normal matrix extend over the retained cap and satisfy C_hat B=N. Conjugating the coefficient columns gives the positive bundle. The explicit oriented replacement boundary of D³ timesD² identifies the cap with the34-fold blowup of P1 timesP1, retaining eta=bar(xi)/rho0². The directed coefficients retain bar(P), whose phase is P^−1, and all extending units. They give roots3D0−2D_infinity+U and2D0−3D_infinity; their product is−19 and determinant square−75. The full reference roots h−4U and−h−4U give c2=0. Thus the actual moving/reference pair is(−56,−101). Receiving notation will specify a conjugate-linear-first Hermitian convention and the complex-linear map bar(v)↦[w↦h(v,w)] explicitly; this does not change the divisor or integer computation."},
    {"scope": "ASI3.1–6: proper exterior, sphere reference, Stokes and four-edge scalar transfer",
     "rederivation": "Re-derived the real period determinant and its uniform positive bounds with all unit terms retained. The finite translated atlas cover and exact rank-one source contractions give the compact Hausdorff quotient. The line connection a_i=−sum rho_k X log g_ik and the lift X−a_i v_i partial_v carry genuine point-line frames even through coincident sections. The full M6 root/Cartier interval goes to the explicit F41 E6-B(6,1) reduced-IV reference via K94/K96; F41 was separately read in its full scope. The circle-first boundary orientation has the five-dimensional radial reversal, and the actual map[y,t]↦[y,1−t] carries the same line to the Jin convention. The four-edge product uses C(t,rho)=(exp(rho G),exp(rho H+2pi i rho(rho−1))), with increments of G,H equal−2pi i,−6pi i. The diagonal-to-MC3 ratio factors into an endpoint-zero logarithm and the full physical winding−6, which extends through the specified cap. This proves integer characteristic additivity for the fixed original scalar and identity source closing. The complete inner pair(−47,4) therefore gives the Jin pair(47,−4), with free pair(−1,48) and index8."},
    {"scope": "IF3.1–6 and VI3.1–6: actual native products and signed vertical class",
     "rederivation": "The fixed-scalar winding matrix is[[2,−1],[6,−3]]. The literal doubled native product has t=−1,l=(−18,6,−6), action trace(34,−8,6), derivative trace(−34,6,−4), V22=−6 and delta2=−30. The ambient-to-star derivative plus the inverse pure-left cap of degree2 gives the native double(16,−12); the specified actual square yields single free pair(8,−6), dividing only free Z². All full q-dependent chart maps retain their holomorphic height inverse and O(norm³) contraction inverse. The C2 coordinates are typed by Z=b,V=c,z=a=q/(ZV); the second chart has Z'=uv,V'=uw, recovering the exact h and B maps. Its Cox lift multiplies(a0,a1,c0,c1) by(1,(AD)^−1,A,D) and preserves q. The unrestricted four-weight quaternion identity gives T(h,q_H)=(q_H^−1 h q_H,q_H) and the full native reset, including oriented central increment n. Thus the first C2 flop changes8 to2. For every signed j the full shear V_j=Z^−jV,h_j=hB^j gives native C1 pair(−(j−3)²,(j−3)(j−4)) and C2 pair((j−2)(j−4),−(j−2)(j−3)), with exact forward/reverse coefficient resets. These yield S_j=8−j(j²−9j+26)/3 as an integral polynomial. The literal branch reflection carries the opposite marked w branch and its reflected fan, without enlarging the cap scope."},
    {"scope": "IVP.1–7: full vertical source, line, tangent, Hopf and collar integer",
     "rederivation": "Solved Q(q',s)=Q(q,s)g(q,s)^j by its actual inverse, with q'=a_j q and g(0,s)^j of winding−j. The ratio c=g(q',s)/g(q,s) has its unique periodic logarithm zero atq=0; (q,Z,gamma_j)↦(q',c^gamma_j Z,gamma_j) satisfies both full deck squares. The graph heights keep the two node preimages strictly ordered; their tube velocity and Cartier multiplicationZ^j carry the fixed sphere, normal arrow and physical cap. Conjugated both integral q/theta decks under gamma_j=gamma−jv,d_j=d−ju. The exact relative line tensor is U_j=U_0,q' tensor T_b^(j²−5j) tensor T_gamma^(2j), with prescribed outer arrow fixed by the free section disc and Cech/logarithm extension. The full tangent derivative is block triangular with a unipotent source connection and a three-variable base block, so its Pontryagin transgression vanishes. The four relative pairings are(1,0,0,2), using the actual BW.2/SCN.9 calibration, decomposable regular-level curvature and the explicit nodal SU2 frame of degree1. The directed Hopf clutch exp(−pi j theta h)exp(pi j theta i) has degree−j in the printed orientations, and the actual parameter reversal gives cap change(−j,−4j). The interior gives(3j²−15j,4j); the full exterior primitive, including j du, gives Euler change−36j+15j²−2j³. Thus delta k=−2j³+18j²−52j and delta ell=0 before any residue. With the actual initial pair this proves the claimed full vertical integers and fixed-C0 seed."},
    {"scope": "AFI.1–6 and all28 witnesses: arbitrary basis fan",
     "rederivation": "For each P the actual dense characters use R=P^−1, with h'_j=h^(P1j)B^(P2j); the four complete coefficients are transported by the displayed exponent tensor, and RP=I proves the exact q heights. The determinant winding remains−2 on the ordinary double. The full action and derivative prisms give the two linear systems, and the native free coordinates are m_i=−1−(Vii+delta_i)/4,n_i=(delta_i−Vii)/4. Literal fan translations/column symmetries give the unique physical-cone representative. Euclidean subtraction strictly decreases the positive coprime pair and terminates at a signed vertical seed. Both conifold rulings, inverses and constant unitary C1 interchange preserve all full source/cap maps; the target selected C2 has V'22=a,delta'2=2a−b. The difference of two symmetric trace solutions annihilates the prism plane and is the outer square of(1/w0,1/w1,1/w2); the selected value fixes its coefficient, while the derivative system has its single coefficient fixed likewise. Actual target existence supplies integrality. Every finite word uses a uniform smaller disc for that word. The independent full Gaussian solves recover all33 distinct target fans on the28 displayed T0 witness paths, all full coefficient powers, free resets and unreduced sums. The example C0,C1 has additions48,300 and sum356, class20. Each residue0–27 has an actual word of length at most7, proving the full image in the exact stated family."},
]

reviews = [
    ("IV-D-069", "night:P3K.106", "Complete checkpoint29 selected-I3 export and all15 supporting proofs",
     "Read and rederived the entire main statement and all15 supporting files, with exact source/Cartier/root maps, the three complete finite end atlases, all compact/lower/moving characteristic terms, both cap Chern classes, proper outer transfer, actual fixed-scalar four-edge square, native products, all signed vertical integers and the finite all-fan algorithm. The detailed section-by-section derivations are in analysis/IV/K106_current_review.json. The resulting physical pair is(47,−4), native fixed-C0 pair(−1,48), initial class8; the signed vertical pair is(47−2j³+18j²−52j,−4). The28 complete T0 native paths realize every class. Scope remains precisely M6,b1,m2,n1, prescribed admissible finite character and full reference. All22 selected atlas/arithmetic/topology replays passed unchanged; their execution credit is separately recorded. The two receiving clarifications type the Hermitian dual and actual C2/Tate coordinate map without changing the result."),
    ("IV-D-070", "night:P3F.41", "Full complementary starred-cap construction, all eight sectors and exact integral topology",
     "Read and rederived the complete SC.1–5 proof. Checked all four original rational elliptic source equations, actual section components and unimodular E7 or E6+A1 source lattices. The reduced roots have the displayed exponents and fixed component labels; the good-root quotient lattice, full common regular refinement and Cartier support max(v_w−(r−1)v_z,0) give exceptional corrections(2,1,1) or(3,2,1,1,1). The actual translation preserves the specified ideals and lifts the correction for every higher root. Its m-division and eigenlift retain the finite character in chi^(n m(m−1)/2) beta^−n; the invariant norm root gives commuting A0,B0 and the Bezout first-scalar contraction. Re-derived both cap meridian arrows, the holomorphic annular cochain and the exact inverse parameter closing. The functorial even-source chain cone retains all translation, fibre and boundary maps; the primitive vanishing-cycle argument gives the required simply connected source exterior. Checked both good-cap torsion isomorphisms via(D^u−1)Lambda=(D−1)Lambda, every retained collar coefficient, the reduced relative-Wang unit column and the integral degree-two isomorphism. The actual degree-one/three matrix[[0,1],[n,−m]], together with all higher/zero degree maps and van Kampen, gives pi1=Z/|n| and the printed complete homology. The primitive Hopf filling and Theta5=Theta6=0 give exactly the signed primitive sphere sectors. This is a full F41 proof review, separately from its bounded M6 reference use in K106."),
    ("IV-D-071", "night:P3F.46", "Full joint IV-star/III cap construction, four source pairs and signed topology criterion",
     "Read and rederived the entire proof. Checked the original source rational chart, source section formula, exact translation sign and h^*M−M=F forward-line direction. Recomputed all four reduced/good root substitutions, retained nonidentity section limits and actual deck weights. The IV-star common refinement gives the full(2,1,1) correction; the good-III quotient blowups and the two explicit contractions give beta*N=pi*alpha*M+E_aG−E_O, with the original tangent weights(1,1). The norm lifts retain their even-order character factor, signed roots and Bezout contractions. The common family uses L=lcm(m6,m2), and the exact global inverse multiplier t^k2(t−tc)^−(k6+k2) has every prescribed local order and extending ratio. Re-derived the full ten-dimensional source lattice, both component inclusions, even-complex mapping cones and marked integral boundary cycles. The source fundamental group follows from the actual III monodromy and unimodular pair(v,Av). Good-cap lattice transport and reduced invariant-fibre traces give every cap column. Checked the exact finite-group CRT arrows and all four symbolic degree-two determinants±1 for arbitrary kappa6,kappa2. The degree-one and degree-three matrices coincide in the stated physical bases, with determinant−(m2 n6+m6 n2). The explicit Bezout substitution makes the full van Kampen group cyclic; the complete sequence gives the printed groups for nonzero determinant and all Z groups at determinant0. Primitive Hopf filling and actual finite flop maps give the standard oriented six-sphere exactly for determinant±1 on every allowed fan. No return class is inferred from this topology theorem."),
]
for eid, label, scope, derivation in reviews:
    assert not any(x["event_id"] == eid for x in events)
    e = {"event_id": eid, "type": "D", "labels": [label], "verdict": "proved",
         "scope": scope, "derivation": derivation, "checker": checker, "recorded_at": now,
         "artifacts": ["analysis/IV/K106_current_review.json", "code/IV/replay_cp29_k106/current_results.json"],
         **locks(label)}
    if label.endswith("K.106"):
        e["supporting_file_locks"] = k106_files
    events.append(e)

for eid, label, scope, derivation in [
    ("IV-L-001", "night:P3K.57", "IE.4, IE.5 and the local Laurent formula IE.7 only, under K68's typed duality",
     "Read and rederived the full finite-chart averaged Stokes argument, the tangent splitting, every1/d stabilizer weight and the actual normal-sphere Thom pushforward. Expanded the point, curve and surface Laurent coefficients and retained the negative-normal conjugation orientation. The connection alpha(delta)=1 is the meridian-one dual line U, identified with M^* by the explicit K68 Hermitian map; both odd characteristic numbers reverse under this exact duality. The circle-first outer sign and[y,t]↦[y,1−t] Jin reversal are checked separately. The source's rejected global physical sign remains Refuted; no whole K57 local construction or compound conclusion is credited here."),
    ("IV-L-002", "night:P3K.76", "BW.2 relative local calibration only",
     "Read and rederived all of BW.2. The actual holomorphic logarithmic interpolation of the four extending unit factors preserves the valuation matrix and compact quotient shells. Its endpoint equation C1 E=C0 retains the fixed closing exponent. The source node horizontal field, prescribed real-period boundary field, fixed graph ordering, Cartier/Hopf normal map and invariant line lift give the relative isomorphism with the exact outer coefficient connection. The frozen-source SCN.9 C2 comparison has parameter-independent outer maps and an extending common inner gauge; its two separate characteristic terms vanish. Its complete retained Euler collar is3B_loc−3, proving the integer pairing B_loc=1. No full K76 theorem verdict is assigned by this local input review."),
]:
    assert not any(x["event_id"] == eid for x in events)
    events.append({"event_id": eid, "type": "L", "labels": [label],
                   "verdict": "complete bounded local input checked; whole-source verdict unchanged",
                   "scope": scope, "derivation": derivation, "checker": checker,
                   "recorded_at": now, **locks(label),
                   "artifacts": ["analysis/IV/K106_current_review.json"]})

for eid, labels, selected, scope in [
    ("IV-C-014", ["night:P3K.106"], replay["results"][:19],
     "Nineteen current unchanged selected-I3 atlas and exact characteristic/fan executions"),
    ("IV-C-015", ["night:P3F.41", "night:P3F.46"], replay["results"][19:],
     "Three current unchanged E7/E6 one-cap and joint-cap integral chain executions"),
]:
    assert not any(x["event_id"] == eid for x in events)
    events.append({"event_id": eid, "type": "C", "labels": labels, "verdict": "pass",
                   "scope": scope, "checker": checker, "recorded_at": now,
                   "source_checkpoint": 29, "executions": selected,
                   "derivation": "Every listed byte-identical original program exited zero in the isolated replay tree. The source manifest locks original inputs and programs; current logs and output hashes retain actual execution times. K106 rebuilds its complete common/corner atlases and characteristic data before the final integer/fan algorithms. Its28 witnesses are additionally reconstructed by fresh full Gaussian solves on33 distinct target fans. The topology programs retain actual source/boundary representatives, all torsion and collar coefficients, symbolic gluing determinants and1056 supplementary Smith cases. These are computation checks, with separate full geometric proof events.",
                   "artifacts": ["code/IV/replay_cp29_k106/source_manifest.json", "code/IV/replay_cp29_k106/current_results.json"]})

review = {"label": "night:P3K.106", "source_checkpoint": 29, "checked_at": now,
          "checker": checker, "verdict": "complete displayed argument rederived",
          "source_main_sha256": k106_files[0]["sha256"], "supporting_file_locks": k106_files,
          "sections": sections,
          "dependencies": [
              {"label": "night:P3F.35", "scope": "Actual periodic flop and common-link topology maps"},
              {"label": "night:P3F.41", "scope": "Explicit E6-B(6,1),m2,n1 sphere-reference sector; whole proof separately IV-D-070"},
              {"label": "night:P3K.23", "scope": "Retained local quaternion, relative-product, Hopf and oriented commutator maps; global refuted assertion excluded"},
              {"label": "night:P3K.29", "scope": "Integral prism/ambient derivative comparison only; historical scalar claim excluded"},
              {"label": "night:P3K.31", "scope": "Actual local single/double product and native reset only; historical global assertion excluded"},
              {"label": "night:P3K.57", "scope": "Only IE.4/5 and local IE.7 under K68 dual-line map; IV-L-001"},
              {"label": "night:P3K.62", "scope": "SCN.9 exact local C2 cap bordism with its extending outer maps"},
              {"label": "night:P3K.68", "scope": "Physical M versus dual U, Hopf orientation and inverse-clutch map"},
              {"label": "night:P3K.76", "scope": "BW.2 local integer pairing calibration only; IV-L-002"},
              {"label": "night:P3K.89", "scope": "VZ.1–7 source/line/tangent/normal/collar constructions, specialized in full IVP"},
              {"label": "night:P3K.94–98", "scope": "Original E6 source, root, Cartier, norm and full annular reference maps; no open attachment assumed"}],
          "computed_conclusions": {"compact_pair": [-63,453], "lower_pair": [72,-348],
               "collision_c2": -19, "reference_c2": 0, "moving_relative_pair": [-56,-101],
               "inner_pair": [-47,4], "Jin_pair": [47,-4], "fixed_C0_pair": [-1,48],
               "initial_class": 8, "reflected_class": 2,
               "vertical_pair": ["47-2j^3+18j^2-52j", "-4"],
               "vertical_index": "8-j(j^2-9j+26)/3", "all_fan_image": list(range(28)),
               "all_witness_maximum_flops": 7},
          "scope_limits": "M6,b1,m2,n1 and the prescribed admissible character/reference only. The literal branch reflection carries the corresponding opposite selected-I3 generator/fan. No higher cap order, opposite norm or additional endpoint is added by K106.",
          "historical_vs_current": "Source export/audit claims stay historical. Current D,L and C events record only the actual work above, including the two receiving notation clarifications. K75 stays Open."}
(A / "K106_current_review.json").write_text(json.dumps(review, indent=2, ensure_ascii=False)+"\n")
(A / "current_check_events.json").write_text(json.dumps(events, indent=2, ensure_ascii=False)+"\n")
def tsv(path, rows, cols):
    with path.open("w", newline="") as f:
        out = csv.DictWriter(f, fieldnames=cols, delimiter="\t")
        out.writeheader()
        for row in rows:
            out.writerow({k: json.dumps(row[k], ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k,"") for k in cols})
tsv(A / "current_check_events.tsv", events,
    ["event_id","type","labels","verdict","scope","derivation","checker","recorded_at","artifacts"])

searches = json.loads((A / "credit_searches.json").read_text())
source_paths = ["work/S6_10_PAPERS/analysis/V/AC26_original_extracted.txt",
                "sources/papers/arXiv_2609.38442_Engel_src/S6.tex",
                "sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex",
                "sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex"]
for _, label, scope, _ in reviews:
    terms = {"night:P3K.106": [r"selected[- ]I.?3", r"47\s*,\s*-4", r"Theta.?_?\{?7", r"all.?28", r"monodromy", r"fan"],
             "night:P3F.41": [r"starred", r"root order", r"complementary", r"Mordell", r"finite cap"],
             "night:P3F.46": [r"joint", r"two.cap", r"IV.?\*", r"meridian", r"Mordell"]}[label]
    sources = []
    for rel in source_paths:
        p=R/rel; lines=p.read_text().splitlines(); hits=[]
        for term in terms:
            found=[{"line":i,"text":line.strip()[:320]} for i,line in enumerate(lines,1) if re.search(term,line,re.I)]
            hits.append({"term":term,"count":len(found),"first_locators":found[:6]})
        sources.append({"file":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"hits":hits})
    rec=next((x for x in searches if x.get("label")==label),None)
    if rec is None:
        rec={"label":label,"paper":"IV","event_type":"bounded_current_credit_search","checker":checker};searches.append(rec)
    rec.update(recorded_at=now,terms=terms,sources=sources,
               assessment="These bounded searches did not establish an identical complete retained-map result. Earlier inputs remain explicitly credited; absence of a matched theorem is not treated as proof of novelty.",
               related_material_read="Full receiving argument: "+scope+". K106 uses the already opened Atiyah–Bott original Thm3.5/eq3.7–3.8 pp8–9 (IV-R-030), Krylov exact preprint local-group loci (IV-R-004/005/019), and K68’s typed comparison. F41/F46 retain the opened section-height and sphere-classification inputs; no new independent reading of those external proofs is inferred.")
(A / "credit_searches.json").write_text(json.dumps(searches,indent=2,ensure_ascii=False)+"\n")
tsv(A / "credit_searches.tsv", searches,
    ["label","paper","event_type","recorded_at","checker","terms","assessment","related_material_read","sources"])
print(json.dumps({"recorded_at":now,"new_D":[x[0] for x in reviews],
                  "bounded_local_events":["IV-L-001","IV-L-002"],
                  "new_C":["IV-C-014","IV-C-015"]}))
