"""Prepare eight owner-local editorial comparisons and exact reversible guards."""
from pathlib import Path
import csv,datetime,difflib,hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch04_working'
P='S6_SERIES_PUBLISH_II_A2_D09_D04_batch04'
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
sha=lambda v:hashlib.sha256(v.encode() if isinstance(v,str) else v).hexdigest()
source_sha=sha(s)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(name,value):
    (OUT/(P+'_'+name+'.json')).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
owners={'02XE':'night:P4.40','02XF':'night:P4.41','02XK':'night:P4.46','02XL':'night:P4.47',
        '02XN':'night:P4.49','02Y9':'night:P4R.16','02YA':'night:P4R.17','02YB':'night:P4R.18'}
blocks={tag:(OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_before.tex').read_text() for tag in owners}
for tag,b in blocks.items(): assert s.count(b)==1,tag
guards=[]
def add(old,new,tag,classes,why,instances=None,owner=None):
    assert old!=new and s.count(old)==1,(tag,old[:90],s.count(old))
    a=s.index(old);b=a+len(old)
    g=dict(id=f'A2-ED04-{len(guards)+1:03d}',owner=owner or owners.get(tag,'Programs'),tag=tag,
           old=old,new=new,old_sha256=sha(old),new_sha256=sha(new),expected_count=1,
           defect_ids=classes,reason=why,source_snapshot_sha256=source_sha,
           source_character_span=[a,b],source_byte_span=[len(s[:a].encode()),len(s[:b].encode())],
           source_line_span=[s.count('\n',0,a)+1,s.count('\n',0,b)+1],instances=instances or [])
    guards.append(g);return g

# Exact historical reference names already identify the same permanent labels.
pat=re.compile(r'(?<![\w:.{\\])P4R?\.\d+(?!\d|\.\d)')
reference_map=[]
for tag,body in blocks.items():
    for line in body.splitlines():
        matches=list(pat.finditer(line))
        if not matches:continue
        changes=[]
        def sub(m):
            target='night:'+m.group(0)
            assert '\\label{'+target+'}' in s,target
            prefix=line[:m.start()].strip()
            command='Cref' if prefix in ['',r'\item'] else 'cref'
            rep='\\'+command+'{'+target+'}'
            changes.append(dict(old=m.group(0),new=rep,target=target,owner=owners[tag]))
            return rep
        new=pat.sub(sub,line)
        range_old=r'\cref{night:P4.47}--\cref{night:P4.48}'
        range_new=r'\cref{night:P4.47,night:P4.48}'
        if range_old in new:
            new=new.replace(range_old,range_new)
            for change in changes:
                if change['target'] in ['night:P4.47','night:P4.48']:
                    change['new']=range_new
        add(line,new,tag,['D04'],'Resolve each raw historical statement reference to its identical existing permanent statement label.',changes)
        reference_map.extend(changes)

add('At a point of an actual support in Part~4.2, suppose the',
    'At a point of a support in the standing setting of\n\\cref{def:II:standing-torus-fibration}, suppose the',
    '02XF',['D05','D08'],'Replace the historical part designation by the existing standing setting, preserving the ambient support domain.')
add('In the requested full-fibration classes, a support with\npositive-genus ruled resolution cannot have positive\nEuler number and generic transverse type $D_4$ along\nevery component of its critical curve.',
    'In the standing setting of \\cref{def:II:standing-torus-fibration},\nsuppose every reduced fibre support is irreducible or has normal\ncrossings. A support with positive-genus ruled resolution cannot\nhave positive Euler number and generic transverse type $D_4$\nalong every component of its critical curve.',
    '02XK',['D05'],'Spell out the exact irreducible/normal-crossing full-fibration domain identified by the attached P4.46 and P4.26 metadata rows and the standing definition.')

# The old paragraph contains a mathematical boundary example, retained here
# with its exact local coordinates instead of its historical process wording.
boundary=r'''At a generic boundary point $(t,0,0)$ of the $x$-axis,
the numbers $t$, $G_y$, $G_z$, and $U$ are nonzero.
For small $\epsilon\ne0$, the equations $G=\epsilon$ and
$h=0$ on this transverse slice have two distinct solutions:
one has $y=0$, and the other has $z=0$. The implicit-function
theorem gives each solution because $G_z$ and $G_y$ are units,
respectively. Their remaining coordinates are nonzero since
$G(t,0,0)=0$. Since $h=tyz$, the two Jacobians are
\[
 \left.\det\frac{\partial(G,h)}{\partial(y,z)}\right|_{y=0}
       =-tzG_z,\qquad
 \left.\det\frac{\partial(G,h)}{\partial(y,z)}\right|_{z=0}
       =tyG_y.
\]
Both are nonzero. A local square root of the unit $U$ makes
$(u,v)=(G-\epsilon,h\sqrt U)$ analytic coordinates at each
point, and the perturbed transverse equation is
\[
 (G-\epsilon)^2+h^2U=u^2+v^2=(u+iv)(u-iv).
\]
The invertible map $(u,v)\mapsto(u+iv,u-iv)$ therefore identifies
each of these two germs with an ordinary node. The same argument
applies on the other axes.

'''
anchor='\\item We exclude $U(0)=0$ by a deformation that keeps the\nthree axes fixed. Add an arbitrarily small generic'
new='\\item We exclude $U(0)=0$ by a deformation that keeps the\nthree axes fixed.\n\n'+boundary+'Add an arbitrarily small generic'
add(anchor,new,'02XL',['D01','D09'],'Move the actual two-node boundary example from the production paragraph into its owning proof, providing the explicit invertible coordinate maps. The seven original proof items and all their calculations remain.')

for tag,body in blocks.items():
    following=(OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text()
    end=s.index(body)+len(body)
    assert s[end:end+len(following)]==following
    next_at=end+len(following);next_line=s[next_at:s.find('\n',next_at)]
    # Preserve subsection headings verbatim, removing only the program paragraph.
    at=following.find('\\subsection')
    retained='\n\n'+following[at:] if at>=0 else '\n\n'
    old='\\end{proof}'+following+next_line
    new='\\end{proof}'+retained+next_line
    classes=['D09']
    if tag=='02XE':classes+=['D02','D08']
    if tag in ['02XF','02XL']:classes+=['D01']
    add(old,new,tag,classes,'Move the exact historical program description and output/history claims to Programs and records. Preserve all mathematical assertions; XL boundary content is now explicitly proved in the owning item, and XE retains its A1 hypothesis.')
    (OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').write_text(retained)

programs=[
 ('curve_excess','First-jet hyperplanes and conductor Euler excess',r'\cref{ii:excess-one-curve-germs,night:P4.40}'),
 ('a3_node','Nodal Hessian defects, adjugates and normalization',r'\cref{night:P4.41}'),
 ('uniform_sectors','Uniform transverse-sector Hessians and defect bounds',r'\cref{night:P4.42,night:P4.44,night:P4.45,night:P4.46}'),
 ('a3_three_axes','Conic polar and three-axis conductor matrices',r'\cref{night:P4.47,night:P4.48,night:P4.49}'),
 ('a3_missing_coefficient','Colon ideals, normalization relations and polar Hessians',r'\cref{night:P4.49}'),
 ('a3_tacnode_line','Tacnode-line conormal elementary divisors',r'\cref{night:P4R.16}'),
 ('a3_delta4','Delta-four curve ideals and conormal lattices',r'\cref{night:P4R.17}'),
 ('horizontal_primary','Primary conductor graph counts',r'\cref{night:P4R.18}'),
]
retrieval=json.loads((OUT/'S6_SERIES_PUBLISH_II_A2_batch04_program_retrieval.json').read_text())
prefix=r'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/'
directory='pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/'
rows=[]
shared_program_rows={
    'curve_excess':'S6_SERIES_PUBLISH_II_A2_P206_curve_algebra.py',
    'horizontal_primary':'S6_SERIES_PUBLISH_II_A2_YB_original_graph.py',
}
for name,description,refs in programs:
    r=next(r for r in retrieval['files'] if r['name']==name+'.py')
    assert r['http_status']==200 and r['url'].endswith(directory+name+'.py')
    assert not re.search(r'\\(?:nolinkurl|path)\{'+re.escape(name+'.py')+r'\}',s[s.index('\\section*{Programs}'):])
    link='\\href{'+prefix+directory+name+'.py}{\\nolinkurl{'+name+'.py}}'
    if name in shared_program_rows:
        existing_name=shared_program_rows[name]
        matching=[line for line in s[s.index('\\section*{Programs}'):].splitlines(True)
                  if '\\nolinkurl{'+existing_name+'}' in line]
        assert len(matching)==1,(name,matching)
        old=matching[0]
        assert old.endswith(' \\\\[3pt]\n')
        new=old[:-len(' \\\\[3pt]\n')]+'; '+link+' \\\\[3pt]\n'
        add(old,new,'',['D09'],'Cite the opened historical program once in the existing row for the same computation, preserving the current verifier link and exact mathematical scope.',owner='Programs')
    else:
        rows.append(description+' ('+refs+') & '+link+' \\\\[3pt]\n')
name='S6_SERIES_PUBLISH_II_A2_D09_batch04_boundary_nodes.py'
rows.append('Transverse nodes of a shifted quadratic square (\\cref{night:P4.47}) & \\href{'+prefix+'code/'+name+'}{\\nolinkurl{'+name+'}} \\\\[3pt]\n')
program_text=''.join(rows)
(OUT/(P+'_Programs_rows.tex')).write_text(program_text)
anchor='\\end{longtable}}\n\n\\begin{thebibliography}{99}'
add(anchor,program_text+anchor,'',['D09'],'Append six opened historical program paths and the new bounded boundary-coordinate verifier; two further historical paths share existing rows for their exact computations. Use the shared commit macro.',owner='Programs')

# Guard intervals must be disjoint in the receiving snapshot.
ordered=sorted(guards,key=lambda g:g['source_character_span'][0])
for a,b in zip(ordered,ordered[1:]):assert a['source_character_span'][1]<=b['source_character_span'][0],(a['id'],b['id'])
candidate=s
for g in guards:
    assert candidate.count(g['old'])==1,g['id'];candidate=candidate.replace(g['old'],g['new'])
inverse=[]
for g in reversed(guards):
    assert candidate.count(g['new'])==1,(g['id'],'inverse',candidate.count(g['new']))
    inverse.append(dict(id=g['id']+'-inverse',old=g['new'],new=g['old'],expected_count=1))
    candidate=candidate.replace(g['new'],g['old'])
assert candidate==s

preservation=[]
for tag,old in blocks.items():
    new=old
    local=[g for g in guards if g['tag']==tag and g['old'] in old]
    for g in local:
        assert new.count(g['old'])==1;new=new.replace(g['old'],g['new'])
    (OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').write_text(new)
    following_old=(OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_before.tex').read_text()
    following_new=(OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').read_text()
    (OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_exact.diff').write_text(''.join(difflib.unified_diff((old+following_old).splitlines(True),(new+following_new).splitlines(True),fromfile=tag+'_before',tofile=tag+'_after')))
    display=lambda x:re.findall(r'\\\[(.*?)\\\]',x,re.S)
    before_displays=display(old);after_displays=display(new)
    it=iter(after_displays);assert all(any(z==d for z in it) for d in before_displays),tag
    anchors=lambda x:re.findall(r'\\(?:label|hypertarget|tag)\{[^}]*\}',x)
    equations=lambda x:re.findall(r'\\eqref\{[^}]*\}',x)
    enum=lambda x:re.findall(r'\\begin\{enumerate\}(?:\[[^\n]*\])?',x)
    assert anchors(old)==anchors(new) and equations(old)==equations(new) and enum(old)==enum(new)
    assert old.count('\\item')==new.count('\\item')
    assert not pat.search(new),tag
    preservation.append(dict(owner=owners[tag],tag=tag,before_sha256=sha(old),after_sha256=sha(new),
        before_bytes=len(old.encode()),after_bytes=len(new.encode()),items_preserved=old.count('\\item'),
        bracket_displays_preserved=len(before_displays),new_bracket_displays=len(after_displays)-len(before_displays),
        all_tags_labels_equation_references_and_enum_formats_preserved=True,
        proof_guard_count=len(local),following_paragraph_removed=True))
dump('guards',guards);dump('inverse_guards',inverse);dump('preservation',preservation);dump('reference_map',reference_map)
with (OUT/(P+'_defects.tsv')).open('w',newline='') as f:
    fields=['id','type','owner','tag','guard_id','old_text','new_text','source_line','status']
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
    for g in guards:
        for d in g['defect_ids']:
            entries=g['instances'] if d=='D04' else [dict(old=g['old'],new=g['new'])]
            for j,e in enumerate(entries,1):
                w.writerow(dict(id=g['id']+'-'+d+'-'+str(j),type=d,owner=g['owner'],tag=g['tag'],guard_id=g['id'],old_text=e['old'],new_text=e['new'],source_line=g['source_line_span'][0],status='proposed; no canonical write'))
dump('verification',dict(created_utc=now,source_snapshot_sha256=source_sha,guards=len(guards),
    raw_statement_reference_instances=len(reference_map),new_program_rows=len(rows),amended_program_rows=len(shared_program_rows),new_program_links=9,owners=len(owners),
    forward_inverse_exact=True,intervals_disjoint=True,canonical_mutations=0,
    all_original_displays_and_steps_preserved=True,D19_equation_references_unchanged=True,
    D10_current_enum_formats_unchanged=True,new_independent_check_credit=0))
print(json.dumps(dict(source_sha256=source_sha,guard_count=len(guards),reference_instances=len(reference_map),preservation=preservation),indent=2))
