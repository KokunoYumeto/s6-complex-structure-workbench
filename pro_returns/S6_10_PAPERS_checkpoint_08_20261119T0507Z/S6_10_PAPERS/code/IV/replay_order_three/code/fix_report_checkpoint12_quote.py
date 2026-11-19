"""Preserve and repair the failed source-text insertion in the report generator."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py'
s=p.read_text()
bad="K35's shortest scalar return"
assert s.count(bad)==2
attempt=root/'records/attempts/update_report_checkpoint12_unescaped_apostrophe.py.txt'
attempt.parent.mkdir(parents=True,exist_ok=True)
attempt.write_text(s)
p.write_text(s.replace(bad,'the shortest scalar return of K35'))
print('Preserved the failed insertion and repaired both source string literals.')
