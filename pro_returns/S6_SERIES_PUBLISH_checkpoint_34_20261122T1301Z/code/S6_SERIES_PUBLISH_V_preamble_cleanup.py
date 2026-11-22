#!/usr/bin/env python3
"""Move unprinted inherited metadata to records and keep only used reference bindings."""
from pathlib import Path
import csv,re,json
from S6_SERIES_PUBLISH_editing import Editor,ROOT
e=Editor('V');a=e.text.index('\\begin{document}');preamble=e.text[:a];body=e.text[a:]
used=set(re.findall(r'\\SeriesRef\{([^}]+)\}',body));oldlines=[];kept=[];rows=[]
pat=re.compile(r'\\expandafter\\def\\csname (SRef|SUse|SBack)@(.+?)\\endcsname\{(.*)\}\s*$')
for line in preamble.splitlines(keepends=True):
 m=pat.match(line.rstrip())
 if m and (m[1] in ('SUse','SBack') or m[2] not in used):
  oldlines.append(line);rows.append({'kind':m[1],'label':m[2],'inherited_tex':m[3]})
 else:kept.append(line)
newpre=''.join(kept)
for label in used:
 assert '\\csname SRef@'+label+'\\endcsname' in newpre,label
if oldlines:
 e.text=newpre+body;e.record('D10',''.join(oldlines),'','Move unprinted dependency/back-link macros into checking records and remove unused static reference bindings from the standalone paper.','preamble')
# The three occurrences denote the same period matrix of the fixed X.
count=e.text.count('\\Pi_c');assert count==3,count
e.replace('\\Pi_c','\\Pi_X','D20','Use a member-indexed symbol for the unchanged period matrix of the chosen six-sphere, avoiding collision with the rank-six real parameter.','def:V:resolved-product-data',count)
line='\\newcommand{\\CurrentChecker}{GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), 18 November 2026}\n'
if line in e.text:e.replace(line,'','D07','Remove the unused historical checker macro; exact checker provenance is in the records.','preamble')
e.save()
with (ROOT/'records/S6_SERIES_PUBLISH_V_inherited_reference_macros.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['kind','label','inherited_tex'],delimiter='\t');w.writeheader();w.writerows(rows)
print('moved bindings',len(rows),'used cross-paper references',len(used))
