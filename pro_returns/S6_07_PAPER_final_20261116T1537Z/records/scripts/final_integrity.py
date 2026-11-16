"""Source, status, bibliography and build-log checks; no mathematical validation."""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re, runpy

ROOT = Path(__file__).resolve().parents[3]
D = ROOT / 'deliverables'
R = D / 'records'
ns = runpy.run_path(str(R / 'scripts/build_audit_tables.py'))
blocks = ns['statement_blocks']((D / 'S6_07_PAPER_paper.tex').read_text())
rows = json.loads((R / 'all_records.json').read_text())
by_label = {r['paper_label']: r for r in rows}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()

literal = []
for r in rows:
    if r['paper_label'] not in blocks:
        continue
    source = r.get('source_statement', '')
    paths = []
    for relative in r['source_file'].split(';'):
        for base in [ROOT / 'inputs/sources', ROOT / 'inputs/context']:
            p = base / relative.strip()
            if p.is_file():
                paths.append(p)
    matches = [str(p.relative_to(ROOT / 'inputs')) for p in paths
               if source and norm(source) in norm(p.read_text())]
    composite = []
    separators = {'push:A.2.periods': '\n\n',
                  'push:B.4.33.scope': 'The untwisted family is',
                  'push:E.2.5.scope': 'Normalize the punctured family'}
    if r['paper_label'] in separators:
        separator = separators[r['paper_label']]
        a, b = source.split(separator, 1)
        chunks = [a, b if separator == '\n\n' else separator+b]
        for chunk in chunks:
            composite.append({'source_excerpt': chunk,
                              'matched_files': [str(p.relative_to(ROOT/'inputs')) for p in paths if norm(chunk) in norm(p.read_text())]})
    literal.append({'paper_label': r['paper_label'], 'matched_files': matches,
                    'source_excerpt_is_literal_after_whitespace_normalization': bool(matches),
                    'declared_noncontiguous_definition_excerpts': composite,
                    'all_declared_excerpts_matched': bool(composite) and all(x['matched_files'] for x in composite)})

master = (D / 'S6_07_PAPER_paper.tex').read_text()
labels = re.findall(r'\\label\{([^}]+)\}', master)
cited = {k.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', master)
         for k in group.split(',')}
bib = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', master))
announce = []
for m in re.finditer(r'\\begin\{announcement\}.*?\\end\{announcement\}', master, re.S):
    lab = re.search(r'\\label\{([^}]+)\}', m.group()).group(1)
    next_env = re.search(r'\\begin\{(?:theorem|proposition|lemma|corollary|cited|computed|announcement|definition|remark|refuted|example)\}', master[m.end():])
    tail = master[m.end():m.end()+next_env.start()] if next_env else master[m.end():]
    # A later unlabelled support proof is reported for inspection, never guessed away.
    announce.append({'paper_label': lab, 'printed_proof_before_next_statement': r'\begin{proof}' in tail,
                     'repository_pointer': 'repository' in tail.lower()})

result = {
    'scope': 'Editorial source fidelity, required status coverage and typesetting; no independent mathematical proof validation.',
    'csv_header': next(csv.reader((D / 'S6_07_PAPER_source_table.csv').open())),
    'source_rows': len(rows), 'formal_statement_entries': len(blocks),
    'status_counts': dict(Counter(r['status'] for r in rows)),
    'master_vs_ledger_mismatches': [r['paper_label'] for r in rows if r['paper_label'] in blocks and r['statement_as_printed'].strip() != blocks[r['paper_label']]['body'].strip()],
    'formal_source_excerpt_comparisons': literal,
    'contiguous_source_statement_count': sum(x['source_excerpt_is_literal_after_whitespace_normalization'] for x in literal),
    'declared_composite_definition_count': sum(x['all_declared_excerpts_matched'] for x in literal),
    'source_excerpt_failures': [x['paper_label'] for x in literal if not x['source_excerpt_is_literal_after_whitespace_normalization'] and not x['all_declared_excerpts_matched']],
    'duplicate_labels': [k for k, v in Counter(labels).items() if v > 1],
    'missing_bibliography_keys': sorted(cited - bib), 'uncited_bibliography_keys': sorted(bib - cited),
    'announcement_checks': announce,
    'proof_environment_count': master.count(r'\begin{proof}'),
    'independence_sentence_present': 'The same statement was obtained independently in the workbench from which this paper grew' in master,
    'version_two_sentence_present': 'Version 2 does not contain it.' in master,
    'prohibited_AI_assisted_wording': 'AI-assisted' in master,
    'external_input_commands': re.findall(r'\\(?:input|include|includegraphics|bibliography)\b[^\n]*', master),
    'sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [D/'S6_07_PAPER_paper.tex', D/'S6_07_PAPER_paper.pdf', D/'S6_07_PAPER_source_table.csv']},
}
(R / 'final_integrity.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps({k: v for k, v in result.items() if k not in ['formal_source_excerpt_comparisons','announcement_checks','sha256']}, ensure_ascii=False, indent=2))
