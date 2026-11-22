from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
DER = OUT.parent / 'clean_derivations'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bound(path):
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(path)}


all_rows = []
source_text = SOURCE.read_text()


def prepare(tag, owner, changes):
    original = OUT / f'S6_SERIES_PUBLISH_II_{tag}_current_before.tex'
    released = OUT / f'S6_SERIES_PUBLISH_II_{tag}_original.tex'
    before = original.read_text()
    assert source_text.count(before) == 1, tag
    text = before
    guards = []
    for number, (kind, old, new, reason, count) in enumerate(changes, 1):
        assert text.count(old) == count, (tag, number, text.count(old), old)
        text = text.replace(old, new)
        guards.append({
            'change_id': f'II-REC-C11-{tag}-{number:02d}',
            'defect_type': kind,
            'old': old,
            'new': new,
            'expected_occurrences_in_owning_block': count,
            'reason': reason,
        })
    proposed = OUT / f'S6_SERIES_PUBLISH_II_{tag}_proposed.tex'
    assert not proposed.exists()
    proposed.write_text(text)
    freeze_pointer = DER / f'S6_SERIES_PUBLISH_II_{tag}_freeze_pointer.json'
    release_pointer = DER / f'S6_SERIES_PUBLISH_II_{tag}_release_pointer.json'
    fp = json.loads(freeze_pointer.read_text())
    rp = json.loads(release_pointer.read_text())
    all_rows.append({
        'tag': tag,
        'statement_owner': owner,
        'checker': 'i_provenance_recovery',
        'freeze_pointer': bound(freeze_pointer),
        'freeze_receipt': bound(ROOT / fp['receipt']),
        'release_receipt': bound(ROOT / rp['receipt']),
        'release_envelope': bound(ROOT / rp['full_block']),
        'derivation': bound(DER / f'S6_SERIES_PUBLISH_II_{tag}_fresh_derivation.md'),
        'released_original_full_block': bound(released),
        'original_full_block': bound(original),
        'proposed_full_block': bound(proposed),
        'receiving_uses': bound(OUT / f'S6_SERIES_PUBLISH_II_{tag}_receiving_uses.json'),
        'guards': guards,
        'statement_domain_changed': tag in ['01FD', '01FF'],
        'conclusions_preserved': True,
        'original_full_proof_actually_read': True,
        'proposed_full_proof_reading_pending': True,
        'source_binding': 'The current complete owning block is the exact replacement target. The released original is separately retained. FF differs only by the previously applied exact E4 primary-citation transport.',
    })


enumeration = (
    'D04,D23',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
    r'\begin{enumerate}[label=\arabic*.,leftmargin=*]',
    'Use ordinary proof-step numbers in place of an iteration label.', 1,
)

prepare('01FD', 'cdp:st:C.3.7', [
    ('D08', '[Proved exclusion of bielliptic fibres]', '[Exclusion of bielliptic fibres]', 'Remove a proof-status marker from the mathematical title.', 1),
    ('D25', 'A compact complex threefold $Y$ with $b_1(Y)=b_2(Y)=0$ has no', 'A connected smooth compact complex threefold $Y$ with $b_1(Y)=b_2(Y)=0$ has no', 'State the smooth total-space domain used by both the frozen derivation and the printed modification/cohomology argument; no singular-domain verification is claimed.', 1),
    ('D18', r'\cite[Theorem~1.1]{Peters1990}', r'\cite[Theorem~11, p.~297]{Buchdahl1999}', 'Bind the compact-surface Kähler criterion to the opened primary theorem, with its exact journal page.', 2),
    enumeration,
    ('D02,D08', '\\item We use precisely the relative Albanese construction of\n\\cite[Proposition~2, pp.~605--608]{Kawai1969}, and not its subsequent\ncorollary. Applied to bielliptic fibres, which have\n$p_g=0$ and $h^0(\\Omega^1)=1$, it gives a compact complex surface', '\\item A bielliptic surface has\n$p_g=0$ and $h^0(\\Omega^1)=1$. The relative Albanese construction of\n\\cite[Proposition~2, pp.~605--608]{Kawai1969} gives a compact complex surface', 'State the precise admitted relative Albanese construction and its hypotheses positively.', 1),
    ('D08', 'To specify the comparison being imported, the\nconstruction forms', 'The\nconstruction forms', 'Remove the import announcement while retaining the period-lattice construction.', 1),
    ('D02,D08', 'In making this last\nstep equivariant, use the sum of the finite orbit of that divisor;\na selected section need not itself be invariant under the covering\ngroup.', 'The sum of the finite orbit of that divisor is invariant under\nthe covering group.', 'Retain the actual equivariant orbit-sum construction in a positive statement.', 1),
    ('D02,D08', ' These are the maps asserted by\nProposition~2, with that equivariant choice made explicit. The\nlater assertion in Kawai\'s corollary about multiple fibres is not\nused here.', '', 'The cited construction and orbit sum have already been specified; remove the recap and the unused-input disclaimer.', 1),
    ('D02,D08', ' All maps in this argument are\nthe displayed relative Albanese map and its modifications; no\ncomparison between the two elliptic fibrations of a bielliptic\nsurface is needed.', '', 'Remove the closing recap/disclaimer after the explicit contradiction; preserve every displayed map and pairing.', 1),
])

prepare('01FE', 'cdp:st:C.3.8', [
    ('D08', '[Proved exclusion of elliptic Hopf general fibres]', '[Exclusion of elliptic Hopf general fibres]', 'Remove a proof-status marker from the title.', 1),
    ('D02,D11', ' This exclusion uses no restriction-surjectivity\nassertion from CDP98 or CDP20.', '', 'The current referenced smooth-domain statement and the positive proof give the scope; remove the closing unused-input disclaimer.', 1),
    enumeration,
    ('D08', '\\item We first verify that a Hopf surface $H$ with $a(H)=1$ satisfies', '\\item A Hopf surface $H$ with $a(H)=1$ satisfies', 'State the anticanonical Iitaka-dimension calculation directly.', 1),
    ('D18', r'\cite[Proposition~3.1 and its proof]{SS2002}', r'\cite[Proposition~3.1 and its proof, pp.~6--7]{SS2002}', 'Bind the normal forms and anticanonical divisors to the exact cited arXiv v2 pages already specified by the bibliography.', 2),
    ('D08', 'These normal forms and the elliptic-fibration description are\nalso used in', 'The normal forms and elliptic-fibration description are given in', 'Give the source attribution directly.', 1),
    ('D08', '\\item Now, for each positive integer $m$, the locus', '\\item For each positive integer $m$, the locus', 'Remove a temporal proof-process transition.', 1),
])

prepare('01FF', 'cdp:st:C.3.9', [
    ('D08', '[Proved exclusion of secondary Kodaira general fibres]', '[Exclusion of secondary Kodaira general fibres]', 'Remove a proof-status marker from the title.', 1),
    ('D25', 'A compact complex threefold with $b_1(Y)=b_2(Y)=0$ and', 'A connected smooth compact complex threefold $Y$ with $b_1(Y)=b_2(Y)=0$ and', 'State the smooth total-space domain required by the manifold E4 input and both complete derivations; no singular-domain verification is claimed.', 1),
    ('D02,D11', ' Rational Betti-number vanishing suffices; no integral\ntorsion-freeness of the fibre is assumed.', '', 'The rational Betti hypotheses are stated positively and the proof kills the actual finite torsion group; remove the repeated negative scope sentence.', 1),
    enumeration,
    ('D08', '\\item We specify the primary cover and the invariant used below.\nLet', '\\item Let', 'Remove the roadmap before the complete canonical-cover construction.', 1),
    ('D08', '\\item The exact primary-surface invariant we use is', '\\item The primary-surface invariant is', 'Introduce the displayed invariant directly.', 1),
    ('D18', r'\cite[Theorem~4 and Remark~1]{Borcea1984}', r'\cite[Theorem~4 and Remark~1, pp.~377, 380]{Borcea1984}', 'Bind the moduli statement and complete period family to their exact printed journal pages.', 2),
    ('D08', 'This is also immediate in Borcea\'s complete\nperiod family.', 'Borcea\'s complete period family gives these local holomorphic\ncoordinates.', 'Retain the actual family input as a positive mathematical explanation.', 1),
    ('D08', ' This proves the claim.\nConsequently', '\nConsequently', 'Remove a closing recap after the explicit tangent-space intersection calculation.', 1),
    ('D02,D11', 'This identity is fibrewise and uses only degrees; it\ndoes not require the divisors $\\rho_c^{-1}(x)$ to\nextend across a singular fibre of $f$.', 'This identity follows by taking degrees on the Albanese elliptic\ncurve.', 'Keep the degree calculation justifying the displayed identity and remove the unused extension disclaimer; all divisor and pullback maps remain defined in the same step.', 1),
    ('D08', 'Applying it to the difference now proves the exact\nline-bundle identity', 'Applying it to the difference gives the line-bundle identity', 'State the norm-map conclusion directly, preserving the exact 12m power.', 1),
    ('D01,D02,D08', '\nThis proves the exclusion without the arbitrary-twist\ncohomological-flatness assertion used in the printed\nKodaira exclusion.', '', 'Remove the process/history closing sentence after the field-dimension contradiction.', 1),
])

binding = json.loads((OUT / 'S6_SERIES_PUBLISH_II_clean_group11_current_bindings.json').read_text())
bib_rows = []
for key in ['Kawai1969', 'Buchdahl1999']:
    old = binding['bibliography'][key]
    assert source_text.count(old) == 1
    new = old.replace('\\newblock \\emph{Verified}.', '').rstrip()
    if key == 'Kawai1969':
        new = new.replace('\\newblock URL', '\\newblock \\doi{10.2969/jmsj/02140604}.\n\n\\newblock URL')
        new = new.replace('/_pdf/-char/ja', '/_pdf/-char/en')
    else:
        new = new.replace('On compact kähler surfaces.', 'On compact {K\\"ahler} surfaces.')
    old_path = OUT / f'S6_SERIES_PUBLISH_II_{key}_original_entry.tex'
    new_path = OUT / f'S6_SERIES_PUBLISH_II_{key}_proposed_entry.tex'
    old_path.write_text(old)
    new_path.write_text(new)
    bib_rows.append({'key': key, 'change_id': f'II-REC-C11-BIB-{key}', 'defect_type': 'D08,D18', 'old': old, 'new': new, 'reason': 'Use primary publisher/archive metadata and remove the verification-status marker.', 'expected_occurrences': 1, 'original_entry': bound(old_path), 'proposed_entry': bound(new_path)})

result = {
    'schema_version': 1,
    'paper': 'II',
    'checker': 'i_provenance_recovery',
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_at_preparation': bound(SOURCE),
    'targets': all_rows,
    'bibliography_guards': bib_rows,
    'original_reading': bound(OUT / 'S6_SERIES_PUBLISH_II_clean_group11_original_reading.json'),
    'prereading_inputs': bound(OUT / 'S6_SERIES_PUBLISH_II_clean_group11_prereading_inputs.json'),
    'status': 'prepared; complete proposed-proof rereading and final comparison bindings remain pending',
    'mathematical_statement_and_values_unchanged': False,
    'scope_exceptions': ['01FD and 01FF explicitly add connected smooth total spaces; current C.3.1 already supplies this domain for 01FE.'],
    'displayed_final_conclusions_preserved': True,
    'canonical_mutations': False,
    'events_added': 0,
}
dest = OUT / 'S6_SERIES_PUBLISH_II_clean_group11_preparation.json'
assert not dest.exists()
dest.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'preparation': bound(dest), 'target_count': len(all_rows), 'owner_guard_count': sum(len(x['guards']) for x in all_rows), 'literal_owner_edits': sum(g['expected_occurrences_in_owning_block'] for x in all_rows for g in x['guards']), 'bibliography_guards': len(bib_rows)}, indent=2))
