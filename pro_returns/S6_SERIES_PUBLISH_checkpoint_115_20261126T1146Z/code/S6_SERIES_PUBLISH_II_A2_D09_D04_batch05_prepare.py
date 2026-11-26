"""Prepare six owner-local program transfers and seven Programs edits."""
from pathlib import Path
import collections,csv,datetime,difflib,hashlib,json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_D09_D04_batch05_working'
P='S6_SERIES_PUBLISH_II_A2_D09_D04_batch05'
s=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
owners={'02YF':'night:P4R.3','02YC':'night:P4R.19','02YE':'night:P4R.20',
        '02WI':'night:P4.11','01BF':'cdp:st:A.5.5','01B8':'cdp:st:A.5.18'}
blocks={t:(OUT/f'S6_SERIES_PUBLISH_II_A2_{t}_before.tex').read_text() for t in owners}
following={t:(OUT/f'S6_SERIES_PUBLISH_II_A2_{t}_following_before.tex').read_text() for t in owners}
guards=[]
def add(old,new,owner,tag,classes,reason,instances=None):
    assert old!=new and s.count(old)==1,(tag,old[:80],s.count(old))
    a=s.index(old);b=a+len(old)
    g=dict(id=f'A2-ED05-{len(guards)+1:03d}',owner=owner,tag=tag,
           old=old,new=new,old_sha256=sha(old),new_sha256=sha(new),expected_count=1,
           defect_ids=classes,reason=reason,instances=instances or [],
           source_snapshot_sha256=sha(s),source_character_span=[a,b],
           source_byte_span=[len(s[:a].encode()),len(s[:b].encode())],
           source_line_span=[s.count('\n',0,a)+1,s.count('\n',0,b)+1])
    guards.append(g)

program_descriptions={}
moved={}
tail='\n\\end{enumerate}\n\\end{proof}'
for tag,body in blocks.items():
    f=following[tag]
    assert s.count(body)==1 and s.count(body+f)==1,tag
    assert body.endswith(tail),tag
    if tag=='01BF':
        start=f.index('The pole allowance')
        split=f.index(' The equalities are checked exactly in')
        example=f[start:split]
        old='Thus the corrected jet comparison applies even in this local\nmodel where holomorphic extension of the uncorrected cubic\nwould fail.'
        new='Thus the conductor-cleared jet comparison applies to\nthis local model with its meromorphic radical cubic.'
        assert old in example
        example=example.replace(old,new)
        rest=f[f.index('The local calculation below'):]
        nf='\n\n'+rest
        program_descriptions[tag]=f[split:f.index('The local calculation below')]
        moved[tag]=example
        nb=body[:-len(tail)]+'\n\n'+example+'\n'+tail
        classes=['D09','D13','D01','D08']
        reason='Move the complete three-display local conductor-clearing example into its owning proof, preserving every formula and exact map. Remove only the historical correction wording and program sentence. The separate Reid credit paragraph remains unchanged for its own owner audit.'
    elif tag=='01B8':
        start=f.index('\\paragraph{Connected double covers')
        code_at=f.index('The integer branch budgets')
        topo_at=f.index('The topological')
        example=f[start:code_at].rstrip()
        topology=f[topo_at:].strip()
        moved[tag]=example+'\n\n'+topology
        program_descriptions[tag]=f[code_at:topo_at]
        nf='\n\n'
        nb=body[:-len(tail)]+'\n\n'+moved[tag]+'\n'+tail
        classes=['D09','D13']
        reason='Move the full connected-rational-double-cover argument and the exact singular-curve quotient comparison into the owning proof. The program paragraph moves to Programs; its two equation references are preserved in the branch-budget Programs row.'
    elif tag=='02YC':
        start=f.index('\\par\\medskip\\noindent\\textbf{The two-direction exception is retained.}')
        code_at=f.index('The exact weighted gaps')
        example=f[start:code_at].rstrip().replace(
            r'\textbf{The two-direction exception is retained.}',
            r'\textbf{Two colliding spectral directions.}')
        moved[tag]=example
        program_descriptions[tag]=f[code_at:f.index('\\subsection')]
        nf='\n\n'+f[f.index('\\subsection'):]
        nb=body[:-len(tail)]+'\n\n'+example+'\n'+tail
        classes=['D09','D13','D08']
        reason='Move the complete two-direction example, both displays, inverse maps and zero-intersection arguments into its owning proof. Replace only the workflow heading and remove program/output narration.'
    else:
        at=f.index('\\subsection')
        nf='\n\n'+f[at:]
        nb=body
        program_descriptions[tag]=f[:at]
        classes=['D09','D13','D08']
        reason='Move the exact program/output paragraph to Programs and records; the complete mathematical proof and subsection heading remain unchanged.'
        instances=None
        if tag=='02YF':
            classes=['D09','D13','D01','D08','D04']
            reason='Remove the historical status paragraph. Its first mathematical assertion is the unchanged YF conclusion; its classification summary is the unchanged P4.58 statement/proof at that theorem\'s exact global hypotheses. The full support comparison is recorded, with no new forward dependency in YF.'
    instances=[]
    if tag=='02YF':
        for m in re.finditer(r'P4R?\.\d+',program_descriptions[tag]):
            target='night:'+m.group(0)
            assert '\\label{'+target+'}' in s
            instances.append(dict(old=m.group(0),new='Existing numbered owner '+target+'; redundant historical status narration removed.',target=target))
    add(tail+f,nb[len(body)-len(tail):]+nf,owners[tag],tag,classes,reason,instances)
    (OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').write_text(nb)
    (OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').write_text(nf)
    (OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_exact.diff').write_text(''.join(difflib.unified_diff(
        (body+f).splitlines(True),(nb+nf).splitlines(True),fromfile=tag+'_before',tofile=tag+'_after')))

prefix=r'https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/'
cdp='pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/'
blind='pro_returns/S6_06_BLIND_checkpoint_15_20261117T1457Z/S6_06_BLIND/code/part4/'
opened={}
for name in ['S6_SERIES_PUBLISH_II_A2_batch05_program_retrieval.json','S6_SERIES_PUBLISH_II_A2_batch05_program_retrieval_extension.json']:
    for row in json.loads((OUT/name).read_text())['files']:
        if row.get('http_status')==200:opened[row['name']]=row
table=s[s.index('\\section*{Programs}'):]
final_rows=[]
def existing_row(filename):
    lines=[line for line in table.splitlines(True) if '\\nolinkurl{'+filename+'}' in line]
    assert len(lines)==1,(filename,lines)
    return lines[0]
def link(name,directory):
    row=opened[name]
    assert row['url'].endswith(directory+name)
    assert '\\nolinkurl{'+name+'}' not in table
    return '\\href{'+prefix+directory+name+'}{\\nolinkurl{'+name+'}}'
def append_link(existing,historic,directory,description=None):
    old=existing_row(existing)
    assert old.endswith(' \\\\[3pt]\n')
    new=old[:-len(' \\\\[3pt]\n')]+'; '+link(historic,directory)+' \\\\[3pt]\n'
    if description:
        new=description+' & '+new.split(' & ',1)[1]
    add(old,new,'Programs','',['D09'],'Cite the opened historical source once in the existing row for the matching computation; preserve the existing verifier link and bind its exact mathematical receiving scope.')
    final_rows.append(new)

append_link('S6_SERIES_PUBLISH_II_BF_prereading_invariant_certificate.py','E_singular_curve.py',cdp,
    r'Conductor-cleared jets, binary-cubic discriminants and derivation-graph quotients (\cref{cdp:st:A.5.5,cdp:st:A.5.7})')
append_link('S6_SERIES_PUBLISH_II_B2_B8_prereading_certificate.py','E_tacnode_bounds.py',cdp,
    r'Symbolic squares, tacnode invariants and branch budgets (\cref{cdp:st:A.5.18}; \eqref{cdp:eq:A.T.10}--\eqref{cdp:eq:A.T.12})')
append_link('S6_SERIES_PUBLISH_II_B2_B8_comparison_certificate.py','E_low_delta_tacnode.py',cdp)
append_link('S6_SERIES_PUBLISH_II_A2_YC_weighted_cubic.py','d4_spectral_triple.py',blind,
    r'Normal-cubic weights, finite maps and two-direction inverses (\cref{night:P4R.19})')
append_link('S6_SERIES_PUBLISH_II_A2_YE_original_conductor.py','degree_two_triple_point.py',blind)
old=existing_row('e_push_two_parameter.py')
new=(r'Integral monodromies, centralizers, fixed and norm lattices, root and nodal defects, and period covariance (\cref{push:src:E.5.2,def:II:two-parameter-period-data,push:src:E.5.3})'
     +' & '+old.split(' & ',1)[1])
add(old,new,'Programs','',['D09'],'Extend the existing single historical source citation to the complete opened computational scope now printed in admitted P208 and E.5.3. Their admitted mathematical blocks are unchanged.')
final_rows.append(new)
new_row=(r'Weierstrass resolution charts, Euler number $24$ and product cell ranks (\cref{night:P4.10,night:P4.11})'
         +' & '+link('necessity_examples.py',blind)+' \\\\[3pt]\n')
anchor='\\end{longtable}}\n\n\\begin{thebibliography}{99}'
add(anchor,new_row+anchor,'Programs','',['D09'],'Cite the exact opened program at its actual two supporting examples. The Euler value is retained; the preceding projective example and Hopf example were both read fully.')
final_rows.append(new_row)
(OUT/(P+'_Programs_rows_after.tex')).write_text(''.join(final_rows))

ordered=sorted(guards,key=lambda r:r['source_character_span'][0])
for a,b in zip(ordered,ordered[1:]):assert a['source_character_span'][1]<=b['source_character_span'][0]
candidate=s
for g in guards:
    assert candidate.count(g['old'])==1,g['id']
    candidate=candidate.replace(g['old'],g['new'])
inverse=[]
for g in reversed(guards):
    assert candidate.count(g['new'])==1,(g['id'],candidate.count(g['new']))
    inverse.append(dict(id=g['id']+'-inverse',old=g['new'],new=g['old'],expected_count=1))
    candidate=candidate.replace(g['new'],g['old'])
assert candidate==s

math=lambda x:re.findall(r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?!\$).*?(?<!\\)\$|\\begin\{(?:align\*?|equation\*?|gather\*?)\}.*?\\end\{(?:align\*?|equation\*?|gather\*?)\}',x,re.S)
anchors=lambda x:re.findall(r'\\(?:label|hypertarget|tag)\{[^}]*\}',x)
eqrefs=lambda x:re.findall(r'\\eqref\{[^}]*\}',x)
enums=lambda x:re.findall(r'\\begin\{enumerate\}(?:\[[^\n]*\])?',x)
preservation=[]
for tag,old in blocks.items():
    new=(OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_after.tex').read_text()
    it=iter(math(new));assert all(any(z==x for z in it) for x in math(old)),tag
    assert anchors(old)==anchors(new) and enums(old)==enums(new),tag
    assert old.count('\\item')==new.count('\\item'),tag
    old_follow=following[tag];new_follow=(OUT/f'S6_SERIES_PUBLISH_II_A2_{tag}_following_after.tex').read_text()
    # Every equation reference is retained. The program paragraph's two
    # B8 references move to its Programs row, not to a different target.
    refs_before=collections.Counter(eqrefs(old+old_follow))
    refs_after=collections.Counter(eqrefs(new+new_follow))
    if tag=='01B8':
        refs_after.update(eqrefs(final_rows[1]))
    assert refs_before==refs_after,(tag,refs_before,refs_after)
    if tag in moved:
        assert all(x in new for x in math(moved[tag])),tag
    preservation.append(dict(owner=owners[tag],tag=tag,before_sha256=sha(old),after_sha256=sha(new),
        before_bytes=len(old.encode()),after_bytes=len(new.encode()),
        original_item_tokens=old.count('\\item'),original_bracket_displays=len(re.findall(r'\\\[.*?\\\]',old,re.S)),
        additional_bracket_displays=len(re.findall(r'\\\[.*?\\\]',new,re.S))-len(re.findall(r'\\\[.*?\\\]',old,re.S)),
        original_math_regions=len(math(old)),all_original_math_regions_retained=True,
        all_equation_references_retained=True,equation_references_moved_to_Programs=2 if tag=='01B8' else 0,
        all_labels_tags_and_current_enum_formats_retained=True,
        mathematical_following_material_moved_into_proof=tag in moved))

def dump(suffix,data):(OUT/(P+'_'+suffix+'.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
dump('guards',guards);dump('inverse_guards',inverse);dump('preservation',preservation)
dump('removed_program_descriptions',program_descriptions)
with (OUT/(P+'_defects.tsv')).open('w',newline='') as f:
    columns=['id','type','owner','tag','guard_id','old_text','new_text','source_line','status']
    writer=csv.DictWriter(f,fieldnames=columns,delimiter='\t');writer.writeheader()
    for g in guards:
        for cls in g['defect_ids']:
            entries=g['instances'] if cls=='D04' else [dict(old=g['old'],new=g['new'])]
            for n,e in enumerate(entries,1):writer.writerow(dict(id=g['id']+'-'+cls+'-'+str(n),type=cls,owner=g['owner'],tag=g['tag'],guard_id=g['id'],old_text=e['old'],new_text=e['new'],source_line=g['source_line_span'][0],status='proposed; no canonical write'))
summary=dict(created_utc=now,source_snapshot_sha256=sha(s),owners=preservation,
             exact_guards=len(guards),exact_inverse_guards=len(inverse),new_program_rows=1,amended_program_rows=6,
             new_historical_program_links=6,existing_historical_scope_expansions=1,
             forward_inverse_exact=True,all_intervals_disjoint=True,canonical_mutations=0,
             new_independent_check_credit=0,required_row_movement=0)
dump('verification',summary)
print(json.dumps(summary,indent=2))
