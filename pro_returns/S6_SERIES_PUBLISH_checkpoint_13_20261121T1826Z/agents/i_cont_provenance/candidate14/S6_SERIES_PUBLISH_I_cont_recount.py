#!/usr/bin/env python3
"""Read-only independent recount of Paper I from its TeX and canonical ledger.

Uses no prior total or generated current-statement table to select events.
An environment owns its statement and immediate proof, and the two explicitly
identified deferred proofs. Historic statement labels in those regions retain
their own associations. Each canonical ledger row is selected at most once.
This is a records computation and creates no mathematical check event.
"""
from pathlib import Path
import argparse, collections, csv, datetime, hashlib, json, re

csv.field_size_limit(100_000_000)
KINDS = ('targeted proof check', 'independent re-proof',
         'computation or formal certificate', 'used and rechecked in this run',
         'carried as background without fault found',
         "refuted, with the refined statement's id")
ENV = re.compile(r'\\begin\{(maintheorem|theorem|lemma|proposition|corollary|definition|remark|cited)\}')
LABEL = re.compile(r'\\label\{([^}]+)\}')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_tsv(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

def proof_end(text, start):
    depth = 0
    for token in re.finditer(r'\\(begin|end)\{proof\}', text[start:]):
        depth += 1 if token[1] == 'begin' else -1
        if depth == 0:
            return start + token.end()
    raise ValueError('Unclosed proof at '+str(start))

def recount(root, base):
    source = root / 'S6_SERIES_PUBLISH_I.tex'
    ledger = root / 'CHECK_EVENTS.tsv'
    tag_source = base / 'S6_SERIES_GRIND_tags.tsv'
    text = source.read_text()
    body_start = text.index(r'\begin{document}')
    starts = list(ENV.finditer(text, body_start))
    historic_tags = read_tsv(tag_source)
    historic_ids = {r['label'] for r in historic_tags if r['kind'] == 'statement'}
    tag_to_label = {'tag:'+r['tag']:r['label'] for r in historic_tags}
    statements = []
    ids = set()
    for index, start in enumerate(starts):
        end_token = '\\end{'+start[1]+'}'
        statement_end = text.index(end_token, start.end()) + len(end_token)
        statement = text[start.start():statement_end]
        header_labels = LABEL.findall(statement)
        record = re.search(r'\\StatementRecord\{([^}]+)\}', statement)
        sid = record[1] if record else header_labels[0] if header_labels else ''
        if not sid:
            raise ValueError('Unidentified environment at '+str(start.start()))
        next_start = starts[index+1].start() if index+1 < len(starts) else len(text)
        gap = text[statement_end:next_start]
        heading = re.search(r'\\(?:section|subsection|subsubsection|part)\*?\{', gap)
        if heading:
            gap = gap[:heading.start()]
        proof = re.search(r'\\begin\{proof\}', gap)
        owned = statement
        if proof:
            pstart = statement_end + proof.start()
            owned += '\n' + text[pstart:proof_end(text, pstart)]
        deferred = {'fam:src:A.3.1':'I:coherent-descent-proof',
                    'fam:src:A.5.1':'app:rederive:fam-src-A.5.1'}
        if sid in deferred:
            label = '\\label{'+deferred[sid]+'}'
            dp = text.index(label)
            pstart = text.index(r'\begin{proof}', dp)
            owned += '\n' + text[dp:proof_end(text, pstart)]
        identities = {sid} | (set(LABEL.findall(owned)) & historic_ids)
        ids.update(identities)
        statements.append({'id':sid, 'kind':start[1],
                           'identities':sorted(identities),
                           'line':text.count('\n',0,start.start())+1})
    assert len({r['id'] for r in statements}) == len(statements)
    events = read_tsv(ledger)
    selected = [(n, r) for n,r in enumerate(events,2)
                if tag_to_label.get(r['statement_id'],r['statement_id']) in ids]
    main_ids = {r['id'] for r in statements if r['kind']=='maintheorem'}
    outlines = [r for r in events if any(r['statement_id'].startswith(s+' step ') for s in main_ids)]
    types = collections.Counter(r['type'] for _,r in selected)
    assert set(types) <= set(KINDS)
    counts = {'paper':'I','scope':'current_printed_statements_and_definitions',
              'statements':len(statements),'subject_identifiers':len(ids),
              'event_associations':len(selected),
              'declared_evidence_groups':len({r['evidence_group'] for _,r in selected}),
              'outline_step_associations_separate':len(outlines),
              **{kind:types[kind] for kind in KINDS}}
    assert sum(counts[k] for k in KINDS)==counts['event_associations']
    return {'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source':str(source),'source_sha256':digest(source),
            'ledger':str(ledger),'ledger_sha256':digest(ledger),
            'historic_tags':str(tag_source),'historic_tags_sha256':digest(tag_source),
            'merged_ledger_rows':len(events),'counts':counts,
            'statements':statements,
            'selected_ledger_rows':[n for n,_ in selected],
            'selected_event_ids':[r['event_id'] for _,r in selected],
            'declared_evidence_groups':sorted({r['evidence_group'] for _,r in selected}),
            'mathematical_events_added':0,
            'scope':'Fresh records recount from current TeX, historical identity registry and canonical CHECK_EVENTS. Existing group/type/outcome semantics are retained; a numerical count supplies no new proof verification.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--base',type=Path)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    root=args.root.resolve();base=args.base or root.parent/'S6_SERIES_PUBLISH_work'
    result=recount(root,base)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('source_sha256','ledger_sha256','merged_ledger_rows','counts','mathematical_events_added')},indent=2))

if __name__=='__main__':main()
