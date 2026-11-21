#!/usr/bin/env python3
"""Merge preserved check rows, verify shipped cp10 bytes, and recount declared scopes.

This is a records audit, not a mathematical proof check. All input CHECK_EVENTS
rows keep their original statement_id, who, type, outcome and evidence_group.
Missing metadata is added reproducibly; original source columns are retained.
The [recorded on: ...] prose is never expanded into duplicate associations.
"""
import argparse
import collections
import csv
import hashlib
import json
import re
import statistics
from pathlib import Path

csv.field_size_limit(10**9)
SUBSTANTIVE = {'targeted proof check', 'independent re-proof',
               'computation or formal certificate'}
ENV = re.compile(r'\\begin\{(maintheorem|theorem|lemma|proposition|corollary|definition|remark)\}')
REF = re.compile(r'\\(?:SeriesRef|cref|Cref|ref|eqref)\*?\{([^}]+)\}')
RANGE_REF = re.compile(r'\\(?:crefrange|Crefrange)\*?\{([^}]+)\}\{([^}]+)\}')

def read_rows(path, delim='\t'):
    with path.open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream, delimiter=delim))

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False,
                                    sort_keys=True).encode()).hexdigest()

def save_rows(path, rows, fields=None, delim='\t'):
    if fields is None:
        fields = list(dict.fromkeys(k for row in rows for k in row))
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter=delim,
                                extrasaction='raise')
        writer.writeheader()
        writer.writerows(rows)

def core(row):
    return tuple(row.get(k, '') for k in ['statement_id', 'date', 'who', 'type', 'outcome'])

def merge(source, extra_paths):
    paths = [source / 'CHECK_EVENTS.tsv',
             source / 'INTAKE_S6_SERIES_GRIND_cp10_20261120_CHECK_EVENTS.tsv',
             source / 'REVIEW_V_A_E_ad85dcfa_20261120_CHECK_EVENTS.tsv'] + extra_paths
    merged, seen_core, seen_ids, rejected = [], {}, {}, []
    for path in paths:
        for n, old in enumerate(read_rows(path), 2):
            row = dict(old)
            row['date'] = row.get('date') or row.get('date_utc', '')
            row.setdefault('source_file', path.name)
            row.setdefault('source_row', str(n))
            row.setdefault('phase', 'post-cp10' if path.name != 'CHECK_EVENTS.tsv' else 'retained')
            row.setdefault('source_event_type', row['type'])
            row.setdefault('event_id', 'publish-received:' + digest(core(row))[:24])
            # An evidence group describes the common dated who/type/outcome/where.
            # Several statement associations can refer to one such group.
            row.setdefault('evidence_group', 'publish-evidence:' + digest([
                row['date'], row['who'], row['type'], row['outcome'], row.get('where', '')
            ])[:24])
            row['publish_input_file'] = path.name
            row['publish_input_row'] = str(n)
            c = core(row)
            if row['event_id'] in seen_ids and seen_ids[row['event_id']] != c:
                raise ValueError('Conflicting event_id: ' + row['event_id'])
            if c in seen_core:
                rejected.append({'input_file': path.name, 'input_row': str(n),
                                 'retained_event_id': seen_core[c],
                                 'reason': 'exact same statement/date/who/type/outcome'})
                continue
            seen_core[c] = row['event_id']
            seen_ids[row['event_id']] = c
            merged.append(row)
    return merged, rejected

def checker(row):
    # Preserve the retained underchecked report's documented grouping algorithm.
    # It is a checker-label count, not a number of independent model families.
    w = re.sub(r'\s*\(.*?\)', '', row['who'])
    return w.split(',')[0].strip() + ' | ' + (w.split(',')[-1].strip() if ',' in w else '')

def statements(path):
    text = path.read_text(encoding='utf-8')
    start = text.index(r'\begin{document}')
    body = text[start:]
    all_label_positions = {m.group(1): m.start()
                           for m in re.finditer(r'\\label\{([^}]+)\}', body)}
    # The end-of-paper program table is reference metadata, not a mathematical
    # premise of the final theorem. Keep its backward citations outside regions.
    program_table_start = body.find(r'\section*{Programs}')
    matches = list(ENV.finditer(body))
    out = []
    for i, m in enumerate(matches):
        end_token = '\\end{' + m.group(1) + '}'
        e = body.index(end_token, m.end()) + len(end_token)
        stop = matches[i+1].start() if i+1 < len(matches) else body.find(r'\begin{thebibliography}', e)
        if stop < 0:
            stop = len(body)
        if program_table_start >= e:
            stop = min(stop, program_table_start)
        block = body[m.start():e]
        primary = re.search(r'\\StatementRecord\{([^}]+)\}', block)
        labels = re.findall(r'\\label\{([^}]+)\}', block)
        sid = primary.group(1) if primary else (labels[0] if labels else '')
        tag = re.search(r'\\hypertarget\{tag-([^}]+)\}', block)
        # References in a theorem/proof region are a machine-readable superset:
        # a human must decide whether each cited label is a used premise.
        region = body[m.start():stop]
        refs = {x.strip() for group in REF.findall(region)
                for x in group.split(',') if x.strip()}
        for left, right in RANGE_REF.findall(region):
            refs.update((left, right))
            if left in all_label_positions and right in all_label_positions:
                lo, hi = sorted((all_label_positions[left], all_label_positions[right]))
                refs.update(label for label, position in all_label_positions.items()
                            if lo <= position <= hi)
        refs = sorted(refs)
        owned_labels = re.findall(r'\\label\{([^}]+)\}', region)
        out.append({'statement_id': sid, 'kind': m.group(1),
                    'tag': tag.group(1) if tag else '', 'labels': labels,
                    'owned_labels': owned_labels,
                    'refs': refs, 'line': str(text.count('\n', 0, start+m.start())+1)})
    return out

def verify_files(source):
    rows = []
    for old in read_rows(source / 'S6_SERIES_GRIND_filelist.tsv'):
        relative = Path(old['path'])
        candidates = [source / relative, source / 'S6_PUBLISH_programs' / relative]
        found = next((p for p in candidates if p.is_file()), None)
        row = dict(old)
        if found is None:
            row.update(status='not shipped at recorded path', shipped_path='',
                       actual_size='', actual_sha256='')
        else:
            size = found.stat().st_size
            sha = hashlib.sha256(found.read_bytes()).hexdigest()
            row.update(status='verified' if size == int(old['size']) and sha == old['sha256'] else 'MISMATCH',
                       shipped_path=str(found.relative_to(source)),
                       actual_size=str(size), actual_sha256=sha)
        rows.append(row)
    return rows

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--tex-dir', type=Path)
    parser.add_argument('--extra-events', type=Path, action='append', default=[])
    args = parser.parse_args()
    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    events, duplicates = merge(args.source, args.extra_events)
    save_rows(out / 'CHECK_EVENTS.tsv', events)
    save_rows(out / 'S6_SERIES_PUBLISH_duplicate_events.tsv', duplicates,
              ['input_file', 'input_row', 'retained_event_id', 'reason'])
    files = verify_files(args.source)
    save_rows(out / 'S6_SERIES_PUBLISH_input_verification.tsv', files)
    tags = read_rows(args.source / 'S6_SERIES_GRIND_tags.tsv')
    inventory = {r['label']: r for r in read_rows(args.source / 'S6_SERIES_GRIND_inventory.csv', ',')}
    tag_by_label = {r['label']: r for r in tags}
    alias = {r['label']: r['label'] for r in tags}
    alias.update({'tag:' + r['tag']: r['label'] for r in tags})
    # The step association is distinct from the entire theorem association.
    # Count it in the paper's record totals, never in the theorem's whole-result count.
    by_id = collections.defaultdict(list)
    for r in events:
        by_id[alias.get(r['statement_id'], r['statement_id'])].append(r)
    all_stats, result_rows, printed_rows, graph_rows, pending_rows = [], [], [], [], []
    current_alias_rows = []
    for paper in ['I', 'II', 'III', 'IV', 'V']:
        path = args.tex_dir / f'S6_SERIES_PUBLISH_{paper}.tex' if args.tex_dir else None
        if path is None or not path.exists():
            path = args.source / ('S6_series_V_corrected_20261120.tex' if paper == 'V' else f'S6_SERIES_GRIND_{paper}.tex')
        sts = statements(path)
        active = {r['statement_id'] for r in sts if r['statement_id']}
        printed_rows.extend({'paper':paper, 'source':str(path), **r,
                             'labels': ';'.join(r['labels']), 'owned_labels': ';'.join(r['owned_labels']),
                             'refs': ';'.join(r['refs'])} for r in sts)
        main_ids = {r['statement_id'] for r in sts if r['kind'] == 'maintheorem'}
        owners = {label:r['statement_id'] for r in sts for label in r['owned_labels']}
        # A consolidated result can keep several historic statement labels.
        # Include those explicitly present labels in its current record scope;
        # do not expand or replicate any event association. Equation labels are
        # excluded here, even though their reference edges have an owner below.
        active_subjects = active | {label for label in owners
            if label in tag_by_label and tag_by_label[label]['kind']=='statement'}
        current_alias_rows.extend({'paper':paper,'current_statement_id':owners.get(label,label),
            'retained_statement_identifier':label,
            'scope':'explicit label retained in current source; event association is not duplicated'}
            for label in sorted(active_subjects))
        graph = {r['statement_id']: {owners.get(x,x) for x in r['refs']} for r in sts if r['statement_id']}
        reachable = set(main_ids)
        stack = list(main_ids)
        while stack:
            sid = stack.pop()
            for target in graph.get(sid, ()):
                if target in active and target not in reachable:
                    reachable.add(target); stack.append(target)
        for sid, refs in graph.items():
            for target in sorted(refs):
                graph_rows.append({'paper':paper,'from':sid,'to':target,
                                   'within_current_paper':str(target in active).lower(),
                                   'interpretation':'reference edge; premise status requires review'})
        scopes = {'cp10_printed_statements':{t['label'] for t in tags if t['paper']==paper and t['kind']=='statement'},
                  'cp10_all_tagged_targets':{t['label'] for t in tags if t['paper']==paper},
                  'current_primary_statement_identifiers':active,
                  'current_printed_statements_and_definitions':active_subjects}
        for scope, ids in scopes.items():
            selected = [r for r in events if alias.get(r['statement_id'],r['statement_id']) in ids]
            if scope.startswith('current_'):
                # Outline step rows describe that paper, and are retained in a
                # separate reported count below, rather than hidden in the total.
                steps = [r for r in events if any(r['statement_id'].startswith(sid+' step ') for sid in main_ids)]
            else:
                steps = []
            counts = collections.Counter(r['type'] for r in selected)
            all_stats.append({'paper':paper,'scope':scope,
                              'statements':len(active) if scope.startswith('current_') else len(ids),
                              'subject_identifiers':len(ids),
                              'event_associations':len(selected),
                              'declared_evidence_groups':len({r['evidence_group'] for r in selected}),
                              'outline_step_associations_separate':len(steps),
                              **{k:counts[k] for k in ['targeted proof check','independent re-proof',
                                  'computation or formal certificate','used and rechecked in this run',
                                  'carried as background without fault found',"refuted, with the refined statement's id"]}})
        for t in (t for t in tags if t['paper']==paper and t['kind']=='statement'):
            es = by_id[t['label']]
            sub = [r for r in es if r['type'] in SUBSTANTIVE]
            groups = {r['evidence_group'] for r in sub}
            checkers = {checker(r) for r in sub}
            row = {'tag':t['tag'],'paper':paper,'number_cp10':t['number'],
                   'page_cp10':t['page'],'label':t['label'],'status':t['status'],
                   'active_current_statement':str(t['label'] in active_subjects).lower(),
                   'current_statement_owner':owners.get(t['label'],t['label']),
                   'main_dependency_reference_closure':str(owners.get(t['label'],t['label']) in reachable).lower(),
                   'main_or_supporting':inventory.get(t['label'],{}).get('main_or_supporting',''),
                   'substantive_associations':len(sub),'substantive_evidence_groups':len(groups),
                   'distinct_checker_labels':len(checkers),'all_associations':len(es),
                   'below_bar':'yes' if len(groups)<2 or len(checkers)<2 else ('two_only' if len(groups)<3 else 'no'),
                   'checker_labels':' || '.join(sorted(checkers))}
            result_rows.append(row)
            if row['below_bar']=='yes' or row['below_bar']=='two_only' and owners.get(t['label'],t['label']) in reachable:
                pending_rows.append(row)
    save_rows(out / 'S6_SERIES_PUBLISH_check_counts.tsv', all_stats)
    save_rows(out / 'S6_SERIES_PUBLISH_statement_check_counts.csv', result_rows, delim=',')
    save_rows(out / 'S6_SERIES_PUBLISH_required_check_candidates.csv', pending_rows, delim=',')
    save_rows(out / 'S6_SERIES_PUBLISH_printed_statements.tsv', printed_rows)
    save_rows(out / 'S6_SERIES_PUBLISH_reference_graph.tsv', graph_rows)
    save_rows(out / 'S6_SERIES_PUBLISH_current_statement_aliases.tsv', current_alias_rows)
    summary = {'input_rows':len(events)+len(duplicates),
               'attached_baseline_rows':sum(len(read_rows(args.source/name)) for name in
                    ['CHECK_EVENTS.tsv','INTAKE_S6_SERIES_GRIND_cp10_20261120_CHECK_EVENTS.tsv',
                     'REVIEW_V_A_E_ad85dcfa_20261120_CHECK_EVENTS.tsv']),
               'merged_rows':len(events),'exact_duplicates_removed':len(duplicates),
               'all_event_types':dict(collections.Counter(r['type'] for r in events)),
               'file_verification':dict(collections.Counter(r['status'] for r in files)),
               'below_bar_cp10_statement_scope':dict(collections.Counter(r['below_bar'] for r in result_rows)),
               'scope_caveats':[
                   'Counts are statement-event associations, not counts of independent experiments or checked proofs.',
                   'Retained types describe original authors\' classifications; actual scope remains in each outcome.',
                   'A whole-result independent check is never inferred from a partial-step or numerical consistency row.',
                   'Checker-label counts preserve the supplied grouping rule; they do not measure independent model families.',
                   'Current-source counts include historic statement labels explicitly retained on consolidated results; no event is expanded or replicated.',
                   'Per-historic-statement gate counts retain their own recorded scopes; an event on a current owner is not automatically transferred to its other labels.',
                   'Current-reference dependency closure is a conservative candidate set requiring mathematical review.',
                   'Missing cp10 files are not corruption claims: the base ZIP intentionally omits run outputs and PDFs.']}
    (out / 'S6_SERIES_PUBLISH_records_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    for r in all_stats:
        if r['paper']=='V': print(json.dumps(r,ensure_ascii=False))

if __name__ == '__main__':
    main()
