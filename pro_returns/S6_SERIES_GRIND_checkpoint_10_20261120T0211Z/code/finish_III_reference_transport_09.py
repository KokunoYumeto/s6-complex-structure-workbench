"""Finish the one-time literal QED and compiled-page definition transport."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
out=R/'analysis/III_QED_and_current_reference_transport_09.json'
assert not out.exists()
old="Each program's exact JSON output is in \\path{code/outputs/}."
new=old+r'\qedhere'
canonical=(R/'parts/III.body.linked.tex').read_text()
assert canonical.count(new)==1
tags=json.loads((R/'analysis/label_tags.json').read_text())
current={p:json.loads((R/f'analysis/current_labels_{p}.json').read_text()) for p in ['I','II','III','IV','V']}
pending={};original={};refs=[]
for paper in current:
 p=R/f'S6_SERIES_GRIND_{paper}.tex';t=p.read_text();original[str(p.relative_to(R))]=t
 if paper=='III':
  assert t.count(old)==1 and new not in t
  t=t.replace(old,new)
 lines=[]
 for line in t.splitlines(keepends=True):
  m=re.match(r'\\expandafter\\def\\csname SRef@([^\n]+?)\\endcsname\{',line)
  if m and m.group(1) in tags:
   lab=m.group(1);info=tags[lab];owner=info['paper']
   if owner!=paper:
    meta=current[owner].get(lab,{})
    value='\\href{S6_SERIES_GRIND_'+owner+'.pdf\\#nameddest=tag-'+info['tag']+'}{'+owner+'.'+meta.get('number','?')+' (p.~'+meta.get('page','?')+')} '
    target='\\expandafter\\def\\csname SRef@'+lab+'\\endcsname{'+value+'}\n'
    if target!=line:refs.append(dict(paper=paper,label=lab,old=line,new=target));line=target
  lines.append(line)
 pending[str(p.relative_to(R))]=''.join(lines)
for name,t in pending.items():(R/name).write_text(t)
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
out.write_text(json.dumps({
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'format_change':{'old':old,'new':new,'canonical':'parts/III.body.linked.tex','generated':'S6_SERIES_GRIND_III.tex','reason':'Move observed orphan QED onto final text line. The canonical edit occurred before the retained failed standalone context guard; this completes the exact generated transport.'},
 'reference_changes':refs,
 'files':{n:{'before':sha(original[n]),'after':sha(v)} for n,v in pending.items()},
 'scope':'The reference formula is exactly assemble_series.py with current compiled label data. IV and V have printed targets changed by III pagination; unused macro-only changes do not affect I or II PDF content.',
 'prior_attempt':'analysis/III_QED_transport_attempt01.json'},indent=2)+'\n')
print(json.dumps({'reference_definitions':len(refs),'format_guards':2}))
