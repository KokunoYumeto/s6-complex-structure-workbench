#!/usr/bin/env python3
"""Prepare local LG proposals with an exact inverse; never edit canonical files."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation8_iii_lg_receiving'
SID = 'maps:src:D.2.4'
NOW = datetime.now(timezone.utc).isoformat()
OLDHASH = '78bde0a45b4dd7f15b7d36ce092787c1c7144e231290f8018a0d5bd11e3dbbc0'
NEWHASH = 'dcc39d05247e5a9e290c6ed46562393d87948cf42204d4b40f23c80b8e5ed69f'
canonical_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
canonical_bytes = canonical_path.read_bytes()
canonical = canonical_bytes.decode()
old = (OUT / 'S6_SERIES_PUBLISH_III_02LG_released_original.tex').read_text()
new = (OUT / 'S6_SERIES_PUBLISH_III_02LG_receiving.tex').read_text()
assert sha256(old.encode()).hexdigest() == OLDHASH
assert sha256(new.encode()).hexdigest() == NEWHASH
assert len(old.splitlines()) == 85 and len(new.splitlines()) == 109
assert '\r' not in old + new
assert canonical.count(old) == 1
start = canonical.index(old)
first_line = canonical[:start].count('\n') + 1
transformed = canonical.replace(old, new, 1)
assert transformed.count(new) == 1
assert transformed.replace(new, old, 1) == canonical
assert transformed.replace(new, old, 1).encode() == canonical_bytes
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}']:
    assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, new))
assert new.count(r'\begin{problem}') == new.count(r'\end{problem}') == 1
assert r'\begin{proof}' not in new and r'\StatementRecord' not in new
assert r'\textnormal{\scriptsize(tag 02LG)}\par' in new
known_labels = set(re.findall(r'\\label\{([^}]+)\}', canonical))
references = re.findall(r'\\(?:eq)?ref\{([^}]+)\}', new)
assert set(references) <= known_labels, set(references) - known_labels


def write(name, fields, rows):
    path = OUT / name
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    assert b'\r' not in path.read_bytes()


def excerpt(text, first, after):
    start_at = text.index(first)
    return text[start_at:text.index(after, start_at)]


write('S6_SERIES_PUBLISH_III_02LG_replacements.tsv',
      ['statement_id', 'old_text', 'new_text', 'reason'],
      [dict(statement_id=SID, old_text=old, new_text=new,
            reason='One open Problem with its original identity and visible tag; preserve all proved reductions, correct the twelve residual D27 assignments, specify the D26 cap marking scope, and cite the single admitted supporting proofs. Exact full-block guard and reverse replacement preserve canonical bytes in memory.')])

defects = []


def defect(key, kind, before, after, reason):
    assert before in old, (key, 'old excerpt')
    assert not after or after in new, (key, 'new excerpt')
    line = 30577 + old[:old.index(before)].count('\n')
    defects.append(dict(
        change_id='c8-III-02LG-' + key, type=kind, statement_id=SID,
        old_location='Released canonical S6_SERIES_PUBLISH_III.tex line ' + str(line),
        old_page='pending final page concordance',
        new_location='Problem maps:src:D.2.4, sole receiving statement',
        new_page='pending final build', old_text=before, new_text=after,
        reason=reason,
        review_status='local whole-original comparison complete; root admission, canonical application and final publication-unit reading pending'))


defect('header', 'D10', re.search(r'\\StatementRecord.*', old).group(0),
       r'\textnormal{\scriptsize(tag 02LG)}\par',
       'Remove the machine status/dependency header, retain the original label and hypertarget, and print the small visible tag.')
defect('title', 'D16', 'Open: the full filling and smooth classification',
       'Remaining filling and smooth classification',
       'Use a short mathematical title; the Problem environment and explicit open request preserve open status.')
defect('open-first', 'D14',
       excerpt(old, 'The full D.2 request remains open', '\n\nThe specified weighted'),
       excerpt(new, 'Determine the marked integral cap maps', '\n\nThe natural catalogue'),
       'Place the precise open families first. All four remaining sectors are preserved, with their supporting scope references.')
defect('prompt-marker', 'D05', 'The full D.2 request remains open',
       'Determine the marked integral cap maps and oriented smooth types in',
       'Replace the request marker by the mathematical task.')
defect('count-reason', 'D22',
       excerpt(old, r'\ref{maps:src:D.2.29}--', r' \ref{maps:src:D.2.37}'),
       excerpt(new, 'The original and logarithmic additive choices', ' The natural sphere sector'),
       'The count 495 is correct in L4--L9. Explain the permitted III*/IV* finite choices and give the exact 459 original-star subset with its LI reference. The row/choice bijection and inclusion/retraction are proved in the historical comparison; no count D26 or count refutation is recorded.')
defect('positive-iterates-scope', 'D22',
       excerpt(old, r'\ref{maps:src:D.2.37},', 'The entire specified'),
       excerpt(new, 'For the original-star sector,', 'The minimal simply connected sector'),
       'State the original-star algorithm scope and the fibrewise at-least-one-narrow section condition explicitly. The admitted period/line maps and their inverses supply the equivalence; all positive iterates, weights, cusp data and the Klein-four subgroup are retained.')
defect('residual-models', 'D27',
       excerpt(old, 'Residual orders $4,8,20$', 'The actual relative spin calculation'),
       excerpt(new, 'In the $18$ patterns of residual orders', 'The relative spin calculation'),
       'The exact zero-position table changes twelve of eighteen assignments, four at each order. Every cyclic isomorphism is multiplication by a unit with inverse; it preserves zero and element order. At c=4, zero versus 2; at c=8, four versus 0; and at c=20, four of order 5 versus 14 of order 10 obstruct the claimed models. The CRT20 map 5x+4y and inverse (z mod 4,4z mod 5) give the corrected models and full invariants. Complete mu=0 and count 18 stand.')
defect('finite-core-wording', 'D02',
       excerpt(old, 'The actual relative spin calculation', '\n\n\\ref{maps:src:D.2.48}'),
       excerpt(new, 'The relative spin calculation', '\n\nThe simply connected weighted Engel family'),
       'State the primitive finite-II core and relative linking computation directly, with the admitted LM proof; remove the defensive ordinary-torus and unproved-formula discussion.')
defect('new-fillings-word', 'D08', 'constructs sixteen\nnew simply connected fillings.',
       'constructs sixteen simply connected\nfillings from those corrections.',
       'State the sixteen fillings without a workflow novelty adjective.')
defect('additive-marked-scope', 'D26',
       excerpt(old, r'\ref{maps:src:D.2.51} computes every', r'\ref{maps:src:D.2.52} consequently'),
       excerpt(new, 'For every invariant-Chern original additive cap,', ' With these original'),
       'Resolve only the inherited scope ambiguity: full columns for nonzero multidegree with h=1, plus unchanged zero-degree caps in their extending frames. For c=0, the exact type-II O(F) meridian map sends mu to mu0+delta and its normal to primitive free -t; inverse W/u preserves that marking. No additional zero-normal assertion is attributed to LG, and no zero-column refutation is recorded.')
defect('global-algorithm-prose', 'D02',
       excerpt(old, r'\ref{maps:src:D.2.52} consequently', '\n\nThe full D.2 request'),
       excerpt(new, 'With these original', '\n\nThe weighted OS45/default member'),
       'Give LU at its stated corrected filling choices and established cap markings; remove the defensive rational/saturated substitution sentence.')
defect('weighted-values-reason', 'D22',
       excerpt(old, 'The actual diagonal source-line graph', 'The unresolved original-cap torsion'),
       excerpt(new, 'The source-line circle bundle', '\n\\end{problem}'),
       'Use the two values required by the admitted relative formula, reference parity 1 and complete critical link -1. The support review proves the old odd global-to-reference degree through the exact Bott/Lie/Borel maps; dropping that redundant true route is no framing refutation.')
defect('open-repeat', 'D14',
       excerpt(old, 'The unresolved original-cap torsion', ' Earlier failed'), '',
       'The precise open list already appears first, so remove the duplicate final open-scope sentence.')
defect('shortcut-history', 'D01',
       excerpt(old, 'Earlier failed half-weight,', '\n\n\n\\end{problem}'), '',
       'Remove the historical shortcut narrative from publication prose; its existing dated records remain and receive no new independent refutation credit.')
defect('now-scalar', 'D01', 'now removes the scalar-iterate restriction:',
       'gives the integral algorithm',
       'State the arbitrary positive pair algorithm directly, without its drafting chronology.')
defect('now-classified', 'D01',
       'The entire specified minimal simply connected smooth sector is now\nclassified:',
       'The minimal simply connected sector with primitive Mumford',
       'State the classification scope directly and retain every finite parameter and simply connected ordinary clutch.')

write('S6_SERIES_PUBLISH_III_02LG_defects.tsv',
      ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
       'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status'], defects)

events = []


def event(key, kind, outcome, stamp=NOW):
    events.append(dict(
        statement_id=SID, date='2026-11-25',
        who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; attributed continuation-seven support and bounded count reviewer /root/lg_fresh/lg_history_counts',
        type=kind, outcome=outcome, event_id='publish:c8:III:02LG:' + key,
        phase='continuation8-lg-receiving', source_file='S6_SERIES_PUBLISH_III.tex',
        source_row='30577', source_event_type=kind,
        evidence_group='publish:c7-c8:III:02LG',
        publish_input_file='agents/continuation8_iii_lg_receiving/S6_SERIES_PUBLISH_III_02LG_CHECK_EVENTS.tsv',
        publish_input_row=str(len(events) + 2), date_utc=stamp,
        where='agents/continuation8_iii_lg_receiving/S6_SERIES_PUBLISH_III_02LG_comparison.md'))


event('pre-exposure-synthesis', 'targeted proof check',
      'Completed the 784-line fresh synthesis before original/history release: frozen 2026-11-25T16:06:08+00:00, hash 2ec88ef8479dc870b20515290225c1e45eb26ac31ddecb7eda6aa68cb7912059, wholly root-read before the 16:07:41.482938 release. The derivation gives integral row/period/primitive-sign maps, full nonsaturated cusp quotient/inverse, finite coefficient/CRT maps, exact marked additive scope and the complete LV reduction with admitted supporting proofs. It preserves the four genuinely open families. The support formulas retain their admitted predecessor proof attribution; this is a completed fresh synthesis of those inputs, not a claim to independently rederive every predecessor theorem.',
      '2026-11-25T16:06:08+00:00')
event('pre-exposure-arithmetic', 'computation or formal certificate',
      'The completed fresh c7 raw-fixture catalogue has 274 wholly read source lines and 922 actual stdout lines; it gives 172 rows, 495 presentations, 459 original-star presentations, 162 minimal patterns and 59 spheres on 50 rows. The new c8 coefficient source has 105 lines and 195 stdout lines, with empty stderr, all wholly read. Exact unit/inverse and full coefficient CRT maps are proved before the arithmetic. The sign choice (u,r)->(-u,-r) is the self-inverse period map -I, with kappa sign transported and actual rank-one monodromy and fibre vector unchanged. Counts are newly evaluated; per-pattern geometric and P formulas are inherited from the admitted predecessor proofs, not derived by enumeration.',
      '2026-11-25T16:06:08+00:00')
event('post-exposure-count-and-residual', 'computation or formal certificate',
      'After release, the bounded count reviewer read six recovered historical source bodies; five saved JSON streams were fully parsed and all used enumeration fields exhaustively compared. Historical mains were not executed and geometric matrix arrays receive no new whole-reading credit. The new 179-line comparison ran once at 16:16:02 UTC; all 71 stdout lines and empty stderr were read by helper, main checker and root. Exact row/choice maps identify 495, retract to 459 with 36 in the complement and expand to 1728 individual cap choices; 164 compatible tuples minus two explicit obstructions give 162, with 59 spheres on 50 rows. The new 82-line residual comparison ran once at 16:20:30 UTC; all 25 stdout lines and empty stderr were read. It checks all 18 old/new invariant assignments, all cyclic units/inverses and both CRT20 composites, yielding 12 changes and 6 unchanged. Pinned retrieval and scope details remain in the helper note; unchanged source_cache is excluded from returned ZIPs.')
event('residual-refinement', "refuted, with the refined statement's id",
      'Refined statement id: maps:src:D.2.4. D27 only: the uniform residual models and P=2,0,14 fail in 12 of 18 assignments. Cyclic isomorphisms multiply by units with inverse and preserve element order; actual residual choices have 0 versus 2 at c=4, 4 versus 0 at c=8, and 4 of order 5 versus 14 of order 10 at c=20. The corrected zero-position tables give P=2epsilon,4epsilon,4+10epsilon and models Z_(4,epsilon), Z_(8,epsilon), Z_(4,epsilon)#Z_(5,1), with explicit CRT map/inverse and full mu=0 preserved. The catalogue 495, sphere 59/50, minimal 162 and residual 18 counts stand. D26 is only the inherited marked-additive scope ambiguity, clarified as c nonzero/h=1 plus unchanged c=0 extending frames; LG asserts no extra zero-normal conclusion to refute. The old odd global-reference framing degree is true. The unrestricted Problem remains open.')
event('whole-original-comparison', 'used and rechecked in this run',
      'Read the complete 85-line released original, with no separate proof body, the 1123-line statement/dependency packet and all six target historical events; read full LL/LM comparison notes and the 167-line bounded LV scope/framing note. The original was exposed only after the 784-line frozen fresh synthesis. Whole comparison covers every original clause, exact count scope and all 18 residual assignments. The 109-line receiver is one Problem retaining its label, hypertarget and visible 02LG tag; proved reductions cite their single admitted body proofs. All receiver text, local defects/events and full-block guard are reviewed at this scope. Root admission and canonical application remain pending; no required-row or publication-unit closure is claimed here.')

write('S6_SERIES_PUBLISH_III_02LG_CHECK_EVENTS.tsv',
      ['statement_id', 'date', 'who', 'type', 'outcome', 'event_id', 'phase',
       'source_file', 'source_row', 'source_event_type', 'evidence_group',
       'publish_input_file', 'publish_input_row', 'date_utc', 'where'], events)

assert canonical_path.read_bytes() == canonical_bytes
print('UTC', NOW)
print('SOURCE_SHA256', sha256(Path(__file__).read_bytes()).hexdigest())
print('OLD_LINES_HASH', len(old.splitlines()), OLDHASH)
print('NEW_LINES_HASH', len(new.splitlines()), NEWHASH)
print('CANONICAL_GUARD_LINES', first_line, first_line + len(old.splitlines()) - 1)
print('ONE_GUARD_EXACT_BYTE_INVERSE', True)
print('ONE_PROBLEM_NO_PROOF_VISIBLE_TAG', True)
print('LABEL_TARGET_MULTISETS_PRESERVED', True, 'REFERENCES_EXIST', len(set(references)))
print('DEFECT_ROWS', len(defects), 'EVENT_ROWS', len(events))
print('CANONICAL_UNCHANGED_SHA256', sha256(canonical_bytes).hexdigest())
for suffix in ['replacements', 'defects', 'CHECK_EVENTS']:
    p = OUT / ('S6_SERIES_PUBLISH_III_02LG_' + suffix + '.tsv')
    print('OUTPUT', p.name, 'physical_lines', len(p.read_bytes().splitlines()),
          'sha256', sha256(p.read_bytes()).hexdigest())
