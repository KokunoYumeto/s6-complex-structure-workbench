#!/usr/bin/env python3
"""Prepare the bounded UN54 application of the separately prepared P337 owner."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, re

root=Path(__file__).resolve().parents[1]
out=root/'agents/continuation3_conductor'
stem='S6_SERIES_PUBLISH_c3_conductor_P337_UN54'
current=(root/'S6_SERIES_PUBLISH_II.tex').read_text()
p=current.index(r'\label{cdp:st:C.2.UN.54}')
a=current.rfind(r'\begin{proposition}',0,p)
b=current.index(r'\end{proof}',p)+len(r'\end{proof}')
old=current[a:b]
reference=(out/'S6_SERIES_PUBLISH_c3_conductor_sec10_initial_reference.tex').read_text()
assert reference.count(old)==1
owner=(root/'agents/continuation3_provenance/occurrence_tail/S6_SERIES_PUBLISH_P337.tex').read_text()
assert r'\cref{cdp:st:D.1.7,lem:II:central-primary-hopf-cover,lem:II:hopf-curves}' in owner
rows=[]
def log(kind,oldtext,newtext,reason,statement='cdp:st:C.2.UN.54'):
    rows.append(dict(change_id=f'II-C3-HOPF337-UN54-{len(rows)+1:04d}',type=kind,statement_id=statement,old_location='Complete original UN54 statement and proof',old_page='Exact full source guard supplied; prior page omitted',new_location='UN54 first two proof items; P337 before UN38',new_page='Pending integrated final PDF',old_text=oldtext,new_text=newtext,reason=reason,review_status='Complete original UN54 and full receiving UN54/P337 read and compared; exposed editorial rereading, with no independent or execution credit.'))
def edit(s,x,y,kind,reason):
    assert s.count(x)==1
    log(kind,x,y,reason)
    return s.replace(x,y,1)

new=old
x=next(l for l in old.splitlines() if l.startswith(r'\StatementRecord'))
y=x.replace(r'\SeriesRef{cdp:st:C.2.UN.37}, ','').replace(r'\SeriesRef{cdp:st:C.2.UN.53}, ','')
y=y[:-1]+r'; \cref{lem:II:hopf-curves,lem:II:hopf-curve-restriction}}'
new=edit(new,x,y,'D12','Declares the earlier complete owners of the curve and cohomology conclusions. The later resonant-curve classification is no longer a premise of restriction nonvanishing; the other UN54 dependencies remain unchanged.')
x=old[old.index(r'\item \par\medskip\noindent\textbf{The curves and the actual restriction maps.}'):old.index(r'\par\medskip\noindent\textbf{Normalization, the graph, and its exact cycle product.}')]
y=r'''\item Apply \cref{lem:II:hopf-curves} to each component $H_v$. Its compact irreducible curves are smooth elliptic and pairwise disjoint. Hence the double curves of $S$ are elliptic and there is no triple point. Apply \cref{lem:II:hopf-curve-restriction} to the same $H_v$ to obtain $h^\bullet(H_v,\OO_{H_v})=(1,1,0)$.

\item For an endpoint $v$ of an edge $e$, apply \cref{lem:II:hopf-curve-restriction} to the inclusion of the corresponding double curve in $H_v$. At the other endpoint compose its restriction isomorphism with pullback by the specified elliptic gluing isomorphism. These are precisely the maps $r_{v,e}$ and $r_{w,e}$ of \eqref{cdp:eq:C.HR.1}, so both are nonzero.

For a secondary component, the lemma uses a finite unramified primary cover $\pi:H'\to H_v$ and a component $C'$ above this same double curve. Its restriction square commutes with $\pi^*$ and $(\pi|_{C'})^*$, both isomorphisms on $H^1(\OO)$. On the primary cover the constant deck class restricts to the cocycle with value $d$, where $\langle F^d\rangle$ is the image of this curve's fundamental group in $\langle F\rangle$; \eqref{cdp:eq:C.HR.4} proves its nonvanishing. Thus the application retains the chosen inclusions and gluing maps at every endpoint.

'''
new=edit(new,x,y,'D12','Transfers the repeated Hopf-curve proof to P248 and the full primary/secondary H1 restriction proof to P337. P337 identifies the connected lifted curve with the covering belonging to ker[pi1(C)->pi1(H)], proves the image dZ nonzero, and obtains C* with F^d acting by multiplication. The same additive deck value d and Laurent constant-coefficient argument are retained at the moved HR4 target. Finite trace and the commuting restriction square preserve both endpoint maps, including the specified elliptic gluing.')
hr4=re.search(r'\\\[.*?\\tag\{C.HR.4\}.*?\\\]',x,re.S).group()
hr4new=re.search(r'\\begin\{equation\}.*?\\label\{cdp:eq:C.HR.4\}.*?\\end\{equation\}',owner,re.S).group()
log('D19',hr4,hr4new,'Transfers C.HR.4 to its complete common proof at P337, using the section equation counter with the same formula, label and permanent target 00N3. The later reference remains an equation reference to this owner.','cdp:eq:C.HR.4')

assert current.count(old)==1
for s in [old,new,owner]:
    assert Counter(re.findall(r'\\begin\{([^}]+)\}',s))==Counter(re.findall(r'\\end\{([^}]+)\}',s))
for kind in ['label','hypertarget']:
    pattern=r'\\'+kind+r'\{([^}]+)\}'
    before=Counter(re.findall(pattern,old))
    after=Counter(re.findall(pattern,new+owner))
    assert all(after[k]==v for k,v in before.items())
    assert all(v==1 for v in after.values())
assert r'\label{cdp:eq:C.HR.4}' not in new
assert not re.search(r'night:P4R\.13|night:P4\.40|\r',new+owner)

def tsv(suffix,fields,data):
    with (out/(stem+suffix)).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
        w.writeheader();w.writerows(data)
for suffix,text in [('_input.tex',old),('_replacement.tex',new),('_P337_receiving.tex',owner)]:
    (out/(stem+suffix)).write_text(text,newline='\n')
with (root/'S6_SERIES_PUBLISH_defects_II.tsv').open() as f:fields=next(csv.reader(f,delimiter='\t'))
tsv('_defects.tsv',fields,rows)
tsv('_remote_repairs.tsv',['statement_id','old_text','new_text','reason'],[dict(statement_id='cdp:st:C.2.UN.54',old_text=old,new_text=new,reason='Admit atomically with provenance P337: the complete UN54 guard removes only the two transferred introductory arguments and updates their input declaration. Every later graph, coherent-dimension, residue, order-minimum and realization argument remains byte-identical. HR4 moves to P337.')])
tsv('_equations.tsv',['old_tag','target_label','statement_id'],[dict(old_tag='C.HR.4',target_label='cdp:eq:C.HR.4',statement_id='lem:II:hopf-curve-restriction')])
tsv('_owner_transfers.tsv',['old_owner','new_owner','conclusion','map'],[
    dict(old_owner='UN54 first curve paragraph',new_owner='P248',conclusion='Every double curve is smooth elliptic and the support has no triple points.',map='Apply to each original Hopf component H_v; pairwise disjointness of its irreducible compact curves excludes three-component incidence.'),
    dict(old_owner='UN54 primary/secondary restriction paragraphs and HR4',new_owner='P337',conclusion='Each given r_v,e is nonzero between one-dimensional complex spaces; h^bullet(H_v,O)=(1,1,0).',map='Apply to the exact inclusion C_e->H_v at one endpoint and compose the other restriction with pullback by its stated gluing isomorphism. For secondary H_v, use pi:Hprime->H_v and a chosen component Cprime above that same curve; the square commutes with the two trace-injective one-dimensional pullbacks. The primary image subgroup <F^d> and deck cocycle d are those of this curve inclusion.')])
tsv('_dependencies.tsv',['consumer','input','map','status'],[dict(consumer='UN54, with UN18/UN41/UN42 handled by their owners',input='P337 after P327 and before UN38; earlier P248 and D1.7',map='All shared owner premises precede P337. UN54 applies its primary and secondary clauses to the exact component inclusions and gluing maps.',status='Bounded common-owner transfer complete. The entire UN54 unit remains open for its continuing all-class rewrite and final placement.')])

now=datetime.now(timezone.utc).isoformat()
events=[]
for statement,key,suffix,outcome in [
    ('cdp:st:C.2.UN.54','UN54','_replacement.tex','Read the complete original UN54 statement and every proof paragraph, then the complete receiving statement/proof. Compared the exact P248 and P337 maps at both endpoints. All graph elimination, semicontinuity on the full reduced fibre, fundamental-group quotient, weighted cycle ratio, coherent dimensions, dual residue vector, canonical-order minimum and algebraic-dimension-zero realization paragraphs remain unchanged. The original later UN53 curve-list premise is removed only from the transferred restriction argument; the covering-subgroup proof establishes the same lifted C* and deck value d without it. HR4 is transferred with its original label and tag.'),
    ('lem:II:hopf-curve-restriction','P337','_P337_receiving.tex','Read the complete receiving P337 statement/proof and compared it with the entire original UN54. Also read the full current D1.7, P248 and P327 statement/proof inputs. Freshly opened Khaled arXiv v2 p18, complete section4.2 and Remark4.5, verifying its explicit Lie-group isomorphism and differentiating zeta=exp(t) to the additive deck basis. Freshly read Kato Theorem9 and full proof pp232-233 in the primary PDF; its circle bundle and finite sphere quotient give the stated rational Betti data, and the primary oriented sphere case gives free integral groups. Checked the image subgroup dZ, rank-one covering kernel, C* parameter, deck multiplication, Laurent constant coefficient, inversion sign and complete secondary trace square. This is an exposed receiving proof comparison of provenance work, not a second independent proof.')]:
    events.append(dict(statement_id=statement,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 conductor agent',type='used and rechecked in this run',outcome=outcome+' No computational execution credit. Final integrated page reading remains open.',event_id='publish:c3:conductor:P337UN54:'+key,phase='publication editorial comparison',source_file='agents/continuation3_conductor/'+stem+suffix,source_row='',source_event_type='used and rechecked in this run',evidence_group='publish:c3:conductor:P337UN54',publish_input_file='',publish_input_row='',date_utc=now,where='Bounded P337 common-owner transfer and complete UN54 receiving guard'))
tsv('_CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where'],events)
statuses=[dict(unit='subsec:II:marked-cycle-tree-constructions',title='Marked cycle and tree constructions, including UN54',criterion=c,status='done' if c in ['D10','D16'] else 'open',reason='D10/D16 prior done status retained. This bounded guard completes only the exact Hopf cohomology proof transfer; the subsection all-class rewrite and final ordering continue in the section10 packages.') for c in [f'D{i:02}' for i in range(1,26)]+['structure']]
tsv('_unit_status.tsv',['unit','title','criterion','status','reason'],statuses)
comparison='''# P337 and the bounded UN54 application — READY

Admit this complete UN54 guard atomically with provenance's P337 insertion. The main source is untouched. Provenance owns the new-owner insertion defects and primary-source records; this package supplies three application/transfer rows, two exposed receiving events, the HR4 mapping and the complete old/new UN54 text.

The complete original and receiving UN54 proofs were read. Only the initial curve and restriction arguments and their input declaration change. P248 applies to each same Hopf component. P337 applies to each same double-curve inclusion; the opposite endpoint includes the specified elliptic gluing pullback. For a secondary component the finite primary cover, selected lifted curve, both trace maps and naturality square remain explicit. The primary image subgroup is generated by F^d, and its constant deck cocycle has value d. C.HR.4 keeps its original target 00N3 at the new complete owner. All later graph, residue, canonical-order and realization arguments are byte-identical.

The entire P337 receiving proof was compared with the original UN54. D1.7, P248 and P327 were read in full. Khaled v2 section4.2 and Remark4.5 p.18 were freshly opened and read: the source explicitly gives a Lie group isomorphism from characters to Picard, so its differential gives the stated basis. Kato's complete Theorem9 and proof pp.232–233 were freshly read in the primary PDF. The new covering-subgroup argument proves the C* domain directly, removes the former forward UN53 premise and retains the Laurent obstruction and the inversion sign. No independent or computational execution credit is claimed.

The exact full old guard matches once. All original statement/equation labels and permanent targets occur with the same multiplicity in the combined UN54/P337 receiving text. The full UN54 all-class rewrite remains open, with D10/D16 retained done. No final PDF reading or whole-section completion is claimed.
'''
(out/(stem+'_comparison.md')).write_text(comparison,newline='\n')
report=f'P337/UN54 READY: {len(rows)} defects, {len(events)} exposed events, full UN54 exact guard, one moved equation, all original identities preserved; enclosing unit remains open.\n'
(root/'code'/('S6_SERIES_PUBLISH_c3_conductor_P337_UN54.out')).write_text(report,newline='\n')
print(report,end='')
