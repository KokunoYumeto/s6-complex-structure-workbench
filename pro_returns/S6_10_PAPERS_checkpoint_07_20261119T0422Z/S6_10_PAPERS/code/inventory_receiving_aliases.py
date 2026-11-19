#!/usr/bin/env python3
"""Map literal co-located receiving statement labels, without proof transfer."""
import collections
import datetime
import hashlib
import json
import re
from pathlib import Path

W = Path(__file__).resolve().parents[1]
status = json.loads((W/'analysis/inventory_manuscript_status.json').read_text())
by_label = collections.defaultdict(list)
statements = []
file_hashes = {}
for paper, data in status['papers'].items():
    for relative in data['source_paths']:
        path = W / relative
        text = path.read_text()
        file_hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        if r'\StatementRecord{' not in text:
            continue
        declarations = list(re.finditer(r'\\label\s*\{([^}]+)\}', text))
        def spacing(value):
            return not re.sub(r'(?<!\\)%[^\n]*', '', value).strip()
        for match in re.finditer(r'\\StatementRecord\s*\{([^}]+)\}', text):
            canonical = match.group(1)
            # Receiving prose paragraphs and refuted/cited environments also
            # carry metadata.  Read only the immediately preceding literal
            # label cluster, rather than borrowing a source section container.
            prior = [x for x in declarations if x.end() <= match.start()]
            assert prior and spacing(text[prior[-1].end():match.start()]), (relative,canonical)
            cluster = [prior[-1]]
            for declaration in reversed(prior[:-1]):
                if not spacing(text[declaration.end():cluster[0].start()]):
                    break
                cluster.insert(0,declaration)
            aliases = [x.group(1) for x in cluster]
            assert canonical in aliases, (relative,canonical,aliases)
            start,end = cluster[0].start(),match.end()
            exact = text[start:end]
            entry = dict(paper=paper, canonical_label=canonical,
                         literal_header_labels=aliases, file=relative,
                         declaration_start=start,declaration_end=end,
                         declaration_sha256=hashlib.sha256(exact.encode()).hexdigest())
            statements.append(entry)
            for label in aliases:
                by_label[label].append(dict(paper=paper,canonical_label=canonical,file=relative,
                                           declaration_sha256=entry['declaration_sha256']))
result = dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              scope='The contiguous literal label cluster immediately before one StatementRecord identifies its receiving declaration. This includes named prose statements. Internal equation/proof labels are excluded. This is declaration identity only and creates no new proof reading or independent check.',
              statement_records=len(statements), source_hashes=file_hashes,
              statements=statements, by_label=by_label,
              conflicting_declarations={k:v for k,v in by_label.items() if len(v)>1},
              shared_header_statements=[x for x in statements if len(x['literal_header_labels'])>1])
(W/'analysis/inventory_receiving_statement_aliases.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(statement_records=len(statements), literal_labels=len(by_label),
                     shared_headers=len(result['shared_header_statements']),
                     conflicting_declarations=list(result['conflicting_declarations'])),indent=2))
