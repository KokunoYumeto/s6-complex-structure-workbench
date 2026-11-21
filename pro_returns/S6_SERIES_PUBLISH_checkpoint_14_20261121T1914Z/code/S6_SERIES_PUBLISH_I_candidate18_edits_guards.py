#!/usr/bin/env python3
"""Prepare the four context-read candidate18 prose guards; no canonical writes."""
from pathlib import Path
import collections
import datetime
import difflib
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_candidate17_combined import block, math, displays, refs, write_stable
from S6_SERIES_PUBLISH_synctex_batch import Scanner

R = Path(__file__).resolve().parents[1]
O = R / 'agents/i_cont_edits'
SOURCE = '3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
PDF = '702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e'
READING = '55a02a28222b270d0b06d2ebf377adb4ab10e22cf697b0053411aa3d483244e3'
sha = lambda b: hashlib.sha256(b).hexdigest()
commands = lambda s: re.findall(r'\\[A-Za-z@]+\*?|\\.', s)

PROPOSALS = [
    (214, (213, 215), 'D02',
     'In particular, no choice of multiplicities or infinitely near\ncentres changes the obstruction: only their nonempty finite\nsupport on $E$ is needed.\n', '', ['$E$'],
     'Delete the redundant nonrequirement sentence after the finite-orbit contradiction. The statement already allows infinitely near centres and requires a nonempty exceptional image on E. The proof retains the finite exceptional image S, equivariance of both maps, preservation of S, the nonempty finite S intersect E, the torsion equation, finite-collection version, normal-line comparison and cusp-period calculation. Exactly one repeated inline mention of E is removed with the sentence; its definition and operative occurrences remain.',
     [
       'Suppose $p:Y\\to H$ is a finite composition of point blow-ups,\nallowing infinitely near centres, and at least one point of $E$\nis an image of its exceptional locus.',
       'The automorphism $h$ preserves $E$, where it is translation by\n$[b]$. Consequently the nonempty finite set $S\\cap E$ would be\ninvariant under that translation.',
       '[b^k v]=[v],\\qquad\\text{equivalently } b^k\\in a^\\Z.'
     ]),
    (221, (220, 221), 'D02',
     'stratum; an\nordinary constant sheaf there would be incorrect if\nbranches permute.', 'stratum.', [],
     'Keep the positive orientation-local-system formulation and delete its negative imagined-alternative tail. The ordered finite branch spaces, alternating summand, exact direct-summand operation over C, augmented branch resolution, spectral-sequence injection and integral incidence calculation remain. No mathematical segment, coefficient convention, hypothesis or reference is removed.',
     [
       'Use the ordered finite\nbranch spaces $D^{[p]}$ and take the alternating\nsummand for the branch-permutation action. Over $\\C$\nthis is an exact direct-summand operation.',
       'Resolve the\nconstant sheaf by this augmented alternating branch\ncomplex. At a point its row is the augmented simplex\ncomplex, so it is exact, including for self-crossings.'
     ]),
    (238, (236, 238), 'D02',
     'on exponentiation, and must not be included in $Y$.', 'on exponentiation.', ['$Y$'],
     'Retain the positive fact that the Z w and Z delta terms disappear on exponentiation; delete the repeated negative inclusion instruction. The period lattice Y=Z u plus Z gamma is defined at the start, the complete character pairing and quotient exact sequence remain, and the u/gamma valuation map and connecting-class obstruction are unchanged. Exactly one repeated inline mention of Y is removed with the clause; every operative lattice, map and formula remains.',
     [
       '$X=\\Z e_1\\oplus\\Z e_2$ and period lattice\n$Y=\\Z u\\oplus\\Z\\gamma$.',
       '$\\gamma$. The terms in $\\Z w+\\Z\\delta$ disappear',
       'u\\longmapsto(12,0),\\quad\n \\gamma\\longmapsto(0,12)'
     ]),
    (239, (239, 240), 'D08',
     ' The computation uses \nthe displayed bivector automorphy.', '', [],
     'Delete the method recap after the anticanonical section computation. The proof already specifies the lifted bivector, its deck-equivariance equation, the Taylor coefficient condition, the two section dimensions and the representing monomials. The full resonance, coherent-direct-image, resolution and finite-base-change argument remains. No mathematical segment or reference is removed.',
     [
       'A section of $K_{H_q}^{-1}$ lifts to\n$f(z,w)\\,\\partial_z\\wedge\\partial_w$ on\n$\\C^2\\setminus\\{0\\}$.',
       'f(\\alpha z,\\beta w)=\\alpha\\beta f(z,w).',
       'The sections in the first case are represented by\n$zw$ and $w^{N+1}$.'
     ]),
]


def main():
    sp = R / 'S6_SERIES_PUBLISH_I.tex'
    pp = R / 'build/I_candidate18/S6_SERIES_PUBLISH_I.pdf'
    rp = O / 'S6_SERIES_PUBLISH_I_final_candidate18_reading_edits.json'
    protected = {p: p.read_bytes() for p in [sp, R/'S6_SERIES_PUBLISH_defects_I.tsv', R/'CHECK_EVENTS.tsv', rp]}
    for pattern in ['S6_SERIES_PUBLISH_I_final_candidate*_reading_edits.json', 'S6_SERIES_PUBLISH_I_candidate*_type_closure_preparation.json']:
        for p in O.glob(pattern): protected[p] = p.read_bytes()
    source = protected[sp].decode()
    assert sha(protected[sp]) == SOURCE and sha(pp.read_bytes()) == PDF
    assert sha(protected[rp]) == READING
    reading = json.loads(protected[rp])
    assert [r['page'] for r in reading['pages']] == list(range(213, 246))
    guards, archives, maps = [], [], []
    proposed = source
    with Scanner(pp) as scanner:
        for i, (page, page_bounds, typ, old, new, removed, reason, witnesses) in enumerate(PROPOSALS, 1):
            gid = f'I18-edits-{i:02d}'
            assert source.count(old) == 1
            pos = source.index(old)
            label, a, b, kind = block(source, pos)
            original = source[a:b]
            replacement = original.replace(old, new, 1)
            assert collections.Counter(math(old)) - collections.Counter(math(new)) == collections.Counter(removed)
            assert not (collections.Counter(math(new)) - collections.Counter(math(old)))
            assert displays(old) == displays(new) and displays(original) == displays(replacement)
            assert commands(original) == commands(replacement)
            assert refs(original) == refs(replacement)
            relative = pos-a
            expected_inline = math(original[:relative]) + math(new) + math(original[relative+len(old):])
            assert math(replacement) == expected_inline
            assert collections.Counter(math(original))-collections.Counter(math(replacement)) == collections.Counter(removed)
            assert re.findall(r'\\(?:label|hypertarget)\{[^}]+\}', original) == re.findall(r'\\(?:label|hypertarget)\{[^}]+\}', replacement)
            statement_end = original.index(r'\end{proposition}') + len(r'\end{proposition}')
            assert replacement.startswith(original[:statement_end])
            ws = []
            for w in witnesses:
                assert original.count(w) == replacement.count(w) == 1, (gid, w)
                ws.append({'exact_text': w, 'sha256': sha(w.encode()), 'source_line': source[:a+original.index(w)].count('\n')+1, 'preserved_byte_identically': True})
            line = source[:pos].count('\n')+1
            pages = sorted({p for ln in range(line, line+old.count('\n')+1) for p in scanner.pages(sp, ln)})
            assert page in pages, (gid, page, pages)
            stem = O/f'S6_SERIES_PUBLISH_I_candidate18_edits_block_{i:02d}'
            pa, pb, pd = [Path(str(stem)+suffix) for suffix in ['_original.tex', '_proposed.tex', '.diff']]
            write_stable(pa, original); write_stable(pb, replacement)
            write_stable(pd, ''.join(difflib.unified_diff(original.splitlines(True), replacement.splitlines(True), fromfile=label+'/candidate18', tofile=label+'/proposed')))
            archive = {'statement_id': label, 'original': str(pa.relative_to(R)), 'original_sha256': sha(pa.read_bytes()), 'proposed': str(pb.relative_to(R)), 'proposed_sha256': sha(pb.read_bytes()), 'diff': str(pd.relative_to(R)), 'diff_sha256': sha(pd.read_bytes()), 'source_line_start': source[:a].count('\n')+1, 'source_line_end': source[:b].count('\n')+1, 'printed_page_start': page_bounds[0], 'printed_page_end': page_bounds[1], 'kind': kind, 'guards': [gid], 'complete_original_statement_and_proof_read': True, 'full_statement_byte_identical': True, 'all_display_mathematical_segments_identical': True, 'all_inline_mathematical_segments_identical': not bool(removed), 'removed_repeated_inline_mentions': removed, 'all_remaining_inline_math_in_identical_order': True, 'all_command_reference_label_target_sequences_identical': True, 'all_content_outside_exact_guard_byte_identical': True}
            archives.append(archive)
            g = {'id': gid, 'page': page, 'type': typ, 'statement_id': label, 'source_line': line, 'before': old, 'after': new, 'reason': reason, 'source_sha256': SOURCE, 'pdf_sha256': PDF, 'candidate18_synctex_pages': pages, 'full_block_archive': archive, 'retained_witnesses': ws, 'inline_math_mentions_removed': removed, 'inline_math_mentions_added': [], 'all_mathematical_segments_identical': not bool(removed), 'all_display_mathematical_segments_identical': True, 'all_remaining_inline_math_in_identical_order': True, 'tex_command_sequence_identical': True, 'citation_reference_sequence_identical': True, 'all_labels_targets_preserved': True, 'status': 'proposed for root exact review; not applied', 'mathematical_events_added': 0}
            guards.append(g)
            q = proposed.index(old)
            maps.append({'guard_id': gid, 'position': q, 'before': old, 'after': new})
            proposed = proposed[:q]+new+proposed[q+len(old):]
    reverse = proposed
    for m in reversed(maps):
        q = m['position']; assert reverse[q:q+len(m['after'])] == m['after']
        reverse = reverse[:q]+m['before']+reverse[q+len(m['after']):]
    assert reverse == source
    assert displays(source) == displays(proposed) and refs(source) == refs(proposed)
    assert commands(source) == commands(proposed)
    permitted = source
    for g in guards:
        if g['inline_math_mentions_removed']: permitted = permitted.replace(g['before'], g['after'], 1)
    assert math(permitted) == math(proposed)
    for p, raw in protected.items(): assert p.read_bytes() == raw, p
    result = {'paper': 'I', 'candidate': 18, 'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'source_sha256': SOURCE, 'pdf_sha256': PDF, 'defect_log_sha256': sha(protected[R/'S6_SERIES_PUBLISH_defects_I.tsv']), 'check_ledger_sha256': sha(protected[R/'CHECK_EVENTS.tsv']), 'reading_record': str(rp.relative_to(R)), 'reading_record_sha256': READING, 'guards': guards, 'full_blocks': archives, 'guard_count': len(guards), 'complete_block_count': len(archives), 'exact_inverse_map': maps, 'proposed_source_sha256': sha(proposed.encode()), 'exact_forward_and_inverse_reconstruction_verified': True, 'all_display_mathematical_segments_identical': True, 'all_inline_mathematical_segments_identical': False, 'inline_math_qualification': 'Only a repeated E mention in I18-edits-01 and a repeated Y mention in I18-edits-03 are removed with their redundant prose clauses. Every other inline segment and all displayed mathematics remain in identical order. Exact defining and operative witnesses are bound for both mentions.', 'all_command_reference_label_target_sequences_identical': True, 'all_statements_byte_identical': True, 'source_modified': False, 'canonical_status_modified': False, 'completed_reading_and_dossier_unchanged': True, 'mathematical_events_added': 0, 'additional_full_page_credit': 0, 'retained_contextual_dispositions': [{'page': 224, 'text': 'This proves every asserted property.', 'disposition': 'Retained as a conventional proof-closing sentence after the concrete gluing, properness, smoothness, flatness and component-rotation conclusions. It introduces no run/file/verification vocabulary and adds no historical or scope disclaimer.'}, {'page': 237, 'text': 'We check the exact admissibility definition', 'disposition': 'Retained with its exact primary definition citation; the following face-by-face calculation is the operative admissibility application. The cited mathematical criterion and its full construction remain.'}, {'pages': [239, 240], 'text': 'The computation uses the displayed bivector automorphy.', 'disposition': 'Confirmed D08 recap after full owning-source read; I18-edits-04 removes only this sentence. The anticanonical lift and exact deck action already appear in the unchanged argument.'}], 'scope': 'Four guarded prose proposals following the33 actual complete-page readings. The four complete owning statements and proofs were read in source against their rendered context. Preserved witnesses, exact full-block pairs, and inverse source maps are provided. Root approval and later application/rendered coverage remain pending.'}
    out = O/'S6_SERIES_PUBLISH_I_candidate18_edits_guards.json'
    assert not out.exists()
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    md = ['# Paper I candidate18 — guarded prose proposals', '', f'Source: `{SOURCE}`', f'PDF: `{PDF}`', f'Immutable actual reading: `{READING}`', '', 'Four proposals in four complete statements/proofs: three D02 clauses and one D08 recap. Every statement, display, label, target, command and reference is preserved. Two repeated inline symbol mentions, E and Y, are removed with their prose clauses and explicitly tied to unchanged definitions and operative uses. No canonical edits or new mathematical events.', '', '| Guard | Page | Type | Owning statement | Reason |', '|---|---:|---|---|---|']
    for g in guards: md.append(f"| {g['id']} | {g['page']} | {g['type']} | `{g['statement_id']}` | {g['reason']} |")
    out.with_suffix('.md').write_text('\n'.join(md)+'\n')
    print(json.dumps({'guard_file': str(out.relative_to(R)), 'sha256': sha(out.read_bytes()), 'guards': len(guards), 'complete_blocks': len(archives), 'proposed_source_sha256': sha(proposed.encode()), 'source_modified': False, 'mathematical_events_added': 0}, indent=2))


if __name__ == '__main__': main()
