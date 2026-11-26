from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json

R = Path(__file__).resolve().parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def bind(p):
    b = (R/p).read_bytes()
    return dict(path=p, sha256=sha(b), bytes=len(b))
bp = R/'S6_SERIES_PUBLISH_references.bib'
old = bp.read_bytes()
assert sha(old) == '066e8fd88d902c1284972761a6c7d42d96e17655b8a629d32abbebe546128622'
assert b'{KerrLazaSaito2022,' not in old
entry = r'''
@article{KerrLazaSaito2022,
  author = {Kerr, Matt and Laza, Radu and Saito, Morihiko},
  title = {Deformation of rational singularities and {Hodge} structure},
  journal = {Algebraic Geometry},
  volume = {9},
  number = {4},
  pages = {476--501},
  year = {2022},
  doi = {10.14231/AG-2022-014},
  url = {https://content.algebraicgeometry.nl/2022-4/2022-4-014.pdf},
  verification = {verified at listed primary-source scope},
  source_note = {Original journal PDF, SHA256 b0898c9eeee06c4613b63bb9cfe4cc0da9ba3190c378b951586b5f5ef9a66bde, 484121 bytes. Root acquired the PDF in memory on 22 November 2026 and read the complete text of printed pages480--481 (PDF pages5--6), including section1.1 equations(1.1.1)--(1.1.3) and the complex-analytic continuation. Exact extracted text SHA256 9ac1ea79ca3b9e02d3d393e3b63200506e9a5ec6cb10978903461a759c12783d. Scope: the rational-singularity structure-sheaf criterion and its equivalent Cohen--Macaulay canonical-trace statement, used for the normal analytic conductor calculation in night:P4R.18. No whole-article or visual-page reading is claimed. Acquisition is recorded in records/S6_SERIES_PUBLISH_II_YB_root_primary_01.json and the subsequent completed reading in records/S6_SERIES_PUBLISH_II_root_continuation2_batch75_review.json.}
}
'''
new = old + entry.encode()
dp = R/'S6_SERIES_PUBLISH_defects_II.tsv'
db = dp.read_bytes()
reader = csv.DictReader(io.StringIO(db.decode()), delimiter='\t')
rows = list(reader); fields = reader.fieldnames
row = dict(change_id='II-C2-YB-MASTER-BIB-001', type='D18', statement_id='Bibliography:KerrLazaSaito2022',
    old_location='master bibliography', old_page='', new_location='master bibliography', new_page='',
    old_text='', new_text=entry,
    reason='Synchronize the master bibliography with the exact primary entry added to Paper II by admission75. Scope verification records the original journal article and the complete analytic canonical-trace locus actually read.',
    review_status='Root read printed480-481 in full; scoped primary verification recorded; no extra check event')
assert row['change_id'] not in {r['change_id'] for r in rows}
s = io.StringIO(newline=''); w = csv.DictWriter(s, fieldnames=fields, delimiter='\t', lineterminator='\n')
w.writeheader(); w.writerow(row)
tail = s.getvalue().split('\n',1)[1].encode()
assert db.endswith(b'\n')
rd = R/'records/S6_SERIES_PUBLISH_II_YB_master_reference_01'
assert not rd.exists(); rd.mkdir()
(rd/'bibliography.diff').write_text(''.join(difflib.unified_diff(old.decode().splitlines(True), new.decode().splitlines(True), fromfile='references.before', tofile='references.after')))
(rd/'defect_row.tsv').write_text(s.getvalue())
now = dt.datetime.now(dt.timezone.utc).isoformat()
manifest = dict(created_utc=now, bibliography_before_sha256=sha(old), bibliography_after_sha256=sha(new),
    defects_before_sha256=sha(db), defects_after_sha256=sha(db+tail), appended_defect_rows=1,
    source=bind('S6_SERIES_PUBLISH_II.tex'), source_changes=0, check_events_added=0,
    primary_acquisition=bind('records/S6_SERIES_PUBLISH_II_YB_root_primary_01.json'),
    completed_root_reading=bind('records/S6_SERIES_PUBLISH_II_root_continuation2_batch75_review.json'),
    admission=bind('records/S6_SERIES_PUBLISH_II_clean_checks_75/manifest.json'),
    global_defect_rows_closed=0, final_page_reading_credit=0)
(rd/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
bp.write_bytes(new)
with dp.open('ab') as f: f.write(tail)
assert bp.read_bytes() == new and dp.read_bytes() == db+tail
text = f'''\n\n## Paper II canonical-trace primary reference — {now}\n\nAdmission75's Kerr--Laza--Saito2022 citation is now also present in the master bibliography, with its exact DOI, original-journal PDF hash and bounded reading of printed480--481. The initial acquisition receipt remains historically unchanged; the completed reading is recorded in the batch75 root review. One D18 defect row and an exact bibliography diff are saved in records/S6_SERIES_PUBLISH_II_YB_master_reference_01. No source, theorem, check-event count or global completion row changes in this bibliography synchronization.\n'''
for name in ('PROGRESS_LEDGER.md', 'S6_SERIES_PUBLISH_report.md'):
    with (R/name).open('a') as f: f.write(text)
print(json.dumps(manifest, indent=2))
