from pathlib import Path
import datetime,hashlib,json,re
root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=root/'S6_SERIES_PUBLISH_I.tex';assert sha(source)=='61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc'
text=source.read_text()
old='The following complexification uses the curve and conjugation of\n\\cref{I:CM-enlargement-coordinates}. Its diagonal values,\nCM translates and normalized second derivatives are computed explicitly.'
assert text.count(old)==1
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'paper':'I','type_id':'D13','recorded_utc':now,'source_sha256':sha(source),'candidate':16,'page':307,'original_text':old,'finding':'The unnumbered subsection preface combines a roadmap and the curve/conjugation convention. Preserve that exact convention inside the following numbered proposition while deleting the roadmap. Root reviewed the actual surrounding subsection/proposition source.','linked_guard':'I16-edits-11, revised relocation pending','mathematical_events_added':0}
p=root/'records/S6_SERIES_PUBLISH_I_candidate16_D13_reopen.json';assert not p.exists();p.write_text(json.dumps(record,indent=2)+'\n')
ledger=root/'PROGRESS_LEDGER.md';s=ledger.read_text()
s,n=re.subn(r'^(\| I \| D13: .*? \|) done;.*? \|$',r'\1 open; retain the p307 convention inside its numbered proposition; records/S6_SERIES_PUBLISH_I_candidate16_D13_reopen.json |',s,flags=re.M);assert n==1
entry=f'\n## Paper I D13 reopened — {now}\n\nThe candidate16 p307 unnumbered preface is being integrated into its following numbered proposition: its exact curve/conjugation input is retained while the announcement is removed. This reopens D13 for the precise relocation associated with revised guard `I16-edits-11`. All underlying mathematical data remain unchanged. Evidence: `records/S6_SERIES_PUBLISH_I_candidate16_D13_reopen.json`.\n'
ledger.write_text(s+entry)
report=root/'S6_SERIES_PUBLISH_report.md';report.write_text(report.read_text()+entry)
print(json.dumps({'record':str(p.relative_to(root)),'sha256':sha(p),'D13':'open'}))
