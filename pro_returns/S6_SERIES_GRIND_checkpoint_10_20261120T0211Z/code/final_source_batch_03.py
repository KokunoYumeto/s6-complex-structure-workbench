"""Reviewed computation prose and current source-credit integration."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1]
p=R/'parts/IV.body.linked.tex';t=p.read_text();before=re.findall(r'\\tag\{([^}]+)\}',t);records=[]
for file in ['audit_corrections/IV_closed_computation_patches.json','audit_corrections/IV_closed_computation_followup_patches.json']:
 for x in json.loads((R/file).read_text()):
  old,new=x['old_text'],x['new_text'];assert t.count(old)==1,(file,x['label'],old[:100],t.count(old))
  t=t.replace(old,new,1);records.append(x)
assert before==re.findall(r'\\tag\{([^}]+)\}',t)
assert t.count('\\begin{proof}')==t.count('\\end{proof}')

# The new full witness output has the actual target matrices at every step.
old=r'''every step are retained in the \texttt{all28\_witnesses} field of
\path{code/part3/e6_selected_i3_m2_all_fans.json}.'''
new=r'''every step are retained in the \texttt{witnesses} field of
\path{code/outputs/IV_K112_fresh_checks.json}.'''
assert t.count(old)==1;t=t.replace(old,new)
records.append({'label':'night:P3K.112','old_text':old,'new_text':new})
a=t.index('\\par\\medskip\\noindent\\textbf{Exact execution and independent full audits.}',t.index('\\label{night:P3K.112}'))
b=t.index('\\end{proof}',a)
old=t[a:b]
new=r'''\par\medskip\noindent\textbf{Exact source, cap and target-prism calculation.}\par
The program \path{code/IV_K112_fresh_checks.py} uses exact rational
Gaussian elimination on all ten equations of the nine-variable
target system. It derives each target independently of the closed
solution and checks the redundant equation. The source and cap
identities use symbolic polynomial and rational-function arithmetic.
Its output \path{code/outputs/IV_K112_fresh_checks.json} records
7859 exact assertions: 220 complete target-prism steps, 360 input
unimodular bases, 46 canonical fans and 1260 cap-character instances.
Every one of the twenty-eight displayed witness bases, directed words,
unreduced integer sums and residues agrees with this calculation.
The output includes each target matrix, derivative, native reset and
multiplier exponent matrix. The full Euler wedge and the signed
source/cap meridian identities are evaluated before reduction.

The terminating construction in AFM2.1--4 proves the assertion for
every integral basis. The VM2, IVM2 and IGC arguments supply the full
source, point-line, relative characteristic and proper cap maps.
The absolute initial pair remains the input from
\cref{night:P3K.111}; the compact and lower-surface integer
evaluations in that statement are the remaining initial-value
calculation for the displayed absolute returns here.

'''
t=t[:a]+new+t[b:];records.append({'label':'night:P3K.112','old_text':old,'new_text':new})
p.write_text(t)
(R/'analysis/IV_closed_computation_changes_03.json').write_text(json.dumps(records,indent=2)+'\n')

csv.field_size_limit(10**9);p=R/'S6_SERIES_GRIND_inventory.csv'
with p.open() as f:rows=list(csv.DictReader(f));fields=list(rows[0])
updates=json.loads((R/'audit_paper_i/I_literature_inventory_updates.json').read_text());used=set();credit=[]
for row in rows:
 if row['label'] in updates:
  data=updates[row['label']]
  for k in data:
   if k not in fields:fields.append(k)
  credit.append({'label':row['label'],'old':{k:row.get(k,'') for k in data},'new':data})
  row.update(data);used.add(row['label'])
assert used==set(updates),set(updates)-used
with p.open('w',newline='') as f:w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
(R/'analysis/I_credit_updates_03.json').write_text(json.dumps(credit,indent=2)+'\n')
print(json.dumps({'IV_paragraph_changes':len(records),'I_credit_rows':len(credit)}))
