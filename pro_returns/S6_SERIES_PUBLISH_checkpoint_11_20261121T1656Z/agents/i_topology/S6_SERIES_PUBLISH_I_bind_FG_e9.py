from pathlib import Path
import hashlib,json,datetime,csv,difflib
R=Path('/workspace/scratch/653608133b22');D=R/'work/agents/i_topology';E=D/'editorial';S=E/'S6_SERIES_PUBLISH_I_final_FG_e9_source_snapshot.tex';C=E/'S6_SERIES_PUBLISH_I_candidate11_source_snapshot.tex';B=E/'S6_SERIES_PUBLISH_I_boundary_batch7_before.tex';s=S.read_text();c=C.read_text();b=B.read_text();sha=lambda t:hashlib.sha256(t.encode()).hexdigest();now=datetime.datetime.now(datetime.timezone.utc).isoformat();assert sha(s)=='e9a12c1a9f1c08b260c3a35dd1a23a15e8894d15cdd42333516e17cdd32061ae'
def block(t,lab):
 p=t.index('\\label{'+lab+'}');a=t.rfind('\\begin{',0,p);e=t.index('\\end{proof}',p)+len('\\end{proof}');return t[a:e]
def head(t,lab):
 p=t.index('\\label{'+lab+'}');a=t.rfind('\\begin{maintheorem}',0,p);e=t.index('\\end{maintheorem}',p)+len('\\end{maintheorem}');return t[a:e]
def outline(t,x):
 a=t.index('\\hypertarget{outline-I-'+x+'}');e=t.index('\\end{enumerate}',a)+len('\\end{enumerate}');return t[a:e]
F=['night:P2.2','night:P2.3','night:P2.4','night:P2.5','night:P2.6','night:P2.7','night:P2.9','night:P2.10','night:P2.11'];G=['push:src:D.1.3','push:src:D.2.1','push:src:D.2.3','push:src:D.3.1','push:src:D.3.2'];records=[]
for lab in F+G:
 bb,cc,nn=block(b,lab),block(c,lab),block(s,lab)
 records.append(dict(statement_id=lab,current_complete_statement_and_proof_actually_read=True,current_block_sha256=sha(nn),retained_batch7_block_sha256=sha(bb),candidate11_block_sha256=sha(cc),changed_since_retained_batch7=bb!=nn,changed_since_candidate11=cc!=nn,retained_batch7_complete_block=bb,candidate11_complete_block=cc,current_complete_block=nn,retained_batch7_to_current_diff='\n'.join(difflib.unified_diff(bb.splitlines(),nn.splitlines(),fromfile='retained3b272246',tofile='e9a12c1a',n=2))))
notes=r'''# F/G final applied binding at e9a12c1a

## Scope and evidence continuity

The complete current Theorems F and G and all12 outline items were read at sourceSHAe9a12c1a9f1c08b260c3a35dd1a23a15e8894d15cdd42333516e17cdd32061ae. Their complete supplying statements and proofs were then read: P2.2/P2.3(the same aliased block),P2.4,P2.5,P2.6,P2.7,P2.9,P2.10,P2.11/A3.2 and D1.3,D2.1,D2.3,D3.1,D3.2. This is13 distinct full proof blocks associated with14 stable IDs. All exact differences against the retained3b272246 full-source snapshot were read, including the complete new P2.6 component-resolution passage. The existing exact calculations and primary receipts are reused with their recorded scopes; no new computation was performed.

This reuses the two earlier exposed global evidence groups `publish-I-topology-final-F` and `publish-I-topology-final-G`, with event IDs `publish-I-topology-final-F-20261121` and `publish-I-topology-final-G-20261121`. It creates no new CHECK_EVENTS row and no independent or targeted credit.

The earlier global comparison was bound toc1726b5d7afea83a38ad1e1bb457810d0508f5cf98019102743696cda8410a1d. A bounded SHA search of217 retained work/*.tex files found no byte-identical whole-source snapshot of that hash. The earlier comparison receipt and check records remain the evidence for that reading. The new receipt records exact block comparisons from the retained3b272246a072bcf423cea040c0eaec5ce2a8f30da5ab06a8fb7651a4c2ffdd1e snapshot and from frozen candidate11(7479a42f...) to current, plus a full new exposed reading of the current supplying proofs. It does not claim unavailable whole-source byte identity fromc1726b5d.

## Theorem F

The admissible data remain b=4l1+3l2,p=12l0−b,a=−p,3∤l1 and oddl2. The partial family usesw=r6, its12 ruled components and rotations4l1,3l2,−b. The exact origin difference and its covered deck differences remain unchanged onq=Q^(12m),r=R^n; the radial γ coefficient is−pn. The ordinary parameter origin, clockwise peripheral conventions and complex-oriented normal meridians match the supplying proof.

P2.4 still supplies a smooth proper modification carrying the marked map, using the bi-anticanonical pencil and the three labelled critical values. The graph construction is explicit and preserves the punctured family. Its changed wording and authenticated published BM97 locators do not change that map. P2.5's determinant6 finite-orbit calculation is unchanged. P2.7 retains the commuting lifts Qo=T_(−mbγ)Q,Ro=R and the ratio equation(mαi+nβi)κj=(mαj+nβj)κi, with positive denominators on every axis component. The strict cusp ratioa and horizontal ratio0 are still compared on a connected compact corner. Arbitrary central components, multiplicities and singularities remain allowed by the resolution/graph/principalization sequence.

For coprime(3k,4l), the current proof retainsN=12kl,w=r^(N/2),q=Q^(Nm),r=R^n, the two exact origin differences withN/2 replacing6, and gcd(a,N)=1. The canonical degree d=4l+3k−kl is proved nonzero. The indicated choice ofK^(−N) orK^N according to its sign, the Veronese equations and the three labelled rational points still recover the degree-one base parameter. These agree with outline step6.

P2.10's corrected marked small resolution remains exactly the one checked earlier: resolve(b,y), with maps(X,Y,Z,V,u)=(z,rw,x,y,r²), first parameters(y,w/r,rk), second parameters(rb,x,j/r), andAB=kj=1. Both involution lifts are retained, as are the two bundle-valued neck equations, compact fundamental cover and finite quotient. The selected diagonal is[e1,e2]. No new selected-resolution correction is needed.

P2.11/A3.2 retains the same derived-normalization virtual tangent class and paired branch-normal calculation giving virtual Euler0, while the untwisted smooth fibre has Euler2. Its conclusion remains confined to Engel's specified one-component pinching, and P2.10 supplies the stated different central filling through its explicit proper modification and quotient. Main F and its7 outline steps agree with these exact scopes.

## Exact effect of the P2.6 repair

The repair changes the supplied proof of the horizontal-meridian input, not the theorem's hypotheses or conclusion. It inserts the proper component resolutionν:Dtilde→D, isomorphic overDreg, and the Stein diagramDtilde→C→B. OnB'=B\Σ,C'=h^−1(B'),V=p^−1(C'), the mapV→C' is a proper submersion with connected fibres, soπ1(V)→π1(C') is onto. RemovingA=V∩ν^−1(Dsing∪⋃E≠D(D∩E)) givesU withπ1(U)→π1(V) onto. The resulting image inπ1(B°) has finite index. The restrictionν|U identifiesU with the original smooth component locus away from other components; its loops transport the original complex-oriented normal circle, λ ande=ord_D(R). Thus P2.5 kills that same class, and P2.7 receives the same horizontal ratio0. The additional explicit dependency is the analytic resolution already supplied in P2.4. Main F outline step3 compresses this exact component-resolution/Stein argument. No new restriction on central-component smoothness is introduced.

## Theorem G

The outer-boundary quantifiers remain: every|w0|=216, every connected neighbourhood, every flat proper map from a reduced complex space with pointwise biholomorphic inner fibres. The intrinsic divisor2S2, itsb1=2 surface and Albanese nomeiw/216 give the same J natural-boundary contradiction. The current D1.3 prose retains pointwise equality of the Albanese invariant and does not assume a holomorphic choice of fibrewise isomorphisms.

The fixed root coordinate and ordered integral basis in D2.1, its theta expansionB(h)=−3ih²+O(h4), and the exact dual formula are unchanged. In D3.1 the real period matrix hasdetA=TDc; the real quadratic cancellation gives t_n=λ·V_n+o(1). The half-integral label latticeLa, primitive survivingK, graph ofell and annihilatorGamma∞ agree word for word with the headline. The realizationV_n=nv+v0 and dn(1+||V_n||²)→0 retains the exact parameter choice making−Dcn(hn)=dn andImcn<H*. The pointed additive quotient limits have precisely the claimed real-torus dimensions.

At fixedc*, D2.3 retains the covectorlcm(2,n)Reξ and its continuous circle-valued map, irrational root-ray escape, actual period-vector approximation, and the full universal Hausdorff factorization. D3.2 compares the exact two parameter paths through their distinct real dimensions. These match all5 outline steps. No dependency of G changes through the P2.6 repair or PI19 extraction.

## Exact effect of the PI19 cusp lemma

PI19 extracts the former self-contained inv:B3.3 Step5 before inv:B3.1's first use. Its maps are the inclusioni:W→N andr:N→W, withr∘i=idW andH(x,u)=Phi[−log(1−u)](x), extended by its uniform limit atu=1, provingi∘r≃idN while fixingW. The new earlier lemma supplies the identical inducedπ1/cohomology comparisons. The full applied blocks were already compared and bound in candidate11_cusp_applied_binding.json.

Neither of the current F/G supplying proof blocks invokes inv:B3.1,inv:B3.3 or PI19. F's untwisted Euler calculation uses its explicit toric strata; its canonical connected-fibre input is the construction/canonical-ring input cited inP2.4. G's surface invariant comes from the finite-root model. Thus the lemma changes the location of the common cusp contraction and the local inv:B3.1 dependency, while preserving the marked geometric data used by F/G.

## Outcome

The current F/G statements, all12 outline items, supplying hypotheses, markings, signs, special cases and conclusions agree at the exacte9a12c1a source. No new proof defect was found in this scoped final binding. The separate P2.6 proof repair and cusp extraction keep their already recorded exposed events; this binding adds none.
'''
md=D/'S6_SERIES_PUBLISH_I_final_FG_e9_applied_binding.md';md.write_text(notes)
prior=D/'S6_SERIES_PUBLISH_I_final_FG_comparison.json';rece=dict(created_utc=now,current_source_path=str(S.relative_to(R)),current_source_sha256=sha(s),prior_global_receipt_path=str(prior.relative_to(R)),prior_global_receipt_sha256=hashlib.sha256(prior.read_bytes()).hexdigest(),prior_bound_source_sha256='c1726b5d7afea83a38ad1e1bb457810d0508f5cf98019102743696cda8410a1d',exact_old_snapshot_availability={'full_c172_snapshot_found':False,'retained_work_tex_files_hashed':217,'actual_comparison_snapshot':str(B.relative_to(R)),'actual_comparison_snapshot_sha256':sha(b),'candidate11_snapshot_sha256':sha(c)},reused_evidence_groups=['publish-I-topology-final-F','publish-I-topology-final-G'],reused_event_ids=['publish-I-topology-final-F-20261121','publish-I-topology-final-G-20261121'],new_check_events=0,new_independent_checks=0,new_program_executions=0,complete_headlines_and_outlines_actually_read={x:dict(statement=head(s,'series:I:'+x),outline=outline(s,x),statement_sha256=sha(head(s,'series:I:'+x)),outline_sha256=sha(outline(s,x))) for x in ['F','G']},current_full_proof_blocks=records,comparison_note=str(md.relative_to(R)),P26_effect='Component resolution nu and its restriction to U preserve the original oriented meridian lambda and multiplicity e, supply finite-index base monodromy transport, and hence retain horizontal ratio0 in P2.7. Resolution input already supplied byP2.4.',PI19_effect='Same inclusion W->N and strong deformation retraction r:N->W, with explicit H. It changes the location of inv:B3.3Step5 and inv:B3.1 reference. No direct use in the F/G supplying proof blocks; no F/G hypothesis or sign changes.',outcome='Current complete headlines/outlines and supplying proofs agree in the scoped final comparison; no new defect or mathematical event.')
(D/'S6_SERIES_PUBLISH_I_final_FG_e9_applied_binding.json').write_text(json.dumps(rece,indent=2)+'\n')
# Update only the two existing row outcomes; same event/group identities and row count.
p=D/'S6_SERIES_PUBLISH_I_final_FG_CHECK_EVENTS.tsv'
with p.open() as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
assert len(rows)==2
for row in rows:row['outcome']+=' Final exposed applied binding to sourcee9a12c1a9f1c08b260c3a35dd1a23a15e8894d15cdd42333516e17cdd32061ae: full current headline/outline and supplying proofs reread; P2.6 resolution and PI19 contraction effects recorded in final_FG_e9_applied_binding.json. Same evidence group; no added check event.'
with p.open('w') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
# Bind the one trace-map event to its applied complete proof, allowing the independently applied citation package.
expected=c
for file in ['S6_SERIES_PUBLISH_I_candidate11_citation_guards.json','S6_SERIES_PUBLISH_I_candidate11_prose_guards.json']:
 for pch in json.loads((E/file).read_text())['patches']:
  assert expected.count(pch['old'])==1;expected=expected.replace(pch['old'],pch['new'])
a=block(expected,'push:src:B.4.26');z=block(s,'push:src:B.4.26');assert a==z
(E/'S6_SERIES_PUBLISH_I_candidate11_prose_applied_binding.json').write_text(json.dumps(dict(created_utc=now,source_sha256=sha(s),scope='The complete B4.26 applied proof equals the previously fully read/compared candidate11 proof with the exact coordinate-map and citation guards. Same event/group; no additional event.',statement_id='push:src:B.4.26',complete_applied_block_sha256=sha(z),complete_applied_block=z,event_id='ce:publish-I-B426-trace-map-exposed-20261121',evidence_group='eg:publish-I-B426-trace-map-exposed',new_check_events=0),indent=2)+'\n')
p=D/'S6_SERIES_PUBLISH_I_candidate11_prose_CHECK_EVENTS.tsv';t=p.read_text();assert 'Applied binding pending.' in t;p.write_text(t.replace('Applied binding pending.','Applied at sourcee9a12c1a; complete applied B4.26 proof exactly matches the compared replacement and citation guards, as recorded in the applied-binding receipt.'))
print(json.dumps({'current_source':sha(s),'full_proof_IDs':len(records),'distinct_full_proof_blocks':len({x['current_block_sha256'] for x in records}),'headline_outline_reading':12,'reused_global_rows':len(rows),'new_events':0,'receipt':str(D/'S6_SERIES_PUBLISH_I_final_FG_e9_applied_binding.json')},indent=2))
