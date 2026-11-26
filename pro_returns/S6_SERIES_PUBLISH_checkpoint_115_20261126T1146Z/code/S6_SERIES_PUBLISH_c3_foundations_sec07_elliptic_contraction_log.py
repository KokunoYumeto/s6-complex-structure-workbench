from S6_SERIES_PUBLISH_c3_foundations_sec07_unit_logs import write_unit_logs

review=('Complete original/current and receiving P454 subsection, A.5.17 and P322 '
 'statements/proofs read. All fixed-r, formal-functions, coordinate descent, '
 'weighted-character, quotient-vertex and full-fibre maps compared. Complete '
 'P452/P453/P451 original/current and bounded receiving proofs also compared; '
 'P452 already invokes the proved unit flow and remains unchanged. Six guards '
 'replay once and retain every old label/target. Source openings and limits are '
 'recorded. Exposed comparison only; no independent credit or required-check '
 'increment. Integrated build/page reading and whole-paper structure remain.')
readings=[
 ('local_sphere','cdp:st:A.5.17',
  'Read every original/current and receiving A.5.17 statement/proof line. The '
  'existing ball-boundary, finite gradient, proper critical-value discriminant, '
  'Ehresmann, explicit square-completion and real Morse-sphere construction '
  'already proves the isolated holomorphic germ assertion without a global '
  'torus. The receiving statement exposes that exact assertion. Its same '
  'boundary transport gives an embedded sphere of square−2 on every small '
  'nonzero local level. The unchanged f=u h^m application follows by '
  'H=u^(1/m)h, preservation of the isolated critical germ, and the identity '
  'local-fibre inclusion into Y_(epsilon^m). Every subsequent individual '
  'factor power, unit, boundary-link calculation, sign coordinate, Hessian '
  'determinant and suspension/Hessian conclusion is retained. The direct '
  'A.5.17 references were inspected for positional-clause breakage; they name '
  'the preserved isolated or Hessian constructions, not a numbered item.'),
 ('milnor_source','cdp:st:A.5.17',
  'Freshly opened the full Milnor1968 primary text of Lemma6.1 and its proof '
  'printed pp55–56, and AppendixB pp111–114 including LemmasB.1–B.3 and '
  'the positive-degree proof. The public OCR view is '
  'https://djvu.online/file/kCFrJq27uCPRi. Its polynomial boundary statement '
  'is mapped to the chosen regular radius; AppendixB starts with analytic '
  'functions, and its boundary-degree perturbation/regular-value argument '
  'is precisely the one retained for the holomorphic gradient. No new '
  'whole-book reading or full-PDF hash is claimed. Two downloaded trial '
  'images showed printed pp58/120, not the desired loci, and are not '
  'credited as page55/111 readings. Existing Princeton1968 bibliography '
  'remains; the mirror URL is only reading evidence, not a bibliography URL.'),
 ('character_owner','lem:II:weighted-initial-monodromy',
  'Read complete old and receiving P322. All compact weighted transport, '
  'dimension-two variation/Wang and free-action inequalities remain. The '
  'added finite-order formula is proved on C={P=1,Rw<=R0}; its compact '
  'real algebraic double is t^2=R0−Rw(z), with mu_d×{±1} acting by '
  'weighted scalars and sign. Equivariant triangulation makes t=0 a '
  'subcomplex and each half a subcomplex. Projection to z and inverse '
  '(z,sqrt(R0−Rw(z))) identify the chosen half exactly with C. Barycentric '
  'subdivision makes a preserved simplex pointwise fixed, so alternating '
  'cellular trace counts the fixed subcomplex. The same invariant gradient '
  'collar identifies fixed cores with fixed affine fibres, yielding '
  'alternating homology trace=chi(F^zeta). The original free bound follows '
  'on the same representation and quotient, with no changed hypotheses.'),
 ('triangulation_source','lem:II:weighted-initial-monodromy',
  'Fresh primary Park–Suh1996 journal PDF opened and rendered pp179–180 '
  'read, including the complete setup and Theorem1.2: a finite group '
  'acting algebraically on a real algebraic variety admits an equivariant '
  'semialgebraic triangulation respecting orbit types. The receiving compact '
  'algebraic double satisfies exactly these hypotheses. This records '
  'statement/setup reading, not the later proof. URL '
  'https://www.jstage.jst.go.jp/article/kyushujm/50/1/50_1_179/_pdf/-char/en; '
  'SHA25650ff3fa390399ba302fc0f80c327aae0c7d2bd1a2fd6c3e3cc44b9e66c719165; '
  'KyushuJMath50(1)(1996),179–205, DOI10.2206/kyushujm.50.179. '
  'Also read the complete Hatcher2002 proof2C.3 pp180–181, especially '
  'the cellular/homology alternating-trace identity and short-exact-sequence '
  'argument on p181. Its cached primary text has PDF SHA256 '
  'bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618.'),
 ('formal_coordinates','night:P4.54',
  'Read every original/current and receiving P454 line. The exact resolution '
  'pi:Vtilde→(V,0) and fixed r of order one yield I_m, L=O_H(−H), '
  'cofinal infinitesimal filtrations, R1pi_*O(−mH)=0, restriction '
  'I_m/I_(m+1)=H0(L^m), and completed ring comparison. Read Grauert1960 '
  'p59 HauptsatzeI/IIa setup, statements and their printed final arguments, '
  'plus the entire1963 two-page erratum35–36 from attached primary texts; '
  'no reading of the whole preceding coherence proof is claimed. All '
  'elliptic section-ring computations d=1,2,3, fixed-r linear/triangular '
  'coordinates, formal lifting G=hf and initial-unit argument remain. '
  'The centre change is (x,y,z)→(x−u(p)z,y−v(p)z,z), inverse adds the '
  'same terms. The descended map x′=ax+by+cr², y′=a′x+b′y+c′r²−alpha r³, '
  'r′=r has the original nonzero Jacobian. Its monomial map '
  'r^a s^b v^c→x^b y^c z^(3+a−b−c) and ratios identify the exact '
  'elliptic function field in all three weighted leading polynomials.'),
 ('weighted_cases_and_cohomology','night:P4.54',
  'Read full old/receiving weighted cases. The original full map Phi=u g^m '
  'and root/inclusion remain; P322 is applied directly to g_u, whose '
  'initial polynomial is alpha P, alpha=exp(log u(0)/m), with c=alpha. '
  'Thus {alpha P=alpha}={P=1} transports to g_u=alpha epsilon^D and '
  'then the full Phi=(alpha epsilon^D)^m. Degree6 retains the finite double cover '
  '(x,y,z)→(x,y,z²), branch B, chiB=3(2−k0), chiF=12+3k0, exact cube '
  'fixed set, rank>=9+3k0 and M=3−k0. Reducedness is now proved before '
  'the character use. The explicit coordinate permutation to ProjC[z,x,y] '
  'preserves every degree7/9 vertex character. Complete prime-order and '
  'order-four branch-orbit arguments remain. Degree7 rank gaps18/11 and '
  'degree6 gap10 remain. Degree9 applies the newly explicit local A.5.17 '
  'clause with H=P9, uses D_lambda^-1 from its small level to P9=1, and '
  'then P322 into g_u=alpha epsilon^9 inside Phi=(alpha epsilon^9)^m. '
  'The final R18 application uses '
  'the full current global irreducible-or-NC/positive-Euler/ruling hypotheses. '
  'Freshly reread Dolgachev1982 Theorem1.4.1 and full proof pp39–41 in '
  'the author PDF; exact S=C[u,v,w], twist−e and the hypersurface sequence '
  'give h1OD=dimS_(e−a−b−c), h0OD=1. Its generic Cech reproof is replaced '
  'by this citation/application. Author URL '
  'https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/weighted82.pdf; '
  'SHA256f93b558ac5ffe7420f5d64c8faac28587fb064b7a7b7cca5405e9b1d89410926. '
  'Publisher metadata confirms LNM956(1982),34–71, DOI10.1007/BFb0101508.'),
 ('root_function_applications','night:P4.53',
  'Read complete current/original P452, P453 and P451 proofs and the complete '
  'receiving P453 proof. P451 already proves the unit homotopy '
  'g_s=exp(s log v)g, its bounded gradient flow and oriented compact-cycle '
  'embedding; P452 explicitly invokes that map and is unchanged. P453 old '
  'wording omitted that intervening existing flow when passing from its root '
  'inclusion to g-levels, an application-map omission rather than a false '
  'theorem. The bounded receiving paragraph applies P322 directly to '
  'g_u=exp(log u/m)g, initial alpha P5, c=alpha, so the unchanged leading '
  'fibre P5=1 maps to g_u=alpha epsilon^5 and then the full '
  'Phi=(alpha epsilon^5)^m. The same exact construction is now explicit '
  'at P454, including its degree-nine sphere. Every other P453 coefficient, '
  'discriminant, covering, monodromy and conductor-normality argument remains.')
]
specific={
 'D01':'Replace the remaining-support phrase with the exact P314 global setting.',
 'D02':'State arbitrary transverse types positively once; identify the graded and analytic coordinate maps explicitly.',
 'D03':'Move the weights to their proof and remove prospective/repeated closing summaries; all mathematical calculations remain at their uses.',
 'D04':'Use stable numbered references for every inherited equation and statement.',
 'D08':'Remove process-relative actual/remaining wording while retaining the fixed original parameter and full map.',
 'D12':'P322 alone owns weighted transport and scalar characters; A.5.17 exposes its existing general local sphere proof; P454 retains every application-specific analytic and vertex calculation.',
 'D13':'The actual subsection consists of a numbered proposition with its complete proof; no orphan paragraph remains.',
 'D14':'Weighted reducedness now precedes the degree-six character use; all shared owners precede P454. Root retains whole-paper placement.',
 'D17':'Opened Dolgachev1.4.1 replaces the generic weighted-Cech proof. Opened Park–Suh1.2/Hatcher trace identity support the short exact algebraic-double comparison. Fixed-r analytic arguments remain because they supply the exact form used.',
 'D18':'Add verified published Dolgachev/Park–Suh entries in author order. Grauert and Milnor citations retain their exact printed locators and existing bibliography.',
 'D19':'All six 4.54w.1–5/4.54a labels survive under section numbering; equation whitespace is checked.',
 'D20':'Every coordinate permutation, centred blowup map, triangular change and weighted level map has an explicit identity/inverse. k0 names the root count; r remains the exceptional parameter.',
 'D22':'The source of d≤3, every allowed weight, branch character and numerical gap is given where used.',
 'D25':'All complete old/receiving proofs compared. P453/P454 now transport directly through g_u with initial alpha P, c=alpha and full Phi=(alpha epsilon^D)^m. P452 already names the proved P451 unit flow and remains unchanged. The degree-nine sphere uses the local A.5.17 clause; all exact R18 hypotheses remain. No theorem is weakened or refuted.'
}
comparison=r'''# Elliptic contraction: complete receiving comparison

Actual unit: `night:P4.54`, heading label `subsec:II:elliptic-contraction`. Its original noncontraction, generic D4, covering-degree2/3 and arbitrary other-component transverse-type conclusions retain the complete P314 irreducible-or-normal-crossings global domain. No new tag is used; P323/P324 remain reserved.

| Existing calculation | Single receiving owner or exact application | Map and preserved conclusion |
|---|---|---|
| A.5.17 isolated critical point proof | A.5.17 local clause, followed by torus application | Same H_lambda, fixed boundary ball, proper discriminant, Ehresmann path, explicit Morse coordinates and sphere−2. Full f=u h^m uses H=u^(1/m)h and the identity inclusion into Y_(epsilon^m). All remaining suspension/individual-power calculations remain. |
| Weighted compact core and free/nonfree scalar character | P322 | C={P=1,Rw≤R0}; algebraic double t²=R0−Rw(z), finite mu_d×{±1} action. The half projection and explicit square-root inverse identify the exact core. Barycentric cellular trace equals chi(fixed set), and the gradient collar restricts to fixed loci. |
| P454 formal functions | Retained at P454 | Same pi:Vtilde→V, L=O_H(−H), I_m, cofinal ideals, restriction maps and completed ring. All d=1/2/3 section rings and the formal relation G=hf proof remain. |
| Fixed exceptional parameter | Retained with explicit centring map | (x,y,z)→(x−u(p)z,y−v(p)z,z), inverse by adding terms; r=z stays fixed. The linear/triangular changes descend to the original displayed polynomial coordinate map with determinant ab′−a′b≠0. |
| Weighted degree/curve correspondence | Retained at P454 | r^a s^b v^c maps to x^b y^c z^(3+a−b−c). The ratios x/z^(1+ws),y/z^(1+wv) give the identical elliptic function field. All higher terms remain. |
| Local leading-cycle comparison | P322, applied at P453/P454 | Original Phi=u g^m, g_u=exp(log(u)/m)g and alpha=exp(log(u(0))/m). G_epsilon=epsilon^-D g_u D_epsilon has initial alpha P; c=alpha makes its source {alpha P=alpha}={P=1}. The target g_u=alpha epsilon^D lies in Phi=(alpha epsilon^D)^m. P452 already names P451's proved unit flow and stays unchanged. |
| Degree6 nonfree character | P322, exact P454 calculation | (x,y,z)→(x,y,z²), branch B, chiB=3(2−k0), chiF=12+3k0. The cube is the only nonidentity element with fixed locus B. Lower bound9+3k0≥12 and M=3−k0≤2 remain; reducedness is established first. |
| General weighted curve cohomology | Dolgachev1.4.1 applied to the original hypersurface sequence | S=C[u,v,w], weights(a,b,c), twist−e. The long exact sequence yields h1OD=dimS_(e−a−b−c), h0OD=1. All monomial counts and elliptic-component degrees remain. |
| Degree7 and degree9 vertex calculations | Retained at P454 | Explicit permutation (x,y,z)→(z,x,y) identifies both printed weight orders. Every prime-order and order-four branch orbit, invariant-order and quadratic-character calculation remains. |
| Degree9 isolated cone | A.5.17 local clause then P322 | H=P9 gives sphere−2 in a small level. D_lambda^-1 takes it to P9=1; G_epsilon transport places it in g_u=alpha epsilon^9 and then Phi=(alpha epsilon^9)^m. No torus hypothesis is imposed on the leading polynomial. |
| Final noncontracted section | Exact current R18 application | Same f,Y,B,mS, normalization resolution and H, with all global irreducible-or-NC/positive-Euler/positive-genus hypotheses explicitly matched. |

The final repeated numerical paragraph is integrated at its unique uses: the Fermat cubic gradient example at the cubic section ring, degree6 gap10 at its contradiction, degree7 gaps18/11 there, and all monomial/quadratic-character counts at their existing proofs. Every equation4.54w.1–5/4.54a retains its prepared label. The full fixed-r construction is preserved rather than replaced by an unproved normal-form identification.

## Primary readings

Dolgachev, Weighted projective varieties, Group Actions and Vector Fields, LNM956(1982),34–71, DOI10.1007/BFb0101508. Complete Theorem1.4.1 and proof pp39–41 read. Author PDF https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/weighted82.pdf; SHA256 f93b558ac5ffe7420f5d64c8faac28587fb064b7a7b7cca5405e9b1d89410926. Publisher metadata verified.

Park and Suh, Kyushu J.Math50(1)(1996),179–205, DOI10.2206/kyushujm.50.179. Rendered primary pp179–180, full setup and Theorem1.2 read; its later proof is not claimed read. URL https://www.jstage.jst.go.jp/article/kyushujm/50/1/50_1_179/_pdf/-char/en; SHA256 50ff3fa390399ba302fc0f80c327aae0c7d2bd1a2fd6c3e3cc44b9e66c719165. The compact algebraic double fits the theorem's real algebraic finite-group hypotheses exactly.

Hatcher2002, proof2C.3 pp180–181, including the cellular/homology alternating-trace identity on181, read in full. The exact half/core comparison is retained for this application.

Milnor1968, full Lemma6.1/proof pp55–56 and AppendixB pp111–114 read in the primary-text OCR at https://djvu.online/file/kCFrJq27uCPRi. No complete PDF download/hash or whole-book reading is claimed. Two trial image downloads showed other printed pages58/120 and receive no credit for the desired loci. Existing Princeton bibliography is unchanged; no mirror URL is inserted there.

Grauert1960 p59 HauptsatzeI/IIa setup, statements and printed final arguments, plus the entire1963 erratum pp35–36, read from attached primary text. This does not claim reading the whole preceding coherence proof. The exact local formal-functions application remains complete in P454.

Six exact guards cover A.5.17, P322, the entire P454 subsection, the bounded P453 root-function paragraph and the two verified bibliography entries. Full original/current and receiving proofs have been compared; every old label/target multiplicity survives. P451's complete unit-flow proof and P452's explicit use were reread; P452 is unchanged, and no false theorem is alleged. Root owns admission, integrated build/page reading, front matter and whole-paper ordering. Exposed evidence only; no independent credit or required-check increment.
'''
write_unit_logs('elliptic_contraction','night:P4.54','Elliptic contraction subsection',
 review,readings,specific,comparison,6)
