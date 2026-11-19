#!/usr/bin/env python3
"""Locate main-result ladders without assigning a new mathematical verdict."""
import collections
import csv
import datetime
import hashlib
import json
import re
from pathlib import Path

W = Path(__file__).resolve().parents[1]


def argument(text, at):
    assert text[at] == '{'
    depth, i = 1, at + 1
    while depth:
        escaped = i > 0 and text[i-1] == '\\'
        if text[i] == '{' and not escaped:
            depth += 1
        elif text[i] == '}' and not escaped:
            depth -= 1
        i += 1
    return text[at+1:i-1], i


inventory = list(csv.DictReader((W / 'S6_10_PAPERS_inventory.csv').open()))
main = collections.defaultdict(set)
for row in inventory:
    if row['main_or_supporting'] == 'main' and not row['in_compendium_only_because']:
        main[row['paper']].add(row['label'])

ladders = []
for paper in ['I', 'II', 'III', 'IV', 'V', 'VI']:
    path = W / 'papers' / paper / 'opening.tex'
    text = path.read_text()
    starts = list(re.finditer(r'\\RungZero\s*\{', text))
    headings = list(re.finditer(r'\\(?:sub)*section\*?\s*\{', text))
    for number, match in enumerate(starts, 1):
        zero, at = argument(text, match.end()-1)
        end = starts[number].start() if number < len(starts) else len(text)
        full = text[match.start():end]
        prior = [m for m in headings if m.start() < match.start()]
        heading = argument(text, prior[-1].end()-1)[0] if prior else 'Series opening'
        refs = set()
        for hit in re.finditer(r'\\(?:c|C|eq|auto)?ref\s*\{([^}]+)\}', full):
            refs.update(x.strip() for x in hit.group(1).split(','))
        rung_one = full.find(r'\RungOne')
        steps = None
        if rung_one >= 0:
            enum = re.search(r'\\begin\{enumerate\}', full[rung_one:])
            if enum:
                begin = rung_one + enum.end()
                depth, count = 1, 0
                for token in re.finditer(r'\\(?:begin\{enumerate\}|end\{enumerate\}|item\b)', full[begin:]):
                    value = token.group()
                    if value == r'\begin{enumerate}':
                        depth += 1
                    elif value == r'\end{enumerate}':
                        depth -= 1
                        if depth == 0:
                            break
                    elif depth == 1:
                        count += 1
                steps = count
        ladders.append(dict(id=f'{paper}.L{number:02}', paper=paper, ordinal=number,
                            file=str(path.relative_to(W)), line=text.count('\n', 0, match.start())+1,
                            heading=heading, rung_zero=zero, steps=steps,
                            references=sorted(refs), explicit_main_labels=sorted(refs & main[paper]),
                            span=[match.start(), end], source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                            text_sha256=hashlib.sha256(full.encode()).hexdigest(), text=full))

direct = {paper: {label: [l['id'] for l in ladders if l['paper'] == paper and label in l['references']]
                  for label in sorted(labels)} for paper, labels in main.items()}
result = dict(recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              scope='Exact opening locations, explicit references and top-level step counts only; grouped coverage and statement scope require the separate current reading.',
              ladders=ladders, direct_main_mapping=direct,
              main_without_direct_reference={p: [label for label, matches in rows.items() if not matches]
                                             for p, rows in direct.items()})
(W / 'analysis/inventory_opening_ladders.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
print(json.dumps(dict(ladders=len(ladders), main_without_direct_reference=result['main_without_direct_reference'],
                      step_counts={p:[(l['id'],l['steps']) for l in ladders if l['paper']==p] for p in main}),indent=2))
