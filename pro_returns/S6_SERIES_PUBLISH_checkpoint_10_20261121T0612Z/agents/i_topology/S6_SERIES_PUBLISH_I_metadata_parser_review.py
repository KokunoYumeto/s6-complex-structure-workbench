#!/usr/bin/env python3
"""Prepare and test bounded metadata guards without writing shared inputs."""
from pathlib import Path
import collections
import datetime
import hashlib
import importlib.util
import json
import re

BASE = Path('/workspace/scratch/653608133b22')
WORK = BASE / 'work'
OUT = WORK / 'agents/i_topology'
SCRIPT = WORK / 'code/S6_SERIES_PUBLISH_current_metadata.py'
REFERENCE = WORK / 'agents/provenance/code/S6_SERIES_PUBLISH_recompute_records.py'
TEX = WORK / 'S6_SERIES_PUBLISH_I.tex'
AUX = WORK / 'build/I_candidate12/S6_SERIES_PUBLISH_I.aux'
PREFIX = 'S6_SERIES_PUBLISH_I_metadata_parser'

def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()

original = SCRIPT.read_text()
source = TEX.read_text()
old = r'''for m in ENV.finditer(s,docstart):
    end=s.index('\\end{'+m[1]+'}',m.end())+len('\\end{'+m[1]+'}')
    after=re.match(r'\s*\\begin\{proof\}',s[end:])
    if after:end=s.index('\\end{proof}',end)+len('\\end{proof}')'''
new = r'''matches=list(ENV.finditer(s,docstart))
program_table_start=s.find(r'\section*{Programs}',docstart)
for i,m in enumerate(matches):
    end=s.index('\\end{'+m[1]+'}',m.end())+len('\\end{'+m[1]+'}')
    stop=matches[i+1].start() if i+1<len(matches) else s.find(r'\begin{thebibliography}',end)
    if stop<0:stop=len(s)
    if program_table_start>=end:stop=min(stop,program_table_start)
    # Include a source-credit paragraph before the immediate proof, but never
    # attach a proof beyond the next numbered environment or section heading.
    gap=s[end:stop]
    heading=re.search(r'\\(?:section|subsection|subsubsection|part)\*?\{',gap)
    if heading:gap=gap[:heading.start()]
    proof=re.search(r'\\begin\{proof\}',gap)
    if proof:
        depth=0
        for token in re.finditer(r'\\(begin|end)\{proof\}',gap[proof.start():]):
            depth+=1 if token.group(1)=='begin' else -1
            if depth==0:
                end+=proof.start()+token.end()
                break
        else:
            raise ValueError('Unclosed immediate proof after statement at line '+str(s.count('\n',0,m.start())+1))'''
assert original.count(old) == 1
proposed = original.replace(old, new)
compile(proposed, str(SCRIPT), 'exec')

code_guard = {
    'target': str(SCRIPT), 'target_sha256': sha(original),
    'reference_parser': str(REFERENCE),
    'reference_parser_sha256': sha(REFERENCE.read_bytes()),
    'guards': [{'old': old, 'new': new,
                'reason': 'Include the immediately following proof through a source-credit paragraph or retained marker gap, bounded by the next numbered environment/section; match the authoritative recompute parser and balance nested proof environments.'}],
    'scope': 'Metadata extraction only. No shared writes, mathematical events, check-row changes, or new mathematical credit.'
}
(OUT / (PREFIX + '_code_guard.json')).write_text(json.dumps(code_guard, indent=2) + '\n')
(OUT / (PREFIX + '_proposed.py')).write_text(proposed)

coherent_old = r'''\subsection{The proper holomorphic family and coherent descent}\hypertarget{tag-01PC}{}\label{fam:section:A.3}\label{I:coherent-descent-proof}

\begin{proposition}[Coherent even shifts and the quotient family]\hypertarget{tag-01Q2}{}\label{fam:src:A.3.1}\label{fam:st:A.3.1}'''
coherent_new = r'''\subsection{The proper holomorphic family and coherent descent}\hypertarget{tag-01PC}{}\label{fam:section:A.3}

\begin{proposition}[Coherent even shifts and the quotient family]\hypertarget{tag-01Q2}{}\label{fam:src:A.3.1}\label{fam:st:A.3.1}\label{I:coherent-descent-proof}'''
assert source.count(coherent_old) == 1
app_marker = r'\hypertarget{tag-000C}{}\label{app:rederive:fam-src-A.5.1}'
app_head = r'\begin{theorem}[Classification of the standard family]\hypertarget{tag-01Q6}{}\label{fam:src:A.5.1}\label{fam:st:A.5.1}\label{wb:pshift:thm:classification}'
start = source.index(app_head)
end = source.index(r'\begin{proof}', start) + len(r'\begin{proof}')
app_old = source[start:end]
assert app_old.count(app_marker) == 1
app_new = app_old.replace(app_head, app_head + app_marker)
app_new = app_new.replace('\\end{theorem}\n' + app_marker + '\n\\begin{proof}', '\\end{theorem}\n\\begin{proof}')
assert app_new.count(app_marker) == 1
source_new = source.replace(coherent_old, coherent_new).replace(app_old, app_new)
tex_guards = {
    'target': str(TEX), 'target_sha256': sha(source),
    'guards': [
        {'old': coherent_old, 'new': coherent_new,
         'reason': 'Make the coherent-descent proof marker inherit its owner proposition number7.5, while retaining the separate subsection label/tag01PC at subsection7.2.'},
        {'old': app_old, 'new': app_new,
         'reason': 'Move the retained classification proof alias/tag000C into its owning theorem header so its number is7.8 rather than the ambient subsection7.4.'}
    ],
    'scope': 'Alias/anchor relocation only; all statement and proof text, every label, and every permanent tag are retained.'
}
(OUT / (PREFIX + '_alias_guards.json')).write_text(json.dumps(tex_guards, indent=2) + '\n')

label_pattern = r'\\label\{([^}]+)\}'
tag_pattern = r'\\hypertarget\{tag-([^}]+)\}'
assert collections.Counter(re.findall(label_pattern, source)) == collections.Counter(re.findall(label_pattern, source_new))
assert collections.Counter(re.findall(tag_pattern, source)) == collections.Counter(re.findall(tag_pattern, source_new))
def without_moved_markers(s):
    for marker in [r'\label{I:coherent-descent-proof}', app_marker]:
        s = s.replace(marker, '')
    return re.sub(r'\s+', '', s)
assert without_moved_markers(source) == without_moved_markers(source_new)

def extract(script, tex, aux_path=AUX):
    """Execute only definitions and the read-only parser, never the output code."""
    namespace = {'__file__': str(SCRIPT)}
    exec(compile(script[:script.index('p=argparse.ArgumentParser()')], str(SCRIPT), 'exec'), namespace)
    namespace.update(s=tex,
        labels=namespace['auxlabels'](aux_path),
        by_label={r['label']: r for r in namespace['rows'](WORK / 'S6_SERIES_PUBLISH_tags.tsv')})
    fragment = script[script.index('docstart=s.index('):script.index('usedby=collections.defaultdict(set)')]
    exec(compile(fragment, str(SCRIPT), 'exec'), namespace)
    return namespace['statements'], namespace['owners'], namespace

old_sts, old_owners, old_ns = extract(original, source)
new_sts, new_owners, new_ns = extract(proposed, source)
rel_sts, rel_owners, rel_ns = extract(proposed, source_new)
old_by = {r['id']: r for r in old_sts}
new_by = {r['id']: r for r in new_sts}
rel_by = {r['id']: r for r in rel_sts}
assert list(old_by) == list(new_by) == list(rel_by)
assert [r['identities'] for r in old_sts] == [r['identities'] for r in new_sts] == [r['identities'] for r in rel_sts]

spec = importlib.util.spec_from_file_location('publish_reference_parser', REFERENCE)
reference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reference)
ref_sts = reference.statements(TEX)
ref_by = {r['statement_id']: r for r in ref_sts}
ref_owners = {lab: r['statement_id'] for r in ref_sts for lab in r['owned_labels']}

changed = []
for sid, a in old_by.items():
    b = new_by[sid]
    if a['references'] != b['references'] or a['end'] != b['end'] or set(a['labels']) != set(b['labels']):
        changed.append({'id': sid, 'number': b['number'],
                        'old_end_line': a['end_line'], 'new_end_line': b['end_line'],
                        'old_references': a['references'], 'new_references': b['references'],
                        'added_references': sorted(set(b['references']) - set(a['references'])),
                        'removed_references': sorted(set(a['references']) - set(b['references'])),
                        'new_owned_labels': sorted(set(b['labels']) - set(a['labels'])),
                        'reference_parser_references': ref_by[sid]['refs'],
                        'references_match_authoritative': b['references'] == ref_by[sid]['refs']})
assert new_by['inv:A3.1']['references'] == ['inv:A1.0', 'inv:A2.4', 'inv:eq:A-absolute-table']
assert old_by['inv:A3.1']['references'] == []
assert new_by['inv:A3.1']['references'] == ref_by['inv:A3.1']['refs']

def synthetic(contents):
    return r'\begin{document}' + contents + r'\begin{thebibliography}{9}\end{thebibliography}\end{document}'
def statement(label):
    return r'\begin{proposition}\hypertarget{tag-test-' + label + r'}{}\label{' + label + r'} Test.\end{proposition}'
fixtures = {
    'credited_immediate_proof': (synthetic(statement('test:a') + r'Credit \cref{credit:input}.\begin{proof}\cref{proof:input}.\end{proof}'), {'credit:input', 'proof:input'}),
    'retained_label_gap': (synthetic(statement('test:a') + r'\hypertarget{tag-test-marker}{}\label{test:marker}\begin{proof}\cref{proof:input}.\end{proof}'), {'proof:input'}),
    'next_numbered_environment_boundary': (synthetic(statement('test:a') + 'Credit only.' + statement('test:b') + r'\begin{proof}\cref{unrelated:input}.\end{proof}'), set()),
    'next_subsection_boundary': (synthetic(statement('test:a') + r'\subsection{Next}\begin{proof}\cref{unrelated:input}.\end{proof}'), set()),
    'balanced_nested_proof': (synthetic(statement('test:a') + r'Credit.\begin{proof}\cref{proof:first}\begin{proof}\cref{proof:inner}\end{proof}\cref{proof:last}\end{proof}'), {'proof:first', 'proof:inner', 'proof:last'}),
}
fixture_results = []
for name, (tex, expected) in fixtures.items():
    sts, _, _ = extract(proposed, tex)
    got = set(sts[0]['references'])
    assert got == expected, (name, got, expected)
    fixture_results.append({'name': name, 'expected': sorted(expected), 'observed': sorted(got), 'passed': True})

marker_rows = []
for marker, owner in [('I:coherent-descent-proof','fam:src:A.3.1'), ('app:rederive:fam-src-A.5.1','fam:src:A.5.1')]:
    marker_rows.append({'marker':marker, 'owner':owner,
        'candidate12_marker_aux':old_ns['labels'][marker],
        'candidate12_owner_aux':old_ns['labels'][owner],
        'original_metadata_owner':old_owners.get(marker),
        'parser_only_metadata_owner':new_owners.get(marker),
        'after_alias_relocation_owner':rel_owners.get(marker),
        'authoritative_recompute_owner':ref_owners.get(marker),
        'expected_rebuilt_marker_number':old_ns['labels'][owner]['number']})
    assert rel_owners[marker] == owner

receipt = {
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'task':'Bounded current-metadata parser and deferred-proof alias ownership review',
    'inputs':{str(p):sha(p.read_bytes()) for p in [SCRIPT,REFERENCE,TEX,AUX,WORK/'S6_SERIES_PUBLISH_tags.tsv',WORK/'CHECK_EVENTS.tsv']},
    'execution_scope':'Executed only definitions and parser fragments in memory. The main output-writing code was not executed. No shared file was written.',
    'source_statement_count':len(old_sts), 'proposed_statement_count':len(new_sts),
    'statement_order_and_primary_ids_unchanged':True,
    'retained_statement_identity_sequences_unchanged':True,
    'all_labels_and_tags_preserved_by_alias_guards':True,
    'nonwhitespace_source_content_unchanged_after_removing_only_moved_markers':True,
    'changed_metadata_regions':changed,
    'deferred_marker_comparison':marker_rows,
    'bounded_parser_fixtures':fixture_results,
    'limitations':['The proposal retains the existing explicit deferred-proof fallback. Its repeated reference extraction is set-valued, so no check row or reference edge is duplicated.',
                   'The two scripts have other intentional reference-scope differences (outline attachment and range expansion); this receipt compares the affected immediate-proof regions and marker ownership, not every feature of both programs.',
                   'Expected rebuilt alias numbers require the next root-owned full build; an isolated label fixture is supplied separately.'],
    'mathematical_events_added':0, 'check_rows_modified':0,
    'proposed_script_sha256':sha(proposed), 'proposed_source_sha256':sha(source_new)
}
(OUT / (PREFIX + '_comparison.json')).write_text(json.dumps(receipt, indent=2) + '\n')
(OUT / (PREFIX + '_relocated_source.tex')).write_text(source_new)
summary = {'printed_environments':len(new_sts), 'changed_regions':changed,
           'markers':marker_rows, 'fixtures_passed':len(fixture_results)}
(OUT / (PREFIX + '_output.json')).write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
