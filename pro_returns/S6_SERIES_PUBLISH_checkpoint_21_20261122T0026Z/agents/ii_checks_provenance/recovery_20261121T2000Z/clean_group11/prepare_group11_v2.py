from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def bound(path):
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


v1 = OUT / 'S6_SERIES_PUBLISH_II_clean_group11_preparation.json'
data = json.loads(v1.read_text())
normalization = r'''Since $Y$ is reduced, $f$ factors as $f=\iota\circ f_{\mathrm{red}}$
through the inclusion $\iota:C_{\mathrm{red}}\hookrightarrow C$ of the
reduced image curve. Let $\nu:C^\nu\to C_{\mathrm{red}}$ be its
normalization. The reduced closure of the regular-locus lift graph in
$Y\times_{C_{\mathrm{red}}}C^\nu$ is finite and birational over $Y$.
Since $Y$ is normal, its projection to $Y$ is an isomorphism. The other
projection gives a holomorphic map $f^\nu:Y\to C^\nu$ with
$f_{\mathrm{red}}=\nu\circ f^\nu$. This map is surjective because its
proper image contains the regular open set of $C^\nu$. For each
$c\in C_{\mathrm{red}}$, the finitely many closed sets
$(f^\nu)^{-1}(c')$, for $c'\in\nu^{-1}(c)$, partition $f^{-1}(c)$;
each is also open in that fibre. Connectedness of $f^{-1}(c)$ forces
a single nonempty piece, so $f^\nu$ has connected fibres. Over the
regular locus $\nu$ is an isomorphism, and the general bielliptic fibre
is unchanged. In the following construction the smooth base $C^\nu$
is denoted by $C$.

'''

for row in data['targets']:
    tag = row['tag']
    proposed_v1 = ROOT / row['proposed_full_block']['path']
    text = proposed_v1.read_text()
    additions = []
    if tag == '01FD':
        additions.append(('D25', '\\begin{proof}\n\n', '\\begin{proof}\n\n' + normalization,
                          'Give the exact lift through the normalization of the reduced image curve, proving preservation of connected and general fibres before the nonsingular-base primary input is applied. This is a postrelease domain clarification; it preserves the stated broad compact-curve target.'))
    elif tag == '01FE':
        additions.extend([
            ('D25', '\\item A Hopf surface $H$ with $a(H)=1$ satisfies\n$\\kappa(H,K_H^{-1})=1$. On a primary Hopf cover the contraction\nnormal forms are diagonal, or',
             '\\item A primary Hopf surface $H$ with $a(H)=1$ satisfies\n$\\kappa(H,K_H^{-1})=1$. The contraction\nnormal forms are diagonal, or',
             'Keep the constructed anticanonical divisor in its primary-surface domain before the separate finite-cover descent; preserve every formula and the final proposition.'),
            ('D25', '\\item The algebraic reduction of an elliptic Hopf surface is a',
             '\\item The algebraic reduction of this primary elliptic Hopf surface is a',
             'Carry the same primary scope through the vertical-divisor calculation; the next step proves the secondary case by its exact finite cover.'),
        ])
    if additions:
        for kind, old, new, reason in additions:
            assert text.count(old) == 1
            text = text.replace(old, new)
            row['guards'].append({'change_id': f"II-REC-C11-{tag}-{len(row['guards']) + 1:02d}", 'defect_type': kind,
                                  'old': old, 'new': new, 'expected_occurrences_in_owning_block': 1, 'reason': reason})
        new_path = OUT / f'S6_SERIES_PUBLISH_II_{tag}_proposed_v2.tex'
        assert not new_path.exists()
        new_path.write_text(text)
        row['proposed_v1_full_block'] = row['proposed_full_block']
        row['proposed_full_block'] = bound(new_path)
    original = (ROOT / row['original_full_block']['path']).read_text()
    assembled = original
    for guard in row['guards']:
        assert assembled.count(guard['old']) == guard['expected_occurrences_in_owning_block']
        assembled = assembled.replace(guard['old'], guard['new'])
    assert assembled == text
    assert (ROOT / 'S6_SERIES_PUBLISH_II.tex').read_text().count(original) == 1

data['preparation_v1'] = bound(v1)
data['updated_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
data['source_at_preparation_v2'] = bound(ROOT / 'S6_SERIES_PUBLISH_II.tex')
data['comparison'] = bound(OUT / 'S6_SERIES_PUBLISH_II_clean_group11_comparison.md')
data['v1_to_v2'] = ['FD: explicit reduced-image/normalization lift, preserving the compact-curve statement through the proved finite birational map.', 'FE: explicit primary scope in steps 1–2 before the step 3 finite-cover descent.', 'FF: proposed block unchanged from v1.']
dest = OUT / 'S6_SERIES_PUBLISH_II_clean_group11_preparation_v2.json'
assert not dest.exists()
dest.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'preparation': bound(dest), 'owner_guard_count': sum(len(x['guards']) for x in data['targets']), 'literal_owner_edits': sum(g['expected_occurrences_in_owning_block'] for x in data['targets'] for g in x['guards']), 'bibliography_guard_count': len(data['bibliography_guards'])}, indent=2))
