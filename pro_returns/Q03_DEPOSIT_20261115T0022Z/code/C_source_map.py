#!/usr/bin/env python3
"""Reproduce the numbered OpenAI-source and Q03 dependency-column concordance.
Source numbering is computed from the section-shared theorem counter declared
in paper.tex, after expanding local input files, rather than guessed from Q03.
"""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'background/sources/papers/openai-scheduling/build'
OUT=ROOT/'Q03_DEPOSIT/code'
events=[]
pattern=re.compile(r'\\input\{([^}]+)\}|\\section\{|\\begin\{(theorem|lemma|proposition|corollary|definition|remark)\}')
def expand(name):
 p=SOURCE/name;s=p.read_text()
 for m in pattern.finditer(s):
  line=s.count('\n',0,m.start())+1
  if m.group(1):
   sub=m.group(1);expand(sub if sub.endswith('.tex') else sub+'.tex')
  elif m.group(2):
   end=s.find('\\end{'+m.group(2)+'}',m.end())
   lab=re.search(r'\\label\{([^}]+)\}',s[m.end():end])
   events.append({'kind':m.group(2),'file':name,'line':line,'label':lab.group(1) if lab else None})
  else:events.append({'kind':'section','file':name,'line':line})
expand('paper.tex')
sec=count=0;statements=[]
for e in events:
 if e['kind']=='section':sec+=1;count=0
 else:
  count+=1;statements.append({**e,'number':f'{sec}.{count}'})
(OUT/'C_preprint_statement_map.json').write_text(json.dumps(statements,indent=2)+'\n')
bylabel={r['label']:r for r in statements}
# Each row is a mathematical counterpart or constituent argument, not a claim
# that the m=3 source proves the new all-m statement or its new constants.
spec=[
('2.1',None,'paper.tex:283-297, frames and fixed topological rank','Section 2.2','Topological rank is fixed in the source preliminaries; Q03 gives a separate lemma.'),
('2.2',None,'paper.tex:109-114, floor/start-time argument','Section 1','The real-to-integer schedule argument appears in unnumbered prose.'),
('2.3','lem:padding',None,None,'Capacity 3 counterpart.'),
('2.4','lem:reorder',None,None,'Capacity 3 counterpart.'),
('2.5',None,'paper.tex:283-310, frame and cone definitions','Section 2.2','Definitions/prose; no separate source lemma.'),
('2.6',None,'paper.tex:322-324, complement by De Morgan','Section 2.3','Prose before Lemma 2.3.'),
('2.7','lem:family',None,None,'The source counts triple primitives, hence exponent 3K.'),
('2.8','prop:algorithm',None,None,'Statement plus Section 3 dynamic program.'),
('2.9','def:hierarchy',None,None,'Source definition of a bounded hierarchy.'),
('2.10','lem:hierarchy-dp',None,None,'Hierarchy-to-DP acceptance.'),
('3.1','lem:separator-description',None,None,'Separator description formulas.'),
('3.2','lem:separator-description',None,None,'Reversal is explicitly included in the statement and proof.'),
('3.3','lem:lex-prefix',None,None,'Normalized-prefix exchange.'),
('3.4','lem:shared',None,None,'Constituent one-advance argument inside the source proof.'),
('3.5','lem:shared',None,None,'Constituent fixed-cutoff walk inside the source proof.'),
('3.6','lem:shared',None,None,'Shared-cutoff walk statement and proof.'),
('3.7','cor:any-ideal',None,None,'Creating a separator.'),
('4.1',None,'construction.tex:19-28, ordered keys','Section 5.1','Key monotonicity is unnumbered prose.'),
('4.2',None,'construction.tex:81-115, cover and center formulas','Section 5.2','Cover equation and same/switch center separator.'),
('4.3',None,'construction.tex:116-136, priority orders and cutoffs','Section 5.2','Replace the original edge-label lemma label with these definitions and justification.'),
('4.4','lem:edge-labels','construction.tex:139-173 and Lemma 5.1',None,'Shared walk construction immediately before the lemma supplies common cutoffs.'),
('4.5','lem:edge-labels',None,None,'Edge boundary/cone/shrinking assertions.'),
('5.1','lem:carry',None,None,'Suffix-carry formula.'),
('5.2','lem:prune',None,None,'Pruning comparison.'),
('5.3','lem:update-labels',None,None,'Qualifier partition and child first invariant.'),
('5.4',None,'lists.tex:115-120, run and combined rank thresholds','Section 6.3','Replace list-length lemma label: entry shape is the preceding prose.'),
('5.5','lem:list-length',None,None,'Source has at most 3 injections and 5 entries; Q03 replaces capacity and bound.'),
('6.1','lem:flatten',None,None,'Flattening the initial pair.'),
('6.2','lem:old-low',None,None,'Source earlier-low extension has at most 21 leaves.'),
('6.3',None,'lists.tex:254-268, equation (ancestry)','Section 6.5','Replace G lemma label: arrangement is the preceding prose/equation.'),
('6.4','lem:G',None,None,'Switch upset.'),
('6.5','lem:entry-size',None,None,'Individual entry counterpart; the aggregate 6m+9 accounting is Q03-specific.'),
('7.1','lem:past',None,None,'Second boundary invariant for children.'),
('7.2','lem:swap',None,None,'Third boundary invariant for children.'),
('7.3','prop:construction-valid',None,None,'Construction validity.'),
('8.1',None,'descriptions.tex:16-40, cutoff-agreement/direct-same/direct-switch equations','Section 8.1','Replace global-child lemma label: predicates are defined immediately before that lemma.'),
('8.2','lem:global-child',None,None,'Global child formula.'),
('8.3','lem:relative-splits',None,None,'Relative descriptions at marked slots.'),
('8.4','lem:final-count',None,None,'Source uses fixed numeric budgets; Q03 uses aggregate linear budgets.'),
('8.5','thm:structure',None,None,'Source theorem has fewer than 500 leaves; Q03 asserts 12m+25.'),
('9.1','thm:main','paper.tex:120-130 and Proposition 3.1',None,'The m=3 main result; capacity-m correctness requires the Q03 proof.'),
('9.2',None,'paper.tex:488-524, proof of Proposition 3.1','Section 9','This is the actual source accounting, rather than only its proposition statement.'),
('9.3',None,'paper.tex:520-524, input length and deadline trials','Section 9','Actual input-exponent derivation; source final exponent is 150020.'),
('9.4','rem:compact',None,None,'Compact isolated-job decision remark; no explicit-output size promise.')]
rows=[]
for ident,lab,loc,display,note in spec:
 s=bylabel.get(lab,{})
 rows.append({'q03_id':ident,'source':'P','source_label':lab,'source_number':s.get('number'),
              'source_kind':s.get('kind'),'source_locator':loc or f"{s['file']}:{s['line']} onward",
              'source_display':display or f"{s['kind'].capitalize()} {s['number']}",'note':note,'check':'S-P'})
(OUT/'C_dependency_source_map.json').write_text(json.dumps(rows,indent=2)+'\n')
lines=['# Dependency source column: exact concordance','',
 'Date: 15 November 2026. [P] is fixed at commit `4eaee87548250b2682affda7d05d947c05554bae`.',
 'Numbers are computed from the source section-shared theorem counter. Source counterparts describe m=3; they do not certify the capacity-m replacement or Q03 constants.',
 '', '| Q03 id | Correct source entry | Exact label/location | Comparison |','|---|---|---|---|']
for r in rows:
 lab='`'+r['source_label']+'`; ' if r['source_label'] else ''
 lines.append(f"| {r['q03_id']} | [P] {r['source_display']} | {lab}{r['source_locator']} | {r['note']} |")
(ROOT/'Q03_DEPOSIT/work/C_dependency_source_map.md').write_text('\n'.join(lines)+'\n')
print(f'{len(statements)} source statements; {len(rows)} Q03 counterpart rows')
print('Label existence, numbering and statement comparison: S-P; general-m proof validity is checked separately.')
