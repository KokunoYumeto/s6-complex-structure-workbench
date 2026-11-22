from pathlib import Path
import datetime, hashlib, json, re

ROOT = Path('/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH')
REC = ROOT/'agents/ii_checks_A/recovery_20261121T195642Z'
OUT = REC/'group05'
OUT.mkdir(exist_ok=True)
releases=json.loads((REC/'S6_SERIES_PUBLISH_II_A_recovery_group05_releases.json').read_text())
original={Path(x['full_block']).parts[3]: (ROOT/x['full_block']).read_text() for x in releases}
current=dict(original)
guards=[]
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def rel(p):return str(p.relative_to(ROOT))
def edit(tag,old,new,types,reason,transport):
    before=current[tag]
    assert before.count(old)==1,(tag,old,before.count(old))
    after=before.replace(old,new,1)
    guards.append(dict(tag=tag,guard_id=f'A_REC_G05_{len(guards)+1:03}',defect_types=types,
      literal_old=old,literal_new=new,reason=reason,mathematical_transport=transport,
      offset_before=before.index(old),intermediate_before_sha256=sha(before),
      intermediate_after_sha256=sha(after),
      full_original_path=rel(OUT/f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex'),
      full_proposed_path=rel(OUT/f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex')))
    current[tag]=after

edit('02WN','[P4.16]',r'[A spherical intersection obstruction]', ['D04','D16'],
 'Give the proposition a mathematical title.', 'Identical hypersurface germs, multiplicities and degeneration hypotheses.')
edit('02WN','No hypothesis on $b_2$ is needed.',
 'The total threefold may have arbitrary second Betti number.', ['D02'],
 'State the full Betti-number scope positively and once.', 'The same unconstrained second Betti number of the total threefold.')
edit('02WN',r'Van Kampen gives $\pi_1(F_n)=0$.',
 r'Van Kampen gives $\pi_1(F_n)=0$; see \cite[Theorem~1.20, p.~43]{Hatcher2002}.', ['D17','D18'],
 'Give the opened primary locator for the fundamental-group computation.',
 'Each displayed intersection y-loop maps to the same generator in U and to zero in its contractible graph neighbourhood.')
edit('02WN','Mayer--Vietoris identifies',
 r'Mayer--Vietoris \cite[\S2.2, pp.~149--150]{Hatcher2002} identifies', ['D17','D18'],
 'Give the opened exact-sequence locator.', 'The same three-open-set cover and the two inclusion maps to H1(U).')
edit('02WN','hence with $\\mathbb Z$. Hurewicz represents its\ngenerator by a map $S^2\\to F_n$.',
 'hence with $\\mathbb Z$. The Hurewicz theorem\n\\cite[Theorem~4.32, pp.~366--367]{Hatcher2002} represents its\ngenerator by a map $S^2\\to F_n$.', ['D17','D18'],
 'Cite the exact primary theorem used for spherical representability.',
 'The Hurewicz map sends a sphere to its integral fundamental homology class on this simply connected F_n.')
edit('02WN','Both infinity divisors are removed, so no extension of the\nrational function at their intersection is asserted or needed.\n','', ['D02','D11'],
 'The complete boundary list already specifies the removed infinity divisors.',
 'T_n minus B is unchanged, and both infinity divisors remain explicitly included in B.')
edit('02WN','Compact-support duality and the sequence of $(T_n,B)$ identify',
 'Compact-support duality \\cite[Theorem~3.35, p.~245]{Hatcher2002}\nand the sequence of $(T_n,B)$ identify', ['D17','D18'],
 'Cite the opened integral duality theorem.',
 'H2(F_n;Z) maps by inverse cap duality to Hc2(F_n;Z)=H2(T_n,B;Z) in cohomological degree two, then to H2(T_n;Z) by cap duality; the map is induced by inclusion.')
edit('02WN','The sequence introduces no multiple: $H_1(B)=0$ injects\n$H^2(T_n,B)$ into $H^2(T_n)$ with precisely the stated kernel.',
 'Since $H^1(B;\\mathbb Z)=0$, the pair sequence injects\n$H^2(T_n,B;\\mathbb Z)$ into $H^2(T_n;\\mathbb Z)$ with\nprecisely this integral kernel.', ['D02','D22'],
 'State the exact cohomology map and its injectivity positively.',
 'H1(B;Z)=0 implies H1 cohomology zero by universal coefficients; exactness gives the identical primitive kernel.')
edit('02WN','The exact matrices, primitive kernels, boundary graphs and\nblowup identities for $n=1,\\ldots,12$ are independently checked\nby \\texttt{code/part4/milnor\\_intersection.py}; its output and\nJSON data are included. The proof is uniform in $n$.',
 'The corresponding computation forms the intersection matrix from\nthese boundary classes and calculates its primitive integral kernel;\nits source is listed in Table~\\ref{tab:II:programs}.', ['D07','D08','D09','D21'],
 'Move the program path and finite-run bookkeeping to the program table and check record.',
 'The uniform integral kernel and square -2n remain proved immediately above; all original finite cases, matrices and blowup charts were rerun and separately compared.')
edit('02WN','We also check the unit and multiplicity in an actual defining\nmap. Take an analytic $m$-th root of its unit. For a unit $h$,',
 'Write the local defining function as $u(x^2-zy^n)^m$, with $u$\na unit, and choose a holomorphic root $h^m=u$. Then', ['D08','D20'],
 'Introduce the defining-map calculation in mathematical language.',
 'The same local holomorphic map is a unit times g^m; the analytic m-th root of that unit is unchanged.')
edit('02WN','Thus the actual local map to the\nbase is $(g\\circ\\Phi)^m$.',
 'Thus the local map to the\nbase is $(g\\circ\\Phi)^m$.', ['D08'],
 'Remove the process modifier.', 'Identity of the displayed analytic morphism and its multiplicity.')

edit('02WO','[P4.17]',r'[The lattice of $x^a-zy^n=1$]', ['D04','D16'],
 'Give the proposition a mathematical title.', 'Identical lattice, normalization examples and obstruction.')
edit('02WO','For all $a\\geq2$ and $n\\geq1$, the germ $x^a-zy^n=0$ is\nexcluded in the setting of P4.16.',
 'For all integers $a\\geq2$ and $n\\geq1$, the germ $x^a-zy^n=0$ is\nexcluded in the setting of Proposition~\\ref{night:P4.16}.', ['D04','D23'],
 'Resolve the inherited reference and make the integer parameters explicit.',
 'The same integer exponents and the same proper torus degeneration with smooth total space.')
edit('02WO','\\item Replace the two roots of $x^2=1$ in P4.16 by the $a$ distinct\nroots of $x^a=1$.',
 '\\item Put $F_{a,n}=\\{x^a-zy^n=1\\}$. Replace the two roots of\n$x^2=1$ in Proposition~\\ref{night:P4.16} by the $a$ distinct\nroots of $x^a=1$.', ['D04','D20'],
 'Define the fibre notation at its first use and resolve its input.',
 'F_{a,n} is exactly the affine nearby fibre already named in the statement.')
edit('02WO','The explicit unit removal\nand torus argument of P4.16 now exclude $v_1$, whose square\nis $-2n$. The program independently checks the complete\nmatrices and primitive bases for $2\\leq a\\leq6$, $1\\leq n\\leq6$.',
 'The unit-removal map and torus argument in\nProposition~\\ref{night:P4.16}, with these weights, exclude $v_1$,\nwhose square is $-2n$. The computation of the integral kernel\nfrom the displayed boundary classes is listed in\nTable~\\ref{tab:II:programs}.', ['D04','D07','D08','D09','D21'],
 'Resolve the theorem reference and move finite-run bookkeeping to its record.',
 'The analytic map is Phi_j=h^(w_j/[a(n+1)])x_j with weights (n+1,a,a); every original matrix and primitive basis is preserved by the stated exceptional-chain basis.')
edit('02WO','For $n=a$ the quotient is smooth with coordinates $(y,v)$,\nand its conductor map is $v\\mapsto v^a$. This verifies\nexplicitly the cyclic branch-permutation description.',
 'For $n=a$ the quotient is smooth with coordinates $(y,v)$,\nand the reduced conductor $\\{y=0\\}$ maps to $\\{x=y=0\\}$\nby $z=v^a$. A positive loop about $z=0$ sends $v$ to\n$e^{2\\pi i/a}v$, cyclically permuting the $a$ branches.', ['D08','D20','D22'],
 'Specify the conductor source, target and induced permutation.',
 'The quotient map remains (x,y,z)=(yv,y,v^a); the reduced conductor and singular axis are its displayed coordinate subspaces.')

edit('02WP','[P4.18]',r'[Spherical classes for binomial surface germs]', ['D04','D16'],
 'Give the proposition a mathematical title.', 'Identical binomial family, common multiplicity, nonzero square and mixed normalization example.')
edit('02WP','in a torus degeneration with smooth total threefold.',
 'in a proper holomorphic degeneration of complex two-tori with\nsmooth total threefold.', ['D20'],
 'Spell out the standing degeneration setting.',
 'The same holomorphic map to a curve and the same smooth compact complex two-torus general fibre used by the cited proposition.')
edit('02WP','with $u$ a unit. Taking a $B$-th root of $u$, rescaling $y$,\nand making an affine coordinate change identifies the preimage\nof $D$ with',
 'with $u$ a unit. Set\n\\[\n X=\\frac{2\\xi-\\alpha-\\beta}{\\beta-\\alpha},\\qquad\n h_0(\\xi)=\\frac{(\\beta-\\alpha)^2}{4}u(\\xi),\\qquad\n y_{\\mathrm{new}}=\\frac{y}{h_0(\\xi)^{1/B}}.\n\\]\nA holomorphic $B$-th root exists on the disc. In these coordinates,\nwriting $y$ for $y_{\\mathrm{new}}$, the preimage of $D$ is', ['D20','D22'],
 'Give the complete coordinate change, including the constant factor.',
 'w=h_0(X^2-1) and y_new^B z^C=X^2-1; the inverse is xi=((beta-alpha)X+alpha+beta)/2 and y_old=h_0^(1/B)y_new.')
edit('02WP',' \\begin{pmatrix}B&C\\\\q&-p\\end{pmatrix},\\qquad \\det=-1.\n\\]\nThus adjoining each neighbourhood kills',
 ' M=\\begin{pmatrix}B&C\\\\q&-p\\end{pmatrix},\\qquad\n M^{-1}=\\begin{pmatrix}p&C\\\\q&-B\\end{pmatrix}.\n\\]\nThe equality $Bp+Cq=1$ proves this integral inverse.\nThus adjoining each neighbourhood kills', ['D22'],
 'Give the integer inverse that proves both meridians are killed.',
 'The same two loop images are the columns of M; its inverse sends beta and tau back to integral combinations of the two source loops.')
edit('02WP','The compact class $v$ in\nP4.16, of square $-2B$, is already supported over $D\'$.',
 'The compact class $v$ in\nProposition~\\ref{night:P4.16}, with $n=B$ and square $-2B$,\nhas a representative supported over $D\'$.', ['D04','D08','D20'],
 'Resolve the exact parameter in the cited class.',
 'The source surface is X^2-y^B Z=1, the same hypersurface with coordinate permutation (x,y,z)=(X,y,Z).')
edit('02WP','For its compact-support dual $\\alpha\\in H_c^2(W\';\\mathbb Z)$,\nproperness and degree give',
 'Let $\\alpha\\in H_c^2(W\';\\mathbb Z)$ be its compact-support dual\nunder \\cite[Theorem~3.35, p.~245]{Hatcher2002}. Proper pullback\npreserves compact support, and the degree formula gives', ['D17','D18','D22'],
 'Identify the duality and the proper map used for the integral class.',
 'The pullback is along pi(X,y,z)=(X,y,z^C), an oriented finite map of degree C between smooth complex surfaces.')
edit('02WP','The dual of $\\pi^*\\alpha$ is spherical\nby $\\pi_1(W)=0$ and Hurewicz.',
 'The dual of $\\pi^*\\alpha$ is spherical\nby $\\pi_1(W)=0$ and \\cite[Theorem~4.32, pp.~366--367]{Hatcher2002}.', ['D17','D18'],
 'Give the exact spherical-representability locator.',
 'Hurewicz is applied to the same simply connected open surface W, before inclusion into F.')
edit('02WP',"nearby fibres. P4.16's explicit unit removal handles the unit\nand common multiplicity.",
 'nearby fibres. The unit-removal map in\nProposition~\\ref{night:P4.16}, with these weights, handles\nthe unit and common multiplicity.', ['D04','D20'],
 'Resolve the theorem reference and its weight substitution.',
 'Phi_j=h^(w_j/[a(b+c)])x_j for weights (b+c,a,a), after taking the m-th root of the defining-map unit.')
edit('02WP','Its conductor is $u^2v^2\\mathbb C\\{u,v\\}$, giving divisor',
 'Since the normalization is generated over the image ring by $1,u$,\nits conductor consists of the series $h$ for which both $h$ and $uh$\nlie in that ring. The even--odd monomial description therefore gives\n$u^2v^2\\mathbb C\\{u,v\\}$, with divisor', ['D22'],
 'Give the finite-module test proving the asserted conductor ideal.',
 'Under the same normalization map, multiplication by u switches parity; the two membership tests require u-exponent at least 2 and v-exponent at least 2.')
edit('02WP','with common divisorial factor $u$.\nThus this example explicitly lies outside P4.15\'s finite\nrank-drop assumption. The 64 exponent matrices for\n$1\\leq b,c\\leq8$, transfer squares and normalization\nidentities are executed in\n\\texttt{code/part4/binomial\\_milnor.py}; its output and\nJSON data are saved alongside it.',
 'and generate the ideal $(u)$. Thus the rank-drop locus is exactly\nthe divisor $\\{u=0\\}$, which maps by $v\\mapsto(0,v,0)$\nto a line. The finite rank-drop hypothesis of\nProposition~\\ref{night:P4.15} fails for this morphism.\nThe exponent-matrix, transfer-pairing and normalization computations\nare listed in Table~\\ref{tab:II:programs}.', ['D04','D08','D09','D21','D22'],
 'Give the exact rank-drop image and move computation bookkeeping to the table.',
 'The minor -2u generates (u) over C; dnu has rank one there because the v derivative has middle coordinate 1. The explicit image line proves the one-dimensional locus.')

edit('02WQ','[P4.19]',r'[A ramified conductor with vanishing nearby homology]', ['D04','D16'],
 'Give a mathematical title naming the conductor and fibre conclusion.',
 'Identical local reduced union, normalization conductor and nearby fibre.')
edit('02WQ','The germ $y(x^2-zy^2)=0$ has ramified conductor, of multiplicity\ntwo on each normalization component, but its affine nearby\nfibre is $\\mathbb C^*\\times\\mathbb C$. Ramification alone\ntherefore does not give the spherical intersection obstruction\nof P4.16--P4.18. This is a local statement, not a compact\ncounterexample to 4.2.',
 'For the reduced hypersurface germ $y(x^2-zy^2)=0$, the normalization\nconductor has multiplicity two on each component and its reduced\nmap to the singular locus is ramified. The affine nearby fibre is\n$\\mathbb C^*\\times\\mathbb C$. Every compact spherical class\nin an open subset of this affine fibre has self-intersection zero.', ['D02','D04','D05','D11','D20'],
 'State the local object, conductor map and zero-square conclusion directly.',
 'The same union germ and fibre F=1 give the same local example of ramification together with vanishing spherical intersection. No compact degeneration is introduced or removed.')
edit('02WQ','On the Whitney component the intrinsic conductor\nis $v\\mathbb C\\{u,v\\}$; multiplication by the added plane\nequation $y=v$ gives $v^2\\mathbb C\\{u,v\\}$. Directly, the\nunion ring is the fibre product of the component rings over\n$\\mathbb C\\{x,z\\}/(x^2)$, giving exactly these conductor ideals.',
 'Write $R_B=\\mathbb C\\{v,uv,u^2\\}$ and\n$N_B=\\mathbb C\\{u,v\\}$. The module $N_B$ is generated over\n$R_B$ by $1,u$. A convergent series lies in $R_B$ precisely when\nits odd powers of $u$ have coefficients divisible by $v$.\nThus $h,uh\\in R_B$ is equivalent to $h\\in vN_B$, proving\nthat the intrinsic conductor is $vN_B$.\nThe union ring is the fibre product of the component rings over\n$\\mathbb C\\{x,z\\}/(x^2)$. On the Whitney component, a\nconductor element $h$ must satisfy $hN_B\\subset vR_B$; the\nintrinsic conductor calculation gives $h\\in v^2N_B$.\nOn the plane, the corresponding kernel is $(x^2)$.\nThese are the two claimed conductor ideals.', ['D20','D22'],
 'Spell out the module membership calculation for the full union conductor.',
 'The fiber-product maps are restriction y=0 on the Whitney ring and quotient modulo x^2 on the plane. The support kernels are vR_B and x^2 C{x,z}; multiplication in each normalization gives exactly v^2 N_B and x^2 C{x,z}.')
edit('02WQ','On $y(x^2-zy^2)=1$ we have $y\\ne0$, and the inverse maps',
 'Put $F=\\{y(x^2-zy^2)=1\\}$. Here $y\\ne0$, and the inverse maps', ['D20'],
 'Define the nearby-fibre symbol used in the inclusion and integral formula.',
 'F is exactly the affine hypersurface already displayed in the original proof.')
edit('02WQ','Its $\\pi_2$ and $H_2$ vanish. Hence every compact spherical\nclass in an open subset has zero square after inclusion,\nand therefore has zero square already in that open subset.',
 'The retraction $(y,x)\\mapsto(y/|y|,0)$ is a homotopy equivalence\nwith $S^1$, so $\\pi_2$ and $H_2$ vanish. For an open inclusion\n$j:U\\hookrightarrow F$, compact-support duality identifies the\nhomology map $j_*$ with extension by zero $j_!$ on dual classes.\nFor the compact-support dual $\\alpha$ of a compact spherical class,\n\\[\n \\int_U\\alpha^2=\\int_F(j_!\\alpha)^2=0.\n\\]\nThis proves the asserted zero self-intersection in $U$.', ['D22'],
 'Specify the homotopy and the exact map preserving the compact intersection pairing.',
 'On C* x C use H_s(y,x)=((1-s+s/|y|)y,(1-s)x). Extension by zero commutes with compactly supported cup products and inverse cap duality sends it to inclusion of compact cycles.')

blocks=[]
for tag in original:
    op=OUT/f'S6_SERIES_PUBLISH_II_{tag}_full_original.tex'
    pp=OUT/f'S6_SERIES_PUBLISH_II_{tag}_full_proposed.tex'
    op.write_text(original[tag]);pp.write_text(current[tag])
    anchors=lambda s:re.findall(r'\\(?:hypertarget|label)\{[^}]*\}',s)
    assert anchors(original[tag])==anchors(current[tag]),tag
    blocks.append(dict(tag=tag,original_path=rel(op),original_sha256=sha(original[tag]),
      proposed_path=rel(pp),proposed_sha256=sha(current[tag]),
      original_characters=len(original[tag]),proposed_characters=len(current[tag]),
      guards=[g['guard_id'] for g in guards if g['tag']==tag],anchors_exact=True))

manifest=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
 checker='ii_check_a',canonical_writes=False,guards=guards,blocks=blocks,
 note='Full owning blocks released only after immutable derivations; root alone integrates. Enumeration wrappers remain for the final global mapping; this batch does not claim global D04 closure.')
p=OUT/'S6_SERIES_PUBLISH_II_A_recovery_group05_editorial_proposals.json'
p.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(manifest=rel(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                     guard_count=len(guards),blocks=blocks),indent=2))
