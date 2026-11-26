from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations'
guards=json.loads((folder/'S6_SERIES_PUBLISH_P244_guards.json').read_text())
text=SOURCE.read_text()
original=text
assert text.count(guards['insert_before'])==1
lemma=(ROOT/guards['lemma_file']).read_text()
assert '\\label{'+guards['label']+'}' not in text
text=text.replace(guards['insert_before'],lemma+'\n\n'+guards['insert_before'],1)
for edit in guards['edits']:
    assert text.count(edit['old'])==1,edit['key']
    text=text.replace(edit['old'],edit['new'],1)
preserve_identifiers(original,text)
SOURCE.write_text(text,newline='\n')
for name,target,key in [
    ('defects','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),
    ('CHECK_EVENTS','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/f'S6_SERIES_PUBLISH_P244_{name}.tsv')
    print(name,append_rows(ROOT/target,rows,key))
print('One earlier owner P244 now supplies the exact shared surface-classification maps to P4.15 and P4R.2.')
