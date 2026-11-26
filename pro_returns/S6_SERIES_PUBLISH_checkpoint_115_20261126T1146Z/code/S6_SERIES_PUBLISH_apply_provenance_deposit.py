#!/usr/bin/env python3
"""Apply reviewed exact replacement files, preserving every other paper verbatim."""
from pathlib import Path
import argparse, csv, datetime, hashlib, io, json, re

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def sections(text):
    matches = list(re.finditer(r'^## Paper ([IV]+)\s*$', text, re.M))
    return text[:matches[0].start()] if matches else text, {
        m[1]: text[m.start():matches[i+1].start() if i+1 < len(matches) else len(text)]
        for i, m in enumerate(matches)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('guard', type=Path)
    ap.add_argument('--paper', required=True)
    ap.add_argument('--receipt', type=Path, required=True)
    a = ap.parse_args()
    g = json.loads(a.guard.read_text())
    assert sha(ROOT / f'S6_SERIES_PUBLISH_{a.paper}.tex') == g['source_sha256']
    assert sha(ROOT / 'CHECK_EVENTS.tsv') == g['ledger_sha256']
    prepared = []
    for u in g['updates']:
        target, replacement = Path(u['target']), Path(u['replacement']['path'])
        assert target.parent == ROOT
        assert sha(target) == u['expected_sha256'], str(target)
        assert sha(replacement) == u['replacement']['sha256']
        assert replacement.stat().st_size == u['replacement']['bytes']
        old, new = target.read_text(), replacement.read_text()
        if target.suffix == '.tsv':
            before = csv.DictReader(io.StringIO(old), delimiter='\t')
            after = csv.DictReader(io.StringIO(new), delimiter='\t')
            assert before.fieldnames == after.fieldnames
            oldrows, newrows = list(before), list(after)
            assert [x for x in oldrows if x['paper'] != a.paper] == [x for x in newrows if x['paper'] != a.paper]
            ids = [x['claim_id'] for x in newrows]
            assert len(ids) == len(set(ids))
        else:
            oldhead, oldparts = sections(old)
            newhead, newparts = sections(new)
            assert oldhead == newhead
            if a.paper not in oldparts:
                # A newly appended paper may add one blank separator after the
                # exact old document. No existing byte is replaced.
                assert new.startswith(old)
                assert new[len(old):] in (newparts[a.paper], '\n' + newparts[a.paper])
            else:
                assert {k:v for k,v in oldparts.items() if k != a.paper} == {k:v for k,v in newparts.items() if k != a.paper}
        prepared.append((target, replacement, u))
    assert not a.receipt.exists(), 'Do not overwrite an application receipt.'
    for target, replacement, _ in prepared:
        target.write_bytes(replacement.read_bytes())
    receipt = {'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'paper':a.paper, 'guard':str(a.guard), 'guard_sha256':sha(a.guard),
               'source_sha256':g['source_sha256'], 'ledger_sha256':g['ledger_sha256'],
               'other_papers_preserved':True, 'math_events_added':0,
               'updates':[u for _,_,u in prepared]}
    a.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'paper':a.paper,'updates':len(prepared),'other_papers_preserved':True}))

if __name__ == '__main__':
    main()
