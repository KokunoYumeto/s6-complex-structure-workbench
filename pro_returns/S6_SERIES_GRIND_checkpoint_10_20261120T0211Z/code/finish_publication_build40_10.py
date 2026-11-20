"""Apply the observed II display repair and current compiled cross-page maps."""
from pathlib import Path
import datetime,hashlib,json,re,shutil
R=Path(__file__).resolve().parents[1]
receipt=R/'analysis/build40_publication_repairs_10.json'
assert not receipt.exists()
sha=lambda b:hashlib.sha256(b).hexdigest()
g=json.loads((R/'audit_sign/comb_09/build40_display_guard_10.json').read_text())
original={};pending={}
for a in g['guards']:
    p=R/a['target'];s=p.read_text();assert sha(p.read_bytes())==a['input_sha256']
    assert s.count(a['old_text'])==a['expected_count']==1
    original[a['target']]=s
    pending[a['target']]=s.replace(a['old_text'],a['new_text'])
tags=json.loads((R/'analysis/label_tags.json').read_text())
current={p:json.loads((R/f'analysis/current_labels_{p}.json').read_text()) for p in ['I','II','III','IV','V']}
refs=[];used_changes=[]
for paper in current:
    name=f'S6_SERIES_GRIND_{paper}.tex';p=R/name
    s=pending.get(name,p.read_text());original.setdefault(name,p.read_text())
    used=set(re.findall(r'\\SeriesRef\{([^}]+)\}',s))
    lines=[]
    for line in s.splitlines(keepends=True):
        m=re.match(r'\\expandafter\\def\\csname SRef@([^\n]+?)\\endcsname\{',line)
        if m and m.group(1) in tags:
            lab=m.group(1);info=tags[lab];owner=info['paper']
            if owner!=paper:
                meta=current[owner].get(lab,{})
                value='\\href{S6_SERIES_GRIND_'+owner+'.pdf\\#nameddest=tag-'+info['tag']+'}{'+owner+'.'+meta.get('number','?')+' (p.~'+meta.get('page','?')+')} '
                target='\\expandafter\\def\\csname SRef@'+lab+'\\endcsname{'+value+'}\n'
                if line!=target:
                    record={'paper':paper,'label':lab,'old':line,'new':target,'used':lab in used}
                    refs.append(record)
                    if lab in used:used_changes.append(record)
                    line=target
        lines.append(line)
    pending[name]=''.join(lines)
for name,s in pending.items():(R/name).write_text(s)
src=R/g['observed_image'];dst=R/'problem_screenshots/II_build40_comb_frame_overflow.png'
assert src.exists() and not dst.exists()
shutil.copy2(src,dst)
receipt.write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'format_guard':g,'reference_changes':refs,'used_reference_changes':used_changes,'files':{n:{'before_sha256':sha(original[n].encode()),'after_sha256':sha(s.encode())} for n,s in pending.items()},'problem_image_sha256':sha(dst.read_bytes())},indent=2)+'\n')
print(json.dumps({'format_guards':len(g['guards']),'cross_definitions':len(refs),'used_cross_references':len(used_changes),'affected_papers':sorted(set(a['paper'] for a in used_changes)|{'II'})}))
