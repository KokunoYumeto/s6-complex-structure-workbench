from pathlib import Path
import re, json, hashlib, datetime, csv

ROOT=Path('/workspace/scratch/653608133b22')
OUT=ROOT/'work/agents/i_analytic'
SRC=ROOT/'work/S6_SERIES_PUBLISH_I.tex'
original=(ROOT/'source/S6_SERIES_GRIND_I.tex').read_text()
base=SRC.read_text(); s=base
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
guards=[]; archives=[]
def add(old,new,reason,ids=(),count=1):
    global s
    assert s.count(old)==count,(reason,s.count(old),count)
    guards.append(dict(id=f'IA-RES-{len(guards)+1:02d}',old=old,new=new,expected_count=count,reason=reason,statement_ids=list(ids)))
    s=s.replace(old,new)
def block(text,key):
    p=text.index('\\label{'+key+'}')
    a=text.rfind('\\begin{',0,p)
    b=text.index('\\end{proof}',p)+len('\\end{proof}')
    return text[a:b]

# Complete reread comparisons are retained for the three proof changes.
targets=['push:src:A.2.1','push:src:A.2.2','ari:C.2.1']
before={k:block(base,k) for k in targets}
oldproof={k:block(original,k) for k in targets}

add(r'''fixing the bottom. The program \texttt{ab\_push\_fan.py} performs
this enumeration in rational arithmetic; intersections are tested
by all vertices of the combined barycentric halfspaces.''',r'''fixing the bottom. To test each pairwise intersection, write both
tetrahedra by their rational barycentric inequalities and enumerate
the vertices of the combined system. The intersection is their
common face exactly when each such vertex belongs to that face.''',
    'Retain the exact finite rational intersection algorithm and result; operative program belongs in the end table.', ['push:src:A.2.1'])
add(r'''not jointly flat. An earlier attempted witness using an orbit
of two-faces did not justify compatibility of intersecting
centres; its correction is retained in
\path{evidence/ab_push_correction_orbit_stars.md}.''',r'''not jointly flat.''',
    'Move the previous-attempt history to this record; retain the complete valid maximal-cone orbit construction.', ['push:src:A.2.1'])
add(r'''other chart $u=xb$, $y=bzv$. It has three smooth affine charts.
The assignments in \texttt{ab\_push\_local\_checks.py} verify
the equations and the map to $q=zv$ exactly. Exchanging the
chosen zero and infinity branches gives the other model.''',r'''other chart $u=xb$, $y=bzv$. Its three smooth affine charts map
to $(x,y,z,v,u;q)$ by
\[
\begin{aligned}
 (u,z,\lambda,y)&\longmapsto(uz\lambda,y,z,\lambda y,u;z\lambda y),\\
 (u,a,\nu,v)&\longmapsto(ua,\nu v,a\nu,v,u;a\nu v),\\
 (x,b,z,v)&\longmapsto(x,bzv,z,v,xb;zv).
\end{aligned}
\]
The first two are the conifold-resolution charts
$a=z\lambda$, $v=\lambda y$ and $z=a\nu$, $y=\nu v$.
Substitution gives $xy=uzv$ and $q=zv$ in every chart.
Exchanging the chosen zero and infinity branches gives the other model.''',
    'Replace the program assertion by its exact three affine morphisms, keeping the chosen conifold resolution and q-map.', ['push:src:A.2.2'])
add(r'''identification are \cref{fam:src:C.2.3}, \cref{fam:src:A.5.1}; the latter is also Theorem~1.4
(label \texttt{p2:thm:exact-period}) of
\cite{DuGuoKusakabeXie2026v1}. Its hypotheses specify precisely the
retained period family, affine finite twists and cusp collar. They
coincide with the marked family $X_c$; the normalization differs
only by the fixed choice of the particular solution, which does not
alter parameter differences. Version 2 drops that theorem; we infer
no mathematical conclusion from this omission.''',r'''identification are \cref{fam:src:C.2.3,fam:src:A.5.1}. The latter
is also \cite[Theorem~1.4, p.~3]{DuEtAl2026v1} under the explicit
parameter map of \cref{night:P5.7}: with
$\delta=\beta^{\rm part}-\beta_0$ and $a=c+\delta$, one has
$\Omega_a=\Pi_c$ and $a'-a=c'-c$. That comparison also identifies
the finite affine twists and the cusp collar.''',
    'Use the already compared exact source parameter morphism and locator; omit repeated version-history prose.', ['ari:C.2.1'])
add(r'''rational-cusp argument proved in Proposition~\ref{push:src:D.1.1}. The phrase ``up to the
radius'' therefore means the open punctured disc, not holomorphy on
its bounding circle or at its central pole.''',r'''rational-cusp argument proved in Proposition~\ref{push:src:D.1.1}.''',
    'The statement already specifies the punctured open disc and pole; remove an explanation of wording no longer in the statement.', ['ari:C.2.1'])
add(r'\begin{proposition}[exact nomes and continuation radius]',r'\begin{proposition}[Exact nomes and continuation radius]','Capitalize the statement title.')
add(r'\begin{proposition}[distribution under isogenies]',r'\begin{proposition}[Distribution under isogenies]','Capitalize the statement title.')
add('proves independence of $m$, not merely numerical agreement.','proves independence of $m$.','Remove numerical-verification production wording without changing the argument.')
add(r'\item For clarity, the recurrence used by the exact program is',r'\item The division-polynomial recurrence is','State the mathematical algorithm directly.')
add('holds by the checked isogeny computation at $i$.',r'holds by \cref{ari:C.1.2}.','Replace generic checking language by the exact existing isogeny result.')
add('local maximum described in C.3.',r'local maximum described in \cref{ari:C.3.1}.','Resolve a stale literal section reference.')
add(r'given rules out a critical point; at $i$, $W=p=0$ but $3Wp-2g_2=-2g_2\ne0$, and C.3 gives',r'given rules out a critical point; at $i$, $W=p=0$ but $3Wp-2g_2=-2g_2\ne0$, and \cref{ari:C.3.1} gives','Resolve the same stale literal section reference in the proof.')
add('No conjectural lower bound is used in the preceding results.\n','','The preceding sentence already states the exact remaining open step; omit redundant defensive status prose.')

# Bibliographic identity maps operate on the same editions.  Their complete old
# entries and removed verification history are preserved below, not newly verified.
def entry(text,key):
    ms=list(re.finditer(r'\\bibitem(?:\[[^\n]*(?:\n[^\n]*)*?\])?\{([^}]+)\}',text))
    # A simpler anchored entry finder avoids consuming a later item.
    ms=list(re.finditer(r'^\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}',text,re.M))
    m=next(m for m in ms if m.group(1)==key)
    nxt=next((n.start() for n in ms if n.start()>m.start()),text.index(r'\end{thebibliography}',m.start()))
    return text[m.start():nxt]
aliases={'DuGuoKusakabeXie2026v1':'DuEtAl2026v1','Grauert1960D':'Grauert60','SS00':'SchroeerSiebert2002Root'}
for oldkey,newkey in aliases.items():
    e=entry(s,oldkey)
    archives.append(dict(kind='duplicate bibliographic entry',old_key=oldkey,canonical_key=newkey,old=e,canonical_before=entry(s,newkey),scope='Exact author/title/edition or version/URL identity within the supplied bibliography; no new primary-source reading claimed.'))
    add(e,'',f'Merge the identical-edition bibliography entry {oldkey} into {newkey}.')
    token='{'+oldkey+'}';replacement='{'+newkey+'}'
    n=s.count(token)
    if n:add(token,replacement,f'Exact citation-key alias {oldkey} to {newkey}; retain each citation locator.',count=n)

for key in ['Grauert60','SchroeerSiebert2002Root']:
    e=entry(s,key);n=e.replace(r'{\natexlab{b}}','')
    add(e,n,f'Remove same-year disambiguation after merging the duplicate {key} entry.')
e=entry(s,'DuEtAl2026v1')
add(e,e.replace('v1, superseded version,','v1,'),'Identify the exact version without a repeated editorial status annotation.')

history_starts={
 'AbateBracciSuwaTovena2010Atiyah':r'\newblock Verified at the cited scope:',
 'AtiyahSinger1968IIIE':r'\newblock Additional verified scope',
 'ErbanVanGorder2021':r'\newblock Primary PDF opened',
}
for key,prefix in history_starts.items():
    e=entry(s,key);a=e.index(prefix);b=e.index(r'\newblock \emph{Verified}.',a)
    old=e[a:b]
    archives.append(dict(kind='historical verification prose',key=key,old=old,scope='Historical prose relocated verbatim; none of its primary-reading assertions is newly adopted by this audit.'))
    add(old,'','Move historical retrieval/reading prose into the record; bibliographic identity and operative body locators remain.')
marker='\\newblock \\emph{Verified}.\n'
marker_count=s.count(marker)
add(marker,'','Remove blanket printed verification labels; scoped source receipts remain in the records.',count=marker_count)

after={k:block(s,k) for k in targets}
for k in targets:
    archives.append(dict(kind='full proof rewrite comparison',statement_id=k,original_locator='source/S6_SERIES_GRIND_I.tex :: '+k,current_locator='work/S6_SERIES_PUBLISH_I.tex :: '+k,original=oldproof[k],before=before[k],after=after[k],original_sha256=sha(oldproof[k]),before_sha256=sha(before[k]),after_sha256=sha(after[k]),reading_class='Full exposed-proof reread, not a new independent derivation.'))

payload=dict(created_utc=now,base=str(SRC),base_sha256=sha(base),policy='Guarded proposals only. Root source untouched. Apply guards sequentially; expected_count is operative, including the blanket bibliography footer removal.',guards=guards)
(OUT/'S6_SERIES_PUBLISH_I_residual_guards.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_residual_archive.json').write_text(json.dumps(dict(created_utc=now,base_sha256=sha(base),archives=archives),indent=2,ensure_ascii=False)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_residual_preview.tex').write_text(s)

notes=f'''# Paper I: bounded residual audit and final local-model presentation

Date: {now}. Source read: `{SRC}`, SHA256 `{sha(base)}`. All changes are proposals; the root source was not written.

## Scope actually read

Read the full current A2.1 and A2.2 statements and every proof step, compared them with the attached original and the existing frozen/check records, and read every proposed replacement. These are exposed-proof rereads. The prior strict checks and post-reading different-method calculation retain their separately logged scopes; this presentation pass gains no independent or computation credit.

Read the full current and original ari:C.2.1 statement and proof, the full existing night:P5.7 exact source comparison, and the short replacements. The source change is the explicit translation a=c+delta, delta=beta_part-beta_0, with Omega_a=Pi_c and a'-a=c'-c; the finite twists/cusp identifications remain in P5.7. No new source theorem, chronology authentication, or mathematical result is asserted.

Read the bounded residual arithmetic/analytic hits, all 127 bibliography titles, the complete duplicate entries and every removed historical paragraph. The exact current final open part was read: it states the unresolved arithmetic questions in prose and keeps the unconditional period-field relation separate by an explicit reference. No open conjecture is promoted to a theorem. This was a source-text audit, not rendered-page QA.

## A2.1 comparison

The six prism triangulations, three with the specified bottom diagonal, two period-compatible rows, determinant checks, exclusion of all new rays under the three stated restrictions, converse, and the full infinite orbit-star construction remain unchanged. The program sentence becomes the rational barycentric-halfspace intersection algorithm already used there. The obsolete failed-two-face narrative moves verbatim to the archive. The complete old and proposed proofs are preserved in `S6_SERIES_PUBLISH_I_residual_archive.json`.

## A2.2 exact morphisms

The total node is xy=uzv with q=zv. After x=ua the conifold is ay=zv. Its two charts are a=z*lambda, v=lambda*y and z=a*nu, y=nu*v; the third original blowup chart is u=x*b, y=b*z*v. Their maps are printed explicitly in the guard. Direct substitution gives xy=uzv and q=zv in all three. On the overlap lambda*nu=1 and a=z*lambda, v=lambda*y, so these are the same conifold resolution charts as the preceding normalization calculation, with exact coordinate correspondence (X,B)=(a,y). The zero/infinity interchange remains the map to the second model. Properness, flatness, central geometry, normal product, exceptional chain and final birational comparison are retained verbatim. No separate computation event is claimed for this exposed substitution.

The historical operative programs are `replay_family_applications/ab_push_fan.py` and `replay_family_applications/ab_push_local_checks.py` in the supplied code tree. Their end-table rows should cite A2.1 and A2.2 respectively and retain the independently authenticated repository paths supplied by the topology/provenance program inventory. This record does not claim a fresh download or execution of those historical programs.

## Bibliography changes and limits

Exact same-edition key maps: DuGuoKusakabeXie2026v1 -> DuEtAl2026v1; Grauert1960D -> Grauert60; SS00 -> SchroeerSiebert2002Root. For the last two, this follows the attached citation-fix key map as well as identical title/author/year/URL metadata. Every operative locator stays at its citation. The Grauert historical paragraph is preserved inside the complete removed duplicate entry. Three additional historical verification paragraphs and {marker_count} remaining blanket Verified footers are removed from the printed bibliography. Before duplicate deletion there were 116 such footers. None is counted as a new verification.

The v1/v2 DGKX entries remain distinct by their exact version URLs. Kajiwara 2008a/b are different supplied titles, publication venues and page ranges and are both retained. BM95AB/BM97 are flagged but retained: they have the same title/arXiv URL and preprint-vs-journal metadata, but neither this reader nor the provenance agent has a current-run primary receipt for the exact edition/pagination correspondence. No unverified merge or journal-page conversion is made. Oda's official retypeset-edition pagination sentence, McHugh's preprint-pagination sentence and Conrad's dated edition identification are bibliographic edition data and remain.

## Other guarded wording

Two statement-title initial capitals; the exact division-polynomial recurrence replaces program wording; the local isogeny value cites ari:C.1.2; two literal C.3 references resolve to ari:C.3.1; numerical-agreement and redundant final open-status wording are removed. These small presentation changes add no check events. No mathematical label/tag is removed by this batch.

## Remaining work

Root integration and rendered-page reading remain. The end-table insertion is root-owned and was not yet in the source snapshot read. The BM edition-identity question remains explicitly flagged. This bounded audit does not claim to inspect untouched topology push A/B material outside A2.1/A2.2 or to supply a new check of inv:B1.0.
'''
md=OUT/'S6_SERIES_PUBLISH_I_residual_comparison.md';md.write_text(notes)
group='eg:publish-ianalytic-residual-'+sha(notes)[:16]
outcomes={
 'push:src:A.2.1':'PASS: EXPOSED-PROOF REREAD ONLY. Full original/current/proposed proof compared. Finite barycentric intersection algorithm retained explicitly, all six/three/two counts and restrictions unchanged; full valid orbit-star construction retained, failed prior-attempt narrative archived. No fresh independent/computation credit.',
 'push:src:A.2.2':'PASS: EXPOSED-PROOF REREAD ONLY. Full original/current/proposed proof compared. Exact three affine chart morphisms replace a historical-program assertion; direct substitutions preserve xy=uzv and q=zv, with (X,B)=(a,y) and reciprocal conifold coordinates on the overlap. All properness, joint-flatness, central/normalization/normal-product and extra flop assertions retained. No fresh independent/computation credit.',
 'ari:C.2.1':'PASS: EXPOSED-PROOF REREAD ONLY. Full original/current/proposed proof and existing P5.7 source comparison read. The known exact-period input now cites v1 Theorem1.4 p3 under the explicit map a=c+delta, Omega_a=Pi_c, a-prime minus a=c-prime minus c. Finite twists/cusp correspondence remains cited; duplicate version-history and obsolete radius-wording explanation archived. All nome/radius/natural-boundary assertions unchanged.'}
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
rows=[]
for k in targets:
    row=dict(statement_id=k,date='2026-11-21',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort, S6_SERIES_PUBLISH/v_analytic_check',type='used and rechecked in this run',outcome=outcomes[k],event_id='ce:publish-ianalytic-'+sha(group+k)[:16],phase='S6_SERIES_PUBLISH',source_file=str(md),source_row='',source_event_type='used and rechecked in this run',evidence_group=group);rows.append(row)
with (OUT/'S6_SERIES_PUBLISH_I_residual_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
receipt=dict(completed_utc=now,source_sha256=sha(base),proposed_source_sha256=sha(s),guard_count=len(guards),bibliography_original_count=127,bibliography_proposed_count=len(re.findall(r'^\\bibitem',s,re.M)),original_verified_marker_count=116,remaining_verified_marker_count=s.count(r'\emph{Verified}'),same_edition_key_map=aliases,unresolved_bibliographic_candidate=['BM95AB','BM97'],comparison_sha256=sha(notes),evidence_group=group,events=rows,root_source_unchanged=SRC.read_text()==base,scope='Bounded source audit and exposed proof rewrite comparison only; no rendered-page QA, independent reproof or new computational event.')
(OUT/'S6_SERIES_PUBLISH_I_residual_comparison.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:receipt[k] for k in ['source_sha256','guard_count','bibliography_proposed_count','remaining_verified_marker_count','root_source_unchanged','evidence_group']},indent=2))
