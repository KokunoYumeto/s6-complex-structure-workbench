"""Integrate explicitly reviewed mathematical corrections; retain exact receipts."""
from pathlib import Path
import json,re,hashlib,csv
ROOT=Path(__file__).resolve().parents[1]
receipt=[]
def exact(paper, old, new, key, reason):
 path=ROOT/f'parts/{paper}.body.linked.tex';s=path.read_text()
 if new in s and old not in s:return
 if s.count(old)!=1:raise ValueError((key,s.count(old)))
 path.write_text(s.replace(old,new,1))
 receipt.append(dict(id=key,paper=paper,reason=reason,old=old,new=new))
for p in json.loads((ROOT/'audit_paper_i/paper_v_review/patches_P1_18.json').read_text()):
 new=p['new']
 if p['operation']!='replace_exact':raise ValueError(p)
 if 'begin{proof}' in new:
  new=new.replace(',quad',r',\quad')
  new=new.replace('blocks of32','blocks of 32').replace('degree600','degree 600').replace('from32','from 32').replace('of16','of 16').replace('are412','are 412').replace('are1088','are 1088').replace('and512','and 512').replace('leaves,1600','leaves, 1600').replace('uses120','uses 120').replace('uses80','uses 80').replace('is8','is 8')
  new=re.sub(r'\bitem([126])\b',r'item \1',new)
  oldchain=r'''The rational matrices $R_c,A_0$ are obtained by substituting in
$D_\lambda^{-1}\Gamma_6D_\lambda+D_\lambda^{-1}D_\lambda'$;'''
  newchain=r'''The chain rule gives the exact $q$ connection
\[
 \Gamma_q=D_\lambda^{-1}\lambda_*\Gamma_6(\lambda(q))D_\lambda
           +D_\lambda^{-1}\frac{dD_\lambda}{dq}
          =\frac{R_c}{q}+\frac{A_0}{1+q}.
\]
The rational matrices $R_c,A_0$ are obtained by this substitution;'''
  assert oldchain in new;new=new.replace(oldchain,newchain)
  a=new.index('These are fresh computations after reading the printed proof.')
  b=new.index(r'\end{enumerate}',a)
  new=new[:a]+new[b:]
 exact('V',p['old'],new,p['id'],p['reason']+' Explicit chain-rule factor and mathematical presentation retained; execution provenance placed in checks.')
for p in json.loads((ROOT/'audit_sign/proposed_patches.json').read_text()):
 exact('II',p['old'],p['new'],p['label']+':'+hashlib.sha256(p['old'].encode()).hexdigest()[:8],p['reason'])
for p in json.loads((ROOT/'audit_corrections/P3F34_proposed_patches.json').read_text()):
 if p['operation']=='replace_statement':
  path=ROOT/'parts/III.body.linked.tex';s=path.read_text();a=s.index(r'\label{night:P3F.34}');a=s.index('\n\n',a)+2;b=s.index(r'\end{theorem}',a)
  exact('III',s[a:b],p['tex']+'\n','P3F34-scope','The receiving theorem and original CSV hypothesis agree in their explicitly coprime sector; state the full noncoprime extension.')
 else:exact('III',p['old'],p['new'],'P3F34-source-relationship','Distinguish exact source scopes by their gcd specialization; remove execution prose from proof.')
exact('III',r'\textbf{Proved; correction to the general-n CSV value.}',r'\textbf{The integral groups for every free cap.}','P3F34-proof-heading','Use the mathematical claim in the proof heading.')
path=ROOT/'analysis/current_audit_integration.json';old=json.loads(path.read_text()) if path.exists() else []
byid={x['id']:x for x in old}
for x in receipt:byid[x['id']]=x
path.write_text(json.dumps(list(byid.values()),indent=2))
print(json.dumps({'newly_applied':len(receipt),'receipts':list(byid)}))
