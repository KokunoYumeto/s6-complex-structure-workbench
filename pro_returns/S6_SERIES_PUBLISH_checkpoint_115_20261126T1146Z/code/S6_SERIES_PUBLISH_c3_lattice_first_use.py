"""Complete receiving comparison and place the lattice proof at first use."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text(); i=s.index(r'\label{night:P4R.17}'); a=s.rfind(r'\begin{proposition}',0,i); b=s.index(r'\end{proof}',i)+len(r'\end{proof}'); old=s[a:b]
new=old.replace(r'\delta\eqref{eq:II:nonordinary-triple-c}',r'\delta(C)')
new=re.sub(r'(\\begin\{equation\}\\label\{eq:II:nonordinary-triple-[a-m]\})\n\n',r'\1\n',new)
assert old.count(r'\delta\eqref{eq:II:nonordinary-triple-c}')==2
apply_edit(old,new,'II-C3-NONORDINARY-RECEIVING-TYPOGRAPHY',['D23','D25'],'night:P4R.17','Complete receiving comparison',
 'Actual receiving-text reading found two delta(C) arguments caught by the manual-equation reference conversion. Restore exactly delta(C), and remove empty paragraphs at the start of the thirteen equation environments. All thirteen intended equation references and labels remain.')

s=SOURCE.read_text(); i=s.index(r'\label{lem:II:rank-one-conormal-lattice}'); a=s.rfind(r'\begin{lemma}',0,i); b=s.index(r'\end{proof}',i)+len(r'\end{proof}'); lemma=s[a:b]+'\n\n'
anchor=r'\begin{proposition}[Euler characteristic of a tacnodal conductor]'
assert s.count(lemma)==1 and s.count(anchor)==1
new=s.replace(lemma,'',1).replace(anchor,lemma+anchor,1)
preserve_identifiers(s,new)
SOURCE.write_text(new,newline='\n')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[{'change_id':'II-C3-LATTICE-AT-FIRST-USE-01','type':'D12','statement_id':'lem:II:rank-one-conormal-lattice; night:P4R.10','old_location':'Before night:P4.42','old_page':'working source','new_location':'Before night:P4R.10','new_page':'integrated build pending','old_text':lemma,'new_text':lemma,'reason':'Move the single unchanged lattice lemma before the first existing tacnodal application, then replace that repeated lattice calculation by its exact inclusion and quotient maps.','review_status':'Complete old R10, shared proof and receiving R10 read by root; same-run comparison.'}],'change_id')
s=SOURCE.read_text(); i=s.index(r'\label{night:P4R.10}'); a=s.rfind(r'\begin{proposition}',0,i); b=s.index(r'\end{proof}',i)+len(r'\end{proof}'); old=s[a:b]; new=old
a=new.index('Let $a_p='); b=new.index(r'\item Now suppose the embedding dimension is two.',a)
new=new[:a]+r'''Apply the column clause and its exact sequence in
\cref{lem:II:rank-one-conormal-lattice} to $E=E_0\subset K$,
the same saturated Hessian line $L$, $d=d_p$ and $\beta=b_p$.
The Hessian columns are differentials of first derivatives of $f$,
which belong to $P$; their images consequently lie in $E_0$.
Writing $a_p=\operatorname{length}(L/(E_0\cap L))_p$, the lemma
gives $d_p\ge a_p$ and $a_p+b_p=\tau_p$. Hence
\[
 \frac{d_p}{2}+b_p\ge\frac{a_p}{2}+b_p
 \ge\frac{\tau_p}{2}\ge m>m-1=r_p.
\]

'''+new[b:]
a=new.index('Write the primitive generator of $L$ as');b=new.index(r'\item We conclude that',a)
new=new[:a]+r'''The displayed tensor lies in $\operatorname{Sym}^2E_0$.
Apply the symmetric-square clause of
\cref{lem:II:rank-one-conormal-lattice} to this same lattice,
whose elementary-divisor orders are $(0,a)$, with $d=d_p$
and $\beta=b_p$. It gives
\[
 d_p/2+b_p\ge a\ge m>m-1=r_p.
\]
Together with the nonplanar calculation this proves the
claimed local inequality at every singular curve point.

'''+new[b:]
apply_edit(old,new,'II-C3-TACNODAL-CONDUCTOR-LATTICE-TRANSFER',['D12'],'night:P4R.10','Complete existing tacnodal conductor proof',
 'Transfer exactly the duplicated primitive-line column proof and its two planar coordinate cases to the unchanged P259 now preceding this proposition. Identify E0, L, d_p, b_p, tau_p and the planar elementary-divisor orders (0,a); preserve the original strict local inequalities, full conductor exact sequences, Riemann--Roch calculation and explicit final Hessian examples.')
add_event('night:P4R.10; night:P4R.17; lem:II:rank-one-conormal-lattice','II-C3-ROOT-LATTICE-FIRST-USE-RECEIVING','used and rechecked in this run',
 'Root read complete old and receiving R10, the full shared lemma and full receiving R17. The actual receiving comparison corrected two accidental delta(C) reference conversions before any build. The unchanged lattice lemma is now before its first application; both R10 clause substitutions name exactly the same lattice, primitive line and quotient. All original conclusions and local lower bounds remain. No independent check or page-reading credit.',
 'S6_SERIES_PUBLISH_II.tex: R10/P259/R17',source=__file__)
print('Receiving delta(C) restored; P259 moved to first use and R10 duplication transferred.')
