from pathlib import Path
import re,json,hashlib,datetime,csv
base=Path('/workspace/scratch/653608133b22');a=base/'work/agents/i_topology';path=base/'work/S6_SERIES_PUBLISH_I.tex';s=path.read_text();orig=(base/'source/S6_SERIES_GRIND_I.tex').read_text()
sha=lambda x:hashlib.sha256(x.encode()).hexdigest()
def block(t,label):
 pos=t.index('\\label{'+label+'}');st=list(re.finditer(r'\\begin\{(?:theorem|proposition|lemma|corollary)\}',t[:pos]))[-1].start();en=t.index('\\end{proof}',pos)+len('\\end{proof}');return t[st:en]
full=block(s,'night:P2.6');start=full.index('\\item The proper map $D\\to B$');end=full.index('\n\\item The orbit',start);old=full[start:end]
new=r'''\item Resolve the reduced compact component $D$ by a proper map
$\nu:\widetilde D\to D$ which is an isomorphism over $D_{\rm reg}$,
using the analytic resolution theorem in \ref{night:P2.4}.
Apply Stein factorization to $f|_D\circ\nu$:
\[
 \widetilde D\xrightarrow{p} C\xrightarrow{h} B,
 \qquad f|_D\circ\nu=h\circ p.
\]
Here $p$ has connected fibres, $p_*\mathcal O_{\widetilde D}=\mathcal O_C$,
and $h$ is finite, by \cite[Theorem~8.5, pp.~80--81]{Movasati24}.
The curve $C$ is normal: a locally meromorphic function integral over
$\mathcal O_C$ pulls back to a holomorphic function on the normal space
$\widetilde D$ and descends by the displayed direct-image equality.
Thus $C$ is a smooth compact curve.

Let $\Sigma\subset B$ consist of $0,1,\infty$, the branch values of $h$,
and the $h$-images of the critical values of $p$. This set is finite.
Put
\[
 B'=B\setminus\Sigma,\qquad C'=h^{-1}(B'),\qquad
 V=p^{-1}(C').
\]
Then $p:V\to C'$ is a proper submersion with connected fibres, and
$h:C'\to B'$ is a finite unramified cover. Path lifting followed by
a path in a fibre gives $\pi_1(V)\twoheadrightarrow\pi_1(C')$.
Consequently the image of $\pi_1(V)$ in $\pi_1(B')$ has index $\deg h$.

Let $E$ range over the other irreducible components of the reduced
parameter-central divisor, and set
\[
 A=V\cap\nu^{-1}\!\left(D_{\rm sing}\cup
                  \bigcup_{E\ne D}(D\cap E)\right),\qquad U=V\setminus A.
\]
This is a proper complex analytic subset $A$ of the smooth manifold $V$.
General position moves every based loop in $V$ off $A$, so
$\pi_1(U)\to\pi_1(V)$ is surjective. The inclusion
$B'\hookrightarrow B^\circ$ is also surjective on fundamental groups;
therefore the image of $\pi_1(U)$ in $\pi_1(B^\circ)$ has index at most
$\deg h$.

The restriction of $\nu$ identifies $U$ with its image in
$D_{\rm reg}$ away from the other central components and over $B'$.
Composing these loops with $\nu$ thus transports the normal circle
in the original smooth total space. Its complex orientation, lattice
class $\lambda$ and parameter degree $e=\ord_D(R)$ are those of step~2.
Hence a finite-index subgroup of the base group transports the
original normal meridian.'''
assert s.count(old)==1
proposed=full.replace(old,new)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
guard={'created_utc':now,'input_sha256':sha(s),'patches':[{'id':'I-P26-component-resolution-01','old':old,'new':new,'statement_ids':['night:P2.6','stmt:P2.6'],'reason':'Resolve the central component itself before applying Stein factorization and loop general position. Smoothness of the total filling alone does not supply component smoothness. The explicit resolution map preserves the original meridian and multiplicity on the stated open set; no hypothesis is narrowed.','proof_change':True}]}
(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_guarded.json').write_text(json.dumps(guard,indent=2)+'\n')
(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_full_proof.tex').write_text(proposed+'\n')
comparison={'created_utc':now,'statement_id':'night:P2.6','current_number':'Theorem18.5','tag':'02RG','source_sha256':sha(s),'original_source_sha256':sha(orig),'original_full_statement_and_proof':block(orig,'night:P2.6'),'current_full_statement_and_proof':full,'replacement_full_statement_and_proof':proposed,'dependency_current':block(s,'night:P2.4'),'dependency_original':block(orig,'night:P2.4'),'method':'Complete original and current 18.3/18.5 statements/proofs actually read; replacement compared in full with all four steps. Exposed repair, not derivation-before-proof and not a new independent computation.','preserved':['Theorem statement and both labels/tag','Step1 exact quotient presentation and cross-cocycle calculation','Step2 original normal circle, class lambda and multiplicity e','Step4 finite-orbit lattice conclusion and local root inheritance'],'repair':'The original/current Step3 asserts D is smooth. The cited total-space/graph resolution establishes smoothness of the ambient filling, not of each central component. The replacement uses nu:Dtilde->D, Stein curve C, finite removed base values, the proper analytic exceptional/intersection subset A, and explicit U->V->Cprime->Bprime->Bcircle maps. Normal circles are taken in the original filling after nu identifies U with an open subset of D_reg.','event_credit':'One exposed used-and-rechecked event; zero targeted/independent/fresh-computation credit.'}
(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
error={'error_id':'ce:publish-I-P26-step3-component-smoothness-gap-20261121','canonical_statement_id':'night:P2.6','refined_proof_claim_id':'night:P2.6/step3/smoothness-of-central-component','tag':'02RG','source_location':'Candidate11 p127, Step3 of Theorem18.5','original_and_current_claim':'Here D is compact smooth and B a smooth curve, so the hypotheses hold.','scope':'Proof dependency gap; no statement-refuted claim or event. The theorem remains stated with its original hypotheses.','origin':'The same smoothness sentence occurs in the attached original S6_SERIES_GRIND_I.tex. The publication edits preserved it.','resolution':'Apply proper resolution to D itself, isomorphic over D_reg, and use its Stein factorization to produce transport loops. The printed proof now specifies all removed base values and exceptional/intersection inverse images, the finite-index image and the identification of original normal meridians.','guard_file':str(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_guarded.json'),'full_comparison_file':str(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_comparison.json'),'statement_changed':False,'independent_credit':False}
(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_ERROR_RECORD.json').write_text(json.dumps(error,indent=2)+'\n')
md=['# Theorem18.5: component-resolution repair','',f'Canonical identity `night:P2.6`, tag02RG. Input source SHA256 `{sha(s)}`.','',comparison['method'],'','## Exact gap and origin','',comparison['repair'],'','The same sentence occurs in the attached original; this is a scoped proof dependency correction, not a refutation of the theorem.','', '## Exact maps and open sets','', 'The proper resolution nu is an isomorphism over D_reg. The Stein factorization of f_D nu is p:Dtilde->C followed by finite h:C->B. The finite set Sigma contains0,1,infinity, branch values of h, and h-images of critical values of p. On Bprime=B minus Sigma, Cprime=h^-1(Bprime), and V=p^-1(Cprime), the first map is a proper submersion with connected fibres and the second is a finite unramified cover.','', 'Remove A=V intersect nu^-1(D_sing union all D-intersections with other central components), and put U=V minus A. General position gives pi1(U)->pi1(V) onto. The image in pi1(Bprime) has index deg(h); the further surjection pi1(Bprime)->pi1(Bcircle) makes the final index at most deg(h). The open isomorphism nu|U sends these paths to D_reg in the original filling. Positive normal circles there keep the complex orientation, lambda and e=ord_D(R).','', 'No ambient or base modification is used in this repair, and no SNC or smooth-component hypothesis is added. The theorem statement and Steps1,2,4 remain unchanged.','', '## Credit','', 'The complete original/current proof and dependency were read before this repair. This is exposed used-and-rechecked work; no targeted-before-proof, independent or computational credit is claimed.']
(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_comparison.md').write_text('\n'.join(md)+'\n')
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
row={'statement_id':'night:P2.6','date':'2026-11-21','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH topology-check agent','type':'used and rechecked in this run','outcome':'Complete original/current P2.4 and P2.6 statements and proofs read; exposed repair of the unsupported component-smoothness sentence. The explicit nu:Dtilde->D, Stein factorization, removed sets and finite-index loop argument preserve the original meridian lambda and multiplicity e. Statement unchanged. No targeted/independent/fresh-computation credit. Guarded replacement compared in full; applied binding pending.','event_id':'ce:publish-I-P26-component-resolution-exposed-20261121','phase':'Paper I rendered-reading proof repair','source_file':str(a/'editorial/S6_SERIES_PUBLISH_I_P26_component_resolution_comparison.md'),'source_row':'complete proof and exact resolution/open-set comparison','source_event_type':'used and rechecked in this run','evidence_group':'eg:publish-I-P26-component-resolution-exposed'}
with (a/'S6_SERIES_PUBLISH_I_P26_component_resolution_CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerow(row)
# Actual primary image receipt for Movasati, Theorem8.5.
pdf=a/'literature/S6_SERIES_PUBLISH_I_Movasati2024_current_primary.pdf';pdfsha=hashlib.sha256(pdf.read_bytes()).hexdigest()
rec={'created_utc':now,'title':'A Course in Complex Geometry and Holomorphic Foliations','author':'Hossein Movasati','edition':'Author version dated May13,2024','url':'https://w3.impa.br/~hossein/myarticles/ComplexGeometry.pdf','retrieved_url':'https://w3.impa.br/%7Ehossein/myarticles/ComplexGeometry.pdf','download':'curl HTTP200 after the unescaped urllib request returned400','pdf':str(pdf),'pdf_sha256':pdfsha,'locator':'Theorem8.5, printedpp80--81, PDFpages94--95','scope':'Both complete page images actually viewed and read: full Stein-factorization statement and proof, including p_*O=O_C, finite h, connected fibres and uniqueness. Source is stated for proper holomorphic maps of analytic varieties; the receiving map f_D nu has smooth compact source. No independent mathematical credit from the locator reading.','pages':[]}
for n in [94,95]:
 im=a/f'literature/S6_SERIES_PUBLISH_I_Movasati2024_page_{n}.png';rec['pages'].append({'pdf_page':n,'printed_page':n-14,'image':str(im),'image_sha256':hashlib.sha256(im.read_bytes()).hexdigest(),'pdf_sha256':pdfsha})
(a/'literature/S6_SERIES_PUBLISH_I_Movasati2024_locator_receipt.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps({'input_sha256':sha(s),'guards':1,'statement_changed':False,'new_exposed_event_rows':1,'independent_credit':False,'Movasati_pdf_sha256':pdfsha}))
