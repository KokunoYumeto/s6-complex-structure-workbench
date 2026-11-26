"""Make the cited projective source's exact assumptions explicit."""
from S6_SERIES_PUBLISH_c4_edit import *
import json
prefix = ROOT / 'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_furushima_scope'
guard, = json.loads(Path(str(prefix) + '_guards.json').read_text())
apply_edit(guard['old'], guard['new'], 'II-C4-FURUSHIMA-SCOPE', ['D18'],
           'cdp:st:A.5.3', 'Source attribution following the exceptional coefficient calculation',
           'The opened Lemma 1.1 and Corollary 1.4 have the distinct explicitly stated source domains; the latter additionally assumes trivial dualizing sheaf, vanishing h1(O) and a very ample polarization. The receiving analytic theorem and its finite-duality and intersection-matrix proof are unchanged.',
           review='Root read the complete exact old/new attribution and the source-reader comparison; the preceding fresh visual primary reading is recorded in the bounded event. No full-proof or independent credit.')
_, events = read_tsv(str(prefix) + '_CHECK_EVENTS.tsv')
for row in events:
    row['evidence_group'] = row['event_id']
    row['source_event_type'] = row['type']
    row['source_file'] = 'agents/continuation4_reductions/S6_SERIES_PUBLISH_c4_citations_comparison.md'
print('Bounded attribution events:', append_rows(ROOT / 'CHECK_EVENTS.tsv', events, 'event_id'))
print('No mathematical statement or unit status changed.')
