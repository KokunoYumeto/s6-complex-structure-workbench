from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *

name='elliptic_contraction'
prefix='S6_SERIES_PUBLISH_sec07_'+name
path=OUT/('S6_SERIES_PUBLISH_II_sec07_'+name+'.tex')
fragment=path.read_text()
guardpath=OUT/(prefix+'_guards.json')
guards=json.loads(guardpath.read_text())
pkg=Package(name,'night:P4.54')
old=r'''The root $g_u=\exp((\log u)/m)g$ and the identity
inclusion $g_u^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$
give zero intersection pairing on its local reduced levels.
For each pair $(w;D)$ just obtained, apply
\cref{lem:II:weighted-initial-monodromy} with
$D_\epsilon(x,y,z)=(\epsilon^{w_x}x,
\epsilon^{w_y}y,\epsilon^{w_z}z)$,
$G_\epsilon=\epsilon^{-D}g\circ D_\epsilon$ and $c=1$.
Every compact pairing on the leading fibre is preserved
by transport to $g=\epsilon^D$, and hence is zero.'''
new=r'''Choose a holomorphic logarithm of $u$ and put
$g_u=\exp((\log u)/m)g$ and
$\alpha=\exp((\log u(0))/m)\ne0$.
The identity inclusion
$g_u^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$
is the full-fibre map in \cref{night:P4.51}; its proof
gives zero intersection pairing on these local $g_u$-levels.
For each pair $(w;D)$ just obtained, the weighted initial
polynomial of $g_u$ is $\alpha P$. Apply
\cref{lem:II:weighted-initial-monodromy} to $g_u$, with
$D_\epsilon(x,y,z)=(\epsilon^{w_x}x,
\epsilon^{w_y}y,\epsilon^{w_z}z)$,
$G_\epsilon=\epsilon^{-D}g_u\circ D_\epsilon$ and
$c=\alpha$. Thus the initial level is
$\{\alpha P=\alpha\}=\{P=1\}$, and every compact
pairing there transports into
$g_u=\alpha\epsilon^D$, inside the full fibre
$\Phi=(\alpha\epsilon^D)^m$. Its pairing is zero.'''
assert fragment.count(old)==1
fragment=fragment.replace(old,new)
pkg.record('D12,D20,D25','night:P4.54',old,new,
 'Apply the existing compact weighted transport directly to the exact root of the full fibre function. The initial scalar alpha and target value agree, so no intervening unit-invariance identification is omitted.')
old9=r'''$G_\epsilon$ transport then puts the same compact
intersection class in a local reduced $g$-level, whose
pairing is zero. This is a contradiction.'''
new9=r'''$G_\epsilon$ transport then puts the same compact
intersection class in $g_u=\alpha\epsilon^9$, inside
$\Phi=(\alpha\epsilon^9)^m$. Its zero pairing gives
the contradiction.'''
assert fragment.count(old9)==1
fragment=fragment.replace(old9,new9)
pkg.record('D20,D25','night:P4.54',old9,new9,
 'Name the identical root-function level and its full-fibre inclusion in the isolated degree-nine sphere application.')
for g in guards:
    if old in g['new']:
        g['new']=g['new'].replace(old,new).replace(old9,new9)
        g['reason']+=' Weighted comparison is applied directly to g_u with initial alpha P and c=alpha.'
path.write_text(fragment,newline='\n')

main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
old53=r'''Its root $g_u=\exp((\log u)/m)g$, the function denoted
$h$ there, and the inclusion
$g_u^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$
therefore give zero intersection pairing on local $g$-levels.
Apply the first clause of
\cref{lem:II:weighted-initial-monodromy} with
\[
 D_\epsilon(x,y,z)=(\epsilon x,\epsilon^2y,\epsilon z),
 \qquad G_\epsilon=\epsilon^{-5}g\circ D_\epsilon,
 \qquad c=1.
\]
Since $G_\epsilon\to P_5$ with all derivatives on compact
sets, every compact intersection calculation on $P_5=1$
maps to a local $g=\epsilon^5$ level. Its intersection
form is consequently zero.'''
new53=r'''Choose a holomorphic logarithm of $u$, and put
$g_u=\exp((\log u)/m)g$, the function denoted $h$ there,
and $\alpha=\exp((\log u(0))/m)\ne0$.
The proof of \cref{night:P4.51}, with the identity inclusion
$g_u^{-1}(\delta)\hookrightarrow\Phi^{-1}(\delta^m)$,
gives zero intersection pairing on these local $g_u$-levels.
The weighted initial polynomial of $g_u$ is $\alpha P_5$.
Apply the first clause of
\cref{lem:II:weighted-initial-monodromy} to $g_u$, with
\[
 D_\epsilon(x,y,z)=(\epsilon x,\epsilon^2y,\epsilon z),
 \qquad G_\epsilon=\epsilon^{-5}g_u\circ D_\epsilon,
 \qquad c=\alpha.
\]
The functions $G_\epsilon$ converge with all derivatives
on compact sets to $\alpha P_5$. The initial level is
$\{\alpha P_5=\alpha\}=\{P_5=1\}$, so every compact
intersection calculation there transports into
$g_u=\alpha\epsilon^5$, inside the full fibre
$\Phi=(\alpha\epsilon^5)^m$. Its pairing is zero.'''
assert main.count(old53)==1
guards.append(dict(key='P453 full-fibre weighted transport',old=old53,new=new53,
 reason='After the complete original/current and receiving P453 comparison, make its existing unit-flow application unnecessary by transporting directly into g_u=alpha epsilon^5 and then the identical full Phi-fibre. P452 already explicitly invokes the proved P451 unit flow and remains unchanged.'))
pkg.record('D12,D20,D25','night:P4.53',old53,new53,
 'The old proposition remains proved by the complete P451 unit flow, already explicitly invoked at P452. This bounded clarification supplies the direct root-function transport and full-fibre inclusion, without alleging an erroneous P452 theorem.')
(OUT/'S6_SERIES_PUBLISH_II_sec07_elliptic_contraction_P453.tex').write_text(block(main,'night:P4.53').replace(old53,new53)+'\n',newline='\n')
guardpath.write_text(json.dumps(guards,ensure_ascii=False,indent=2)+'\n',newline='\n')
dp=OUT/(prefix+'_defects.tsv')
with dp.open(newline='') as f:
    rr=csv.DictReader(f,delimiter='\t');fields=rr.fieldnames;rows=list(rr)
for r in pkg.rows:
    r['change_id']=f'II-C3-S07-ELLIPTIC_CONTRACTION-{len(rows)+1:03}'
    rows.append(r)
with dp.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(f'Corrected P454 and bounded P453 root-function applications: {len(guards)} guards, {len(rows)} defect rows.')
