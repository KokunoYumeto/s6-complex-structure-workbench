"""Record completed, exposed III bibliography/source readings locally.

No canonical source, shared table, count, inventory or primary-source copy is
created.  Every event states its actual bounded reading and its attribution.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation8_iii_later'
SOURCE = 'agents/continuation8_iii_integration/units/root/bibliography.tex'
REVIEW = 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_bibliography_publication_review.md'
DEFECTS = LANE / 'S6_SERIES_PUBLISH_III_bibliography_publication_defects.tsv'
EVENTS = LANE / 'S6_SERIES_PUBLISH_III_bibliography_publication_CHECK_EVENTS.tsv'
EXPECTED = '20547d3717632f0c8dea540ca711543f23a7638b62a33d9b11e37199e3b5ca84'
text = (ROOT / SOURCE).read_text()
assert sha256(text.encode()).hexdigest() == EXPECTED
assert (ROOT / REVIEW).is_file()

with DEFECTS.open(newline='') as handle:
    reader = csv.DictReader(handle, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
other_fields = [{k: v for k, v in row.items() if k != 'review_status'} for row in rows]
status = ('Whole original695-line and final449-line bibliography read; every current III citation key retained, '
          'exact same-edition consolidation follows root actual body substitutions, and all source/edition scopes '
          'are in the wholly read publication review. Source-local exposed publication work completed. '
          'No independent, blind, required-check or criterion-count credit. Root owns canonical application, '
          'exact locator proposal application, final reference/PDF gates and joint totals.')
for row in rows:
    row['review_status'] = status
assert other_fields == [{k: v for k, v in row.items() if k != 'review_status'} for row in rows]
with DEFECTS.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

WHO = 'GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed'
UTC = datetime.now(timezone.utc).isoformat()
COMMON = (' Exposed use and rechecking only; no new independent/blind/required-check credit, '
          'full-paper verification, historical execution, canonical admission or final PDF credit. '
          'Exact URLs, hashes, failed endpoints and application limits are in the linked review.')
SPECS = [
 ('series:III:bibliography', 'whole-source',
  'Read the whole695-line original, whole449-line candidate, all current III citation keys, complete named staged '
  'bibliographies/source records and complete420-line local publication review. Retained surviving keys and '
  'literal anchor multiplicities; exact entry edits are in local defects. Removed only duplicate identical '
  'editions after root actual citation replacements. Retained all actual preprint/translation pagination.'),
 ('bib:manYang26', 'yang-primary',
  'Newly opened exact arXiv2609.29666v1; whole printed11,13--14,21--25,65--67 read as text; actual rendered13 '
  'and14 viewed. Prop3.1p11,Prop3.4p13,Prop3.6p14; geometric cusp/component owner Thm4.8pp22--23/Cor4.13p25. '
  'AppendixB.4 chain material kept at its actual scope. Root applied these locators and geometric owner.'),
 ('bib:manLR26', 'lr-primary',
  'Newly retrieved exact2609.33826v2 matching c5 SHA; title/version and complete printed7--8,11--14,21 read; '
  'actual p21 image viewed. Prop2.12/Def2.13pp7--8 with sigma/Psi inverses, Lem3.10pp11--12,Prop3.11p12, '
  'Props3.12--3.13pp13--14,Thm5.1p21. Direct retrieval succeeded despite disabled web-open endpoint.'),
 ('bib:DebrayGunningham2018Root', 'debray-primary',
  'Newly opened author PDF with actual v1/date on first page; whole printed6 and its real image read, '
  'including Thm3.2,Rem3.3,Thm3.6,Example3.8. Primary archive/author metadata gives Contemp.Math718(2018) '
  '49--87 and DOI10.1090/conm/718/14478. Body pages explicitly remain preprint pages.'),
 ('bib:manUU21', 'ulmer-primary',
  'Newly retrieved2002.01906v2; complete title/version and printed6--7 read for local-period table and '
  'Betti-foliation passage. Official publication metadata retained. No new visual reading or journal/preprint '
  'page equivalence claimed.'),
 ('bib:manViaclovskyTwo26', 'viac-two-primary',
  'Newly retrieved sole posted2609.33785v1; whole printed1--2,6--9,19--20 read. Exact scopes:Thm1.1p2; '
  'primitive Mumford filling/specialization Prop3.1pp6--7; Lem3.2pp7--8 and logarithmic section3.3pp8--9; '
  'Prop6.4pp19--20. Poincare hexagonal citation owner corrected in proposal to Prop3.1 while exact maps remain.'),
 ('bib:manViaclovskyLogs26', 'viac-logs-primary',
  'Newly retrieved sole posted2610.39102v1; whole printed1,4--6,9--10,14 read. Data2.11--2.12p4, '
  'Prop2.3 and inverse-translation proof5--6,Prop4.1 integral H2 cap-map cokernelp9,Cor4.6p14. Root accepted '
  'Q109 attribution wording naming second homology of the initial family, keeping its full III theorem intact.'),
 ('bib:E26', 'engel-primary',
  'Newly retrieved2609.38442v1; full printed3--9,18--19,24 read as text. Lem2.1/Cor2.2pp3--4, '
  'actual norm contraction Prop2.4p5,Props2.7--2.9pp6--7,Prop3.1/Cor3.2pp8--9,Lem7.4pp18--19 '
  '(Mumford clausep19),Rem8.5p24. Full fibrewise degree-zero line scope retained. No new visual reading claimed.'),
 ('bib:manSS10', 'schuett-shioda-primary',
  'Newly retrieved0907.0298v3 matching c5 SHA; complete printed14,23,29,39,41,51--52 read as text. '
  'Exact loci:4.5/Table1p14,Thm6.3p23,6.11/Cor6.13p29,8.4p39,8.8p41,11.8/Table4pp51--52,11.10(22)p52. '
  'These are new bounded page readings, not retroactive expansion of foundations attribution.'),
 ('bib:manBesserLivne12', 'besser-livne-primary',
  'Newly retrieved1202.2808v2 matching c5 SHA; complete printed9--10 and17 read as text. '
  'Table1p10 with explanationp9 and author-data section9p17. No source-code execution or visual reading claimed.'),
 ('bib:manFukae02', 'fukae-primary',
  'Newly retrievedmath/0205062v1 matching c5 SHA; title/version and complete printed35(PDF36) read. '
  'Actual rendered35 viewed, with Table3 rows50/56 and footer35 visible. New bounded locator reading only.'),
 ('bib:manWang26', 'wang-primary',
  'Newly retrieved2609.11541v2 matching c5 SHA; complete printed15 and AppendixB17--19 read as text '
  'for exact Thm7.1 orientation/type statement and its cited appendix. The actual cited printed pages '
  'are now established; no new independent classification proof is claimed.'),
 ('bib:Pontryagin1955Root', 'pontryagin-translation',
  'Actual English scan images first spread,108--113 and translator/end114 viewed; entire Thm24/proof109--112 '
  'read. MathNet original and AMS Translations11 publication records opened. Corrected bibliography retains '
  'Russian1955pp3--139 and identifies Hilton English1959pp1--114 with English body pagination.'),
 ('bib:Pontryagin1950Root', 'pontryagin-original',
  'Actual original Russian Doklady70(1950) printed957--959 visually read from two source images. '
  'Retained title/publication/language and removed third-party link. Appended review supplies no primary proof credit.'),
 ('bib:BHS19', 'bhs-publication',
  'Opened actual publisher journal PDF title metadata:Acta231(2)(2023)205--344,DOI10.4310/ACTA.2023.v231.n2.a1. '
  'Retained actually used arXiv1910.14116v3(10May2022) body pagination. Prior front-matter v3 reading remains '
  'at its exact pp7--8 scope; no full journal proof reading claimed.'),
 ('series:III:bibliography:metadata', 'publisher-metadata',
  'Bounded metadata openings:APSII Cambridge issue/DOI;Miranda Springer DOI;Milne author version1.31/22Mar2017; '
  'Teschl author preliminary-version notice;Redden primary archive publication/DOI;Schuett--Shioda chapter DOI '
  'publisher identity plus opened AMS research bibliography. Thomas1959 automated Paul author field rejected '
  'against actual article Emery identity; no guessed DOI added. These are metadata readings only.'),
 ('series:III:bibliography:predecessors', 'predecessor-records',
  'Read complete named c7 staged bibliographies; complete LL,LF,LP,LN,LU,c8LV source-check records; '
  'whole c4J7 Johnson reading record; whole root base-map/quotient-map reviews for Hatcher. '
  'JohnsonThm3Ap371,Hatcher4.24pp360--361/4.25p361,Kaplan239--240/243--246,Zhubr English796/806--810 '
  'retain predecessor opening attribution. No new Johnson/Hatcher/Kaplan/Zhubr primary opening is claimed.'),
 ('series:III:bibliography:programs', 'actual-helper-streams',
  'Read complete70-line current source retrieval helper, complete565-line bibliography editor and actual '
  'source/editions/locators/remaining stdout plus empty outer stderr, and the editor actual six-line stdout/empty '
  'stderr. Extraction font warnings remain in JSON fields and all actual extraction statuses are zero. '
  'External source bytes stay under tmp and are not returned artifacts.'),
 ('series:III:bibliography:locators', 'locator-proposal',
  'Read complete211-line guarded locator proposal and all72 initial actual inspect stdout lines/empty stderr; '
  'subsequent two exact supplying-result changes read in full. Inspection made no source mutation. '
  'The initial log is retained at its true earlier scope; root owns final --apply, actual successor reading '
  'and exact shared D06/event rows. Source passages supplying both semantic changes were fully read.'),
]
event_fields = ['statement_id','date','who','type','outcome','event_id','phase','source_file',
                'source_row','source_event_type','evidence_group','publish_input_file',
                'publish_input_row','date_utc','where']
event_rows = []
for index, (statement, name, outcome) in enumerate(SPECS, 2):
    key = statement[4:] if statement.startswith('bib:') else None
    source_row = ''
    if key:
        marker = ']{'+key+'}'
        if marker in text:
            source_row = str(text.count('\n', 0, text.index(marker))+1)
    event_rows.append(dict(statement_id=statement, date=UTC[:10], who=WHO,
        type='used and rechecked in this run', outcome=outcome+COMMON,
        event_id='publish:c8:III:bibliography:'+name,
        phase='continuation8-bibliography-publication', source_file=SOURCE,
        source_row=source_row, source_event_type='used and rechecked in this run',
        evidence_group='publish:c8:III:bibliography-publication',
        publish_input_file=str(EVENTS.relative_to(ROOT)), publish_input_row=str(index),
        date_utc=UTC, where=REVIEW))
with EVENTS.open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(event_rows)
assert b'\r' not in DEFECTS.read_bytes() and b'\r' not in EVENTS.read_bytes()
print('UTC', UTC)
print('completed bibliography source-local review recorded; exact old/new defect fields unchanged')
print('bounded actual source readings and predecessor attribution written to local CHECK_EVENTS with LF')
print('no canonical source, shared table, primary-source copy or derived file written')
