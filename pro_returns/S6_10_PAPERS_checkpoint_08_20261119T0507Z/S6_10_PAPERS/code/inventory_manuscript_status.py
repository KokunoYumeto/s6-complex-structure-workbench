"""Reconcile actually selected statement records against explicit current events.

This measures coverage, not publication readiness. Source gates, computations,
identity transfers and a full mathematical rederivation remain distinct.
"""
from pathlib import Path
import ast
import collections
import csv
import datetime
import hashlib
import json
import re

B = Path(__file__).resolve().parents[1]
inventory = list(csv.DictReader((B / 'S6_10_PAPERS_inventory.csv').open()))
by_label = collections.defaultdict(list)
for row in inventory:
    by_label[row['label']].append(row)
events = json.loads((B / 'analysis/inventory_current_events_by_label.json').read_text())

def braced(s, at):
    assert s[at] == '{'
    depth, i = 1, at + 1
    while depth:
        if s[i] == '{' and s[i-1] != '\\': depth += 1
        if s[i] == '}' and s[i-1] != '\\': depth -= 1
        i += 1
    return s[at+1:i-1], i

def kind(e):
    t = e['type'].lower()
    scope = e.get('scope', '').lower()
    if t == 'r-refutation':
        return 'refutation_review'
    if t == 'p-provenance':
        return 'provenance_scope_review'
    if (t == 'used and rechecked in this run' and
            'exact label identity' in scope and 'identity propagation' in scope and
            'sha256' in scope):
        return 'same_reading_identity'
    if (t == 'd' or 'proof check' in t or 're-proof' in t or 'reproof' in t or
            'proof re-derivation' in t or t == 'full retained-argument and refutation review'):
        return 'argument_review'
    if ('independent mathematical rederivation' in t or
            t == 'full source-proof reading and mathematical rederivation'):
        return 'argument_review'
    if 'receiving-summary' in t:
        return 'summary_deduction'
    if 'archived argument' in t:
        return 'known_formula_comparison'
    if t == 'a-identity':
        return 'same_reading_identity'
    if t == 'f-partial' or 'open-boundary' in t:
        return 'bounded_or_partial_review'
    if t == 'c' or 'comput' in t or 'certificate' in t or 'program replay' in t:
        return 'computation_only'
    if 'citation' in t or 'primary-source' in t:
        return 'source_locus'
    if t in {'e', 'scope-record', 'editorial_reconciliation', 'p-provenance'}:
        return 'editorial_or_scope_review'
    return 'bounded_dependency_review'

def paths_for(paper):
    if paper in {'I', 'III'}:
        tree = ast.parse((B / 'code' / paper / 'build_preview.py').read_text())
        parts = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == 'parts' for t in n.targets))
        return [B / 'papers' / paper / (n + '.tex') for n in parts]
    return [B / 'papers' / paper / n for n in ['frontmatter.tex', 'opening.tex', 'body.tex']
            if (B / 'papers' / paper / n).exists()]

papers = {}
all_records = []
for paper in ['I', 'II', 'III', 'IV', 'V', 'VI']:
    paths = paths_for(paper)
    text = '\n'.join(p.read_text() for p in paths)
    statement_records = []
    for m in re.finditer(r'\\StatementRecord\s*\{', text):
        label, at = braced(text, m.end()-1)
        while text[at].isspace(): at += 1
        status, _ = braced(text, at)
        rows = by_label.get(label, [])
        ev = events.get(label, [])
        kinds = sorted({kind(e) for e in ev})
        compendium = bool(rows) and all(r['in_compendium_only_because'] for r in rows)
        has_arg = bool(set(kinds) & {'argument_review', 'summary_deduction', 'same_reading_identity', 'refutation_review'})
        provenance_only = 'provenance_scope_review' in kinds and not has_arg
        open_row = 'open' in status.lower() or any(r['status'].lower().startswith('open') for r in rows)
        refuted_row = 'refuted' in status.lower() or status.lower().startswith('false as stated')
        audit_only = 'computation' in status.lower() or 'audit' in status.lower()
        rec = dict(paper=paper, label=label, printed_status=status,
                   inventory_rows=len(rows), inventory_papers=sorted({r['paper'] for r in rows}),
                   compendium_or_known_input=compendium, event_kinds=kinds,
                   provenance_scope_only=provenance_only,
                   argument_reading_or_exact_identity_recorded=has_arg,
                   current_event_sources=sorted({e['source'] for e in ev}),
                   open=open_row, refuted_history=refuted_row, bounded_audit=audit_only)
        rec['genuinely_unreviewed_receiving_argument'] = not ev and not (compendium or has_arg or provenance_only or open_row or refuted_row or audit_only)
        rec['argument_scope_needs_separate_resolution'] = bool(ev) and not (compendium or has_arg or provenance_only or open_row or refuted_row or audit_only)
        rec['retained_refutation_without_argument_event'] = refuted_row and not has_arg
        statement_records.append(rec)
    labels = {r['label'] for r in statement_records}
    selected = [r for r in inventory if r['paper'] == paper and not r['in_compendium_only_because']
                and not json.loads(r['notes']).get('receiving_integration_pending')]
    all_declared_labels = set(re.findall(r'\\label\{([^}]+)\}', text))
    papers[paper] = dict(
        source_paths=[str(p.relative_to(B)) for p in paths],
        source_sha256=hashlib.sha256(text.encode()).hexdigest(),
        statement_records=len(statement_records), unique_statement_labels=len(labels),
        known_input_records=sum(r['compendium_or_known_input'] for r in statement_records),
        receiving_records=sum(not r['compendium_or_known_input'] for r in statement_records),
        argument_review_or_exact_identity=sum(r['argument_reading_or_exact_identity_recorded'] for r in statement_records if not r['compendium_or_known_input']),
        exact_identity_records=sum('same_reading_identity' in r['event_kinds'] for r in statement_records if not r['compendium_or_known_input']),
        refutation_review_records=sum('refutation_review' in r['event_kinds'] for r in statement_records if not r['compendium_or_known_input']),
        provenance_scope_records=[r['label'] for r in statement_records if r['provenance_scope_only']],
        missing_inventory=sorted(labels-by_label.keys()),
        wrong_paper_assignment=[r['label'] for r in statement_records if r['inventory_rows'] and paper not in r['inventory_papers']],
        genuinely_unreviewed_receiving_arguments=[r['label'] for r in statement_records if r['genuinely_unreviewed_receiving_argument']],
        partial_computation_or_disposition_scopes=[{'label': r['label'], 'event_kinds': r['event_kinds']} for r in statement_records if r['argument_scope_needs_separate_resolution']],
        lacking_argument_review_event=[r['label'] for r in statement_records if not r['compendium_or_known_input'] and not r['argument_reading_or_exact_identity_recorded'] and not r['provenance_scope_only'] and not r['open'] and not r['bounded_audit']],
        retained_refutations_without_argument_event=[r['label'] for r in statement_records if r['retained_refutation_without_argument_event']],
        open_records=[r['label'] for r in statement_records if r['open']],
        bounded_audit_records=[r['label'] for r in statement_records if r['bounded_audit']],
        selection_labels_not_declared_in_body=sorted({r['label'] for r in selected}-all_declared_labels),
        provisional_exports_not_in_frozen_manuscript=[r['label'] for r in inventory if r['paper'] == paper and json.loads(r['notes']).get('receiving_integration_pending')],
        rows=statement_records)
    all_records += statement_records

result = dict(generated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              rule='Actual StatementRecord blocks from the owners selected fragments. Coverage categories are mechanical provenance buckets, not new proof verdicts. No full-proof credit is inferred from computations, aliases, citation openings or scoped events. Exact-identity events retain the original reading and add no independent review.',
              inventory_rows=len(inventory),
              source_gate_note='Exact primary-source gates are maintained separately by the root cited-source audit; their closure is not inferred from an argument event.',
              papers=papers)
(B / 'analysis/inventory_manuscript_status.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({p: {k: v for k, v in r.items() if k not in {'rows','source_paths','source_sha256'}} for p, r in papers.items()}, indent=2))
