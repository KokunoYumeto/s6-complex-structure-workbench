from pathlib import Path
import csv, datetime, hashlib, json
from S6_SERIES_PUBLISH_editing import Editor, block

r = Path(__file__).resolve().parents[1]
ed = Editor('I')
subjects = ['fam:src:C.1.1', 'push:src:E.3.1', 'I:rem:coefficient-sources', 'night:P5.7']
before = {lab: block(ed.text, lab) for lab in subjects}
guards = [
    ('The actual cohomology jump loci are locally discrete in this\nPicard line, and the generic tuple', 'The cohomology jump loci are locally discrete in this\nPicard line, and the generic tuple', 'D08', 'series:I:E'),
    ('\\item For completeness the cusp value follows directly from the normally\nconvergent Fourier expansion, rather than from a quoted Eichler--Zagier\nconstant:',
     '\\item The cusp value follows from the normally convergent Fourier\nexpansion:', 'D02', 'fam:src:C.1.1'),
    ('One can see the branch without a numerical convention: on the rectangular',
     'On the rectangular', 'D02', 'fam:src:C.1.1'),
    ('Inserting the actual transformed arguments gives', 'Inserting the transformed arguments gives', 'D08', 'fam:src:C.1.1'),
    ('isomorphism, including its product rather than just its dimensions.',
     'isomorphism.', 'D02', 'push:src:E.3.1'),
    ('The atlas map is etale.', "The atlas map is \\'etale.", 'D23', 'push:src:E.3.1'),
    ('$\\Omega_a=\\Pi_c$, with the ordered lattice, vectors and fan retained.',
     '$\\Omega_a=\\Pi_c$, using the same ordered lattice, vectors and fan.', 'D08', 'I:rem:coefficient-sources'),
    ('the actual locally miniversal parameter family.', 'the locally miniversal parameter family.', 'D08', 'night:P5.7'),
]
for old, new, kind, lab in guards:
    ed.replace(old, new, kind,
               'Read the complete current result and proof; remove a process modifier or redundant contrast while retaining every hypothesis, formula and exact comparison map.', lab)
ed.save()
after = {lab: block(ed.text, lab) for lab in subjects}
receipt = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_sha256': hashlib.sha256(ed.text.encode()).hexdigest(),
    'scope': 'Complete exposed readings of the four listed current blocks and comparison with their replacements. The original attached C1.1 was also read in full. No derivation-before-exposure or computation credit is claimed. The first-part E deletion is a statement epithet only. Methodology refutation wording, the corrected projected divisor class and permanent identifiers were retained as mathematical/provenance uses.',
    'subjects': {lab: {'before_sha256': hashlib.sha256(before[lab].encode()).hexdigest(),
                       'after_sha256': hashlib.sha256(after[lab].encode()).hexdigest(),
                       'before': before[lab], 'after': after[lab]} for lab in subjects},
}
rp = r / 'records/S6_SERIES_PUBLISH_I_root_residual_comparison.json'
rp.write_text(json.dumps(receipt, indent=2) + '\n')
rows = []
for i, lab in enumerate(subjects, 1):
    rows.append({'statement_id': lab, 'date': '2026-11-21',
                 'who': 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH root',
                 'type': 'used and rechecked in this run',
                 'outcome': 'Complete current block and replacement read. All formulas, hypotheses and exact coordinate/cup-product/source maps are identical; only process wording, a redundant contrast or an accent changes. Exposed comparison with no independent derivation or computation credit.',
                 'event_id': f'ce:publish-I-root-residual-{i}-20261121',
                 'phase': 'publication residual source comparison',
                 'source_file': str(rp.relative_to(r)), 'source_row': lab,
                 'source_event_type': 'used and rechecked in this run',
                 'evidence_group': 'eg:publish-I-root-residual-20261121'})
with (r / 'records/S6_SERIES_PUBLISH_I_root_residual_CHECK_EVENTS.tsv').open('w') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'exposed_rows': len(rows), 'evidence_groups': 1, 'independent_checks': 0}))
