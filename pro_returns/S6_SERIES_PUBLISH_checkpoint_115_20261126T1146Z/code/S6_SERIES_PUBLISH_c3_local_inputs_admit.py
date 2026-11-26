from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
fragment=folder/'S6_SERIES_PUBLISH_II_sec07_local_inputs.tex'
guards=json.loads((folder/'S6_SERIES_PUBLISH_sec07_local_guards.json').read_text())
before=SOURCE.read_text()
after=before
for guard in guards:
    assert after.count(guard['old'])==1,guard['key']
    after=after.replace(guard['old'],guard['new'],1)
    print('Applied',guard['key'])
assert fragment.read_text().strip() in after
assert 'Choose a nonzero class $\\gamma_S\\in H^1(S,\\mathbb Z)$' in after
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    for name,count in old.items():assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
                          ('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,incoming=read_tsv(folder/('S6_SERIES_PUBLISH_sec07_local_'+suffix))
    print(suffix,append_rows(ROOT/target,incoming,key))

path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields,rows=read_tsv(path)
selected=[r for r in rows if r['paper']=='II' and r['unit_id']=='subsec:II:local-numerical-conductor-inputs']
assert len(selected)==26
for row in selected:
    row.update(unit_id='subsec:II:contracted-ruled-boundaries',unit_title='Contracted ruled boundaries',
               detail=row['detail']+' Remainder boundary migrated after the fully compared local-input extraction; no closure credit for this migration.')
_,incoming=read_tsv(folder/'S6_SERIES_PUBLISH_sec07_local_unit_progress.tsv')
for item in incoming:
    criterion=item['row']
    if criterion=='restructuring':criterion='structure'
    status=item['status'];detail=item['basis']
    if criterion in ['D14','structure']:
        status='open';detail+=' Final whole-paper placement remains open.'
    rows.append(dict(zip(fields,['II',item['unit'],'Local numerical and conductor criteria',
        'structure' if criterion=='structure' else 'defect','' if criterion=='structure' else criterion,
        status,now(),item['fragment'],detail])))
write_tsv(path,fields,rows)
add_event('lem:II:torus-tube-numerical; lem:II:plane-branch-conductor; lem:II:torus-tube-character; cdp:st:C.2.MH.1; cdp:st:C.2.MH.2',
          'II-C3-ROOT-LOCAL-INPUTS-ADMISSION','used and rechecked in this run',
          'Root read every line of the complete receiving local-input subsection and the revised P289 statement with its nonzero integral class explicitly chosen. The foundations agent full original/receiving comparison of MH.1/MH.2 and all five affected consumer proofs is imported as exposed reading. Eleven exact guards matched once; every existing label and target retains its multiplicity. P281 retains the broader local tube scope, P282 moves the exact intrinsic-plus-intersection conductor formula before IRR.1, and P289 retains the class premise. The remaining contracted-boundary unit stays open; final placement and final rendered pages are uncredited.',
          'S6_SERIES_PUBLISH_II.tex',source='code/S6_SERIES_PUBLISH_c3_local_inputs_admit.py')
print('Local-input subsection admitted with explicit class scope and preserved consumer maps.')
