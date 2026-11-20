"""One-time final canonical imports and actual-view receipts for checkpoint08.

This records the root's completed comparisons and actual image observations.
It does not execute the historical or current mathematical certificates.
The first run completed UN13 and P1.4, then stopped at the incorrect P1.19
owner assertion. finish_checkpoint08_imports.py completes only that tail;
the first two imports must not be rerun.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R = Path(__file__).resolve().parents[1]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p, value):
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')
utc = datetime.now(timezone.utc).isoformat()
receipt_path = R/'analysis/final_imports_checkpoint08.json'
assert not receipt_path.exists(), 'One-time import already recorded'

# These five pages were actually viewed in the preceding root calls, before
# build32. Only these five pages receive actual-view credit from that session.
render = json.loads((R/'analysis/build31_V_final_part_render.json').read_text())
qa31 = {
    'recorded_utc': utc, 'actual_view_before_utc': '2026-11-20T00:42:40.349218+00:00',
    'result': 'PASS', 'pdf_sha256': render['pdf_sha256'],
    'pages': list(range(213,218)),
    'images': [x for x in render['images'] if x['page'] in range(213,218)],
    'scope': 'Root actually viewed all five pages of the relocated P1.19 open problem: all thirteen retained local/algebraic steps, the new polyhedral calculation, and the explicit remaining integral geometric adapter. Text, matrices and equation tags are legible. Pages218–221 in the rendering receipt were not viewed and receive no actual-view credit here.'
}
write(R/'audit_root/build31_V_final_part_visual_QA.json', qa31)
pdfsha = sha(R/'S6_SERIES_GRIND_V.pdf')
assert pdfsha == '93dc731d09882725fd0642b95893882342f2bd4d975d506ce21829d520740ec0'
pages = [94,95,96,107,137,138]
qa32 = {
    'recorded_after_actual_view_utc': utc, 'result': 'PASS',
    'pdf_sha256': pdfsha, 'pages': pages,
    'images': [{'page': n, 'file': f'audit_root/QA_build32/V_{n}.png',
                'sha256': sha(R/f'audit_root/QA_build32/V_{n}.png')} for n in pages],
    'observations': {
        'night:P1.4': 'Entire statement and all three proof steps on pages94–95: root-chart table, exact orders, nodal dualizing extension and Hodge splitting all legible and correctly scoped.',
        'night:P1A.6': 'Entire statement and all three proof steps on pages137–138: Cayley map and explicit Cartan/Stein torsor argument legible. This current two-page evidence supersedes any earlier whole-row page-range shorthand.',
        'night:P1.13_diagnostic': 'Page107 now explicitly attributes actual manifold homology to P1.12 and describes P1.19 as the final-part open integral-comparison problem.',
        'page96': 'Actually viewed adjacent geometric quotient statement and opening proof only; no new mathematical completion claim for that row.'
    }
}
write(R/'audit_root/build32_V_visual_QA_08.json', qa32)

# UN13: exact guarded metadata import and whole-row acceptance.
proposal_path = R/'audit_sign/UN13_final_completion_proposal_08.json'
proposal = json.loads(proposal_path.read_text())
ip = R/'S6_SERIES_GRIND_inventory.csv'
with ip.open() as f:
    reader = csv.DictReader(f); columns = list(reader.fieldnames); inventory = list(reader)
row = [x for x in inventory if x['label'] == proposal['label']]
assert len(row) == 1
for change in proposal['guarded_source_updates']:
    field = change['field']; assert row[0].get(field,'') == change['old_value'], field
    if field not in columns: columns.append(field)
    row[0][field] = change['new_value']
ap = R/'audit_sign/row_assessments.json'; assessments = json.loads(ap.read_text())
old_un13 = assessments[proposal['label']].copy()
assert not old_un13.get('completion_state','').startswith('done')
new_un13 = proposal['assessment_proposal'].copy()
transport_path = R/'audit_sign/UN13_comb_build31_to32_layout_transport_08.json'
transport = json.loads(transport_path.read_text()); assert transport['all_pixel_identical']
assert sha(R/'S6_SERIES_GRIND_II.pdf') == transport['new_pdf_sha256']
new_un13['layout_check'] += ' Build32 current full-row transport PASS: every page581–585 is PNG-byte-identical to its actually viewed build31 page; receipt audit_sign/UN13_comb_build31_to32_layout_transport_08.json, SHA256 ' + sha(transport_path) + '.'
new_un13['remaining_risk'] = new_un13['remaining_risk'].replace('Root owns final import and subsequent build32 cross-reference transport.', 'Root accepted this exact import after successful build32 full-row pixel transport and the clean current reference audit.')
assessments[proposal['label']] = new_un13
with ip.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns); writer.writeheader(); writer.writerows(inventory)
write(ap, assessments)
write(R/'analysis/UN13_final_completion_08.json', {
    'utc': utc, 'proposal_sha256': sha(proposal_path), 'before': old_un13,
    'after': new_un13, 'source_updates': proposal['guarded_source_updates'],
    'scope': 'Root has read the complete report, certificate source, retained chronology and final proposal;321 current exact checks remain at their actual post-reading scope. Full13-step retained prereading union is unchanged.'
})

# P1.4: complete fresh derivation plus full receiving comparison and current QA.
cp = R/'audit_corrections/row_assessments.json'; corrections = json.loads(cp.read_text())
p14path = R/'audit_p14_fresh/whole_row_proposal_08.json'
p14proposal = json.loads(p14path.read_text()); old_p14 = corrections['night:P1.4'].copy()
assert not old_p14.get('completion_state','').startswith('done')
fresh = p14proposal['row'].copy()
fresh.update({
    'remaining_risk': 'No row-specific mathematical, full before-receiving derivation, exact-certificate, concrete-source, source-format or current full-row-layout gate remains at the literal-pencil and canonical relative-dualizing Hodge scope.',
    'format_check': 'PASS: full current three-step receiving proof agrees with the frozen derivation. The stated dualizing Hodge extension, root-chart scalings, deck characters, line divisors and permanent label/tag are intact; no mathematical source guard was required.',
    'layout_check': 'PASS: root actually viewed the complete statement and all three proof steps on build32 pages94–95, PDFSHA'+pdfsha+'. Exact image hashes and observations: audit_root/build32_V_visual_QA_08.json.',
    'completion_state': 'done'
})
corrections['night:P1.4'] = fresh
corrections['night:P1A.6']['layout_check'] = 'PASS: current entire statement and all three proof steps actually viewed by root on build32 pages137–138, PDFSHA'+pdfsha+'. Exact image hashes and complete scope in audit_root/build32_V_visual_QA_08.json. This current receipt supersedes earlier page-range shorthand.'
write(cp, corrections)
write(R/'analysis/P14_final_completion_08.json', {
    'utc': utc, 'proposal_sha256': sha(p14path), 'before': old_p14, 'after': fresh,
    'qa': 'audit_root/build32_V_visual_QA_08.json',
    'reading_scope': 'Root read the entire frozen derivation, entire after-reading comparison, entire40-assertion certificate program and saved output. The agent froze before release; expected target answer exposure and inherited model family are explicit. No rerun of the fresh program is claimed by this import.'
})

# P1.19 remains open; only its final-part format and visual gates change here.
rp = R/'audit_root/row_assessments.json'; root = json.loads(rp.read_text())
assert 'night:P1.19' in root
old_p119 = root['night:P1.19'].copy()
root['night:P1.19']['format_check'] = 'PASS for the open-problem disposition: P1.19 is in the final part with original permanent labels and all formula tags retained. Global geometric-complex claims are qualified; the exact integral polyhedral-to-finite-cap/based-meridian adapter is stated as the remaining gate. Inventory status is open.'
root['night:P1.19']['layout_check'] = 'PASS: root actually viewed all final-part pages213–217 in build31; audit_root/build31_V_final_part_visual_QA.json. Each page is exactly pixel-identical in current build32; audit_root/build32_V_final_part_transport.json. Build32 page107 diagnostic was separately viewed. This grants no mathematical completion.'
assert not root['night:P1.19'].get('completion_state','').startswith('done')
write(rp, root)
write(receipt_path, {'utc': utc, 'UN13': 'done', 'P1.4': 'done', 'P1.19': 'open; format/layout updated only', 'P119_before': old_p119, 'P119_after': root['night:P1.19']})
print(json.dumps({'utc': utc, 'completed': ['cdp:st:C.2.UN.13','night:P1.4'], 'open': 'night:P1.19', 'current_V_QA_pages': pages}))
