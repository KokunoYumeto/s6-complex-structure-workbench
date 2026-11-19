"""Pure layout changes justified by the actual cp27 preview overflow log."""
layout_records=[]
def layout_replace(old,new):
 global s
 n=s.count(old)
 assert n,('Layout source absent',old[:100])
 s=s.replace(old,new)
 layout_records.append({'old':old,'new':new,'occurrences':n})
# The sole occurrence moved with the complete F19/F20 rederivation into
# the research archive when their known conclusions became citations.
if r'\texttt{other\_family\_checks.py}' in s:
 layout_replace(r'\texttt{other\_family\_checks.py}',r'\path{other_family_checks.py}')
layout_replace(r'(\columnwidth - 4\tabcolsep)',r'(\linewidth - 4\tabcolsep)')
if r'(\columnwidth - 8\tabcolsep)' in s:
 layout_replace(r'(\columnwidth - 8\tabcolsep)',r'(\linewidth - 8\tabcolsep)')
layout_replace(r''' C_4=\mathbb Z,\ C_3=\mathbb Z^2,\ C_2=\operatorname{NS}(S),
 \ C_1=\mathbb Z^9,\ C_0=\mathbb Z,\qquad
 d_4=(1,1)^t,\quad d_2=L^tB,\quad d_3=d_1=0.''',
 r'''\begin{gathered}
 C_4=\mathbb Z,\quad C_3=\mathbb Z^2,\quad C_2=\operatorname{NS}(S),\\
 C_1=\mathbb Z^9,\quad C_0=\mathbb Z,\\
 d_4=(1,1)^t,\quad d_2=L^tB,\quad d_3=d_1=0.
\end{gathered}''')
layout_replace(r''' W_0=s_0t/u_P,\quad Z_0=u_Gs_1w,\quad
 V_0=E_+^2s_0/s_1^2,\quad
 Q=q_1q_2u_Q,\quad P=u_P/q_2,\quad u_G=u_Qu_P .''',
 r'''\begin{gathered}
 W_0=s_0t/u_P,\quad Z_0=u_Gs_1w,\quad V_0=E_+^2s_0/s_1^2,\\
 Q=q_1q_2u_Q,\quad P=u_P/q_2,\quad u_G=u_Qu_P .
\end{gathered}''')
layout_replace(r''' h:(Z,V)\longmapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\longmapsto(gZ,q\eta V),\qquad
 \operatorname{wind}(\kappa,\alpha,g,\eta)=(1,-a,b,-2),''',
 r'''\begin{gathered}
 h:(Z,V)\longmapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\longmapsto(gZ,q\eta V),\\
 \operatorname{wind}(\kappa,\alpha,g,\eta)=(1,-a,b,-2).
\end{gathered}''')
layout_replace(r''' (k_M,\ell_M)=(-6-18j(j-1),0),\quad
 A_M=-1-3j(j-1),\quad(m_{\rm native},n_{\rm native})
       =(0,-6-18j(j-1)).''',
 r'''\begin{gathered}
 (k_M,\ell_M)=(-6-18j(j-1),0),\quad A_M=-1-3j(j-1),\\
 (m_{\rm native},n_{\rm native})=(0,-6-18j(j-1)).
\end{gathered}''')
layout_replace(r''' y^2=x^3+r x^2+t x+t^2,\quad G=(0,t),\quad
 s=\tfrac14-r,\quad U=y-t-x/2,\quad
 f_2=\frac U{x-s},\quad T(p)=p-G.''',
 r'''\begin{gathered}
 y^2=x^3+r x^2+t x+t^2,\quad G=(0,t),\quad s=\tfrac14-r,\\
 U=y-t-x/2,\quad f_2=\frac U{x-s},\quad T(p)=p-G.
\end{gathered}''')
layout_replace(r''' X_{\rm orig}=\epsilon^{-2/3}X_{\rm new},\quad
 Y_{\rm orig}=\epsilon^{-1}Y_{\rm new},\qquad
 X_{\rm new}=\eta^{2l}U,\quad Y_{\rm new}=\eta^{3l}V,
 \quad (X_{\rm orig},Y_{\rm orig})=(U,V).''',
 r'''\begin{gathered}
 X_{\rm orig}=\epsilon^{-2/3}X_{\rm new},\quad
 Y_{\rm orig}=\epsilon^{-1}Y_{\rm new},\\
 X_{\rm new}=\eta^{2l}U,\quad Y_{\rm new}=\eta^{3l}V,\qquad
 (X_{\rm orig},Y_{\rm orig})=(U,V).
\end{gathered}''')
layout_replace(r'''\begin{split}
 d^0(a,b_0,b_1,z)={}&((A_1-I)a,(A_2-I)a,
 (A_1-I)b_0,(A_2-I)b_1,a-b_0,a-b_1,a-Jz),\\
 d^1(p,q,r,s,u_0,u_1,w)={}&(KN_1r,LN_2s,
 p-r-(A_1-I)u_0,q-s-(A_2-I)u_1,\\
 &\hspace{30mm}-A_0p-A_0A_1q-(A_0-I)w).
\end{split}''',
 r'''\begin{aligned}
 d^0(a,b_0,b_1,z)={}&((A_1-I)a,(A_2-I)a,
 (A_1-I)b_0,(A_2-I)b_1,\\
 &\qquad a-b_0,a-b_1,a-Jz),\\
 d^1(p,q,r,s,u_0,u_1,w)={}&(KN_1r,LN_2s,p-r-(A_1-I)u_0,\\
 &\qquad q-s-(A_2-I)u_1,\\
 &\qquad -A_0p-A_0A_1q-(A_0-I)w).
\end{aligned}''')
layout_replace(r''' e(II)=2,\quad e(III)=3,\quad e(IV)=4,\quad
 e(I_1^*)=7,\quad e(IV^*)=8,\quad e(III^*)=9,
 \quad e(I_2)=2.''',
 r'''\begin{gathered}
 e(II)=2,\quad e(III)=3,\quad e(IV)=4,\quad e(I_1^*)=7,\\
 e(IV^*)=8,\quad e(III^*)=9,\quad e(I_2)=2.
\end{gathered}''')
layout_replace(r''' 0\le x\le L=s+rc,\qquad f(x)\le y\le f(x)+s,\quad
 f(x)=0\ (x\le s),\quad f(x)=(d/c)(x-s)\ (x\ge s).''',
 r'''\begin{gathered}
 0\le x\le L=s+rc,\qquad f(x)\le y\le f(x)+s,\\
 f(x)=0\ (x\le s),\qquad f(x)=(d/c)(x-s)\ (x\ge s).
\end{gathered}''')
layout_replace(r''' Q_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 Q_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix},\qquad
 Q_2=\begin{pmatrix}1&1\\0&1\end{pmatrix},
 \qquad P'=PQ_i,\qquad i'=(2,2,0)_i.''',
 r'''\begin{gathered}
 Q_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 Q_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix},\qquad
 Q_2=\begin{pmatrix}1&1\\0&1\end{pmatrix},\\
 P'=PQ_i,\qquad i'=(2,2,0)_i.
\end{gathered}''')
layout_replace(r''' k_\alpha=-\sum_\beta\chi_\beta E_{\alpha\beta},\qquad
 \omega=\bar\partial k_\alpha,\qquad
 v(q,\zeta)=\frac1\pi\int\frac{\omega(w,\zeta)}{q-w}\,dA(w),
 \qquad h_{-,\alpha}=h^0_{-,\alpha}+k_\alpha-v.''',
 r'''\begin{gathered}
 k_\alpha=-\sum_\beta\chi_\beta E_{\alpha\beta},\qquad
 \omega=\bar\partial k_\alpha,\\
 v(q,\zeta)=\frac1\pi\int\frac{\omega(w,\zeta)}{q-w}\,dA(w),\qquad
 h_{-,\alpha}=h^0_{-,\alpha}+k_\alpha-v.
\end{gathered}''')
layout_replace(r''' e_1=(0,0,-2A,0),\quad e_2=(0,-B,0,0),\quad
 t_1=2A a_1,\quad t_2=-B a_2,
 \qquad a_1=w,\ a_2=w-\delta.''',
 r'''\begin{gathered}
 e_1=(0,0,-2A,0),\qquad e_2=(0,-B,0,0),\\
 t_1=2A a_1,\quad t_2=-B a_2,\qquad
 a_1=w,\quad a_2=w-\delta.
\end{gathered}''')
if r'\label{night:P3K.106}' in s:
 layout_replace(r''' h:(Z_T,V_T)\mapsto(P^2R Z_T,R^{-3}V_T),\qquad
 B:(Z_T,V_T)\mapsto(P^{-1}Z_T,\lambda R c_q K V_T),
 \quad K=(P/t)^3\eta^6,''',
 r'''\begin{aligned}
 h:(Z_T,V_T)&\mapsto(P^2R Z_T,R^{-3}V_T),\\
 B:(Z_T,V_T)&\mapsto(P^{-1}Z_T,\lambda R c_q K V_T),
 \qquad K=(P/t)^3\eta^6.
\end{aligned}''')
 layout_replace(r''' M_0(r,h)=\begin{pmatrix}r+3h&-h\\6h&r+2h\end{pmatrix},
 \quad M_1(r,h)=\begin{pmatrix}3r&-r\\0&4(r+h)\end{pmatrix},
 \quad M_\infty(r,h)=\begin{pmatrix}7h&2h\\h&r+2h\end{pmatrix}.''',
 r'''\begin{gathered}
 M_0(r,h)=\begin{pmatrix}r+3h&-h\\6h&r+2h\end{pmatrix},\qquad
 M_1(r,h)=\begin{pmatrix}3r&-r\\0&4(r+h)\end{pmatrix},\\
 M_\infty(r,h)=\begin{pmatrix}7h&2h\\h&r+2h\end{pmatrix}.
\end{gathered}''')
if r'\label{night:P3K.107}' in s:
 layout_replace(r'''v2=eta P\^{}\{2j\}Vreg/f\_(P\textsuperscript{2})(Q\^{}jZ). Each end record keeps its source band and
full period word. MP.5--9 identify the point/O module frames with the
actual P\^{}\{-2j\} and P\^{}\{-2j-2\} coefficients and the directed suspension Hom.''',
 r'''\[
 v_2=\eta P^{2j}V_{\rm reg}/f_{P^2}(Q^jZ).
\]
Each end record keeps its source band and full period word.
MP.5--9 identify the point/O module frames with the actual
\(P^{-2j}\) and \(P^{-2j-2}\) coefficients and the directed
suspension Hom.''')
(W/'analysis/IV/layout_repairs.json').write_text(json.dumps(layout_records,indent=2)+'\n')
