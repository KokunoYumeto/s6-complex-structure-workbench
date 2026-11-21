from pathlib import Path
import json,hashlib,datetime,re,csv
base=Path('/workspace/scratch/653608133b22');a=base/'work/agents/i_topology';f=base/'work/S6_SERIES_PUBLISH_I.tex';s=f.read_text();old=(base/'source/S6_SERIES_GRIND_I.tex').read_text()
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
patches=[]
def p(name,before,after,ids,reason):
 assert s.count(before)==1,(name,s.count(before))
 patches.append({'id':name,'old':before,'new':after,'statement_ids':ids,'reason':reason,'proof_change':False})
p('I-topology9-01',r'''This use of a common modification is legitimate here
because the common fan has already constructed it.
It is not an assumed extension of an arbitrary punctured
isomorphism.
''','',['push:src:A.4.7'],'The preceding sentences explicitly construct the proper common modification by cone intersections and resolve it; delete the repeated defensive contrast. Both maps and all hypotheses remain.')
p('I-topology9-02',r'''side is a period. The scalar correction
$-\boldsymbol\delta/24$ is retained: the bare fraction
$\boldsymbol\gamma/12$ would not have the required
twelfth iterate.''',r'''side is a period. The sum of the twelve fractions
$\boldsymbol\gamma(s+k,t)/12$ is
$\boldsymbol\gamma(s,t)-11\boldsymbol\delta/2$.
The twelve constant terms $-\boldsymbol\delta/24$
contribute $-\boldsymbol\delta/2$, giving the integral period
$\boldsymbol\gamma(s,t)-6\boldsymbol\delta$.''',['push:src:B.4.18'],'Express the existing corrected-versus-bare-deck comparison by its exact finite sums. All displayed deck, period, scalar-unit and twelfth-iterate identities are preserved; no independent computation credit.')
p('I-topology9-03',r'''This retains the affine cusp marking, rather
than only identifying its fibrewise Jacobians.''',r'''This map preserves the affine cusp marking.''',['push:src:B.4.18'],'The explicit map zeta -> zeta-sigma+F immediately precedes this sentence and preserves the full marked-family claim.')
p('I-topology9-04',r'''\item For completeness, for the negative rotation keep the same positive
root-base rotation and use the inverse translation
$-b$. The resulting valuation shear is $H^{-1}$;
its twelfth iterate is $G_2^{-1}$. It preserves
the same fan and has the same freeness properties.
This is the opposite convention and is not the model
used below. In the retained convention the clockwise
cusp generator is $g_0:s\mapsto s-1$. Thus the''',r'''\item Keeping the same positive root-base rotation and using translation
$-b$ gives valuation shear $H^{-1}$ and twelfth iterate
$G_2^{-1}$. This action preserves the same fan and has the same
freeness properties. For the family in the statement we use
translation by $b$ and the clockwise cusp generator
$g_0:s\mapsto s-1$. Thus the''',['push:src:B.4.18'],'Retain the exact sign-changing substitution and both shears, then specify the chosen action positively. Clockwise shift -1 and positive-loop shift +1 remain verbatim afterward.')
p('I-topology9-05',r'''They identify the marked family with that Tate
model, not only its individual smooth fibres.''',r'''They identify the marked family with that Tate
model over $\Delta_s$.''',['push:src:B.4.20'],'The monomial node charts and exact collar map immediately preceding give the same identification of the entire marked family.')
p('I-topology9-06',r'''The factor $a(s)$ gives the
retained gluing parameter around the cycle.''',r'''The factor $a(s)$ gives the
gluing parameter around the cycle.''',['push:src:B.4.20'],'Same holomorphic unit and normal-line gluing parameter; remove the redundant retention epithet.')
p('I-topology9-07',r'''These marked quantities are not conflated.
''','',['push:src:B.4.20'],'The preceding text already specifies M inverse, M, the theta multiplier and the separate a inverse-sixth translation, with their exact relations; delete only defensive commentary.')
p('I-topology9-08',r'''\item We record the neighbourhood limitation explicitly.
At a central node, the smooth Kato total space''',r'''\item At a central node, the smooth Kato total space''',['push:src:B.4.20'],'The entire local differential calculation proving the asserted obstruction remains.')
p('I-topology9-09',r'''line, with the inherited map from $\mathcal D$,
would instead have $s=uv$, with a critical normal''',r'''line, with the inherited map from $\mathcal D$,
has $s=uv$, with a critical normal''',['push:src:B.4.20'],'The normal-line total space is the explicitly defined local model. State its existing base map directly; the comparison with s=uv-h and the critical-locus proof remain.')
p('I-topology9-10',r'''\item An inverse-normal plumbing variable $f$ would
give the local equation''',r'''\item With an inverse-normal plumbing variable $f$, the local equation is''',['push:src:B.4.20'],'Keep the explicit local equation r=f(uv-s), its smoothness/normal-crossing calculation and derivative. This sentence concerns exactly that local model.')
p('I-topology9-11',r'''Further deformations or a different map to the
original base are outside this obstruction.
''','',['push:src:B.4.20'],'The preceding conclusion already states the precise fixed-base localized plumbing scope. No construction or hypothesis is removed.')
preview=s
for x in patches:
 assert preview.count(x['old'])==1,x['id']
 preview=preview.replace(x['old'],x['new'])
labels=lambda t:sorted(re.findall(r'\\(?:label|hypertarget)\{([^}]+)\}',t))
assert labels(preview)==labels(s)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
out={'created_utc':now,'input_sha256':sha(s),'preview_sha256':sha(preview),'scope':'Assigned candidate indices20--26 and28--35 only, with contextual cleanup in the full affected A4.7/B4.18/B4.20 proofs. Same existing exposed evidence groups; zero new check events.','patches':patches}
(a/'editorial/S6_SERIES_PUBLISH_I_residual_batch9_guarded.json').write_text(json.dumps(out,indent=2)+'\n')
def block(t,label):
 pos=t.index('\\label{'+label+'}')
 start=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|remark|corollary)\}',t[:pos]))[-1].start()
 end=t.index('\\end{proof}',pos)+len('\\end{proof}')
 return t[start:end]
excerpts={}
for label in ['push:src:A.4.7','push:src:B.4.18','push:src:B.4.20']:
 excerpts[label]={'original_full_statement_and_proof':block(old,label),'current_full_statement_and_proof':block(s,label),'proposed_full_statement_and_proof':block(preview,label),'original_block_sha256':sha(block(old,label)),'current_block_sha256':sha(block(s,label)),'proposed_block_sha256':sha(block(preview,label))}
(a/'editorial/S6_SERIES_PUBLISH_I_residual_batch9_full_comparison.json').write_text(json.dumps(excerpts,indent=2)+'\n')
dispositions={
20:'Keep. Retained boundary triangulation is the fixed geometric boundary condition used to exclude additional rays; no production claim.',
21:'Keep. Supplied by Engel identifies the cited general construction. The complete receiving marked resolution map and both transitions remain explicitly printed; no anti-diagonal is attributed to Engel.',
22:'Keep. Separate branches before the period quotient are required mathematical data for the branch count and T1 calculation.',
23:'Keep. Rather than compares smoothing and small resolution through their explicit local Euler contributions 0 and2 replacing1; it is the proved geometric comparison.',
24:'Remove four lines of defensive prose after the explicit common-fan construction/resolution. The preceding cone-intersection morphism and primary resolution citation, and the following pi1 maps, remain.',
25:'Keep. Face self-identifications are data needed by the strictification and factorization procedure.',
26:'Keep. Corrected form refers to the cited published Matsuki erratum, with its exact hypothesis on centres and maps to the target.',
28:'Keep. The supplied smoothing section is the explicit coordinate u=xy and identifies the tensor product of normal lines.',
29:'Keep. The successive blow-up multiplicities are the coefficients in the mathematical exceptional divisor n[-s].',
30:'Replace retention/contrasting prose by the exact uncorrected sum gamma-11delta/2 and the constant contribution -delta/2, yielding gamma-6delta. This is the same existing finite-sum comparison, with all period and unit identities retained.',
31:'Retain the exact negative-translation comparison -b, H inverse, G2 inverse; specify the chosen positive b and clockwise s->s-1 action without process language. Remove the adjacent defensive fibrewise contrast while retaining the full marked map.',
32:'Retain a(s) as the cycle gluing parameter. After full original/current proof reread, remove redundant defensive phrases while preserving all normal-line and marked-period equations, the proved differential obstruction, and the fixed-base local-plumbing scope.',
33:'Keep. Period ambiguity is the explicitly defined lattice quotient in B4.24, required for norm descent; retained describes that mathematical quotient.',
34:'Keep. Supplied by the proper family refers to its coherent extension sheaves; the explicit counterexample and scope are mathematical claims, not production commentary.',
35:'Keep. Ordered local branches are necessary data at self-crossings for the angular homology calculation.'}
receipt={'created_utc':now,'source_sha256':sha(s),'original_source_sha256':sha(old),'candidate_indices':list(dispositions),'dispositions':dispositions,'full_original_and_current_proofs_actually_read':['push:src:A.4.7','push:src:B.4.18','push:src:B.4.20'],'existing_evidence_groups':['publish-I-topology-editorial7-push-src-A-4-7','publish-I-topology-editorial7-push-src-B-4-18','publish-I-topology-editorial7-push-src-B-4-20'],'new_mathematical_events':0,'independent_credit':False,'labels_and_hypertargets_preserved':True,'comparison':'All three complete old/current proofs and all replacements were read. In B4.18 the exact already-printed gamma(s+k)=gamma-k delta formula gives the displayed finite-sum comparison; b,F,sigma, both period shears, root-base rotation, scalar-unit cancellation, clockwise identification and two-open gluing remain. In B4.20 all Cartier, normal-line, theta, scaling and differential maps remain; only scope repetition is removed.'}
(a/'editorial/S6_SERIES_PUBLISH_I_residual_batch9_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
md=['# Final contextual residue review','',f'Input SHA256 `{sha(s)}`. Eleven minimal guards. Zero new mathematical events; the three full proof comparisons use their existing exposed evidence groups.','', '## Candidate dispositions','']
for i,v in dispositions.items(): md+=[f'- **{i}:** {v}']
md+=['','## Full proof comparison','',receipt['comparison'],'','The full original/current/proposed passages and their hashes are recorded in the adjacent full-comparison JSON. All labels and hypertargets are unchanged.']
(a/'editorial/S6_SERIES_PUBLISH_I_residual_batch9_comparison.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'guards':len(patches),'input_sha256':sha(s),'preview_sha256':sha(preview),'candidate_dispositions':len(dispositions),'new_events':0}))
