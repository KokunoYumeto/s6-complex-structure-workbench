from pathlib import Path
import json,hashlib,datetime,csv
R=Path('/workspace/scratch/653608133b22');D=R/'work/agents/i_topology';E=D/'editorial';S=E/'S6_SERIES_PUBLISH_I_candidate11_source_snapshot.tex';O=R/'source/S6_SERIES_GRIND_I.tex';s=S.read_text();orig=O.read_text();patches=[]
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
def block(t,lab):
 p=t.index('\\label{'+lab+'}');a=t.rfind('\\begin{',0,p);b=t.index('\\end{proof}',p)+len('\\end{proof}');return t[a:b]
def edit(old,new,ids,why,proof=True):
 global s
 assert s.count(old)==1,(old,s.count(old));patches.append(dict(id=f'I-topology-c11-cusp-{len(patches)+1:02d}',old=old,new=new,statement_ids=ids,reason=why,proof_change=proof));s=s.replace(old,new)
lemma=r'''\begin{lemma}[Contraction of the cusp tube]
\hypertarget{tag-TOPOLOGY-CUSP-TAG}{}\label{I:lem:cusp-tube-contraction}
\StatementRecord{I:lem:cusp-tube-contraction}{proved}{TOPOLOGY-CUSP-TAG}{The normal-crossing charts of the proper local cusp filling}
The reduced one-component hexagonal cusp fibre $W$ in the proper local
filling has a closed tube $N=\{|t_c|\le\epsilon\}$ that strongly
deformation retracts onto $W$. The retraction fixes $W$ pointwise.
\end{lemma}

\begin{proof}
Choose $\epsilon>0$ small enough that the compact tube is covered by
finitely many normal-crossing charts
$t_c=z_1\cdots z_r$, $1\le r\le3$. Off the divisor, take the real
vector field whose $z_i$ component is
\[
 -\frac{z_i|z_i|^{-2}}{\sum_{j=1}^r|z_j|^{-2}},
\]
with its other coordinate components zero. It satisfies
$\dot t_c=-t_c$. Each component has absolute value at most
$(\sum_j|z_j|^{-2})^{-1/2}\le\min_j|z_j|
\le|t_c|^{1/r}$, so the norm is at most $C|t_c|^{1/r}$.
A finite partition of unity preserves $\dot t_c=-t_c$ and gives a
global field of norm at most $C'|t_c|^{1/3}$ after shrinking the tube
so that $|t_c|\le1$. Extend the field by zero on $W$.

Its flow $\Phi_T$ on $N\setminus W$ satisfies
$t_c(\Phi_T(x))=e^{-T}t_c(x)$. It therefore remains in the compact
tube and exists for every $T\ge0$. Its length after time $T$ is at most
\[
 3C'|t_c(x)|^{1/3}e^{-T/3}
 \le3C'\epsilon^{1/3}e^{-T/3}.
\]
The flow converges uniformly to a continuous map $r:N\to W$,
with $r|_W=\mathrm{id}_W$. The same estimate gives continuity at
$W$ after extending every $\Phi_T$ by the identity there. The map
\[
 H(x,u)=
 \begin{cases}
 \Phi_{-\log(1-u)}(x),&0\le u<1,\\
 r(x),&u=1
 \end{cases}
\]
is continuous at $u=1$ by the uniform tail estimate. It has
$H(x,0)=x$, $H(x,1)\in W$, and $H(w,u)=w$ for $w\in W$,
which proves the strong deformation retraction.
\end{proof}

'''
head=r'\begin{proposition}[Connected cyclic covers and the cusp comparison]\hypertarget{tag-01S7}{}\label{inv:B3.1}'
edit(head,lemma+head,['inv:B3.1','inv:B3.3','I:lem:cusp-tube-contraction'],'Extract the already printed self-contained normal-crossing contraction before its first use, with the same vector field and explicit time reparametrization. Placeholder tag is for parent allocation.')
edit(r'\StatementRecord{inv:B3.1}{proved}{01S7}{\SeriesRef{inv:B3.3}, \SeriesRef{inv:B1.1}}',r'\StatementRecord{inv:B3.1}{proved}{01S7}{\cref{I:lem:cusp-tube-contraction}, \SeriesRef{inv:B1.1}}',['inv:B3.1'],'Replace the statement-level forward dependency by the extracted local input.',False)
edit('of the tube onto $W$ given in \\ref{inv:B3.3} identifies their fundamental groups,','of the tube onto $W$ in Lemma~\\ref{I:lem:cusp-tube-contraction} identifies their fundamental groups,',['inv:B3.1'],'The same contraction now precedes its first use; the induced fundamental-group map is unchanged.',False)
old=block(S.read_text(),'inv:B3.3');a=old.index('\\item The comparison with $N$ is given');b=old.index('\n\\item The constant-sheaf',a)
edit(old[a:b],'\\item Lemma~\\ref{I:lem:cusp-tube-contraction} gives the strong\ndeformation retraction $N\\to W$, fixing $W$ pointwise.\n',['inv:B3.3'],'Replace the second printed copy by invocation of the single complete earlier proof; all subsequent cohomology and attachment maps remain unchanged.')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();data=dict(created_utc=now,input_sha256=sha(S.read_text()),scope='Exposed complete original/current proof comparison, then extraction of the same contraction before first use. No new independent or computational credit. Parent must allocate TOPOLOGY-CUSP-TAG.',patches=patches)
(E/'S6_SERIES_PUBLISH_I_candidate11_cusp_guards.json').write_text(json.dumps(data,indent=2)+'\n')
rows=[]
for lab in ['inv:B3.1','inv:B3.3']:
 rows.append(dict(statement_id=lab,original_source_sha256=sha(orig),candidate11_source_sha256=sha(S.read_text()),original_complete_block=block(orig,lab),candidate11_complete_block=block(S.read_text(),lab),proposed_complete_block=block(s,lab),comparison='Full original and candidate11 statements and proofs actually read in this pass. All matrices, signs, collar maps, multiplicities, cohomology maps and conclusions are retained. inv:B3.1 now cites the same contraction before its first use. inv:B3.3 Step5 is represented by the full extracted lemma; remaining eight steps are unchanged.'))
archive=dict(created_utc=now,scope=data['scope'],blocks=rows,extracted_lemma_complete=lemma,exposure='The printed target proofs were already exposed. This is an exposed source rewrite comparison, never a derivation-before-proof check.',additional_verification='The displayed component bound follows from a_i/(sum a_j^2)<=1/sqrt(sum a_j^2), a_i=1/|z_i|; the existing tail bound yields the explicit H(x,u)=Phi[-log(1-u)] and its continuous endpoint. No program execution.',dependency_disposition='The old statement-level inv:B3.1->inv:B3.3->inv:B3.1 cycle was a forward location of a self-contained Step5, not a refutation of either proposition. The local contraction now precedes inv:B3.1.')
(E/'S6_SERIES_PUBLISH_I_candidate11_cusp_full_comparison.json').write_text(json.dumps(archive,indent=2)+'\n')
(E/'S6_SERIES_PUBLISH_I_candidate11_cusp_full_proofs.tex').write_text('% Original, candidate11 and proposed complete proofs; checking archive only.\n\n'+'\n\n'.join('% '+x['statement_id']+' ORIGINAL\n'+x['original_complete_block']+'\n\n% CANDIDATE11\n'+x['candidate11_complete_block']+'\n\n% PROPOSED\n'+x['proposed_complete_block'] for x in rows)+'\n\n% EXTRACTED LEMMA\n'+lemma)
(E/'S6_SERIES_PUBLISH_I_candidate11_cusp_comparison.md').write_text('# Cusp contraction: complete exposed proof comparison\n\n'+archive['exposure']+'\n\n'+archive['dependency_disposition']+'\n\n'+archive['additional_verification']+'\n\nThe original and candidate11 inv:B3.1 and inv:B3.3 complete proofs were read. The complete source blocks and proposed replacements are archived in the adjacent JSON/TeX files. No statement is refuted; no new experiment, independent check, or targeted check is claimed. Signed p is already defined globally by p=12l0−4l1−3l2; its use in inv:B3.1 is unchanged.\n')
# A single exposed association for the explicit proof rewrite, not for mere movement/reference formatting.
field=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
event=dict(statement_id='inv:B3.3',date='2026-11-21',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH topology-check agent',type='used and rechecked in this run',outcome='Full original/candidate11 inv:B3.1 and inv:B3.3 statements and proofs read; exposed extraction of inv:B3.3 Step5 before first use. Same vector field and tail bound, now with explicit component inequality and continuous homotopy H(x,u)=Phi[-log(1-u)]. All other matrices, signs, maps and conclusions unchanged. No independent, targeted or computational credit. Applied binding pending.',event_id='ce:publish-I-cusp-contraction-exposed-20261121',phase='Paper I rendered-reading proof restructuring',source_file=str(E/'S6_SERIES_PUBLISH_I_candidate11_cusp_comparison.md'),source_row='complete original/current/proposed inv:B3.1 and inv:B3.3 proof comparison',source_event_type='used and rechecked in this run',evidence_group='eg:publish-I-cusp-contraction-exposed')
with (D/'S6_SERIES_PUBLISH_I_candidate11_cusp_CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=field,delimiter='\t');w.writeheader();w.writerow(event)
print(json.dumps({'guards':len(patches),'source':data['input_sha256'],'complete_archived_blocks':len(rows),'new_exposed_rows':1}))
