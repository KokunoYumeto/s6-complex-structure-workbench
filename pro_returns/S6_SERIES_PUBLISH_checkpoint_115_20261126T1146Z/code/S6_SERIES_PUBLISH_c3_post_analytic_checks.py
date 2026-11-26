from S6_SERIES_PUBLISH_c3_edit import *

add_event('paper:II','II-C3-BUILD-ANALYTIC-RANKTWO-CLEAR','working standalone build',
 'After the cusp, class-VII, weighted-sphere, analytic/LR and rank-two admissions, three standalone pdfLaTeX passes exited zero. The resulting PDF has787 pages and5179147 bytes. There are two overfull boxes, neither exceeding2pt, and zero undefined references/citations, missing fonts/glyphs, multiply defined labels, duplicate destinations or rerun requests. This is a working build; final rendered-page reading credit is zero. The subsequent bibliography metadata edit is outside this build.',
 'build/II_c3_working/S6_SERIES_PUBLISH_II.pdf; code/S6_SERIES_PUBLISH_c3_build_latest.out',source='code/S6_SERIES_PUBLISH_c3_build.py')

folder=ROOT/'agents/continuation3_conductor'
_,rows=read_tsv(folder/'S6_SERIES_PUBLISH_c3_conductor_bib153_edits.tsv')
assert len(rows)==1
r=rows[0];s=SOURCE.read_text();assert s.count(r['old_text'])==1
SOURCE.write_text(s.replace(r['old_text'],r['new_text'],1),newline='\n')
print('Bibliography rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
_,events=read_tsv(folder/'S6_SERIES_PUBLISH_c3_conductor_bib153_CHECK_EVENTS.tsv')
print('Exposed metadata events',append_rows(ROOT/'CHECK_EVENTS.tsv',events,'event_id'))
_,sources=read_tsv(folder/'S6_SERIES_PUBLISH_c3_conductor_bib153_sources.tsv')
mapped=[]
for row in sources:
    mapped.append(dict(source=row['source_id'],url=row['url'],version=row['version'],locus=row['exact_locus'],
      date_utc=row['date_utc'],sha256=row['sha256'],own_word_summary=row['own_paraphrase'],
      use='Yoshihara bibliography metadata only; '+row['reader']))
print('Primary metadata records',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',mapped,'source'))
add_event('bib:Yoshihara1995','II-C3-ROOT-YOSHIHARA-METADATA-ADMISSION','used and rechecked in this run',
 'Root read the exact old/new bibliography entry and the complete two-source metadata report. The full primary title page and EMS record, read by the conductor agent, confirm that the existing journal and1995 year were correct despite the suggestive J-STAGE path. They remain unchanged; the verified DOI and unambiguous publisher URL are added. No new mathematical proof reading or independent credit is claimed.',
 'S6_SERIES_PUBLISH_II.tex bibliography; II-C3-PROV-153',source='agents/continuation3_conductor/S6_SERIES_PUBLISH_c3_conductor_bib153_sources.tsv')
print('Working build recorded and exact metadata correction admitted.')
