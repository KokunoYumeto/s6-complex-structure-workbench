"""Resolve notation and duplicate input maps after full native/cusp reading."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
root=Path(__file__).resolve().parent.parent
folder=root/'agents/continuation8_iii_integration/units/root'
lane=root/'agents/continuation8_iii_weighted_units'
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
items={}
for name,sha,prefix,count,number in [
    ('cusp_nullbordism','ae1a2201fe55540fc988b2197b2ddf5cc4ea1f970447ba3f69cdf45cb4259ece','CUSP_NULLBORDISM',42,14),
    ('full_sphere_nullity','4d1b5914254626f9ab8917f1fae410456bc3b4e20043487d84574ba8bd8ab0e3','NATIVE_SPHERE',81,28)]:
    p=folder/(name+'.tex');t=p.read_text();assert hashlib.sha256(p.read_bytes()).hexdigest()==sha
    table=lane/('S6_SERIES_PUBLISH_'+prefix+'_publication_defects.tsv')
    with table.open(newline='') as f:
        r=csv.DictReader(f,delimiter='\t');rows=list(r);assert r.fieldnames==fields
    assert len(rows)==count
    items[name]={'path':p,'old':t,'text':t,'table':table,'rows':rows,'number':number,'prefix':prefix}
def edit(name,old,new,kinds,reason,owner):
    item=items[name];t=item['text'];assert t.count(old)==1,(name,old[:100],t.count(old))
    line=t.count('\n',0,t.index(old))+1
    item['text']=t.replace(old,new,1);item['number']+=1
    prefix='CUSP' if name=='cusp_nullbordism' else 'NATIVE-SPHERE'
    for kind in kinds:
        item['rows'].append(dict(zip(fields,[f"III-C8-{prefix}-PUB-{item['number']:03}-{kind}",kind,owner,f'{name}.tex sequential line {line}','pending page concordance','root/'+name+'.tex','pending final build',old,new,reason,'whole first candidate read; bounded follow-up readback pending; global gates open'])))
    print('BOUNDED_EDIT',name,item['number'],','.join(kinds),reason)
    print('NEW_TEXT\n'+new)

name='cusp_nullbordism';owner='wb:cusp-null:thm'
edit(name,r'''The coefficient map and its inverse identify the quotient torus
with $\overline T^2=\mathbb R^2/\mathbb Z^2$.
''',r'''The quotient torus is identified with
$\overline T^2=\mathbb R^2/\mathbb Z^2$ by the inverse marked maps
\[
 \beta:[a\widehat\gamma+b\widehat u]\longmapsto[a,b],\qquad
 \beta^{-1}:[a,b]\longmapsto[a\widehat\gamma+b\widehat u].
\]
''',['D05','D20','D22'], 'Put the full marking map and inverse in the numbered input, with the same two generators and circle order.', 'wb:def:marked-cusp-nullbordism-data')
edit(name,r'''The based marking
\[
 \beta:[a\widehat\gamma+b\widehat u]\longmapsto[a,b],
 \qquad \beta^{-1}:[a,b]\longmapsto[a\widehat\gamma+b\widehat u]
\]
gives inverse torus maps carrying the two marked coordinate circles
onto the two coordinate circles. It induces inverse maps
''',r'''The inverse marking maps $\beta,\beta^{-1}$ in
Definition~\ref{wb:def:marked-cusp-nullbordism-data} carry the two
marked coordinate circles onto the two coordinate circles.
They induce inverse maps
''',['D12','D20'], 'Replace the exact repeated torus formulas by their numbered owner, retaining all induced quotient and suspension maps in this proof.',owner)
edit(name,r'''The based map $g:(X,x_0)\to(S^3,*)$ of
\eqref{wb:cusp-null:eq:g} is based null-homotopic.
''',r'''The based map $g:(X,x_0)\to(B,*)$ of
\eqref{wb:cusp-null:eq:g}, with the sphere identification
$h_3\phi:B\to S^3$ of
Definition~\ref{wb:def:marked-cusp-nullbordism-data}, is based
null-homotopic.
''',['D20','D22'], 'Keep the actual quotient target B explicit; its exact round-sphere identification and inverse already occur in Q258, so the map and its homotopy have one unambiguous domain/target.',owner)
edit(name,r'''Composing its based null-homotopy with this suspension homeomorphism
proves the first assertion.
''',r'''Write $S_\beta$ for the first suspension homeomorphism and
$H_0$ for that proved based null-homotopy. Then
$H_g(x,s)=S_\beta H_0(x,s)$ has initial map $g$, constant terminal
map and $H_g(x_0,s)=*$; its inverse transport is $S_\beta^{-1}H_g=H_0$.
This proves the first assertion.
''',['D20','D22'], 'Print the actual composed homotopy, all endpoints, fixed basepoint and inverse transport from the proved earlier angle-forgetting homotopy.',owner)
edit(name,r'''$\phi:W_\delta\to U\subset X$ and $\phi^{-1}$, where
''',r'''$\iota_U:W_\delta\to U\subset X$ and $\iota_U^{-1}$, where
''',['D20','D23'], 'The publication readback caught the newly introduced collision between target phi and the old source chart phi. Rename only the source chart to iota_U with its same inverse; no geometric map changes.',owner)
edit(name,r'''For $x_0\in U$, write $w^*=\phi^{-1}(x_0)$.
''',r'''For $x_0\in U$, write $w^*=\iota_U^{-1}(x_0)$.
''',['D20'], 'Use the renamed source-chart inverse in the arbitrary-basepoint exclusion, preserving exactly its radius inequalities.',owner)
t=items[name]['text'];start=t.index('For an explicit parametrization of its disk factor, take');end=t.index('Its spatial coordinates satisfy',start)
block=t[start:end]
new=block.replace('f(|z|^2)','f_D(|z|^2)').replace('f(s)','f_D(s)').replace('f(0)','f_D(0)').replace('so $f$','so $f_D$')
edit(name,block,new,['D20','D23'], 'Rename the scalar disk-radius factor f_D by the identity f_D=f and inverse notation f=f_D, keeping it distinct from the source map f:X to the base. Every parametrization/inverse and derivative stays identical.',owner)
edit(name,r'''$\delta^{-1}(0)=0$. This establishes the coefficient here, before
any computation for arbitrary one-copy classes.
''',r'''$\delta^{-1}(0)=0$.
''',['D08','D12','D15'], 'Remove the editorial ordering comment after the complete native even-coordinate proof; the actual dependency order is stated in the review.', 'wb:cusp_s12_carrier_homotopy:L567')

name='full_sphere_nullity';t=items[name]['text']
start=t.index('Let $d:C_6\\to(X,x_0)$ be the fixed based source homeomorphism.')
end=t.index('All smash coordinates use',start)
edit(name,t[start:end],r'''Use the same $d,\phi$ and $g_C=\phi gd$ of
Definition~\ref{wb:def:marked-cusp-nullbordism-data}, with inverse
transport $g=\phi^{-1}g_Cd^{-1}$. In homotopy groups $[g]$ denotes
$[g_C]$.
''',['D12','D20','D22'], 'Use the complete already stated Q258 source/target maps and inverses; their original repeated formulas agree exactly on each open cell and basepoint. No coordinate convention changes.', 'wb:def:native-sphere-carriers')
edit(name,r'''The former induces the Lie stable tangent frame
$(-\partial_a,\partial_b)$ with Arf invariant one, with the
''',r'''In the displayed complex chart and normal-first order, the former
induces the Lie stable tangent frame $(-\partial_a,\partial_b)$
with Arf invariant one, with the
''',['D20','D26'], 'Name the exact orientation/frame convention proved in the retained chart before applying its global sphere class; all source-framing comparison remains in that complete predecessor.', 'wb:remark:two-cusp-postcompositions')

for name,item in items.items():
    t=item['text'];assert '\r' not in t
    units.check_permanent_identifiers(item['old'],t)
    _,changes,issues,aliases=presentation.remove_manual_equation_tags(t)
    assert not changes and not issues and not aliases
    assert not presentation.unresolved_literal_equation_references(t)
    temp=item['path'].with_suffix('.tex.tmp');temp.write_text(t,encoding='utf-8',newline='\n');temp.replace(item['path'])
    with item['table'].open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(item['rows'])
    print('FINAL',name,'LINES',len(t.splitlines()),'SHA256',hashlib.sha256(t.encode()).hexdigest(),'EDITS',item['number'],'DEFECT_ROWS',len(item['rows']))
print('OLD_IDENTITIES_PRESERVED; CANONICAL_AND_SHARED_WRITES 0; NO_INDEPENDENT_CREDIT')
