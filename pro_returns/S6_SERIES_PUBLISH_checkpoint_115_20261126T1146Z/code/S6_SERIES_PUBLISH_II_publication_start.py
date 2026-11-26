"""First exact presentation transport for Paper II; no proof-check credit."""
from pathlib import Path
import argparse, collections, csv, datetime, hashlib, io, json, re
from S6_SERIES_PUBLISH_engine_baseline import portable

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = '74497bfe327fae25c9cdcb17334b3bf42a9793a9df7c0a4404d97568f2f760f0'
sha = lambda b: hashlib.sha256(b).hexdigest()
p = argparse.ArgumentParser()
p.add_argument('--apply', action='store_true')
a = p.parse_args()
source = ROOT / 'S6_SERIES_PUBLISH_II.tex'
before = source.read_bytes()
assert sha(before) == EXPECTED
text = before.decode()
changes = []

def replace(old, new, kind, reason, context):
    global text
    assert text.count(old) == 1, (context, text.count(old))
    offset = text.index(old)
    changes.append(dict(old=old, new=new, type=kind, statement_id=context,
                        offset=offset, source_line=text[:offset].count('\n')+1,
                        reason=reason))
    text = text[:offset] + new + text[offset+len(old):]

_, font_changes = portable(text)
for old, new in font_changes:
    replace(old, new, 'D23', 'Use the standard pdfLaTeX font declarations; the entire document body is identical under this preamble-only transport.', 'preamble')
lo = text.index('\\newcommand{\\StatementRecord}')
hi = text.index('\\newcommand{\\ExternalPaperRef}', lo)
replace(text[lo:hi], r'\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}'+'\n',
        'D10', 'Print the permanent tag alone. Every statement call, its identifier, status and uses argument remain in source and the check records; the macro no longer prints check-file links or dependency/back-link prose.', 'preamble')
replace(r'\AfterEndEnvironment{proof}{\par\begingroup\footnotesize\noindent\hyperref[sec:results]{Return to \S1.}\par\endgroup\smallskip}', '',
        'D10', 'Remove the repeated proof-navigation footer; preserve every theorem, proof and result-section anchor.', 'preamble')
replace(r'\crefname{corollary}{corollary}{corollarys}', r'\crefname{corollary}{corollary}{corollaries}',
        'D23', 'Correct the generated plural of corollary.', 'preamble')
replace(r'\date{19 November 2026}', r'\date{21 November 2026}',
        'D15', 'Date this publication revision.', 'title block')

# Only the date changes in the document body at this stage. The exact body
# identity protects every formula, statement, proof, label and target.
old_body = before.decode().split('\\begin{document}', 1)[1]
new_body = text.split('\\begin{document}', 1)[1]
assert new_body == old_body.replace(r'\date{19 November 2026}', r'\date{21 November 2026}', 1)
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\StatementRecord\{([^}]+)\}']:
    assert re.findall(pattern, before.decode()) == re.findall(pattern, text)

inverse = text
for c in reversed(changes):
    i = c['offset']
    assert inverse[i:i+len(c['new'])] == c['new']
    inverse = inverse[:i] + c['old'] + inverse[i+len(c['new']):]
assert inverse.encode() == before

log = ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv'
original_log = log.read_bytes()
reader = csv.DictReader(io.StringIO(original_log.decode()), delimiter='\t')
fields = reader.fieldnames
rows = list(reader)
assert not rows
for i,c in enumerate(changes, 1):
    c['change_id'] = f'II-{i:05d}'
    rows.append(dict(change_id=c['change_id'], type=c['type'], statement_id=c['statement_id'],
                     old_location='original publication source line '+str(c['source_line']),
                     old_page='pending baseline mapping', new_location=c['statement_id'],
                     new_page='pending final build', old_text=c['old'], new_text=c['new'],
                     reason=c['reason'], review_status='applied; final page review pending'))
buf = io.StringIO(); writer=csv.DictWriter(buf,fieldnames=fields,delimiter='\t'); writer.writeheader();writer.writerows(rows)
out = ROOT / 'records/S6_SERIES_PUBLISH_II_publication_start'
out.mkdir(exist_ok=True)
receipt = dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), paper='II',
               before_source_sha256=sha(before), after_source_sha256=sha(text.encode()),
               before_defect_log_sha256=sha(original_log), after_defect_log_sha256=sha(buf.getvalue().encode()),
               changes=changes, body_unchanged_except_date=True, exact_forward_and_inverse_maps_verified=True,
               all_labels_targets_and_statement_calls_preserved=True, mathematical_events_added=0, applied=a.apply)
name='apply_receipt.json' if a.apply else 'preparation.json'
assert not (out/name).exists()
(out/name).write_text(json.dumps(receipt,indent=2)+'\n')
if a.apply:
    source.write_text(text); log.write_text(buf.getvalue())
else:
    (out/'proposed.tex').write_text(text)
    (out/'proposed_defects.tsv').write_text(buf.getvalue())
print(json.dumps({k:v for k,v in receipt.items() if k!='changes'},indent=2))
