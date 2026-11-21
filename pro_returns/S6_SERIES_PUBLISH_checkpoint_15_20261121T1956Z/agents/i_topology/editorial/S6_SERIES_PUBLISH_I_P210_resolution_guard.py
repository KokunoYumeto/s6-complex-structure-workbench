from pathlib import Path
import hashlib,json,datetime,csv
base=Path('/workspace/scratch/653608133b22'); out=base/'work/agents/i_topology'; p=base/'work/S6_SERIES_PUBLISH_I.tex';s=p.read_text()
i=s.index('\\label{night:P2.10}');a=s.index('\\item At a smooth point of $F_\\infty$',i);b=s.index('\\end{enumerate}',a)
old=s[a:b]
new=r'''\item At a smooth point of $F_\infty$ the first neck is $zw=rq$; at its node it is $zw=rxy$, with $q=xy$. The ideal of one globally distinguished central component is locally $(z,r)$. Because the two global components are distinct, this is a global coherent ideal. Blow it up. At the node its two charts are
\begin{align*}
 r=za,\quad w=axy;&\qquad (z,a,x,y)\text{ are smooth coordinates},\\
 z=rb,\quad bw=xy;&\qquad (r,b,w,x,y)\text{ with the displayed relation}.
\end{align*}
The remaining singularity is an ordinary threefold node times the parameter disc. Its singular section does not meet the first chart. Resolve $(b,y)$ in the second chart. Its two charts are
\begin{align*}
 b=yk,\quad x=kw;&\qquad (r,y,k,w),\\
 y=bj,\quad w=jx;&\qquad (r,b,j,x).
\end{align*}
They are smooth, with transition $j=k^{-1}$ and $(b,x)=k(y,w)$. Off the singular section the ideal is invertible, so this proper small resolution glues to the identity. The analogous blowup charts at smooth points of $F_\infty$ are already smooth. The resulting total space is smooth, and its parameter central divisor is reduced NC: in the first chart $r=za$, and in both small-resolution charts $r$ is a coordinate. Parameter torsion freeness proves flatness.

\item We identify the compactified generic fibre, including its chosen marked cusp. For fixed $r\ne0$ the first blowup is an isomorphism. Put $W=rw$ and $u=r^2$; the first neck becomes $zW=u xy$. On its dense torus use $(x,z,q)$, with $y=q/x$ and $W=uq/z$. The four affine monomials have exponents
\[
 (1,0,0),\quad(-1,0,1),\quad(0,1,0),\quad(0,-1,1).
\]
The dual cone is $0\le\alpha,\beta\le\gamma$, the cone over the unit square at height one. The resolution of $(z,y)$, equal to that of $(b,y)$ when $r$ is a unit, divides it along $\alpha+\beta=\gamma$: the chart character $k=z/(ry)$ has valuation $\alpha+\beta-\gamma$. Its two cones, over the triangles with common edge $[e_1,e_2]$, are unimodular. The exact comparison with the coordinates $(X,Y,Z,V)$ in the node $XY=uZV$ of Theorem~\ref{push:src:A.1.2} is
\[
 (X,Y,Z,V)=(z,rw,x,y).
\]
In its first resolution chart the parameters are $(V,Y/u,A)=(y,w/r,rk)$, and in its second they are $(X,Z,B)=(rb,x,j/r)$. These give respectively
\[
 (X,Y,Z,V)=(rk y,rw,kw,y),\qquad
 (X,Y,Z,V)=(rb,rjx,x,bj),
\]
and $AB=kj=1$ on the overlap. Thus both chart maps and their transition agree with the selected resolution of Theorem~\ref{push:src:A.1.2}. In the two charts, $q=kyw$ and $q=bxj$, respectively. The Tate and linearization periods shift the two marked lattice directions by one; their unit factors act holomorphically on these charts. This is the chosen marked triangular filling supplied by Engel's general construction in \cite[Proposition~2.8, pp.~6--7]{Engel2026}. Together with the quotient comparison, the displayed map identifies the entire compact generic fibre with $X(u)$.

\item The involution $r\mapsto-r$ fixes the $Y_0$ fibre coordinate and negates the $Y_1$ coordinate. It preserves both equations and the global component ideal. In the nodal blowup chart it acts as $(b,w,x,y,r)\mapsto(-b,-w,x,y,-r)$ and preserves $(b,y)$. Its lifts on the two resolution charts are
\[
 (r,y,k,w)\longmapsto(-r,y,-k,-w),\qquad
 (r,b,j,x)\longmapsto(-r,-b,-j,x).
\]
The transition $j=k^{-1}$ intertwines these maps. Its finite quotient is proper and Hausdorff over $u=r^2$. Its invariant local rings are torsion free over the discrete valuation ring $\C\{u\}$ and hence flat. Away from zero the involution exchanges the two roots of $u$, while $W=rw$ and the $Y_0$ coordinate are invariant. The displayed marked comparison therefore identifies the quotient fibre with one copy of $X(u)$. This is a filling in the original parameter.
'''
assert s.count(old)==1
patch={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'patches':[{'id':'I-topology-P210-selected-resolution','old':old,'new':new,'reason':'Correct the selected-diagonal identification in proof Steps6–8; retain the theorem statement and prove the exact marked node map, both chart transitions and involution lift.','statement_ids':['night:P2.10']} ]}
(out/'editorial/S6_SERIES_PUBLISH_I_P210_resolution_guarded.json').write_text(json.dumps(patch,indent=2)+'\n')
(out/'editorial/S6_SERIES_PUBLISH_I_P210_resolution_old.tex').write_text(old)
(out/'editorial/S6_SERIES_PUBLISH_I_P210_resolution_new.tex').write_text(new)
orig=(base/'source/S6_SERIES_GRIND_I.tex').read_text();oi=orig.index('\\label{night:P2.10}');oe=orig.index('\\end{proof}',oi)
assert 'Resolve $(b,x)$' in orig[oi:oe] and 'divides it along $a=b$' in orig[oi:oe]
record={'error_event_id':'ce:publish-itopology-P210-selected-diagonal-error-20261121','statement_id':'night:P2.10','scope':'Proof Step7 identification of the selected marked resolution, propagated to Steps6 and8','original_source_contains_same_step':True,'original_source_sha256':hashlib.sha256((base/'source/S6_SERIES_GRIND_I.tex').read_bytes()).hexdigest(),'exposed_current_source_sha256':patch['input_sha256'],'old_claim':'The (b,x), generically (z,x), resolution along the main diagonal is the selected marked cusp used for X(u).','exact_comparison':'(X,Y,Z,V,u)=(z,rw,x,y,r^2) to the A1.2 node. The selected A1.2 edge is [e1,e2], requiring (z,y), hence (b,y), with valuation alpha+beta-gamma.','correction':'Use b=yk,x=kw and y=bj,w=jx; j=k^-1,(b,x)=k(y,w). The two maps to A1.2 have parameters (y,w/r,rk) and (rb,x,j/r). The involution lifts as written in the guard.','comparison_between_old_and_new_resolutions':'Both map properly to bw=xy and are isomorphisms off its node. The common blowup has exceptional quadric [b:x:y:w] with bw=xy, parametrized by [u0v0:u0v1:u1v0:u1v1]; its two projections to the row/column projective factors give the two small resolutions and contract opposite rulings. No nonisomorphism assertion about the compact threefolds is made.','theorem_statement_unchanged':True,'refined_statement_id':None,'literature_scope':'Engel Proposition2.8 permits any periodic unimodular triangular tiling. The required chosen edge is Paper I’s marked A1.2 choice, not a purported uniquely prescribed Engel anti-diagonal.','computation':'code/S6_SERIES_PUBLISH_I_P210_resolution_exact.py','output':'output/S6_SERIES_PUBLISH_I_P210_resolution_exact.json','credit':'Exposed correction and exact computation; no before-proof targeted check credit.'}
(out/'S6_SERIES_PUBLISH_I_P210_resolution_ERROR_EVENT.json').write_text(json.dumps(record,indent=2)+'\n')
who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH topology-check agent'
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
rows=[]
for typ,outcome,tail,file in [('used and rechecked in this run','Full P2.10 proof and F receiving scope reread; original/current Step7 selects the opposite marked edge. Corrected Steps6–8 compared through the explicit node map, transitions and finite involution; theorem statement unchanged.','reread','S6_SERIES_PUBLISH_I_P210_resolution_comparison.md'),('computation or formal certificate','Fresh exposed exact substitutions verify both corrected resolution charts, inverse transition, A1.2 marked map, involution lifts, q-products and unimodular cone determinants. This is one scoped execution, not an independent whole-theorem check.','computation','output/S6_SERIES_PUBLISH_I_P210_resolution_exact.json')]:
 rows.append(dict(zip(fields,['night:P2.10','2026-11-21',who,typ,outcome,'publish-I-topology-P210-resolution-'+tail+'-20261121','Paper I selected-resolution correction','work/agents/i_topology/'+file,'',typ,'publish-I-topology-P210-resolution-'+tail])))
with (out/'S6_SERIES_PUBLISH_I_P210_resolution_CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print('ONE_GUARD',patch['input_sha256'],'ORIGINAL_ERROR_CONFIRMED','TWO_SCOPED_ROWS')
