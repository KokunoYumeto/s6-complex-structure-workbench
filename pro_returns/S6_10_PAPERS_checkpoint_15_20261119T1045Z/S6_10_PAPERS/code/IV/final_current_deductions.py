"""Integrate the reviewed companion deductions and verified legacy locators.

Called inside revise_body.py. All original reader bytes are retained in
the reconciliation receipt. No mathematical check is inferred by execution.
"""
import hashlib
import importlib.util

legacy_path = W/'code/fix_verified_legacy_locators.py'
spec = importlib.util.spec_from_file_location('verified_legacy_locators', legacy_path)
legacy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(legacy)
s, locator_changes = legacy.fix_legacy_locators(s, 'papers/IV/body.tex')
(W/'analysis/IV/root_legacy_locator_integration.json').write_text(json.dumps({
    'operation': 'verified locator substitutions after full receiving assembly; no proof credit',
    'changes': locator_changes
}, indent=2)+'\n')

def strip_record(text):
    pos=text.find(r'\StatementRecord{')
    assert pos>=0
    end=pos+len(r'\StatementRecord')
    for _ in range(4):
        while text[end].isspace():end+=1
        assert text[end]=='{'
        depth=1;end+=1
        while depth:
            if text[end]=='{' and text[end-1]!='\\':depth+=1
            elif text[end]=='}' and text[end-1]!='\\':depth-=1
            end+=1
    return text[:pos]+text[end:]

deductions=[]
fam=json.loads((W/'analysis/IV_root_retained/fam_E23_receiving_replacement.json').read_text())
label=fam['label'];loc=s.index(r'\label{'+label+'}')
a=s.rfind(r'\begin{remark}',0,loc);b=s.index(r'\end{remark}',loc)+len(r'\end{remark}')
old=s[a:b];expected=fam['exact_old_after_locator_repair']
assert strip_record(old)==strip_record(expected), 'fam:E2.3 mathematical original differs from the reviewed replacement input'
s=s[:a]+fam['exact_new']+s[b:]
deductions.append({'label':label,'old':old,'new':fam['exact_new'],
    'reason':fam['reason'],'current_check_owner':'root; records/IV_root_retained_events.tsv'})
changes.append({'label':label,'reason':fam['reason']})

k75=json.loads((W/'analysis/IV_K75_receiving/receiving_replacement.json').read_text())
label=k75['label'];loc=s.index(r'\label{'+label+'}')
a=s.rfind(r'\begin{theorem}',0,loc);b=s.index(r'\end{proof}',loc)+len(r'\end{proof}')
old=s[a:b]
# The replacement was drafted against the prior repaired reader block.
# The current assembly has the separately reviewed CP30 registration text.
# Its exact scope and historical tail are archived here before replacement.
assert old.count(r'\label{night:P3K.75}')==1
assert r'The selected-I3 \(M_2\) return' in old
assert 'P3K.76--108 cited in the statement.' in old
assert 'Historical working record from checkpoint 19.' in old
assert r'\StatementRecord{night:P3K.75}{open}' in old
s=s[:a]+k75['exact_new']+s[b:]
deductions.append({'label':label,'old':old,'new':k75['exact_new'],
    'reason':'Integrate the complete six-step current reduction and precise remaining selected-I3 M2/site/endpoint scope; archive the earlier failed-route chronology. The status remains Open.',
    'old_cp30_receiving_sha256':hashlib.sha256(old.encode()).hexdigest(),
    'new_sha256':hashlib.sha256(k75['exact_new'].encode()).hexdigest(),
    'scope_check':'Complete new statement and all six steps read against the current target scopes by monodromy_fourfold; root owns the formal deduction event.',
    'current_check_owner':'root; separate K75 deduction event'})
changes.append({'label':label,'reason':deductions[-1]['reason']})
(W/'analysis/IV/current_deductions_integration.json').write_text(json.dumps(deductions,indent=2)+'\n')
