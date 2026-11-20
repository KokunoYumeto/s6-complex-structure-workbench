from pathlib import Path
import re,json,hashlib,difflib

P=Path(__file__).resolve().parent
source=P.parent/'parts/IV.body.linked.tex'
original=source.read_text()
patches=[]; details=[]

def block(n):
    start=original.index(r'\begin{theorem}\label{night:P3F.'+str(n)+'}')
    m=re.search(r'\n\\begin\{(?:theorem|lemma)\}\\label\{',original[start+1:])
    return original[start:start+1+m.start()] if m else original[start:]

def fix(n, pairs):
    old=block(n); new=old; changes=[]
    for a,b in pairs:
        count=new.count(a)
        if count==0: raise AssertionError((n,'missing',a))
        new=new.replace(a,b)
        changes.append({'old':a,'new':b,'occurrences_within_row':count})
    assert re.findall(r'\\label\{([^}]+)\}',old)==re.findall(r'\\label\{([^}]+)\}',new)
    assert old!=new
    patches.append({'label':f'night:P3F.{n}','old':old,'new':new,'reason':'Notation-only conversion of literal raw formulas/prose to TeX math; same symbols, coefficients, signs, maps and source assertions. No mathematical status change.'})
    details.append({'label':f'night:P3F.{n}','changes':changes})

def listing(a,b):
    return ('\\begin{lstlisting}\n'+a+'\n\\end{lstlisting}', '\\[\n'+b+'\n\\]')

fix(10,[
 (r'twists\(0,1,-1\)',r'twists \((0,1,-1)\)'),
 ('invariant gamma character',r'invariant \(\gamma\) character'),
 (r'S1\_gamma times the punctured base',r'\(S^1_\gamma\) times the punctured base'),
 listing('(S1_gamma timesDelta_s)/(g,s)->(g+l_j/m_j,zeta_j s).',r'(S^1_\gamma\times\Delta_s)/\bigl\langle(g,s)\longmapsto(g+\ell_j/m_j,\zeta_js)\bigr\rangle.'),
 ('relations are3x=gamma and4y=-gamma; after the cusp solid torus the third isx+y=0.',r'relations are \(3x=\gamma\) and \(4y=-\gamma\); after the cusp solid torus the third is \(x+y=0\).'),
 ('on S3 with weights3,4',r'on \(S^3\) with weights \(3,4\)'),
 ('orders are3,4',r'orders are \(3,4\)'),
 (r'from\(log s\)/\(2pi i\)Pi v\_j',r'from \((\log s)/(2\pi i)\,\Pi v_j\)'),
 ('outer gamma marking',r'outer \(\gamma\) marking'),
 ('actual orbit Y=S5 to the weighted S3',r'actual orbit \(Y=S^5\) to the weighted \(S^3\)'),
 (r'in E\_I1 timesS1\_gamma',r'in \(E_{I_1}\times S^1_\gamma\)'),
 (r'node map(x,y,gamma)-\textgreater(xy,gamma)',r'node map \((x,y,\gamma)\longmapsto(xy,\gamma)\)'),
 ('a value t* different from0,1,infinity',r'a value \(t_*\notin\{0,1,\infty\}\)'),
 (r'b\textsuperscript{3}-a\textsuperscript{4}=1, embedded in S3',r'\(b^3-a^4=1\), embedded in \(S^3\)'),
 listing('(a,b)->(rho^3 a,rho^4 b),\nrho^6|a|^2+rho^8|b|^2=1, rho>0.',r'(a,b)\longmapsto(\rho^3a,\rho^4b),\qquad'+'\n'+r'\rho^6|a|^2+\rho^8|b|^2=1,\quad\rho>0.'),
 (r'of b\textsuperscript{3}-a\textsuperscript{4} on',r'of \(b^3-a^4\) on'),
 ('degree12 map', 'degree-12 map'),
 ('binding value to t*',r'binding value to \(t_*\)'),
 ('a genus3 surface C°',r'a genus-three surface \(C^\circ\)'),
 ('in the weighted S3 intersects this page in12 points',r'in the weighted \(S^3\) intersects this page in twelve points'),
 ('inverse image V0 in Y',r'inverse image \(V_0\) in \(Y\)'),
 ('fibration over C°',r'fibration over \(C^\circ\)'),
 ('hence T3. It need not be S3.',r'hence \(T^3\). It need not be \(S^3\).'),
 ('its gamma image',r'its \(\gamma\) image'),
 ('critical gamma circle',r'critical \(\gamma\) circle'),
 ('The delta circle bundle',r'The \(\delta\)-circle bundle'),
 ('over V0.',r'over \(V_0\).'),
 ('bundle over C°',r'bundle over \(C^\circ\)'),
 (r'gives H\textsuperscript{2}=0',r'gives \(H^2=0\)'),
 ('integer Cech obstruction',r'integer \v{C}ech obstruction'),
 ('class of P, not6P',r'class of \(P\), not \(6P\)'),
 (r'definition M=O\(P-O\)',r'definition \(M=\mathcal O(P-O)\)'),
 ('the u column contains mu while the gamma column contains6mu',r'the \(u\) column contains \(\mu\) while the \(\gamma\) column contains \(6\mu\)'),
 ('supplied by M and',r'supplied by \(M\) and'),
 ("on V0 its Chern class is that of the Jacobian line O(P'-O')",r"on \(V_0\) its Chern class is that of the Jacobian line \(\mathcal O(P'-O')\)"),
 ('restriction to T3',r'restriction to \(T^3\)'),
 ('If u and u+delta g are two lifts, with g in H1(boundary V0;Z), the absolute class of delta g is zero and restriction of the absolute class of u to the boundary is zero.',r'If \(u\) and \(u+\delta g\) are two lifts, with \(g\in H^1(\partial V_0;\mathbb Z)\), the absolute class of \(\delta g\) is zero and the restriction of the absolute class of \(u\) to the boundary is zero.'),
 listing('u cup delta g=delta(i*u cup g)=0,\n(delta g)^2=0.',r'u\smile\delta g=\delta(i^*u\smile g)=0,\qquad(\delta g)^2=0.'),
 ('regular fibre timesD2',r'regular fibre times \(D^2\)'),
 ("with twelve I1 fibres. Its P'-O' line",r"with twelve \(I_1\) fibres. Its \(P'-O'\) line"),
 listing("s_delta=(P'-O')^2=-2chi-2(P'.O')=-2.",r"s_\delta=(P'-O')^2=-2\chi-2(P'\cdot O')=-2."),
 ('section line P, not the square of6P',r'section line \(P\), not the square of \(6P\)'),
 ('product of U1 groups',r'product of \(U(1)\) groups'),
 ('has zero pi3',r'has zero \(\pi_3\)'),
 listing('chi(O of the capped Jacobian)=1,\nsignature(V0)=signature(capped Jacobian)=-8,\np_rel=integral p1(capped Jacobian)=3signature=-24.',r'\begin{aligned}'+'\n'+r'\chi(\mathcal O_{\text{capped Jacobian}})&=1,\\'+'\n'+r'\operatorname{signature}(V_0)&=\operatorname{signature}(\text{capped Jacobian})=-8,\\'+'\n'+r'p_{\rm rel}&=\int_{\text{capped Jacobian}}p_1=3\operatorname{signature}=-24.'+'\n'+r'\end{aligned}'),
 ('neighbourhood T2 timesD2',r'neighbourhood \(T^2\times D^2\)'),
 ('closed T3 boundary',r'closed \(T^3\) boundary')
])

fix(11,[
 listing('A(Phi)=(4k(f)-ell(f))/24.',r'A(\Phi)=\frac{4k(f)-\ell(f)}{24}.'),
 (r'exactly6A\(Phi\)',r'exactly \(6A(\Phi)\)'),
 ('in Z/28 from multiplication by6 in Z/28',r'in \(\mathbb Z/28\) from multiplication by \(6\) in \(\mathbb Z/28\)'),
 (r'E+=O\(1\) direct-sum O\(-1\), trivial as an SU2 bundle',r'\(E_+=\mathcal O(1)\oplus\mathcal O(-1)\), trivial as an \(SU(2)\) bundle'),
 ('loop of SO3 gauge',r'loop of \(SO(3)\) gauge'),
 ('boundary S2 and',r'boundary \(S^2\) and'),
 listing('alpha:S3 -> SO3.',r'\alpha:S^3\longrightarrow SO(3).'),
 (r'replacement S2-meridian timesD3 this comparison is exactly \(x,y\)-\textgreater(alpha(y)x,y)',r'replacement \(S^2\)-meridian times \(D^3\), this comparison is exactly \((x,y)\longmapsto(\alpha(y)x,y)\)'),
 ('Hopf line {[}u{]}',r'Hopf line \([u]\)'),
 ('twist a to an integral power',r'twist \(a\) to an integral power'),
 (r'Map\_*\(S2,SO3\)-\textgreater Map\(S2,SO3\)-\textgreater SO3',r'\(\operatorname{Map}_*(S^2,SO(3))\longrightarrow\operatorname{Map}(S^2,SO(3))\longrightarrow SO(3)\)'),
 (r'pi3\(SO3\) plus pi1\(SO3\)',r'\(\pi_3(SO(3))\oplus\pi_1(SO(3))\)'),
 ('of the S2 variable and extends over the D3',r'of the \(S^2\) variable and extends over \(D^3\)'),
 ('displayed alpha',r'displayed \(\alpha\)'),
 ('fixed S2 also extends by its radial SO3 action on D3',r'fixed \(S^2\) also extends by its radial \(SO(3)\) action on \(D^3\)'),
 ('of Diff+(S2) to SO3',r'of \(\operatorname{Diff}^+(S^2)\) to \(SO(3)\)'),
 (r'Let n\_-,n\_+ be',r'Let \(n_-,n_+\) be'),
 (r'Over S2\_F timesS2\_theta, write h,t',r'Over \(S^2_F\times S^2_\theta\), write \(h,t\)'),
 listing('h-n_- t,      -h+n_+ t.',r'h-n_-t,\qquad -h+n_+t.'),
 (r'c1=\(n_+-n_-\)t and c2=\(n_-+n_+\)h t',r'\(c_1=(n_+-n_-)t\) and \(c_2=(n_-+n_+)ht\)'),
 listing('p1=c1^2-4c2=-4(n_-+n_+)h t.',r'p_1=c_1^2-4c_2=-4(n_-+n_+)ht.'),
 (r'generator alpha normalized by p1=+4, the comparison is -\(n_-+n_+\)a',r'generator \(\alpha\) normalized by \(p_1=+4\), the comparison is \(-(n_-+n_+)a\)'),
 ('alter k and ell',r'alter \(k\) and \(\ell\)'),
 (r'multiple of\(1,4\)',r'multiple of \((1,4)\)'),
 ('leaves A unchanged',r'leaves \(A\) unchanged'),
 ('Jin Theorem4.9, with g=1',r'Jin Theorem 4.9, with \(g=1\)'),
 ('over CP-infinity',r'over \(\mathbb{CP}^{\infty}\)'),
 (r'are\(A,k\)',r'are \((A,k)\)'),
 ('representatives a,b',r'representatives \(a,b\)'),
 ('diffeomorphisms f and g, so the replacement of the composite is fg',r'diffeomorphisms \(f\) and \(g\), so the replacement of the composite is \(fg\)'),
 (r'gives A\(fg\)=A\(f\)+A\(g\)',r'gives \(A(fg)=A(f)+A(g)\)'),
 ('kernel of A in the exact presentation I(S2 timesS3)=Za direct-sum Zb is Za',r'kernel of \(A\) in the exact presentation \(I(S^2\times S^3)=\mathbb Za\oplus\mathbb Zb\) is \(\mathbb Za\)'),
 ('every a-power and extends it over D4 timesS3',r'every \(a\)-power and extends it over \(D^4\times S^3\)')
])

fix(12,[
 ('normalization C has genus3',r'normalization \(C\) has genus three'),
 ('one I12 fibre',r'one \(I_{12}\) fibre'),
 ('translation by6P',r'translation by \(6P\)'),
 (r'Delta\_Q F=gamma-6delta',r'\(\Delta_QF=\gamma-6\delta\)'),
 (r'Let Lambda\_E be',r'Let \(\Lambda_E\) be'),
 ('cusp of C.',r'cusp of \(C\).'),
 listing('A=[[0,1],[-1,-1]], shift4;\nB=[[0,-1],[1,0]], shift-3.',r'A=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},\quad\text{shift }4;\qquad'+'\n'+r'B=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad\text{shift }-3.'),
 listing('G=[A,B]=[[1,-1],[-1,2]],\nG-I=[[0,-1],[-1,1]], det(G-I)=-1.',r'G=[A,B]=\begin{pmatrix}1&-1\\-1&2\end{pmatrix},\quad'+'\n'+r'G-I=\begin{pmatrix}0&-1\\-1&1\end{pmatrix},\quad\det(G-I)=-1.'),
 (r'H0(C minus cusp;Lambda\_E)=0',r'\(H_0(C\setminus\{\text{cusp}\};\Lambda_E)=0\)'),
 ('For C0=C minus an open cusp disc',r'For \(C_0\) equal to \(C\) minus an open cusp disc'),
 (r'H\textsuperscript{2}(C0,boundary;Lambda\_E)',r'\(H^2(C_0,\partial C_0;\Lambda_E)\)'),
 (r'H\textsuperscript{1}(C0;Lambda\_E) to H\textsuperscript{1}(boundary; Lambda\_E)',r'\(H^1(C_0;\Lambda_E)\longrightarrow H^1(\partial C_0;\Lambda_E)\)'),
 (r'an I\_n Tate chart with parameter Q',r'an \(I_n\) Tate chart with parameter \(Q\)'),
 (r'unit a\(Q\)',r'unit \(a(Q)\)'),
 (r'of the I\_n fibre',r'of the \(I_n\) fibre'),
 (r'Locally a\(Q\)',r'Locally \(a(Q)\)'),
 ('contains log Q',r'contains \(\log Q\)'),
 ('through Q=0',r'through \(Q=0\)'),
 listing('0 -> j_*Lambda_E -> L_infty -> A^0 -> 0,',r'0\longrightarrow j_*\Lambda_E\longrightarrow\mathcal L_\infty\longrightarrow\mathcal A^0\longrightarrow0,'),
 (r'where L\_infty is',r'where \(\mathcal L_\infty\) is'),
 ('defect6P',r'defect \(6P\)'),
 ('component: P has',r'component: \(P\) has'),
 ('original I1 fibre',r'original \(I_1\) fibre'),
 ('zero in I12',r'zero in \(I_{12}\)'),
 (r'H\textsuperscript{1}\(C,A^0\)=0',r'\(H^1(C,\mathcal A^0)=0\)'),
 ('local I12 extension',r'local \(I_{12}\) extension'),
 ('fixed I12 resolution',r'fixed \(I_{12}\) resolution'),
 ('over C and',r'over \(C\) and'),
 ('Picard point is P,',r'Picard point is \(P\),'),
 ('components of I12',r'components of \(I_{12}\)'),
 ('source line P-O:',r'source line \(P-O\):'),
 ("by O(P'-O')",r"by \(\mathcal O(P'-O')\)"),
 ('at I12 its unit gluing has product1',r'at \(I_{12}\) its unit gluing has product one'),
 ('At I12 the construction',r'At \(I_{12}\) the construction'),
 (r'node units eta\_i',r'node units \(\eta_i\)'),
 (r'because product eta\_i=1',r'because \(\prod_i\eta_i=1\)'),
 ('smoothly in Q,',r'smoothly in \(Q\),'),
 ('line bundle on C.',r'line bundle on \(C\).'),
 listing("c1(L)=c1(O(P'-O'))+n F       for an integer n.",r"c_1(L)=c_1\bigl(\mathcal O(P'-O')\bigr)+nF,\qquad n\in\mathbb Z."),
 (r"F\textsuperscript{2}=F.(P'-O')=0",r"\(F^2=F\cdot(P'-O')=0\)"),
 ('exactly-2',r'exactly \(-2\)'),
 ('so p1 of the compact sheet pairs to-24',r'so \(p_1\) of the compact sheet pairs to \(-24\)'),
 ('integer n records',r'integer \(n\) records')
])

fix(13,[
 (r'let F\(s,v\)',r'let \(F(s,v)\)'),
 (r'keep gamma\(s,v\)=\(6mu,C-s-12v\)',r'keep \(\gamma(s,v)=(6\mu,C-s-12v)\)'),
 ('for real theta',r'for real \(\theta\)'),
 listing('F(s,v+theta)-F(s,v)\n   = theta gamma(s,v)+6theta(1-theta)delta.       (P3F.13.1)',r'F(s,v+\theta)-F(s,v)=\theta\gamma(s,v)+6\theta(1-\theta)\delta.\tag{P3F.13.1}'),
 ('circle, v=ib+theta',r'circle, \(v=ib+\theta\)'),
 ('the delta direction',r'the \(\delta\) direction'),
 ('equal to1',r'equal to \(1\)'),
 ('the gamma-translation loop',r'the \(\gamma\)-translation loop'),
 ('independent of theta',r'independent of \(\theta\)'),
 (r'Since gamma\(s+12,v\)= gamma\(s,v\)-12delta',r'Since \(\gamma(s+12,v)=\gamma(s,v)-12\delta\)'),
 listing('[F(s+12,v+theta)-F(s+12,v)]\n   -[F(s,v+theta)-F(s,v)]=-12theta delta.        (P3F.13.2)',r'\begin{aligned}'+'\n'+r'&[F(s+12,v+\theta)-F(s+12,v)]\\'+'\n'+r'&\qquad-[F(s,v+\theta)-F(s,v)]=-12\theta\delta.'+'\n'+r'\end{aligned}\tag{P3F.13.2}'),
 ('on the Q deck by the unitary gauge exp(-24pi i theta) in the exp(2pi i zeta2) convention, of winding-12',r'on the \(Q\)-deck by the unitary gauge \(\exp(-24\pi i\theta)\) in the \(\exp(2\pi i\zeta_2)\) convention, of winding \(-12\)'),
 listing('X=Qz, r=zY;          Q=Xw, Y=wr.',r'X=Qz,\quad r=zY;\qquad Q=Xw,\quad Y=wr.'),
 ('At a node Q=uv of the resolved source I12 surface the remaining chart uv=Xw',r'At a node \(Q=uv\) of the resolved source \(I_{12}\) surface the remaining chart \(uv=Xw\)'),
 listing('X=uk, v=kw;          u=Xk, w=kv.',r'X=uk,\quad v=kw;\qquad u=Xk,\quad w=kv.'),
 (r'product S2 bundle with Euler class u+c1\(L\)',r'product \(S^2\) bundle with Euler class \(u+c_1(L)\)'),
 ('has K=5F',r'has \(K=5F\)')
])

fix(14,[
 ('Let S be',r'Let \(S\) be'),
 (r'let L\_+,L\_- be',r'let \(L_+,L_-\) be'),
 ('weights+1,-1',r'weights \(+1,-1\)'),
 (r'B=P(L\_+ direct-sum conjugate(L\_-))',r'\(B=\mathbb P(L_+\oplus\overline{L_-})\)'),
 ('Euler class x has integral1',r'Euler class \(x\) has integral \(1\)'),
 listing('pi_*(x)=1, pi_*(x^2)=a-b,\npi_*(x^3)=a^2-ab+b^2,\np1(TB)=pi^*(p1(TS)+(a+b)^2).',r'\begin{aligned}'+'\n'+r'\pi_*(x)&=1,&\pi_*(x^2)&=a-b,\\'+'\n'+r'\pi_*(x^3)&=a^2-ab+b^2,&p_1(TB)&=\pi^*\bigl(p_1(TS)+(a+b)^2\bigr).'+'\n'+r'\end{aligned}'),
 ('with roots a,-b',r'with roots \(a,-b\)'),
 listing('integral_B exp(D/2) exp(x) Ahat(TB).',r'\int_B e^{D/2}e^x\widehat A(TB).'),
 listing('(3d^2-p1(TS))/24 + (a^2+ad)/2\n   = chi(O_S)+(a^2-a.K_S)/2\n   = chi(S,L_+).',r'\begin{aligned}'+'\n'+r'\frac{3d^2-p_1(TS)}{24}+\frac{a^2+ad}{2}'+'\n'+r'&=\chi(\mathcal O_S)+\frac{a^2-a\cdot K_S}{2}\\'+'\n'+r'&=\chi(S,L_+).'+'\n'+r'\end{aligned}'),
 ('structure on S or on B',r'structure on \(S\) or on \(B\)'),
 (r'with D=0 the same index polynomial is (4x\textsuperscript{3}-p1 x)/24, the integer A',r'with \(D=0\) the same index polynomial is \((4x^3-p_1x)/24\), the integer \(A\)'),
 (r'a=M+nF, chi\(O\)=1, M\textsuperscript{2}=-2, M.K=F\textsuperscript{2}=M.F=0',r'\(a=M+nF\), \(\chi(\mathcal O)=1\), \(M^2=-2\), and \(M\cdot K=F^2=M\cdot F=0\)'),
 ('therefore0', 'therefore zero'),
 (r'line O\(-1\)',r'line \(\mathcal O(-1)\)'),
 ('on P1',r'on \(\mathbb P^1\)'),
 ('spin-c symbol',r'\(\mathrm{spin}^c\) symbol')
])

fix(15,[
 ('twelfth-iterate gamma period',r'twelfth-iterate \(\gamma\) period'),
 (r'Put rho=Qr, zeta=exp\(2pi i/12\), eta=exp\(pi i/12\), and index the node charts by i in Z, modulo the gamma period of length12',r'Put \(\rho=Qr\), \(\zeta=\exp(2\pi i/12)\), \(\eta=\exp(\pi i/12)\), and index the node charts by \(i\in\mathbb Z\), modulo the \(\gamma\) period of length twelve'),
 listing('X_i=W/rho^i, Y_i=rho^(i+1)/W, X_i Y_i=rho.',r'X_i=W/\rho^i,\qquad Y_i=\rho^{i+1}/W,\qquad X_iY_i=\rho.'),
 listing('D:(Q,i,W)->(zeta Q,i-1,eta rho^(-1) W).',r'D:(Q,i,W)\longmapsto(\zeta Q,i-1,\eta\rho^{-1}W).'),
 listing("X'_(i-1)=eta zeta^(1-i) X_i,\nY'_(i-1)=eta^(-1) zeta^i Y_i.",r"X'_{i-1}=\eta\zeta^{1-i}X_i,\qquad Y'_{i-1}=\eta^{-1}\zeta^iY_i."),
 ('product is zeta rho',r'product is \(\zeta\rho\)'),
 ('even at Q=0',r'even at \(Q=0\)'),
 ('elliptic translation-P/2; the twelfth step is-6P',r'elliptic translation \(-P/2\); the twelfth step is \(-6P\)'),
 ('inverse gamma period',r'inverse \(\gamma\) period'),
 ('fixed-radius r-circle',r'fixed-radius \(r\)-circle'),
 ('angular winding-1',r'angular winding \(-1\)'),
 ('same W/exp(zeta2) sign conversion',r'same \(W/\exp(\zeta_2)\) sign conversion'),
 ('cusp for r nonzero',r'cusp for \(r\ne0\)'),
 ('source I12 exceptional curves',r'source \(I_{12}\) exceptional curves')
])

fix(23,[
 (r'\item \textbf{Proof.} Use the cusp parameter',r'\item Use the cusp parameter'),
 ('one positive gamma turn',r'one positive \(\gamma\) turn'),
 ('additional real delta coefficient',r'additional real \(\delta\) coefficient')
])
fix(24,[(r'\item \textbf{Proof.} First isotope',r'\item First isotope')])

candidate=original
for p in patches:
    assert candidate.count(p['old'])==1
    candidate=candidate.replace(p['old'],p['new'])
assert sorted(re.findall(r'\\label\{([^}]+)\}',candidate))==sorted(re.findall(r'\\label\{([^}]+)\}',original))
for p in patches:
    assert '\\begin{lstlisting}' not in p['new']
    assert not any(ord(c)<32 and c not in '\n\t\r' for c in p['new'])
    for a,b in [(r'\(',r'\)'),(r'\[',r'\]')]:
        assert p['new'].count(a)==p['new'].count(b),(p['label'],a)
    assert p['new'].count(r'\begin{aligned}')==p['new'].count(r'\end{aligned}')

(P/'IV_F10_F24_notation_patches.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
(P/'IV_F10_F24_notation_changes.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n')
(P/'IV_F10_F24_notation.diff').write_text(''.join(difflib.unified_diff(original.splitlines(True),candidate.splitlines(True),fromfile='current_IV.body.linked.tex',tofile='proposed_IV.body.linked.tex')))
receipt={'author':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family',
 'source_sha256':hashlib.sha256(original.encode()).hexdigest(),'patch_count':len(patches),
 'individual_literal_conversions':sum(len(x['changes']) for x in details),
 'rows_changed':[p['label'] for p in patches],
 'unchanged_rows_checked_for_listing_residuals':['night:P3F.'+str(n) for n in range(16,23)],
 'all_guards_unique':True,'label_multiset_unchanged':True,'math_delimiters_balanced':True,
 'all_23_raw_math_listing_blocks_converted':sum(p['old'].count(r'\begin{lstlisting}') for p in patches),
 'shared_body_mutated':False,
 'boundary':'Notation only. The literal W/exp(zeta2) convention in F15 is converted as printed, without changing its exponent or asserting a new normalization.'}
(P/'IV_F10_F24_notation_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
