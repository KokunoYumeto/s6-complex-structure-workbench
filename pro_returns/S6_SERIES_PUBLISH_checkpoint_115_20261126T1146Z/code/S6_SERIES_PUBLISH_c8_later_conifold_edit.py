#!/usr/bin/env python3
"""Whole-read conifold publication edits; exact local changes and guards."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
from collections import Counter
import csv,difflib,re,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation8_iii_later'
PATH=ROOT/'agents/continuation8_iii_integration/units/later/conifold_constructions.tex'
old=PATH.read_text()
assert sha256(old.encode()).hexdigest()=='fa629c3079a3b45fff032cfc7a9b811cb0259597439acfdf8105fd840cc8912b'
new=old
changes=[]

def record(kind,sid,before,after,reason,pos,new_location='same result and complete proof'):
    changes.append(dict(type=kind,statement_id=sid,
      old_location='conifold_constructions.tex sequential edit line '+str(new[:pos].count('\n')+1),
      old_page='pending final concordance',new_location=new_location,
      new_page='pending final build',old_text=before,new_text=after,reason=reason,
      review_status='whole repaired proofs and admitted comparisons read; final readback pending'))

def edit(before,after,kind,reason,sid,count=1):
    global new
    assert new.count(before)==count,(before,new.count(before),count)
    for match in re.finditer(re.escape(before),new):
        record(kind,sid,before,after,reason,match.start())
    new=new.replace(before,after)

edit('\\subsection{Moving the zero of the linearization}\n\\section{Short receiving applications of the cited classification theorems}\n\n\n',
     '\\section{Conifold smoothings and transverse pullbacks}\n\\subsection{Moving the zero of the linearization}\n\n',
     'D14/D16','Place the section before its subsection and replace the production title with the mathematical subjects.','maps:src:D.3.1')

# The full M1 block is moved unchanged before M2, its actual consumer.
a=new.index('\\begin{theorem}[Topology of the smooth conifold fibre]')
b=new.index('\\end{proof}',a)+len('\\end{proof}')
block=new[a:b]
record('D14','maps:src:D.3.2',block,block,
       'Move the entire unchanged topology theorem and proof before the complex-invariants theorem, whose divisor argument uses its H1/H2 vanishing. The inverse relocation restores this exact block to its old position.',a,
       'immediately before maps:src:D.3.3')
new=new[:a]+new[b:]
at=new.index('\\begin{theorem}[Complex invariants of the smoothing]')
new=new[:at]+block+'\n\n'+new[at:]

for target in ['maps:src:D.3.2','maps:src:D.3.4']:
    text='The complete credited statement and re-derivation are in \\cref{'+target+'}.\n'
    edit(text,'','D01/D07',
      'Remove the orphan production pointer; the complete formal result is placed in dependency order and its mathematical uses retain permanent references.',target)

literature="Engel's general zero/pole construction is stated in \\cite[Remark~8.5]{manEngel26}; his Remark~8.1 concerns the separate degeneration as $u$ tends to zero. The full moving-section plumbing and its geometric comparisons are proved above.\n"
edit(literature,'','D08/D18',
     'Move the two exact primary locators to the corresponding construction and boundary arguments; remove the orphan retrospective proof summary.','maps:src:D.3.1')
edit('pp.~5--7]{manEngel26}; the cusp compactification is described in',
     'pp.~5--7]{manEngel26}; see also the zero/pole construction in\n\\cite[Remark~8.5, p.~24]{manEngel26}. The cusp compactification is described in',
     'D18','Place the established exact zero/pole source locator at its construction use.','maps:src:D.3.1')
edit('giving the pinched projective bundle described above.\n\\end{proof}',
     'giving the pinched projective bundle described above\n\\cite[Remark~8.1, p.~22]{manEngel26}.\n\\end{proof}',
     'D18','Place the existing scale-boundary citation at the actual u=0 equation.','maps:src:D.3.1')

edit('holomorphic family $\\mathcal Y_u\\to\\Delta_s$, with a holomorphic\nmap to $\\mathbb P^1$. Its finite fillings have the same',
     'holomorphic family $\\mathcal Y_u\\to\\Delta_s$, with a holomorphic\nmap to $\\mathbb P^1$. Its joint map to $\\mathbb P^1\\times\\Delta_s$\nis also proper and flat. Its finite fillings have the same',
     'D13','State the joint properness and flatness already proved in full in the admitted proof; no parameter or hypothesis change.','maps:src:D.3.1')

headings=[('maps:src:D.3.2','Topology of the smooth conifold fibre','Topology of the smoothing'),
          ('maps:src:D.3.3','Complex invariants of the smoothing','Complex invariants of the smoothing'),
          ('maps:src:D.3.4','Comparison with Calabi--Eckmann deformations','Comparison with Calabi--Eckmann deformations')]
for sid,title,heading in headings:
    env='proposition' if sid.endswith('.4') else 'theorem'
    token='\\begin{'+env+'}['+title+']'
    edit(token,'\\subsection{'+heading+'}\n'+token,'D14/D16',
         'Place the sole complete statement and proof in its actual mathematical subsection.',sid)

for tag,number in [('02M0','1'),('02M1','2'),('02M2','3'),('02M3','4')]:
    token='\\hypertarget{tag-'+tag+'}{}\\label{maps:src:D.3.'+number+'}'
    edit(token,token+'\n{\\normalfont\\scriptsize tag '+tag+'}\\par',
         'D10','Print the existing permanent tag once without a production statement record.','maps:src:D.3.'+number)

edit('$g:Y_{u,s}\\to B$ be the above map and',
     '$g:Y_{u,s}\\to B=\\mathbb P^1$ be the map of\n\\cref{maps:src:D.3.1}, and',
     'D04/D11','Identify the base and exact family owner within the statement.','maps:src:D.3.3')
for title in ['The canonical form.','Meromorphic functions.','Structure-sheaf cohomology.']:
    edit('\\emph{'+title+'}','\\paragraph{'+title+'}',
         'D16','Use a mathematical proof paragraph below the actual subsection.','maps:src:D.3.3')

edit('\\begin{theorem}[Credited re-derivation: transverse pullback and the trivial case]',
     '\\subsection{Transverse pullbacks of the sphere fibration}\n\\begin{theorem}[Transverse pullbacks and products]',
     'D07/D14/D16','Give the actual pullback theorem its own mathematical subsection and title.','maps:src:E.2.2')
edit('\\StatementRecord{maps:src:E.2.2}{proved}{02MK}{the definitions and constructions stated in the proof}',
     '{\\normalfont\\scriptsize tag 02MK}\\par',
     'D07/D10','Replace production metadata by the existing visible tag.','maps:src:E.2.2')
edit('Let $Y$ be a compact complex manifold and $h:Y\\to B$ a holomorphic\nmap which is a submersion at every point over $p_0,p_1,p_2$.',
     'Let $f:X\\to B$ be the original sphere fibration of\n\\cref{maps:src:B.2.1}, with exceptional values $p_0,p_1,p_2$\nas in \\cref{mapsIII:def:marked-family}. Let $Y$ be a compact\ncomplex manifold and $h:Y\\to B$ a holomorphic map which is a\nsubmersion at every point over these three values.',
     'D04/D11','Make the pre-existing fixed X/f/B data explicit through their earlier owners; retain the same three critical values and transversality domain.','maps:src:E.2.2')
edit('$\\dim_{\\mathbb C}Y+2$.  If $Y=B\\times N$ with its projection,',
     '$\\dim_{\\mathbb C}Y+2$. For $Y=B\\times N$ with its projection,',
     'D08','State the existing product specialization directly.','maps:src:E.2.2')
edit('\\chi(P)=2\\chi(N).\n \\tag{E.15}\\hypertarget{tag-029L}{}\\label{maps:eq:E.15}\n\\]',
     '\\chi(P)=2\\chi(N).\n \\hypertarget{tag-029L}{}\\label{maps:eq:E.15}\n\\end{equation}',
     'D19','Retain the permanent equation identities and mathematical body while replacing the manual number by the common counter.','maps:src:E.2.2')
edit('S^6\\times N$, and\n\\[','S^6\\times N$, and\n\\begin{equation}',
     'D19','Open the automatic equation environment corresponding to the retained E.15 identities.','maps:src:E.2.2')

a=new.index('\\begin{proof}',new.index('\\label{maps:src:E.2.2}'))
b=new.index('\\end{proof}',a)+len('\\end{proof}')
mk_old=new[a:b]
mk_new=r'''\begin{proof}
The pullback is the inverse image of the diagonal under
\((f,h):X\times Y\to B\times B\). At a point of this inverse
image, either \(df\) is onto, or the common base value is one
of the three exceptional values and \(dh\) is onto. Hence
\(df-dh:T_xX\oplus T_yY\to T_{f(x)}B\) is onto.
The holomorphic implicit-function theorem gives a complex
submanifold of dimension \(3+\dim_{\mathbb C}Y-1\).
It is closed in the compact product, hence compact.

For the projection \(B\times N\to B\), the mutually inverse
holomorphic maps are
\[
 (x,(t,n))\longmapsto(x,n),\qquad
 (x,n)\longmapsto(x,(f(x),n)).
\]
Choose the diffeomorphism \(\sigma:X\to S^6\) from the sphere
construction. The smooth product map is
\((x,n)\mapsto(\sigma(x),n)\), with inverse
\((v,n)\mapsto(\sigma^{-1}(v),n)\).

The integral K\"unneth map has no Tor terms because
\(H_*(X;\mathbb Z)=H_*(S^6;\mathbb Z)\) is free. Its map
for the displayed direct sum and its inverse are
\[
 (a,b)\longmapsto[x_0]\times a+[X]\times b,\qquad
 c\longmapsto\bigl((\operatorname{pr}_N)_*c,
  (\operatorname{pr}_N)_*(\operatorname{pr}_X^*\omega\frown c)\bigr),
\]
where \(x_0\in X\) and \(\omega\in H^6(X;\mathbb Z)\)
satisfies \(\langle\omega,[X]\rangle=1\). The two composites
are the identity on the K\"unneth summands. Projection to N
and the section \(n\mapsto(x_0,n)\) induce inverse fundamental
group maps, since \(\pi_1(X)=0\). The Euler characteristic of
the product is \(\chi(X)\chi(N)=2\chi(N)\).
\end{proof}'''
edit(mk_old,mk_new,'D08/D20/D22',
     'Retain the complete transversality and product proof, remove its one-item machine list, and display the actual smooth, homology and fundamental-group maps and inverses. No new theorem scope.','maps:src:E.2.2')
edit('\\end{proof}\n\\clearpage\n','\\end{proof}\n','D23',
     'Remove the forced page break from the fragment; final pagination is root-owned.','maps:src:E.2.2')

for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}']:
    assert Counter(re.findall(pattern,old))==Counter(re.findall(pattern,new))
assert len(re.findall(r'\\begin\{proof\}',new))==5
assert len(re.findall(r'\\end\{proof\}',new))==5
assert new.index('\\label{maps:src:D.3.1}')<new.index('\\label{maps:src:D.3.2}')<new.index('\\label{maps:src:D.3.3}')<new.index('\\label{maps:src:D.3.4}')
assert '\\StatementRecord' not in new and '\\tag{' not in new

fields=['change_id','type','statement_id','old_location','old_page',
        'new_location','new_page','old_text','new_text','reason','review_status']
for i,row in enumerate(changes,1):row['change_id']='c8-III-conifold-'+str(i).zfill(3)
with (OUT/'S6_SERIES_PUBLISH_III_conifold_publication_defects.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(changes)
diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='conifold_repaired_input',tofile='conifold_publication_v001'))
(OUT/'S6_SERIES_PUBLISH_III_conifold_publication_v001.diff').write_text(diff)
PATH.write_text(new)
print('EDITED_UTC',datetime.now(timezone.utc).isoformat())
print('SOURCE_LINES',len(new.splitlines()),'SHA256',sha256(new.encode()).hexdigest())
print('EXACT_LOCAL_EDITS',len(changes),'NEW_IDENTITIES',0)
print('ALL_EXISTING_LABEL_TARGET_MULTIPLICITIES_RETAINED; FIVE_COMPLETE_PROOFS')
print('NO_CANONICAL_OR_SHARED_LEDGER_WRITES; FINAL_WHOLE_READBACK_PENDING')
