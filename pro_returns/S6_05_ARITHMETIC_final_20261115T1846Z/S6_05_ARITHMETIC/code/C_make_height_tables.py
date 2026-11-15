#!/usr/bin/env python3
"""Collate, without recomputation or truncation of source data, the CM tables."""
from pathlib import Path
import re, json, ast
import mpmath as mp
root=Path(__file__).resolve().parents[1]
mp.mp.dps=270
raw=(root/'code/C_cm_local_heights.out').read_text()
blocks=re.split(r'\nINDEX ',raw)[1:]
rows=[]
for b in blocks:
    m=re.match(r'(\d+) j (-?\d+) model (\[.*?\]) P (\[.*?\])',b)
    idx,jj=int(m[1]),int(m[2]); model=ast.literal_eval(m[3]); P=ast.literal_eval(m[4])
    locals=[]
    for line in b.splitlines():
        if not line.startswith('p '):continue
        a=re.match(r'p (\d+) localred \[(\d+), (-?\d+),.* component_order (\d+) .* lambda/logp (.*)',line)
        p,kod,order=int(a[1]),int(a[3]),int(a[4])
        ty={1:'I_0',2:'II',3:'III',4:'IV',-1:'I_0^*',-2:'IV^*',-3:'III^*',-4:'II^*'}.get(kod)
        if ty is None:ty=('I_{%d}'%(kod-4)) if kod>4 else ('I_{%d}^*'%(-kod-4))
        locals.append((p,ty,order,a[5]))
    rows.append(dict(i=idx,j=jj,model=model,P=P,local=locals))
prec={}
for line in (root/'code/C_cm_250.out').read_text().splitlines():
    if '|' in line:
        j,h,w1,w2=line.split('|');prec[int(j)]=mp.mpf(h)
A=[mp.sqrt(6),2**(mp.mpf(2)/3)*3**(mp.mpf(1)/4),2**(mp.mpf(3)/4),2,2,mp.sqrt(3),1,3**(mp.mpf(5)/12),1,1,1]
out=[r'\begingroup\small',r'\begin{longtable}{r r r r r r}',r'\toprule Row & $j$ & $a_3$ & $a_4$ & $a_6$ & $y_P$\\\midrule\endhead']
for r in rows:out.append('%d & %d & %d & %d & %d & %d\\\\'%(r['i'],r['j'],r['model'][2],r['model'][3],r['model'][4],r['P'][1]))
out.extend([r'\bottomrule\end{longtable}',r'\begin{longtable}{r r l c c l}',r'\toprule Row & $p$ & Type & Component & Order & $\lambda_p/\log p$\\\midrule\endhead'])
for r in rows:
    for p,ty,order,coeff in r['local']:
        if '/' in coeff:
            a,b=coeff.split('/');coeff=r'\frac{%s}{%s}'%(a,b)
        out.append('%d & %d & $%s$ & $%s$ & %d & $%s$\\\\'%(r['i'],p,ty,'0' if order==1 else 'c_P',order,coeff))
out.extend([r'\bottomrule\end{longtable}',r'\endgroup',r'\noindent The next table prints 52 significant digits. The last column is both the directly computed $\log N$ and the independently computed $\log A_t-\widehat h_O(P_t)$; the agreement is more precise than the digits printed.',r'\begingroup\small',r'\begin{longtable}{r l}',r'\toprule Row & Height and archimedean logarithm\\\midrule\endhead'])
for r,a in zip(rows,A):
    h=prec[r['j']];l=mp.log(a)-h
    out.extend(['%d & $\\widehat h_O=%s$\\\\'%(r['i'],mp.nstr(h,52)),r' & $\log N=%s$\\[3pt]'%mp.nstr(l,52)])
out.extend([r'\bottomrule\end{longtable}\endgroup'])
(root/'sections/C_height_tables.tex').write_text('\n'.join(out)+'\n')
(root/'records/C_cm_exact_local_data.json').write_text(json.dumps(rows,indent=2)+'\n')
print('Collated eleven exact models, all bad local contributions, and 52-digit height identities.')
