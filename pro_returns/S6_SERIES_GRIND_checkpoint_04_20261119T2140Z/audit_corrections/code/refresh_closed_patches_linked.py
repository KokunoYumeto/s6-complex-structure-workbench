from pathlib import Path
import re,json,hashlib
root=Path(__file__).resolve().parents[1]
source=root.parent/'parts/IV.body.linked.tex'
text=source.read_text()
patches=json.loads((root/'IV_closed_computation_patches.json').read_text())
prefixes={1:'The local inputs are K96 EX.1--6',4:'The companion exact calculation retains the finite-source identity',5:r'\par\medskip\noindent\textbf{Exact coefficient calculations.}\par'}
paragraphs=[m.group().strip() for m in re.finditer(r'\S[\s\S]*?(?:\n\s*\n|\Z)',text)]
for i,prefix in prefixes.items():
    hits=[p for p in paragraphs if p.startswith(prefix)]
    assert len(hits)==1,(i,len(hits))
    patches[i]['old_text_pre_root_cleanup']=patches[i]['old_text']
    patches[i]['old_text']=hits[0]
for p in patches:
    assert text.count(p['old_text'])==1,(p['label'],p['paragraph_index'],text.count(p['old_text']))
    text=text.replace(p['old_text'],p['new_text'])
(root/'IV_closed_computation_patches.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
(root/'IV_closed_computation_linked_match_QA.json').write_text(json.dumps({'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'patch_count':len(patches),'all_old_text_matches_unique':True,'updated_indices':list(prefixes)},indent=2)+'\n')
items=json.loads((root/'IV_closed_computation_followup_candidates.json').read_text())
new=[]
new.append(items[0]['old_text'].replace('The independent\ncalculation retains','The rational-function calculation retains'))
new.append('')
new.append(items[2]['old_text'].replace('Full independent root proof','Root proof'))
new.append(items[3]['old_text'].split('The executable peer')[0].strip())
new.append(items[4]['old_text'].replace('Complete independent source','Source'))
new.append('\n'.join(items[5]['old_text'].splitlines()[1:]).replace('This independent proof\nchecks the complete','The proof uses the complete'))
new.append(items[6]['old_text'].replace('Our independent calculation uses','Substitution uses'))
new.append(items[7]['old_text'].replace('Our independent execution checks both\nsource inverses, and the three chronological plus-source\ncomposites give','The three chronological plus-source composites give'))
new.append(items[8]['old_text'].replace('Complete independent comparison proof.','Comparison of the complete endpoint maps.'))
new.append(r'''Exact rational-function substitution gives the original odd-line
Miller pullbacks and inverse-source coefficients before their central
values. Integer arithmetic checks the root characters, signed norm
equation, root exponents and full cyclic scalar identity. The four
page formulas provide the characteristic inputs to exact rational
nine-variable target-prism elimination. The source, line, root,
reference and parameter maps are the constructions above; the
terminating fan construction and residue identities establish the
unbounded image.''')
new.append(items[10]['old_text'].split('This was the one source-graph')[0].strip())
new.append(items[11]['old_text'].replace('independent full target systems','full target systems'))
follow=[]
for q,replacement in zip(items,new):
    count=text.count(q['old_text'])
    assert count==1,(q['label'],q['old_text'][:60],count)
    follow.append({**q,'new_text':replacement,'operation':'replace_exact_text',
      'purpose':'Remove remaining execution-history prose while retaining every displayed mathematical equation and scope.'})
    text=text.replace(q['old_text'],replacement)
(root/'IV_closed_computation_followup_patches.json').write_text(json.dumps(follow,ensure_ascii=False,indent=2)+'\n')
(root/'IV_closed_computation_followup_receipt.json').write_text(json.dumps({'scope':'12 additional exact paragraph changes; apply after the first41','patches':follow},ensure_ascii=False,indent=2)+'\n')
print('All41 exact matches against linked body;12 followups match the proposed result.')
