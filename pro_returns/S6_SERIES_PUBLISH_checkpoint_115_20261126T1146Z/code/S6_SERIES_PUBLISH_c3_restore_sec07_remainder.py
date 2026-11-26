"""Restore the omitted original unit identity; bounded consumer reads did not exhaust its tail."""
from S6_SERIES_PUBLISH_c3_edit import *

fields, rows = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
assert not any(r['paper'] == 'II' and r['unit_id'] == 'sec:II:07' for r in rows)
detail = ('Restored after the 804-page contents/source review exposed an omitted original remainder. '
          'The current subsec:II:reduced-horizontal-boundaries contains complete IRR.1, RAT.1-5/7-9, '
          'D4.1-3, UN7/12, INT.1-3 and MH4 owners. Foundations confirmed that its earlier packages '
          'fully compared preceding subsections and only bounded premise/consumer passages here; '
          'no complete old/current/receiving comparison covered this tail. The stable original '
          'sec07 identity remains open on this exact unread remainder. D10 and D16 stay done. '
          'No movement credit arises from restoration or later subdivision. Provenance is assigned '
          'the complete tail after its bounded first-part package.')
for kind in [f'D{i:02d}' for i in range(1,26)] + ['structure']:
    rows.append(dict(zip(fields, ['II', 'sec:II:07',
        'Original sec07 remainder: reduced horizontal and rational boundary covers',
        'structure' if kind == 'structure' else 'defect', '' if kind == 'structure' else kind,
        'done' if kind in {'D10', 'D16'} else 'open', now(),
        'CHECK_EVENTS.tsv: II-C3-SEC07-REMAINDER-RESTORED', detail])))
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, rows)
add_event('sec:II:07;subsec:II:reduced-horizontal-boundaries',
          'II-C3-SEC07-REMAINDER-RESTORED', 'used and rechecked in this run',
          detail + ' This is a scope reconciliation, not a full proof reading or a defect closure.',
          '804-page working contents, current source tail and foundations owner-scope confirmation', source=__file__)
print('Original sec07 remainder restored: 24 open rows, inherited D10/D16 done.')
