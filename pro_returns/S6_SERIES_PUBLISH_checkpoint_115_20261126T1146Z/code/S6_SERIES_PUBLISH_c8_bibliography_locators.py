"""Exact Paper III citation-locator proposal; inspection is the default.

Root alone may run --apply.  Every edit below changes one already identified
citation's printed locator.  The same exact edits are guarded in their owned
fragments and in the canonical Paper III source.  This program makes no
shared-ledger, event-table, count, bibliography or other-paper changes.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
UNITS = Path('agents/continuation8_iii_integration/units')
CANONICAL = Path('S6_SERIES_PUBLISH_III.tex')
REVIEW = 'agents/continuation8_iii_later/S6_SERIES_PUBLISH_III_bibliography_publication_review.md'

# Fragment, exact old citation, exact replacement, expected occurrences,
# primary-edition/page evidence.  Repeated occurrences are intentional.
EDITS = [
 ('foundations/elliptic_basic_families.tex',
  r'\cite[\S2.1, (2.11)--(2.12)]{manViaclovskyLogs26}',
  r'\cite[\S2.1, equations~(2.11)--(2.12), p.~4]{manViaclovskyLogs26}', 1,
  'Viaclovsky Logs v1: complete printed page4 newly read.'),
 ('foundations/elliptic_basic_families.tex',
  r'\cite[Proposition~2.3]{manViaclovskyLogs26}',
  r'\cite[Proposition~2.3, pp.~5--6]{manViaclovskyLogs26}', 1,
  'Viaclovsky Logs v1: whole proposition and proof newly read on5--6.'),
 ('foundations/elliptic_basic_families.tex',
  r'\cite[Proposition~4.1]{manViaclovskyLogs26}',
  r'\cite[Proposition~4.1, p.~9]{manViaclovskyLogs26}', 1,
  'Viaclovsky Logs v1: whole proposition and proof newly read on9.'),
 ('foundations/elliptic_basic_families.tex',
  r'\cite[Theorem~7.1 and Appendix~B]{manWang26}',
  r'\cite[Theorem~7.1, p.~15; Appendix~B, pp.~17--19]{manWang26}', 1,
  'Wang v2: complete15,17--19 newly read for the actual cited orientation/type scope; SHA matches admitted c5 v2.'),
 ('foundations/elliptic_finite_multiplicities.tex',
  r'\cite[Corollary~6.13; \S8.8; \S\S11.8 and 11.10, (22)]{manSS10}',
  r'\cite[Corollary~6.13, p.~29; \S8.8, p.~41; \S11.8 and Table~4, pp.~51--52; \S11.10, equation~(22), p.~52]{manSS10}', 1,
  'Schuett--Shioda v3: complete29,41,51--52 newly read; matches foundations existing opened-formula record.'),
 ('foundations/elliptic_finite_multiplicities.tex',
  r'\cite[Lemma 3.10]{manLR26}',
  r'\cite[Lemma~3.10, pp.~11--12]{manLR26}', 1,
  'Liu--Rollenske v2: complete11--12 newly read.'),
 ('foundations/elliptic_finite_multiplicities.tex',
  r'\cite[Proposition 3.11]{manLR26}',
  r'\cite[Proposition~3.11, p.~12]{manLR26}', 1,
  'Liu--Rollenske v2: complete12 newly read.'),
 ('foundations/elliptic_marked_data.tex',
  r'\cite[Table~3, rows~50 and~56]{manFukae02}',
  r'\cite[Table~3, rows~50 and~56, p.~35]{manFukae02}', 1,
  'Fukae v1: complete printed35 (PDF36) read as text and rendered image; exact two rows and footer visible.'),
 ('foundations/elliptic_marked_data.tex',
  r'\cite[\S8.4]{manSS10}',
  r'\cite[\S8.4, p.~39]{manSS10}', 1,
  'Schuett--Shioda v3: complete39 newly read, exact minimal degree criterion.'),
 ('foundations/elliptic_marked_data.tex',
  r'\cite[Theorem 6.3]{manSS10}',
  r'\cite[Theorem~6.3, p.~23]{manSS10}', 1,
  'Schuett--Shioda v3: complete23 newly read, actual section-to-NS/T map.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Table 1 and \S9]{manBesserLivne12}',
  r'\cite[Table~1, p.~10; \S9, p.~17]{manBesserLivne12}', 1,
  'Besser--Livne v2: complete9--10 and17 newly read; same SHA as admitted c5 record.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[\S8.4]{manSS10}',
  r'\cite[\S8.4, p.~39]{manSS10}', 1,
  'Schuett--Shioda v3: complete39 newly read.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Lemma 2.1 and Corollary 2.2]{E26}',
  r'\cite[Lemma~2.1 and Corollary~2.2, pp.~3--4; Proposition~2.4, p.~5]{E26}', 1,
  'Engel v1: complete3--5 newly read. Add the actual contraction/properness owner Proposition2.4 to the retained line/section owners.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Propositions 2.7 and 2.9]{E26}',
  r'\cite[Propositions~2.7 and~2.9, pp.~6--7]{E26}', 1,
  'Engel v1: complete6--7 newly read, periods and section extension.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Proposition 2.7]{E26}',
  r'\cite[Proposition~2.7, p.~6]{E26}', 1,
  'Engel v1: complete6 newly read.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Lemma 3.2 and \S3.3]{manViaclovskyTwo26}',
  r'\cite[Proposition~3.1, pp.~6--7]{manViaclovskyTwo26}', 1,
  'Viaclovsky two-parameter v1: complete6--9 newly read. The invoked primitive hexagonal filling/specialization belongs to Proposition3.1; Lemma3.2/section3.3 concern the order-four good-reduction and logarithmic construction. The exact KZ owner and displayed maps remain unchanged.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Proposition 3.1]{E26}',
  r'\cite[Proposition~3.1, pp.~8--9]{E26}', 1,
  'Engel v1: complete8--9 newly read.'),
 ('foundations/elliptic_poincare.tex',
  r'\cite[Proposition 3.1 and Corollary 3.2]{E26}',
  r'\cite[Proposition~3.1 and Corollary~3.2, pp.~8--9]{E26}', 1,
  'Engel v1: complete8--9 newly read, with exact order-three/order-four base-change scope retained.'),
 ('later/os49_construction.tex',
  r'\cite[\S4.5 and \S8.4]{manSS10}',
  r'\cite[\S4.5 and Table~1, p.~14; \S8.4, p.~39]{manSS10}', 1,
  'Schuett--Shioda v3: complete14 and39 newly read.'),
 ('later/os49_construction.tex',
  r'\cite[\S6.11 and \S11]{manSS10}',
  r'\cite[\S6.11, p.~29; \S11.8 and Table~4, pp.~51--52]{manSS10}', 1,
  'Schuett--Shioda v3: complete29,51--52 newly read, exact rank and local height formulas.'),
 ('later/os49_construction.tex',
  r'\cite[Proposition~3.1]{manViaclovskyTwo26}',
  r'\cite[Proposition~3.1, pp.~6--7]{manViaclovskyTwo26}', 1,
  'Viaclovsky two-parameter v1: complete6--7 newly read.'),
 ('later/os49_construction.tex',
  r'\cite[Lemma~7.4]{E26}',
  r'\cite[Lemma~7.4, pp.~18--19]{E26}', 1,
  'Engel v1: whole lemma/proof18--19 newly read; this application invokes its Mumford clause on19.'),
 ('later/os49_graph_caps.tex',
  r'\cite[Proposition~2.8]{E26}',
  r'\cite[Proposition~2.8, pp.~6--7]{E26}', 1,
  'Engel v1: whole periodic fan statement/proof6--7 newly read.'),
 ('later/os49_graph_caps.tex',
  r'\cite[Remark~8.5]{E26}',
  r'\cite[Remark~8.5, p.~24]{E26}', 1,
  'Engel v1: whole24 newly read, full fibrewise degree-zero line scope retained.'),
 ('later/limits_and_open_points.tex',
  r'\cite[Remark~8.5]{E26}',
  r'\cite[Remark~8.5, p.~24]{E26}', 1,
  'Engel v1: whole24 newly read, full open-family scope retained.'),
 ('root/full_sphere_nullity.tex',
  r'\cite[Corollary~4.24]{Hatcher2002}',
  r'\cite[Corollary~4.24, pp.~360--361]{Hatcher2002}', 2,
  'Recorded root whole primary reading, quotient_maps_unit_review.md D18; no new primary reading claimed here.'),
 ('root/full_sphere_nullity.tex',
  r'\cite[Corollary~4.25]{Hatcher2002}',
  r'\cite[Corollary~4.25, p.~361]{Hatcher2002}', 1,
  'Recorded root whole corollary/proof reading, base_map_unit_review.md source section; this pass read that record.'),
 ('root/sphere_smash_pairing.tex',
  r'\cite[Corollary~4.24]{Hatcher2002}',
  r'\cite[Corollary~4.24, pp.~360--361]{Hatcher2002}', 1,
  'Recorded root whole primary reading, quotient_maps_unit_review.md D18; no new primary reading claimed here.'),
 ('root/sphere_smash_pairing.tex',
  r'\cite[Corollary~4.25]{Hatcher2002}',
  r'\cite[Corollary~4.25, p.~361]{Hatcher2002}', 1,
  'Recorded root whole corollary/proof reading, base_map_unit_review.md source section; this pass read that record.'),
 ('weighted/residual_even_types.tex',
  r'\cite[Sections~3.11--3.14]{manZhubr75}',
  r'\cite[Sections~3.11--3.14, pp.~806--808]{manZhubr75}', 2,
  'Exact English-edition locator in wholly read c7 LF source_checks section4; no new Zhubr page opening claimed.'),
 ('weighted/residual_even_types.tex',
  r'\cite[Definition~1.7, Remark~1.8 and Theorem~3.1]{mapsKaplan79}',
  r'\cite[Definition~1.7 and Remark~1.8, pp.~239--240; Theorem~3.1, pp.~243--246]{mapsKaplan79}', 2,
  'Wholly read c7 LL source_checks: actual indexed-primary text239--240,243--246, not a successful PDF/image opening.'),
 ('weighted/three_primary_types.tex',
  r'\cite[\S\S3.11--3.14 and Theorem~5]{manZhubr75}',
  r'\cite[\S\S3.11--3.14, pp.~806--808; Theorem~5, p.~796]{manZhubr75}', 1,
  'Exact English-edition locator in wholly read c7 LF source_checks section4; no new Zhubr page opening claimed.'),
]


def anchors(text):
    return {name: Counter(re.findall(r'\\'+name+r'\{([^{}]+)\}', text))
            for name in ('label', 'hypertarget')}


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--apply', action='store_true',
                    help='Root-only: apply exactly the inspected citation replacements.')
args = parser.parse_args()
grouped = defaultdict(list)
canonical_edits = {}
for fragment, old, new, count, evidence in EDITS:
    assert old.startswith(r'\cite[') and new.startswith(r'\cite[')
    assert old.rsplit('{', 1)[1] == new.rsplit('{', 1)[1]
    grouped[UNITS / fragment].append((old, new, count, evidence))
    if old in canonical_edits:
        prior_new, prior_count, prior_evidence = canonical_edits[old]
        assert prior_new == new
        canonical_edits[old] = (new, prior_count + count, prior_evidence)
    else:
        canonical_edits[old] = (new, count, evidence)
grouped[CANONICAL] = [(old, new, count, evidence)
                      for old, (new, count, evidence) in canonical_edits.items()]

prepared = {}
rows = []
for relative, replacements in grouped.items():
    path = ROOT / relative
    old_text = path.read_text()
    new_text = old_text
    for old, new, count, evidence in replacements:
        actual = old_text.count(old)
        if actual != count:
            raise ValueError(f'{relative}: expected {count} occurrences of {old!r}, found {actual}')
        for match in re.finditer(re.escape(old), old_text):
            context = old_text[max(0, match.start()-110):min(len(old_text), match.end()+110)]
            rows.append(dict(path=str(relative), line=old_text.count('\n', 0, match.start())+1,
                             old=old, new=new, context=context,
                             type='D06;D18', evidence=evidence, review=REVIEW))
        new_text = new_text.replace(old, new)
    assert anchors(old_text) == anchors(new_text)
    prepared[path] = (old_text, new_text)

print(json.dumps(dict(mode='apply' if args.apply else 'inspect-only',
                      utc=datetime.now(timezone.utc).isoformat(),
                      scope='exact citation-locator tokens; no theorem or parameter change'),
                 ensure_ascii=False))
for row in rows:
    print(json.dumps(row, ensure_ascii=False, sort_keys=True))
if args.apply:
    # All source and anchor guards pass before the first mutation.
    for path, (old_text, new_text) in prepared.items():
        assert path.read_text() == old_text, 'Concurrent source change: '+str(path)
    for path, (_, new_text) in prepared.items():
        path.write_text(new_text, encoding='utf-8', newline='\n')
    print('APPLIED exactly the declared fragments and canonical III citation locators; shared records untouched.')
else:
    print('INSPECTED ONLY: no source or shared record was written; root owns --apply and D06/event admission.')
