"""Locate working-edition topology results without treating extraction as checking."""
from pathlib import Path
import re, csv, json, hashlib

ROOT=Path('/workspace/scratch/037cd144174c')
OUT=ROOT/'deliverables/work/maps_audit'
files=['integral_leray','topology_reduction','cusp_toric_cover_completion',
       'cusp_globalization_replacement','cusp_cone_sphere_routes',
       'cusp_sphere_route_strengthening','cusp_s12_carrier_homotopy']
env_re=re.compile(r'\\begin\{(theorem|proposition|lemma|corollary|claim|definition|remark|conjecture|example|construction|computation|test|auditrecord)\}(?:\s*\[([^]]*)\])?')
rows=[]; labels=[]
mapping={
'thm:p0-integral-specialization':('MAPS:B.5.1; MAPS:B.5.2','Same specialization input; retain independent nearby-cycle proof in Paper I.'),
'prop:leray-e2':('MAPS:B.5.2','Alternative Leray route; retain all terms and integral lattices.'),
'lem:first-transgression':('MAPS:B.5.2','Leray proof of primitive attaching coefficient; retain as independent proof.'),
'lem:higher-transgressions':('MAPS:B.5.2','Leray proof of higher attaching coefficients; retain independently.'),
'thm:h2-vanishing':('MAPS:B.5.2','Same integral sphere conclusion, independent route.'),
'prop:geometric-pi1':('MAPS:B.5.2','Same actual fundamental-group computation; full geometric presentation retained.'),
'cor:candidate-sphere':('MAPS:B.5.2','Sphere and Chern-number consequence; Paper I foundation.'),
'prop:topological-spine':('MAPS:B.5.1','Related cusp mapping-cylinder model; compare proofs before deduplication.'),
'lem:collapse-straightening':('MAPS:B.5.1','Auxiliary straightening proof used by working collapse route.'),
'lem:positive-collapse':('MAPS:B.5.1','Positive toric quotient; compare Waldhausen route in final run.'),
'lem:phase-spread-collapse':('MAPS:B.5.1','Alternative equivariant collapse proof, retain.'),
'prop:verified-cellular-collapse':('MAPS:B.5.1','Explicit cellular collapse, retain full chain model.'),
'prop:verified-collapse-homology':('MAPS:B.5.1; MAPS:B.5.2','Integral induced collapse maps, retain independent calculation.'),
'thm:collapse-equals-specialization':('MAPS:B.5.1; MAPS:B.5.2','Comparison of distinct proof routes, not merely duplicate statement.'),
'record:vankampen':('MAPS:B.5.2','Recorded audit assertion; does not replace a new proof check.'),
'prop:actual-finite-band-maps':('MAPS:B.5.2','Actual finite-band maps; retain primitive bases and signs.'),
'prop:cusp-mv-blocks':('MAPS:B.5.2','Actual cusp blocks; retain all coefficients.'),
'thm:mv-leray-comparison':('MAPS:B.5.2','Comparison result absent as separate final-row claim; retain.'),
'lem:cohomological-closure':('MAPS:B.5.2','General classical six-dimensional closure lemma; re-derivation appendix.'),
'thm:sphere-recognition':('MAPS:B.5.2','General sphere recognition; classical input and application separated.'),
'cor:abstract-s6':('MAPS:B.5.2','Abstract application of exact inputs; preserve hypotheses.'),
'cor:candidate-mv-sphere':('MAPS:B.5.2','Independent Mayer–Vietoris certificate; do not discard second proof.'),
'cusp-cover-extension-theorem':('MAPS:C.1.1','Corrected Kummer completion; final run extends scope.'),
'cusp-cover-naive-action-failure':('MAPS:C.1.1','Counterexample to unmodified action; retain computation.'),
'cusp-cover-global-scope':('MAPS:C.1.2; MAPS:C.1.3; MAPS:C.1.4; MAPS:C.1.5','Earlier limitation resolved in final run; preserve provenance and corrected scope.'),
'cusp-spec-globalization-obstruction':('MAPS:A.1.1; MAPS:A.1.2; MAPS:A.1.3; MAPS:B.3.3','Only parts taken over: metric limits, minimal-copy and fibre-product statements remain working-edition results.'),
'cusp-s12-one-copy-invariant':('MAPS:B.3.2','This is the angle-forgetting local cusp map, not repaired global circle quotient.'),
'cusp-null:thm':('MAPS:B.3.2','Same nullity conclusion, explicit framed-nullbordism proof is distinct and must be retained.'),
}
for name in files:
    p=ROOT/'sources/workbench'/f'{name}.tex'; t=p.read_text(); ms=list(env_re.finditer(t))
    for i,m in enumerate(ms):
        close=t.find('\\end{'+m.group(1)+'}',m.end())
        if close<0: raise RuntimeError((p,m.start()))
        close+=len('\\end{'+m.group(1)+'}')
        segment=t[m.start():close]
        lab=re.search(r'\\label\{([^}]+)\}',segment)
        source_id=lab.group(1) if lab else f'{name}:L{t.count(chr(10),0,m.start())+1}'
        next_start=ms[i+1].start() if i+1<len(ms) else len(t)
        proof=re.search(r'\\begin\{proof\}',t[close:next_start])
        ps=close+proof.start() if proof else None
        pe=t.find('\\end{proof}',ps)+len('\\end{proof}') if ps is not None else None
        if pe is not None and pe>next_start: pe=None
        taken,note=mapping.get(source_id,('','No final-run row identified yet; preserve as separate working result.'))
        paper='I appendix; III cross-reference' if name in ['integral_leray','topology_reduction'] else 'III'
        row=dict(source_run='working_edition',source_id=source_id,source_file=str(p.relative_to(ROOT)),
                 start_line=t.count('\n',0,m.start())+1,end_line=t.count('\n',0,close)+1,
                 kind=m.group(1),title=re.sub(r'\s+',' ',m.group(2) or ''),
                 statement=segment,proof_start_line=(t.count('\n',0,ps)+1 if ps is not None else ''),
                 proof_end_line=(t.count('\n',0,pe)+1 if pe is not None else ''),paper=paper,
                 taken_over_by=taken,overlap_status=('partial or same conclusion; proof comparison pending' if taken else 'additional working-edition result'),
                 recorded_checks='Source Verified/AuthorSelfCheck markers retained; reader-specific matching pending.',
                 your_check='Inventory locator established; no mathematical pass inferred.',
                 check_outcome='pending proof and citation audit',notes=note,
                 source_sha256=hashlib.sha256(p.read_bytes()).hexdigest())
        rows.append(row)
    for m in re.finditer(r'\\label\{([^}]+)\}',t):
        n=t.count('\n',0,m.start())+1
        owner=next((r['source_id'] for r in reversed(rows) if r['source_file']==str(p.relative_to(ROOT)) and r['start_line']<=n and (not r['proof_end_line'] or n<=r['proof_end_line'])), '')
        labels.append(dict(source_file=str(p.relative_to(ROOT)),label=m.group(1),line=n,containing_result=owner))

# The course has a proper machine-readable result register. Preserve its exact IDs.
course=ROOT/'sources/codex_workspace/courses/CG-S6'; cat=json.loads((course/'course.json').read_text())
for r in cat['results']:
    if not r['id'].startswith(('CG-S6-07-','CG-S6-11-')): continue
    src,_,anchor=r['source'].partition('#'); p=course/src; t=p.read_text()
    marker='{#'+anchor+'}'; pos=t.find(marker); line=t.count('\n',0,pos)+1 if pos>=0 else ''
    rows.append(dict(source_run='course_CG-S6',source_id=r['id'],source_file=str(p.relative_to(ROOT)),start_line=line,end_line='',kind='course registered result',title=r['statement'],statement=r['statement'],proof_start_line=line,proof_end_line='',paper='I appendix; III cross-reference' if r['id'] in ['CG-S6-07-HOMOLOGY','CG-S6-07-HOMOTOPY'] else 'III classical appendix',taken_over_by='MAPS:B.5.2' if r['id'].startswith('CG-S6-07-') else '',overlap_status='classical re-derivation and application; retain proof',recorded_checks='sources/notes/G2_notes.md §1.2 or §1.4: Claude Fable 5.2, 12 November 2026; effort must be joined from WHO_WROTE_WHAT (not inferred). Source author self-check only; exact scope in G2 notes.',your_check='Course register and source anchor located.',check_outcome='pending proof and citation audit',notes='Exact source provenance: GPT-6 Astra (OpenAI), Ultra, October 2026; differs from umbrella August–September working-edition attribution and must be preserved.',source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))

# Every section that actually proves the sphere-twist route, including its examples.
p=course/'src/sphere-twists-and-the-original-smooth-six-sphere-comparison.md';t=p.read_text()
heads=list(re.finditer(r'^#{2,3} (\d+(?:\.\d+)?\.?[^\n]*)',t,re.M))
for i,m in enumerate(heads):
    if m.group(1).startswith('9.'):continue
    end=heads[i+1].start() if i+1<len(heads) else len(t)
    anchor=re.search(r'\{#([^}]+)\}',m.group(1));sid=anchor.group(1) if anchor else 'sphere-twist-'+m.group(1).split()[0]
    rows.append(dict(source_run='course_CG-S6',source_id=sid,source_file=str(p.relative_to(ROOT)),start_line=t.count('\n',0,m.start())+1,end_line=t.count('\n',0,end),kind='numbered proof section',title=m.group(1),statement=m.group(1),proof_start_line=t.count('\n',0,m.start())+1,proof_end_line=t.count('\n',0,end),paper='III classical appendix',taken_over_by='CG-S6-07-SMOOTH',overlap_status='expanded proof of registered course result; must retain',recorded_checks='sources/notes/G2_notes.md §1.3: whole chapter read by Claude Fable 5.2, 12 November 2026; §G2-3 records its proof analysis. Exact effort to join from WHO_WROTE_WHAT.',your_check='Inventory and explicit source provenance located.',check_outcome='pending stepwise proof/citation comparison',notes='Source header: GPT-6 Astra (OpenAI), Ultra, 11 October 2026. Theta6 classical, not new; no claim of fibration-adapted handles.',source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))

# G2-8 is a mathematical claim in the reader record, expressly absent from the course.
p=ROOT/'sources/notes/G2_notes.md';t=p.read_text();pos=t.index('### G2-8.');end=t.index('\n## ',pos)
rows.append(dict(source_run='working_edition_reader_extension',source_id='G2-8',source_file=str(p.relative_to(ROOT)),start_line=t.count('\n',0,pos)+1,end_line=t.count('\n',0,end),kind='classical corollary',title='Almost complex homotopy class of J_X',statement=t[pos:end],proof_start_line=t.count('\n',0,pos)+1,proof_end_line=t.count('\n',0,end),paper='III',taken_over_by='',overlap_status='not present in run result tables',recorded_checks='Claude Fable 5.2, 12 November 2026; statement and short argument in G2-8; effort to join from WHO_WROTE_WHAT.',your_check='Re-derived using relative section obstruction theory on S6 × I, fibre SO(6)/U(3)=CP3; pi6(CP3)=0 from Hopf fibration.',check_outcome='mathematical argument checked; exact source identity SO(6)/U(3)=CP3 to cite or derive',notes='Compare the orientation-compatible octonionic structure: source labelled octonionic field has opposite orientation. Do not identify sections with maps into a globally trivial twistor bundle.',source_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))

OUT.mkdir(parents=True,exist_ok=True)
with (OUT/'working_results_inventory.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(OUT/'working_results_inventory.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
with (OUT/'working_all_labels.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(labels[0]));w.writeheader();w.writerows(labels)
print(f'{len(rows)} result/numbered-proof rows; {len(labels)} TeX label occurrences.')
