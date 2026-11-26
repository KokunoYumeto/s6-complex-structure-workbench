"""Stage exact root image findings after full bounded source reading; no master writes."""
from pathlib import Path
from datetime import datetime, timezone
import csv, io, re, difflib, hashlib
ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT.parents[1]/'tmp/c9_root_image_repairs'
OUT=ROOT/'agents/continuation9_root_image_repairs'
SOURCE=ROOT/'S6_SERIES_PUBLISH_III.tex'
source=SOURCE.read_text(); initial=source
blocks={}; history=[]; scopes={}

def block(tag):
 if tag not in blocks:
  old=(TMP/(tag+'_old.tex')).read_text()
  if tag=='02M2':
   old=r'\subsection{Complex invariants of the smoothing}'+'\n'+old
  assert source.count(old)==1,tag
  blocks[tag]=[old,old]
 return blocks[tag][1]

def change(tag,name,begin,end,pairs,reason,kind='D20'):
 s=block(tag);a=s.index(begin);b=s.index(end,a) if end else len(s)
 old=s[a:b];new=old; counts=[]
 for x,y in pairs:
  n=new.count(x);assert n,(tag,name,x)
  new=new.replace(x,y);counts.append((x,y,n))
 assert old!=new and s.count(old)==1
 blocks[tag][1]=s[:a]+new+s[b:]
 history.append(dict(tag=tag,name=name,old=old,new=new,reason=reason,kind=kind,counts=counts))

def symbol_pairs(s,pairs):
 # Used only for explicitly read scopes; returns whole exact scope as one replacement.
 out=s
 for x,y in pairs:
  pattern=r'(?<![A-Za-z\\])'+re.escape(x)+r'(?![A-Za-z_])'
  out,n=re.subn(pattern,lambda m:y,out);assert n,(x,s[:60])
 return [(s,out)]

change('02S3','based-matrix-index',r' F_{p,q}=',r'The logarithms',[(r'F_{p,q}',r'F_{p,q_\delta}')],
 'The already declared second integer coefficient is q_delta, with kappa=p w_Z+q_delta delta. F_{p,q_delta} is exactly the displayed involution matrix, fixing all four ordered coordinates under the identity name map; its inverse remains itself. Every occurrence through the finite-vector conjugation changes together. The cusp coordinate q is retained.')
change('02S3','ordinary-point',r' D_n(p,V)=',r'\]',[(r'(p,V)',r'(p_E,V)'),(r'(p,t^nV)',r'(p_E,t^nV)'),(r'(p,t^{-n}V)',r'(p_E,t^{-n}V)')],
 'p_E is the same point of the ordinary elliptic source in D_n and its displayed inverse. The map p_E→p and its inverse p→p_E fix that point; the independent integer p in the marked period matrix is retained. All scalar multipliers remain t^n and t^-n.')
change('02S3','extending-origin',r'Subtraction of the two origins',r'For the based lift',[(r'\sigma',r'\sigma_{\rm ext}')],
 'sigma_ext is the existing additive extending-origin vector nv epsilon+nmv(v-1)delta. Its occurrence in sigma_ext-o and its extension at q=0 are changed together; the inverse name map fixes that vector. The earlier finite-root coordinate sigma and t=sigma^m retain their original domain and formula.')
local=block('02M2');local=local[local.index('At $t=0$'):local.index('On the moving chart')]
change('02M2','local-weierstrass-coordinates','At $t=0$','On the moving chart',symbol_pairs(local,[('X',r'X_{\rm W}'),('Y',r'Y_{\rm W}')])+[(r'dX',r'dX_{\rm W}'),(r'qY}',r'qY_{\rm W}}')],
 'X_W and Y_W are the displayed local Weierstrass coordinate functions in the three explicitly specified charts. Every coordinate formula, cubic equation, differential and nodal point is obtained by the identity substitution X_W=X,Y_W=Y on that chart, with inverse X=X_W,Y=Y_W. The threefold Y=Y_{u,s}, its structure sheaf and cohomology retain Y.')
change('02M3','general-fibre-name','Hence the general fibre',r'Both total spaces',[(r'$F_t$',r'$\mathcal F_t$'),(r'H_1(F_t;',r'H_1(\mathcal F_t;')],
 'mathcal F_t denotes the same general torus fibre g^-1(t), with identity comparison and inverse on its points. Its integral H1 group is unchanged. F_t later remains the restriction of a proposed biholomorphism, with its already explicit inverse; the domain and map receive distinct printed names.')
change('02M2','subsection-opening',r'\subsection{Complex invariants of the smoothing}',r'\begin{theorem}',[
 (r'\subsection{Complex invariants of the smoothing}',r'\Needspace{12\baselineskip}'+'\n'+r'\subsection{Complex invariants of the smoothing}')],
 'The actual candidate02 page591 leaves the subsection title at the foot while the theorem opens on592. Reserve room before the entire subsection so its title and the formal opening accompany substantive text. All statement and proof text, labels and targets remain fixed.','D04')
change('Q019','base-coordinate-name','Definition~\\ref{mapsIII:def:kummer-data}.','\\[', [('Write $t=q$, with inverse\n$q=t$, for its base coordinate.','Write $t=q$ for its base coordinate.')],
 'The retained t=q names the same base coordinate. The inverse name assignment q=t composes to the identity; only its redundant restatement is removed. Every actual target/source root action, rho_N and the normalization data remain unchanged.','D08')
change('035X','based-rotation','Take the diffeomorphism',r'The compact product',[(r'rotation $R$',r'rotation $O_{\rm rot}$'),(r'$Rh(x_0)',r'$O_{\rm rot}h(x_0)'),(r'$h_0=Rh$',r'$h_0=O_{\rm rot}h$'),(r'$h^{-1}R^{-1}$',r'$h^{-1}O_{\rm rot}^{-1}$')],
 'O_rot is exactly the same target rotation formerly R. The based diffeomorphism is h0=O_rot h and its inverse remains h^-1 O_rot^-1; both composites are identities by the same inverse rotations. The metric radius R throughout the theorem is unchanged.')
change('0375','loop-exponent','The dual form is',r'the integral double-annihilator',[(r'G_*^h',r'G_*^{j_{\rm loop}}'),('6hb_i',r'6j_{\rm loop}b_i'),('hb_i',r'j_{\rm loop}b_i')],
 'j_loop is the same integer power in the all-power loop formula. Substitution j_loop=h fixes the loop operator G_* and both resulting character coordinates, with inverse h=j_loop. The later based diffeomorphism h:X→S6 retains h.')
old=r''' u_T:(0,1)^2\longrightarrow Q_T\setminus K_T^{(1)},\quad
        a\longmapsto[Y_Ta],\qquad
 v_T:(0,1)\longrightarrow C_T\setminus\{0\},\quad
        a\longmapsto[\ell_Ta]'''
new=r''' \begin{aligned}
 u_T:(0,1)^2&\longrightarrow Q_T\setminus K_T^{(1)},\quad
        a\longmapsto[Y_Ta],\\
 v_T:(0,1)&\longrightarrow C_T\setminus\{0\},\quad
        a\longmapsto[\ell_Ta].
 \end{aligned}'''
change('036V','paired-map-width','Here are coordinates and inverses.',r'are homeomorphisms.',[(old,new)],
 'The actual candidate02 page639 places the paired maps beyond the normal right text margin. The two identical maps are set on separate aligned lines; their domains, targets and formulas remain term-for-term the same. Both following inverse constructions remain intact.','D04')
change('038W','retract-map-statement','there\nare based maps',r'The initial quotient maps',[(r'$R:',r'$R_{\rm ret}:'),(r'$RJ',r'$R_{\rm ret}J'),(r'$R_*',r'$(R_{\rm ret})_*')],
 'R_ret is the existing homotopy retract from A smash A to C6. The renamed map is literally the same composition mu_(4,2)(r4 smash r2), with the same R_ret J based homotopy and induced detection class. The radius R in the metric assertions is unchanged.')
change('038W','retract-map-proof','For the inclusion $i_4',r'\emph{2. The initial maps',[(r'\qquad R=',r'\qquad R_{\rm ret}='),(r'$RJ',r'$R_{\rm ret}J'),(r' R_*',r' (R_{\rm ret})_*'),(r'$R_*',r'$(R_{\rm ret})_*')],
 'The construction and both induced homology/homotopy detections use the same R_ret as the statement. Exact inverse name substitution R=R_ret returns all original formulas; J, r2, r4, mu and their domains are fixed.')
change('038W','subset-index','All other homology groups vanish.',r'Each increasing',[(r'|J|',r"|I'|"),(r'e_J',r"e_{I'}"),(r'I=J',r"I=I'")],
 'I-prime is the same second nonempty subset in the degree comparison; the index bijection J↔I-prime fixes its cell and cardinality. The map J:C6→A smash A retains its letter throughout the statement and proof.')

change('02LW','invariant-basis-columns','The reduced invariant bases are',r'For an edge-kernel vector',[(r'F_1',r'\mathsf B_1'),(r'F_2',r'\mathsf B_2'),(r'F_3',r'\mathsf B_3')],
 'The three displayed invariant column lists are named mathsf B_i. The comparison mathsf B_i=F_i fixes every listed vector and every ordered column of L, with inverse F_i=mathsf B_i on this basis-list scope. The reduced central surfaces F_i in H1, H3 and H4 retain their names.')
change('02LW','abelian-source-and-quotient','The integral specialization',r'We now compute the finite boundary map',[
 ('H^3(F_i)$ free of ranks','H^3(F_i)$ free abelian of ranks'),('free group $Q$','free abelian group $Q$')],
 'Both occurrences concern additive integral homology or its quotient with displayed integral bases. The same group, operation, generators and identity maps remain; the word abelian specifies the operation already used.','D02')
change('02LX','period-shear-name','At $I_2$ the period change',r'The monomial map',[
 ('$g=Fh^3$',r'$g_{\rm per}=Fh^3$'),('$F=gh^{-3}$',r'$F=g_{\rm per}h^{-3}$')],
 'g_per is precisely the multiplicative period Fh^3 in the same unimodular shear, and its displayed inverse remains F=g_per h^-3. The later affine deck transformation g and all its normal forms remain unchanged.')
local=block('02LX');local=local[local.index('The common fibre coinvariants'):local.index('The section therefore gives')]
change('02LX','coinvariant-relation-vectors','The common fibre coinvariants','The section therefore gives',
 symbol_pairs(local,[('p',r'p_{\rm rel}'),('q',r'q_{\rm rel}'),('w',r'w_{\rm rel}')]),
 'p_rel,q_rel,w_rel are exactly the three displayed relation vectors e1+e2,e1+2e2,2e2+e3. Their inverse formulas for e1,e2,e3 are changed by the same identity substitutions. The earlier additive period coordinate p, the graph cutting map p, and the marked cohomology coordinate w remain fixed.')
change('02LX','invariant-basis-columns','The reduced fixed lattices have bases',r'For a graph-kernel vector',[
 (r'F_2',r'\mathsf B_2'),(r'F_+',r'\mathsf B_+'),(r'F_-',r'\mathsf B_-')],
 'The three invariant column lists become mathsf B_2,mathsf B_+,mathsf B_-. Each is the identical ordered list formerly F_2,F_+,F_-, so substitution and its inverse fix the eight columns of L. The central surfaces F_i and the period F in Fh^3 retain their names.')
local=block('02LX');local=local[local.index('Writing $h=2a_0+a_1$'):local.index('Substitution in either direction')]
change('02LX','edge-scalar','Writing $h=2a_0+a_1$','Substitution in either direction',
 symbol_pairs(local,[('h',r'h_{\rm edge}')]),
 'h_edge is the same graph-coordinate scalar 2a0+a1. Every occurrence in the inverse vector eta changes together, and the reverse substitution recovers that vector. The multiplicative period h and the logarithmic translations h_u retain their meanings.')
local=block('02LX');local=local[local.index('The quotient by the eight reduced tori'):local.index('The two rank-one fibres,')]
change('02LX','reduced-homology-quotient','The quotient by the eight reduced tori','The two rank-one fibres,',
 symbol_pairs(local,[('Q',r'\mathcal Q_{\rm red}')])+[('free group', 'free abelian group')],
 'mathcal Q_red is the same quotient of H2(V) by the eight reduced normal-torus classes, with coordinate map [Z]↦(integral_Z Omega,e0-dual(p(Z)_*)) and inverse (a,b)↦as+bt. All subsequent finite-boundary images use this identical quotient. The elliptic section Q=6P in the statement is unchanged; abelian records the displayed additive operation.','D20;D02')
change('02LX','period-basis-introduction','In the additive coordinates',r'The multiplicative line coordinate',[
 (r'a_0',r'\alpha^{\rm per}_0'),(r'a_1',r'\alpha^{\rm per}_1'),(r'a_2',r'\alpha^{\rm per}_2'),(r'a_3',r'\alpha^{\rm per}_3')],
 'alpha_i^per is exactly the original additive period vector a_i, in its original order and with the same coordinate values. The explicit map to (e0,e1,e2,e3) remains unchanged after substitution. This prevents the later graph components a_i from also naming periods.')
change('02LX','period-basis-filling-import','Every invariant period acts',r'The logarithmic disc terms',[
 (r'a_3',r'\alpha^{\rm per}_3'),(r'a_2',r'\alpha^{\rm per}_2'),(r'a_1',r'\alpha^{\rm per}_1')],
 'The zero-valuation and elliptic period formulas use precisely the alpha_i^per introduced above. Their ordered sums and determinant-one change are unchanged under the inverse substitution alpha_i^per↦a_i.')
change('02LX','period-basis-final-import','At $(k,n,r)=(1,1,0)$, the vector',None,[
 (r'a_3',r'\alpha^{\rm per}_3'),(r'a_2',r'\alpha^{\rm per}_2'),(r'a_1',r'\alpha^{\rm per}_1')],
 'The final Wang-model vector is the same ordered period combination alpha3^per+2alpha2^per-4alpha1^per=ell. All identity maps on the root-disc and Mumford charts are retained.')
change('02LX','graph-cutting-map','Cut the torus bundle',None,[
 (r'\xrightarrow{p}',r'\xrightarrow{p_{\rm cut}}'),('p(Z)',r'p_{\rm cut}(Z)')],
 'p_cut is the existing cutting homomorphism H2(V)→kerD, used with the same coordinate in the quotient map. The identity comparison and inverse fix its image and all sweep coordinates. The analytic period p in the original additive marking retains p.')
change('0374','loop-power','Consequently, for every integer',r'For each positive integer',[
 (r'U^h',r'U^{k_{\rm loop}}'),(r'\(h\)',r'\(k_{\rm loop}\)'),(r'\(h>0\)',r'\(k_{\rm loop}>0\)'),
 (r'hL_0',r'k_{\rm loop}L_0'),(r'-hu',r'-k_{\rm loop}u'),(r'+h\delta',r'+k_{\rm loop}\delta'),
 (r'\(hu_i',r'\(k_{\rm loop}u_i'),(r'(-h,1)',r'(-k_{\rm loop},1)')],
 'k_loop is the identical integer power of U in the finite-index argument. Its coefficient in U^k_loop, every lattice vector and every projected plane changes together. The inverse k_loop↦h fixes U, its inverse word and all lattice inclusions. Later diffeomorphisms h keep their specified domains.')
local=block('0374');local=local[local.index('For the construction of'):local.index(r'\emph{Almost-complex structures.}')]
new=local.replace('_N',r'_{N_{\rm cov}}').replace('^N',r'^{N_{\rm cov}}')
new=symbol_pairs(new,[('N',r'N_{\rm cov}')])[0][1]
new=new.replace(r'NZ_',r'N_{\rm cov}Z_').replace('Ns_v',r'N_{\rm cov}s_v').replace('N\\zeta_v',r'N_{\rm cov}\zeta_v')
change('0374','finite-cover-index','For the construction of',r'\emph{Almost-complex structures.}',[(local,new)],
 'N_cov is exactly the integer cover parameter N from the cited finite-normal-cover construction. All indexed lattices, quotient groups, base maps, component periods, degree N_cov^2 and scaled coordinates change consistently. The inverse name substitution recovers every cover and both identity-induced maps. The primitive kernel N in the earlier rank bound retains N.')
change('0374','transported-smoothing-map','To apply this precise scope',r'For \(2n=12,24\)',[
 (r'h:M',r'h_{\rm sm}:M_{\rm sm}'),(r'manifold \(M\)',r'manifold \(M_{\rm sm}\)'),
 (r'h(V)',r'h_{\rm sm}(V)'),(r'h^{-1}',r'h_{\rm sm}^{-1}'),(r'\(h\)',r'\(h_{\rm sm}\)'),
 (r'\(TM\)',r'\(TM_{\rm sm}\)'),(r'dh\circ',r'dh_{\rm sm}\circ')],
 'h_sm:M_sm→S^(2n) is the existing homeomorphism used to transport the arbitrary smoothing, with inverse h_sm^-1. Every transported chart and tangent conjugation uses this same map. Its inverse renaming fixes the complete construction; the earlier based h:X→S6 and integer M for the fibre cover remain fixed.')
change('036J','distance-coordinates','For $x,y\\in Q_T^2$, write',r'The inverse image of',[
 (r'a_i',r'\alpha_i'),(r'b_i',r'\beta_i')],
 'alpha_i and beta_i are exactly the distances from x_i and y_i to the transported one-skeleton. Both minima and both branches of the quotient-distance equality use the same substitution, with inverse alpha_i↦a_i,beta_i↦b_i. The earlier a_j remain cube coordinates with their displayed tangent/arctangent inverse.')
change('037M','loop-homology-generators','Their adjoint\nloop classes',r'These computations take place',[
 ('$a,b,c$',r'$e_3,f_3,g_5$'),('[a,[b,c]]=abc+acb-bca-cba',r'[e_3,[f_3,g_5]]=e_3f_3g_5+e_3g_5f_3-f_3g_5e_3-g_5f_3e_3'),
 ('$a,c$',r'$e_7,g_9$'),('[a,[a,c]]=aac-caa',r'[e_7,[e_7,g_9]]=e_7e_7g_9-g_9e_7e_7')],
 'The first free tensor-algebra generators (a,b,c) are renamed (e3,f3,g5), and the second pair (a,c) is renamed (e7,g9), with their subscripts recording the already stated degrees. The inverse ordered generator maps extend uniquely to inverse tensor-algebra isomorphisms and carry every displayed commutator term with its sign unchanged. Fundamental-group a,b,h retain their earlier presentation.')
change('037M','cell-coordinate-projection','For $x\\in D^n$, write',r'maps onto $D^d$',[
 ('$u$',r'$u_{\rm cell}$'),('2u,',r'2u_{\rm cell},'),('2(1-r)u/r',r'2(1-r)u_{\rm cell}/r')],
 'u_cell is the same projection of x to its first d real coordinates, so p(x) is pointwise unchanged in both branches and has the same contraction. The primitive H2(C) generator u and all its homology maps retain u.')
change('037M','null-surjection','Pinch $S^n$ onto a finite wedge',r'All these surjections',[
 ('$h:S^n',r'$h_{\rm null}:S^n'),(r'f\vee h',r'f\vee h_{\rm null}'),('[h]',r'[h_{\rm null}]')],
 'h_null is the already constructed based null-homotopic surjection, with precisely the same cellwise maps and contraction. The pinch formula [f]+[h_null]=[f] is unchanged under h_null↦h. The fundamental-group central generator h retains h.')
change('036N','zero-chart-radius','For a zero-fibre point represented',r'Its restriction is an open',[
 ('$a>0$',r'$a_{\rm ch}>0$'),('2a+C',r'2a_{\rm ch}+C'),('B_a^',r'B_{a_{\rm ch}}^'),('$2a$',r'$2a_{\rm ch}$')],
 'a_ch is the same positive radius of the zero-fibre half-space chart. Its ball and both length bounds are changed together, preserving the precise injectivity proof. The later real marking vector a and its nonintegral coset keep a.')
change('038X','quaternion-value','The inverse of $b$ away',r'then in each coordinate',[
 (r'\mathcal Q^{-1}(q)',r'\mathcal Q^{-1}(q_{\mathbb H})'),(r'\operatorname{Im}(q)',r'\operatorname{Im}(q_{\mathbb H})'),
 (r'\operatorname{Re}(q)',r'\operatorname{Re}(q_{\mathbb H})')],
 'q_H is the same unit quaternion argument of the explicitly given inverse stereographic formula. The identity substitution q_H=q preserves both numerator and denominator. The later tubular collapse q:D3_rho→S3_H retains q.')
change('038X','rotation-axis','cover with kernel',r'Based maps from',[
 ('axis $u$',r'axis $\omega_{\rm ax}$'),(r'+u\sin',r'+\omega_{\rm ax}\sin')],
 'omega_ax is the same unit imaginary quaternion axis in the double-cover formula. Substitution omega_ax=u fixes the rotation and its covering quaternion, with the reverse name map as inverse. The real marking vector u retains its earlier coordinates.')
change('038X','rotation-map','In the boundary definition of $J$',r'The identity-family map',[
 ('$f:S^3',r'$f_{\rm rot}:S^3'),('$Jf:',r'$Jf_{\rm rot}:'),(r'q(f(x)v)',r'q(f_{\rm rot}(x)v)')],
 'f_rot is the same based map S3→SO(3) used in the boundary definition of J. The formula Jf_rot=q(f_rot(x)v) is pointwise the original, with the identical cap value. The elliptic base map f in the entire-fibre formula retains f.')
change('038X','coefficient-unit','Let $u=\\operatorname{coef}',r'Orient a three-ball',[
 ('$u=',r'$u_{\rm coef}='),('$k=u^{-1}',r'$k=u_{\rm coef}^{-1}')],
 'u_coef is precisely coef_nu9(b_*^-1 Jxi), the existing unit in Z/12. Its inverse degree k is unchanged, and the inverse name substitution recovers both equations. The real marking vector u and the separately named rotation axis keep their meanings.')
change('038X','framing-rotation','Extend $\\kappa=1$ over',r'Both $F_i$ are based smooth',[
 (r'\theta',r'\Theta_{\rm fr}')],
 'Theta_fr is the existing SO(3)-valued map Ad_kappa. Its inverse in tau1, its action on the tubular normal vector, and the computed derivative all change together, so every smooth map and frame is pointwise unchanged. The earlier angular coordinate theta retains theta.')
change('03DF','rank-polynomial-variable','After the additional local-homology shift,',r'In particular, the top groups',[
 ('the rank polynomials are',r'the rank polynomials in the formal variable \(z\) are'),
 ('t^','z^'),('3t','3z'),('2t','2z')],
 'The formal rank-polynomial variable z replaces t under the ring isomorphism Z[t]→Z[z], t↦z, with inverse z↦t. Every coefficient and exponent remains fixed. The real collar parameters t and their explicit inverse maps retain t.')
change('03DF','cone-link-name',r'Let \(d=\dim L\)',r'volume of the link.',[
 (r'Let \(d=\dim L\)',r'For the chosen link \(L_{\rm link}\in\{L_3*L_3,L_2^{*4},\partial W\}\), let \(d=\dim L_{\rm link}\)')],
 'L_link names the already constructed link of the chosen carrier: L3*L3, L2 joined four times, or boundary W, with the identity map on that selected link and its inverse. The volume argument therefore uses its established dimension 7 or 11. Earlier L=boundary M retains its original collar and quotient maps.')

change('0374','radial-residual-name',r'where \(L=T+H\)',r'The marking is',[
 (r'\(q=L-B\)',r'\(B_{\rm rad}=B\), \(q=L-B_{\rm rad}\)')],
 'B_rad denotes the same bounded radial residual coefficient B, with its exact assignment stated where it enters q. The inverse substitution leaves q and the physical period matrix unchanged. The base B and the later congruence matrix receive their own established scopes.')
change('0374','congruence-matrix','A congruence base subgroup',r'and the same formula applies',[
 ('MB)',r'M\mathsf C)'),('B_{',r'\mathsf C_{')],
 'mathsf C is the same integral congruence matrix formerly B. Its four blocks and the displayed S_M conjugation are fixed under mathsf C=B and the inverse B=mathsf C. All powers of M remain identical; the base B and the explicitly named radial residual retain their meanings.')
local=block('039U');local=local[local.index('For $A='):local.index(r'Neither \(S^{12}\)')]
change('039U','torus-factor-statement','For $A=',r'Neither \(S^{12}\)',
 symbol_pairs(local,[('A',r'A_{\rm tor}')]),
 'A_tor is the same torus factor, either (R/Z)^2 or R/Z, in the cone projection. The identity map on this chosen torus and its inverse preserve [r,z,a]↦a and the entire cone relation.')
local=block('039U');local=local[local.index(r'With \(m=m_j\)'):local.index('The simultaneous-root model')]
change('039U','local-rings',r'With \(m=m_j\)','The simultaneous-root model',
 symbol_pairs(local,[('A',r'\mathcal A_{\rm loc}'),('R',r'\mathcal R_{\rm loc}')]),
 'mathcal A_loc is exactly the displayed convergent-power-series quotient ring, and mathcal R_loc is exactly C{s1,z}. The identity substitutions and their inverses fix its monomial module basis, evaluation map to the product of branches, localization, torsion-free argument and integral closure. The torus factor and metric radius are unchanged.')
change('039U','flat-complex-operator',r'Let \(J_z\)',r'The radial and angular terms',[
 (r'J_z',r'\mathcal J_z')],
 'mathcal J_z is the same flat real-coordinate complex structure formerly J_z, namely Pi_R(z)^-1 composed with multiplication by i and Pi_R(z). Both names specify this identical endomorphism with identical square -I; the translation formula uses it unchanged. The holomorphic group family J retains J.')
change('039U','cusp-class-representative',r'Represent it by \(h_0:',r'The phase torus',[
 (r'h_0',r'h_{\rm cusp}'),(r'function \(A\)',r'function \(\alpha_{\rm htpy}\)'),(r'+uA',r'+u\alpha_{\rm htpy}')],
 'h_cusp is the same map N0→S1 representing the extended integral H1 class, and alpha_htpy is the same real lift of its difference from theta_gamma. Every restriction and the linear homotopy use these same objects. The inverse substitutions h_cusp↦h0 and alpha_htpy↦A recover the full paragraph. The later sphere diffeomorphism h0 is retained.')
local=block('039U');local=local[local.index('For a fixed fibre inclusion'):local.index('In dimension $d$')]
change('039U','based-target-rotation','For a fixed fibre inclusion','In dimension $d$',
 symbol_pairs(local,[('R',r'O_{\rm rot}')])+[(r'\mathbb O_{\rm rot}',r'\mathbb R'),('Rh_0',r'O_{\rm rot}h_0')],
 'O_rot is the same explicitly specified orthogonal rotation, with inverse transpose and the same plane matrix. The based diffeomorphism is h=O_rot h0 and its inverse h0^-1 O_rot^t, so both inverse composites are unchanged. R continues to denote metric-ball radii.')
local=block('039U');local=local[local.index('For $A='): ]
change('039U','torus-factor-proof','For $A=',None,
 symbol_pairs(local,[('A',r'A_{\rm tor}'),('p',r'p_{\rm cone}')]),
 'A_tor is the torus factor from the statement and p_cone is precisely [r,z,a]↦a on its positive cone. Their inverse name maps fix the source quotient, the displayed section and both constant projected paths. The earlier universal-cover lift p and the local rings retain their meanings.')
change('039U','radial-coefficient-statement',r'circumference',r'\smallskip',[
 ('=T+H-B+O',r'=T+H-B_{\rm rad}+O'),
 (r'In particular, \(\ell_T\to\infty\).',r'Here \(B_{\rm rad}=B\) denotes the bounded radial coefficient. In particular, \(\ell_T\to\infty\).')],
 'The necessary name B_rad=B fixes the bounded radial coefficient in the circumference expansion. The equality is stated explicitly and its inverse is the identity on that coefficient. The base B retains B; no estimate or limit is altered.')
change('039U','radial-coefficient-proof','The expansions in',r'which proves',[
 ('(2H-B)',r'(2H-B_{\rm rad})')],
 'The determinant expansion uses the same B_rad=B as the circumference statement, so D_T and every coefficient of its expansion are unchanged under the stated inverse name substitution.')

# Packet writing uses only the bounded proofs actually read above.
OUT.mkdir(parents=True,exist_ok=True)
def fields(path):
 with path.open(newline='') as f:return next(csv.reader(f,delimiter='\t'))
df=fields(ROOT/'S6_SERIES_PUBLISH_defects_III.tsv');ef=fields(ROOT/'CHECK_EVENTS.tsv')
rows=[];events=[];now=datetime.now(timezone.utc).isoformat();candidate_source=source
for tag,(old,new) in blocks.items():
 hs=[h for h in history if h['tag']==tag]; inverse=new
 for h in reversed(hs):
  assert inverse.count(h['new'])==1,(tag,h['name'])
  inverse=inverse.replace(h['new'],h['old'],1)
 assert inverse==old,tag
 for pattern in [r'\\(?:label|hypertarget)\{[^{}]+\}',r'\\(?:[Cc]ref|[Ee]qref|ref|cite)(?:\[[^]]*\])?\{[^{}]+\}']:
  assert re.findall(pattern,old)==re.findall(pattern,new),tag
 for letter in 'RCZQ':
  pattern=r'\\mathbb\s*(?:\{'+letter+r'\}|'+letter+r')'
  assert len(re.findall(pattern,old))==len(re.findall(pattern,new)),(tag,'blackboard field',letter)
 sid=re.search(r'\\label\{([^}]+)\}',old)[1]
 before=old.splitlines(True);after=new.splitlines(True)
 matcher=difflib.SequenceMatcher(a=before,b=after,autojunk=False)
 for context in range(1,10):
  groups=list(matcher.get_grouped_opcodes(context));frags=[(''.join(before[g[0][1]:g[-1][2]]),''.join(after[g[0][3]:g[-1][4]])) for g in groups]
  if all(candidate_source.count(a)==1 for a,b in frags):break
 else:raise AssertionError(tag+' ambiguous fragments')
 for i,(a,b) in enumerate(frags,1):
  candidate_source=candidate_source.replace(a,b,1)
  image_scope='Root read the complete old bounded source and each proposed difference against that source; the assigned first-quarter reader read the corresponding actual page images.' if tag in ('02LW','02LX') else 'Root read the complete old bounded source and actual page images, then each proposed difference against that source.'
  rows.append(dict(change_id=f'CLAUDE-III-C9-PDF-ROOT-{tag}-{i:03d}',type=';'.join(sorted({code for h in hs for code in h['kind'].split(';')})),statement_id=sid,old_location='Complete '+tag+' statement/proof or definition; exact fragment',old_page='candidate02 actual page images in assigned reading log',new_location='same formal owner and permanent labels',new_page='pending repaired full build and actual image reading',old_text=a,new_text=b,reason=' '.join(h['reason'] for h in hs),review_status=image_scope+' Exact reverse restores every original byte; full final image reading remains.'))
 (TMP/(tag+'_proposed.tex')).write_text(new,newline='\n')
 (OUT/(f'S6_SERIES_PUBLISH_c9_root_{tag}.diff')).write_text(''.join(difflib.unified_diff(before,after,fromfile=tag+' original',tofile=tag+' proposed')),newline='\n')
 event={k:'' for k in ef};eid=f'publish:c9:III:{tag}:root-image-source-context'
 event.update(statement_id=sid,date='2026-11-26',who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine',type='used and rechecked in this run',event_id=eid,phase='publication continuation 9',source_file=SOURCE.name,source_row='complete '+tag+' statement/proof or definition',source_event_type='used and rechecked in this run',evidence_group=eid,publish_input_file='../CLAUDE_READING_LOG_PAPER_III.md',publish_input_row='candidate02 image findings; P11/P15 and layout',date_utc=now,where='code/S6_SERIES_PUBLISH_c9_root_image_repairs.py; agents/continuation9_root_image_repairs/',outcome=f'Read the complete {len(before)}-line {tag} statement/proof or definition and its actual rendered pages, followed every specified scope, and compared all proposed exact differences. Reverse scope substitutions recover every baseline byte. Labels, references and mathematical constructions remain fixed under the recorded maps. This exposed review supplies no independent re-proof or final repaired-page credit.')
 events.append(event)
 print(tag,len(before),'lines;',len(frags),'exact fragments;',len(hs),'bounded operations; inverse source comparison passed')
for path,fs,rs in [(OUT/'S6_SERIES_PUBLISH_c9_root_image_defects.tsv',df,rows),(OUT/'S6_SERIES_PUBLISH_c9_root_image_events.tsv',ef,events)]:
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fs,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rs)
assert SOURCE.read_text()==initial
assert sum(new!=old for old,new in blocks.values())==len(blocks)
print('Staged',len(rows),'exact defects and',len(events),'exposed used-only events; canonical source unchanged.')
