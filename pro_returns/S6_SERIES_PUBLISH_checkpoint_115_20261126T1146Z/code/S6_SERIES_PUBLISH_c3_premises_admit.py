from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations'
text=SOURCE.read_text()
original=text
for change in json.loads((folder/'S6_SERIES_PUBLISH_premise_placement_guards.json').read_text()):
    assert text.count(change['old'])==1, change['owner']
    text=text.replace(change['old'],change['new'],1)
a=text.index('\\section{Smooth fibres and Hopf bundles}')
b=text.index('\\section{Cotangent torsion and the Campana--Demailly--Peternell endpoint argument}',a)
fragment=folder/'S6_SERIES_PUBLISH_II_smooth_fibres_with_inputs.tex'
text=text[:a]+fragment.read_text()+text[b:]
preserve_identifiers(original,text)
SOURCE.write_text(text,newline='\n')
for name,target,key in [
    ('defects','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
    ('CHECK_EVENTS','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/f'S6_SERIES_PUBLISH_premises_{name}.tsv')
    print(name,append_rows(ROOT/target,rows,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields,rows=read_tsv(path)
for row in rows:
    if row['row_kind']=='defect' and row['defect_type']=='restructuring':
        row['row_kind']='structure'
        row['defect_type']=''
        row['status']='open'
        row['detail']+=' Corrected the incoming criterion name; no status closure or movement credit.'
    if row['unit_id']=='sec:II:fibre-classification':
        row['unit_title']='Compact torus and Hopf fibrations'
        row['detail']+=' Complete D.2.7 construction now precedes C.3.6 here; its all-class review is in the premises proposal.'
        row['evidence']=str(fragment.relative_to(ROOT))
        row['date_utc']=now()
new_rows=[]
for row in rows:
    if row['unit_id']=='sec:II:fibre-classification':
        copy=dict(row)
        copy.update(unit_id='sec:II:complete-fibres',unit_title='Complete classification and cohomology')
        copy['detail']='The already fully reviewed C.3.11 now has this subsection after both occurrence constructions. Unit subdivision itself gives no movement credit. '+row['detail']
        new_rows.append(copy)
rows.extend(new_rows)
write_tsv(path,fields,rows)
print('Moved D.2.7 before its final-classification consumer, retained all tags, and removed its later duplicate.')
print('C.3.10 now applies the opened Steenbrink analytic comparison directly; no forward D.2.3 dependence.')
print('The new program-table row is included in the pending consolidated 125-path provenance proposal.')
print('P213 remains in its later unit; no full-unit completion is claimed from that scoped edit.')
