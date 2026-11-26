"""Regenerate Paper II publication records once its text is final.

prepare updates the methodology/deposit count prose from the admitted event
table. finish binds the final source and PDF numbering, then writes the
inventory, check entries, tags, counts and records paths. Other papers' rows
are retained. No old derived-file copy, diff or edit-level receipt is made.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import argparse
import csv
import hashlib
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'
csv.field_size_limit(100000000)
TYPES = ('targeted proof check', 'independent re-proof',
         'computation or formal certificate', 'used and rechecked in this run',
         'carried as background without fault found',
         "refuted, with the refined statement's id")
SUBSTANTIVE = set(TYPES[:3])
RECORDS_URL = 'https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/main/RECORDS.md#paper-ii'
COMMIT = 'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7'
# These historical statement aliases are explicitly retained in the current
# statement headers. The old tag table classifies two as remark/reference
# targets and omits some workbench aliases; none is an equation identifier.
EXTRA_STATEMENT_ALIASES = {
    'wbII:prop:criterion':'cdp:st:A.1.1',
    'wbII:prop:filtration':'cdp:st:A.1.1',
    'wbII:lem:conormal':'cdp:st:A.1.1',
    'wbII:lem:conormal-injective':'cdp:st:A.1.1',
    'wbII:prop:missing-global-section-criterion':'cdp:st:A.1.1',
    'wbII:prop:missing-cotangent-filtration':'cdp:st:A.1.1',
    'wbII:lem:conductor':'cdp:st:A.2.2',
    'wbII:lem:conductor-square':'cdp:st:A.2.2',
    'wbII:thm:nodal-test':'cdp:st:B1',
    'wbII:prop:family-geometry':'cdp:st:B1',
    'wbII:prop:nodal-counterexample':'cdp:st:B1',
    'wbII:rem:scope':'cdp:st:B1',
    'wbII:prop:conductor-differential':'wbII:prop:conductor',
    'wbII:thm:corrected-global':'wbII:thm:corrected-cdp-global',
    'wbII:cor:relative':'wbII:cor:corrected-cdp-relative',
    'scope:II:positive-ruled-configuration':'lem:II:positive-ruled-conductor-graph',
}

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def read_rows(path, delimiter='\t'):
    with Path(path).open() as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return reader.fieldnames, list(reader)

def write_rows(path, fields, rows, delimiter='\t'):
    with Path(path).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter,
                                lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

def braced(text, start):
    """Read one TeX brace group, retaining nested and escaped braces."""
    assert text[start] == '{', (start, text[start:start+30])
    level, pos = 1, start + 1
    while level:
        if text[pos] in '{}':
            slash = pos - 1
            while slash >= 0 and text[slash] == '\\':
                slash -= 1
            escaped = (pos - slash - 1) % 2
            if not escaped:
                level += 1 if text[pos] == '{' else -1
        pos += 1
    return text[start+1:pos-1], pos

def hidden_free(text):
    arities = {'StatementRecord':4, 'Uses':1, 'UsedBy':1}
    while match := re.search(r'\\(StatementRecord|Uses|UsedBy)\s*\{', text):
        end = match.end() - 1
        for _ in range(arities[match[1]]):
            while text[end].isspace():
                end += 1
            _, end = braced(text, end)
        text = text[:match.start()] + text[end:]
    return text

def references(text, positions):
    refs = {v.strip() for group in re.findall(
        r'\\(?:SeriesRef|[Cc]ref|[Ee]qref|ref)\*?\{([^}]+)\}', text)
        for v in group.split(',') if v.strip()}
    refs.update(re.findall(r'\\hyperref\[([^]]+)\]', text))
    for left, right in re.findall(r'\\[Cc]refrange\*?\{([^}]+)\}\{([^}]+)\}', text):
        refs.update((left, right))
        if left in positions and right in positions:
            lo, hi = sorted((positions[left], positions[right]))
            refs.update(k for k, p in positions.items() if lo <= p <= hi)
    return refs

def parse_statements(text):
    """Only statements and their immediate proofs own dependency edges."""
    start = text.index(r'\begin{document}')
    body = text[start:]
    positions = {m[1]:start+m.start() for m in re.finditer(r'\\label\{([^}]+)\}', body)}
    envnames = re.findall(r'\\newtheorem\{([^}]+)\}', text[:start])
    env = re.compile(r'\\begin\{(' + '|'.join(map(re.escape, envnames)) + r')\}')
    matches = list(env.finditer(body))
    result = []
    for i, match in enumerate(matches):
        end_token = r'\end{' + match[1] + '}'
        end = body.index(end_token, match.end()) + len(end_token)
        limit = matches[i+1].start() if i+1 < len(matches) else len(body)
        block = body[match.start():end]
        labels = re.findall(r'\\label\{([^}]+)\}', block)
        # The first header label belongs to the current printed owner.
        # Consolidated statements may list historical StatementRecord aliases
        # before the current owner's metadata (P360 and P4.58 do so).
        sid = labels[0] if labels else ''
        if not sid:
            raise ValueError(('Unlabelled numbered statement', match[1], start+match.start()))
        gap = body[end:limit]
        heading = re.search(r'\\(?:section|subsection|subsubsection|part)\*?\{', gap)
        if heading:
            gap = gap[:heading.start()]
        proof = re.search(r'\\begin\{proof\}', gap)
        stop = end
        if proof:
            proof_start, depth = end + proof.start(), 0
            for token in re.finditer(r'\\(begin|end)\{proof\}', body[proof_start:]):
                depth += 1 if token[1] == 'begin' else -1
                if depth == 0:
                    stop = proof_start + token.end()
                    break
            else:
                raise ValueError(('Unclosed immediate proof', sid))
        region = body[match.start():stop]
        tag = re.search(r'\\hypertarget\{tag-([^}]+)\}', block)
        title = re.match(r'\[([^\n]*?)\]', body[match.end():])
        result.append(dict(statement_id=sid, kind=match[1],
            tag=tag[1] if tag else '', title=title[1] if title else '',
            labels=labels, owned_labels=re.findall(r'\\label\{([^}]+)\}', region),
            refs=references(hidden_free(region), positions),
            start=start+match.start(), stop=start+stop,
            line=text.count('\n', 0, start+match.start())+1,
            status='proved' if match[1] not in ('problem','question','openq','conjecture') else 'open problem'))
    by_id = {r['statement_id']:r for r in result}
    assert len(by_id) == len(result)
    steps = defaultdict(list)
    for match in re.finditer(r'\\hypertarget\{outline-II-([A-Z])\}\{\}', body):
        sid = 'series:II:' + match[1]
        end = body.index(r'\end{enumerate}', match.end())
        by_id[sid]['refs'].update(references(body[match.end():end], positions))
        fragment = body[match.end():end]
        parts = list(re.finditer(r'\\hypertarget\{(step-II-[A-Z]-\d+)\}\{\}', fragment))
        for n, item in enumerate(parts):
            finish = parts[n+1].start() if n+1 < len(parts) else len(fragment)
            for label in references(fragment[item.end():finish], positions):
                steps[label].append(item[1])
    owners = {}
    for row in result:
        for label in row['owned_labels']:
            if label in owners and owners[label] != row['statement_id']:
                raise ValueError(('Multiple statement owners', label))
            owners[label] = row['statement_id']
    return result, owners, positions, steps

def current_data():
    text = SOURCE.read_text()
    statements, owners, positions, steps = parse_statements(text)
    _, events = read_rows(ROOT / 'CHECK_EVENTS.tsv')
    assert len({r['event_id'] for r in events}) == len(events)
    _, tags = read_rows(ROOT / 'S6_SERIES_PUBLISH_tags.tsv')
    historical = {r['label'] for r in tags if r['paper'] == 'II' and r['kind'] == 'statement'}
    active = {r['statement_id'] for r in statements}
    by_id = {r['statement_id']:r for r in statements}
    for alias, owner in EXTRA_STATEMENT_ALIASES.items():
        assert owners.get(alias)==owner and alias in by_id[owner]['labels'], (alias,owner)
    subjects = active | (historical & set(owners)) | set(EXTRA_STATEMENT_ALIASES)
    tag_aliases = {'tag:'+r['tag']:r['label'] for r in tags}
    for row in statements:
        key = 'tag:' + row['tag']
        assert key not in tag_aliases or tag_aliases[key] == row['statement_id'], ('Current primary tag mismatch', key)
        tag_aliases[key] = row['statement_id']
    selected = [r for r in events if tag_aliases.get(r['statement_id'],r['statement_id']) in subjects]
    # Preserve inherited administrative rows and their original types.
    # Only exact statement-event associations enter the six-type count prose.
    assert set(r['type'] for r in selected) <= set(TYPES)
    counts = Counter(r['type'] for r in selected)
    groups = {r.get('evidence_group') or r['event_id'] for r in selected}
    return dict(text=text, statements=statements, owners=owners, positions=positions,
                steps=steps, events=events, tags=tags, active=active, subjects=subjects,
                selected=selected, counts=counts, groups=groups, tag_aliases=tag_aliases)

def count_prose(data, tex=False):
    c = data['counts']
    return (f"The records associate {len(data['selected']):,} entries with statements of this paper:\n"
            f"{c[TYPES[0]]:,} examinations of proof steps, {c[TYPES[1]]:,} independent\n"
            f"re-derivations, {c[TYPES[2]]:,} computations or formal certificates,\n"
            f"{c[TYPES[3]]:,} readings of proofs and applications, {c[TYPES[4]]:,} uses of\n"
            f"background results without a fault found, and {c[TYPES[5]]:,} refutation\n"
            "records associated with their corrected statements.\n"
            f"These entries belong to {len(data['groups']):,} recorded groups; one argument or\n"
            "calculation can be associated with several statements and kinds of\n"
            "examination. The counts describe those recorded associations, and\n"
            "each outcome specifies its scope and prior proof exposure.")

def prepare():
    data = current_data()
    old = re.search(r'The records associate [\s\S]+?each outcome specifies its scope and prior proof exposure\.', data['text'])
    if not old:
        raise ValueError('Methodology count paragraph not found exactly.')
    # Imported only here: reading this program never modifies the manuscript.
    from S6_SERIES_PUBLISH_c4_edit import apply_edit
    new = count_prose(data, tex=True)
    if old[0] != new:
        apply_edit(old[0], new, 'II-C4-FINAL-COUNTS', ['D15'], 'methodology',
                   'Section 1.5, final admitted-event count paragraph',
                   'Recomputed from the authoritative final admitted CHECK_EVENTS table. Exact current primary statement identifiers and explicitly retained historical statement labels are counted once per event; no prepared unadmitted bundle is imported.',
                   review='Deterministic exact-subject/event-ID selection and evidence-group recomputation; no mathematical check or independent credit added.')
    text = SOURCE.read_text()
    date_old, date_new = r'\date{22 November 2026}', r'\date{23 November 2026}'
    if date_old in text:
        apply_edit(date_old, date_new, 'II-C4-FINAL-DATE', ['D24'], 'title-block',
                   'Paper II title date', 'Date the completed fourth-continuation text on 23 November 2026.',
                   review='Title date only; no mathematical text changed.')
    text = SOURCE.read_text()
    repo_urls = set(re.findall(r'https://github\.com/[^\s{}]+', text))
    assert repo_urls == {RECORDS_URL.replace('#',r'\#')}, repo_urls
    assert re.findall(r'(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])', text) == [COMMIT]
    assert text.count(r'\SsixRepositoryCommit') == 2

    draft = ROOT / 'agents/continuation3_provenance/S6_SERIES_PUBLISH_deposit_fields_II_proposed.json'
    deposit = json.loads(draft.read_text())
    # The controlling submitted-V metadata, read as a form only, supplies the
    # current field schema. No I/V manuscript is opened here.
    schema = json.loads((ROOT.parent/'HEXAGON_METADATA_V_public_v3.json').read_text())
    assert set(schema) <= set(deposit)
    deposit = {key:deposit[key] for key in schema}
    deposit['provenance'] = deposit['provenance'].replace('20–22 November 2026','20–23 November 2026')
    start = deposit['provenance'].index('How it was checked.')
    end = deposit['provenance'].index('Human understanding.',start)
    deposit['provenance'] = deposit['provenance'][:start] + (
        'How it was checked. ' + count_prose(data).replace('\n',' ') + ' '
        'The selection uses the exact current primary statement identifiers and the historical statement labels explicitly retained in the source. Each admitted event is counted once. '
        'The compact example with three doubled nodal supports supplies two conductor-scope refutations through one construction. It was developed after one participating model had read the affected proofs; its subsequent comparisons and computations add no independent re-derivation to these totals. '
        'The local curve-ring calculation and the reviews of its applications form a separate recorded group. Derivations completed before target-proof release and comparisons made after release retain their exact chronology. Computational comparisons record the previous and new methods and any unavailable historical program.\n\n'
    ) + deposit['provenance'][end:]
    opening = 'Text: AI-authored; none of it was written by a human. The submitter takes responsibility for the veracity of the text.'
    assert deposit['provenance'].startswith(opening)
    for key in ('comments','provenance'):
        assert set(re.findall(r'https://github\.com/[^\s]+',deposit[key])) <= {RECORDS_URL, RECORDS_URL+'.'}
    out = ROOT / 'S6_SERIES_PUBLISH_deposit_fields_II.json'
    old_deposit = out.read_text()
    new_deposit = json.dumps(deposit,ensure_ascii=False,indent=2)+'\n'
    out.write_text(new_deposit,newline='\n')
    from S6_SERIES_PUBLISH_c4_final_provenance import write_deposit_markdown
    write_deposit_markdown(deposit)
    # The existing defect table records this final draft update, without an
    # extra copy or per-edit manifest.
    from S6_SERIES_PUBLISH_c4_edit import append_rows
    append_rows(ROOT / 'S6_SERIES_PUBLISH_defects_II.tsv', [dict(
        change_id='II-C4-FINAL-DEPOSIT', type='D15', statement_id='Paper II deposit fields',
        old_location=out.name, old_page='not applicable', new_location=out.name,
        new_page='not applicable', old_text=old_deposit, new_text=new_deposit,
        reason='Admit the previously source-compared metadata, extend the documented publication dates through 23 November, and replace every check count with the final admitted-event recomputation. The prescribed responsibility opening and sole records-page URL are retained.',
        review_status='Root compared the complete prepared metadata with the prompt, current main results, source-reading records and exact final event selection. Final PDF metadata/first-page reading remains open.')], 'change_id')
    print('Final statement-associated events:',len(data['selected']))
    print('Final evidence groups:',len(data['groups']))
    print('Types:',json.dumps(dict(data['counts']),sort_keys=True))
    print('Methodology/date/deposit prose updated; final numbered records await the final PDF.')

def parse_aux(path):
    labels = {}
    for line in Path(path).read_text(errors='strict').splitlines():
        if not line.startswith(r'\newlabel{'):
            continue
        name,end = braced(line,len(r'\newlabel'))
        if name.endswith('@cref'):
            continue
        raw,end = braced(line,end)
        values,position = [],0
        while position < len(raw):
            while position < len(raw) and raw[position].isspace():
                position += 1
            if position >= len(raw):
                break
            value,position = braced(raw,position)
            values.append(value)
        if len(values)>=2:
            labels[name] = dict(number=values[0],page=values[1],
                                title=values[2] if len(values)>2 else '',
                                anchor=values[3] if len(values)>3 else '')
    return labels

def program_records(text):
    table = text[text.index(r'\section*{Programs}'):text.index(r'\begin{thebibliography}')]
    printed = re.findall(r'\\(?:path|nolinkurl)\{([^}]+)\}',table)
    assert printed, 'No printed program paths found'
    assert len(printed) == len(set(printed)), 'Duplicate printed program path'
    available = {}
    for path in sorted((ROOT/'agents/continuation3_provenance').glob('S6_SERIES_PUBLISH_records_II*.tsv')):
        _, rows = read_rows(path)
        for row in rows:
            old = available.get(row['printed_path'])
            assert old is None or old == row, ('Conflicting program identity',row['printed_path'])
            available[row['printed_path']] = row
    repository = (ROOT.parent/'REPOSITORY_PROGRAM_PATHS.txt').read_text().splitlines()
    listed = set(line.strip() for line in repository if line.strip())
    answer = []
    for name in printed:
        row = available.get(name)
        if row is None:
            raise ValueError(('Printed program missing from verified path records',name))
        path = row['repository_path']
        if path.startswith('code/'):
            local = ROOT/path
            if not local.is_file():
                raise ValueError(('Restore required identical code path',path))
            assert sha(local.read_bytes()) == row['sha256'],path
        else:
            assert path in listed or any(line.endswith(path) for line in listed),path
            assert re.fullmatch('[0-9a-f]{64}',row['sha256'])
        answer.append(row)
    return answer


def required_dispositions(data):
    """Read and preserve the admitted gate; raw count flags do not reopen it."""
    names = (
        'records/S6_SERIES_PUBLISH_required_check_completion_manifest.json',
        'records/S6_SERIES_PUBLISH_additional_required_checks_II.json',
        'records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json',
    )
    preserved = {name:(ROOT/name).read_bytes() for name in names}
    completed = json.loads(preserved[names[0]])['rows']
    additional = json.loads(preserved[names[1]])
    resolution = json.loads(preserved[names[2]])
    ii = {sid:row for sid,row in completed.items() if row['paper']=='II'}
    expected = additional['historical_II_required_count'] + len(additional['rows'])
    assert expected == len(ii) == 198
    assert all(row['status']=='done' for row in ii.values())
    assert set(ii) <= set(data['owners']), 'A required disposition lost its printed label.'
    historical = resolution['required_row'].removeprefix('check:')
    retained = resolution['printed_owner']
    assert (historical,retained)==('night:P3K.36','ii:LR:covering')
    assert data['owners'][historical] == historical
    assert data['owners'][retained] == retained and retained in ii
    return preserved, ii, resolution

def replace_ii_rows(existing, replacement):
    """Keep all other papers' values and relative order unchanged."""
    first = next((i for i,r in enumerate(existing) if r['paper']=='II'),len(existing))
    insertion = sum(r['paper']!='II' for r in existing[:first])
    others = [r for r in existing if r['paper']!='II']
    result = others[:insertion] + replacement + others[insertion:]
    assert [r for r in result if r['paper']!='II'] == others
    return result

def remaining_derived_records(data, statement_counts, completed, resolution):
    """Prepare existing auxiliary products in memory; never write on import."""
    printed_path = ROOT/'records/S6_SERIES_PUBLISH_printed_statements.tsv'
    printed_fields, old_printed = read_rows(printed_path)
    printed = [dict(paper='II',source=str(SOURCE),
        statement_id=r['statement_id'],kind=r['kind'],tag=r['tag'],
        labels=';'.join(r['labels']),owned_labels=';'.join(r['owned_labels']),
        refs=';'.join(sorted(r['refs'])),line=r['line'],
        reference_scope='Current statement, immediate proof and its own outline; hidden historical metadata excluded.')
        for r in data['statements']]
    printed = replace_ii_rows(old_printed,printed)
    candidate_path = ROOT/'records/S6_SERIES_PUBLISH_required_check_candidates.csv'
    candidate_fields, old_candidates = read_rows(candidate_path,',')
    candidates = [dict(r) for r in statement_counts if r['paper']=='II' and
        (r['below_bar']=='yes' or (r['below_bar']=='two_only' and
         r['main_dependency_reference_closure']=='true'))]
    candidates = replace_ii_rows(old_candidates,candidates)
    summary_path = ROOT/'records/S6_SERIES_PUBLISH_records_summary.json'
    summary = json.loads(summary_path.read_text())
    summary['merged_rows'] = len(data['events'])
    summary['input_rows'] = len(data['events']) + summary['exact_duplicates_removed']
    summary['all_event_types'] = dict(Counter(e['type'] for e in data['events']))
    summary['below_bar_cp10_statement_scope'] = dict(Counter(r['below_bar'] for r in statement_counts))
    summary['last_refresh_scope'] = 'Paper II only; other paper rows and sources held at their recorded state. Global ledger aggregates use the unchanged authoritative CHECK_EVENTS table.'
    summary['updated_utc'] = now()
    summary['paper_II_required_check_dispositions'] = dict(
        total=len(completed),resolved=len(completed),
        completion_record='records/S6_SERIES_PUBLISH_required_check_completion_manifest.json',
        historical_required_row=resolution['required_row'],
        retained_resolution_owner=resolution['printed_owner'],
        scope='Raw historical candidate flags do not replace or reopen admitted required-check dispositions. The historical compound fan assertion remains false as stated.')
    return ((printed_path,printed_fields,printed),
            (candidate_path,candidate_fields,candidates),
            (summary_path,summary))

def finish(pdf_path, aux_path):
    data = current_data()
    preserved_required, completed_required, required_resolution = required_dispositions(data)
    ledger_bytes = (ROOT/'CHECK_EVENTS.tsv').read_bytes()
    assert count_prose(data) in data['text'], 'Final event counts changed after preparation.'
    labels = parse_aux(aux_path)
    pdf_path = Path(pdf_path)
    source_hash, pdf_hash = sha(SOURCE.read_bytes()), sha(pdf_path.read_bytes())
    reading = (ROOT/'S6_SERIES_PUBLISH_reading_II.md').read_text()
    assert 'Final-candidate status: complete.' in reading, 'Actual final-page reading is still open.'
    assert source_hash in reading and pdf_hash in reading, 'Reading belongs to different source/PDF bytes.'
    final_heading = '## Fourth-continuation final page coverage\n'
    assert reading.count(final_heading) == 1, 'Final page-by-page evidence is missing or ambiguous.'
    coverage = reading.split(final_heading,1)[1]
    page_rows = re.findall(r'(?m)^\| (\d+) \| ([0-9a-f]{64}) \| (.+) \|$',coverage)
    import fitz
    with fitz.open(pdf_path) as pdf:
        page_count = len(pdf)
    assert [int(r[0]) for r in page_rows] == list(range(1,page_count+1)), 'Incomplete final image coverage.'
    image_folder = pdf_path.parent/'pages_120dpi'
    for page, image_hash, evidence in page_rows:
        assert sha((image_folder/f'page-{int(page):04d}.png').read_bytes()) == image_hash
        assert evidence.strip() and 'PENDING' not in evidence, ('Open final page',page)
    event_hash = sha((ROOT/'CHECK_EVENTS.tsv').read_bytes())
    rows = data['statements']
    by_id = {r['statement_id']:r for r in rows}
    for sid in by_id:
        assert sid in labels, ('Missing final auxiliary label',sid)
    graph = {r['statement_id']:{data['owners'].get(x,x) for x in r['refs']}
             - {r['statement_id']} for r in rows}
    reverse = defaultdict(set)
    for sid, targets in graph.items():
        for target in targets:
            reverse[target].add(sid)
    main = {r['statement_id'] for r in rows if r['kind']=='maintheorem'}
    reachable, todo = set(main), list(main)
    while todo:
        for target in graph[todo.pop()]:
            if target in by_id and target not in reachable:
                reachable.add(target)
                todo.append(target)
    events_by_subject = defaultdict(list)
    for event in data['events']:
        subject = data['tag_aliases'].get(event['statement_id'],event['statement_id'])
        events_by_subject[subject].append(event)
    owner_subjects = defaultdict(set)
    for subject in data['subjects']:
        owner_subjects[data['owners'].get(subject,subject)].add(subject)
    steps_by_owner = defaultdict(set)
    for target, steps in data['steps'].items():
        steps_by_owner[data['owners'].get(target,target)].update(steps)

    tag_fields, tags = read_rows(ROOT/'S6_SERIES_PUBLISH_tags.tsv')
    other_tags = [r.copy() for r in tags if r['paper']!='II']
    old_tag_ids = {r['tag'] for r in tags}
    current_tag_map = {}
    for row in tags:
        if row['paper']!='II':
            continue
        label = row['label']
        if label in labels:
            row['number'],row['page'] = labels[label]['number'],labels[label]['page']
            row['current_owner'] = data['owners'].get(label,label)
            binding = 'Retained permanent target; number/page from the final Paper II PDF.'
            prior = row.get('publication_disposition','')
            row['publication_disposition'] = prior if binding in prior else prior + (' ' if prior else '') + binding
        current_tag_map[label] = row['tag']
    for row in rows:
        if not row['tag']:
            raise ValueError(('Numbered owner has no permanent tag',row['statement_id']))
        if row['tag'] in old_tag_ids:
            continue
        sid = row['statement_id']
        tags.append(dict(tag=row['tag'],paper='II',number=labels[sid]['number'],
            page=labels[sid]['page'],label=sid,status=row['status'],kind='statement',
            current_owner=sid,publication_disposition='New receiving owner; inherited proof transfers and exact comparison scopes are recorded in the event table.'))
        current_tag_map[sid] = row['tag']
        old_tag_ids.add(row['tag'])
    assert [r for r in tags if r['paper']!='II']==other_tags

    inv_fields, inventory = read_rows(ROOT/'S6_SERIES_PUBLISH_inventory.csv',',')
    other_inventory = [r.copy() for r in inventory if r['paper']!='II']
    existing_ii = {r['label']:r for r in inventory if r['paper']=='II'}
    for row in rows:
        sid = row['statement_id']
        if sid not in existing_ii:
            entry = {k:'' for k in inv_fields}
            entry.update(paper='II',label=sid,tag=row['tag'],kind=row['kind'],status=row['status'],
                main_or_supporting='main' if sid in main else 'supporting',
                source_run='Publication receiving owner',source_id=sid,
                check_record='{}',notes='Current numbered owner; exact transferred arguments and comparison scopes are documented in its check entry.')
            inventory.append(entry)
            existing_ii[sid] = entry
    _, searches = read_rows(ROOT/'S6_SERIES_PUBLISH_c4_literature_searches.tsv')
    for entry in (r for r in inventory if r['paper']=='II'):
        sid = entry['label']
        printed_owner = data['owners'].get(sid,entry.get('current_statement_owner') or sid)
        owner = printed_owner
        direct = events_by_subject[sid]
        counts = Counter(e['type'] for e in direct)
        record = json.loads(entry['check_record']) if entry['check_record'].strip().startswith('{') else {'retained_source_record':entry['check_record']}
        record['canonical_check_events'] = [{k:e.get(k,'') for k in
            ('event_id','date','date_utc','who','type','phase','evidence_group','source_file','source_row','outcome')} for e in direct]
        record['current_ledger_sha256'] = event_hash
        record['current_event_scope'] = 'Exact original statement identifier; events on the current owner are linked separately and are not transferred as independent checks.'
        if sid == required_resolution['required_row'].removeprefix('check:'):
            assert entry['status']=='false as stated'
            owner = required_resolution['printed_owner']
            assert entry['current_statement_owner']==owner
            resolution_name = 'records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json'
            record['current_printed_anchor_owner'] = printed_owner
            record['required_check_resolution_owner'] = owner
            record['required_check_resolution_record'] = resolution_name
            record['required_check_resolution_sha256'] = sha(preserved_required[resolution_name])
            record['owner_field_scope'] = 'current_statement_owner preserves the admitted required-check disposition to the retained covering theorem; current_printed_anchor_owner identifies the reference remark. The uses, used_by and outline fields describe that printed anchor. No equality with the historical compound claim or transfer of proof events is asserted.'
        record['current_printed_owner_check_entry'] = 'S6_SERIES_PUBLISH_checks_II.md#tag-'+by_id[printed_owner]['tag'] if printed_owner in by_id else ''
        record['current_owner_check_entry'] = 'S6_SERIES_PUBLISH_checks_II.md#tag-'+by_id[owner]['tag'] if owner in by_id else ''
        record['current_event_outcomes_locator'] = record['current_printed_owner_check_entry']
        entry['check_record'] = json.dumps(record,ensure_ascii=False)
        entry['check_summary'] = f'{len(direct)} exact-subject event associations; '+ '; '.join(f'{kind}: {count}' for kind,count in sorted(counts.items()))
        entry['current_statement_owner'] = owner
        entry['current_source_sha256'], entry['current_pdf_sha256'] = source_hash,pdf_hash
        if sid in labels:
            entry['current_number'],entry['current_page'] = labels[sid]['number'],labels[sid]['page']
        if printed_owner in by_id:
            entry['uses'] = ';'.join(sorted(graph[printed_owner]))
            entry['used_by'] = ';'.join(sorted(reverse[printed_owner]))
            entry['outline_backlinks'] = ';'.join(sorted(steps_by_owner[printed_owner]))
            entry['placement_state'] = 'Final current mathematical owner and dependency order verified.'
            entry['writing_state'] = 'Publication text admitted; final rendered-page gate recorded in the reading log.'
            entry['publication_review_status'] = 'Required-check dispositions remain in the admitted records; exact current proof comparisons and page reading are recorded without upgrading independence.'
        if sid in main:
            letter = sid.rsplit(':',1)[-1]
            fresh = [r for r in searches if letter in r['main_theorems'].split('/')]
            previous = entry.get('literature_searches','')
            addition = json.dumps(fresh,ensure_ascii=False)
            if addition not in previous:
                entry['literature_searches'] = previous + ('\n' if previous else '') + addition
    assert [r for r in inventory if r['paper']!='II']==other_inventory

    tag_by_label = {r['label']:r for r in tags}
    def link(target):
        owner = data['owners'].get(target,target)
        if owner in by_id:
            return f"[II.{labels[owner]['number']}](#tag-{by_id[owner]['tag']})"
        known = tag_by_label.get(target)
        if known:
            return f"[{known['paper']}.{known['number']}](S6_SERIES_PUBLISH_checks_{known['paper']}.md#tag-{known['tag']})"
        return '`'+target+'`'
    document = ['# Paper II: statements, references and check events\n\n',
        f'Final source SHA-256: `{source_hash}`. Final PDF SHA-256: `{pdf_hash}`.\n\n',
        f'Admitted event-table SHA-256: `{event_hash}`. Numbers and pages come from the final auxiliary file.\n\n',
        'Each event keeps its original identifier, checker, type, outcome and evidence group. A reference or label transfer gives its exact mathematical owner; it does not create another event or independent proof. The reading log records the final page inspection separately.\n\n']
    for row in rows:
        sid = row['statement_id']
        owned = owner_subjects[sid] | {sid}
        event_rows = [e for e in data['events'] if data['tag_aliases'].get(e['statement_id'],e['statement_id']) in owned]
        anchors = {row['tag']}
        anchors.update(r['tag'] for r in tags if r['paper']=='II' and r['label'] in owned)
        for anchor in sorted(anchors):
            document.append(f'<a id="tag-{anchor}"></a>\n')
        document.append(f"## {row['kind'].capitalize()} II.{labels[sid]['number']}: {row['title']}\n\n")
        document.append(f"Label: `{sid}`. Permanent tag: `{row['tag']}`. Page {labels[sid]['page']}.\n\n")
        if sid == required_resolution['required_row'].removeprefix('check:'):
            retained = required_resolution['printed_owner']
            document.append('Historical disposition: the original compound universal fan assertion remains false as stated. This current numbered entry is the parameter-covering/fan-return reference remark. Its admitted required-check allocation resolves to '+link(retained)+' at the retained covering scope, as recorded in `records/S6_SERIES_PUBLISH_required_owner_resolution_02UH_20261122.json`. Events below retain their exact original subjects and are not transferred to that theorem.\n\n')
        document.append('Retained statement identifiers: '+', '.join('`'+v+'`' for v in sorted(owned))+'.\n\n')
        document.append('Uses: '+(', '.join(link(v) for v in sorted(graph[sid])) or 'No numbered mathematical input is cited.')+'\n\n')
        document.append('Used by: '+(', '.join(link(v) for v in sorted(reverse[sid])) or 'No current numbered owner cites this result.')+'\n\n')
        document.append('Outline steps: '+(', '.join('`'+v+'`' for v in sorted(steps_by_owner[sid])) or 'None.')+'\n\n')
        document.append('### Recorded checks\n\n')
        for event in event_rows:
            document.append(f"#### {event['date']} — {event['type']}\n\nWho: {event['who']}\n\nEvent: `{event['event_id']}`. Evidence group: `{event.get('evidence_group') or event['event_id']}`. Subject: `{event['statement_id']}`.\n\n")
            document.append('Source: `'+event.get('source_file','')+'`'+('; locus: '+event['where'] if event.get('where') else '')+'.\n\n')
            document.append(event['outcome']+'\n\n')
        if not event_rows:
            document.append('No event is associated with this exact owner or its retained historical statement identifiers. Its mathematical inputs and publication comparison remain recorded at their own identifiers.\n\n')

    counts_path = ROOT/'records/S6_SERIES_PUBLISH_check_counts.tsv'
    existing_fields, count_rows = read_rows(counts_path)
    _, baseline_tags = read_rows(ROOT.parent/'S6_SERIES_GRIND_tags.tsv')
    scopes = {
        'cp10_printed_statements':{r['label'] for r in baseline_tags if r['paper']=='II' and r['kind']=='statement'},
        'cp10_all_tagged_targets':{r['label'] for r in baseline_tags if r['paper']=='II'},
        'current_primary_statement_identifiers':data['active'],
        'current_printed_statements_and_definitions':data['subjects'],
    }
    count_rows = [r for r in count_rows if r['paper']!='II']
    for scope, subjects in scopes.items():
        selected = [e for e in data['events'] if data['tag_aliases'].get(e['statement_id'],e['statement_id']) in subjects]
        kinds = Counter(e['type'] for e in selected)
        count_rows.append(dict(paper='II',scope=scope,
            statements=len(rows) if scope.startswith('current_') else len(subjects),
            subject_identifiers=len(subjects),event_associations=len(selected),
            declared_evidence_groups=len({e.get('evidence_group') or e['event_id'] for e in selected}),
            outline_step_associations_separate=sum(any(e['statement_id'].startswith(m+' step ') for m in main) for e in data['events']) if scope.startswith('current_') else 0,
            **{kind:kinds[kind] for kind in TYPES}))

    statement_counts_path = ROOT/'records/S6_SERIES_PUBLISH_statement_check_counts.csv'
    statement_count_fields, statement_counts = read_rows(statement_counts_path,',')
    for row in statement_counts:
        if row['paper']!='II':
            continue
        sid = row['label']
        exact = events_by_subject[sid]
        substantive = [e for e in exact if e['type'] in SUBSTANTIVE]
        groups = {e.get('evidence_group') or e['event_id'] for e in substantive}
        def checker(e):
            value = re.sub(r'\s*\(.*?\)','',e['who'])
            return value.split(',')[0].strip()+' | '+(value.split(',')[-1].strip() if ',' in value else '')
        checkers = {checker(e) for e in substantive}
        owner = data['owners'].get(sid,row.get('current_statement_owner') or sid)
        row.update(active_current_statement=str(sid in data['subjects']).lower(),
            current_statement_owner=owner,
            main_dependency_reference_closure=str(owner in reachable).lower(),
            substantive_associations=len(substantive),substantive_evidence_groups=len(groups),
            distinct_checker_labels=len(checkers),all_associations=len(exact),
            below_bar='yes' if len(groups)<2 or len(checkers)<2 else 'two_only' if len(groups)<3 else 'no',
            checker_labels=' || '.join(sorted(checkers)))
    graph_path = ROOT/'records/S6_SERIES_PUBLISH_reference_graph.tsv'
    graph_fields, graph_rows = read_rows(graph_path)
    graph_rows = [r for r in graph_rows if r['paper']!='II'] + [dict(
        paper='II',**{'from':sid,'to':target},within_current_paper=str(target in by_id).lower(),
        interpretation='Reference in the statement, immediate proof or its own outline; mathematical premise scope is documented by the complete comparisons.')
        for sid in graph for target in sorted(graph[sid])]
    aliases_path = ROOT/'records/S6_SERIES_PUBLISH_current_statement_aliases.tsv'
    alias_fields, alias_rows = read_rows(aliases_path)
    alias_rows = [r for r in alias_rows if r['paper']!='II'] + [dict(
        paper='II',current_statement_id=data['owners'].get(sid,sid),retained_statement_identifier=sid,
        scope='Explicit current label and exact owner; no event is duplicated or upgraded by this correspondence.') for sid in sorted(data['subjects'])]
    programs = program_records(data['text'])
    printed_product, candidate_product, summary_product = remaining_derived_records(
        data, statement_counts, completed_required, required_resolution)
    assert SOURCE.read_text() == data['text'], 'Source changed during derivation.'
    assert (ROOT/'CHECK_EVENTS.tsv').read_bytes() == ledger_bytes, 'Event ledger changed during derivation.'
    for name, original in preserved_required.items():
        assert (ROOT/name).read_bytes() == original, ('Required disposition changed',name)
    # All in-memory validation precedes writes. These are the final derived
    # products, not copies or a sequence of intermediate inventories.
    write_rows(ROOT/'S6_SERIES_PUBLISH_tags.tsv',tag_fields,tags)
    write_rows(ROOT/'S6_SERIES_PUBLISH_inventory.csv',inv_fields,inventory,',')
    (ROOT/'S6_SERIES_PUBLISH_checks_II.md').write_text(''.join(document),newline='\n')
    write_rows(counts_path,existing_fields,count_rows)
    write_rows(statement_counts_path,statement_count_fields,statement_counts,',')
    write_rows(graph_path,graph_fields,graph_rows)
    write_rows(aliases_path,alias_fields,alias_rows)
    write_rows(ROOT/'S6_SERIES_PUBLISH_records_II.tsv',['printed_path','repository_path','sha256'],programs)
    write_rows(*printed_product)
    write_rows(*candidate_product, delimiter=',')
    summary_product[0].write_text(json.dumps(summary_product[1],ensure_ascii=False,indent=2)+'\n',newline='\n')
    (ROOT/'records/CHECK_EVENTS.tsv').write_bytes(ledger_bytes)
    for name, original in preserved_required.items():
        assert (ROOT/name).read_bytes() == original, ('Required disposition changed',name)
    assert (ROOT/'CHECK_EVENTS.tsv').read_bytes() == ledger_bytes
    from S6_SERIES_PUBLISH_c4_final_provenance import finalize_provenance
    finalize_provenance(data, programs, source_hash, pdf_hash, event_hash)
    print('Preserved Paper II required-check dispositions:',len(completed_required))
    print('Final current mathematical owners:',len(rows))
    print('Statement-associated event count:',len(data['selected']))
    print('Exact program records:',len(programs))
    print('Other papers inventory/tag/count rows preserved.')
    print('No event added, independence upgraded, historical proof discarded, or derived diff saved.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=('prepare','finish'))
    parser.add_argument('--pdf',type=Path)
    parser.add_argument('--aux',type=Path)
    args = parser.parse_args()
    if args.mode=='prepare':
        prepare()
    else:
        assert args.pdf and args.aux
        finish(args.pdf,args.aux)

if __name__=='__main__':
    main()
