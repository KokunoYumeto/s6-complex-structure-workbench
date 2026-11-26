#!/usr/bin/env python3
"""Exact comparison records for the guarded elliptic-star publication unit."""
from pathlib import Path
from datetime import datetime, timezone
import csv, re, hashlib, importlib.util
code=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('conductor16_source',code/'S6_SERIES_PUBLISH_c3_conductor_16.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
root,out,stem=c.root,c.out,c.stem
original,owners,fragments=c.original,c.owners,c.fragments
for key,value in fragments.items():assert (out/(stem+'_'+key+'.tex')).read_text()==value,key
assert (out/(stem+'_replacement.tex')).read_text()==c.main_new
assert c.current.count(c.main_old)==1
for row in c.remote_rows:assert c.current.count(row['old_text'])==1,row['statement_id']
def tsv(suffix,fields,rows):
 with (out/(stem+suffix)).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def part(text,first,last=None):
 a=text.index(first);b=text.index(last,a) if last else len(text);return text[a:b]
def statement(s):return s[:s.index(r'\begin{proof}')]
def proof(s):return part(s,r'\begin{proof}')
definition,boundary,leaf,insertion,criterion=[fragments[k] for k in ('P350','P351','P352','P353','criterion')]
destinations={49:[definition,boundary,boundary+criterion,fragments['P330_replacement']+criterion,fragments['P331_replacement']+insertion,insertion,insertion],50:[definition,definition+boundary,definition,boundary,boundary,boundary+criterion,fragments['P330_replacement']+fragments['P331_replacement']+insertion,insertion,insertion,insertion],53:[fragments['P325_replacement']+leaf+boundary,criterion,boundary+criterion,insertion]}
segments={}
for n,text in original.items():
 if n==50:
  off=text.index(r'\begin{proof}');starts=[off+m.start() for m in re.finditer(r'\\item\s+',text[off:])]
  titles=['Invariant coarse maps','Normal root character','Inverse product map','Integral boundary matrix','Hopf cap comparison','Canonical form and common period','Four-period family and finite chart','Lifted contraction','Norm and properness','Cluster and simultaneous gluing']
 else:
  matches=list(re.finditer(r'\\par\\medskip\\noindent\\textbf\{([^}]+)\}',text));starts=[m.start() for m in matches];titles=[m.group(1) for m in matches]
 assert len(starts)==len(destinations[n]),(n,len(starts))
 segments[n]=[(a,starts[i+1] if i+1<len(starts) else len(text),titles[i],destinations[n][i]) for i,a in enumerate(starts)]
def route(n,pos):
 for a,b,title,dest in segments[n]:
  if a<=pos<b:return title,dest
 return 'Complete statement and given-quasibundle specialization',statement(criterion)+statement(definition)+statement(boundary)
def para(text,pos):
 a=text.rfind('\n\n',0,pos)+2;b=text.find('\n\n',pos);return text[a:b if b>=0 else len(text)]
rows=[]
def log(kind,owner,old,new,reason,oldwhere='',newwhere=''):
 rows.append(dict(change_id=f'II-C3-STARS16-{len(rows)+1:04d}',type=kind,statement_id=owner,old_location=oldwhere or owner+' complete original source',old_page='Exact source span supplied; previous PDF page omitted',new_location=newwhere or 'Early P325/P330/P331 and five elliptic-star subsections',new_page='Pending integrated final PDF',old_text=old,new_text=new,reason=reason,review_status='Complete original and receiving proofs read and compared; exposed editorial rereading. No independent proof or computational execution credit; final PDF open.'))
for n in (49,50,53):
 owner=f'cdp:st:C.2.UN.{n}'
 log('D12',owner,statement(original[n]),statement(criterion),'One complete criterion carries all three permanent statement identities. The arbitrary-P theorem preserves the full local/compact equivalence and every component/gluing realization. Primary and secondary nonlinear criteria are explicit n=1 and all-nonlinear specializations using the SAME supplied q. Every hypothesis and conclusion is preserved.',newwhere='subsec:II:reduced-hopf-star-criterion')
 for a,b,title,dest in segments[n]:log('D12',owner,original[n][a:b],dest,'Complete proof block transferred to its single receiving owner. Exact component, root, period, finite-action and inverse morphisms are compared in owner_transfers.tsv and comparison.md. This is a full old/new proof comparison, without independent credit.',oldwhere=owner+': '+title)
log('D13','def:II:elliptic-star-data',original[49][segments[49][0][0]:segments[49][0][1]],definition,'The inverse transform, integral Chern class and choices were defined inside a later proof. A numbered definition now precedes every consumer, with complete finite translation gauge, invariant root model, inverse product and coordinate-independence maps.')
log('D14','def:II:elliptic-star-data',c.main_old,c.main_new,'Order the full stars as data, boundary/canonical periods, leaf classification, compact insertion, criterion. The old subsection label remains. Separate descriptive headings mark the untouched weighted-cycle and support/tree units as open. Local order is complete; final whole-paper structure remains open.')
log('D14','lem:II:reduced-anticanonical-hopf',owners[325],fragments['P325_replacement'],'Move complete P325 immediately after P337, before all star consumers. P327/P337 and its exact sources precede this point. The former terminal-ruled subsection remains nonempty with UN64.')
log('D12','lem:II:reduced-anticanonical-hopf',owners[325]+original[53][segments[53][0][0]:segments[53][0][1]],fragments['P325_replacement']+leaf,'The existing effective-anticanonical proof states its proved one-curve central-cover consequence, with connected inverse curve, d=r+1 and same marked contraction. AS8/AS9/AS11 transfer to it. P352 applies D=aJ and keeps the full secondary centralizer, affine averaging and character argument. Every earlier conclusion remains.')
log('D12','lem:II:zero-chern-elliptic-torsor',owners[330]+original[49][segments[49][3][0]:segments[49][3][1]],fragments['P330_replacement']+insertion,'Use P330 on the SAME q0:T0->B, F1=F, Gamma=Gamma_B, (z,w)_KX=(p,z). Its Cech zero-cochain translations and inverse identify the original torsor over B. Only NS14 joins KX14/PT8 as an alias; statement/proof unchanged.')
log('D12','lem:II:logarithmic-period-family',owners[331]+original[49][segments[49][4][0]:segments[49][4][1]],fragments['P331_replacement']+insertion,'The full rank-four compact clause uses the same V_t/infinity frame; its inverse/norm and uniformly bounded matrices prove the proper compact quotient. The existing logarithmic clause is unchanged. The star uses this exact Lambda0 under t=s^R, and NS15 is exactly V_t((p,z)).')
all_new=c.main_new+'\n'+'\n'.join(fragments[f'P{n}_replacement'] for n in (325,330,331))
new_displays={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',all_new,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
aliases={x['old_tag']:x for x in c.alias_maps}
changes={
 'C.NS.13':('Same base generators renamed a_B,b_B to distinguish boundary a,b.',lambda s:s.replace('a_B','a').replace('b_B','b')),
 'C.NS.16':('Old coordinate p_i is p^(i), distinct from marked point p_i^0. R=r on the original all-nonlinear scope.',lambda s:s.replace(r'p^{(i)}','p_i').replace('s^R','s^r')),
 'C.NS.17':('Original primary all-nonlinear case has n_i=1, gamma_i=beta_i and R=r; primitive periods and d_i are the same.',lambda s:s.replace(r'\gamma_i',r'\beta_i').replace('s^R','s^r')),
 'C.SN.9':('The common r is r_i in the mixed insertion; set every r_i=r for the identical original finite action.',lambda s:s.replace('r_i','r')),
 'C.AS.15':('The same transported integral cycle gamma is gamma_core, distinct from deck multiplier gamma=beta^n.',lambda s:s.replace(r'\gamma_{\rm core}',r'\gamma')),
 'C.AS.16':('The same integral cycle gamma is gamma_core; its diagonal order estimate is unchanged.',lambda s:s.replace(r'_{\gamma_{\rm core}}',r'_\gamma'))}
def payload(s):
 s=re.sub(r'\\SsixEquationAliases\{(?:\s*\\label\{[^}]+\})+\s*\}','',s)
 s=re.sub(r'\\tag\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}|\\label\{[^}]+\}','',s)
 for x in (r'\[',r'\]',r'\begin{equation}',r'\end{equation}'):s=s.replace(x,'')
 return re.sub(r'\s+','',s)
formula_rows=[]
for tag,old in c.equations.items():
 label=c.established[tag];new=new_displays[label]
 if tag in aliases:explanation=aliases[tag]['map'];result='Exact formula alias under the stated morphism/specialization'
 else:
  explanation,transform=changes.get(tag,('Identical mathematical payload, variables and maps.',lambda s:s));assert payload(old)==payload(transform(new)),tag;result='Formula payload preserved under the declared coordinate identity'
 formula_rows.append(dict(old_tag=tag,target_label=label,result=result,map=explanation))
 log('D19',label,old,new,'Replace the manual tag by section equation numbering, preserving its permanent target and established D19 label. '+explanation)
for n,text in original.items():
 owner=f'cdp:st:C.2.UN.{n}'
 for m in re.finditer(r'(?<![:{])\bC\.[A-Z]+\.\d+',text):
  tag=m.group();assert tag in c.established,tag;title,dest=route(n,m.start());label=c.established[tag]
  log('D04',owner,para(text,m.start()),new_displays.get(label,dest),f'Printed internal scheme {tag} resolves through established label {label}, or its displayed common owner proving the identical map. Exact scope is in the owner/formula maps.',oldwhere=f'{owner} line {text[:m.start()].count(chr(10))+1}, character {m.start()}: {title}')
 for m in re.finditer(r'\b(actual|genuine|retain(?:ed|s|ing)?|supplied|specified|surviving)\b',text,re.I):
  title,dest=route(n,m.start());log('D08',owner,para(text,m.start()),dest,f'Replace this assurance/process occurrence of "{m.group()}" by its explicit mathematical object and proved maps. The receiving block preserves the full component, torsor, character, lattice or gluing datum; mathematical original-data comparisons remain.',oldwhere=f'{owner} line {text[:m.start()].count(chr(10))+1}, character {m.start()}: {title}')
 for m in re.finditer(r'(?im)^.*(?:rather than|not merely|not just|not a formal|No extension|no assumption|No assertion|no initial|without an a priori|unproved).*(?:\n.*){0,2}',text):
  title,dest=route(n,m.start());log('D02',owner,para(text,m.start()),dest,'Delete the defensive contrast. Its mathematical scope is stated positively: same q, degree-one root cover, primitive characters, full analytic transitions, and all-diagonal R choice where relevant.',oldwhere=f'{owner} line {text[:m.start()].count(chr(10))+1}: {title}')
program=part(original[53],'The exact symbolic checks in',r'\end{proof}')
log('D09','cdp:st:C.2.UN.53',program,fragments['P325_replacement']+insertion,'Remove body path and finite-search bookkeeping. The weight equation is proved for all weights at P325; P353 proves base maps, faithful finite charts and period insertion. The pinned root_mixed_hopf_stars.py row is admitted in Programs appendix addition162. No execution credit.',newwhere='P325/P353 mathematics; Programs appendix correction162')
log('D17','lem:II:hopf-single-canonical-curve',original[53][segments[53][0][0]:segments[53][0][1]],leaf,'Freshly opened the complete Khaled arXiv:2310.05265v2 Theorem2.1 and Remark2.2, printed p5. Its classIII parameters (a,b,d)=(A,C,B) give the exact centralizer; classIV GL2 with the marked-axis lower-left entry zero gives r=1. Finite-affine averaging, coordinate inverse and canonical character remain proved. No unprinted classification proof is claimed.')
notation=[
 ('cdp:eq:C.NS.13',c.equations['C.NS.13'],new_displays['cdp:eq:C.NS.13'],'Base generators become a_B,b_B; boundary angular/deck generators remain a,b. Identity on each geometric loop gives the same group presentation.'),
 ('cdp:eq:C.NS.16',c.equations['C.NS.16'],insertion,'Use p^(i) for the family coordinate, p_i^0 for its marked lift, and p_loc=p-p_i^0. The weighted map is p_loc=x^(r_i)z,s=xw; the inverse product recovers p_loc.'),
 ('cdp:eq:C.AS.15',c.equations['C.AS.15'],new_displays['cdp:eq:C.AS.15'],'The transported integral gamma becomes gamma_core, with the same orientation and integral; gamma=beta^n stays the multiplier.'),
 ('lem:II:reduced-anticanonical-hopf',owners[325],fragments['P325_replacement'],'Use e in u=eq,v=ep and F^e, leaving d for the effective divisor coefficient. The same finite unramified cover preserves all coefficients.'),
 ('lem:II:compact-elliptic-star-insertion',proof(original[53]),insertion,'The norm multiplier is varrho_i(s); lambda_i remains a period basis vector. The exact expression and uniform bounds are unchanged. gamma_i=beta_i^(n_i), and R=r on the former all-nonlinear domain.'),
 ('lem:II:hopf-single-canonical-curve',proof(original[53]),leaf,'beta_0 is the distinguished central multiplier; beta generates the full discrete contraction group. The central element is a positive power times a finite element, with the same r-weighted marked-axis maps.')]
for owner,old,new,reason in notation:log('D20',owner,old,new,reason)
log('D22','def:II:elliptic-star-data',proof(original[49])+proof(original[50]),definition,'Write the finite gauge h(s)=-(1/m)sum_j j upsilon(zeta^j s) and prove h(zeta s)-h(s)=-upsilon(s). Changes of Bezout choices by (na,ra) give X->Xu^a and fix p,W; every choice has its precise reason and inverse map.')
log('D22','cdp:st:C.2.UN.53',para(original[53],original[53].index('R=1+')),criterion,'The all-diagonal value R=1+max r_i satisfies all strict inequalities. A nonlinear leaf fixes the finite vanishing order by its nonzero core integral. No nonzero period is imposed on an all-diagonal given family.')
false_sentence='The non-torsion flat line and every original primitive fibre direction are retained by these actual period maps.'
assert false_sentence in re.sub(r'\s+',' ',original[53])
log('D25','cdp:st:C.2.UN.53',para(original[53],original[53].index('The non-torsion flat line')),insertion,'The permitted product T0=F times B is a counterexample to the intermediate non-torsion adjective. Complementary periods with zero fibre coordinate have factors1, hence M_(i,0) is trivial. Remove only non-torsion. Degree zero suffices; its constant factors, unitary metric and complete period maps remain proved. Every original theorem statement and compact realization conclusion is unchanged.')
log('D23','lem:II:zero-chern-elliptic-torsor',owners[330],fragments['P330_replacement'],'PT8 and transferred NS14 share ONE SsixEquationAliases call after both permanent targets. Every receiving equation has at most one hook and no blank paragraph. Formula/targets unchanged; final rendering stays open.')
for display in re.findall(r'\\begin\{equation\}.*?\\end\{equation\}',all_new,re.S):
 assert display.count(r'\SsixEquationAliases')<=1
 assert not re.search(r'\n[ \t]*\n',display)
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],[dict(old_tag=k,target_label=c.established[k],statement_id='Receiving owner in formula_comparisons.tsv') for k in c.equations])
tsv('_formula_comparisons.tsv',['old_tag','target_label','result','map'],formula_rows)
maps=[
 ('UN49/UN50/UN53 statement identities','UN53 with UN49/UN50 aliases','Full local/compact equivalence and the same given-quasibundle tests.','Same S,P,H_i,J_i and maps. UN49 uses n_i=1,k=0,l=-1,u=z,X=x,W=x^-1. UN50 uses arbitrary coprime n_i and all nonlinear leaves. The supplied q is kept; equal r, marked multiplicities, no unmarked multiples and integral Chern tests remain.'),
 ('UN49 inverse transform; UN50 items1–3','P350','Complete marked data, root charts, normal order, inverse transform and choice independence.','(z,x)->(u=z^n,X=xz^k) has exactly mu_n orbit fibres. Product exponent matrix has determinant-1 and inverse u=p^nW^r,X=p^kW^l. Explicit finite gauge and dual normal covers give the same q neighbourhood. Changing k,l gives X->Xu^a, fixing p,W.'),
 ('UN49 boundary/topology; UN50 items4–5','P351','Primitive meridians, full n_i correction, same smooth fibre and common integral core cycle.','SN6 columns(a,b,mu_P), rows(delta,e,h), determinant1. Hopf delta_H=na-k mu_H,e_H=ra-l mu_H; xy=t gives mu_H=-mu_P. P326 applies to the same full reduced SNC/no-triple star. Finite-equivariant resonant-coefficient homotopy uses a uniform compact annulus and axis-tangent transport.'),
 ('UN49/50/53 canonical and periods','P351 and merged criterion','Arbitrary-P canonical orders, broad q canonical/direct-image map, nonlinear/diagonal period orders and zero Chern necessity.','UN17 applies on the same proper-disc full-reduced star. The separate quasibundle formula precedes its marked-fibre use; invariant a(s)ds alpha gives a=s^(m-1)b(s^m). gamma_core is the same oriented Hopf core/ordinary q0 fibre; secondary angular period is2pi i/n. pi2(B)=0 injects fibre pi1, and the same Chern commutator vanishes.'),
 ('UN53 weighted-anticanonical proof','Early P325','All old effective/reduced conclusions and connected central cover of a multiple single curve.','Take D=aJ. P327 central cover and its central F^e power preserve coefficients. Factor the same weighted polynomial into axes and z^q-cw^p; ampq=p+q. Coordinate changes/inverses preserve divisor and contraction. The single curve has d=r+1 and w=0; reduced marking and log form remain.'),
 ('UN53 secondary leaf classification','P352','Exactly all marked Hopf pairs with K=-aJ, a=r+1.','P248 gives J elliptic; P337 h0(K)=0 gives a>0; P325 gives connected axis cover. SH3/SH4 split the nonlinear group. Khaled classIII/IV gives Az+Cw^r,Bw; finite-affine averaging gives z_prime=z-cw^r with inverse. Canonical character forces A=B^r; freeness forces gcd(r,n)=1.'),
 ('UN49 NS14 and repeats','P330','Same analytic zero-Chern torsor as full lattice quotient over B.','F1=F,Gamma=Gamma_B,(z,w)_KX=(p,z),Lambda_F1=Lambda_F. Same cocycle differs by c_j-c_i; translations w->w+c_i and inverse preserve q0. NS14 is the KX14 alias.'),
 ('UN49 NS15 and repeated compact family','P331 rank-four clause','Compact proper smooth family with exact central lattice and s^R pullback.','V_t(w)=w+tJ bar w, V_s^infinity=J bar w+s w on O(1)^2. Existing norm/inverse gives uniformly invertible four-period matrices; compact parallelepipeds prove properness. NS15 ell_t(p,z)=V_t((p,z)); logarithmic clause unchanged.'),
 ('UN49/50/53 weighted insertion','P353','Compact realization with every analytic component, finite group, primitive direction and elliptic gluing.','Exact q0 lattice, t=s^R,gamma_i=beta_i^(n_i),same fibre periods. M_i,s is degree zero. At p_loc=p-p_i^0=x^(r_i)z,s=xw, line weight-ni gives the same free mu_ni chart. AS18 gives SN10 at R=r_i=r and NS19 when also n_i=1. Exponential/local-log maps match all four generators.'),
 ('UN49/50/53 properness and gluing','P353 final proof','Free proper local quotient, Hausdorff compact replacement, exact P/leaves/gluings and Euler-zero supports.','Unitary gauge gives0<varrho_-<=varrho_i<=varrho_+<1. Two-sided polynomial distortion exponent n_i/r_i is dominated by exponential contraction. Fixed compact norm annulus gives properness. O(log|x|) iterates and |s|^Rlog|x|->0 put all clusters on F_i; closed graphs and nested compact refinements prove gluing. Inverse product recovers p_loc and transitions; weighted axis automorphisms commute with every finite group.'),
 ('UN53 arbitrary-P necessity','Merged UN53','P is a torus or identity-monodromy elliptic quasibundle over elliptic B, with all J_i as marked fibres.','Full multiplicity1 gives generic x=s^N and degree-one strict component cover; both minimal models equal P. UN28 bounds pg; UN31/P306 give pg=g(B). Disjoint torus elliptic curves have one subgroup direction. Horizontal curves contradict effective multiple-fibre canonical divisor or pulled-back Chern class; Chern0 applies P330 to the same q. A supplied q is preserved.')]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],[dict(zip(['old_owner','new_owner','conclusion','map'],r)) for r in maps])
deps=[
 ('Early P325','P327/P337/P248 and exact Hopf sources','Same W,full group,central cover and divisor; no star input.','Backward after approved move; old terminal-ruled heading remains nonempty.'),
 ('P350','P306 and P330 sheaf sequence','Same relatively minimal fixed-Jacobian quasibundle, all fibres elliptic multiples.','Backward; before all star consumers.'),
 ('P351','P350/P326/UN17','Boundary domain full reduced SNC/no-triples; arbitrary-P canonical domain; separate broad q canonical domain.','Backward; every application domain explicit.'),
 ('P352','P248/P337/P327/P325/P351 and UN43 SH3–4','Same H,J,D=aJ,connected central axis; full nonlinear group split.','Backward; complete P325 moves earlier.'),
 ('P353','P350/P330/P331/UN42 NH6–11 and P306/P337','Exact q0 lattice, arbitrary degree-zero M,faithful weighted line and same uniform annulus.','Backward; P331 extension admitted atomically. Provenance UN42 keeps weighted charts unchanged.'),
 ('Merged UN53','P350–353,UN17/28/31,P306,cyclic-component cover','Multiplicity1 means degree-one root cover. Same P,canonical and pg maps; supplied q preserved.','Local order complete; no refined P4R.13/P4.40 use.'),
 ('UN52','Weighted Hopf cycles subsection','Complete weighted-cycle text untouched.','Open; full original reading is not a completed publication unit.'),
 ('UN54/56/58–63','Hopf support graphs and rational-root trees','Admitted UN54/P337 and UN61/P330 deltas untouched.','Open; section10 identity and full-section structure remain open.')]
tsv('_dependencies.tsv',['consumer','input','map','status'],[dict(zip(['consumer','input','map','status'],r)) for r in deps])
now=datetime.now(timezone.utc).isoformat()
event_defs=[
 ('cdp:st:C.2.UN.49','UN49','_criterion.tex','Read complete original primary nonlinear-star statement/proof and all receiving owners. Compared same-q tests, inverse transform, integral boundaries, core transport, canonical/equal-period argument, Chern-zero torus, full rank-four family, weighted insertion, uniform properness, clusters and compact gluing. Explicit n=1,k=0,l=-1,u=z,X=x,W=x^-1 preserves every conclusion and target.'),
 ('cdp:st:C.2.UN.50','UN50','_criterion.tex','Read complete original secondary-star statement and all ten proof items, and every receiving owner. Compared invariant finite maps/inverses, normal character, determinant-one matrix, full n_i meridian, primitive2pi i/n period, four-period quotient, faithful line, contraction, compact annulus, cluster and exact gluing. The all-nonlinear specialization uses the SAME q with every coprime secondary order.'),
 ('cdp:st:C.2.UN.53','UN53','_criterion.tex','Read complete original mixed-star statement/proof and complete merged receiver. Compared canonical leaf classification, degree-one root component map, minimality/pg, torus/quasibundle alternatives, horizontal-curve exclusions, normal multiplicities, period orders and all-diagonal R, full compact construction. Corrected only the false non-torsion adjective: product F times B makes M_i,0 trivial. Complete degree-zero/unitary proof and theorem conclusions remain.'),
 ('def:II:elliptic-star-data','P350','_P350.tex','Read complete receiving definition/proof against all three full originals. Verified finite gauge h(zeta s)-h(s)=-upsilon(s), exact torsion order, invariant monomial quotient/inverse, dual normal roots, unimodular product/inverse, analytic gluing, integral Chern class and every compatible coordinate change.'),
 ('lem:II:elliptic-star-boundary','P351','_P351.tex','Read complete receiving statement/proof. Compared separate arbitrary-P canonical and broad-q canonical domains, primitive boundary matrices/sign, diagonal/nonlinear caps, finite-equivariant smooth contraction homotopy, exact P326 hypotheses, T0 and gamma_core, root differential direct image, canonical forms, nonlinear determinant, diagonal order, Stokes holomorphic period and injected-fibre Chern commutator.'),
 ('lem:II:hopf-single-canonical-curve','P352','_P352.tex','Read complete receiving classification against original UN53 and full current P325/P327/P337/UN43 inputs. Freshly read Khaled v2 pp3–5, including full Theorem2.1/Remark2.2 p5. ClassIII parameters map to(A,C,B); classIV plus marked axis gives r=1. Kept finite-affine averaging/inverse, nonlinear SH3/SH4 split, primitive versus central multiplier, canonical character and coprimality.'),
 ('lem:II:compact-elliptic-star-insertion','P353','_P353.tex','Read complete receiving construction against all UN49/50/53 compact blocks and full proposed UN42. Compared exact torsor/lattice, rank-four family, all four periods/exponential inverse, degree-zero line/unitary gauge, centred coordinates, finite roots, deck action, contraction normalization, weighted distortion/annulus, freeness, clusters, closed graphs and finite compact refinement. Exact P,leaves,markings,elliptic maps and Euler numbers remain.'),
 ('lem:II:reduced-anticanonical-hopf','P325','_P325_replacement.tex','Read full original/receiving P325 and full UN53 application. Preserved all effective/reduced alternatives and marked reduced conclusion. Existing weight proof gives connected single-curve central cover with d=r+1. AS8/9/11 move with exact finite-cover, factorization and log-form maps; gcd power e differs from coefficient d. Freshly read Abasheva–Deev v1 pp4–5, including sections2.2.2 and2.2.6.'),
 ('lem:II:zero-chern-elliptic-torsor','P330','_P330_replacement.tex','Read complete current P330 and alias-only receiver, compared full original NS14 Cech construction. Same q0:T0->B,F1=F,Gamma=Gamma_B,(z,w)=(p,z) give KX14. Complete local translations/inverses unchanged. NS14 and PT8 use one alias hook after both targets.'),
 ('lem:II:logarithmic-period-family','P331','_P331_replacement.tex','Read full admitted P331 and complete receiver. Logarithmic clause/proof unchanged. Verified rank-four translation quotient on O(1)^2,infinity frame,V_t norm/inverse,uniform period matrices/inverses,compact parallelepipeds,connected torus fibres,compact proper total family. Exact pullback t=s^R is star input. NS15 equals V_t((p,z)) under the explicit coordinate identity.')]
events=[]
for owner,key,suffix,result in event_defs:
 events.append(dict(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=result+' Exposed editorial reading and comparison only; no independent proof or computational execution credit. All bounded final notation, wording and alias-hook changes were reread. No refined P4R.13/P4.40 use occurs. Final integrated PDF pages remain unread.',event_id='publish:c3:conductor16:'+key,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+stem+suffix,source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor16:elliptic-stars',publish_input_file='',publish_input_row='',date_utc=now,where='Complete original/receiving star units and bounded P325/P330/P331 owners'))
tsv('_CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
units=[('subsec:II:elliptic-star-data','Elliptic star data and inverse transforms; preserves star-weighted-constructions identity'),('subsec:II:star-boundary-periods','Boundary maps and periods of elliptic stars'),('subsec:II:hopf-leaf-pairs','Canonical divisors on Hopf leaf pairs'),('subsec:II:compact-elliptic-star-insertion','Compact insertion of elliptic stars'),('subsec:II:reduced-hopf-star-criterion','The reduced Hopf-star criterion'),('subsec:II:logarithmic-period-families','Logarithmic period families with compact rank-four clause'),('subsec:II:weighted-hopf-cycles','Weighted Hopf cycles'),('subsec:II:hopf-support-tree-remainder','Hopf support graphs and rational-root trees')]
statuses=[];open_units={units[-1][0],units[-2][0]}
for unit,title in units:
 for test in [f'D{i:02}' for i in range(1,26)]+['structure']:
  state='done';reason='Complete original and receiving unit compared across all25 classes; local instances are repaired in exact per-instance rows and owner/formula maps.'
  if test in ('D10','D16'):reason='Prior done status preserved. Every old label/permanent tag remains; all new owners have mathematical titles.'
  elif unit in open_units:state='open';reason='Following complete weighted-cycle or support/tree publication unit remains open. Only its heading changes; no completed unit review is claimed.'
  elif test in ('D14','structure'):reason='Local order and five actual star subsections complete. P325 moves after P337; P330/P331 precede data,boundary,leaf,insertion,criterion. Remaining section10 and final whole-paper structure stay open.'
  elif test=='D18':state='open';reason='Exact primary versions/loci freshly read and recorded; source-wide bibliography remains a separate gate.'
  elif test=='D23':state='open';reason='Source environments,single alias hooks and equation paragraph breaks checked; final integrated PDF pages remain open.'
  elif test=='D24':state='open';reason='Body owners/headings complete; final results-list and organization reconciliation remains with root.'
  elif test=='D19':reason='All49 inherited targets/established labels preserved, with exact aliases and explicit variable maps. Section numbering replaces all manual tags.'
  elif test=='D25':reason='Every inference/map compared. The non-torsion assertion is corrected by the permitted product counterexample; degree zero suffices and full unitary/period proof remains. Canonical domains and degree-one component cover are explicit.'
  statuses.append(dict(unit=unit,title=title,criterion=test,status=state,reason=reason))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],statuses)
sources=[]
for key,url,version,locus,path,paraphrase in [
 ('Khaled-v2-star-centralizers','https://arxiv.org/pdf/2310.05265v2','arXiv:2310.05265v2, 4 December 2023','Complete printed pp3–5; normal-form list(1) p3; full Theorem2.1 and Remark2.2 p5','/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/Khaled2024_v2.pdf','ClassIII centralizer is (Az+Cw^r,Bw); classIV is GL2, and marking w=0 gives the r=1 upper triangular form. Nonlinear list also read. These are recalled source statements; no classification proof is printed at this locus.'),
 ('AbashevaDeev-v1-star-curves-lines','https://arxiv.org/pdf/2303.10764v1','arXiv:2303.10764v1, 19 March 2023','Complete printed pp4–5; section2.2.2 p4; section2.2.6 and sections2.2.7–2.2.9 p5','/tmp/S6_SERIES_PUBLISH_c3_conductor_primary/AbashevaDeev2023_v1.pdf','Nonlinear unique elliptic axis, diagonal curve cases, degree-zero constant factors and full line-coordinate conversion. The broad automorphism assertion in section2.2.5 is not used; P352 applies Khaled classIII/IV.')]:
 data=Path(path).read_bytes();sources.append(dict(source_id=key,url=url,version=version,exact_locus=locus,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),own_paraphrase=paraphrase,reader='continuation3 conductor; exposed editorial primary-locus reading',date_utc=now,storage='Primary PDF read from temporary cache; no PDF/extract added to checkpoint artifacts.'))
tsv('_primary_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)
assert (out/(stem+'_comparison.md')).exists()
for path in out.glob(stem+'*'):
 if path.is_file():assert b'\r' not in path.read_bytes(),path
report=f'16 READY: {len(rows)} defects; {len(events)} exposed full-proof events; {len(maps)} exact owner maps; {len(formula_rows)} inherited equation identities; {len(units)} actual units/{len(statuses)} criteria. Main plus5 remote guards match once. Tags P350/P351/P352/P353; no central writes.\n'
(code/'S6_SERIES_PUBLISH_c3_conductor_16.out').write_text(report,newline='\n')
print(report,end='')
