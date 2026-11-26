from pathlib import Path
import datetime as dt, hashlib, json

R=Path(__file__).resolve().parents[1]
ip='agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Y6_partial_cases_v1_index.json'
def bind(p):
 b=(R/p).read_bytes();return dict(path=p,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
assert bind(ip)['sha256']=='d61f621adf7a3f9dc1f2119607b471610d36e4c1fc1a276227c7a9472510f7c7'
d=json.loads((R/ip).read_text());ev={}
def walk(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:
   b=bind(x['path']);assert b['sha256']==x['sha256']
   if 'bytes' in x:assert b['bytes']==x['bytes']
   ev[x['path']]=b
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(d)
p='records/S6_SERIES_PUBLISH_II_R13_root_research_06.json';assert not (R/p).exists()
out=dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),owner='night:P4R.13',tag='02Y6',
 reading='Root actually read the complete13328-byte rational-branch derivation in one untruncated return, the complete4825-byte reduced-horizontal inventory, and every line of the25146-byte doubled-horizontal derivation in four untruncated bounded returns. Root read the complete sealed index. Every bound file was rehashed; this hash verification gives no new reading credit for the remaining supporting files. The exact local quotient and its program/output had already been read in root research05. The R13 original target remains unopened.',
 index=bind(ip),evidence=list(ev.values()),
 mathematical_review=[
  'Rational normalization resolution: push the effective pole divisor through actual point blowdowns to P2 or F_n. A nonrational horizontal component consumes degree3 on P2 or weighted ruling degree2 on F_n. Adjunction and its elliptic normalization force the component to be smooth elliptic and disjoint from every possible remainder; every ruling fibre meets it, so the full divisor is just H0. Reverse coefficients mu-1 keep only the smooth H. R6 then leaves no normalization-resolution exceptional curve, so N is smooth rational and its whole conductor is the reduced Cartier H.',
  'At the generic conductor point exponent1 permits exactly two smooth transverse plane branches. Thus H to the elliptic normalization E is an unramified double cover. Over a point p with r branches of C, normalization has exactly2r local branches. Any pair of hypersurface branches meets in a curve, whose image in each normalization lies in its single smooth conductor germ; all image germs coincide. Hence r1 and exactly two surface branches occur. Each is R1 and S2, therefore normal and isomorphic to its smooth normalization. The exact fibre product O_Y/(f1f2) -> O_Y/(f1) plus O_Y/(f2) -> O_Y/(f1,f2), with conductor ideals(f2|S1),(f1|S2), makes the intersection the smooth reduced conductor. The coordinate map(f1,f2,z) has invertible Jacobian. The whole global conductor sequence has no finite quotient. Its H1 map is minus pullback on the elliptic double cover, an isomorphism by trace composed with pullback=2. Thus h1(O_S)=0 and chi(O_S)=1, contradicting the actual standing P4.12 values.',
  'Positive-genus reduced horizontal divisor: adjunction and Riemann--Hurwitz force genus1 and either one smooth elliptic bisection or two disjoint sections, with no vertical remainder. Reverse blowups and R6 give a smooth normalization. The generic node makes rank drop finite; the already established P4.15 gives minimality, no rank drop, smooth disjoint elliptic image curves and e(S)=0. The exact local two-factor conductor algebra then gives node product coordinates. The actual component map list is exhaustive: one bisection double covers one image; two sections over one image each map with degree1; or two sections each double cover a different image. The last configuration remains open globally, despite the proved local quotient realization.',
  'Doubled horizontal branch: D=2H+V on the resolved ruled surface, with V a full effective vertical divisor and all rational trees retained. The ruling and section give an explicit inverse to pi1(A)->pi1(T). The actual conductor pushout gives pi1(S)=pi1(C). Its normalized-curve graph has fundamental group a free product of all curve groups and a free group. Virtual abelianness and the present elliptic factor exclude every additional positive-genus factor and every graph cycle by a quotient onto F2. Thus exactly one elliptic-normalized component C0 occurs, the other components are rational, and C0 is unibranch.',
  'The primary conductor I0 along C0 retains the full quotient Q=I0/I. Rational canonical trace identifies sigma_*O_T(-D) with the actual conductor ideal; finite conductor duality injects O_Csch into rho_*O_D. Its Q-image vanishes on the entire generic2H and hence everywhere on that pure scheme. It therefore lies in O_V(-2H)=omega_V tensor torsion-line inverse. The torsion line pulls back through the ruling and is trivial on each full vertical scheme. Rr_*O_T=O on the base, the whole-fibre divisor sequence, induction on nF and quotient to V give H1(O_V)=0 even with multiplicities. Hence H0(Q)=0 and g-1<=chi(O_Y/I0).',
  'Exponent2 on every sheet over C0 leaves precisely the cusp, tacnode and ordinary triple cases with d1,2,3. The residue/conductor branch formula proves the exhaustive list. In A2 purity gives I0=P0, and in D4 it gives I0=P0^(2) using the actual three-branch second-order values. The elliptic normalization sequence or the already proved X3 symbolic-square inequality gives chi<=0 with equality only for smooth C0. Thus g1 and C0 smooth in both cases.',
  'For A3 the exact primary module J=P0/I0 injects into n_*(K/L) under the projected differential. Its normalized lattice colengths give chi(O_Y/I0)=-sum delta-sum(d/2+b-r)-sum q. At a nonplanar branch E_con lies in t^mu K, alpha+b>=2mu and d>=alpha, giving d/2+b>=mu>r. At a planar branch P0=(z,H), ordinary and symbolic squares agree; the Hessian in the lattice<dz,t^alpha u> gives d/2+b>=alpha>=mu>r in both primitive-line coordinate cases. Smooth points have nonnegative terms. The comparison forces genus1, smooth C0 and a nowhere-vanishing rank-one Hessian. No whole-curve uniform-type assumption was used.',
  'The product maps now remove every other image component: A3 uses the already proved R15 at each point with the actual Hessian; A2 uses the degree-zero quadratic-line and intrinsic kernel cubic, then F_x=0, X=u sqrt(A),Y=y B^(1/3), giving X2+Y3; D4 uses the nowhere-zero discriminant in(det K)^6 tensor M^4, Weierstrass roots v_i, q_i=y-xv_i, and X=a q1,Y=-b q2, giving a unit times XY(X-Y). Each entire local critical locus is the one smooth axis. Since C is connected, C=C0. The explicit normalizations are smooth; finite normalization and the elliptic target exclude every vertical rational component, so D=2H. A possible rational(-1)-curve has(K+2H).E=-1+2H.E, impossible. Thus N is minimal elliptic ruled and e(S)=e(N)-e(H)+e(C0)=0. This argument does not assume Euler zero before proving it.'
 ],
 complete_whole_target_derivation=False,whole_target_freeze=False,whole_target_original_comparison=False,
 unresolved='Compact realization or exclusion of the positive-genus reduced-horizontal configuration with two different elliptic image components; C is constructing exact global period and affine gluing maps, and A is independently auditing them.',
 new_primary_reading_credit=0,canonical_source_changes=0,events_added=0,required_rows_completed=0,
 next_requirement='Finish the whole-domain derivation or exact counterexample before releasing and comparing the R13 original proof; keep all partial results and chronology intact.')
(R/p).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(record=bind(p),bound_files=len(ev),whole_R13_open=True)))
