#!/usr/bin/env python3
"""Current Paper II structure and reference inventory; creates no check credit.

Only Paper II is opened. References are candidate dependencies, to be read in
context before any reordering; a cross-reference can compare results rather
than supply an input. This program does not certify mathematical dependence.
"""
from pathlib import Path
import bisect, collections, csv, datetime as dt, hashlib, importlib.util, json, re

R = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ii_packets', R / 'code/S6_SERIES_PUBLISH_II_packets.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def sha(s):
    return hashlib.sha256(s.encode() if isinstance(s, str) else s).hexdigest()

def refs(s):
    values = set(mod.refs(s))
    for pattern in [r'\\SeriesRef\{([^}]+)\}', r'\\CompendiumRef\{[^}]+\}\{([^}]+)\}', r'\\hyperref\[([^]]+)\]']:
        values.update(re.findall(pattern, mod.mask_comments(s)))
    return sorted(values)

def scc(graph):
    count = 0
    stack, indices, low, on, result = [], {}, {}, set(), []
    def visit(v):
        nonlocal count
        indices[v] = low[v] = count
        count += 1
        stack.append(v)
        on.add(v)
        for w in graph[v]:
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            group = []
            while True:
                w = stack.pop()
                on.remove(w)
                group.append(w)
                if w == v:
                    break
            result.append(group)
    for v in graph:
        if v not in indices:
            visit(v)
    return result

src = mod.parse_source(R / 'S6_SERIES_PUBLISH_II.tex', 'II')
s = src['text']
rows = src['statements']
sections = [h for h in src['headings'] if h['level'] == 'section']
starts = [h['start'] for h in sections]
for i, h in enumerate(sections):
    h['id'] = i + 1
    h['end'] = sections[i + 1]['start'] if i + 1 < len(sections) else len(s)
    h['chars'] = h['end'] - h['start']
    h['lines'] = s[h['start']:h['end']].count('\n')
    h['statements'] = []

alllabels = {}
owner_by_index = {}
for i, row in enumerate(rows):
    owner = row['owner']
    owner_by_index[owner] = i
    row['all_end'] = max([row['end']] + [p['end'] for p in row['proofs']])
    row['section_id'] = bisect.bisect_right(starts, row['start'])
    sections[row['section_id'] - 1]['statements'].append(owner)
    block = s[row['start']:row['all_end']]
    row['all_labels'] = mod.LABEL.findall(mod.mask_comments(block))
    row['all_tags'] = re.findall(r'\\hypertarget\{tag-([^}]+)\}', mod.mask_comments(block))
    row['all_refs'] = refs(block)
    row['all_cites'] = mod.cites(block)
    row['block_sha256'] = sha(block)
    row['production_headers'] = block.count('\\StatementRecord{')
    row['explicit_equation_tags'] = re.findall(r'\\tag\*?\{([^}]+)\}', mod.mask_comments(block))
    for label in row['all_labels'] + row['record_ids']:
        alllabels[label] = owner

graph = {row['owner']: set() for row in rows}
forward = []
external = collections.Counter()
for row in rows:
    row['reference_targets'] = {}
    for label in row['all_refs']:
        target = alllabels.get(label)
        row['reference_targets'][label] = target
        if target is None:
            external[label] += 1
        elif target != row['owner']:
            graph[row['owner']].add(target)
            if owner_by_index[target] > owner_by_index[row['owner']]:
                forward.append(dict(owner=row['owner'], label=label, target=target, section_from=row['section_id'], section_to=rows[owner_by_index[target]]['section_id']))

groups = sorted((g for g in scc(graph) if len(g) > 1), key=len, reverse=True)
section_edges = collections.Counter()
for owner, targets in graph.items():
    a = rows[owner_by_index[owner]]['section_id']
    for target in targets:
        b = rows[owner_by_index[target]]['section_id']
        if a != b:
            section_edges[(a, b)] += 1

outdir = R / 'records/S6_SERIES_PUBLISH_II_structure_current'
outdir.mkdir(exist_ok=True)
metadata = {k: v for k, v in src.items() if k in ['paper', 'path', 'sha256', 'headings']}
metadata.update(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(), sections=sections, statements=rows,
    reference_cycles=groups, forward_reference_candidates=forward,
    cross_section_reference_counts=[dict(source=a, target=b, count=n) for (a,b),n in sorted(section_edges.items())],
    unresolved_or_cross_paper_references=dict(external),
    mathematical_dependency_certification=False, source_changes=0, check_events_added=0, publication_page_reading_credit=0,
    limitations='Only reference locations are inventoried. Dependencies, duplicates, editorial decisions and all mathematical assertions require contextual reading; this file creates no proof or page-review credit.')
(outdir / 'metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
with (outdir / 'statements.tsv').open('w') as f:
    fields = ['owner', 'environment', 'title', 'section_id', 'start_line', 'end_line', 'proof_lines', 'proof_chars', 'production_headers', 'all_tags', 'all_refs', 'all_cites']
    w = csv.DictWriter(f, fields, delimiter='\t')
    w.writeheader()
    for row in rows:
        w.writerow({k: ';'.join(row[k]) if isinstance(row[k],list) else row[k] for k in fields})
summary = dict(created_utc=metadata['created_utc'], source_sha256=src['sha256'], statements=len(rows), proof_environments=len(src['proofs']), sections=len(sections), production_headers=sum(r['production_headers'] for r in rows), explicit_equation_tags=sum(len(r['explicit_equation_tags']) for r in rows), forward_reference_candidates=len(forward), cross_section_forward_candidates=sum(x['section_from'] != x['section_to'] for x in forward), reference_cycles=groups, metadata_sha256=sha((outdir / 'metadata.json').read_bytes()), check_events_added=0, page_reading_credit=0)
(outdir / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k:v for k,v in summary.items() if k != 'reference_cycles'},indent=2))
print('Reference cycle sizes:', [len(g) for g in groups])
