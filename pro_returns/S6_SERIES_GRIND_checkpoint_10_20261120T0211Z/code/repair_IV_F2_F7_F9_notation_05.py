from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parents[1]
p=R/'parts/IV.body.linked.tex';old=p.read_text();s=old
start=s.index(r'\begin{theorem}\label{night:P3F.7}')
end=s.index(r'\begin{theorem}\label{night:P3F.10}',start)
a=s[start:end];original=a;changes=[]
def sub(x,y):
 global a
 n=a.count(x)
 assert n,(x,n)
 a=a.replace(x,y)
 changes.append({'old':x,'new':y,'count':n})
sub(r'''\begin{lstlisting}
r0=(0,0,1), r1=(0,1,1), r+=(1,0,1), r-=(-1,1,1).
\end{lstlisting}''',r'''\[
 r_0=(0,0,1),\quad r_1=(0,1,1),\quad
 r_+=(1,0,1),\quad r_-=(-1,1,1).
\]''')
sub(r'''r++r-=r0+r1. The two adjacent unimodular charts have coordinates\(x0,x1,z\) and(x0',x1',z'), with exact transition''',r'''\(r_++r_-=r_0+r_1\). The two adjacent unimodular charts have coordinates \((x_0,x_1,z)\) and \((x'_0,x'_1,z')\), with exact transition''')
sub(r'''\begin{lstlisting}
x0'=z x0,  x1'=z x1,  z'=1/z,
q=x0 x1 z=x0' x1' z'.
\end{lstlisting}''',r'''\[
 x'_0=zx_0,\qquad x'_1=zx_1,\qquad z'=1/z,\qquad
 q=x_0x_1z=x'_0x'_1z'.
\]''')
sub(r'''The fixed curve is x0=x1=0. The transitions give O\(-1\)\textsuperscript{2}, and the cocharacter e2 has weights\(-1,+1,0\).''',r'''The fixed curve is \(x_0=x_1=0\). The transitions give \(\mathcal O(-1)^{\oplus2}\), and the cocharacter \(e_2\) has weights \((-1,+1,0)\).''')
sub(r'''\begin{lstlisting}
A=x0, B=z x0, C=x1, D=z x1
\end{lstlisting}''',r'''\[
 A=x_0,\qquad B=zx_0,\qquad C=x_1,\qquad D=zx_1
\]''')
sub('contracts the curve to AD=BC.',r'contracts the curve to \(AD=BC\).')
sub(r'on\(A,B,C,D\). On AD-BC=epsilon nonzero the action is free. For epsilon=1, polar decomposition of SL2\(C\) as U H gives the explicit equivariant diffeomorphism SU2 times R3, with the circle acting on U by left multiplication and acting trivially on H. A compact Milnor neighbourhood is thus S3 times D3 and its quotient is S2 times D3.',r'''on \((A,B,C,D)\). On \(AD-BC=\varepsilon\ne0\) the action is free. For \(\varepsilon=1\), polar decomposition of \(SL_2(\mathbb C)\) as \(UH\) gives the explicit equivariant diffeomorphism with \(SU(2)\times\mathbb R^3\), with the circle acting on \(U\) by left multiplication and acting trivially on \(H\). A compact Milnor neighbourhood is thus \(S^3\times D^3\) and its quotient is \(S^2\times D^3\).''')
sub(r'''Let A=X minus F and B=A/S1. General position gives pi1\(A\)=0. Alexander duality gives H*\(A;Z\)=Z in degrees0,3 and zero otherwise. The oriented normal link S3 is a primitive generator of H3\(A\). Its quotient is the normal link S2, and the circle bundle on these links is the Hopf bundle. In the Gysin sequence, e generates H2\(B\), and integration H3\(A\)-\textgreater H2\(B\) is multiplication by1: evaluate on this linked S2 and its Hopf preimage. Every other positive-degree group of B vanishes. Also pi1\(B\)=0 by the homotopy sequence of the principal circle bundle.''',r'''Let \(A=X\setminus F\) and \(B=A/S^1\). General position gives \(\pi_1(A)=0\). Alexander duality gives \(H^*(A;\mathbb Z)=\mathbb Z\) in degrees \(0,3\) and zero otherwise. The oriented normal link \(S^3\) is a primitive generator of \(H_3(A)\). Its quotient is the normal link \(S^2\), and the circle bundle on these links is the Hopf bundle. In the Gysin sequence, \(e\) generates \(H^2(B)\), and integration \(H^3(A)\to H^2(B)\) is multiplication by \(1\): evaluate on this linked \(S^2\) and its Hopf preimage. Every other positive-degree group of \(B\) vanishes. Also \(\pi_1(B)=0\) by the homotopy sequence of the principal circle bundle.''')
sub(r'''O\(1\) plus O\(-1\). Its clutching loop diag\(z,z^-1\) in SU2 bounds the explicit disc with SU2 coordinates''',r'''\(\mathcal O(1)\oplus\mathcal O(-1)\). Its clutching loop \(\operatorname{diag}(z,z^{-1})\) in \(SU(2)\) bounds the explicit disc with \(SU(2)\) coordinates''')
sub('rank2 bundle','rank-two bundle');sub('rank3 bundle','rank-three bundle')
sub('the boundary is F times S2, and the Euler class is just the meridian generator, with no F term.',r'the boundary is \(F\times S^2\), and the Euler class is just the meridian generator, with no \(F\) term.')
sub('Now Y=X/S1 is the union of B (truncated at that boundary) and F times D3. The maps on H0 and H2 in Mayer--Vietoris, with domain H2 ordered (F,meridian) and target(complement,tube), are respectively',r'''Now \(Y=X/S^1\) is the union of \(B\) (truncated at that boundary) and \(F\times D^3\). The maps on \(H_0\) and \(H_2\) in Mayer--Vietoris, with domain \(H_2\) ordered as \((F,\text{meridian})\) and target ordered as \((\text{complement},\text{tube})\), are respectively''')
sub(r'''\begin{lstlisting}
[1;-1],       [[0,1],[-1,0]].
\end{lstlisting}''',r'''\[
 \begin{pmatrix}1\\-1\end{pmatrix},\qquad
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]''')
sub(r'''The latter has determinant1. H4(boundary)=Z maps to zero and gives H5\(Y\)=Z;''',r'''The latter has determinant \(1\). The group \(H_4(\text{boundary})=\mathbb Z\) maps to zero and gives \(H_5(Y)=\mathbb Z\);''')
sub(r'''Van Kampen gives pi1\(Y\)=0. Thus Y is a homotopy5-sphere. Kervaire--Milnor1963, the order table on p.~504 and the Smale comparison on p.~505, gives Theta5=0, so Y is diffeomorphic to S5. Haefliger1966 Corollary6.6 says \(C_n^q=0\) for n\textless2q-3; with n=2,q=3, and Theorem1.2 converting concordance to isotopy, every embedding S2 in S5 is unknotted.''',r'''Van Kampen gives \(\pi_1(Y)=0\). Thus \(Y\) is a homotopy \(5\)-sphere. Kervaire--Milnor's order table on p.~504 and the Smale comparison on p.~505 give \(\Theta_5=0\), so \(Y\) is diffeomorphic to \(S^5\). Haefliger's Corollary~6.6 gives \(C_n^q=0\) for \(n<2q-3\); with \(n=2,q=3\), and Theorem~1.2 converting concordance to isotopy, every embedding \(S^2\) in \(S^5\) is unknotted.''')
for x,y in [
 ('D3 times D4',r'\(D^3\times D^4\)'),('S2 times D3',r'\(S^2\times D^3\)'),('S3 times D3',r'\(S^3\times D^3\)'),
 ('S2 times S2 to S1',r'\(S^2\times S^2\to S^1\)'),('H1(S2 times S2;Z)=0',r'\(H^1(S^2\times S^2;\mathbb Z)=0\)'),
 ('Harvey--Kerin--Shankar2020 Theorem4.1','Harvey--Kerin--Shankar, Theorem~4.1'),('codimension4','codimension-four'),(r'H2\(F;Z\) without2-torsion',r'\(H^2(F;\mathbb Z)\) without \(2\)-torsion'),
 ('S2 times D4',r'\(S^2\times D^4\)'),('D3 times S3',r'\(D^3\times S^3\)'),('S3 timesS3',r'\(S^3\times S^3\)'),('S2 timesD3',r'\(S^2\times D^3\)'),('S2 timesS3',r'\(S^2\times S^3\)'),(r'pi2\(SO4\)=0',r'\(\pi_2(SO(4))=0\)'),
 ('Let Phi be',r'Let \(\Phi\) be'),('diffeomorphism f of',r'diffeomorphism \(f\) of'),('clutched by Phi',r'clutched by \(\Phi\)'),(r'lambda\(f\)',r'\(\lambda(f)\)'),('invariants of f.',r'invariants of \(f\).'),
 ('the delta circle action',r'the \(\delta\)-circle action'),('a P1 bundle',r'a \(\mathbb P^1\)-bundle'),('degree-1',r'degree \(-1\)'),(r'PGL2\(C\)',r'\(PGL_2(\mathbb C)\)'),('P1 timesS1',r'\(\mathbb P^1\times S^1\)'),(r'O\(-1\)',r'\(\mathcal O(-1)\)'),
 (r'H2(\(\mathbb P^1\times S^1\);Z)=Z',r'\(H^2(\mathbb P^1\times S^1;\mathbb Z)=\mathbb Z\)'),
 ]: sub(x,y)
sub(r'''\begin{lstlisting}
(S2_y timesD4_u) union (D3_y timesS3_u),
\end{lstlisting}''',r'''\[
 (S^2_y\times D^4_u)\cup(D^3_y\times S^3_u),
\]''')
for x,y in [('the u coordinate',r'the \(u\) coordinate'),('the y factor',r'the \(y\) factor'),('orientation of X.',r'orientation of \(X\).'),('restriction of Phi',r'restriction of \(\Phi\)'),(r'tilde f of D3\_y timesS3\_u',r'\(\widetilde f\) of \(D^3_y\times S^3_u\)'),(r'D3\_y timesS2\_u',r'\(D^3_y\times S^2_u\)'),(r'S3\_y',r'\(S^3_y\)'),(r'S2\_u',r'\(S^2_u\)')]:sub(x,y)
sub(r'f:\(S^3_y\) times\(S^2_u\) -\textgreater{} \(S^3_y\) times\(S^2_u\)',r'\(f:S^3_y\times S^2_u\to S^3_y\times S^2_u\)')
sub('the H2 generator',r'the \(H_2\) generator');sub('fix H3 as well. Consequently f',r'fix \(H_3\) as well. Consequently \(f\)')
sub(r'Its Hopf lift A on \(S^3_y\) timesS3\_u equals tilde f',r'Its Hopf lift \(A\) on \(S^3_y\times S^3_u\) equals \(\widetilde f\)')
sub(r'\(S^2\times S^3\) -\textgreater{} S1. Its H1 is zero',r'\(S^2\times S^3\to S^1\). Its \(H^1\) is zero')
sub(r'boundary(D4\_u timesD4\_y)',r'\(\partial(D^4_u\times D^4_y)\)')
sub(r'''\begin{lstlisting}
H=D4_u timesS3_y,  K=S3_u timesD4_y,
N=S3_u timesD3_y in boundary H=boundary K.
\end{lstlisting}''',r'''\[
 H=D^4_u\times S^3_y,\qquad K=S^3_u\times D^4_y,\qquad
 N=S^3_u\times D^3_y\subset\partial H=\partial K.
\]''')
sub(r'''Our gluing convention identifies x in boundary H with A\(x\) in boundary K, after the standard product-boundary identification. The ball B7=D4\_u timesD3\_y has boundary equal to N union (D4\_u timesS2\_y). Its complement in the rounded product boundary is the other standard7-ball: this follows by taking the two hemispheres of the y boundary and rounding their product collars. Regluing H to K by A changes the identification only on N. Equivalently cut out B7 and reglue its boundary by the map equal to tilde f on N and the identity on D4\_u timesS2\_y. That boundary map is precisely Phi in the displayed decomposition of S6. The identity on the common collar makes the two quotient constructions coincide pointwise outside N, and their collar identifications coincide on N.''',r'''Our gluing convention identifies \(x\in\partial H\) with \(A(x)\in\partial K\), after the standard product-boundary identification. The ball \(B^7=D^4_u\times D^3_y\) has boundary \(N\cup(D^4_u\times S^2_y)\). Its complement in the rounded product boundary is the other standard \(7\)-ball: this follows by taking the two hemispheres of the \(y\) boundary and rounding their product collars. Regluing \(H\) to \(K\) by \(A\) changes the identification only on \(N\). Equivalently cut out \(B^7\) and reglue its boundary by the map equal to \(\widetilde f\) on \(N\) and the identity on \(D^4_u\times S^2_y\). That boundary map is precisely \(\Phi\) in the displayed decomposition of \(S^6\). The identity on the common collar makes the two quotient constructions coincide pointwise outside \(N\), and their collar identifications coincide on \(N\).''')
sub(r'''\begin{lstlisting}
D7 union_Phi D7  =  (D4_u timesS3_y) union_A (S3_u timesD4_y)
\end{lstlisting}''',r'''\[
 D^7\cup_\Phi D^7=(D^4_u\times S^3_y)\cup_A(S^3_u\times D^4_y)
\]''')
sub(r'''\begin{lstlisting}
H(t)delta, H(t)=-(4l1 log t+3l2 log(t-1))/(2pi i),
\end{lstlisting}''',r'''\[
 H(t)\delta,\qquad
 H(t)=-\frac{4\ell_1\log t+3\ell_2\log(t-1)}{2\pi i},
\]''')
sub('coefficient -p after carrying the collar integer l0.',r'coefficient \(-p\) after carrying the collar integer \(\ell_0\).')
sub('conifold xy=uv, with the circle acting on u,v with weights+1,-1 and fixing x,y.',r'conifold \(xy=uv\), with the circle acting on \(u,v\) with weights \(+1,-1\) and fixing \(x,y\).')
sub(r'''\begin{lstlisting}
(x,v,z),   u=xz, y=vz;
(u,y,w),   x=uw, v=yw;      w=1/z.
\end{lstlisting}''',r'''\[
 \begin{aligned}
 (x,v,z):&\quad u=xz,\quad y=vz;\\
 (u,y,w):&\quad x=uw,\quad v=yw,\quad w=1/z.
 \end{aligned}
\]''')
sub(r'''\begin{lstlisting}
(x,y,b), b=(|z|^2-|v|^2)/2;
(x,y,b'), b'=(|u|^2-|w|^2)/2.
\end{lstlisting}''',r'''\[
 (x,y,b),\quad b=\frac{|z|^2-|v|^2}{2};\qquad
 (x,y,b'),\quad b'=\frac{|u|^2-|w|^2}{2}.
\]''')
sub(r'r=\textbar z\textbar\textsuperscript{2}\textgreater0',r'\(r=|z|^2>0\)')
sub(r'''\begin{lstlisting}
2b=r-|y|^2/r,       2b'=|x|^2r-1/r,
db'/db=(|x|^2+r^(-2))/(1+|y|^2r^(-2))>0.       (P3F.9.1)
\end{lstlisting}''',r'''\[
 2b=r-\frac{|y|^2}{r},\qquad
 2b'=|x|^2r-\frac1r,\qquad
 \frac{db'}{db}=\frac{|x|^2+r^{-2}}{1+|y|^2r^{-2}}>0.
 \tag{P3F.9.1}
\]''')
sub(r'For epsilon\textgreater0 choose the unique r\textgreater0 solving',r'For \(\varepsilon>0\) choose the unique \(r>0\) solving')
sub(r'''\begin{lstlisting}
|x|^2r-|y|^2/r+2epsilon(r-1)/(r+1)=0.
\end{lstlisting}''',r'''\[
 |x|^2r-\frac{|y|^2}{r}+2\varepsilon\frac{r-1}{r+1}=0.
\]''')
sub(r'''\textbar x\textbar\textsuperscript{2}+\textbar y\textbar\textsuperscript{2}/r\textsuperscript{2}+4epsilon/\(r+1\)\textsuperscript{2}\textgreater0. Consequently r is a smooth positive function of\(x,y\), and the representatives z=sqrt\(r\),v=y/sqrt\(r\),u=x sqrt\(r\)''',r'''\(|x|^2+|y|^2/r^2+4\varepsilon/(r+1)^2>0\). Consequently \(r\) is a smooth positive function of \((x,y)\), and the representatives \(z=\sqrt r\), \(v=y/\sqrt r\), \(u=x\sqrt r\)''')
sub('each line with R by flow',r'each line with \(\mathbb R\) by flow');sub(r'over C\textsuperscript{2}',r'over \(\mathbb C^2\)')
sub('weight1.','weight one.');sub('the A2 triangulation',r'the \(A_2\) triangulation')
sub(r'\(q=uv,(|u|\textsuperscript{2}-|v|\textsuperscript{2})/2\)',r'\((q,b)=(uv,(|u|^2-|v|^2)/2)\)')
sub(r'E\_I1 timesS1\_gamma',r'\(E_{I_1}\times S^1_\gamma\)')
sub(r'E\_I1 timesS1',r'\(E_{I_1}\times S^1\)');sub(r'E\_I1',r'\(E_{I_1}\)')
sub('the gamma deck translates by the section6P',r'the \(\gamma\) deck translates by the section \(6P\)')
sub(r'a\(q\)',r'\(a(q)\)');sub(r'Z-\textgreater exp(t log a(q)) Z',r'\(Z\mapsto\exp(t\log a(q))Z\)')
sub('the integral gamma,u,w and q markings',r'the integral \(\gamma,u,w,q\) markings')
sub('in the gamma direction',r'in the \(\gamma\) direction');sub(r"a'=z\textsuperscript{2}a, namely O\(-2\)",r"\(a'=z^2a\), namely \(\mathcal O(-2)\)")
sub('is-2. The gamma coordinate',r'is \(-2\). The \(\gamma\) coordinate');sub(r'S1\_gamma',r'\(S^1_\gamma\)');sub('boundary gamma circle action',r'boundary \(\gamma\)-circle action')
# All substitutions preserve the given mathematical objects and formulas; no proof step removed.
assert a.count(r'\item')==original.count(r'\item')
assert re.findall(r'\\label\{([^}]+)\}',a)==re.findall(r'\\label\{([^}]+)\}',original)
s=s[:start]+a+s[end:]
# The F2 table's plain labels receive their literal mathematical typesetting.
f2start=s.index(r'\begin{theorem}\label{night:P3F.2}');f2end=s.index(r'\begin{theorem}\label{night:P3F.3}',f2start)
f2=s[f2start:f2end];f2old=f2
for n in [8,7,5,4,3]:
 x='(I\\_'+str(n)+')';y=r'\(I_'+str(n)+r'\)'
 if x in f2: f2=f2.replace(x,y);changes.append({'old':x,'new':y,'scope':'F2'})
for x,y in [('(A\\_1)',r'\(A_1\)'),('(A\\_2,A\\_1)',r'\((A_2,A_1)\)'),('component3 or5','component 3 or 5'),('component2 or5','component 2 or 5'),('component2 or3','component 2 or 3'),('component1 or3','component 1 or 3'),('component1 or4','component 1 or 4'),('component1 at','component 1 at'),('component3 at','component 3 at'),('at0 ','at \(0\) '),('degree3 map','degree-three map'),('Equation\\(P3F.2.1\\)','Equation \(P3F.2.1\)'),('three separate I2 fibres',r'three separate \(I_2\) fibres')]:
 if x in f2: f2=f2.replace(x,y);changes.append({'old':x,'new':y,'scope':'F2'})
s=s[:f2start]+f2+s[f2end:]
p.write_text(s)
(R/'analysis/IV_F2_F7_F9_notation_05.json').write_text(json.dumps({'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(s.encode()).hexdigest(),'patches':changes,'F7_F9_before':original,'F7_F9_after':a,'F2_before':f2old,'F2_after':f2,'proof_item_count_preserved':True,'scope':'Literal notation transports; every proof paragraph and mathematical claim retained. Rendered check remains necessary.'},indent=2)+'\n')
print(len(changes),'notation transports')
