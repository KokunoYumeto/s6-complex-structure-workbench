#!/usr/bin/env python3
"""Paper I reference-scope audit; reads existing counts without refreshing them.

This records references in each statement and immediate proof, plus each main
theorem's own outline. Hidden StatementRecord data and Further results are
excluded. Reference reachability is reported for subsequent premise review.
No mathematical check event is created by this metadata scan.
"""
from pathlib import Path
from collections import defaultdict, deque
import csv
import hashlib
import importlib.util
import json
import re

BASE = Path('/workspace/scratch/653608133b22')
OUT = BASE / 'work/agents/i_provenance'
SOURCE = BASE / 'work/S6_SERIES_PUBLISH_I.tex'
COUNTS = BASE / 'work/records/S6_SERIES_PUBLISH_statement_check_counts.csv'
LEDGER = BASE / 'work/records/CHECK_EVENTS.tsv'
HELPER = BASE / 'work/agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py'
OUT.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('s6_records', HELPER)
records = importlib.util.module_from_spec(spec)
spec.loader.exec_module(records)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def environment_end(text, start, name):
    tokens = re.compile(r'\\(begin|end)\{' + re.escape(name) + r'\}')
    depth = 0
    for m in tokens.finditer(text, start):
        depth += 1 if m[1] == 'begin' else -1
        if not depth:
            return m.end()
    raise ValueError('Unclosed environment: ' + name)

def refs(region, positions):
    region = records.without_hidden_record(region)
    # Old Uses/UsedBy lines are production metadata as well, even where the
    # unrevised macro currently prints them. Their historical references are
    # not a substitute for references in the actual statement/proof.
    for command in ['Uses', 'UsedBy']:
        while True:
            m = re.search(r'\\' + command + r'\s*\{', region)
            if not m:
                break
            j = m.end(); depth = 1
            while depth:
                if region[j] == '{' and region[j-1] != '\\': depth += 1
                if region[j] == '}' and region[j-1] != '\\': depth -= 1
                j += 1
            region = region[:m.start()] + region[j:]
    result = records.explicit_refs(region, positions)
    result.update(re.findall(r'\\hyperref\[([^\]]+)\]', region))
    return result

data = SOURCE.read_bytes()
source_sha = hashlib.sha256(data).hexdigest()
snapshot = OUT / ('S6_SERIES_PUBLISH_I_source_snapshot_' + source_sha[:12] + '.tex')
if snapshot.exists():
    assert snapshot.read_bytes() == data
else:
    snapshot.write_bytes(data)
text = data.decode('utf-8')
start = text.index(r'\begin{document}')
end = text.find(r'\begin{thebibliography}', start)
if end < 0:
    end = len(text)
# Replace comments by spaces so offsets/line locators remain exact.
body = re.sub(r'(?<!\\)%[^\n]*', lambda m: ' ' * len(m[0]), text[start:end])
positions = {m[1]: m.start() for m in re.finditer(r'\\label\{([^}]+)\}', body)}
statements = []
# Paper I still uses the theorem-like 'cited' environment for eleven known
# inputs. It includes all eight mandatory below-bar results and must therefore
# participate in premise reachability. TikZ 'scope' is not a theorem environment.
statement_env = re.compile(r'\\begin\{(maintheorem|theorem|lemma|proposition|corollary|definition|remark|cited)\}')
statement_matches = list(statement_env.finditer(body))
for index, m in enumerate(statement_matches):
    end_statement = environment_end(body, m.start(), m[1])
    statement = body[m.start():end_statement]
    primary = re.search(r'\\StatementRecord\{([^}]+)\}', statement)
    labels = re.findall(r'\\label\{([^}]+)\}', statement)
    sid = primary[1] if primary else (labels[0] if labels else '')
    tag = re.search(r'\\hypertarget\{tag-([^}]+)\}', statement)
    stop = end_statement
    next_statement = statement_matches[index+1].start() if index+1 < len(statement_matches) else len(body)
    gap = body[stop:next_statement]
    heading = re.search(r'\\(?:section|subsection|subsubsection|part)\*?\{', gap)
    if heading:
        gap = gap[:heading.start()]
    proof = re.search(r'\\begin\{proof\}', gap)
    preproof_interlude = ''
    if proof:
        preproof_interlude = gap[:proof.start()].strip()
        proof_start = stop + proof.start()
        stop = environment_end(body, proof_start, 'proof')
    region = body[m.start():stop]
    statements.append({
        'statement_id': sid,
        'kind': m[1],
        'tag': tag[1] if tag else '',
        'labels': labels,
        'owned_labels': re.findall(r'\\label\{([^}]+)\}', region),
        'refs': sorted(refs(region, positions)),
        'statement_line': text.count('\n', 0, start + m.start()) + 1,
        'region_end_line': text.count('\n', 0, start + stop) + 1,
        'immediate_proof': bool(proof),
        'preproof_interlude': preproof_interlude,
        'own_outline_refs': []
    })
by_id = {s['statement_id']: s for s in statements if s['statement_id']}
owners = {label: s['statement_id'] for s in statements for label in s['owned_labels']}
mains = [s['statement_id'] for s in statements if s['kind'] == 'maintheorem']
outlines = []
for m in re.finditer(r'\\hypertarget\{outline-I-([A-Z])\}\{\}', body):
    sid = 'series:I:' + m[1]
    e = body.index(r'\begin{enumerate}', m.end())
    stop = environment_end(body, e, 'enumerate')
    region = body[e:stop]
    found = sorted(refs(region, positions))
    by_id[sid]['own_outline_refs'] = found
    by_id[sid]['refs'] = sorted(set(by_id[sid]['refs']) | set(found))
    steps = list(re.finditer(r'\\item\\hypertarget\{step-I-([A-Z])-([0-9]+)\}\{\}', region))
    for k, step in enumerate(steps):
        step_stop = steps[k + 1].start() if k + 1 < len(steps) else len(region)
        part = region[step.start():step_stop]
        step_refs = sorted(refs(part, positions))
        outlines.append({'main': sid, 'step': int(step[2]), 'line': text.count('\n', 0, start + e + step.start()) + 1, 'refs': step_refs, 'owners': sorted({owners.get(r, r) for r in step_refs})})

graph = {sid: sorted({owners.get(r, r) for r in s['refs']} - {sid}) for sid, s in by_id.items()}
paths = {}
main_reached = {}
for main in mains:
    seen = {main: [main]}
    q = deque([main])
    while q:
        node = q.popleft()
        for target in graph.get(node, []):
            if target in by_id and target not in seen:
                seen[target] = seen[node] + [target]
                q.append(target)
    main_reached[main] = sorted(seen)
    for target, path in seen.items():
        paths.setdefault(target, {})[main] = path
reachable = set(paths)
with COUNTS.open(newline='') as stream:
    count_rows = [r for r in csv.DictReader(stream) if r['paper'] == 'I']
required = []
outside = []
for row in count_rows:
    sid = row['label']
    owner = owners.get(sid, sid)
    result = dict(row)
    result.update(current_statement_owner=owner, precise_main_closure=str(owner in reachable).lower(),
                  reached_from=';'.join(sorted(paths.get(owner, {}))),
                  paths=json.dumps(paths.get(owner, {}), sort_keys=True),
                  source_line=str(by_id.get(owner, {}).get('statement_line', '')))
    if row['below_bar'] == 'yes' or row['below_bar'] == 'two_only' and owner in reachable:
        required.append(result)
    elif row['below_bar'] == 'two_only':
        outside.append(result)

def save_csv(name, rows):
    path = OUT / name
    fields = list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)

save_csv('S6_SERIES_PUBLISH_I_required_check_targets.csv', required)
save_csv('S6_SERIES_PUBLISH_I_two_only_outside_main_closure.csv', outside)
unowned = []
for sid in sorted(reachable):
    for target in graph.get(sid, []):
        if target not in by_id:
            unowned.append({'from': sid, 'to': target, 'label_in_body': target in positions})
result = {
    'paper': 'I', 'source': str(SOURCE), 'source_sha256': source_sha, 'source_snapshot': str(snapshot),
    'ledger': str(LEDGER), 'ledger_sha256': sha(LEDGER), 'existing_counts': str(COUNTS), 'existing_counts_sha256': sha(COUNTS),
    'counts_recomputed': False, 'mathematical_events_added': 0,
    'method': 'Actual statement and immediate proof regions, with each main theorem\'s own numbered outline attached only to that theorem. Hidden StatementRecord arguments, comments, later Further results lists and all other unrelated interstatement prose excluded. All explicit equation/statement aliases map to the region which owns their label. References establish candidates; mathematical premise status still requires contextual review.',
    'printed_environments': len(statements), 'primary_subjects': len(by_id), 'main_ids': mains,
    'main_closure_environments': len(reachable),
    'below_bar_targets': [r['label'] for r in required if r['below_bar'] == 'yes'],
    'two_only_main_closure_targets': [r['label'] for r in required if r['below_bar'] == 'two_only'],
    'two_only_outside_main_closure': [r['label'] for r in outside],
    'unowned_reference_targets_in_main_closure': unowned,
    'outlines': outlines, 'main_reachability': main_reached,
    'statements': statements, 'reference_graph': graph,
    'required_target_rows': required
}
(OUT / 'S6_SERIES_PUBLISH_I_dependency_scope_snapshot.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
lines = ['# Paper I: initial main-dependency check targets', '',
         'This metadata audit reads the existing merged counts and creates no mathematical check events. It excludes hidden statement records and unrelated Further results; every main theorem receives only its own outline.', '',
         'Source SHA256: `' + source_sha + '`.', '',
         f"Main reference closure: {len(reachable)} of {len(statements)} environments.", '',
         '## Required target candidates', '',
         '| ID | Gate | Existing substantive groups | Main theorem(s) | Source line |',
         '|---|---|---:|---|---:|']
for row in required:
    lines.append('| `' + row['label'] + '` | ' + row['below_bar'] + ' | ' + row['substantive_evidence_groups'] + ' | ' + row['reached_from'].replace('series:I:', '') + ' | ' + row['source_line'] + ' |')
lines += ['', 'Shortest explicit-reference paths are recorded for every target in the CSV and JSON. Each path still requires contextual premise review; generic reachability alone does not establish a mathematical dependence.', '',
          '## Two-only targets outside the main reference closure', '', ', '.join('`' + r['label'] + '`' for r in outside), '']
(OUT / 'S6_SERIES_PUBLISH_I_initial_dependency_targets.md').write_text('\n'.join(lines))
print(json.dumps({k: result[k] for k in ['source_sha256', 'printed_environments', 'main_closure_environments', 'below_bar_targets', 'two_only_main_closure_targets', 'two_only_outside_main_closure']}, indent=2))
