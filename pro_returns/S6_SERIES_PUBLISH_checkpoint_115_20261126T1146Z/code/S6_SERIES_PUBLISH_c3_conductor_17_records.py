#!/usr/bin/env python3
"""Record the fully compared weighted-cycle consolidation; no central writes."""
from pathlib import Path
from datetime import datetime,timezone
import csv,re,hashlib,importlib.util
code=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('conductor17_source',code/'S6_SERIES_PUBLISH_c3_conductor_17.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
root,out,stem=c.root,c.out,c.stem
original,fragments=c.original,c.fragments
for key,value in fragments.items():assert (out/(stem+'_'+key+'.tex')).read_text()==value,key
assert (out/(stem+'_replacement.tex')).read_text()==c.main_new
assert (out/(stem+'_input.tex')).read_text()==c.main_old
def tsv(suffix,fields,rows):
 with (out/(stem+suffix)).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def statement(s):return s[:s.index(r'\begin{proof}')]
def proof(s):return s[s.index(r'\begin{proof}'):]
def part(s,first,last=None):
 a=s.index(first);return s[a:s.index(last,a) if last else len(s)]
def para(s,pos):
 a=s.rfind('\n\n',0,pos)+2;b=s.find('\n\n',pos);return s[a:b if b>=0 else len(s)]
definition,roots,affine,periods,examples=[fragments[k] for k in ('P355','P356','P357','P358','P359')]
general,suspension=fragments['UN59_replacement'],fragments['UN56_replacement']
destinations={
 52:[definition+roots,roots,roots+general,affine+suspension,suspension,roots+suspension,examples],
 56:[definition+roots,roots,roots+affine+suspension,suspension],
 59:[definition+roots+general,affine,periods,general+roots,periods+general,examples],
}
segments={}
for n,s in original.items():
 matches=list(re.finditer(r'\\par\\medskip\\noindent\\textbf\{([^}]+)\}',s))
 assert len(matches)==len(destinations[n])
 segments[n]=[(m.start(),matches[i+1].start() if i+1<len(matches) else len(s),m.group(1),destinations[n][i]) for i,m in enumerate(matches)]
def route(n,pos):
 for a,b,title,dest in segments[n]:
  if a<=pos<b:return title,dest
 return 'Complete statement and exact scope',statement(definition)+statement(roots)+statement(general)+statement(suspension)
rows=[]
def log(kind,owner,old,new,reason,oldwhere='',newwhere=''):
 rows.append(dict(change_id=f'II-C3-WEIGHTED17-{len(rows)+1:04d}',type=kind,statement_id=owner,
  old_location=oldwhere or owner+' complete original source',old_page='Exact source span supplied; old PDF page omitted',
  new_location=newwhere or 'P355–P359 and the weighted-cycle criterion/suspension subsections',new_page='Pending final integrated PDF',
  old_text=old,new_text=new,reason=reason,
  review_status='Complete original and receiving proofs read and compared; exposed editorial rereading, including the explicitly proved P333/UN48 extensions. No independent proof or mathematical-program execution credit. Final PDF open.'))
for n in (52,56,59):
 owner=f'cdp:st:C.2.UN.{n}'
 receiver=general if n==59 else suspension
 log('D12',owner,statement(original[n]),statement(receiver)+statement(roots),
  'One general weighted criterion owns the full local and conjugate compact construction. The merged UN52/56 keeps both permanent identities and the stronger algebraic-dimension-zero elliptic-suspension construction. Every original hypothesis, finite map, multiplicity, inertia and Euler conclusion is preserved by the explicit specializations in comparison.md.')
 for a,b,title,dest in segments[n]:
  log('D12',owner,original[n][a:b],dest,
   'Transfer this complete proof block to the single receiving owner(s), with every local root, lattice, finite action, period, properness and inverse map compared explicitly in owner_transfers.tsv and comparison.md. This records full old/new proof reading, without independent credit.',oldwhere=owner+': '+title)
log('D13','def:II:weighted-normal-cycle',original[52][segments[52][0][0]:segments[52][0][1]],definition,
 'The full weighted normal lines, sections, leading coefficients and boundary line maps were defined inside the criterion proof. A numbered definition now precedes their uses and includes the canonical-divisor-section construction from a given weighted degeneration.')
log('D13','ex:II:weighted-cycle-examples',original[52][segments[52][-1][0]:]+original[59][segments[59][-1][0]:],examples,
 'Move the three complete explicit quotient families from proof tails to one numbered example. Preserve every component action, invariant ring, axis power map, compact suspension comparison and finite linear action; add the explicit elliptic lattices supporting orders2,3,4,6.')
log('D14','def:II:weighted-normal-cycle',c.main_old+c.original[56]+c.original[59],c.main_new,
 'Order seven actual units as weighted data, root/inertia maps, finite affine data, equivariant periods, general criterion, algebraic-dimension-zero suspension, examples. Preserve weighted-hopf-cycles as the first-unit alias. The general criterion precedes its specialization; no proof depends on the later illustrative example.')
log('D14','lem:II:moving-marked-cycle',c.p333+c.un48,fragments['P333_replacement']+fragments['UN48_replacement'],
 'Place the full compressed monomial resolution and coframe comparison at the earlier P333 owner. UN48 applies h_i=d,t=s,(a_j,b_j)=(u_j,v_j), removing a forward construction premise. The complete h_i=1 theorem/proof stays unchanged. The later weighted families apply only the explicitly constructed marked neighbourhoods.',newwhere='subsec:II:moving-marked-cycles; subsec:II:cycle-elliptic-suspensions')
log('D12','lem:II:moving-marked-cycle',c.p333+c.un48oldpart,fragments['P333_replacement'],
 'Explicitly proved extension, not wording-only work: compressed xy=t^h, same four radii with delta^h<r0^2, normality, all monomial charts/transitions and proper graph closure, h-1 ruled components, full reduced resolved fibre, unchanged punctured fibre and h-fold normal periods. The existing smooth h=1 clauses and proof are retained in full.')
log('D12','cdp:st:C.2.UN.48',c.un48,fragments['UN48_replacement'],
 'Full original/receiving comparison. The monomial resolution is now the exact earlier P333 application. The existing nodal pencil/Tate/suspension proof is explicitly stated for every0<|q0|<1,a in C* minus1,d>=1; its I_d, section coordinate, all periods, connected torus fibres, compact smooth total space and all-support Euler-zero conclusions are proved by that same construction. The original marked-cycle assertion remains.')
log('D14','subsec:II:hopf-tree-reductions',original[56],c.remote_rows[0]['new_text'],
 'After moving the entire UN56 criterion/proof, introduce the actual following-unit heading before untouched UN58. UN54 remains under hopf-support-tree-remainder. Both full publication units and the enclosing original sec10 stay open.',newwhere='subsec:II:hopf-tree-reductions')

new_displays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',c.new_all,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
aliases={x['old_tag']:x for x in c.alias_maps}
def payload(s):
 s=re.sub(r'\\SsixEquationAliases\{(?:\s*\\label\{[^}]+\})+\s*\}','',s)
 s=re.sub(r'\\tag\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}|\\label\{[^}]+\}','',s)
 for x in (r'\[',r'\]',r'\begin{equation}',r'\end{equation}'):s=s.replace(x,'')
 return re.sub(r'\s+','',s)
def inverse_notation(tag,s):
 if tag in ('C.WH.1','C.WH.2','C.WH.3','C.WM.2','C.WM.4'):s=s.replace(r'\mathcal N',r'\mathcal L')
 if tag in ('C.WH.1','C.WH.2','C.WH.6'):s=s.replace('V_i','H_i').replace('V_{i+1}','H_{i+1}')
 if tag=='C.WM.1':s=s.replace(r'\mathcal L_i','L_i')
 if tag in ('C.WM.3','C.WM.6'):s=s.replace(r'\mathcal L',r'L')
 if tag.startswith('C.EW.'):s=s.replace(r'\mathbf b','b')
 if tag=='C.WH.10':s=s.replace('d=Nq',r'\delta=Nq')
 return s
formula_rows=[]
for tag,old in c.equations.items():
 label=c.established[tag];new=new_displays[label]
 if tag in aliases:
  explanation=aliases[tag]['map'];result='Exact alias under the stated specialization/map; surrounding stated hypotheses retained'
 else:
  assert payload(old)==payload(inverse_notation(tag,new)),tag
  explanation='Identical mathematical payload, with section numbering and the same established target.'
  if tag in ('C.WH.1','C.WH.2','C.WH.3','C.WM.2','C.WM.4'):explanation+=' The weighted normal line is now mathcal N; its identity map preserves every section and power.'
  if tag in ('C.WH.1','C.WH.2','C.WH.6'):explanation+=' V_i denotes the same component, equal to H_i on the original Hopf domain; ruled instances are the already proved UN56/59 scope.'
  if tag in ('C.WM.1','C.WM.3','C.WM.6'):explanation+=' The degree-zero ruling line L is mathcal L, with exactly the same base and power map.'
  if tag.startswith('C.EW.') and r'\mathbf b' in new:explanation+=' Edge constants b_j are bold b_j, the same common vectors as P333; their sum remains b.'
  if tag=='C.WH.10':explanation+=' Old primitive divisor delta is d, so d=Nq is unchanged; q is the suspension index.'
  result='Formula payload identical under the explicit notation identity'
 formula_rows.append(dict(old_tag=tag,target_label=label,result=result,map=explanation))
 log('D19',label,old,new,'Use section equation numbering while preserving the old permanent target and exact prepared D19 label. '+explanation)

for n,s in original.items():
 owner=f'cdp:st:C.2.UN.{n}'
 for m in re.finditer(r'(?<![:{])\bC\.[A-Z]+\.\d+',s):
  tag=m.group();assert tag in c.established,tag;title,dest=route(n,m.start());label=c.established[tag]
  log('D04',owner,para(s,m.start()),new_displays.get(label,dest),
   f'Printed internal equation scheme {tag} now resolves through {label}, or its exact formula alias/application. Every underlying map and target is retained.',oldwhere=f'{owner} line {s[:m.start()].count(chr(10))+1}, character {m.start()}: {title}')
 for m in re.finditer(r'\b(actual|genuine|retain(?:ed|s|ing)?|supplied|specified|saved)\b',s,re.I):
  title,dest=route(n,m.start());log('D08',owner,para(s,m.start()),dest,
   f'Replace this process/assurance use of "{m.group()}" by the mathematical component, line, lattice or map. The complete receiving block proves the same analytic or finite quotient comparison.',oldwhere=f'{owner} line {s[:m.start()].count(chr(10))+1}, character {m.start()}: {title}')
 seen=set()
 for m in re.finditer(r'(?i)\b(?:rather than|not merely|not just|No assertion|For clarity|does not identify|not a formal|without replacing|without any Hopf assumption)\b',s):
  old=para(s,m.start())
  if old in seen:continue
  seen.add(old);title,dest=route(n,m.start());log('D02',owner,old,dest,
   'Remove the defensive contrast. Preserve its mathematical content positively in the full domain and exact map: local flat axis charts, finite normalization, ruled frame, chosen normal constants, or descended translation torsor.',oldwhere=f'{owner} line {s[:m.start()].count(chr(10))+1}: {title}')
 for m in re.finditer(r'\\path\{([^}]+)\}',s):
  title,dest=route(n,m.start());log('D09',owner,para(s,m.start()),dest,
   'Remove the body file path, saved-output language and finite check counts. Every normalization, inertia, resolution, equivariance, determinant and infinity calculation is proved for the full stated domain. Programs appendix addition162 already gives the exact pinned plain path and computation scope for '+m.group(1)+'. No program execution is claimed.',newwhere='Programs appendix addition162; complete receiving mathematics at P355–P359')

log('D11','cdp:st:C.2.UN.52',para(original[52],original[52].index('it does not identify')),statement(suspension)+statement(general),
 'State the compact-realization scope once and positively: every central component/gluing/multiplicity is preserved and normal-product constants are chosen. P333 gives an exact comparison only on the constructed marked neighbourhoods; no repeated negative scope disclaimer remains.')
log('D17','lem:II:weighted-cycle-affine-data',original[59][segments[59][1][0]:segments[59][1][1]],affine,
 'Freshly reopened the complete Khaled arXiv:2310.05265v2 Theorem2.1 and Remark2.2, printed p5. For two-axis diagonal lifts use IIc, III(Az+Cw^r,Bw) with C=0, and IV GL2 with diagonal marked subgroup. Keep the exact Hartogs/inverse/derivative map identifying the source contraction with the target deck element, and keep the separate ruled affine proof. The source recalls the centralizer statement; no unpublished source proof is claimed.')
log('D18','cdp:st:C.2.UN.56',para(original[52],original[52].index('holomorphic Cousin theorem')),part(suspension,'The coherent sheaf',r'Use this isomorphism'),
 'Replace the unlocated Cousin-theorem reference by freshly opened Cartan1957 section2, fundamental theorem B, printed p80 (PDF5), applied to the coherent sheaf O^2 on the Stein punctured disc. Keep the explicit local-system cellular H2=0 argument and the complete torsor cocycle/section map. Bibliography already contains this primary source; source-wide bibliography remains open.')
log('D18','cdp:st:C.2.UN.56',original[52][segments[52][3][0]:segments[52][3][1]],part(suspension,'Projection along',r'The finite linear part'),
 'Use freshly reopened Abasheva–Deev arXiv:2303.10764v1 section2.2.6 p5 for the nonresonant two-axis curve list. The secondary case uses the exact earlier P327 central cover and its algebraic-dimension equality. P248 is not assigned the stronger axis-list conclusion absent from its statement.')
for tag in ('C.WH.1','C.WH.2','C.WH.3','C.WH.6','C.WH.10','C.WM.1','C.WM.2','C.WM.3','C.WM.4','C.WM.6','C.EW.2','C.EW.3','C.EW.4','C.EW.12','C.EW.13','C.EW.21'):
 log('D20',c.established[tag],c.equations[tag],new_displays[c.established[tag]],
  next(r['map'] for r in formula_rows if r['old_tag']==tag)+' Weighted normal mathcal N and degree-zero ruling mathcal L are defined separately at P355; all identifications are the identity on the original line or common period vector.')
log('D20','def:II:weighted-normal-cycle',original[52][segments[52][0][0]:segments[52][0][1]],definition+roots,
 'Fix x as the ambient normal to V_i and y as the normal to V_(i+1), so t=x^(m_i)y^(m_(i+1)). In the original local core paragraph the unlabelled two coordinates were listed in the opposite order; exchanging x and y there gives the identical product and keeps the labelled WH4/EW1 finite maps unchanged.')
log('D22','cdp:st:C.2.UN.56',original[52][segments[52][4][0]:segments[52][4][1]],part(suspension,'The full affine relation',r'Write $q_i$')+part(suspension,'Use the lattice-coordinate',r'Put $t=s^N$'),
 'Prove the exact choice q=div(u)/N from (R-I)b-u/N in Lambda and R=I. State resolved root length sum h_j and compare it through the explicit monomial resolution and normalized-root projection. The coframe period becomes log(t)(u/N)/(2pi i). Apply UN48 with its integer d equal to this q, preserving all q0,a, section and full-fibre maps.')
log('D22','lem:II:finite-equivariant-periods',original[59][segments[59][2][0]:segments[59][2][1]],periods,
 'P331 is applied at z=s^k. Its determinant is affine in the logarithmic coefficient c and holds for all positive integer c, hence the polynomial identity holds at c=d/k. log z=k log s gives EW11 in the same real coordinate order. Actual monodromy is d V_s p, integral in the unchanged lattice.')
log('D22','ex:II:weighted-cycle-examples',original[59][segments[59][-1][0]:],examples,
 'Supply the explicit elliptic lattices for every finite order: any E with -1 for2; square lattice with i for4; hexagonal lattice with exp(2pi i/3) or exp(pi i/3) for3 or6. Preserve every EW21 action, integer sum, quotient component and gluing map.')
log('D23','lem:II:weighted-cycle-roots',c.equations['C.EW.1']+c.equations['C.EW.17']+c.equations['C.WH.9'],roots+affine,
 'Every receiving equation has one aggregated SsixEquationAliases hook at most and no blank paragraph. All old targets survive once; acute accents in etale are retained. The final integrated rendering remains open.')

fields=next(csv.reader((root/'S6_SERIES_PUBLISH_defects_II.tsv').open(),delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],[dict(old_tag=k,target_label=c.established[k],statement_id='Receiving owner and exact map in formula_comparisons.tsv') for k in c.equations])
tsv('_formula_comparisons.tsv',['old_tag','target_label','result','map'],formula_rows)

maps=[
 ('UN52/UN56/UN59 statements','P355–P358, general UN59 and merged UN52/56','All local criteria and both complete compact realization scopes.','General domain keeps every diagonal primary/secondary Hopf and degree-zero ruled vertex. UN52 is the all-Hopf a=0 specialization; UN56 permits ruled vertices and at least one a=0 Hopf. Same components, sections, elliptic maps, full mi and chosen normal constants. Both statement tags remain on the merged suspension criterion.'),
 ('UN52 weighted-data definition and plumbing; UN56 ruled lines; UN59 root input','P355/P356','Canonical weighted lines, sections, flat axis charts and proper smooth weighted plumbing.','N_i=O_Y(V_i)|Vi; divide f by its canonical divisor section to get sigma_i. WH2 identifies the same two restricted normal lines. Divide the transferred mth-power connection by m, match the leading coefficient by an mth root, and identify the full functions. On ruled R, N=O(d0 C+) tensor pi*A0 with deg A0=0. Four radii and weighted normal bounds give the same closed-graph and finite compact cover.'),
 ('UN52 normalized root; UN56 ruled finite cover; UN59 EW1','P356','Every component map, axis ramification, graph and inertia.','Core xi=s^(N/mi)/v. Edge a=gA,b=gB,N=gABh gives g branches uv=s^h,x=u^B,y=v^A. Finite/one-to-one/normal proves normalization. Hopf angular least multiples give coordinate powers and free diagonal finite quotient; ruled Lambda-prime projection gives E-prime->E, kernel z->z^q, (L-prime)^q=pi*L and the homogeneous power map. Connected inverse axes and sheet counts give r, all degrees, K,Ii products/intersections.'),
 ('UN48 full monomial resolution','Earlier P333; UN48 exact application','Proper full reduced resolution and compressed coframe family.','h_i=d,t=s,a_j=u_j,b_j=v_j gives x=u_j^(j+1)v_j^j,y=u_j^(d-j-1)v_j^(d-j),s=u_jv_j. Adjacent a_next=1/b,b_next=t b. Proper graph closure of[x:t^k] has the displayed ratio coordinates; h=1 is identity. Flat line transitions give h-1 degree-zero ruled components; resolution is an isomorphism off0 and repeats the same normal h times.'),
 ('UN52/56/59 integral test and given-degeneration comparison','P356/general UN59','Connected graph iff connected nearby fibre; injected semidirect lattice; exact necessity.','P333 applies to the resolved root cycle. Reduced central fibre makes its proper Stein-factor degree1 on a connected graph. The fixed s-fibre maps isomorphically to the t=s^N fibre. Given canonical divisor sections and unit roots give identical core/collar maps; P326 applies to the full reduced resolved SNC support. Abelian torus pi1 forces M=I; the common closed coframe gives the converse.'),
 ('UN59 finite-affine proof; UN52 translation-domain proof','P357 and merged UN52/56','Full finite action, primitive normal divisor and a=0 identity linear part.','Khaled IIc/III/IV gives the two-axis diagonal lifts after exact Hartogs/inverse/derivative comparison; ruled maps descend affinely with constant logarithmic derivative. EW3 is the full overlap/order identity. Resolve compressed edges and use UN57 height with h repetitions, yielding u=dp,ell(iu)!=0,Rp=p. Extend p to a lattice basis. Finite integral two-lattice trace gives orders1,2,3,4,6 and vertex stabilizers give R^r=I. In the a=0 domain a torsion L would give a compact curve via an explicit trivializing isogeny, so beta*L=L forces beta=1 and R=I.'),
 ('UN59 punctured periods and infinity frame','P358','Full finite-equivariant proper torus family, all translations and conjugate infinity data.','P331 map at z=s^k and affine determinant coefficient c=d/k gives EW11. tau_j(s)=V_(zeta s)tau_j is in the target frame. Transport rational correction h n/N and the entire order sum to get V_s mu. EW6 gives the last-period difference. Subtract theta_j to obtain one finite action on the quotient. Divide by s^k: W_w=J conjugate+w^k, Rinf=rho^-1 R=J conjugate(R)J^-1, tauinf=W_(zeta^-1 w)tau; all overlaps/order equations transform identically.'),
 ('UN52 and UN59 quotient smoothness','P356 final clause','Every moving compressed quotient is smooth with the same full mi.','Pointwise stabilizer has orderhAB. Bezout c0 A+d0 B=1 gives characters(zeta_B^c0,zeta_A^d0,zeta_hAB). Reynolds u=uU,v=vV and invariant axis coordinate preserve branch divisors; invariant UV can be divided out while keeping s and uv=s^h. First order-h invariants give C{u,v}; residual independent B,A powers give C{x,y},t=x^a y^b. Remaining axis map etale, generic inertia normal reflection, off0 base action free.'),
 ('UN59 zero/infinity fillings and compact gluing','General UN59','Exact compact realization of the original weighted support and its conjugate.','P333 receives the same V_s lattice, Hopf frames EW16, separate ruled frame, h_j and bold b_j(s); full period equals EW10. R P_j=P_sigma(zeta s) extends the entire finite action, and EW13/15 makes the punctured coframe isomorphism equivariant. P356 gives exact weighted quotient charts. At infinity normals are -W_w n_j and frames J conjugate(P_j), so every component, gluing and finite character is the conjugate. Closed smaller filling discs plus a closed middle annulus prove compactness; quotient fibre is one of the N root fibres.'),
 ('UN52/UN56 compact elliptic-suspension proof','Merged UN52/56 and UN48 parameter clause','Stronger compact suspension realization with all full weighted maps and Euler-zero supports.','u/N integral implies d=Nq. Resolved length=sum h_j via h_j-1 inserted vertices; resolution and root projection carry log(s)u to log(t)u/N. Choose UN48(q0,a,d_old=q). Orbit normal adjustments give sum bold b=0; rational left-kernel relations and a fixed right inverse transport the exact affine solution. Same compressed finite action and invariant rings give smooth quotient. R=I descends the O^2 coframe. Cartan B plus circle local-coefficient H2=0 kills the complete torsor cocycle, giving the full punctured-family isomorphism for compact annulus replacement.'),
 ('UN52 unequal examples and UN59 finite-linear examples','P359','Same compact families and all explicit quotient maps.','For(1,n), anti-diagonal and extra scalar actions give t=x^nY, power map(Z^n,W^n),axis z^-n and the same q0=alpha beta,a=beta^n with suspension index1. Triangle actions preserve HG16, give the same three primary pairs and inversion/id/inversion maps. EW21 gives all finite orders2,3,4,6; exact lattice choices,endpoint -2p,Nth sums and inverse-generator gluing rho^-1 are retained.'),
]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],[dict(zip(['old_owner','new_owner','conclusion','map'],r)) for r in maps])
deps=[
 ('P333 compressed clause','P329/P326 and the transferred full monomial resolution','Only constructed marked neighbourhoods; same flat normal lines and integer moving lattice. Every existing smooth h=1 clause stays.','Earlier than UN41/UN48 and every weighted consumer; no weighted-theorem input.'),
 ('UN48 parameter clause','P333, UN41 nodal pencil/Tate, Schutt–Shioda exact prior loci','h_i=d,t=s,(a_j,b_j)=(u_j,v_j); arbitrary0<|q0|<1,a!=0,1,d>=1; complete suspension proof unchanged.','Earlier than weighted criteria; no circular root-cycle premise.'),
 ('P355/P356','P329/P333/P326','Canonical normal data; full weighted chart maps; given-degeneration application after normalized root/resolution is full-reduced SNC.','Backward; all component/axis/inertia maps explicit.'),
 ('P357','P356,P329,P333,UN57 and Khaled v2 Theorem2.1 p5','Resolve each compressed edge and repeat its normal h times; exact marked automorphism lift; same finite lattice group.','Backward; no P248 axis-list overstatement.'),
 ('P358','P357/P331','z=s^k,c=d/k polynomial determinant substitution; actual monodromy d V_s p integral.','Backward; target/infinity frames and full affine order explicit.'),
 ('General UN59','P355–P358/P333','Same complete marked weighted input, finite root data and two conjugate fillings.','Local order complete.'),
 ('Merged UN52/56','General UN59/P356/P357/UN48/P333/P327 and exact Cartan/Abasheva–Deev loci','Same support with at least one a=0 Hopf, all Hopf a=0; q=d/N parameter map and full torsor trivialization.','Backward proof dependencies. P359 reference is a following illustration, not a proof premise.'),
 ('P359','Merged UN52/56/general UN59/UN57/P332/UN48','Same explicit component and axis quotient maps, including d/N=1 in the two Hopf examples.','Backward; every finite order has a concrete elliptic lattice.'),
 ('UN54','subsec:II:hopf-support-tree-remainder','Current admitted P337 receiver left intact.','Open complete publication unit; no full-unit closure claimed.'),
 ('UN58/60–63','subsec:II:hopf-tree-reductions','Current admitted P330 receiver at UN61 left intact; following trees untouched.','Open; original sec10 and whole-paper structure remain open.'),
]
tsv('_dependencies.tsv',['consumer','input','map','status'],[dict(zip(['consumer','input','map','status'],r)) for r in deps])

now=datetime.now(timezone.utc).isoformat()
event_defs=[
 ('cdp:st:C.2.UN.52','UN52','_UN56_replacement.tex','Read the entire original UN52 statement and seven proof blocks, then every receiving owner and merged criterion. Compared weighted normal data, full smooth plumbing, Hopf root normalization/connected axes, semidirect lattice, common strict count and inertia, a=0 translation proof, d/N integral period, exact finite holomorphic transport, all invariant rings, full torsor and compact suspension, both unequal examples. All 18 WH targets remain with explicit aliases.'),
 ('cdp:st:C.2.UN.56','UN56','_UN56_replacement.tex','Read the entire original mixed-cycle statement and four proof blocks and complete merged receiver. Compared ruled normal degree, local flat/global line maps, connected finite lattice cover, base map and q-power line, homogeneous finite morphism, ramification/index/base degree, root graph, non-torsion ruling line and two-Hopf count, independent ruled frame, full finite action and compact suspension. Same marked surfaces and all multiplicities remain.'),
 ('cdp:st:C.2.UN.59','UN59','_UN59_replacement.tex','Read the entire original general weighted-cycle statement and six proof blocks and full receiving general criterion plus owners. Compared all-a/all-ruled domain, finite root action with R and every affine constant, full period determinant, target-frame transport/order, zero filling/invariant quotient, infinity conjugation, compact Hausdorff gluing and finite examples. All 21 EW targets and the full two-conjugate-support realization remain.'),
 ('def:II:weighted-normal-cycle','P355','_P355.tex','Read the complete receiving definition/proof against the three complete original scopes. Compared identical weighted normal line/section and every leading coefficient, canonical divisor sections and both edge line maps. V_i=H_i on the original Hopf domain; ruling mathcal L and normal mathcal N have exact identity maps. The unlabelled local x,y order is explicitly reconciled with the labelled normalization equation.'),
 ('lem:II:weighted-cycle-roots','P356','_P356.tex','Read complete receiving statement/proof. Verified connection division, exact section gauge, global ruled line, weighted proper compact cover, xi=s^(N/mi)/v, finite normalization and connected axes, all Hopf and ruled power maps, lattice index, Stein connectedness, same given-degeneration collars, root graph rotation and every inertia count. Read the full moving quotient character/averaging proof and invariant ring, including preservation of s and the product uv=s^h.'),
 ('lem:II:weighted-cycle-affine-data','P357','_P357.tex','Read complete receiving statement/proof against the full original finite-action blocks. Freshly reopened Khaled v2 full Theorem2.1/Remark2.2 p5; exact Hartogs/inverse/derivative identifies the deck contraction, then IIc/III/IV gives the marked diagonal lift. Compared ruled affine map, full EW3/order, h-fold resolved height, primitive p, integral finite orders, R^r, orbit constants and descent relation.'),
 ('lem:II:finite-equivariant-periods','P358','_P358.tex','Read complete original period/infinity blocks and full receiving lemma. Compared every EW8–15/18–20 formula. Exact P331 substitution z=s^k,c=d/k uses the proved polynomial identity; actual monodromy stays integral. Verified target-frame tau, rational overlap correction, full Nth translation, accumulated-edge map, last period, inverse infinity frame and conjugated finite action. No program was executed.'),
 ('ex:II:weighted-cycle-examples','P359','_P359.tex','Read complete original unequal/finite-linear example blocks and full receiving example. Compared both neck equivariances, anti-diagonal scalar quotient, invariant coordinates/multiplicities, axis power isomorphisms, q0/a and root degree index-one compact comparison, all triangle maps/primary pairs and the exact EW21 endpoint/order sums. Added explicit elliptic lattices for2,3,4,6 and kept the inverse-generator gluing rho^-1.'),
 ('lem:II:moving-marked-cycle','P333','_P333_replacement.tex','Read complete current original P333 and full receiving statement/proof, plus the entire monomial resolution proof transferred from UN48. This is a proved compressed-neck extension, not solely text editing: same four radii and delta^h bound, normality, all charts/transitions, proper graph closure and h=1 identity, h-1 degree-zero ruled components, full reduced fibre and exact h-fold coframe period on the same punctured family. Every earlier smooth h=1 clause and proof remains unchanged.'),
 ('cdp:st:C.2.UN.48','UN48','_UN48_replacement.tex','Read complete current original and receiving UN48 statement/proof. Compared the whole nodal cubic/point, transverse pencil, base change, resolution, translation extension, exact Tate parameter, suspension, four periods and inverse exponential map, moving component/affine maps, compact annulus replacement and all-support Euler proof. P333 receives h=d,t=s,a_j=u_j,b_j=v_j. The newly stated arbitrary q0,a,d clause is proved by the same complete pencil/Tate/suspension construction; all original marked-cycle conclusions remain.'),
]
events=[]
for owner,key,suffix,result in event_defs:
 events.append(dict(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',
  type='used and rechecked in this run',outcome=result+' Exposed reading and old/new comparison only; no independent proof or mathematical-program execution credit. Final bounded notation, source-locus, h=1 and resolved-length/period-map refinements were reread. No refined P4R.13/P4.40 use occurs. Final integrated pages remain open.',
  event_id='publish:c3:conductor17:'+key,phase='publication full proof comparison and explicitly proved owner extension',source_file='agents/continuation3_conductor/'+stem+suffix,source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor17:weighted-cycles',publish_input_file='',publish_input_row='',date_utc=now,where='Complete original/receiving weighted units and bounded full P333/UN48 owners'))
tsv('_CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
units=[
 ('subsec:II:weighted-cycle-data','Weighted normal data on marked cycles; preserves weighted-hopf-cycles identity'),
 ('subsec:II:weighted-cycle-roots','Root covers and inertia of weighted cycles'),
 ('subsec:II:weighted-cycle-affine-data','Finite affine data on root cycles'),
 ('subsec:II:finite-equivariant-periods','Finite-equivariant logarithmic periods'),
 ('subsec:II:weighted-cycle-criterion','The weighted cycle criterion and compact realization'),
 ('subsec:II:weighted-cycle-suspensions','Weighted cycles of algebraic dimension zero'),
 ('subsec:II:weighted-cycle-examples','Explicit weighted cycles and finite linear actions'),
 ('subsec:II:moving-marked-cycles','Proper normal products and moving lattices; full compressed extension'),
 ('subsec:II:cycle-elliptic-suspensions','Elliptic suspensions realizing marked cycles; exact arbitrary-parameter clause'),
 ('subsec:II:hopf-support-tree-remainder','Hopf support graphs; current complete UN54 unit remains open'),
 ('subsec:II:hopf-tree-reductions','Canonical and period reductions on Hopf trees; UN58/60–63 remain open'),
]
statuses=[];open_units={x[0] for x in units[-2:]}
for unit,title in units:
 for test in [f'D{i:02}' for i in range(1,26)]+['structure']:
  state='done';reason='Complete original/receiving proof comparison across all25 classes; every observed local instance is repaired and recorded. Exact owner/formula maps preserve scope.'
  if test in ('D10','D16'):reason='Prior done status preserved; every statement label and permanent target remains, and all new owners have mathematical titles.'
  elif unit in open_units:state='open';reason='Following full publication unit remains open. UN54 current P337 receiver and UN61 current P330 application are unchanged; no completed full-unit review is claimed.'
  elif test in ('D14','structure'):reason='Local dependency order complete: earlier P333 resolution and UN48 parameter construction precede seven weighted units. The illustrative example is not a proof premise. Original sec10 remainder and final whole-paper structure remain open.'
  elif test=='D18':state='open';reason='Exact primary versions/loci freshly opened and applied; source-wide bibliography and final consistency remain a separate gate.'
  elif test=='D23':state='open';reason='Source environments, accents, all preserved targets and single alias hooks checked. Final integrated PDF pages remain open.'
  elif test=='D24':state='open';reason='Body owners and local headings are complete; final outline/results-list reconciliation remains with root.'
  elif test=='D19':reason='All48 inherited formula identities use section numbering and exact established labels; five old formulas use the proved common-owner aliases. Two new P333 formula labels are explicit.'
  elif test=='D25':reason='Every original/receiving inference and coordinate map was compared; no false original intermediate assertion was found in this package. The P333 extension and UN48 exposed parameter clause have complete proofs. Root length and d/N are related by explicit resolution/root/coframe maps.'
  statuses.append(dict(unit=unit,title=title,criterion=test,status=state,reason=reason))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],statuses)
source_defs=[
 ('Khaled-v2-weighted-marked-centralizers','https://arxiv.org/pdf/2310.05265v2','arXiv:2310.05265v2, 4 December2023','Full Theorem2.1 and Remark2.2, printed p5=PDF5; preceding normal-form list(1) p3 already read in package16','/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Khaled2024_v2.pdf','The recalled table gives IIc diagonal, III(Az+Cw^r,Bw), and IV GL2 centralizers. Preserving both axes sets C=0 or the off-diagonal entries to0. No classification proof is printed at this locus.'),
 ('AbashevaDeev-v1-weighted-a0-curves','https://arxiv.org/pdf/2303.10764v1','arXiv:2303.10764v1, 19 March2023','Full section2.2.6 and sections2.2.7–2.2.9, printed p5=PDF5','/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/AbashevaDeev2023_v1.pdf','The nonresonant diagonal surface has precisely the two axis curves. Its punctured line presentation and degree-zero line factors are explicit. The secondary application passes through the already proved finite central cover; the broad automorphism sentence in section2.2.5 is not used.'),
 ('Cartan1957-weighted-torsor','https://www.numdam.org/article/BSMF_1957__85__77_0.pdf','Bulletin de la Societe Mathematique de France85 (1957),77–99; original Numdam scan','Section2 setup and complete fundamental theorem A/B statement, printed p80=PDF5; title/setup pp77–80 already opened in this package','/workspace/scratch/9fcd229a9ed4/tmp/c3_provenance_primary/Cartan1957.pdf','The recalled fundamental theorem B makes positive coherent-sheaf cohomology vanish on a Stein complex manifold. Apply it to O^2 on the punctured disc; the separate circle cellular calculation supplies H2 of the lattice local system. Only the source statement/setup at this locus was read, not a full proof of theorem B.'),
]
sources=[]
for key,url,version,locus,path,paraphrase in source_defs:
 data=Path(path).read_bytes();sources.append(dict(source_id=key,url=url,version=version,exact_locus=locus,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),own_paraphrase=paraphrase,reader='continuation3 conductor; exposed primary-locus reading',date_utc=now,storage='Temporary primary PDF cache only; no PDF/extract or image added to checkpoint artifacts.'))
tsv('_primary_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)
assert (out/(stem+'_comparison.md')).exists()
for path in out.glob(stem+'*'):
 if path.is_file():assert b'\r' not in path.read_bytes(),path
report=f'17 READY: {len(rows)} defects; {len(events)} exposed full-proof events; {len(maps)} exact owner maps; {len(formula_rows)} inherited equation identities; {len(units)} actual units/{len(statuses)} criteria;3 primary loci. Main plus4 remote guards match once. Tags P355/P356/P357/P358/P359. No central writes.\n'
(code/'S6_SERIES_PUBLISH_c3_conductor_17.out').write_text(report,newline='\n')
print(report,end='')
