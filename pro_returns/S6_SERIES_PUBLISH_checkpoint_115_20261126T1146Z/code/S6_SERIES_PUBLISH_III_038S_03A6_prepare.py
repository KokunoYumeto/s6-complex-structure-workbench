#!/usr/bin/env python3
"""Prepare fully compared 038S/03A6 guards and proposed rows; no source edit."""
from collections import Counter
import csv
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
SOURCE_HASH = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == SOURCE_HASH
source = source_bytes.decode('utf-8')
now = datetime.now(timezone.utc).isoformat()

# Exact formal Laurent-polynomial comparison of the original and fresh
# frame formulas. Variables are r,k,a,b,c,d with k=1/(2pi), Y=[[a,b],[c,d]].
zero = (0,)*6


def const(c):
    return {} if not c else {zero: F(c)}


def monomial(i, exponent=1):
    e = list(zero)
    e[i] = exponent
    return {tuple(e): F(1)}


def add(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            out[e] = out.get(e, F(0))+c
    return {e: c for e, c in out.items() if c}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            ef = tuple(x+y for x, y in zip(e, f))
            out[ef] = out.get(ef, F(0))+c*d
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return mul(p, const(c))


def mm(a, b):
    return [[add(*(mul(a[i][h], b[h][j]) for h in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def det3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return add(mul(a, add(mul(e, i), scale(mul(f, h), -1))),
               scale(mul(b, add(mul(d, i), scale(mul(f, g), -1))), -1),
               mul(c, add(mul(d, h), scale(mul(e, g), -1))))


r, k, a, b, c, d = [monomial(i) for i in range(6)]
ir, ik = monomial(0, -1), monomial(1, -1)
A = [[scale(mul(y, ik), -1) for y in row] for row in [[a,b],[c,d]]]
J = [[const(F(1,2)), scale(add(A[0][0], A[1][0]), -1),
      scale(add(A[0][1], A[1][1]), -1)],
     [const(F(1,4)), A[0][0], A[0][1]],
     [const(F(1,4)), A[1][0], A[1][1]]]
Q = [[r, r, r], [{}, scale(k, -1), {}], [{}, {}, scale(k, -1)]]
Hi = [[ir, {}, {}], [{}, const(1), {}], [{}, {}, const(1)]]
fresh = [[const(1), {}, {}],
         [scale(mul(k, ir), F(-1,4)), a, b],
         [scale(mul(k, ir), F(-1,4)), c, d]]
assert mm(mm(Q, J), Hi) == fresh
delta = add(mul(a, d), scale(mul(b, c), -1))
assert det3(J) == mul(delta, monomial(1, -2))
assert det3(Q) == mul(r, monomial(1, 2))
assert det3(fresh) == delta
print('Exact Laurent-polynomial frame conversion Q J diag(1/r,I2)=fresh frame verified.')
print('det(J)=det(Y)/k^2, det(Q)=r k^2, det(fresh)=det(Y), k=1/(2pi).')
print('No numerical sampling is used.')


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


with (ROOT / 'CHECK_EVENTS.tsv').open() as stream:
    EVENT_FIELDS = next(csv.reader(stream, delimiter='\t'))

specs = [
    ('038S', 'wb:cusp-null:thm', 'theorem',
     'f766b40166c404c16972f91ab14451b459daed8454878f14a5e3b67522f6a96d',
     '4e29014da53d8f4428286a200380d5bb202b6c20639076e20242427363f2eb4d',
     '2026-11-24T12:21:26.198670+00:00'),
    ('03A6', 'wb:cusp_s12_carrier_homotopy:L567', 'corollary',
     '47acfe28373228d8ab95fd74ee819747e42c4ad90869c1adf82a2c6c59af154d',
     'e11784a40e98e85239fa8651548d3e6e188d589f1ada119910a977b5f156efa6',
     '2026-11-24T12:21:26.575563+00:00'),
]

for tag, label, environment, proof_hash, fresh_hash, release in specs:
    prefix = 'S6_SERIES_PUBLISH_III_'+tag
    fresh_path = D / (prefix+'_fresh_derivation.md')
    assert hashlib.sha256(fresh_path.read_bytes()).hexdigest() == fresh_hash
    statement = (D / (prefix+'_released_statement.tex')).read_text()
    statement = statement[statement.index('\\begin{'+environment+'}'):].strip()
    proof = (D / (prefix+'_released_proof.tex')).read_text()
    proof = proof[proof.index('\\begin{proof}'):].strip()
    assert hashlib.sha256(proof.encode()).hexdigest() == proof_hash
    begin = source.index(statement)
    pbegin = source.index(proof, begin+len(statement))
    assert not source[begin+len(statement):pbegin].strip()
    old = source[begin:pbegin+len(proof)]
    first = source.count('\n', 0, begin)+1
    last = source.count('\n', 0, pbegin+len(proof))+1
    receiver_path = D / (prefix+'_receiving.tex')
    new = receiver_path.read_text().strip()
    for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
        assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
    assert '\\StatementRecord' not in new
    assert '\\begin{enumerate}' not in new
    assert new.count('\\begin{proof}') == 1
    assert (D / (prefix+'_comparison.md')).exists()
    write(D / (prefix+'_replacements.tsv'),
          ['statement_id', 'old_text', 'new_text', 'reason'],
          [dict(statement_id=label, old_text=old, new_text=new,
                reason='Complete individually released original statement and '
                       'adjacent full proof; full original/fresh/receiving comparison '
                       'completed; preserve every permanent tag and label; canonical '
                       'source application and unit/page gates remain for root.')])

    defects = []

    def defect(suffix, kind, before, after, why):
        assert before in old, (tag, suffix, 'old fragment missing')
        assert not after or after in new, (tag, suffix, 'new fragment missing')
        defects.append(dict(
            change_id='c6-III-'+tag+'-'+suffix, type=kind, statement_id=label,
            old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}', old_page='',
            new_location=receiver_path.relative_to(ROOT).as_posix(), new_page='',
            old_text=before, new_text=after, reason=why,
            review_status='proposed; complete original/receiving comparison done; '
                          'root admission, source application and final page review pending'))

    header = statement[statement.index('\\StatementRecord'):].split('\n\n', 1)[0]
    defect('header', 'D10', header, '',
           'Remove the machine statement record and keep all permanent tags and labels.')
    enum = '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]'
    defect('enumeration', 'D10', enum, '',
           'Replace the generated item hierarchy by connected mathematical proof text.')
    defect('title', 'D16', statement.splitlines()[0], new.splitlines()[0],
           'Give the statement a concise mathematical title matching its proved content.')
    if tag == '038S':
        defect('defensive-change', 'D02',
               'not a replacement of \\(C(t)\\).', '',
               'The printed F and G are explicit inverse holomorphic maps preserving t; '
               'delete the defensive clause while keeping the full period units.')
        defect('repeated-nullity-proof', 'D12',
               '\\item \\textbf{4. The based map represented by this framed inverse image.}',
               'Composing its based null-homotopy with this suspension homeomorphism',
               'Use the admitted angle-forgetting based homotopy through the exact '
               'marked-torus and suspension isomorphisms once. The full original '
               'relative smoothing and Milnor argument has been checked in the '
               'comparison; print the additional framed-cap result here.')
        defect('chart-dependency', 'D12',
               'The original free properly\ndiscontinuous action supplies a neighborhood',
               'The cited chart lemma gives inverse coordinate maps',
               'Refer to the admitted chart proof03AE, with exact F/G and U/W_delta '
               'domains, instead of repeating a local injectivity proof. Receiving '
               'unit ordering must place that dependency before its use.')
        defect('basepoint-choice', 'D22',
               'Choose the injective chart to exclude \\(x_0\\) if its center is not',
               'For $x_0\\in U$, write $w^*=\\phi^{-1}(x_0)$.',
               'Keep the admitted fixed chart and give explicit compatible radius '
               'bounds that avoid the original arbitrary basepoint, including all '
               'central-coordinate cases.')
    else:
        defect('undefined-back-reference', 'D06',
               'The previously defined homomorphism', 'The homomorphism',
               'Define Theta_g at this statement. Root exact-name inspection found '
               'no separate preceding definition in III or the supplied earlier sources.')
        defect('undefined-marked-character', 'D06',
               'its composite with the marked peripheral character are zero.',
               'For every additive character',
               'The indicated marked character has no located definition. State and '
               'prove the consequence for every additive character to R/Z, then '
               'state its multiplicative S1 identity convention; invent no marking.')
        defect('coefficient-conversion', 'D20',
               'Thus the unique\ncoefficient of \\([g]\\) in any generator of \\(\\mathbb Z/12\\) is zero.',
               'By the definition $[E^6g]=2a\\nu_9$, where $\\nu_9$ has order $24$,',
               'Use the actual coefficient definition038Z and the injective map '
               '[a]12 to2a nu9, with inverse on its image, to connect the zero '
               'suspension to a=0. The original one-copy coefficient assertion is '
               'correct but does not itself supply this distinct conversion.')
    write(D / (prefix+'_defects.tsv'), list(defects[0]), defects)

    event_id = 'publish:c6:III:'+tag+':targeted'
    outcome = ('Complete fresh derivation saved and fully reread before root review '
               'completion2026-11-24T12:21:13+00:00 (SHA256 '+fresh_hash+'), '
               'then this original individually released '+release+'. ')
    if tag == '038S':
        outcome += ('Read the complete original statement, all320 proof lines and '
                    'the complete receiving proof. Checked exact period quotient, '
                    'inverse chart/unit maps, complete fibre and angular mapping '
                    'torus, every embedded equation, original/fresh frame conversion, '
                    'both full cap constructions with explicit diffeomorphism, '
                    'product collars, frame extension and arbitrary fixed-basepoint '
                    'avoidance. Opened and read Milnor1965 at the cited theorem, '
                    'full product construction and interpolation proof, with relative '
                    'basepoint application checked. Receiving based-nullity clause '
                    'uses admitted02Q7 via exact marking/suspension isomorphisms. ')
    else:
        outcome += ('Read the complete original statement, all10 proof lines and '
                    'the complete receiver. Checked fixed source identification, '
                    'both suspension placements and homotopy endpoints, actual '
                    'equation038Z coefficient map and its inverse on the even '
                    'subgroup, Theta_g descent and all additive/multiplicative '
                    'character conventions. Repaired the missing prior definition '
                    'and unlocated marked-character reference with explicit '
                    'character-independent statements. ')
    outcome += ('No theorem refuted; exactly one proposed targeted event for this '
                'identity. Source application, unit restructuring and page gates remain open.')
    row = dict.fromkeys(EVENT_FIELDS, '')
    evidence = [fresh_path, D / (prefix+'_comparison.md'),
                D / (prefix+'_replacements.tsv')]
    if tag == '038S':
        evidence.append(D / (prefix+'_comparison_primary_reading.md'))
    row.update(statement_id=label, date=now[:10],
               who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not '
                   'separately exposed; sixth-continuation carriers checker',
               type='targeted proof check', outcome=outcome, event_id=event_id,
               phase='fresh derivation followed by individual authorized full comparison',
               source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
               source_event_type='targeted proof check', evidence_group=event_id,
               publish_input_file=(D / (prefix+'_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
               publish_input_row='2', date_utc=now,
               where='; '.join(path.relative_to(ROOT).as_posix() for path in evidence))
    write(D / (prefix+'_CHECK_EVENTS.tsv'), EVENT_FIELDS, [row])
    print(tag, 'source lines', first, '-', last, '; original', len(old.splitlines()),
          'lines; receiver', len(new.splitlines()), 'lines; defects', len(defects))
    print('Guard SHA256 without terminal LF:', hashlib.sha256(old.encode()).hexdigest())
    print('Permanent tags preserved:', ','.join(re.findall(r'\\hypertarget\{tag-([^}]+)\}', old)))
    print('One proposed event:', event_id)
    for suffix in ['receiving.tex', 'comparison.md', 'replacements.tsv', 'defects.tsv', 'CHECK_EVENTS.tsv']:
        assert b'\r' not in (D / (prefix+'_'+suffix)).read_bytes()
    assert hashlib.sha256(fresh_path.read_bytes()).hexdigest() == fresh_hash

assert SOURCE.read_bytes() == source_bytes
print('Canonical source and both frozen fresh derivations unchanged.')
print('LF comparison packets prepared', now)
