"""Move the vacated subsection heading to its relocated proof owner."""
from S6_SERIES_PUBLISH_c3_edit import *

heading=r'\subsection{Effective anticanonical boundaries on Hopf surfaces}\label{subsec:II:anticanonical-hopf-boundaries}'
owner=r'\begin{lemma}[Effective anticanonical Hopf boundaries]\hypertarget{tag-P325}{}\label{lem:II:reduced-anticanonical-hopf}'
before=SOURCE.read_text()
assert before.count(heading)==before.count(owner)==1
start=before.index(heading)
end=before.index(r'\subsection',start+len(heading))
assert not before[start+len(heading):end].strip()
after=before[:start]+before[end:]
after=after.replace(owner,heading+'\n\n'+owner,1)
assert identifiers(before)==identifiers(after)
SOURCE.write_text(after,newline='\n')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[
 dict(change_id='II-C3-ANTICANONICAL-HEADING-PLACEMENT',type='D14',statement_id='subsec:II:anticanonical-hopf-boundaries',
 old_location='Empty subsection after terminal ruled contractions',old_page='working PDF',
 new_location='Immediately before P325, after the central Hopf cover and cohomology restrictions',new_page='integrated build pending',
 old_text=heading,new_text=heading,
 reason='The complete P325 proof has already moved to its first receiving Hopf-boundary construction. Move its vacated heading and permanent label to that earlier owner; its following UN38 boundary application remains in place.',
 review_status='Root read the empty interval, the exact earlier heading and proof boundaries. All statements and proofs remain byte-identical. Whole-paper structure stays open.')],'change_id')
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv'
fields,rows=read_tsv(path)
for row in rows:
 if row['paper']=='II' and row['unit_id']=='subsec:II:anticanonical-hopf-boundaries':
  row['detail']+=' The vacated heading now stands at the earlier P325 owner, with its already reviewed UN38 receiving application; no closure or movement credit is assigned to this placement.'
write_tsv(path,fields,rows)
add_event('subsec:II:anticanonical-hopf-boundaries',
 'II-C3-ANTICANONICAL-HEADING-PLACEMENT','used and rechecked in this run',
 'The interval below the vacated heading contained only whitespace. The same heading and label now precede the relocated P325 owner and its following UN38 application. All statement and proof bytes are unchanged. The unit identity persists and all statuses remain unchanged; whole-paper D14/structure stay open.',
 'Anticanonical Hopf subsection placement',source=__file__)
print('Empty subsection removed by moving its heading to the complete earlier owner; all proof bytes unchanged.')
