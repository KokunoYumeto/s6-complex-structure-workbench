from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p=R/'parts/V.body.linked.tex';s=p.read_text();receipt=[]
def rep(old,new,key):
 global s
 if new in s:return
 assert s.count(old)==1,(key,s.count(old));s=s.replace(old,new,1);receipt.append({'id':key,'old':old,'new':new})
rep(r'''\lambda=u^4,\quad D_0=\operatorname{diag}(1,u^6,u^3,1,u^{-3},u^{-6}),
 \qquad
 \lambda=u^{-5},\quad D_\infty=
 \operatorname{diag}(1,u^{-8},u^{-4},1,u^4,u^8).''',r'''\begin{gathered}
 \lambda=u^4,\qquad D_0=\operatorname{diag}(1,u^6,u^3,1,u^{-3},u^{-6}),\\
 \lambda=u^{-5},\qquad D_\infty=
 \operatorname{diag}(1,u^{-8},u^{-4},1,u^4,u^8).
 \end{gathered}\label{layout:V:fresh-gauges}''','V-fresh-gauges')
rep(r'''h_b(\infty)=
 -1.0945402503114027801162682630549457037255332694053308977705\ldots
 \quad(\text{stored midpoint radius}<4\cdot10^{-76}).''',r'''\begin{gathered}
 h_b(\infty)=
 -1.0945402503114027801162682630549457037255332694053308977705\ldots,\\
 \text{stored midpoint radius}<4\cdot10^{-76}.
 \end{gathered}\label{layout:V:fresh-minimum}''','V-fresh-minimum')
rep(r'''-1.094540250311402780116268263054945703726
 <h_b(\infty)
 <-1.094540250311402780116268263054945703725.''',r'''\begin{aligned}
 -1.094540250311402780116268263054945703726&<h_b(\infty),\\
 h_b(\infty)&<-1.094540250311402780116268263054945703725.
 \end{aligned}\label{layout:V:fresh-bounds}''','V-fresh-bounds')
rep(r'''N=B^{-1}A^{-1}-I,\quad N^2=0,\quad\det J=\pm1,\quad
 J^{-1}NJ=\begin{pmatrix}0&I_3\\0&0\end{pmatrix},\quad
 e_J=J^{-1}e_0=(1,0,0,0,0,0)^t.''',r'''\begin{gathered}
 N=B^{-1}A^{-1}-I,\qquad N^2=0,\qquad\det J=\pm1,\\
 J^{-1}NJ=\begin{pmatrix}0&I_3\\0&0\end{pmatrix},\qquad
 e_J=J^{-1}e_0=(1,0,0,0,0,0)^t.
 \end{gathered}\label{layout:V:fresh-marking}''','V-fresh-marking')
rep(r'''-0.1811385443749874439019453406721083768036152044186687798893\ldots
 \quad(\text{stored midpoint radius}<8\cdot10^{-76}),''',r'''\begin{gathered}
 -0.1811385443749874439019453406721083768036152044186687798893\ldots,\\
 \text{stored midpoint radius}<8\cdot10^{-76},
 \end{gathered}\label{layout:V:fresh-splitting}''','V-fresh-splitting')
p.write_text(s)
q=R/'analysis/new_V_layout_repairs.json'
if receipt:q.write_text(json.dumps(receipt,indent=2))
print(json.dumps({'repaired_displays':len(receipt)}))
