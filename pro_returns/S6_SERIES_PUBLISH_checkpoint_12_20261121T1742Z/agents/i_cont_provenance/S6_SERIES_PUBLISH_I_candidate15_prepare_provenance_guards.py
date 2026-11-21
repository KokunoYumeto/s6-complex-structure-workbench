#!/usr/bin/env python3
"""Prepare exact, unapplied editorial guards from the actual candidate15 page reading."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import difflib
import hashlib
import json
import re
from S6_SERIES_PUBLISH_I_cont_recount import proof_end

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8'
PDF_SHA = 'b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def shatext(text):
    return hashlib.sha256(text.encode()).hexdigest()


source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
assert sha(source) == SOURCE_SHA
text = source.read_text()
guards = []


def add(number, page, kind, scope, before, after, reason):
    assert text.count(before) == 1, (number, text.count(before), before)
    assert before != after
    guards.append({
        'id': f'I15-prov-{number:02d}', 'page': page, 'type': kind,
        'statement_id': scope,
        'line': text.count('\n', 0, text.index(before))+1,
        'before': before, 'after': after, 'reason': reason,
        'source_sha256': SOURCE_SHA, 'pdf_sha256': PDF_SHA,
        'status': 'proposed, not applied', 'mathematical_events_added': 0,
    })


add(1, 308, 'D02', 'ari:C.7.11',
    'This proves periodicity on all of $\\C^2$, not only\non the real diagonal.',
    'This proves periodicity on all of $\\C^2$.',
    'The positive scope already states all of C^2, and the preceding sigma multiplier calculation proves it. Remove the repeated contrast with the diagonal; the same domain, function, transformation and proof remain.')
add(2, 308, 'D02', 'ari:C.7.11',
    'This proves the rank assertion, with no extra algebraic\nindependence assumption on $u$ and the periods.',
    'This proves the rank assertion.',
    'The preceding two sentences derive alpha=0 and omega=0 from nontorsion, then state that Z[beta]u and the period lattice are independent over Z. Remove the negative-assumption tail. The repeated inline name u in that tail refers to the identical u already retained in those equations and in the statement; no hypothesis, quantifier, map or value is removed.')
add(3, 309, 'D02', 'ari:C.7.11',
    '\\eqref{ari:eq:cc-fixedfield} places all values in $K[H_0]$,\nwith no algebraicity assumption on $H_0$.',
    '\\eqref{ari:eq:cc-fixedfield} places all values in $K[H_0]$.',
    'The exact fixed-field identity and the construction of the number field K give the positive membership statement K[H0]. Remove the negative-assumption tail. H0 remains explicitly defined as H(u,u)=N(Q)^4 in the same proposition and appears in the retained membership statement.')
add(4, 311, 'D08', 'ari:C.7.12',
    'The explicit interpolation and tangent\ncalculations below record what these bounds establish.',
    '',
    'This closing sentence announces what following calculations will record and states no mathematical assertion. All division values, field statements, height/degree bounds, parameter maps and the existing open-question pointer remain, as do the complete following calculations.')
add(5, 315, 'D11', 'ari:C.7.12',
    'These precise inputs supply no evaluation of $N_0$ here.\n',
    '',
    'This is a repeated negative scope conclusion after the exact Mahler and entropy inputs. The complete Taylor coefficient, transcendence argument, multiplication map, entropy sequence and citations remain. The repeated inline name N0 has the unchanged definition N0=N(Q), retained throughout the statement/proof and final open-question section.')
add(6, 315, 'D11', 'ari:C.7.12',
    "These\nexplicit ranks leave that question open.",
    '',
    'The preceding sentence already gives the exact point-algebraicity reduction, following the rank-one period line, bound 3 and rank-two span. Remove only the repeated closing scope sentence; all ranks and the exact reduction remain.')
add(7, 316, 'D01', 'night:P5.7',
    '\\begin{remark}[Source comparison for the credited re-derivations]',
    '\\begin{remark}[Period and deformation comparison]',
    'The title names the production of re-derivations. The replacement names the mathematical comparison proved in the same remark, with its number, tag and labels preserved.')
add(8, 316, 'D01', 'night:P5.7',
    'For the fixed standard $(3,4,\\infty)$ data, our re-derived tangent\ncohomology',
    'For the fixed standard $(3,4,\\infty)$ data, the tangent\ncohomology',
    'Remove the own-work history adjective while retaining the same fixed data, tangent tuple, germ, automorphism group, equivalence and named external source.')
add(9, 316, 'D01', 'night:P5.7',
    'assertions. The tangent and deformation calculations in this appendix\nwere re-derived after reading version~1. Our working-edition chronology records the public proof of the exact\n$2\\mathbb Z$ equivalence by 8 September 2026. Version~1, submitted on\n23 September 2026, states that equivalence as its Theorem~1.4.',
    'assertions. Version~1, submitted on\n23 September 2026, states the exact $2\\mathbb Z$ equivalence as its Theorem~1.4.',
    'Remove the two own-production chronology sentences, whose facts remain in the archived original block and inherited records. Keep the external version/date/locator and the identical exact 2Z equivalence. The complete coordinate map, inverse, half-plane relation, ordinary/finite/cusp comparisons and all four source assertions remain in the proof.')
add(10, 316, 'D11', 'night:P5.7',
    'This comparison records the contents of the two specified versions;\nit assigns no reason for the change.\n',
    '',
    'The preceding sentences give the precise positive contents of version 2 and the specific omitted sections/assertions. Remove the repeated closing disclaimer about assigning a reason; the mathematical comparison and its exact sources remain.')
add(11, 321, 'D23', 'I:standard-deformation-credit',
    'the tangent dimensions and smooth reduced Kuranishi germ are\n\\cite[Theorem~6.12, pp.~81--82; Proposition~6.16, p.~85]{DuEtAl2026v1}.',
    'the tangent dimensions and smooth reduced Kuranishi germ are given in\n\\cite[Theorem~6.12, pp.~81--82; Proposition~6.16, p.~85]{DuEtAl2026v1}.',
    'Complete the grammatical relation to the citation while preserving the exact cited theorem, proposition and page numbers.')
add(12, 321, 'D08', 'I:standard-deformation-credit',
    'We re-derive that case in this appendix. The weighted calculation\n',
    'The weighted calculation\n',
    'Remove the production-oriented re-derivation sentence. The preceding exact standard-case credit and the following positive account of the coprime multiplicities and coarse tangent images remain.')
add(13, 326, 'D23', 'night:P5.2',
    'The root splitting and structure-sheaf direct images are\n\\cref{inv:D1.2,push:src:E.3.1}; in the standard data these are also\n\\cite[Proposition~6.6, pp.~77--78; Lemma~6.7, p.~78;\nProposition~6.10, pp.~79--80]{DuEtAl2026v1}.',
    'The root splitting and structure-sheaf direct images are given in\n\\cref{inv:D1.2,push:src:E.3.1}; in the standard data these are also computed in\n\\cite[Proposition~6.6, pp.~77--78; Lemma~6.7, p.~78;\nProposition~6.10, pp.~79--80]{DuEtAl2026v1}.',
    'Complete the two grammatical citation constructions. Both internal references, all three external locators and every mathematical formula in the complete theorem/proof remain.')
add(14, 335, 'D18', 'bib:BumpFriedbergHoffstein1990',
    '\\newblock URL \\url{https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf}.',
    '\\newblock \\doi{10.1007/BF01233440}.',
    'Replace the third-party personal-site copy with the publisher DOI actually opened. The Springer page matches the existing title, all three authors, journal, volume 102, pages 543--618 and year 1990. The attached prior proof-reading records and exact printed locators remain untouched.')
add(15, 340, 'D18', 'bib:CrGross1991',
    '\\newblock Chapter scan: \\url{https://wstein.org/papers/bib/gross-kolyvagins_work_on_modular_elliptic_curves.pdf}.\n',
    '',
    'Remove the third-party personal-site scan link. The existing DOI 10.1017/CBO9780511526053.009 remains and its Cambridge page was actually opened, matching author, book, printed pages 235--256 and year 1991. The inherited chapter title and all theorem locators remain; prior actual source-reading receipts retain their own scope.')
add(16, 342, 'D18', 'bib:Merkulov1995D',
    '\\newblock URL \\url{https://doi.org/10.1017/S0305004100073473}.\n',
    '',
    'The identical DOI is already printed immediately above. Remove its second rendering as a URL; retain one publisher DOI and all bibliography metadata.')
add(17, 342, 'D18', 'bib:Movasati24',
    '\\newblock Author version dated 13 May 2024, 2024.',
    '\\newblock Author version dated 13 May 2024.',
    'Remove the duplicated year after the complete version date. The cited date, title, author and author-hosted URL remain.')
add(18, 344, 'D18', 'bib:silverman2006heights',
    '\\newblock MSRI workshop lecture slides, January 2006, 2006.',
    '\\newblock MSRI workshop lecture slides, January 2006.',
    'Remove the duplicated year after the complete month/year date. The lecture version, title, author and official workshop URL remain.')


def bibblock(key):
    occurrences = list(re.finditer(r'\\bibitem\[', text))
    for index, marker in enumerate(occurrences):
        end = occurrences[index+1].start() if index+1 < len(occurrences) else text.index(r'\end{thebibliography}', marker.end())
        block = text[marker.start():end].rstrip('\n')
        header = block[:block.index('\n')]
        if '{'+key+'}' in header:
            return block
    raise ValueError(key)


format_specs = [
    (19, 336, 'ConradSL2Z'), (20, 336, 'Cornulier2011'),
    (21, 336, 'CDL24'), (22, 337, 'Drinfeld1973'),
    (23, 341, 'LinWang2010'), (24, 341, 'MazurSteinTate2006'),
    (25, 343, 'RR70push'), (26, 343, 'RRV71'),
]
for number, page, key in format_specs:
    before = bibblock(key)
    after = re.sub(r'(?<!\n)\n(?=\\newblock)', '\n\n', before)
    reason = ('Separate the existing author/title/publication/link fields with the same paragraph boundaries used by the surrounding bibliography. All existing field text, edition qualifications and URLs are preserved.')
    if key == 'Cornulier2011':
        after = after.replace(r'\href{https://doi.org/10.2140/agt.2011.11.2007}{doi:10.2140/agt.2011.11.2007}', r'\doi{10.2140/agt.2011.11.2007}')
        reason += ' Render the identical DOI through the existing common DOI macro.'
    if key == 'RR70push':
        after = after.replace('Ramis, J.-P. and Ruget, G. (1970).', 'J.-P. Ramis and G. Ruget.')
        after = after.replace(r'38:77--91.', r'38:77--91, 1970.')
        after = after.replace(r'\url{https://doi.org/10.1007/BF02684652}', r'\doi{10.1007/BF02684652}')
        reason += ' Put the same initials before the surnames and the same year after the journal/page field, matching the surrounding style; use the common macro for the identical DOI. The citation key and optional author-year label remain unchanged.'
    if key == 'RRV71':
        after = after.replace('Ramis, J.-P., Ruget, G., and Verdier, J.-L. (1971).', 'J.-P. Ramis, G. Ruget, and J.-L. Verdier.')
        after = after.replace(r'13:261--283.', r'13:261--283, 1971.')
        after = after.replace(r'\url{https://doi.org/10.1007/BF01406078}', r'\doi{10.1007/BF01406078}')
        reason += ' Put the same initials before the surnames and the same year after the journal/page field, matching the surrounding style; use the common macro for the identical DOI. The citation key and optional author-year label remain unchanged.'
    add(number, page, 'D18', 'bib:'+key, before, after, reason)


assert [g['id'] for g in guards] == [f'I15-prov-{n:02d}' for n in range(1,27)]
proposed = text
for guard in guards:
    assert proposed.count(guard['before']) == 1, guard['id']
    proposed = proposed.replace(guard['before'], guard['after'], 1)


def all_anchors(value):
    return re.findall(r'\\(?:label|hypertarget)\{[^}]+\}', value)


def display_math(value):
    return re.findall(r'\\\[.*?\\\]|\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}', value, re.S)


def inline_math(value):
    return re.findall(r'(?<!\\)\$(?:\\.|[^$\\])*?(?<!\\)\$', value, re.S)


assert all_anchors(proposed) == all_anchors(text)
assert display_math(proposed) == display_math(text)
assert re.findall(r'\\(?:cite\w*|cref|Cref|ref|eqref)(?:\[[^\]]*\])?\{[^}]+\}', proposed) == re.findall(r'\\(?:cite\w*|cref|Cref|ref|eqref)(?:\[[^\]]*\])?\{[^}]+\}', text)
removed_inline = []
for guard in sorted(guards, key=lambda g: text.index(g['before'])):
    # Each exact mutation starts and ends outside inline math. Comparing the
    # balanced mutation fragments avoids assigning dollar delimiters in TeX
    # comments or macro definitions to printed mathematics.
    assert guard['before'].count('$') % 2 == guard['after'].count('$') % 2 == 0
    left, right = inline_math(guard['before']), inline_math(guard['after'])
    for kind, i, j, k, l in difflib.SequenceMatcher(a=left, b=right, autojunk=False).get_opcodes():
        if kind != 'equal':
            assert kind == 'delete', (guard['id'], kind, left[i:j], right[k:l])
            removed_inline += left[i:j]
assert removed_inline == ['$u$', '$H_0$', '$N_0$'], removed_inline

archive_dir = OUT / 'candidate15_review_blocks'
archive_dir.mkdir(exist_ok=True)


def statement_block(sid):
    position = text.index('\\label{'+sid+'}', text.index(r'\begin{document}'))
    starts = list(re.finditer(r'\\begin\{(proposition|theorem|lemma|remark|definition|cited)\}', text[:position]))
    match = starts[-1]
    end = text.index('\\end{'+match[1]+'}', position)+len('\\end{'+match[1]+'}')
    proof_match = re.match(r'\s*\\begin\{proof\}', text[end:])
    if proof_match:
        pstart = end+proof_match.end()-len(r'\begin{proof}')
        end = proof_end(text, pstart)
    return text[match.start():end]


groups = collections.defaultdict(list)
for guard in guards:
    groups[guard['statement_id']].append(guard)
archives = []
for index, (sid, members) in enumerate(groups.items(), 1):
    before = bibblock(sid[4:])+'\n' if sid.startswith('bib:') else statement_block(sid)
    after = before
    for guard in members:
        assert after.count(guard['before']) == 1, (sid, guard['id'])
        after = after.replace(guard['before'], guard['after'], 1)
    before_path = archive_dir / f'block_{index:02d}_before.tex'
    after_path = archive_dir / f'block_{index:02d}_proposed.tex'
    before_path.write_text(before+'\n')
    after_path.write_text(after+'\n')
    info = {'scope_id': sid, 'guards': [g['id'] for g in members],
            'before': str(before_path.relative_to(ROOT)), 'before_sha256': sha(before_path),
            'proposed': str(after_path.relative_to(ROOT)), 'proposed_sha256': sha(after_path),
            'all_display_math_identical': display_math(before) == display_math(after),
            'all_labels_and_targets_identical': all_anchors(before) == all_anchors(after)}
    archives.append(info)
    for guard in members:
        guard['original_full_block'] = info['before']
        guard['original_full_block_sha256'] = info['before_sha256']
        guard['proposed_full_block'] = info['proposed']
        guard['proposed_full_block_sha256'] = info['proposed_sha256']
        guard['all_display_math_identical'] = info['all_display_math_identical']
        guard['all_labels_and_targets_identical'] = info['all_labels_and_targets_identical']

guard_path = OUT / 'S6_SERIES_PUBLISH_I_candidate15_provenance_guards.json'
guard_path.write_text(json.dumps(guards, ensure_ascii=False, indent=2)+'\n')
publisher = OUT / 'S6_SERIES_PUBLISH_I_candidate15_publisher_link_receipts.json'
receipt = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'paper': 'I', 'candidate': 15, 'source_sha256': SOURCE_SHA,
    'pdf_sha256': PDF_SHA,
    'guard_file': str(guard_path.relative_to(ROOT)), 'guard_sha256': sha(guard_path),
    'proposals': len(guards), 'types': dict(collections.Counter(g['type'] for g in guards)),
    'whole_proposed_source_sha256': shatext(proposed),
    'all_display_math_sequences_identical': True,
    'all_labels_and_hypertargets_identical': True,
    'all_citation_and_reference_commands_identical': True,
    'inline_math_sequence_difference': {
        'removed_repeated_names_only': removed_inline,
        'guard_map': {'I15-prov-02': '$u$', 'I15-prov-03': '$H_0$', 'I15-prov-05': '$N_0$'},
        'retained_identity_map': {
            '$u$': 'The identical logarithm u remains defined by Q=exp_E u in Proposition 26.19 and appears in alpha u+omega and Z[beta]u immediately before the deleted tail.',
            '$H_0$': 'The identical H0 remains defined by H0=H(u,u)=N(Q)^4 and remains the generator in the retained K[H0] membership assertion.',
            '$N_0$': 'The identical N0 remains defined by N0=N(Q) in Proposition 26.20, with all scalar models, parameter formulas, bounds and final open-question identification unchanged.',
        },
        'no_new_or_changed_inline_formula': True,
        'note': 'A literal all-inline-segments-identical claim would be false. Three redundant variable-name occurrences are removed with their prose-only scope tails; their exact existing definitions and mathematical uses remain.',
    },
    'block_archives': archives,
    'publisher_link_receipts': {'path': str(publisher.relative_to(ROOT)), 'sha256': sha(publisher)},
    'reading_record': 'agents/i_cont_provenance/S6_SERIES_PUBLISH_I_final_candidate15_reading_provenance.json',
    'mathematical_statement_changes': 0,
    'mathematical_events_added': 0,
    'source_changes_applied': False,
    'shared_files_modified': False,
    'scope': 'Exact proposals from actual full-page reading and complete relevant source-block comparison. Every equation, hypothesis, quantifier, map and mathematical value is retained; explicit repeated-name deletions are mapped above. Publisher verification authenticates bibliography replacements only and adds no proof credit.',
}
receipt_path = OUT / 'S6_SERIES_PUBLISH_I_candidate15_provenance_guard_receipt.json'
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
fence = chr(96)*3
md = ['# Candidate15: exact provenance-agent editorial proposals', '',
      f'Source SHA-256: {SOURCE_SHA}. PDF SHA-256: {PDF_SHA}.', '',
      'These 26 proposals remain unapplied. All display-math sequences, labels, hypertargets and citation/reference commands are unchanged in the composed proposal. Three repeated inline names are removed from deleted scope tails; their retained definitions are documented in the JSON receipt. No mathematical event is added.', '']
for guard in guards:
    md.extend([f"## {guard['id']} — page {guard['page']}, {guard['type']}", '',
               guard['reason'], '', 'Before:', '', fence+'tex', guard['before'], fence, '',
               'After:', '', fence+'tex', guard['after'], fence, ''])
(OUT / 'S6_SERIES_PUBLISH_I_candidate15_provenance_guards.md').write_text('\n'.join(md)+'\n')
assert sha(source) == SOURCE_SHA
print(json.dumps({'guard_file': str(guard_path.relative_to(ROOT)), 'guard_sha256': sha(guard_path),
                  'receipt': str(receipt_path.relative_to(ROOT)), 'receipt_sha256': sha(receipt_path),
                  'proposals': len(guards), 'types': receipt['types'],
                  'proposed_source_sha256': shatext(proposed),
                  'removed_repeated_inline_names': removed_inline,
                  'source_changes_applied': False, 'mathematical_events_added': 0}, indent=2))
