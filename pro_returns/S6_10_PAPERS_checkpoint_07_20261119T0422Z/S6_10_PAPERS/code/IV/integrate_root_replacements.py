"""Apply exact parent-reviewed blocks and remove the obsolete numerical Uses cycle."""
root_replacements=json.loads((W/'analysis/IV/root_replacements.json').read_text())
for root_label,root_edits in root_replacements.items():
 def apply_root(t,root_edits=root_edits,root_label=root_label):
  for edit in root_edits:
   assert edit['old'] in t,(root_label,edit['old'][:100])
   t=t.replace(edit['old'],edit['new'],1)
  lines=t.splitlines()
  for i,line in enumerate(lines):
   if line.startswith(r'\StatementRecord'):
    if root_label in ['maps:src:B.6.18','maps:src:B.6.19']:
     line=line[:-1]+r'; \cref{maps:src:B.6.20}}'
    elif root_label=='maps:src:B.6.20':
     line=line.replace(r'; \cref{maps:src:B.6.19}','').replace(r'\cref{maps:src:B.6.19}; ','')
     line=line[:-1]+r'; \cref{maps:src:B.6.16}; \cref{maps:src:B.6.17}}'
    lines[i]=line
    break
  return '\n'.join(lines)+'\n'
 change(root_label,apply_root,
  'Integrate the exact independently reviewed parent replacement, retaining its numbered local proof and source credit; use the completed B6.20 numerical calculation forward from B6.18/19 without a reverse proof dependency.')
