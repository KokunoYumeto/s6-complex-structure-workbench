"""Keep the refined statements and merge the exact positive-ruled repetition."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
start=s.index(r'\begin{lemma}[The conductor graph at positive Euler number]')
end=s.index(r'\subsection{The excess-one curve calculation and the ordinary-double sector}',start)
old=s[start:end];new=old
rs=new.index(r'\begin{remark}[The positive ruled configuration]')
re_=new.index(r'\end{remark}',rs)+len(r'\end{remark}')
removed=new[rs:re_]
new=new[:rs]+new[re_:]
anchor=r'\StatementRecord{lem:II:positive-ruled-conductor-graph}{proved}{P314}{\cref{night:P4.26,night:P4.35,night:P4R.13}}'
alias=r'''
\hypertarget{tag-P203}{}\label{scope:II:positive-ruled-configuration}
\StatementRecord{scope:II:positive-ruled-configuration}{proved}{P203}{}'''
assert new.count(anchor)==1;new=new.replace(anchor,anchor+alias,1)
a=r'''For the minimal resolved normalization $\rho:T\to S$, the pole
divisor $D$ has horizontal part $2H$, and its reduced support
$A$ is the section $H$ with rational trees attached.
The reduced conductor image'''
b=r'''Write $\rho=\nu\sigma:T\to N\to S$ for the minimal resolved
normalization. Its pole divisor $D$ has horizontal part $2H$,
and $A=D_{\rm red}=\rho^{-1}(C)_{\rm red}$ is the section $H$
with rational trees attached. The inclusion $A\hookrightarrow T$
induces an isomorphism on fundamental groups, and the map
$T\cup_A C\to S$ induced by $\rho$ and $C\hookrightarrow S$
is a homeomorphism. The reduced conductor in $N$ has an acyclic
normalization-incidence graph.
The reduced conductor image'''
assert a in new;new=new.replace(a,b,1)
a=r'''$\pi_1(C)\simeq\pi_1(S)\simeq\mathbb Z$.
\end{lemma}'''
b=r'''$\pi_1(C)\simeq\pi_1(S)\simeq\mathbb Z$. Moreover,
\[
 e(S)=2,\qquad e(S_{\rm reg})=0,\qquad
 \sum_{p\in C}(r_p-1)=2,
\]
where $r_p$ is the number of analytic branches of $C$ at $p$.
\end{lemma}'''
assert a in new;new=new.replace(a,b,1)
a=r'''with $(X,Y,A,C,h)=(T,S,A,C,\rho)$, using a compatible analytic
triangulation. It gives the isomorphism induced by $C\hookrightarrow S$;'''
b=r'''with $(X,Y,A,C,h)=(T,S,A,C,\rho)$, using a compatible analytic
triangulation. Its quotient map is exactly the displayed
homeomorphism $T\cup_A C\to S$. It gives the isomorphism induced by $C\hookrightarrow S$;'''
assert a in new;new=new.replace(a,b,1)
a=r'''$c=1$, since $b=1$. Hence $c=2$, proving all the assertions.'''
b=r'''$c=1$, since $b=1$. Hence $c=2$. The inequalities already proved
give $2=e(C)\le e(S)\le2$, so $e(S)=2$ and $e(S_{\rm reg})=0$.
The same normalization-incidence formula is
$b=1-c+\sum_p(r_p-1)$; substitution of $b=1,c=2$ gives the
last displayed equality. These are the maps of the positive
ruled configuration with $D_T=A$ and $D_N=\sigma(A)_{\rm red}$.'''
assert a in new;new=new.replace(a,b,1)
apply_edit(old,new,'II-C3-POSITIVE-RULED-SINGLE-OWNER',['D12','D14','D25'],
 'lem:II:positive-ruled-conductor-graph; scope:II:positive-ruled-configuration; night:P4.51',
 'Complete local-intersection-forms subsection',
 'The complete P203 remark repeats the same T,N,S, sigma, nu, conductor inverse image and pushout. Transfer its homeomorphism, acyclic graph and final Euler/branch equalities into P314 with D_T=A and D_N=sigma(A)_red; retain its permanent tag and label as aliases. The full P4.51 statement and proof remain byte-identical.',
 'Root read complete current P314/P4.51/P203 before the edit and every receiving addition; the earlier refined-consumer package records the complete original/receiving comparisons. All original P203 content is retained verbatim in this defect row, and every mathematical conclusion has its displayed map and proof.')

anchor=r'\begin{example}[A compact fibration with three doubled nodal supports]'
apply_edit(anchor,r'\subsection{Three doubled nodal supports}'+'\n\n'+anchor,
 'II-C3-ELLIPTIC-EXAMPLE-UNIT',['D14'],'ii:three-doubled-nodal-fibres','Subsection boundary before compact example',
 'Give the complete compact construction its own mathematical unit. Its entire statement and proof remain unchanged and all unreviewed local rows remain open; the boundary alone earns no movement credit.')
path=ROOT/'S6_SERIES_PUBLISH_unit_progress.tsv';fields,rows=read_tsv(path)
oldunit='night:P4R.13';oldrows=[r for r in rows if r['paper']=='II' and r['unit_id']==oldunit]
assert len(oldrows)==26
assert not any(r['paper']=='II' and r['unit_id']=='ii:three-doubled-nodal-fibres' for r in rows)
for prior in oldrows:
    item=dict(prior);item.update(unit_id='ii:three-doubled-nodal-fibres',unit_title='Three doubled nodal supports',
      status='done' if prior['defect_type'] in ['D10','D16'] else 'open',date_utc=now(),
      evidence='code/S6_SERIES_PUBLISH_c3_refined_unit_owners.py',
      detail='The unchanged complete compact example is a separate open unit. No unit-subdivision or reading credit.')
    rows.append(item)
write_tsv(path,fields,rows)
for unit,event in [('night:P4R.13','II-C3-ROOT-ELLIPTIC-CONDUCTOR-UNIT'),('night:P4.51','II-C3-ROOT-POSITIVE-RULED-UNIT')]:
    add_event(unit,event,'used and rechecked in this run',
      ('Root read the entire current P313/R13 unit and the exact separation of the following untouched example. All refined R13 statement bytes are retained. The read includes the rational-resolution conductor square, finite double cover and branch-coordinate maps, three reduced-horizontal component maps, same primary quotient and Euler comparison, all A2/A3/D4 jet transitions and product coordinates, exclusion of attached curves, and minimality. The complete old/receiving R13 comparison is also recorded by the refined-consumer agent. The compact example remains fully open.' if unit=='night:P4R.13' else
       'Root read the entire current P314/P4.51/P203 unit and the exact combined receiving guard. The old P203 hypotheses and every conclusion map to the identical rho=nu sigma, A=D_T, D_N=sigma(A)_red, and proper conductor pushout. The Euler and branch-count substitutions are printed in P314. Full P4.51 is unchanged, including the curve-selection gradient estimate, unit flow, covering lift, exterior-square map and intersection signs. The refined agent comparison supplies its complete old/receiving proof read.')+
       ' All local defect classes were reviewed; final placement, bibliography-wide verification and final rendered pages remain open. No independent proof or final-page credit.',
      'S6_SERIES_PUBLISH_II.tex: complete refined-conductor unit',source=__file__)
    for number in range(1,26):
        kind=f'D{number:02}'
        if kind in ['D10','D16']:continue
        status='open' if kind in ['D14','D18','D23'] else 'done'
        set_unit_status(unit,kind,status,
          'Complete current unit read; remaining whole-paper placement, bibliography or final-render task.' if status=='open' else
          'Complete current mathematical unit read for this defect class; every identified instance is recorded and no local residue found.',
          'CHECK_EVENTS.tsv: '+event)
print('P203 conclusions have one full owner; P205 is separately open. R13 and P4.51 local receiving reads recorded.')
