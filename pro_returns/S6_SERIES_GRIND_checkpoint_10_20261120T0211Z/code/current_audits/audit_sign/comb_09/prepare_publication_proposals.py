"""Prepare reviewable comb proposals. Never edit receiving/shared sources."""
from pathlib import Path
import csv
import datetime as dt
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
WORK=HERE.parents[1]
now=dt.datetime.now(dt.timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(rel): return (WORK/rel).read_text()
guards=[]
def guard(target,old,new,reason,label='inv:E2.5'):
    actual=read(target).count(old)
    assert actual==1,(target,actual,old[:100])
    guards.append(dict(target=target,label=label,old_text=old,new_text=new,
                       expected_count=1,reason=reason,
                       input_sha256=sha(WORK/target)))

body=read('parts/II.body.tex')
proof=(HERE/'E25_proposition_and_proof.tex').read_text()
newlabels=re.findall(r'\\label\{([^}]+)\}',proof)
collisions=[]
for p in (WORK/'parts').glob('*.tex'):
    text=p.read_text()
    for label in newlabels:
        if '\\label{'+label+'}' in text:
            collisions.append({'path':str(p.relative_to(WORK)),'label':label})
assert not collisions,collisions
anchor=r'\begin{proposition}[Counterexample: The universal two-vector-field bound]\label{inv:E2.4}'
guard('parts/II.body.tex',anchor,proof+'\n\n'+anchor,
      'Insert the complete newly received proposition after E2.2 and before E2.4; all new statement/formula labels were checked against all current parts.')

old=r'''The integer $m$ and the stated limiting data do not determine in
this paper the splitting of the rank-three bundle $K_m$ in \eqref{invII:eq:E.6},
or its exact number of sections. This splitting calculation is unfinished.'''
new=r'''Proposition~\ref{inv:E2.5} determines the actual splitting
$K_{12}=\mathcal O_B(-8)\oplus\mathcal O_B(-9)^2$ and its zero
space of sections on a nonempty open family of twelve-tooth smoothings.
The remaining problem is to determine the splitting of the rank-three
bundle $K_m$ in \eqref{invII:eq:E.6} for general tooth counts and for
special members outside that proved open family, together with its
exact number of sections.'''
guard('parts/II.body.tex',old,new,
      'Preserve E2.3 as the remaining general/special-member problem, explicitly recording the new proved open family.',label='inv:E2.3')
old=r'''The smallest undecided instance
is the splitting of \eqref{invII:eq:E.6} for one specified smoothed 12-tooth period
section. The
attached construction supplies an existence argument and an open
set of smoothing choices, not the transition matrices of a uniquely
specified $X_{12}$. We have not chosen and solved its nonlinear
period-section smoothing equations, and have not run two numerical
methods on those missing matrices. Formulas \eqref{invII:eq:E.5}--\eqref{invII:eq:E.7} and the
growth bounds are proved, but they are not replacements for that
remaining bundle-splitting calculation.'''
new=r'''Proposition~\ref{inv:E2.5} now computes the actual kernel on a
nonempty open family of smoothed twelve-tooth period sections. Its
flat relative kernel, exact conic two-jet maps and tooth-collapse
comparison give the splitting
$(-8,-9,-9)$, the vanishing cokernel and the attained values
$h^{1,1}=49$, $h^{1,2}=48$. This proves the open-family case without
assigning transition matrices to an unspecified individual member.
The remaining calculation concerns general tooth counts and special
members outside that open family; formulas
\eqref{invII:eq:E.5}--\eqref{invII:eq:E.7} and the uniform bounds
remain the constraints for those calculations.'''
guard('parts/II.body.tex',old,new,
      'Replace the obsolete smallest-undecided-instance assertion by the actual proved open-family result; preserve the unsolved classification scope.',label='inv:E2.3')
old=r'''In particular $0\le h^0(K_{12})\le26$. No balanced splitting has been
assumed, and these bounds are not asserted to be sharp.'''
new=r'''In particular $0\le h^0(K_{12})\le26$.
Proposition~\ref{inv:E2.5} attains the lower endpoint on its open
family, and therefore attains the lower Hodge bounds for $m=12$.
The derivation of the uniform bounds above uses the stated
splitting constraints. Their upper endpoints have not been shown
sharp by this calculation.'''
guard('parts/II.body.tex',old,new,
      'Record the newly attained m=12 lower endpoints while keeping the general upper-bound question explicit.',label='inv:E2.3')

front='audit_sign/frontmatter_II.tex'
old=r'\paragraph{Theorem F (Fibration retention and deformation spaces).}'
new=r'\paragraph{Theorem F (Fibrations, deformation spaces and comb Hodge numbers).}'
guard(front,old,new,'Name the additional exact comb conclusion in the existing main theorem.',label='series:II:F')
old=r'''Its local period-section family retains the affine attachment
classes, three critical values, multiplicities $3,4$, and the
hexagonal fibre type.'''
new=old+r'''
For the original marked section on $\mathbb P(3,4)$, there is a
nonempty open family obtained by embedded smoothings of twelve
admissible deformed twistor conics at distinct ordinary points,
fixing the three marked period planes, whose actual cup kernel is
\[
 K_{12}=\mathcal O_{\mathbb P^1}(-8)
       \oplus\mathcal O_{\mathbb P^1}(-9)^2,
 \qquad \operatorname{coker}\kappa_1=0.
\]
Here $K_{12}$ and $\kappa_1$ are the actual sheaf and cup map of
\eqref{invII:eq:E.6}. These members have
$h^{1,1}=49$ and $h^{1,2}=48$.'''
guard(front,old,new,'State full actual construction scope and identify the exact kernel/cup before giving its Hodge values.',label='series:II:F')
old=r'''directions, and propagation preserves the ordered multiplicities.
\textit{Relation to literature.}'''
new=r'''directions, and propagation preserves the ordered multiplicities.
The flat kernel at a comb node gives a cyclic two-jet quotient;
actual conic frames and tooth collapse transport its balanced
cohomology to the smooth section.
\textit{Relation to literature.}'''
guard(front,old,new,'Add the actual kernel mechanism without inferring an unrelated main-theorem dependency.',label='series:II:F')
old=r'''The comb vector-field value corrects the bound in
\cite[Corollary~1.3, p.~2]{HKP2000}, as explained in
\ref{inv:E2.4}.'''
new=old+r'''
The twelve-tooth calculation gives the stated open-family values
in the remaining-Hodge-number question of
\cite[Section~10(2)]{Viaclovsky2026Combs}; the general and
special-member splitting problem remains in \ref{inv:E2.3}.'''
guard(front,old,new,'Give bounded construction/question credit and preserve the remaining splitting scope.',label='series:II:F')
old=r'''\ref{cdp:st:E15}, \ref{push:src:E.2.23}, \ref{push:src:E.2.24}.'''
new=r'''\ref{cdp:st:E15}, \ref{inv:E2.2}, \ref{inv:E2.5},
\ref{push:src:E.2.23}, \ref{push:src:E.2.24}.'''
guard(front,old,new,'Include the exact body statements for the added main conclusion.',label='series:II:F')
old=r'''(\hyperref[push:src:E.2.24]{\ref*{push:src:E.2.24}}).
\end{enumerate}'''
claim=r'''The actual flat cup kernel on a smoothed
comb imposes a cyclic two-jet condition at each node. The explicit
conic frame map realizes a dense open set of these quotients;
twelve teeth attain the balanced cohomology. The exact collapse
and semicontinuity maps give $K_{12}=\mathcal O(-8)\oplus\mathcal O(-9)^2$
on the stated open family, and the actual Hodge formula gives
$(h^{1,1},h^{1,2})=(49,48)$
(\hyperref[inv:E2.5]{\ref*{inv:E2.5}},
\hyperref[inv:E2.2]{\ref*{inv:E2.2}}).'''
new=r'''(\hyperref[push:src:E.2.24]{\ref*{push:src:E.2.24}}).
\item\hypertarget{step-II-F-7}{} '''+claim+r'''
\end{enumerate}'''
guard(front,old,new,'Add a seventh linked outline step; existing six anchors and all existing dependency claims remain unchanged.',label='series:II:F')

old=r'''Liu--Rollenske family. The remaining comb splitting problem is given
with its proved tangent data and exact gap.'''
new=r'''Liu--Rollenske family. An actual flat-kernel and conic two-jet
calculation gives a nonempty open family of twelve-tooth smoothings
with kernel $\mathcal O(-8)\oplus\mathcal O(-9)^2$ and Hodge numbers
$h^{1,1}=49$, $h^{1,2}=48$. The remaining general and special-member
comb splitting problem is stated with its precise scope.'''
guard('code/assemble_series.py',old,new,'Update the generated active Paper II abstract at its actual source.',label='series:II:F')

mapping=json.loads(read('audit_sign/frontmatter_II_map.json'))
F=next(x for x in mapping['main_theorems'] if x['letter']=='F')
map_updates={
 'target':'audit_sign/frontmatter_II_map.json','letter':'F',
 'expected_old_title':F['title'],
 'new_title':'Fibrations, deformation spaces and comb Hodge numbers',
 'append_body_labels':['inv:E2.2','inv:E2.5'],
 'expected_existing_step_numbers':[s['number'] for s in F['steps']],
 'append_step':{'number':7,'anchor':'step-II-F-7','body_targets':['inv:E2.5','inv:E2.2'],'claim_tex':claim},
 'dependency_note':'The new step uses E2.5 and the actual E2.2 Hodge formula. No new edge between existing lettered main theorems is inferred.'}

payload={'date_utc':now,'new_statement':'inv:E2.5','state':'reviewable proposals only; no receiving source/canonical mutation',
         'proof_path':'audit_sign/comb_09/E25_proposition_and_proof.tex','proof_sha256':sha(HERE/'E25_proposition_and_proof.tex'),
         'new_labels':newlabels,'label_collisions':collisions,'guards':guards,'map_updates':[map_updates],
         'integration_order':'Read/review full proof. Apply guards exactly to raw body/frontmatter/assembler, update the map by the declared append operation, then assemble linked sources, build, and inspect new and changed pages. E2.3 remains open.'}
(HERE/'publication_guards.json').write_text(json.dumps(payload,indent=2)+'\n')

receipt={'date_utc':now,'label':'inv:E2.5','verdict':'full mathematical receiving PASS at stated nonempty-open-family scope',
 'independent_freeze':{'path':'audit_sign/comb_09/independent_two_jet_derivation.md','sha256':sha(HERE/'independent_two_jet_derivation.md'),'actual_exposure':'Prior E15/E2.2/E2.3 and route cues exposed; full new route frozen before root target/supplement/certificate.'},
 'full_receiving_report':{'path':'audit_sign/comb_09/receiving_comparison.md','sha256':sha(HERE/'receiving_comparison.md')},
 'post_receiving_certificate':{'path':'audit_sign/comb_09/receiving_exact_certificate.json','sha256':sha(HERE/'receiving_exact_certificate.json'),'passed':25,'total':25,'code_exposure':'Full producer code read before own implementation; no producer import.'},
 'producer_certificate_scope':'Full 170-line program read; all53 outcomes received; three complete arrays independently reconstructed. Producer program not re-executed by this reviewer.',
 'remaining_mathematical_gate_for_scoped_result':None,
 'remaining_publication_gates':['Root acceptance/integration of full proposal and scope revisions','Source/outline map import','Actual built-page formatting/layout review'],
 'general_row':'inv:E2.3 remains open for general/special-member splitting; this receipt does not close it.'}
(HERE/'receiving_comparison.json').write_text(json.dumps(receipt,indent=2)+'\n')

source={'label':'inv:E2.5','relation_to_sources':'The actual conic/filling/smoothing construction is credited to the attached Viaclovsky original; the new proof supplies the flat-kernel two-jet/collapse calculation for its nonempty open twelve-tooth family.',
 'bibkey':'Viaclovsky2026Combs',
 'original_source_path':'S6_GRIND_6_literature/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex',
 'original_source_sha256':'42dea62b023dfb75a009a8c83c15349ddc8f853162f753e3547ca583d07b74d5',
 'actual_openings':[{'locator':'Lemma labelled twistor and complete proof; definition d:comb; proposition comb and complete proof','lines':'1260–1490','order':'before own independent freeze; full comb proof reopened during receiving'},
                   {'locator':'equation originalnormal and sufficient twelve-tooth bound','lines':'2445–2498','order':'before own independent freeze'},
                   {'locator':'Section future / Questions, item2, remaining Hodge numbers','lines':'2701–2708','order':'after independent freeze, during receiving'}],
 'current_internal_inputs':[{'label':'cdp:st:E15','scope':'Actual finite-character graph divisions, uniform cusp period chart, toric/final affine filling and compact family; previously exposed complete proof reopened.'},
                            {'label':'inv:E2.2','scope':'Actual cup kernel, coarse degrees and exact Hodge formula; previously exposed complete proof reopened.'}],
 'worldwide_novelty_search':'No new worldwide priority search or assertion in this receipt.',
 'suggested_source_fields':{'credited_to':'Viaclovsky2026Combs: Lemma twistor, Proposition comb, originalnormal and sufficient m=12 bound; E15/E2.2 exact root/cup inputs.',
 'literature_disposition':'Retain the complete new kernel calculation: the opened original supplies the construction and asks the remaining Hodge question in Section10(2); this proof establishes the specified open-family answer by explicit maps.',
 'source_credit':'opened_exact_sources_with_full_new_map_comparison',
 'source_comparison_ref':'audit_sign/comb_09/receiving_comparison.md; source_comparison.json',
 'remaining_source_gap':'No unclosed source application for this scope; no general/special-member splitting or worldwide novelty claim.'}}
(HERE/'source_comparison.json').write_text(json.dumps(source,indent=2)+'\n')

who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, not separately exposed; S6_SERIES_GRIND/sign_theorem_audit'
events=[
 ('independent re-proof','Full new twelve-tooth node/frame/kernel/collapse/smoothing derivation frozen01:33:18UTC before receiving root target, supplement or certificate. Prior existing E15/E2.2/E2.3 and route cues explicitly exposed. Actual root lift and full mixed/frame terms retained; exact nonempty open-family splitting(-8,-9,-9), e12=0. Same-model-family route; no blind whole-old-E2.3 claim.','comb_independent_freeze_09'),
 ('targeted proof check','Read complete root seven-section target, complete family lift supplement and complete170-line producer program after freeze. All determinant/frame, root division, genericity and collapse maps agree. Exact analytic sufficiency and U=R,V=HR basis transport supplied in full receiving report and insertion-ready proposition. Mathematical PASS only for stated nonempty open m12 family; general E2.3 remains open.','comb_full_receiving_09'),
 ('computation or formal certificate','Post-receiving own program PASS25 exact assertions: universal determinant cup identity, both jet conventions, complete normal-form branch maps, all finite character cells, complete three saved Hermite arrays with independent Fraction ranks, and central Euler/degree. Producer code was read before this implementation and not imported. Root53 output received, not re-executed/reclassified.','comb_receiving_exact_09'),
 ('used and rechecked in this run','Opened attached original Viaclovsky complete twistor lemma/comb proposition proofs and originalnormal/twelve-tooth bound before freeze, and exact Questions10(2) after freeze. Reopened actual E15 finite/cusp family and E2.2 cup/Hodge inputs. Exact locators/hash/application recorded in source_comparison.json. No worldwide novelty assertion.','comb_source_comparison_09')]
with (HERE/'events.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome','event_id','phase'])
    for typ,outcome,suffix in events:
        w.writerow(['inv:E2.5',now,who,typ,outcome,'S6_SERIES_GRIND_sign_'+suffix,'S6_SERIES_GRIND_09'])
manifest={p.name:{'sha256':sha(p),'bytes':p.stat().st_size} for p in HERE.iterdir() if p.is_file() and p.name!='handoff_manifest.json'}
(HERE/'handoff_manifest.json').write_text(json.dumps({'utc':now,'guards':len(guards),'labels':newlabels,'files':manifest},indent=2)+'\n')
print(json.dumps({'utc':now,'guards':len(guards),'new_labels':newlabels,'collisions':collisions,'receipt_sha256':sha(HERE/'receiving_comparison.json'),'guards_sha256':sha(HERE/'publication_guards.json'),'events_sha256':sha(HERE/'events.tsv')}))
