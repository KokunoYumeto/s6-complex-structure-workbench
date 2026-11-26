from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_contracted_duality_'
s=SOURCE.read_text();after=s
for guard in json.loads((folder/(prefix+'guards.json')).read_text()):
    assert after.count(guard['old'])==1,guard['key']
    after=after.replace(guard['old'],guard['new'],1)
    print('Applied',guard['key'])
preserve_identifiers(s,after)
for old,new in zip(identifiers(s),identifiers(after)):
    for name,count in old.items():
        assert new[name]==count,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    print(suffix,append_rows(ROOT/target,rows,key))
add_event('lem:II:contracted-section-duality; cdp:st:C.2.CR.1; cdp:st:C.2.CR.2; cdp:st:C.2.UN.10',
    'II-C3-ROOT-CONTRACTED-DUALITY-ADMISSION','used and rechecked in this run',
    'Root read the complete receiving P293, all five full old/new guard fragments and all three consumer statements. Checked the unchanged local proper torus-family domain; formal-functions restriction onto the contracted section; coherent and constant-sheaf Leray maps; finite-duality branch embedding in the same local ring; proper-duality length equality; residue quotient; maximal-ideal-square inclusion with all vertical vanishing orders; proper conductor premise for Nakayama; genus-two ideal and unique-branch argument; and the exact delta-one ring application. All old equation labels and tags retain exact multiplicity; the residue alias is before the equation body. Foundations complete old/new consumer-proof readings are imported as exposed events. The enclosing subsection remains open. CR2 temporarily retains its stronger inherited domain pending the complete alias/consumer-domain consolidation; no unit closure, independent credit or final PDF credit is claimed.',
    'S6_SERIES_PUBLISH_II.tex: contracted ruled boundaries',source='code/S6_SERIES_PUBLISH_c3_contracted_duality_admit.py')
print('Admitted bounded duality owner; enclosing unit remains open.')
