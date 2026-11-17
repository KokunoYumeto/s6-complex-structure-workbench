"""Concrete layout-only repairs for the observed III build10 overflows."""
from pathlib import Path
import hashlib,json,re
D=Path(__file__).resolve().parents[2]

def transform(s):
    records=[]
    def change(old,new,why,count=1,qa_anchor=True):
        nonlocal s
        n=s.count(old)
        assert n==count,(why,n,count)
        for i in range(n):
            pos=s.index(old);anchor='qa:III:layout:'+str(len(records)+1) if qa_anchor else None
            # A label at the repaired locus gives an exact final page after
            # later pagination changes; it carries no mathematical assertion.
            replacement=(r'\phantomsection\label{'+anchor+'}\n' if anchor else '')+new
            records.append({'anchor':anchor,'reason':why,'before':old,'after':new,
                            'before_sha256':hashlib.sha256(old.encode()).hexdigest(),
                            'after_sha256':hashlib.sha256(new.encode()).hexdigest(),
                            'mathematical_change':'none; line breaking or command/file typography only'})
            s=s[:pos]+replacement+s[pos+len(old):]

    change(r'''\[
 (\arg t,\arg w_1,\arg w_2)\longleftrightarrow
 (\arg w_0,\arg w_1,\arg w_2),\qquad
 \arg w_0=\arg t-\arg w_1-\arg w_2\pmod{2\pi},
\]''',r'''\[
\begin{gathered}
 (\arg t,\arg w_1,\arg w_2)\longleftrightarrow
 (\arg w_0,\arg w_1,\arg w_2),\\
 \arg w_0=\arg t-\arg w_1-\arg w_2\pmod{2\pi},
\end{gathered}
\]''','4.06342pt angular-coordinate display')
    change(r'''\[
 (P_iq_i)=\bigl((-5,2),(4,0),(1,-2)\bigr),\qquad
 \sum_i z_i\wedge q_i=-3-\frac{16}{3}+\frac14
 =-\frac{97}{12},\qquad
 \sum_{i<j}(P_iq_i)\wedge(P_jq_j)=-8.
\]''',r'''\[
\begin{gathered}
 (P_iq_i)=\bigl((-5,2),(4,0),(1,-2)\bigr),\\
 \sum_i z_i\wedge q_i=-3-\frac{16}{3}+\frac14
 =-\frac{97}{12},\qquad
 \sum_{i<j}(P_iq_i)\wedge(P_jq_j)=-8.
\end{gathered}
\]''','6.14790pt marked junction calculation for50/II')
    change(r'''\[
 (P_iq_i)=\bigl((-2,1),(0,0),(1,0),(1,-1)\bigr),\qquad
 \sum_i z_i\wedge q_i=-\frac12-\frac15-\frac13
 =-\frac{31}{30},\qquad
 \sum_{i<j}(P_iq_i)\wedge(P_jq_j)=-1.
\]''',r'''\[
\begin{gathered}
 (P_iq_i)=\bigl((-2,1),(0,0),(1,0),(1,-1)\bigr),\\
 \sum_i z_i\wedge q_i=-\frac12-\frac15-\frac13
 =-\frac{31}{30},\qquad
 \sum_{i<j}(P_iq_i)\wedge(P_jq_j)=-1.
\end{gathered}
\]''','32.27287pt marked junction calculation for56/II')
    change(r'''\par\medskip\noindent\textbf{Executable certificate.}\quad 
The exact verifier
\texttt{code/invariants\_arithmetic/}
\texttt{certify\_modular\_collision\_realizations.py}''',r'''\par\medskip\noindent\textbf{Executable certificate.}\quad
The exact verifier
\path{code/invariants_arithmetic/certify_modular_collision_realizations.py}''','150.32729pt unbreakable certificate filename')
    change(r'''\begin{equation}
\cdots\longrightarrow H^{j-r}(B;G)
\xrightarrow{\,a\mapsto a\smile e(V)\,}H^j(B;G)
\xrightarrow{\pi_0^*}H^j(E_0;G)
\xrightarrow{\pi_!}H^{j-r+1}(B;G)
\xrightarrow{\,\smile e(V)\,}H^{j+1}(B;G)\longrightarrow\cdots .
\label{courseIII:projective-splitting-for-lesson11:eq:1.1}
\end{equation}''',r'''\begin{equation}
\begin{aligned}
\cdots\longrightarrow H^{j-r}(B;G)
&\xrightarrow{\,a\mapsto a\smile e(V)\,}H^j(B;G)
\xrightarrow{\pi_0^*}H^j(E_0;G)\\
&\xrightarrow{\pi_!}H^{j-r+1}(B;G)
\xrightarrow{\,\smile e(V)\,}H^{j+1}(B;G)\longrightarrow\cdots .
\end{aligned}
\label{courseIII:projective-splitting-for-lesson11:eq:1.1}
\end{equation}''','40.46014pt full Gysin exact sequence')
    change(r'''\begin{equation}
a=-2,\qquad
 \delta(u)=
 \begin{cases}4e^{-1/(1-u^2)},&|u|<1,\\0,&|u|\geq1,\end{cases}
 \qquad h(u)=u+\delta(u),\qquad
 F_b(u,y,z)=h(u)-A(y)+B(z).
 \label{courseIII:creating-an-original-cancelling-handle-pair:eq:1.2}
\end{equation}''',r'''\begin{equation}
\begin{gathered}
a=-2,\qquad
 \delta(u)=
 \begin{cases}4e^{-1/(1-u^2)},&|u|<1,\\0,&|u|\geq1,\end{cases}\\
 h(u)=u+\delta(u),\qquad
 F_b(u,y,z)=h(u)-A(y)+B(z).
\end{gathered}
 \label{courseIII:creating-an-original-cancelling-handle-pair:eq:1.2}
\end{equation}''','22.06790pt explicit handle-creation functions')
    # Repair whole paragraphs so the QA label remains outside inline math.
    m=re.search(r'^Human source context is Kiran Luecke,.*$',s,re.M)
    assert m
    old=m[0];new=old.replace(r'\texttt{2f1cd08cb4f7b7b643eec441eae78637bbb71973}',r'\path{2f1cd08cb4f7b7b643eec441eae78637bbb71973}')
    change(old,new,'19.55638pt source revision identifier')
    m=re.search(r'^The original-author source for this algebraic presentation is Isaksen--Wang--Xu,.*$',s,re.M)
    assert m
    old=m[0];new=old.replace(r'tau\_i and xi\_\{i+1\} correspond to zeta\_i and zeta\_i squared',
        r'\(\tau_i\) and \(\xi_{i+1}\) correspond to \(\zeta_i\) and \(\zeta_i^2\)').replace(r'zeta\_1 of degree one',r'\(\zeta_1\) of degree one')
    new=new.replace('arXiv:2001.04247v1',r'\path{arXiv:2001.04247v1}')
    change(old,new,'2.53334pt literal source-symbol typography')
    # The long integers are data, not prose: retain each integer unchanged
    # and permit breaks only between consecutive list entries.
    p=D/'work/maps_audit/coefficient_h28_complete_certificate.tex'
    raw=p.read_text()
    # The source block is inserted verbatim before the final Uses pass.
    assert raw in s
    fixed=raw.replace(r'\begin{longtable}{l l}',r'\begin{longtable}{@{}p{38mm}p{110mm}@{}}')
    fixed=fixed.replace(r',\ ',r',\allowbreak\ ')
    for weight in range(5):
        oldhead=r'\subparagraph{Weight $'+str(weight)+r'$.}'
        if oldhead in fixed:fixed=fixed.replace(oldhead,oldhead+r'\label{qa:III:coefficient-weight-'+str(weight)+'}')
    change(raw,fixed,'Four coefficient-certificate tables overflowed by99.59400pt or28.41891pt; all exact integers retained')
    old=r'The ordered real complex basis changes from \((v_1,Jv_1,v_2,Jv_2,v_3,Jv_3)\) to \((v_1,-Jv_1,v_2,-Jv_2,v_3,-Jv_3)\), so its orientation changes by \((-1)^3=-1\).'
    new=r'''The ordered real complex basis changes as
\[
(v_1,Jv_1,v_2,Jv_2,v_3,Jv_3)
\longmapsto (v_1,-Jv_1,v_2,-Jv_2,v_3,-Jv_3).
\]
Its orientation therefore changes by \((-1)^3=-1\).'''
    change(old,new,'39.49140pt ordered real-basis comparison')
    change(r'''\begin{equation}
 \pi_{12}(S^8)\cong\pi_4^{\mathrm S}=0
 \quad
 \text{\cite[Corollary~4.24, p.~360]{Hatcher2002};
 \cite[Table~1, p.~113]{IsaksenWangXu2023}}.
 \label{wb:cusp-cone-fourth-stable-stem}
\end{equation}''',r'''\begin{equation}
 \pi_{12}(S^8)\cong\pi_4^{\mathrm S}=0.
 \label{wb:cusp-cone-fourth-stable-stem}
\end{equation}
Here we use \cite[Corollary~4.24, p.~360]{Hatcher2002} and
\cite[Table~1, p.~113]{IsaksenWangXu2023}.''','16.68358pt build11 stable-stem equation with two long citations; citations moved to adjacent prose')
    change(r'\subsection{The framed three-torus and the class of $e$}',
        r'\subsection{The framed three-torus and the class of \texorpdfstring{$e$}{e}}',
        'PDF bookmark: preserve the mathematical e and supply its plain-text bookmark')
    change(r'\subsection{The remaining torsion in bidegree \((2,8)\) is zero}',
        r'\subsection{The remaining torsion in bidegree (2,8) is zero}',
        'PDF bookmark: ordinary numerals require no math-mode delimiters')
    change(r'\subsection{Finiteness of the original stable homology of \(H\)}',
        r'\subsection{Finiteness of the original stable homology of \texorpdfstring{\(H\)}{H}}',
        'PDF bookmark: preserve H and supply its plain-text bookmark')
    change(r'{u_\alpha\choose2}',r'\binom{u_\alpha}{2}',
        'Equivalent amsmath binomial command, replacing the legacy atopwithdelims expansion',qa_anchor=False)
    (D/'records/III_layout_repairs_build10.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    return s
