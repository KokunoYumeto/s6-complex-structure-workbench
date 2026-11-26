#!/usr/bin/env python3
"""Prepare the complete Hopf-axis adjacency unit and bounded P327 scope map."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv,re,hashlib

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
prefix='S6_SERIES_PUBLISH_c3_conductor_14'
reference=(out/'S6_SERIES_PUBLISH_c3_conductor_sec10_initial_reference.tex').read_text()
old=reference[:reference.index(r'\begin{proposition}[The diagonal Hopf cycle')]
current=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
pos=current.index(r'\hypertarget{tag-P327}')
a=current.rfind(r'\begin{lemma}',0,pos);b=current.index(r'\end{proof}',pos)+len(r'\end{proof}')
old327=current[a:b]
rows=[];REVIEWED=True
def log(kind,a,b,reason,owner='cdp:st:C.2.UN.40',where='Complete UN40 original statement/proof'):
    rows.append(dict(change_id=f'II-C3-SEC10ADJ14-{len(rows)+1:04d}',type=kind,statement_id=owner,old_location=where,old_page='exact source span supplied; original PDF page omitted',new_location='subsec:II:hopf-axis-adjacency; bounded P327 guard where named',new_page='pending integrated final PDF',old_text=a,new_text=b,reason=reason,review_status='Complete original and receiving statements/proofs compared; exposed editorial rereading; final PDF open.' if REVIEWED else 'Complete original read; receiving comparison pending.'))
def edit(s,a,b,kind,reason,owner='cdp:st:C.2.UN.40',where='Complete UN40 original statement/proof'):
    assert s.count(a)==1,(a[:100],s.count(a));log(kind,a,b,reason,owner,where);return s.replace(a,b,1)
def span(s,a,b):i=s.index(a);return s[i:s.index(b,i)]

new327=old327
a=r'''Hopf covering. Pullback identifies $\mathcal M(H)$ with a subfield
of $\mathcal M(P)$ over which $\mathcal M(P)$ is algebraic;
in particular $a(P)=a(H)$.'''
b=r'''Hopf covering. For every finite connected unramified cover $p:P'\to H$, pullback identifies $\mathcal M(H)$ with a subfield of $\mathcal M(P')$ over which $\mathcal M(P')$ is algebraic. Thus $a(P')=a(H)$; in particular $a(P)=a(H)$ for the central primary cover $\pi$.'''
new327=edit(new327,a,b,'D12','States the full arbitrary finite connected unramified-cover domain already proved by the same local-sheet polynomial construction. The central primary-cover conclusion and every covering map in its proof remain unchanged.','lem:II:central-primary-hopf-cover','Complete current P327 statement/proof')
a=span(old327,'For $g\\in\\mathcal M(P)$',r'\end{proof}')
b=r'''For $g\in\mathcal M(P')$, take the elementary symmetric functions of its values on the finitely many local sheets of the given finite unramified cover $p:P'\to H$. They are unchanged by the sheet permutations, so glue to meromorphic functions on $H$. Their monic polynomial annihilates $g$. Since $p$ is surjective, pullback is injective. This proves the asserted algebraic field inclusion for this $p$. Algebraic extensions have the same transcendence degree over $\C$, giving $a(P')=a(H)$. Taking $p=\pi$ gives the central-cover instance.
'''
new327=edit(new327,a,b,'D12','Uses p and its actual local sheets throughout the existing monic-polynomial argument. The proof applies equally to a nongalois finite unramified cover because the symmetric functions are invariant under all local sheet permutations.','lem:II:central-primary-hopf-cover','Complete current P327 statement/proof')

new=old
a=next(x for x in old.splitlines() if x.startswith(r'\section'))
b=a+'\n\n'+r'\subsection{Hopf axes and canonical-order ratios}\label{subsec:II:hopf-axis-adjacency}'
new=edit(new,a,b,'D14','Places the complete adjacency theorem in its own actual subsection before every cycle/tree consumer. The section identity and permanent tag remain unchanged.','subsec:II:hopf-axis-adjacency','Section10 opening')
a=next(x for x in old.splitlines() if x.startswith(r'\StatementRecord'))
b=r'\StatementRecord{cdp:st:C.2.UN.40}{proved}{01DK}{\cref{cdp:st:C.2.UN.17,lem:II:central-primary-hopf-cover}; \cite[arXiv v2, normal forms (1), p.~3; Theorem~2.1, p.~5]{Khaled2024Hopf}; \cite[arXiv v1, \S2.2.2, p.~4; \S2.2.6, p.~5]{AbashevaDeev2024AB}}'
new=edit(new,a,b,'D18','Uses the exact opened versions and loci for the primary normal forms and the nonlinear/diagonal curve lists, and names the shared canonical and finite-cover owners.')
a=span(old,r'\item The direct image $f_*K_U$',r'For $j\ne i$ put')
b=r'''\item Apply \cref{cdp:st:C.2.UN.17} to the same $f:U\to\Delta$ and full fibre $\sum_i m_iE_i$. Its canonical evaluation is the generator chosen in the statement, with $K_U\simeq\OO_U(\sum_i k_iE_i)$. Each smooth $E_i$ has identity normalization and resolution and intrinsic conductor divisor zero. The principal-fibre and adjunction maps \eqref{cdp:eq:C.CA.3}--\eqref{cdp:eq:C.CA.4} therefore apply directly to $E_i$.
For $j\ne i$ put'''
new=edit(new,a+'For $j\\ne i$ put',b,'D12','Reuses the proved canonical generator on the identical proper family. Smooth SNC components have identity normalization/resolution and intrinsic conductor zero; the arbitrary full multiplicities are preserved. The following integral HA3 elimination remains explicit.')
a='Thus \\eqref{cdp:eq:C.HA.3} has no rational divisor or divisibility convention.'
new=edit(new,a,'','D02','The displayed integral divisor-class identity and the explicit multiplication by m_i already state the required convention positively.')
a='This is a\ndivisor-class homomorphism; no equality with the coherent\ndirect image of an arbitrary line bundle is asserted.\n'
new=edit(new,a,'','D02','The preceding prime-divisor pushforward and common-function-field map explicitly define the homomorphism being used; removes the unneeded contrast with a different functor.')
a=span(old,r'We record precisely the curve and line',r'\item For completeness, denote')
b=r'''The primary normal forms are \cite[arXiv v2, normal forms (1), p.~3; Theorem~2.1, p.~5]{Khaled2024Hopf}. Apply \cref{lem:II:central-primary-hopf-cover} to this given finite connected unramified cover $p:P\to H_i$. Its field inclusion is the pullback by $p$, and gives $a(P)=a(H_i)=0$.

For a diagonal contraction, a relation $\alpha^a\beta^b=1$ for a nonzero integer pair would make $z^aw^b$ a nonconstant meromorphic function on $P$. Thus no such relation holds. The primary curve classification \cite[arXiv v1, \S2.2.6, p.~5]{AbashevaDeev2024AB} then gives precisely the two axis curves $C_1,C_2$. For the nonlinear contraction, \cite[arXiv v1, \S2.2.2, p.~4]{AbashevaDeev2024AB} gives precisely $C=(w=0)$, including resonance $r=1$.

\item Denote'''
new=edit(new,a+r'\item For completeness, denote',b,'D17','Replaces the full Remmert–Stein/eigenfunction reproof of the published curve classification by the exact freshly opened primary loci. Keeps the monomial map proving that a(P)=0 satisfies the nonresonance hypothesis of the diagonal locus. The finite-cover field inclusion is applied to the given p through the expanded P327 statement.')
a='This proves both assertions on the\noriginal component after all its point blowups, with\nthe actual finite-primary-cover comparison included.'
b='The divisor pushforward and the pullback by $p$ prove both assertions on the original component after all its point blowups.'
new=edit(new,a,b,'D08','Names the exact composed divisor maps producing the original-component conclusion.')
a='The theorem gives these exact\nadjacency restrictions and does not infer a global\nnonexistence assertion from a local decrease.'
new=edit(new,a,'','D02','The theorem already states its precise local adjacency conclusions; removes a defensive comparison with an unstated global claim.')
for p in new.split('\n\n'):
    q=re.sub(r'\bactual\s+','',p)
    q=q.replace('an finite','a finite')
    q=q.replace('We specify its pushforward through the point blowdowns.','Push the divisor class forward through the point blowdowns.')
    if p!=q:new=edit(new,p,q,'D08','States the given finite covering, components, evaluation or divisor map directly, preserving the same named objects and every coefficient.')

with (root/'agents/continuation2_B/D19/S6_SERIES_PUBLISH_II_B2_D19_v1_equation_map.tsv').open() as f:
    established={r['old_tag']:r['target_label'] for r in csv.DictReader(f,delimiter='\t') if r['old_tag']}
equations=[]
def num(m):
    a=m.group();tags=re.findall(r'\\tag\{([^}]+)\}',a)
    if not tags:return a
    assert len(tags)==1;tag=tags[0];lab=re.findall(r'\\label\{([^}]+)\}',a)[0];assert established[tag]==lab
    b=a.replace(r'\[',r'\begin{equation}',1);b=b[:-2]+r'\end{equation}';b=b.replace(r'\tag{'+tag+'}','')
    log('D19',a,b,'Uses the section equation counter and preserves the exact integral formula, label and permanent target.',lab)
    equations.append(dict(old_tag=tag,target_label=lab,statement_id='cdp:st:C.2.UN.40'));return b
new=re.sub(r'\\\[.*?\\\]',num,new,flags=re.S)
new=re.sub(r'\n{4,}','\n\n\n',new).rstrip()+'\n\n'
nextheading=r'\subsection{Marked cycle and tree constructions}\label{subsec:II:marked-cycle-tree-constructions}'+'\n\n'
new+=nextheading
log('D14','',nextheading,'Provides a stable heading for the following UN46-onward unit, whose inherited all-25-class rows remain open until its complete rewrite. This package closes only Hopf-axis-adjacency.','subsec:II:marked-cycle-tree-constructions','Immediately before unchanged UN46')

def payload(s):
    s=re.sub(r'\\tag\{[^}]+\}|\\label\{[^}]+\}|\\hypertarget\{[^}]+\}\{\}','',s)
    for x in [r'\[',r'\]',r'\begin{equation}',r'\end{equation}']:s=s.replace(x,'')
    return re.sub(r'\s+','',s)
old_disp={lab:m.group() for m in re.finditer(r'\\\[.*?\\\]',old,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
new_disp={lab:m.group() for m in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',new,re.S) for lab in re.findall(r'\\label\{([^}]+)\}',m.group())}
assert len(equations)==6
for lab,d in old_disp.items():assert payload(d)==payload(new_disp[lab]),lab
for kind in ['label','hypertarget']:
    p=r'\\'+kind+r'\{([^}]+)\}';before=Counter(re.findall(p,old+old327));after=Counter(re.findall(p,new+new327))
    assert all(after[k]==v for k,v in before.items());assert max(after.values())==1
for s in [new,new327]:assert Counter(re.findall(r'\\begin\{([^}]+)\}',s))==Counter(re.findall(r'\\end\{([^}]+)\}',s))
assert not re.search(r'\\tag\{|\(C\.|night:P4R\.13|night:P4\.40|\r|\\path\{|\\textbf\{',new)
assert current.count(old)==1 and current.count(old327)==1

def tsv(suffix,fields,data):
    with (out/(prefix+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(data)
for suffix,s in [('_input.tex',old),('_replacement.tex',new),('_P327_input.tex',old327),('_P327_replacement.tex',new327)]:
    (out/(prefix+suffix)).write_text(s,newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_equations.tsv',['old_tag','target_label','statement_id'],equations)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],[dict(statement_id='lem:II:central-primary-hopf-cover',old_text=old327,new_text=new327,reason='Full bounded P327 guard. Central-primary-cover construction unchanged; arbitrary finite connected unramified-cover field clause is proved by the identical symmetric polynomial on the given p local sheets. UN40 applies that clause to its chosen p.')])
if not REVIEWED:
    print(f'14 PREPARED: {len(rows)} defects; six unchanged equation payloads; exact main and P327 guards match once. Complete receiving review pending.')
    raise SystemExit

now=datetime.now(timezone.utc).isoformat()
maps=[dict(old_owner='UN40 canonical generator',new_owner='UN17',conclusion='The same vertical canonical divisor and integral HA3 identity with arbitrary full multiplicities.',map='Same f:U->Delta, same full sum m_iE_i; smooth E_i has identity normalization/resolution and intrinsic conductor zero. CA3/CA4 give K_Ei and m_iN_i; substitute the principal relation and add m_iD_i to obtain the unchanged coefficients.'),dict(old_owner='UN40 finite-cover meromorphic field paragraph',new_owner='P327 arbitrary-cover clause',conclusion='The exact pullback p*:M(H_i)->M(P) is injective with algebraic image extension, so a(P)=a(H_i)=0.',map='Apply the broadened clause to the given finite connected unramified primary p:P->H_i, with Pprime=P and H=H_i. Elementary symmetric functions are formed on these local sheets, independent of any Galois assumption or choice of the central primary cover.'),dict(old_owner='UN40 Remmert–Stein/eigenfunction curve-list reproof',new_owner='Abasheva–Deev arXiv v1, sections2.2.2/2.2.6',conclusion='Nonlinear primary has exactly C=(w=0); nonresonant diagonal primary has exactly its two axes.',map='The diagonal relation alpha^a beta^b=1 would descend the nonconstant meromorphic monomial z^a w^b, so a(P)=0 meets section2.2.6 nonresonance. The nonlinear normal form is (beta^r z+w^r,beta w), including r=1, exactly section2.2.2. The separate automorphism assertion in section2.2.5 is not used.')]
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],maps)
deps=[dict(consumer='UN40',input='UN17 and P327',map='Same proper family and same finite primary covering; all arbitrary multiplicities and point blowdowns retained.',status='Both owners precede section10. The full bounded P327 guard is included. Local mathematical order complete.'),dict(consumer='UN46 onward',input='UN40 and the existing later construction chain',map='The next unit receives a stable open heading. Its complete rewrite, consolidation and placement are the continuing section10 task.',status='Open; no all-25-class or final placement completion is claimed for that following unit.')]
tsv('_dependencies.tsv',['consumer','input','map','status'],deps)

eventfields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
events=[]
for owner,key,where,outcome,suffix in [
('cdp:st:C.2.UN.40','UN40','subsec:II:hopf-axis-adjacency','Read the complete original and receiving statement and every proof step. Preserved full arbitrary central multiplicities, arbitrary point-blowdown map, arbitrary chosen finite unramified primary cover and both exact adjacency conclusions. Compared UN17 on the same f and all m_i; retained the explicit integral HA3 elimination. The class pushforward sends every dominating prime to its image and each exceptional prime to zero, preserves principal divisors and the canonical class, and proves B_i reduced by generic SNC uniqueness. P327 applies to the given p, not only a constructed central cover. Freshly opened Abasheva–Deev v1 pp4–5 supplies the precise axis lists; the diagonal monomial map proves the nonresonance hypothesis. Retained the full character injection through Hartogs of a trivializing eigenfunction and its inverse, all HA5 integral classes, independence/infinite order, missing-axis coefficient contradiction, nonlinear HA6 coefficient and the neighbouring noncontractible elliptic-axis comparison. All six formula payloads are unchanged. No statement hypothesis or conclusion changes.','_replacement.tex'),
('lem:II:central-primary-hopf-cover','P327','bounded P327 guard in subsec:II:hopf-component-boundaries','Read the complete original and receiving P327 statement/proof. The full central contraction construction, normal core, Hartogs extensions and inverses, fixed origin, log absolute determinant homomorphism, excluded inversion and free quotient map remain byte-identical. The field statement now explicitly covers every finite connected unramified p:Pprime->H. The same symmetric-function polynomial is formed on the local sheets of this p; permutation invariance glues its coefficients and surjectivity makes pullback injective. Taking p=pi recovers the unchanged central-cover conclusion. The full UN40 receiving application uses Pprime=P and H=H_i. Freshly reopened source pp3/5 and p8 confirm the unchanged normal-form/finite-cover input scope.','_P327_replacement.tex')]:
    events.append(dict(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=outcome+' Exposed editorial comparison only; no independent proof or computational execution credit. All permanent identities preserved; no refined P4R.13/P4.40 use encountered. Final integrated PDF reading open.',event_id='publish:c3:conductor14:'+key,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+prefix+suffix,source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor14:axis-adjacency',publish_input_file='',publish_input_row='',date_utc=now,where=where))
tsv('_CHECK_EVENTS.tsv',eventfields,events)

statuses=[]
for c in [f'D{i:02}' for i in range(1,26)]+['structure']:
    status='done';reason='Complete original and receiving adjacency statements/proofs compared; every local instance found has its exact defect row and owner map.'
    if c in ['D10','D16']:reason='Prior done status preserved: hidden statement records and every permanent label/target remain; the theorem has its mathematical title.'
    elif c=='D12':reason='The repeated canonical generator uses UN17; the finite-sheet field proof has its complete general owner at P327 and the exact given-p application.'
    elif c in ['D14','structure']:reason='The adjacency theorem has its own first subsection, after all of its inputs and before every cycle/tree consumer. Its local final placement and owner order are complete. The following construction unit remains explicitly open.'
    elif c=='D15':reason='This is a body unit with no new front-matter process claim.'
    elif c=='D17':reason='The primary curve-list reproof is replaced only after reading exact Abasheva–Deev v1 sections2.2.2/2.2.6. The integral character, class pushforward and adjacency coefficients remain proved in their required scope.'
    elif c=='D18':status='open';reason='Exact opened versions, loci and hashes are recorded. Source-wide bibliography review remains a separate gate.'
    elif c=='D19':reason='Six inherited equations now use the section counter with every payload, permanent target and label unchanged; complete old-tag map supplied.'
    elif c=='D23':status='open';reason='Source spacing and article corrected; final integrated page inspection remains open.'
    elif c=='D24':reason='The section identity is preserved; no front-matter promise is changed.'
    elif c=='D25':reason='Every unchanged and rewritten inference was compared. The arbitrary primary p meets the exact broadened P327 clause, and a(P)=0 supplies the nonresonance required by the opened primary source. All six coefficients and both ratio conclusions remain unchanged.'
    statuses.append(dict(unit='subsec:II:hopf-axis-adjacency',title='Hopf axes and canonical-order ratios',criterion=c,status=status,reason=reason))
    statuses.append(dict(unit='subsec:II:marked-cycle-tree-constructions',title='Marked cycle and tree constructions',criterion=c,status='done' if c in ['D10','D16'] else 'open',reason='Carries the existing open section10 work beginning at UN46; the complete cycle/tree rewrite has not yet been admitted. D10/D16 remain done.'))
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],statuses)

sources=[]
for filename,url,version,locus,paraphrase in [
('AbashevaDeev2023_v1.pdf','https://arxiv.org/pdf/2303.10764v1','arXiv:2303.10764v1, 19 March 2023','Complete printed pp.4–5 and p.8 reopened; used section2.2.2 p4, section2.2.6 p5 and section2.3.1 p8','The nonlinear normal form has only its axis curve. A diagonal primary with no positive-power resonance has exactly its two axis curves. Every secondary Hopf surface is a free finite quotient of a primary. The p4 section2.2.5 automorphism assertion is not used.'),
('Khaled2024_v2.pdf','https://arxiv.org/pdf/2310.05265v2','arXiv:2310.05265v2, 4 December 2023','Complete normal-form list (1), printed p.3; complete Theorem2.1 and Remark2.2, printed p.5 reopened','The normal forms include resonant diagonal typeIII, nonlinear typeIIa with r>=2, and Jordan typeIIb with r=1. The theorem supplies the primary classification and full centralizers; it recalls that classification rather than printing its original proof.')]:
    p=Path('/tmp/S6_SERIES_PUBLISH_c3_conductor_primary')/filename
    sources.append(dict(source_id=filename[:-4],url=url,version=version,exact_locus=locus,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,own_paraphrase=paraphrase,reader='continuation3 conductor; exact primary loci personally opened/read before the citation replacement',date_utc=now,storage='Temporary primary cache outside checkpoint; no source PDF, extract or page image is copied into deliverable.'))
tsv('_sources.tsv',['source_id','url','version','exact_locus','sha256','bytes','own_paraphrase','reader','date_utc','storage'],sources)

comparison=r'''# Package 14: Hopf-axis adjacency and the arbitrary finite-cover field map

## Full review and boundary

The complete original UN40 statement/proof and the complete receiving statement/proof were read and compared, including the unchanged integral divisor and neighbour calculations. The full original/receiving P327 statement/proof were also read. This is exposed editorial rereading. The main fragment begins with the existing section10 heading and ends immediately before UN46. Both section10 identities and all UN40 identities remain. It creates the actual subsection `subsec:II:hopf-axis-adjacency`, then a following open heading `subsec:II:marked-cycle-tree-constructions` for UN46 onward. The exact main original and P327 original each match current source once. No central source was edited.

The package contains 20 per-instance defects, two exposed proof events, three exact owner maps, two dependency rows, six old-tag mappings, two primary-source records and 52 criterion rows for one reviewed unit and one following open unit. All six equation payloads are unchanged, and all old label/target multiplicities are preserved. No refined P4R.13/P4.40 use occurs.

## Canonical orders and point blowdowns

UN40 retains its full arbitrary-multiplicity SNC domain, arbitrary sequence of point blowdowns to a Hopf minimal surface of algebraic dimension zero, and arbitrary chosen finite unramified primary cover p:P→H_i. Its exact diagonal equality and nonlinear strict ratio drop are unchanged.

The repeated rank-one canonical-generator construction now applies UN17 to the same f and the same full fibre. The smooth component has identity normalization/resolution and intrinsic conductor zero. CA3/CA4 therefore give the same adjunction and principal-normal relations. The short integral calculation remains explicitly in UN40: multiply by m_i, substitute m_iE_i|E_i=−Σm_jD_ij, and add m_iD_i. This gives every unchanged coefficient of HA3.

The complete divisor-class pushforward is retained. Every prime dominating a curve maps to that curve, each exceptional prime maps to zero, and principal divisors use the same meromorphic function. Pullback of a meromorphic canonical form has only exceptional Jacobian discrepancy, so its class pushes to K_Hi. Generic isomorphism and the two-branch SNC locus prove that the pushed boundary B_i is reduced. This justifies HA4 on the same minimal surface after every allowed point blowup.

## Exact primary cover and published curve lists

P327 originally stated the algebraic meromorphic-field inclusion only for its constructed central primary cover, although its proof uses just the local sheets of a finite unramified cover. The bounded guard now states that conclusion for each finite connected unramified p:P′→H and uses p throughout the same symmetric-polynomial proof. Its coefficients glue because they are invariant under every local sheet permutation; no Galois assumption is needed. Surjectivity gives injectivity of pullback, and the polynomial gives algebraicity. The entire central-cover construction and its conclusion remain unchanged. Taking p=π is the old central instance.

UN40 applies this exact clause with P′=P and H=H_i, preserving its chosen p. Thus a(P)=a(H_i)=0. On a diagonal primary, a relation α^aβ^b=1 for a nonzero integer pair would descend the nonconstant meromorphic monomial z^aw^b. This proves the nonresonance required by Abasheva–Deev v1, section2.2.6 p.5, which gives precisely the two axes. Its section2.2.2 p.4 gives the unique nonlinear axis. Both complete pages were reopened before replacing the repeated Remmert–Stein/eigenfunction proof. Section2.2.5's broader automorphism assertion is not used. Khaled v2's full normal-form list p.3 and Theorem2.1/Remark2.2 p.5 were reopened, including nonlinear exponent one. The finite-primary-cover paragraph in Abasheva–Deev section2.3.1 p.8 was reopened as well.

## Integral characters and adjacency

The short character calculation remains a proof. If the line associated to a multiplier λ is trivial, a nowhere-zero holomorphic eigenfunction and its inverse extend by Hartogs, and evaluation at zero forces λ=1. The coordinate functions and Jacobian then give HA5. The two diagonal curve classes are integrally independent because a relation, including a torsion relation after a positive power, would give the excluded meromorphic monomial. The nonlinear axis class has infinite order because |β|<1.

The finite unramified inverse image of B_i is reduced. An absent diagonal axis would have coefficient −m_i on one side of HA4 and zero on the other. Both axes therefore occur and coefficient comparison gives HA1. An absent nonlinear axis would give −m_i(r+1)C=0; its infinite order excludes this. Its actual coefficient is one, and HA6 gives the same −m_i r coefficient and HA2 ratio decrease. The original case in which one boundary has more than one component in its finite inverse image remains covered explicitly.

Finally, the shared strict axis is elliptic and cannot be exceptional for a neighbouring point-blowdown map, whose exceptional curves are rational. On an algebraic-dimension-zero Hopf neighbour it is therefore a minimal axis. The diagonal equality contradicts the nonlinear strict drop, and the nonlinear neighbour gives the opposite strict inequality. This preserves every asserted adjacency restriction, with all maps from the original components retained.

## Status

The adjacency unit's local order and restructuring are complete: its inputs precede it and its cycle/tree consumers follow it. D18 remains open for the source-wide bibliography gate, and D23 for final integrated-page reading. D10/D16 remain done. The following UN46-onward unit carries every inherited open criterion except D10/D16; no completion is claimed there. No manifest, seal, receipt, inventory difference or census refresh was made.
'''
(out/(prefix+'_comparison.md')).write_text(comparison,newline='\n')
report=f'14 READY: {len(rows)} defects; {len(events)} exposed full-proof events; six unchanged formula payloads; one reviewed adjacency unit and following open unit; exact main/P327 guards match once; all old labels/targets preserved; no new permanent tag.\n'
for p in out.glob(prefix+'*'):
    if p.is_file():assert b'\r' not in p.read_bytes()
(root/'code'/('S6_SERIES_PUBLISH_c3_conductor_14.out')).write_text(report,newline='\n')
print(report,end='')
