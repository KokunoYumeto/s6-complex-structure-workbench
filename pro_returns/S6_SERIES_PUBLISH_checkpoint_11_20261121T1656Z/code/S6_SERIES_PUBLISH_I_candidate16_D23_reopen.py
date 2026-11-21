from pathlib import Path
import datetime,hashlib,json,re
root=Path(__file__).resolve().parents[1]
src=root/'S6_SERIES_PUBLISH_I.tex'; text=src.read_text()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)=='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
hits=list(re.finditer(r'(?<!\\v )\bCech\b',text))
assert len(hits)==8
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
rows=[]
for h in hits:
 a=text.rfind('\n',0,h.start())+1;b=text.find('\n',h.end())
 rows.append({'line':text.count('\n',0,h.start())+1,'context':text[a:b],'offset':h.start()})
record={'paper':'I','type_id':'D23','recorded_utc':now,'source_sha256':sha(src),'findings':rows,'status':'D23 remains open; eight newly found plain Cech spellings require the caron already used in the same paper; complete owning-context review and exact guards pending','mathematical_events_added':0}
p=root/'records/S6_SERIES_PUBLISH_I_candidate16_D23_accent_findings.json'; assert not p.exists(); p.write_text(json.dumps(record,indent=2)+'\n')
ledger=root/'PROGRESS_LEDGER.md'; s=ledger.read_text()
assert re.search(r'^\| I \| D23: .*? \| open \|$',s,re.M)
entry=f'\n## Paper I D23 accent findings — {now}\n\nA source check prompted by the complete A.3 proof found eight plain Cech spellings alongside the already established caron spelling. D23 remains open while their complete owning contexts and exact accent guards are reviewed. The previous D23 row was already open; eighteen type rows remain closed and seven remain open. No mathematical event is added. Receipt: `records/S6_SERIES_PUBLISH_I_candidate16_D23_accent_findings.json`.\n'
ledger.write_text(s+entry)
r=root/'S6_SERIES_PUBLISH_report.md';s=r.read_text();s=s.replace('Remaining D08 prose announcements and D18 preprint-version entries are being resolved','Remaining D08 prose announcements, D18 preprint-version entries and D23 accent spellings are being resolved',1);r.write_text(s+entry)
print(json.dumps({'findings':len(rows),'record':str(p.relative_to(root)),'sha256':sha(p),'closed_types':18,'open_types':7}))
