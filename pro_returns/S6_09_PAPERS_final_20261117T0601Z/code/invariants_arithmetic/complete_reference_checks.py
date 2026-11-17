"""Append the original-source checks completed after the first bibliography pass.

This preserves existing records and changes no source originals.  Locators describe
the actual passages opened, including visually inspected scans where OCR was weak.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / 'deliverables/work/invariants_arithmetic'
CACHE = ROOT / 'sources/audit_cache/inv_ari/literature'
records = {r['citation_key']: r for r in json.loads((D / 'references_verified.json').read_text())}
fetch = {r['key']: r for r in json.loads((CACHE / 'fetch_manifest.json').read_text())}


def checked(key, locator, use, hypotheses, source=None, url=None, visual=None, web=None):
    r = records.setdefault(key, {'citation_key': key, 'citation_contexts': []})
    r.update(status='verified_for_stated_use', verified=True,
             checker='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro',
             date='2026-11-17', opened_locator=locator, actual_use=use,
             hypotheses_and_normalization_check=hypotheses,
             extent='The complete cited statement and its relevant surrounding hypotheses were opened. The application and its limits were checked independently; this is not a claim to reprove every external theorem.')
    if key in fetch:
        r['retrieval'] = fetch[key]
        if not source and fetch[key].get('kind') == '.pdf':
            source = fetch[key]['file']
    if source:
        p = ROOT / source
        r.update(local_source=source, source_sha256=hashlib.sha256(p.read_bytes()).hexdigest())
    if url:
        r['url'] = url
    if visual:
        r['visual_check'] = visual
    if web:
        r['web_open_locator'] = web


checked('CrDarmon2009', 'Section 3, pp.4–5, Assumption 3.1 and the definition of the canonical Hecke character/theta series (extracted text lines160–220).',
        'Exact CM theta coefficients used by Crank_cm_stream.cpp and the Gross–Zagier interval regeneration.',
        'Imaginary quadratic class number one, unit group {+1,-1}, odd prime discriminant D=7,11,19,43,67,163; canonical curve conductor D^2 and psi((a))=epsilon_D(a mod sqrt(-D))a. The half-sum over nonzero lattice elements becomes the real paired coefficient used in the integer stream. No generalized-cycle statement is used.')
checked('bertrand2017', 'Original author slides5–8 and final slide15, comment(c); full displayed semi-abelian exponential and real compact determinant on slides7–8.',
        'Context for the compact-subgroup interpretation in C.7.2 and precise documentation of the withdrawn unrestricted-lift theta inference in C.7.7.',
        'Slides7–8 use f_v(z)=sigma(v+z)/(sigma(v)sigma(z)) exp(-zeta(v)z), the specified algebraic section and real place. The final-slide pointwise equivalence requires original lift conventions: replacing v by v+omega changes the expression by (eta(omega)-s2 omega)u. Neither direction of that unverified unrestricted-lift assertion is used. The compact character in the manuscript is calculated independently.')
checked('bertrand1995', 'Original paper, Theorem2.1 p.147 and its construction; Proposition2.2 and Theorem3.1 p.150 (extracted text lines90–160 and240–290).',
        'Counterexamples to a universal claim that an algebraic point in a multiplicative extension’s maximal compact subgroup is torsion; distinction from the additive extension theorem.',
        'Theorem2.1 assumes a real number field, a geometrically simple polarized abelian variety with a non-Rosati-invariant endomorphism and infinitely many rational points. The example uses an antisymmetric endomorphism h-h^dagger and a Ribet lift. The additive statement in Theorem3.1 does not transfer to multiplicative extensions.')
checked('bost2009', 'Theorems3.1.1–3.1.2, p.386 (extracted text lines1245–1310).',
        'Exact scope of the unitary algebraic-connection/universal-vector-extension alternative considered after C.7.7.',
        'The algebraic point must lie in the maximal compact subgroup of the universal vector extension, equivalently an algebraic connection must be unitary at an embedding. A point in a multiplicative extension’s compact subgroup alone does not meet this hypothesis.')
checked('nguyen2023', 'Theorem1.4 and Corollary1.6, p.3 (extracted text lines105–145).',
        'Scope check of a polynomial canonical-height/Böttcher-coordinate route; no application to prove the Lattès norm.',
        'Nonintegrable polynomial dynamics and an argument in the Böttcher domain are essential. Corollary1.6 gives algebraicity only in the bounded-conjugates case. The family uses a rational Lattès map and does not satisfy these polynomial hypotheses.')
checked('xie2024algebraicity', 'Theorem1.3 p.3 and Theorem2.3 p.12 (extracted text lines125–165 and640–670).',
        'Check of the quantitative algebraicity criterion for the compact leaf in C.7.11.',
        'A local analytic germ defined over a fixed number field and points rational over that field, together with the stated positive approximation/height lower ratio, are required. The proposed compact-leaf germ has a transcendental tangent slope, so the field-of-definition hypothesis fails before any approximation estimate is considered.')
checked('noguchi2024', 'Theorem1.3, p.2 and the definitions immediately preceding it (extracted text lines25–100).',
        'Scope check of the semi-abelian functional transcendence route.',
        'The theorem concerns an A-nondegenerate entire map into a semi-abelian variety and the transcendence degree of its graph, at least dim(A)+1. It is a functional statement and does not assert transcendence of the metric norm at an algebraic point.')
checked('waldschmidt1975dimension', 'Theorem1 and inequalities(1)–(3), p.24; proof pp.25–27.',
        'Exact multivariable interpolation threshold in the complexified norm obstruction.',
        'Values lie in one fixed number field; meromorphic functions admit entire denominators with the stated growth and value-size bounds, sampling cardinality at least N^ell, separation at least N^(-lambda). The sufficient inequality is (d-1)ell > sum(rho_j)+2d(n-1)(lambda+1). The proposed d=3,n=2,ell=4,rho_j=2 would need 8>12+6lambda and fails. An upper degree envelope is never treated as a lower bound.',
        visual='sources/audit_cache/inv_ari/literature/scans/waldschmidt1975dimension-03.png, printed p.24, inspected visually.')
checked('waldschmidt2009auxiliary', 'Theorem3.4 (one-variable Schneider–Lang criterion) and Theorem3.6 (several-variable criterion), extracted text lines1320ff. and1477–1505.',
        'Check of derivative-closed fixed-number-field interpolation assumptions.',
        'The derivatives must be polynomial expressions over one number field in the entire functions; the multivariable theorem additionally uses finite growth and a lattice basis. In the proposed theta route the logarithmic derivative is transcendental at the algebraic point, so the needed arithmetic closure has not been established.')
checked('herblot2012meromorphic', 'Theorem6.1 p.31, extracted text lines1814–1855, with the arithmetic-formal-curve hypotheses in its statement.',
        'Exact scope of the variable-residue-degree formal-curve alternative in C.7.11.',
        'Projective variety over Q, formal curves over the residue number fields of the marked closed points, alpha_j-arithmetic estimates and a common meromorphic uniformization of order rho. The inequality involves sum 1/(alpha_j d_j). A transcendental tangent slope prevents the proposed germ from being defined over its residue number field.')
checked('gasbarri2010analytic', 'Definition2.1 and the setup, Definition3.7 pp.14–15, Theorem4.16 p.25 (extracted text lines312–333,806–837,1390–1425).',
        'Exact LG-germ and number-field assumptions in the alternative algebraicity criterion.',
        'The formal germ is defined over the point’s number field, is analytic at finite places, and admits a good formal parameterization with the specified factorial denominator bounds outside a finite set of places. These are additional hypotheses, not consequences of algebraicity of a sequence of norm values.')
checked('gramain1986values', 'Theorem2.1 and hypotheses(1)–(8), original printed pp.101–102; auxiliary-function proof pp.102–103.',
        'The exact variable-degree interpolation inequality used to diagnose the division-value approach in C.7.11.',
        'The degree bound is the joint field degree of all k values. Hypothesis(5) is d product_j max(d psi_j,theta_j(R)) <= c0 mu^(k-1) phi^k, with phi=log((R^2+r(N)r(N+1))/(R(r(N)+r(N+1)))); monotonicity and mu phi/d tending to infinity are also required. On fixed nested discs our proved degree/count estimates do not establish the decisive inequality. This is a failed sufficient certificate, not a lower bound on actual degrees or an impossibility theorem.',
        visual='sources/audit_cache/inv_ari/literature/scans/gramain1986values-03.png and -04.png (printed pp.100–103), inspected visually.', web='turn84view0; turn85view0')
checked('adamczewski2017mahler', 'System(1.2), definition of regular argument and Theorem1.1, p.56.',
        'Mahler-method scope check after C.7.11.',
        'Functions have algebraic Taylor coefficients and solve a linear system f(z)=A(z)f(z^q), A in GL_n(Qbar(z)); the algebraic argument is inside convergence and regular along its forward power orbit. No such representation has been obtained for the compact normalization and its rational Lattès map. The text does not rule out every possible alternative representation.')
checked('einsiedler2001entropy', 'Section5, Theorem5.1 pp.9–10, definitions x(2^nQ)=a_n/b_n^2 and r(n)=4^n, with the full proof.',
        'Scope of the entropy interpretation of the canonical height.',
        'The transformations are the nonautonomous sequence T_j(x)=b_j x on R, and the scale is 4^n. This is not the entropy of a single algebraic automorphism and does not provide algebraicity of the exponential of a height.')
checked('waldschmidt1988periodrank', 'Theorem4.1 and formula(4.2), pp.385–386; Corollary4.3 p.386.',
        'Period-refined rank bound for the compact complex line of C.7.9/C.7.11.',
        'A finitely generated subgroup Y of V exponentiates to algebraic points; kappa is rank(Y intersect ker exp). For a Zariski-dense one-dimensional analytic subgroup, Corollary4.3 bounds total rank by (d1+2d2-kappa)/(d-1). For the nonsplit two-dimensional G_Q, d0=d1=0,d2=2,kappa=1, so the allowed rank is3 and the available rank2 gives no contradiction. d1 is a multiplicative quotient dimension, not the torus-subgroup dimension.',
        visual='sources/audit_cache/inv_ari/literature/scans/waldschmidt1988periodrank-06.png and -07.png (printed pp.384–387), inspected visually.')
checked('roy1993periodrank', 'Definition of d0,d1,alpha on p.359; main theorem p.363, conditions(i)–(iii); proof pp.363–364.',
        'Independent, refined algebraic-group rank statement used after C.7.11.',
        'Psi is rational over Qbar, W is a Qbar-rational subspace of V, and V contains no nonzero obstruction subspace Psi(S). The bound is (alpha_K(G)-kappa) dim(V/W). For K=Q, nonsplit G_Q has alpha=4 and kappa=1. Its compact line has no nonzero algebraic vector, so W=0 and the bound permits rank3.',
        url='https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A1E35F3798690D084664ACD83D1557E8/S0008439500013138a.pdf/autour_du_theoreme_du_sousgroupe_algebrique.pdf', web='turn84view2 lines48–64,170–237; turn85view2')
checked('waldschmidt1988theta', 'Original published exposition, p.15-03 (CM normalized sigma result and regularized s2), p.15-05 (periodic functional-equation theorem).',
        'Verified published statement of transcendence of the holomorphic normalized sigma value; precise exclusion of the algebraic-q route for CM tau.',
        'The lattice has algebraic invariants, E has CM and exp_E(u) is algebraic nontorsion; the asserted value is sigma(u)exp(-s2 u^2/2), where s2 is the explicitly regularized lattice sum. This concerns the holomorphic value, not its Hermitian norm. The periodic functional-equation theorem assumes q=exp(i pi tau) in a number field; CM tau makes this q transcendental. The exposition attributes the first theorem to Bertrand1982; it is not a claim that the inaccessible original proof was read.',
        visual='sources/audit_cache/inv_ari/literature/scans/waldschmidt1988theta-04.png and -06.png, printed pp.15-03 and15-05, inspected visually.')
checked('reyssat1982weierstrass', 'Corollary2, first page and proof Section5.1, original Acta Arithmetica paper.',
        'Precise independence statement for the alternative normalized sigma function in C.7.7.',
        'Algebraic Weierstrass invariants, a nonzero period omega and an elliptic logarithm u of an algebraic nontorsion point. At least two of exp(pi i u/omega), s_omega(u), s_omega_prime(u) are algebraically independent. This does not assert that s_omega(u) alone is transcendental; if it were algebraic, the other two can account for the required independence.',
        url='https://matwbn.icm.edu.pl/ksiazki/aa/aa41/aa4137.pdf', web='turn84view1; turn85view1, Corollary2 lines50–55 and proof lines665–686')
checked('callSilverman1993', 'Theorem4.1 and following elliptic-family remark, pp.183–184; full setup on p.183.',
        'General specialization limit and author reproduction of Tate’s stronger elliptic-family bounded-variation theorem in C.6.4.',
        'Smooth projective one-dimensional base, degree-one base height, a section, and a fibrewise morphism multiplying the chosen divisor class by alpha>1. Theorem4.1 is the ratio limit. The following remark separately states hhat(P_t)=h_{T,D_P}(t)+O_P(1), deg D_P=hhat(P_generic), for elliptic families. The explicit 1/2 log2 bound is proved locally in this manuscript and is not attributed to the general theorem.',
        visual='sources/audit_cache/inv_ari/literature/scans/callSilverman1993-22.png and -23.png (printed pp.183–184), inspected visually.')
checked('silverman2006heights', 'Original author slides21–22, extracted text lines478–510.',
        'Author reproduction of the 1983 specialization limit and uniform canonical-versus-Weil height bound.',
        'Slide21 bounds the height difference by c1 h_T(t)+c2. Slide22 gives the specialization ratio limit. The constant-part condition belongs to the subsequent injectivity corollary, not to the limit theorem. The unavailable 1983 original is explicitly identified as not opened.')

# Expand, rather than replace, the already checked 1-motive source scope.
r = records['bertolin2022']
r['opened_locator'] += ' Also Definitions2.3–2.4 and semi-abelian exponential lines375–458; Proposition4.12 and Remark4.13 lines971–1005; Section6.1 elliptic Weil bracket lines1276–1365; corrected Table2 lines1403–1452.'
r['hypotheses_and_normalization_check'] += ' The generalized logarithm includes first-, second- and third-kind coordinates and depends on a path modulo the specified periods. Proposition4.12 is conditional on the Generalized Period conjecture; the P=Q specialization is Remark4.13. The corrected dependent nondeficient row has unipotent dimension3 and total dimensions5(CM),7(non-CM), matching the explicitly nonzero diagonal bracket 2 psi in C.7.3.'

checked('Friedman2016AB', 'Definition1.1 and Lemma1.2 pp.4–5; Lemma2.2 p.11; Theorem2.4 pp.12–13 and Lemma2.7 p.14.',
        'Rational anticanonical-pair charge used in PUSH B.4.28: Q=Euler(Y minus D)>=0 and Q=0 exactly for toric pairs.',
        'The standing pair is a smooth projective rational surface and a reduced anticanonical cycle, including the one-component nodal case. No negative-definiteness assumption is required by Lemma2.7. Interior blowups increase Q by1; corner blowups preserve it. Inspection of the complete minimal-pair list plus these blowup rules proves the characterization. These hypotheses match the rational normalized components after the proof reduces to anticanonical cycles.',
        source='sources/external/root/retrieved/Friedman2016AB.pdf', url='https://arxiv.org/pdf/1502.02560')
checked('Dloussky2005AB', 'Definition2.20 and standing VII_0^+ hypotheses p.14; Corollary2.25 pp.16–17; Lemma2.26 p.17; Proposition2.27 and complete proof pp.17–19.',
        'Classification of a minimal class VII component with reduced actual anticanonical divisor in PUSH B.4.28.',
        'Minimality and b2>0 are standing assumptions. A global spherical shell is not assumed. Corollary2.25 gives a cycle in the NAC support; an actual reduced anticanonical divisor is the m=1,F=0 case and has coefficient1 on that cycle. Lemma2.26 removes branches, and Proposition2.27(i) gives an Inoue or Inoue–Hirzebruch surface. The proof explicitly includes the square-zero/Enoki case, which with NAC is the parabolic Inoue case. The half-Inoue alternative is excluded separately by the absence of an actual anticanonical divisor.',
        source='sources/external/root/retrieved/Dloussky2005AB.pdf', url='https://arxiv.org/pdf/math/0406387')
checked('FujikiPontecorvo2010AB', 'Sections3.2–3.3, printed pp.20–22, definitions and equations(8)–(10), Lemmas3.2–3.3.',
        'Identify the parabolic/hyperbolic/half Inoue cases and their canonical divisors in PUSH B.4.28.',
        'Hyperbolic has two rational cycles; parabolic has one rational cycle and one elliptic curve; these are the unique maximal reduced curves and satisfy -K=C, also after corner blowups. Half Inoue has empty |-K| and C in |-(K+L)| for nontrivial two-torsion L. Lemmas3.2–3.3 themselves additionally assume pi1=Z and a disconnected anticanonical curve: they are NOT used to classify an arbitrary class VII component before Dloussky’s result. For the parabolic case C_cycle^2=0 and K^2=-b2 imply E^2=-b2.',
        source='sources/external/root/retrieved/FujikiPontecorvo2010AB.pdf', url='https://archive.ymsc.tsinghua.edu.cn/pacm_download/21/834-JDG-85-1-A2-fujiki.pdf')
checked('Oda1978D', 'Section15, definitions of U_N and U_N^+ pp.128–129; Theorem15.1 and its complete geometric proof/sketch pp.130–131.',
        'Toric-lattice description and complement topology of a hyperbolic Inoue–Hirzebruch surface in PUSH B.4.28.',
        'N is a rank2 lattice in a real quadratic field. Multiplication by the generator of the totally positive unit group U_N^+ acts on N with determinant1 and positive reciprocal unequal eigenvalues, hence is hyperbolic. The first/fourth quadrant toric construction has two cycles; the complement is R times a compact-real-torus bundle over S1. The half quotient uses U_N rather than U_N^+ and is not substituted for the two-cycle case. The rank of T-I is2 over Q. Adjacent smooth toric rays supply the primitive angular lattice used by the manuscript.',
        source='sources/external/root/retrieved/Oda1978D.pdf', url='https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr58.pdf')

for r in records.values():
    r['verified'] = r['status'].startswith('verified_')

(D / 'references_verified.json').write_text(json.dumps(list(records.values()), ensure_ascii=False, indent=2) + '\n')
print('references', len(records))
print('unverified', [(k, r['status']) for k, r in records.items() if not r['verified']])
