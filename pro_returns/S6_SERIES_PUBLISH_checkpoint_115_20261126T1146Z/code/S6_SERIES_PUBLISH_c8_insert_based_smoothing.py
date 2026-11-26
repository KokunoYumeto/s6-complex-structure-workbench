"""Place the complete reviewed common proof before its actual applications."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_apply_ready_units as a
import S6_SERIES_PUBLISH_c8_root_units as r

before = u.repairs.SOURCE.read_text(encoding='utf-8')
fragment = (u.WORK / 'root/based_smoothing.tex').read_text(encoding='utf-8')
assert fragment.count('\\begin{proof}') == fragment.count('\\end{proof}') == 1
assert '\\label{mapsIII:based-regular-fibre-smoothing}' not in before
owners = a.current_owners()
pieces = u.parse_pieces(before, owners)
anchor = next(p for p in pieces if p.unit_key == 'base_map')
assert before[anchor.start:].startswith('\\subsection{The holomorphic map to the base}')
after = before[:anchor.start] + fragment + before[anchor.start:]
u.check_permanent_identifiers(before, after,
    {'mapsIII:based-regular-fibre-smoothing'}, {'tag-Q255'})
newpieces = u.parse_pieces(after, owners)
assert ''.join(after[p.start:p.end] for p in newpieces) == after
assert after.count(fragment) == 1
df, ds = r.table(r.DEFECTS)
ident = 'III-C8-PLACE-BASED-SMOOTHING'
assert not any(x['change_id'] == ident for x in ds)
ds.append(dict(change_id=ident, type='D14',
    statement_id='mapsIII:based-regular-fibre-smoothing',
    old_location='between the complete framing unit and the base-map unit',
    old_page='pending page concordance',
    new_location='Based smoothing at a regular fibre, before the base-map subsection',
    new_page='pending final PDF', old_text='', new_text=fragment,
    reason='Insert the complete128-line common based smoothing proof before every actual geometric application, including the three-family retained torus. All existing bytes and identities remain in order. Application consolidation and criterion admission are separately checked.',
    review_status='full source and all28-criterion review read; inserted; actual boundary readback and consolidated-application admission pending'))
u.repairs.SOURCE.write_text(after, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
print('UTC', datetime.now(timezone.utc).isoformat())
print('INSERTED_LINES', fragment.count('\n'), 'BEFORE_CURRENT_LINE', before.count('\n',0,anchor.start)+1)
print('ALL_OLD_IDENTITIES_AND_UNSELECTED_TEXT_PRESERVED; NO_CRITERION_CREDIT')
