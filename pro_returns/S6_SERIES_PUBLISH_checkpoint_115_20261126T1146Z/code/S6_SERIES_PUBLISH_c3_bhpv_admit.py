"""Admit the exact minimal-model classification locator and application."""
from S6_SERIES_PUBLISH_c3_edit import *
folder=ROOT/'agents/continuation3_provenance/final_sources'
_,guards=read_tsv(folder/'S6_SERIES_PUBLISH_bhpv_guard.tsv')
assert len(guards)==1
r=guards[0]
apply_edit(r['old_text'],r['new_text'],r['change_id'],r['type'].split(';'),
    r['statement_id'],r['new_location'],r['reason'],r['review_status']+
    ' Root previously read the complete current P410 and now read the complete receiving classification paragraph and exact source record.')
_,events=read_tsv(folder/'S6_SERIES_PUBLISH_bhpv_CHECK_EVENTS.tsv')
for e in events:
    if 'effort' not in e['who']:e['who']+='; effort setting not separately exposed'
append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id')
_,sources=read_tsv(folder/'S6_SERIES_PUBLISH_bhpv_sources.tsv')
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[dict(
    source=r['source_key']+' (third-continuation rational Weierstrass application)',
    url=r['url'],version=r['version'],locus=r['locus_read']+'; '+r['read_extent'],
    date_utc=r['date_utc'],sha256=r['sha256'],
    own_word_summary=r['own_paraphrase'],use=r['exact_application']) for r in sources],'source')
set_unit_status('night:P4.10','D18','done',
    'The exact remaining BHPV locator is verified on the complete official theorem/table preview, pp243–244, with its precise projective Hodge and minimal-model application. Previously checked local citations and the full P410/P411 example comparisons remain.',
    'CHECK_EVENTS.tsv: publish:c3:provenance:BHPV-P410')
add_event('night:P4.10','II-C3-ROOT-BHPV-APPLICATION','used and rechecked in this run',
    'The complete current P410 was read before this bounded edit; root now read its full receiving classification paragraph and the exact source record. The same projective S has b1=2h1(O)=0, its minimal-model contraction preserves b1 and plurigenera, and the opened BHPV VI1.1/Table10 rational row applies. No construction, other example, statement scope or final-page credit changes.',
    'P410 classification paragraph',source=__file__)
print('Exact BHPV pp243–244 application admitted.')
