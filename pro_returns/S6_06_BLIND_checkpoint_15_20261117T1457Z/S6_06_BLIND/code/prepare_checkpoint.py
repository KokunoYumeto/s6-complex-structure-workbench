"""Retain source records and merge the chronological audit before an hourly ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import re,shutil,json
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'external_source_cache'
copied=[]
for p in sorted(CACHE.rglob('*')):
    if not p.is_file():continue
    q=ROOT/'records/external_source_cache'/p.relative_to(CACHE)
    q.parent.mkdir(parents=True,exist_ok=True)
    if not q.exists() or q.stat().st_size!=p.stat().st_size:
        shutil.copy2(p,q);copied.append(str(q.relative_to(ROOT)))
log=ROOT/'S6_06_BLIND_literature_log.md'
backup=ROOT/'records/literature_log_before_checkpoint02.md'
if not backup.exists():shutil.copy2(log,backup)
rows=[]
for line in log.read_text().splitlines():
    if re.match(r'^\|\s*20\d\d-',line):
        # Regenerate merged agent rows from their authoritative originals.
        # In particular, do not retain earlier overlong header parses.
        if 'Original complete entry: records/literature_' in line:continue
        if '| See agent source log | literature_' in line:continue
        rows.append(line.strip())
for name in ('literature_checks.md','literature_fourfold.md','literature_control.md'):
    p=ROOT/'records'/name
    agent_text=p.read_text()
    for line in agent_text.splitlines():
        if re.match(r'^\|\s*20\d\d-',line):rows.append(line.strip())
        elif re.match(r'^20\d\d-',line):
            parts=line.split(' — ',1)
            if len(parts)==2:rows.append(f'| {parts[0]} | {parts[1]} | See agent source log | {name} |')
    blocks=list(re.finditer(r'^##\s+(20\d\d-\d\d-\d\d(?:T\S+|[ \t]+\d\d:\d\d:\d\d(?:[ \t]+UTC)?))\s+—\s+(.+)$',agent_text,re.M))
    for i,m in enumerate(blocks):
        body=agent_text[m.end():blocks[i+1].start() if i+1<len(blocks) else len(agent_text)]
        body=' '.join(body.split()).replace('|',r'\|')
        timestamp=m[1]
        if 'T' not in timestamp:
            timestamp=timestamp.replace(' UTC','').replace(' ','T',1)+'+00:00'
        rows.append(f'| {timestamp} | {m[2]} | {body} | Original complete entry: records/{name} |')
unique={}
for row in rows:
    key=re.sub(r'\s*\|\s*','|',row)
    unique.setdefault(key,row)
rows=sorted(unique.values(),key=lambda r:re.search(r'20\d\d-[^| ]+',r).group(0))
header='# S6_06_BLIND literature log\n\nTimes are UTC. Original per-agent logs remain under records/. Entries distinguish supplied assertions from independent derivations.\n\n| Time | Source opened | Reason | Material used |\n|---|---|---|---|\n'
log.write_text(header+'\n'.join(rows)+'\n')
# Keep the generated register's prose consistent with its updated item table.
p=ROOT/'code/update_report.py'
s=p.read_text()
s=s.replace('For the fourfold, the full Hodge table, real structures and the ends of the parameter domain remain under calculation.','The fourfold analytic invariants, real structures, global parameter minimum and both endpoint nonexistence arguments are proved; the independent cell certificate is recorded separately.')
s=s.replace('Its actual orbit/conifold comparison has been constructed; its characteristic pair has not yet been computed.','Its actual orbit/conifold comparison, page invariants, local clutch and cyclic labels have been constructed; the global corner comparison needed to assign its characteristic pair remains unproved.')
s=s.replace('For the irreducible-fibre sign assertion the remaining case is a nonnormal support whose conductor has more general planar singularities; the regular-locus Euler number has been proved nonnegative.','For the irreducible-fibre sign assertion the remaining cases have generic cuspidal, tacnodal or triple conductors, or singular normalizations. Smooth globally unibranch supports and smooth normalizations with ordinary double germs off finitely many points are now covered; the regular-locus Euler number is nonnegative in full generality.')
p.write_text(s)
record={'utc':datetime.now(timezone.utc).isoformat(),'source_records_copied':copied,'chronological_rows':len(rows)}
(ROOT/'records/checkpoint_preparation.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
