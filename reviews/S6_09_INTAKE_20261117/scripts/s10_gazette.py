# Build gazette_candidates.tsv: paper, label, one_line, status, proof_label, uses.
# label = printed kind and number + TeX label (from the aux); uses = labels in the \Uses{...} line after the statement.
import csv, re, json
csv.field_size_limit(10**9)
R = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\returns\S6_09_PAPERS_final_20261117T0601Z_unzipped"
D = r"C:\Users\user\Documents\s6_pro_prompts_20261112_work\reviews\S6_09_INTAKE_20261117"
BS = chr(92)
inv = list(csv.DictReader(open(R + r"\S6_09_PAPERS_inventory.csv", encoding="utf-8", newline="")))
aux = json.load(open(D + r"\out\aux_labels.json", encoding="utf-8"))
tex = {p: open(R + r"\S6_09_PAPERS_%s.tex" % p, encoding="utf-8").read() for p in ("I", "II", "III")}
short = {"FAM": "S6_02_FAMILY", "PUSH": "S6_02_PUSH", "INV": "S6_01_INVARIANTS", "CDP": "S6_03_CDP", "MAPS": "S6_04_MAPS_MANIFOLDS", "ARI": "S6_05_ARITHMETIC"}
P = "proved here"
C = "proved here; computer-assisted (certificate printed and re-run)"
X = "counterexample or correction of a printed statement, proved here"
O = "open (stated with what is proved)"
def K(src):
    return "known (%s); re-derived here" % src
L = [
 # ---------------- Paper I
 ("FAM:A.1.1", "K_X = O(-2S_2); the anticanonical ring is C[U,V]; f is the bi-anticanonical map, so every biholomorphism between members covers the identity of P^1.", K("[AC26] Thm 9.1 for K_X; DGKX v1 for the intrinsic pencil")),
 ("FAM:A.5.1", "X_c is biholomorphic to X_c' exactly when c' - c is in 2Z (standard data); the isomorphism classes are the punctured disc 0 < |w| < e^(-pi M), w = exp(-pi i c).", K("DGKX v1 Thm 1.4; our working edition had the proof by 8 Sep 2026")),
 ("FAM:A.5.2", "h^q(X_c, T) = (1,1,1,0); the Kuranishi germ is a smooth line and the w-family is miniversal; direct images f_*T = O + O(-1), R^1 = O + O(-1)^2, R^2 = O.", K("DGKX v1 Thm 6.12, Prop. 6.16")),
 ("FAM:B.2.1", "All admissible twist vectors and cusp collars: X(c;w_1,w_2,sigma) is classified by (|p|, exp(-pi i (c + k_2))), p = 12 l_0 - 4 r_1 - 3 r_2.", P),
 ("FAM:B.2.2", "For fixed Engel parameter u the sphere members form exactly two isomorphism classes, exchanged by a circuit of u around 0 (Viaclovsky's Question 3 for (3,4)).", P),
 ("FAM:B.2.3", "Engel's Remark 8.1: the family with fixed sphere data exists over the punctured w-disc (w^2 = u) and does not descend to the u-disc.", X),
 ("PUSH:E.1.2", "Classification of Viaclovsky's X_{3k,4l} (gcd(3k,4l) = 1) in his coordinates: identification subgroup 2kl Z, 2kl classes at fixed u.", P),
 ("FAM:B.4.1", "Aut(X_c) = C^*, all components.", K("DGKX v1 Thm 1.4")),
 ("FAM:B.4.2", "The conjugate of X_c is X_{1 - conj(c)}; antiholomorphic maps exist exactly for w in iR, with full group C^* semidirect Z/2.", P),
 ("MAPS:A.3.2", "The two classes of antiholomorphic involutions and all their fixed loci (every non-empty fixed locus is a 3-sphere; both classes have fixed points for w = -ir, one for w = ir).", P),
 ("FAM:C.1.1", "The missing period in closed form: beta^part = (6i/pi) Log(theta_1(mu,tau) / (2 sqrt3 eta(tau))), mu the zero of the Weierstrass function; special values at the cusp, z_1, z_2.", P),
 ("FAM:C.2.3", "M = max D_part = -(3/pi) log 6, attained only at t = 1; so the parameter disc is exactly 0 < |w| < 216 (0 < |u| < 6^6). Three proofs: interval certificate, its Arb re-certification, and a certificate-free division-ladder proof.", C),
 ("ARI:C.2.1", "The Albanese curves of the two multiple fibres have nomes i w/216 and -w^2/48^3; their ratio q_1/q_2^2 = 27/64; exact continuation radius.", P),
 ("ARI:C.4.2", "The division identity: on the locus where P has exact order m, N^12 = |Delta| / |psi_m(P)|^(12/(m^2-1)); the values at all orders through eight.", P),
 ("ARI:C.6.3", "The eleven rational CM fibres: their models and height identities for the section P.", P),
 ("ARI:C.8.15", "Every critical point and level set of the norm: t = 1 is the unique global maximum and the only critical point on the t-plane; t = 0 is a non-critical C^1 point; no saddle.", P),
 ("FAM:F.1.1", "The monodromy group <A_1, A_2> is the kernel of an explicit character to Z/12 on the integral stabilizer of delta-hat: index 12 there, 24 in the line stabilizer.", P),
 ("FAM:F.2.2", "Klingler's question: the monodromy group does not act properly discontinuously on Sp_4(R)/U(1,1); the largest invariant open set where it does is {psi(delta, J delta) != 0}, which contains every admissible period.", P),
 ("FAM:D.1.4", "The Neron-Severi group of every smooth fibre as the integer kernel of one explicit period equation; E^2 = -2 Pf(E).", P),
 ("INV:A3.1", "The complete Hodge table of X_c: h^{1,1} = h^{2,2} = 2, h^{1,2} = h^{2,1} = 1, h^{0,1} = h^{3,2} = 1, for every admissible c.", P),
 ("INV:C2.1", "Frölicher degenerates at E_2 and not at E_1; the complete Bott-Chern and Aeppli tables (totals (1,0,2,2,2,2,1) and (1,2,2,2,2,0,1)).", P),
 ("INV:A4.2", "Correction to [AC26] Remarks 9.21 and 1.3: the relative cotangent sheaf has torsion exactly on S_1 and S_2 in degree one; along the cusp it is torsion-free and not locally free.", X),
 ("INV:D4.5", "h^q(X, T_X tensor L) for every L in Pic(X) = C, with all jump loci; for integral twists the closed formulas of Prop. 11.1.", P),
 ("PUSH:A.3.2", "Engel's Conjecture 8.2 is false as worded: the pinched space Q has virtual Euler number 0, the fibres X(u) have 2; the two semistable fillings and the nodal filling are the replacements.", X),
 ("PUSH:B.4.19", "After w = r^6 the sphere family has a proper smooth partial filling over (P^1 x disc) minus one point, with a twelve-cycle of components in the central divisor.", P),
 ("PUSH:B.4.33", "The punctured sphere family has no proper Hausdorff complex-analytic filling at w = 0 after any finite cover of the parameter (no Kahler or flatness hypothesis).", P),
 ("PUSH:D.1.3", "No flat proper family extends the X_w across any point of |w| = 216: j(Alb S_2) = J(i w/216) has the circle as natural boundary.", P),
 # ---------------- Paper II
 ("CDP:A.1.1", "For a reduced Cartier divisor S: 0 -> N* -> K -> Tors -> 0, and under the two endpoint vanishings the ambient sections are the kernel of the connecting map delta_A. This is the term the endpoint argument of CDP20 p. 692 omits.", P),
 ("CDP:B1", "A proper family (nodal cubic) x P^1 in which both endpoint vanishings hold and the ambient group is C for every twist: the inference fails without any use of S^6.", X),
 ("CDP:A.4.9", "CDP20 Proposition 7.3 holds, with a complete replacement proof; a specific implication of its printed proof is false (Prop. 5.17).", P),
 ("CDP:D.1.2", "The component count with monodromy: r = 2g + s - 1 + t' - b_1, t' the rank of the coinvariants; it replaces CDP98 Lemma 3.2 = CDP20 Lemma 4.2.", P),
 ("CDP:C.3.1", "The very general fibre of a holomorphic algebraic reduction of a threefold with b_1 = b_2 = 0, a = 1 is a 2-torus or a Hopf surface of algebraic dimension 0; all occur; bielliptic, Kodaira, Inoue, elliptic Hopf are excluded.", P),
 ("CDP:C.2.G.1", "Torus fibrations with b_1 = b_2 = 0, fibres unrestricted: B = P^1, c_3 in {0, 2}, b_3 = 2 - c_3, every fibre support has Euler number >= 0; complete description of the case c_3 = 0.", P),
 ("CDP:C4f", "The replacement of CDP20 Theorem 2.2: generic vanishing H^q(Y, T tensor L) = 0 (q != 1) holds exactly when Pic(Y) -> Pic(normalization) is non-zero for every irreducible non-normal fibre support; otherwise H^2 != 0 for every L.", P),
 ("CDP:C4b", "On a rational homology 6-sphere fibred over P^1 every L has a fibre with H^2 != 0; one fibre has rational normalization with H^2(K tensor ...) = C for every L.", P),
 ("CDP:C5b", "For X itself: h^q(T_X tensor M_n) in closed form for all integral twists; the map to H^2(dP_6, K) = C has rank one exactly for n in {-6,-3,-2} or n >= 0.", P),
 ("CDP:D.2.5", "Trivial rational monodromy forces c_3 <= 0 and b_3 >= 2, fibres unrestricted.", P),
 ("CDP:D.2.7", "A compact complex threefold with H_1 = H_2 = 0, a = 1, identity monodromy and c_3 = 0: fibres E x E, three reduced fibres each a Kodaira surface and a Hopf surface meeting in an elliptic curve.", P),
 ("CDP:E6", "Stability: a torus fibration over P^1 with Kodaira-Spencer rank two at one regular value keeps its fibration under every small deformation; with b_2 = 0 the algebraic dimension stays 1. Applies to all named S^6 families (Prop. 15.3).", P),
 ("CDP:E3", "A complex structure on S^6 has algebraic dimension 0 or 1, and for 1 the reduction is holomorphic onto P^1.", K("CDP98; CDP20 Thm 2.1; Lehn-Rollenske-Schinko")),
 ("CDP:E15", "Tangent cohomology of the other families: two-parameter family and Liu-Rollenske (1,2,2,0); positive combs (2m+1, 8m+1, 6m+1, 0), with smooth Kuranishi germs.", P),
 ("PUSH:E.2.23", "Members of different coprime pairs (3k,4l) are never joined by a chain of deformations; the locus of one pair is open and closed in the space of complex structures on S^6 (Cor. 16.31): Viaclovsky's Question 1.", P),
 ("INV:E2.3", "The kernel splitting of the comb bundles.", O),
 # ---------------- Paper III
 ("MAPS:B.1.2", "The repaired circle quotient e: S^6 -> S^3 has class 6 nu' = eta_3 eta_4 eta_5, the element of order two of pi_6(S^3) = Z/12.", P),
 ("MAPS:B.2.1", "The holomorphic map f: X -> P^1 is null-homotopic.", P),
 ("MAPS:A.2.2", "Engel's Remark 8.3: agreement with the literal quotient off a neighbourhood of W does not determine a homotopy class; all twelve classes occur.", X),
 ("PUSH:C.3.24", "The monodromy of the w-family around w = 0 is trivial in pi_0 Diff^+(S^6) = Theta_7 = Z/28 (reference fan; all admissible sphere twists): by the orbit-knot integer.", P),
 ("PUSH:C.3.27", "Second determination of the same class by an explicit spin^c coboundary.", P),
 ("MAPS:B.6.24", "Third determination (free-circle quotient of the mapping torus), and the same value 0 for every coprime (3k,4l) family (reference fan).", P),
 ("MAPS:B.5.1", "A finite CW structure on X adapted to f (the T^4-bundle over the pair of pants and the three special fibres), with cell counts (5,20,45,56,42,17,3).", P),
 ("MAPS:C.1.3", "The local Kummer covers of the cusp do not extend to a smooth branched cover of X; a connected normal finite-flat source exists (C.1.5).", P),
 ("MAPS:D.1.11", "The universal covers of the members with pi_1 = Z/d (d > 1): Euler number 2d, b_2 >= d - 1, so not a connected sum of copies of S^3 x S^3 (Thm 4.1); their homology, cohomology ring and diffeomorphism type (Thms 4.4-4.9, A.4).", P),
 ("MAPS:D.2.28", "The other rational elliptic surfaces with Mordell-Weil rank one: the sphere question on all twenty-one natural profiles; with Thms 4.53-4.54 the minimal simply connected sector is classified up to diffeomorphism.", P),
 ("MAPS:D.2.4", "The full table of configurations (Viaclovsky's Question 4) and the residue 0 or 4 in Z/8 of one example.", O),
 ("MAPS:D.3.3", "The conifold transition of Engel's Remark 8.5: the moving-zero family (Thm 4.63), whose smooth side is S^3 x S^3 (Thm A.6), with its complex invariants.", P),
 ("MAPS:E.2.1", "The fibre-product fourfold Z: K_Z = Pi^*L^(-5), a(Z) = 2, h^{0,q} = (1,1,0,0,0), not in class C, signature 2.", P),
 ("MAPS:F.2.6", "A closed 8-manifold glued from rank-six data (free affine fibres of multiplicity 5 and 4, one index-one cusp): simply connected, signature 2, lattice 3<1> + <-1> (Thm 6.8), with free integral homology and H_2 = H_3 = 0 (Thm 6.10).", P),
 ("MAPS:F.3.6", "A holomorphic rank-three period family with that monodromy, from the primitive exterior square of the genus-two pencil y^2 = x^5 + lambda^3 x + lambda^4.", P),
 ("MAPS:F.4.1", "A compact complex fourfold, fibred in 3-tori over P^1, three-connected with Euler number 6, diffeomorphic to 3 HP^2 # (-HP^2).", P),
 ("MAPS:F.2.39", "The effective integral classification of all rank-six gluing data of this kind (per-input algorithm, no height bound).", P),
 ("MAPS:B.3.1", "The retained-angle cusp collapse map H: X -> S^4 is eta_4 eta_5, non-zero in pi_6(S^4) = Z/2; the angle-forgetting maps to S^3 and S^2 are null (Thm 2.6).", P),
]
def find(run, sid):
    run = short.get(run, run)
    hit = [r for r in inv if r["source_run"] == run and r["source_id"] == sid]
    if not hit:
        hit = [r for r in inv if r["source_id"] == sid or r["printed_label"].endswith(sid)]
    return hit[0] if hit else None
rows = []
missing = []
for key, one, status in L:
    run, sid = key.split(":", 1)
    r = find(run, sid)
    if r is None:
        missing.append(key)
        continue
    p, lab = r["paper"], r["printed_label"]
    a = aux[p].get(lab, {})
    kind = a.get("anchor", "?").split(".")[0].capitalize()
    label = "%s %s, p. %s [%s]" % (kind, a.get("num", "?"), a.get("page", "?"), lab)
    pos = tex[p].find(BS + "label{" + lab + "}")
    seg = tex[p][pos:pos + 40000]
    m = re.search(re.escape(BS + "Uses{") + r"(.*?)\}\s*\n", seg, re.S)
    uses = []
    proof_label = lab
    if m:
        u = m.group(1)
        for g in re.findall(re.escape(BS) + r"c?ref\{([^}]*)\}", u):
            for x in g.split(","):
                x = x.strip()
                if x.startswith("app:rederive"):
                    proof_label = x
                elif x and x != lab and x not in uses:
                    uses.append(x)
        for g in re.findall(re.escape(BS) + r"cite[tp]?(?:\[[^\]]*\])?\{([^}]*)\}", u):
            for x in g.split(","):
                x = "cite:" + x.strip()
                if x not in uses:
                    uses.append(x)
    rows.append((p, label, one, status, proof_label, "; ".join(uses)))
with open(D + r"\gazette_candidates.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["paper", "label", "one_line", "status", "proof_label", "uses"])
    for row in rows:
        w.writerow(row)
import collections
print("rows", len(rows), collections.Counter(r[0] for r in rows), "missing", missing)
for r in rows:
    print(r[0], "|", r[1][:60], "|", r[4][:40], "| uses:", len(r[5].split("; ")) if r[5] else 0)
for lab in ("sec:II:06", "sec:II:12"):
    print(lab, aux["II"].get(lab))
