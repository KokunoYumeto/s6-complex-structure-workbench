"""Read-back grammar, accents and five line-end workflow qualifiers."""
import csv, difflib, hashlib
from pathlib import Path
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
p=root/'agents/continuation8_iii_integration/units/weighted/three_primary_types.tex'
old=p.read_text();text=old;edits=[]
assert hashlib.sha256(p.read_bytes()).hexdigest()=='944157471f66ed2c9763fbdad6ab2af3310bc0ef31c46ccb3b826d751566997d'
changes=[
 (r'sends $\gamma$ to itself',r'fixes $\gamma$','D23','Restore the parallel grammar fixing gamma and the additive meridian.'),
 (r'\emph{period maps',r'\emph{Period maps','D23','Capitalize the mathematical proof-stage title.'),
 ('\nsectors of its meridional disc','\nSectors of its meridional disc','D23','Capitalize the sentence after removing its workflow qualifier.'),
 ('actual\n','\n','D08','Remove the line-end workflow qualifier; every following map and construction remains unchanged.'),
 ('characters now vanish','characters vanish','D08','State the character value directly.'),
 ('injectivity of constants now give','injectivity of constants give','D08','State the mathematical implication directly.'),
 ('now applies to $X$','applies to $X$','D08','State the recognition application directly.'),
 ('The exact CRT maps now give','The exact CRT maps give','D08','State the exact arithmetic conclusion directly.'),
 ('We now transport','We transport','D08','State the next mathematical map directly.'),
 ('Bezout',r"B\'ezout",'D23','Supply the conventional accent in the integer inverse construction.')]
for before,after,kind,why in changes:
 count=text.count(before);assert count>0,before
 for _ in range(count):
  a=text.index(before);owner='LF' if a<text.index(r'\subsubsection{Orders six') else 'LJ'
  edits.append((owner,kind,text.count('\n',0,a)+1,before,after,why))
  text=text[:a]+after+text[a+len(before):]
units.check_permanent_identifiers(old,text)
table=lane/'S6_SERIES_PUBLISH_THREE_publication_defects.tsv'
with table.open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;rows=list(r)
for i,(owner,kind,line,before,after,why) in enumerate(edits,1):
 rows.append(dict(zip(fields,[f'III-C8-THREE-TEXTFINISH-{i:03d}-{kind}',kind,
 'maps:src:D.2.'+('39' if owner=='LF' else '42'),f'three_primary_types.tex final prose line{line}',
 'pending page concordance','weighted/three_primary_types.tex','pending final build',before,after,why,
 'whole source and previous prose diff read; this exact edit read at creation; global gates open'])))
with table.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
p.write_text(text,newline='\n')
print('UTC',datetime.now(timezone.utc).isoformat())
print('LINES',len(text.splitlines()),'EDITS',len(edits),'TOTAL_ROWS',len(rows),'SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
print(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True),fromfile='THREE_prose',tofile='THREE_final')),end='')
