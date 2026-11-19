# Executed in revise_body.py after source-preserving gate repairs.
# Each historical block is archived byte-for-byte in rejected_blocks/.

def strip_notice(t):
 t=re.sub(r'\\par\\noindent\\textbf\{Physical-line correction, 17 November 2026\.\}[\s\S]*?\\medskip\\par\s*','',t,count=1)
 return t

def subst(label,replacements,reason,extra=''):
 def f(t):
  t=strip_notice(t)
  for a,b in replacements:
   assert a in t,(label,a[:90]);t=t.replace(a,b)
  if extra:
   m=t.index(r'\begin{enumerate}[label=\arabic*.]')+len(r'\begin{enumerate}[label=\arabic*.]')
   t=t[:m]+'\n\\item '+extra+'\n'+t[m:]
  return t
 change(label,f,reason)

physical=r'''We retain the complete source, line, cap and frame maps below.
The meridian-one graph line is \(U=M^{-1}\): the fibre map
\(D_M(v)(w)=\langle v,w\rangle/\langle v,v\rangle\), with the
Hermitian form linear in its second argument, satisfies
\(D_M(e^{i\theta}v)=e^{-i\theta}D_M(v)\).
Its \(SU(2)\)-equivariant spinor extension is
\((a,b)\mapsto(\overline b,-\overline a)\).
The first-to-second cap maps in \cref{night:P3K.68} give
\(\lambda_M(F)=-\Sigma_{F^{-1}}\) and
\(\lambda_U(F)=\Sigma_{F^{-1}}\); cancelling the opposite
product collars gives \(A_M=-A_U\). We use the
intermediate meridian-one number \(A_U=(4k_U-\ell_U)/24\)
and its physical return \(A_M=-A_U\) throughout this calculation.'''

subst('night:P3F.25',[
 ('The actual real trace gives $A=(12s_\\delta-p_{\\rm rel})/24=-R\\cdot O$','The meridian-one real trace gives $A_U=(12s_\\delta-p_{\\rm rel})/24=-R\\cdot O$, and the physical return is $A_M=R\\cdot O$'),
 ('The positive weighted OS47 loop has $A=-4$, oriented class $24\\pmod{28}$','The positive weighted OS47 loop has $A_M=4$, oriented class $4\\pmod{28}$'),
 ('Thus the actual physical return satisfies','Thus the meridian-one dual completion satisfies'),
 ('A=\\frac{3b^2-p_1(T\\bar X)}{24}','A_U=\\frac{3b^2-p_1(T\\bar X)}{24}'),
 ('A=\\frac{-168+72}{24}=-4,\n \\qquad\\mu(\\Sigma_\\Phi)=-\\frac4{28}.','A_U=\\frac{-168+72}{24}=-4,\n \\qquad A_M=4,\qquad\\mu(\\Sigma_\\Phi)=\\frac4{28}.')
 ],'Retain the full trace/page construction; identify its computed dual-line number and apply the explicit cap duality to obtain physical class 4.',physical)

subst('night:P3K.10',[
 ('A=-3,\\qquad \\mu(\\Sigma_\\Phi)=-\\frac3{28},\\qquad\n [\\Phi]=25','A_M=3,\\qquad \\mu(\\Sigma_\\Phi)=\\frac3{28},\\qquad\n [\\Phi]=3'),
 ('its Euler line has positive meridian one','its dual meridian line has positive meridian one'),
 ('A=\\frac{12s_\\delta-p_{\\rm rel}}{24}\n   =\\frac{-96+24}{24}=-3.','A_U=\\frac{12s_\\delta-p_{\\rm rel}}{24}\n   =\\frac{-96+24}{24}=-3,\qquad A_M=-A_U=3.'),
 ('asserted oriented class \\(25\\)','asserted oriented class \\(3\\)'),
 ('classes \\(-3n\\pmod{28}\\)','classes \\(3n\\pmod{28}\\)')
 ],'Retain the OS45 source, exact Hom lift, norm shell, topology and origins; correct the physical reference to 3 through the explicit dual-line map.',physical)

subst('night:P3K.22',[
 ('& \\(-3\\) & 25','& \\(3\\) & 3'),('& \\(-6\\) & 22','& \\(6\\) & 6'),('& \\(-9\\) & 19','& \\(9\\) & 9'),('& \\(-14\\) & 14','& \\(14\\) & 14'),
 ('A=\\frac{12M^2-p_1(S)}{24}\n   =1-\\frac d2=-\\frac{d-2}{2}.','A_U=\\frac{12M^2-p_1(S)}{24}\n   =1-\\frac d2,\qquad A_M=\\frac d2-1=\\frac{d-2}{2}.'),
 ('The orientation dictionary of P3K.7 and P3F.25','The explicit line and cap dictionary of \\cref{night:P3K.68}')
 ],'Keep all ten source, period, topology and page constructions; the physical values are 3,6,9,14.',physical)

subst('night:P3K.24',[
 ('A(\\Phi)=-(3l+2),','A_M(\\Phi)=3l+2,'),
 ('\\mu(\\Sigma_\\Phi)=-\\frac{3l+2}{28}','\\mu(\\Sigma_\\Phi)=\\frac{3l+2}{28}'),
 ('[\\Phi]=26-3l','[\\Phi]=3l+2'),
 ('$b|_V=2\\kappa c_1(M)$','$b|_V=-2\\kappa c_1(M)$'),
 ('A(\\Phi)=\\kappa\\frac','A_U(\\Phi)=\\kappa\\frac'),
 ('A(\\Phi)=\\frac{12(-2m)+24\\chi}{24}\n        =\\chi-m=-(3l+2).','A_U(\\Phi)=\\frac{12(-2m)+24\\chi}{24}\n        =\\chi-m=-(3l+2),\qquad A_M=3l+2.'),
 ('$26-3l$ exhaust','$3l+2$ exhaust')
 ],'Retain both reduced-III families and every root/cap/endpoint map; physical class is 3l+2.',physical)

# In these two framing blocks the intermediate A is explicitly the dual number.
subst('night:P3K.27',[
 ('(6,\\ 3d-6,\\ 1-d/2\\bmod28)','(6,\\ 3d-6,\\ d/2-1\\bmod28)'),
 ('m_{\\rm rel}=-k+6A=-\\ell/4=6,','m_{\\rm rel}=-k+6A_U=-\\ell/4=6,'),
 ('n_{\\rm rel}=-6A=3d-6.','n_{\\rm rel}=-6A_U=3d-6.'),
 ('The central class is \\(A=1-d/2\\pmod{28}\\) by its\nalready proved Hopf transfer.','The central class is \\(A_M=-A_U=d/2-1\\pmod{28}\\) by the explicit dual cap transfer.'),
 ('rotating characteristic pair and the corresponding relative','meridian-one dual characteristic pair and the corresponding physical relative')
 ],'Preserve the complete matched normal clutch and vanishing Pontryagin transgression; correct only the physical central coordinate.',physical)

subst('night:P3K.30',[
 ('s&=\\chi-H/2\\pmod{28}.','s&=H/2-\\chi\\pmod{28}.'),
 ('m_{\\rm rel}=-k+6A=-\\ell/4,','m_{\\rm rel}=-k+6A_U=-\\ell/4,'),
 ('n_{\\rm rel}=-6A,\\qquad s=A\\bmod28 .','n_{\\rm rel}=-6A_U,\\qquad s=-A_U\\bmod28 .'),
 ('\\(A=\\chi-H/2\\)','\\(A_U=\\chi-H/2\\)'),
 ('the individual Jin pair and','the individual meridian-one dual pair and')
 ],'Preserve the signed page/root and exact clutch comparison; retain free integers and change the central coordinate by the physical duality.',physical)

# Three first-edge constructions retain every native map; only their central seed changes.
subst('night:P3K.45',[
 ('[\\Sigma_{\\Phi,J(T)}]=1','[\\Sigma_{\\Phi,J(T)}]=-1'),
 ('fixed-edge flop has class23','fixed-edge flop has class21'),
 ('P3F.56 proves the class of the original positive rho return is one.','The physical transfer of \\cref{night:P3K.68} gives the original positive rho return class $-1$.'),
 ('23; its edge is','21; its edge is')
 ],'Retain the literal half-source maps and their two-component endpoint conjugacy; the reflected physical class is -1, fixed-edge class -7.')

subst('night:P3K.46',[
 ('(m_{C_0},n_{C_0},s)=(0,-6,1)','(m_{C_0},n_{C_0},s)=(0,-6,-1)'),
 ('Its actual Jin\ncharacteristic pair','Its meridian-one dual\ncharacteristic pair'),
 ('Its index is consequently \\(A=(4k-\\ell)/24=1\\),\nin agreement with the independent oriented conjugacy calculation\nof P3K.45.','Its dual index is \\(A_U=(4k-\\ell)/24=1\\), and the explicit cap comparison gives \\(A_M=-1\\), in agreement with the oriented conjugacy of \\cref{night:P3K.45}.'),
 ('n_{C_0}=-6A=-6,','n_{C_0}=-6A_U=-6,'),
 ('m_{C_0}=6A-k=0,\\qquad s=1','m_{C_0}=6A_U-k=0,\\qquad s=-1')
 ],'Retain the cap diffeomorphism and its pullback of the Euler line; distinguish the dual pair (6,0) from the physical pair (-6,0).',physical)

subst('night:P3K.50',[
 ('(m_0,n_0,s)=(6,-6,1)','(m_0,n_0,s)=(6,-6,-1)'),
 (r'[\Phi_H]=L^0R^{-6}\mathcal C',r'[\Phi_H]=L^0R^{-6}\mathcal C^{-1}'),
 (r'[\Phi_O]=L^6R^{-6}\mathcal C,',r'[\Phi_O]=L^6R^{-6}\mathcal C^{-1},'),
 ('(m,n,s)=(6,-6,1)','(m,n,s)=(6,-6,-1)')
 ],'Keep the complete pure-left native-to-ordinary cylinder map and derivative calculation; replace the physical central seed by -1.')

subst('night:P3K.52',[
 ('Their central coordinate is one.','Their physical central coordinate is $-1$.'),
 ('return, namely one from F56.','return, namely $-1$ by the explicit F56-to-physical cap map of \\cref{night:P3K.68}.')
 ],'Retain the full stable derivative vector and both closed Spin lifts; correct the shared physical central seed.')

subst('night:P3K.54',[
 ('23,\\qquad23,\\qquad1','21,\\qquad21,\\qquad27'),
 ('C_0&0&-6&1','C_0&0&-6&-1'),('C_1&0&-6&1','C_1&0&-6&-1'),('C_2&-6&0&1.','C_2&-6&0&-1.'),
 ('return one in each case.','return $-1$ in each case by \\cref{night:P3K.68}.'),
 ('coordinates \\((-5,-5,1)\\)','coordinates \\((-7,-7,-1)\\)'),
 ('\\((23,23,1)\\)','\\((21,21,27)\\)'),
 ('The diagonal value one','The diagonal value $-1$')
 ],'Keep all three native unit maps and the exact directed Cox conjugacy; add right integers (-6,-6,0) to the physical seed -1.')

subst('night:P3K.56',[
 ('s(n)=1-3n(n-1)','s(n)=-1-3n(n-1)'),
 (r'\{1,7,9,11,15,21,23,25\}',r'\{5,7,9,13,19,21,23,27\}'),
 ('initial source return is \\(s(0)=1\\)','initial physical source return is \\(s(0)=-1\\)'),
 ('1,1,23,11,21,25,23,15,1,9,11,7,25,9,15.','27,27,21,9,19,23,21,13,27,7,9,5,23,7,13.')
 ],'Retain the actual adjacent fan/source/period maps and recurrence; correct the physical seed and recompute every displayed residue.')

subst('night:P3K.6',[
 ('outer boundary this class is the actual delta-circle Euler class.','outer boundary this class is the Euler class of the Hermitian-dual delta line $U=M^{-1}$.'),
 ('section is exactly \\(c_1(M)\\).','section is exactly \\(-c_1(M)\\).'),
 ('The actual delta bundle has that value,','The Hermitian-dual delta bundle has that value,'),
 (r's^*x=c_1(L_\delta|_V)=c_1(M).',r's^*x=c_1(L_\delta^{-1}|_V)=-c_1(M).'),
 ('The last equality is the exact circle-line comparison P3F.10.','The last equality is P3F.10 followed by the explicit Hermitian dual map of \\cref{night:P3K.68}.')
 ],'Retain the embedded trace, compression, integral uniqueness and normal-section homotopy; its meridian-one line is the explicit dual U=M^{-1}.',physical)

subst('night:P3K.23',[
 ('return\'s Jin index as','return\'s physical index and meridian-one dual pair as'),
 ('A=\\frac{4k-\\ell}{24},','A_M=-A_U,\\qquad A_U=\\frac{4k_U-\\ell_U}{24},'),
 ('-5A\\pmod {28}','7A_M\\pmod {28}'),
 ('Original index \\(A\\)','Original physical index \\(A_M\\)'),
 ('\\(8\\) & \\(-3\\) & \\(15\\)','\\(8\\) & \\(3\\) & \\(21\\)'),
 ('\\(14\\) & \\(-6\\) & \\(2\\)','\\(14\\) & \\(6\\) & \\(14\\)'),
 ('\\(20\\) & \\(-9\\) & \\(17\\)','\\(20\\) & \\(9\\) & \\(7\\)'),
 ('\\(30\\) & \\(-14\\) & \\(14\\)','\\(30\\) & \\(14\\) & \\(14\\)'),
 ('example of index \\(-4\\) gives class\n\\(20\\)','example of physical index \\(4\\) gives class\n\\(0\\)'),
 ('\\ell-4k=-4b,\\qquad b=6A,\\qquad n=-6A.','\\ell_U-4k_U=-4b,\\qquad b=6A_U,\\qquad n=-6A_U=6A_M.'),
 ('of the original relative class is its actual class \\(A\\bmod28\\).\nEquation (K23.6) adds \\(n\\) to that exponent, and (K23.10) gives\n\\(n=-6A\\).','of the original relative class is its actual physical class \\(A_M\\bmod28\\).\nEquation (K23.6) adds \\(n\\) to that exponent, and (K23.10) gives\n\\(n=6A_M\\).')
 ],'Retain the exact common-link/quaternion maps and oriented commutator plumbing; the native right coordinate is 6A_M and the physical fixed-edge result is 7A_M.',physical+r' In the intermediate Hopf-quotient calculation below, unadorned \(k,\ell\) denote \(k_U,\ell_U\).')

def k23_orientation(t):
 a=t.index(r'\item There are two explicit reversals in comparing this plumbing with')
 b=t.index(r'\item Finally',a)
 new=r'''\item The physical comparison uses the explicit cap maps of
\cref{night:P3K.68}, with the oppositely oriented \(y\)-ball
implemented by the reflection
\(\rho(y_0,y_1,y_2,y_3)=(-y_0,y_1,y_2,y_3)\).
For \(L=D^4_y\times S^3_q\), \(R=S^3_y\times D^4_q\), and
first-to-second clutch \(F\), the physical pieces are \(-R,-L\).
Writing \(L\) first changes the arrow to \(F^{-1}\), hence
\(\lambda_M(F)=-\Sigma_{F^{-1}}\).
A disc-supported clutch and its inverse bound the cylinder obtained
by cancelling their opposite product collars, so
\(\Sigma_{F^{-1}}=-\Sigma_F\). Therefore
\(\lambda_M(\mathcal C)=\Sigma_{\mathcal C}\) with the positive
value in (K23.11). This fixes the central generator independently
of the dual Euler line used in the characteristic calculation.

'''
 return t[:a]+new+t[b:]
change('night:P3K.23',k23_orientation,'Replace the old ambiguous Hopf-coordinate orientation paragraph by the explicit oriented product reflection, piece exchange and inverse-clutch cancellation.')

subst('night:P3K.32',[
 ('A^{\\rm Jin}&=\\chi-H/2','A_U&=\\chi-H/2'),
 ('&s&=A^{\\rm Jin}\\pmod {28}.','&s&=-A_U=H/2-\\chi\\pmod {28}.'),
 ('A^{\\rm Jin}=1-d/2.','A_M=d/2-1.'),
 ('the actual flop maps transport its relative coordinates to\nthe returns for the other allowed fans.','the complete marked-prism transport of \\cref{night:P3K.73} computes the other whole-zero scalar fans. The individual reference fixed-star product alone supplies no simultaneous outer plumbing product.'),
 ('and $(4k-\\ell)/24=\\chi-H/2$ with the stated\nnormal and Jin signs.','and $A_U=(4k-\\ell)/24=\\chi-H/2$, while the explicit physical cap comparison gives $A_M=-A_U$.')
 ],'Retain the full order-one clutch, signed norm reduction, source/line arrows and page calculation; correct the central sign and restrict the all-fan deduction to K73.',physical)

subst('night:P3K.40',[
 ('=-5=23\\quad','= -7=21\\quad'),
 ('so P3F.56 gives \\(s=1\\pmod {28}\\).','so the explicit physical transfer of \\cref{night:P3K.68} gives \\(s=-1\\pmod {28}\\).'),
 ('n=-b=-6A.','n=-b=-6A_U.'),
 ('\\(A=1\\) by P3F.56','\\(A_U=1\\) in the dual-line computation of P3F.56'),
 ('1-6=-5=23\\pmod {28}.','-1-6=-7=21\\pmod {28}.'),
 ('\\(-5\\). To compute','\\(-7\\). To compute')
 ],'Keep the full single fixed-star family and all winding-six units; the exact native Cox arrow adds -6 to the physical seed -1.',physical)

subst('night:P3K.59',[
 ('1-3j(j+1)','-1-3j(j+1)'),('-5-24j(j+1)','-7-24j(j+1)'),
 (r'\{3,15,19,23\}',r'\{1,13,17,21\}'),
 ('has class three.','has class one.'),
 ('\\(23+4j(j+1)\\)','\\(21+4j(j+1)\\)'),
 ('23,3,19,15,19,3,23 .','21,1,17,13,17,1,21 .'),
 ('has the actual positive return class three.','has the actual positive return class one.')
 ],'Retain every exact matrix, native pair and directed mutation; change the physical central seeds and recompute the two residue sequences.')

subst('night:P3K.58',[
 ('[Z_{\\mathcal T}]+[Z_{J\\mathcal T}]+1+[I_{\\mathcal T}]','[Z_{\\mathcal T}]+[Z_{J\\mathcal T}]-1+[I_{\\mathcal T}]'),
 ('(1,2,4p)&0&-1','(1,2,4p)&0&1'),
 ('(2,1,4p-1)&1-2k(1-3p)&-2+2k(1-3p)','(2,1,4p-1)&-1-2k(3p-1)&2+2k(3p-1)'),
 ('[\\Phi_0]=1.','[\\Phi_0]=-1.'),
 ('A^{\\rm scalar}=1-3p','A^{\\rm scalar}=3p-1'),
 ('selected-cusp term \\(1\\)','selected-cusp term \\(-1\\)')
 ],'Retain the bounded parameter-surface family, all cut endpoint arrows, D^-4 root correction and full scalar cochain. Its physical cut relation uses selected class -1 and infinity classes 0,-1.')

subst('night:P3K.60',[
 ('\\bigl(-a+kA_{\\rm scalar}+14e,\\ kA_{\\rm scalar}+14e\\bigr)','\\bigl(kA_{\\rm scalar}+14e,\\ a+kA_{\\rm scalar}+14e\\bigr)'),
 ('1-3p,&(a,b,m)','3p-1,&(a,b,m)'),
 ('A_{\\rm scalar}=1-3p','A_{\\rm scalar}=3p-1'),
 ('=-a+2kA_{\\rm scalar}.','=a+2kA_{\\rm scalar}.'),
 ('2\\bigl([Z_{J\\mathcal T}]-kA_{\\rm scalar}\\bigr)','2\\bigl([Z_{\\mathcal T}]-kA_{\\rm scalar}\\bigr)'),
 ('=(-a+kA_{\\rm scalar}+14e,\\ kA_{\\rm scalar}+14e),','=(kA_{\\rm scalar}+14e,\\ a+kA_{\\rm scalar}+14e),'),
 ('Its value\nis not selected, and no class in \\(\\Theta_7\\) is divided by two.','This particular sum-and-difference argument does not select its value; the completed absolute calculation is \\cref{night:P3K.88}. No class in \\(\\Theta_7\\) is divided by two.')
 ],'Retain the complete single/double parameter square and native pair (1-a,a); use the corrected physical sum while preserving the precise scope of the two-element ambiguity.')

# A current theorem on a retained local construction replaces the old compound
# assertion. The original complete text is in rejected_blocks/<id>.tex.
def metadata_end(t):
 at=t.index(r'\StatementRecord')+len(r'\StatementRecord')
 for _ in range(4):
  while t[at].isspace():at+=1
  assert t[at]=='{';depth=1;at+=1
  while depth:
   if t[at]=='{' and t[at-1]!='\\':depth+=1
   elif t[at]=='}' and t[at-1]!='\\':depth-=1
   at+=1
 return at

def statement(t,new):
 a=metadata_end(t);b=t.index(r'\end{theorem}',a)
 return t[:a]+'\n'+new+'\n'+t[b:]

def current_proof(t):
 return t.replace(r'\begin{proof}[Preserved earlier argument; scope corrected above]',r'\begin{proof}')

def cut_tail(t,marker,ending):
 a=t.index(marker);b=t.index(r'\end{enumerate}',a)
 # Find the outer end, not a nested list end: all selected tail markers are
 # beyond the last nested source enumeration in these specific blocks.
 b=t.rindex(r'\end{enumerate}')
 return t[:a]+'\n\\item '+ending+'\n\n'+t[b:]

outer_obstruction=r'''The actual outer attaching map has to be retained as well.
For full periods \(h:(Z,V)\mapsto(\kappa qZ,\alpha V)\) and
\(B:(Z,V)\mapsto(gZ,q\eta V)\), the second outer star has
\(z_1=(g/\kappa)z_0\) and normal coefficient map
\[
 (N_1^-,N_1^+)=
 ((\eta/\alpha)N_0^-,\;\kappa\alpha/(g\eta)N_0^+).
\]
Conjugating the negative-weight normal coordinate makes its
complex determinant \((\kappa/g)(\alpha/\overline\alpha)
(\overline\eta/\eta)\), of parameter winding \(-2J\).
The simultaneous marked equivariant product equations would give
\(-J=0\), whereas the scalar family has \(J\ne0\).
These are the full coefficient arrows of \cref{night:P3K.61}.
The inner charged-cap calculation above therefore cannot be glued
with an unchanged outer product to deduce equality of the returns.'''

def k17(t):
 t=statement(t,r'''The real master-space resolution, its two moment-face maps,
inner free-orbit line and charged joint-cap maps below are defined
for the actual OS49 local square. Their common inner correction
has the displayed vanishing characteristic pair. The historical
assertion that the two complete OS49 returns are equal is false:
for cap order \(m=3k\) their physical whole-loop classes are
\(-3k\) on the negative fan and \(0\) on the positive fan.
For their actual shorter loop the classes are \(-k\) and \(0\),
by the complete marked outer comparison in \cref{night:P3K.65}.''')
 # Preserve all actual master-space, inner line, moment rescaling and
 # fixed-locus normal charts. Stop before the unsupported global gluing.
 t=cut_tail(t,r'\item Apply the explicit collar construction of P3K.7',
 r'''The preceding construction is the inner master-space and charged-cap
comparison. Its actual outer attachment in the OS49 family is the
component-line map, with its unequal two-node defects, carried in
\cref{night:P3K.65}. That proof gives native diagonal pair
\((-k,k)\) for the shorter negative-to-positive comparison. The
literal Cox conjugacy adds its right integer \(k\), so starting
from the proved positive return \(0\) gives the negative return
\(-k\). The map \(w=r^3\) pulls the shorter family back to the
whole family and composes three actual positive returns, giving
\(-3k\). At \(k=1\) the two classes are \(25\) and \(0\).
Thus the claimed equality of the complete returns is refuted,
while all the local master-space and joint-cap arrows above remain
available with their displayed source and target.''')
 return current_proof(t)
change('night:P3K.17',k17,'Retain every local master-space, charged-cap and fixed-locus chart; remove the unsupported outer gluing and replace equal-zero returns by the actual K65 counterexample.')

def k25(t):
 t=statement(t,r'''The literal square charts, period reindexing, scalar Cox lift,
common origin difference and inner charged-cap maps below exist
for each primitive scalar source of \cref{night:P3K.22}.
The assertion that every vertical shear has the same complete
return is false. For the actual OS45 family the reference fan
has physical class \(3\), whereas \(T_2\) has class \(2\).
The missing outer determinant is calculated explicitly below.''')
 t=cut_tail(t,r'\item The two actual endpoint conifold mapping tori have opposite',outer_obstruction+r'''
For OS45, \(J=1,H=8,\chi=1\). The exact vertical source and period
arrows \(Z_n=Z, V_n=Z^{-n}V, h_n=hB^n, B_n=B\) in
\cref{night:P3K.72} give
\(A_M(n)=H/2-\chi-Jn(n-1)/2=3-n(n-1)/2\).
Thus \(A_M(0)=3\) and \(A_M(2)=2\), proving the stated counterexample.''')
 return current_proof(t)
change('night:P3K.25',k25,'Retain square/source/line and inner-cap maps; replace the equality claim by the full outer determinant obstruction and OS45 T0/T2 counterexample.')

def k29(t):
 t=statement(t,r'''The integral cellular bases and reciprocal-section common-exterior
maps below give
\[
 m'_0=-m_0+2m_1+2m_2,\quad m'_j=m_j\ (j=1,2),\qquad
 D'_0=-D_0,\quad D'_j=D_j+2D_0.
\]
The symmetry of variation and the exact stable frame-change pairing
also hold for the actual relative return maps to which those
constructions are applied. The old scalar initialization
\(V=\operatorname{diag}(v,0,0)\) and vanishing nonfixed right
integers are refuted by the full outer coefficient maps of
\cref{night:P3K.61,night:P3K.62}.''')
 a=t.index(r'\par\medskip\noindent\textbf{3. The actual relative return')
 end=t.rindex(r'\end{enumerate}')
 keep=r'''\item For a relative map \(F\) equal to the identity on the boundary,
its variation is the integral chain map
\(\operatorname{Var}_F(D)=F(D)-D\).
Double the common exterior and extend \(F\) by the identity.
The meridians and doubled relative cycles have pairings
\(m_i\cdot D_j=\delta_{ij}\) and \(D_j\cdot m_i=-\delta_{ij}\).
The extended map fixes the meridians and sends
\(D_j\mapsto D_j+\sum_i V_{ij}m_i\). Preservation of
\(D_i\cdot D_j\) gives \(-V_{ij}+V_{ji}=0\), proving symmetry.
This applies to the closed actual ordinary products constructed
in \cref{night:P3K.71,night:P3K.73}; it makes no scalar
initialization from the static meridian map.

\item For stable frames related by \(\sigma'=\sigma g\), the exact
matrix identity is
\[
 c_{\sigma'}(F)(p)=g(Fp)^{-1}c_\sigma(F)(p)g(p).
\]
The primitive third class of Spin changes on a relative cycle \(D\)
by \(-\langle g^*\eta,F(D)-D\rangle\).
Indeed Spin is two-connected, so choose a cellular representative
of \(g\) constant on the two-skeleton. On each three-cell the
product obstruction is the sum of the three factor integers;
the boundary terms cancel because \(F\) is the identity there.
The remaining chain is exactly \(F(D)-D\), with the displayed minus
sign. This proves the frame-change formula integrally.

\item '''+outer_obstruction+r'''
On the actual native \(C_1\) star \cref{night:P3K.62} gives the
free pair \((J,-J)\). At \(J=1\) its right integer is \(-1\),
which directly refutes the old vanishing claim. The static cell
and reciprocal-section maps proved above remain the input maps
for the corrected marked-prism calculation.
'''
 return current_proof(t[:a]+keep+t[end:])
change('night:P3K.29',k29,'Keep the full integral cell and reciprocal-section proofs plus exact symmetry/frame-change derivations; remove the false simultaneous scalar-product initialization and its consequences.')

def k31(t):
 t=statement(t,r'''The actual single-star product frame differs from the ambient
stable frame by its displayed degree-one normal generator.
The literal common-link flop changes the ambient third frame
class by \(2e_i\), and the explicit orientation-preserving reset
\((y,q)\mapsto(Jy,Jq)\) swaps the free generators.
Consequently the native directed update is
\((m,n,s)\mapsto(m+2n,-n,s+n)\).
The historical universal norm polynomial is false: the actual
OS45 fans \(T_0,T_2\) both have physical cocharacter norm \(1\),
but their physical classes are \(3,2\).''')
 a=t.index(r'\item The third object is the oriented central return class')
 b=t.index(r'\item A different global stable frame',a)
 t=t[:a]+r'''\item The third object is the physical central return class
\(s\in\mathbb Z/28\). It is carried together with the actual
variation and derivative data; no diagonal initialization of the
full scalar plumbing is made here.

'''+t[b:]
 t=cut_tail(t,r'\par\medskip\noindent\textbf{5. The complete common-exterior recurrence.}',
 r'''The maps just proved are local comparison maps with their exact
frames and source/target markings. The remaining ordinary-product
transport is supplied, with all outer units, by
\cref{night:P3K.71,night:P3K.73}. For the counterexample use OS45
\(J=1,H=8,\chi=1\) and the literal vertical changes
\(Z_n=Z,V_n=Z^{-n}V,h_n=hB^n,B_n=B\).
The physical cocharacter is still \(e_2\), so its coordinates are
\((0,1)\) and the proposed norm equals \(1\) for both \(n=0,2\).
The actual class \(3-n(n-1)/2\) is \(3\) and \(2\), respectively.
Thus no function of that norm alone gives these scalar returns;
the rejected recurrence and its residue table are preserved only
in the historical audit file.''')
 return current_proof(t)
change('night:P3K.31',k31,'Keep the full degree-one product frame, +2ei flop frame and anti-quaternion reset proofs; remove the false scalar recurrence and norm polynomial, with exact counterexample.')

def k33(t):
 t=statement(t,r'''For logarithmic orders \(3K,4L\), \(\gcd(3K,4L)=1\), and
sphere equation \(4Ln_0+3Kn_1=\varepsilon=\pm1\), the explicit
integral cochain and chartwise translations below construct the
single endpoint for
\(w_h=e^{-\pi i c/(KL)},\ u=\kappa w_h^{2KL},\ w_h=r^6\).
They retain every finite character and give the reference
fixed-star dual pair \((-KL,-4KL)\), native free pair \((KL,0)\)
and physical reference class \(0\).
The all-fan polynomial formerly attached to this endpoint is
refuted: for \(K=L=1\), the actual \(T_2\) shorter return is
\(26\pmod{28}\), while that polynomial is zero.''')
 t=t.replace('3. A closed original-loop product on every cusp chart.','3. The closed endpoint atlas and the reference fixed-star framing.')
 t=t.replace('Thus (P3K.33.12) is a closed simultaneous Cox product for the single\npositive \\(w_h\\)-loop.','Thus (P3K.33.12) closes the toric endpoint characters for the single\npositive \\(w_h\\)-loop. It supplies the reference fixed-star framing; it does not identify the complete marked outer plumbing with a product.')
 t=t.replace('This proves the required simultaneous normal endpoint comparison.','This proves the reference fixed-star normal endpoint comparison; the other displayed character maps are retained as endpoint maps.')
 t=t.replace('in the actual simultaneous Cox product (P3K.33.12).','in the actual reference fixed-star product carried by (P3K.33.12).')
 t=cut_tail(t,r'\par\medskip\noindent\textbf{5. Applying the proved common-exterior recurrence.}',
 r'''The endpoint and reference free invariants just constructed are the
inputs to \cref{night:P3K.73}, with shorter scalar winding
\(J=2KL\), \(\widehat H=KL/3\), and
\(\widehat\chi=KL/6\).
Their actual vertical class is
\(\widehat H/2-\widehat\chi-Jn(n-1)/2=-KL\,n(n-1)\).
For \(K=L=1,n=2\) this is \(-2=26\), whereas the physical
cocharacter still has coordinates \((0,1)\) and norm \(S=1\).
The rejected expression \(KL(S-1)(S-3)/8\) is zero there.
The complete all-fan answer is the actual marked-prism algorithm,
whose original-family witness \(P=\left(\begin{smallmatrix}1&-2\\0&1\end{smallmatrix}\right)\)
has class \(3\), and whose full image is all of \(\mathbb Z/28\),
as proved in \cref{night:P3K.73,night:P3K.74}.''')
 return current_proof(t)
change('night:P3K.33',k33,'Keep the full original one-period cochain, root/cusp endpoint translations and signed fixed-star framing; replace the false all-fan polynomial and range by the actual K73 input and T2 counterexample.')

def k34(t):
 t=statement(t,r'''For the component-supported OS49 families with
\(\lambda=r^{3k}\), \(k>0\), signed primitive cap norm
\(n=\pm1\), and retained character \(d\delta\), the positive-fan
source, line, solid-torus and normal-frame maps below give
\[
 (k_U,\ell_U)=(-6k,-24k),\qquad
 (k_M,\ell_M)=(6k,24k),\qquad
 (m_{\rm rel},n_{\rm rel},s)=(6k,0,0).
\]
The actual component line retains its \(I_2\) multidegree
\((-1,+1)\) and relative square \(-2k\).
The old universal fan polynomial is refuted by the negative fan:
its whole-loop class is \(-3k\), and its actual shorter-loop
class is \(-k\), by \cref{night:P3K.65}. The complete all-fan
calculation is \cref{night:P3K.77}.''')
 return current_proof(t)
change('night:P3K.34',k34,'Retain the fully corrected cp25 positive-fan proof and actual component-line/cap markings; remove its obsolete all-fan statement and cite the proved negative-fan counterexample.')

def f53(t):
 a=t.index('The fixed-source canonical scalar sphere families')
 b=t.index(r'\end{theorem}',a);head=t[a:b]
 head=head.replace('pair \\((-3H,-24\\chi)\\) and return index \\(A=\\chi-H/2\\).','dual pair \\((-3H,-24\\chi)\\) and physical return index \\(A_M=H/2-\\chi\\).')
 q=head.index('On the actual fan');e=head.index('The actual shorter original loop',q)
 head=head[:q]+r'''For every actual transported fan, the complete units and endpoint
maps enter the marked-prism calculation of \cref{night:P3K.73}.
The historical polynomial in the physical cocharacter norm is
refuted by the OS45 reference value \(3\), for which it gave \(25\).
'''+head[e:]
 t=statement(t,head)
 t=t.replace('(m_{\\rm rel},n_{\\rm rel},A)&=\n           (6\\chi,3H-6\\chi,\\chi-H/2).','(m_{\\rm rel},n_{\\rm rel},A_M)&=\n           (6\\chi,3H-6\\chi,H/2-\\chi).')
 a=t.index(r'\item For an allowed index-one unimodular periodic fan')
 b=t.index(r'\par',a)
 t=t[:a]+r'''\item For an allowed fan, retain the full period functions and
apply \cref{night:P3K.73} with \(J=M\), reference data
\(H,\chi\), and the displayed source/cap endpoint.
For the actual shorter family use \(J=M/b\),
\(\widehat H=H/b,\widehat\chi=\chi/b\), through its explicit
covering morphism. The physical reference is
\(\widehat H/2-\widehat\chi\).
Pullback \(r=z^h\) composes \(h\) actual positive returns;
F50's displayed inverse-action map sends a large-scalar expanding
circle to the inverse return. The old norm polynomial is not used.

'''+t[b:]
 t=t.replace('on (SC.2), including the simultaneous Cox\nproduct used by K31. Thus the class (SC.6)\nbelongs to the constructed closed family.','on (SC.2), including its actual closed cusp endpoint atlas and reference fixed-star product. Its further fan values use the complete marked-prism construction of \\cref{night:P3K.73}.')
 t=t.replace('reference index is \\(A/b\\)','physical reference index is \\(A_M/b\\)')
 t=t.replace('and a checked primitive norm witness','and a historical primitive norm witness')
 t=t.replace('checks the full norm formulas just proved.\nAll 437 exact checks pass.','checks the full norm formulas just proved. Its 437 recorded checks are historical; the former all-fan polynomial fields in that output are refuted and are not used here.')
 return current_proof(t)
change('night:P3F.53',f53,'Keep both source/root tables, all exact norm solutions and source/cap/divisor morphisms; correct the physical reference and remove false polynomial/range fields while preserving historical certificate scope.')

def k35(t):
 a=t.index('Write the actual source line as');b=t.index(r'\end{theorem}',a);head=t[a:b]
 head=head.replace('The single positive \\(w\\)-loop has a closed simultaneous Cox product.','The single positive \\(w\\)-loop has the closed endpoint atlas and reference fixed-star framing constructed below.')
 head=head.replace('A_w=\\frac{\\chi-H/2}{b}.','A_{U,w}=\\frac{\\chi-H/2}{b},\qquad A_{M,w}=\\frac{H/2-\\chi}{b}.')
 q=head.index('For a fan with primitive');head=head[:q]+r'''For every fan the return is computed from these actual endpoint
maps and all full period units by \cref{night:P3K.73}, with
\(J=M/b,\widehat H=H/b,\widehat\chi=\chi/b\).
The old all-fan polynomial is refuted by the OS45 \(b=1\)
reference return \(3\). No homotopy-sphere class is divided.
'''
 t=statement(t,head)
 t=t.replace('5. Exact cyclic norm and simultaneous closed Cox origin.','5. Exact cyclic norm and closed cusp endpoint origin.')
 t=t.replace('Its index is \\(A_w=(4k_w-\\ell_w)/24\\), and the proved\nHopf transfer assigns the initial central class\n\\(A_w\\pmod{28}\\).','Its dual index is \\(A_{U,w}=(4k_w-\\ell_w)/24\\), and the explicit cap duality of \\cref{night:P3K.68} assigns the physical central class \\(A_{M,w}=-A_{U,w}\\pmod{28}\\).')
 t=t.replace('Applying K31 to the simultaneous product in (P3K.35.20)\nthen proves (P3K.35.5).','The full outer coefficient maps are retained in \\cref{night:P3K.73}; applying its marked-prism algorithm to this constructed shorter endpoint gives the remaining fan returns.')
 t=t.replace('4k_w-\\ell_w=24A_w','4k_w-\\ell_w=24A_{U,w}')
 return current_proof(t)
change('night:P3K.35',k35,'Keep all actual meromorphic source lifts, cap characters, norm roots, rational endpoint and covering naturality; replace the universal formula by the complete actual shorter-loop prism computation.')

def k37(t):
 a=t.index('Keep the exact source, component line');b=t.index(r'\end{theorem}',a);head=t[a:b]
 q=head.index('For every actual allowed fan');head=head[:q]+r'''Its physical reference value on the positive fan is zero; on the
negative fan the same actual shorter loop has class \(-k\), by
\cref{night:P3K.65}. The full fan transport is
\cref{night:P3K.77}. The old polynomial is refuted already at
\(k=1\) on the negative fan, where it gives zero and the actual
class is \(27\). These comparisons use the constructed covering
and endpoint maps, with no division in \(\Theta_7\).
'''
 t=statement(t,head)
 a=t.index(r'\par\medskip\noindent\textbf{7. Exact scalar-loop witnesses and the range.}')
 t=cut_tail(t,r'\par\medskip\noindent\textbf{7. Exact scalar-loop witnesses and the range.}',
 r'''The constructed endpoint, finite-root commuting square and
framed covering above remain the geometric descent proof.
The positive fan has the displayed dual pair \((-2k,-8k)\),
whose physical index is zero. The explicit component-normal
comparison of \cref{night:P3K.65} gives native pair \((-k,k)\)
for the negative-to-positive flop, hence negative class \(-k\).
At \(k=1\) this is \(27\), refuting the old zero at norm \(S=1\).
Every further fan is computed by \cref{night:P3K.77}; the old
polynomial witnesses and claimed even-only range are archived
with the rejected compound assertion.''')
 # Remove the obsolete invocation in the naturality step, preserving its
 # two integer characteristic pullbacks and all actual covering maps.
 t=re.sub(r'Applying K31[\s\S]*?(?=\\item|\\par\\medskip)',
 lambda m:r'The full fan transport is \cref{night:P3K.77}; no norm-polynomial deduction is made from this fixed-star covering.\n\n',t)
 return current_proof(t)
change('night:P3K.37',k37,'Keep all component-line, finite-root and actual shorter-parameter maps and free naturality; replace false polynomial/even-range claims with the actual -k/0 comparison and K77 transport.')

# The cap and moving-site proofs already give complete family morphisms.
# Only the old numerical substitution at their end is rejected.
def rewrite_iterate(t,kind):
 start={'P3K.41':'Fix a marked rational elliptic source','P3K.43':'Fix the marked rational elliptic source','P3K.44':'Fix the actual OS49 source'}[kind]
 a=t.index(start);b=t.index(r'\end{theorem}',a);head=t[a:b]
 if kind=='P3K.41':
  a=head.index('For the transported fan coordinate');b=head.index('The proof retains',a)
  head=head[:a]+r'''For the transported fan \(P\), write \(A_{
m short}(P)\)
for the actual shorter return computed by \cref{night:P3K.73}.
The oriented return is \(N A_{
m short}(P)\).
'''+head[b:]
 elif kind=='P3K.43':
  a=head.index('For the transported fan coordinate');b=head.index('The statement concerns',a)
  head=head[:a]+r'''For the transported fan \(P\), its oriented class is
\(N A_{
m short}(P)\), where \cref{night:P3K.73} computes the
actual shorter return from the full period and endpoint maps.
'''+head[b:]
 else:
  a=head.index('For the same transported fan');b=head.index('The statement keeps',a)
  head=head[:a]+r'''For the two fixed component-fan objects its classes are
\(N(-k)\) on the negative fan and \(0\) on the positive fan,
by \cref{night:P3K.65}. For a general transported fan \(P\)
the exact expression is \(N A_{
m short}(P)\), with
\(A_{
m short}(P)\) computed by \cref{night:P3K.77}.
'''+head[b:]
 t=statement(t,head)
 if kind=='P3K.43':
  a=t.index('For the fixed transported fan coordinate');b=t.index(r'\item This proves',a)
  t=t[:a]+r'''For the fixed transported fan \(P\), the actual class is
\(N A_{
m short}(P)\), where the endpoint just compared is the
input to \cref{night:P3K.73}. In the allowed OS45 constant-site
case \(N=1,P=T_0\), the result is \(3\), whereas the rejected
polynomial gave \(25\). This is the located counterexample.

'''+t[b:]
 elif kind=='P3K.44':
  a=t.index('In particular\nfixed scalar gives the trivial sphere bundle')
  b=t.index(r'\end{enumerate}',a)
  t=t[:a]+r'''In particular fixed scalar gives the trivial sphere bundle.
For the negative and positive component fans, respectively,
\cref{night:P3K.65} gives \(N(-k)\) and \(0\); for a transported
fan \(P\) the same actual arrow gives \(N A_{
m short}(P)\),
using \cref{night:P3K.77}. The case \(N=k=1\) on the negative
fan has class \(27\), contradicting the old norm polynomial's zero.
The scalar reduction has been proved by the literal forward
endpoint square and inverse-endpoint physical return above.

'''+t[b:]
 else:
  end=t.rindex(r'\end{enumerate}')
  t=t[:end]+r'''\item The actual OS45 datum has \(b=M=1\), \(H=8\),
\(\chi=1\), and physical reference return \(3\).
Taking this cap-data loop with \(N=1\) gives \(3\) through
(CP.10)--(CP.11), while the old numerical substitution gave
\(25\). The family-morphism reduction is retained; only that
substitution is refuted.

'''+t[end:]
 return current_proof(t)
for ident in ['P3K.41','P3K.43','P3K.44']:
 change('night:'+ident,lambda t,ident=ident:rewrite_iterate(t,ident),
 'Keep the complete Lie/cochain, scalar-winding, finite-kernel and actual endpoint-square proof; replace only the rejected numerical polynomial by the exact iterate of the constructed shorter return.')

subst('night:P3K.57',[
 ('positive \\(\\epsilon\\)-loop has Jin characteristic integer and oriented','positive \\(\\epsilon\\)-loop has the meridian-one dual characteristic integer and physical oriented'),
 ('(2,1)&1&1.','(2,1)&1&-1.'),
 ('Jin differences are respectively \\(0\\) and \\(+1\\).','meridian-one dual differences are respectively \\(0\\) and \\(+1\\).')
 ],'Preserve the complete source/root/line/annular maps, relative excision and all residue arithmetic; identify the computed index as dual and transfer it by the explicit physical cap map.',physical)

def k57_transfer(t):
 a=t.index(r'\item On the complement of that tube, P3F.22\textquotesingle s Hopf lift') if r'\item On the complement of that tube, P3F.22\textquotesingle s Hopf lift' in t else t.index(r"\item On the complement of that tube, P3F.22's Hopf lift")
 b=t.index(r'\item The old',a)
 return t[:a]+r'''\item On the free complement, apply the Hermitian line map
\(D_M:M^\times\to U^\times\) to the actual equivariant return.
It conjugates the lifted physical map to its meridian-one dual
lift and extends across the tube by
\((a,b)\mapsto(\overline b,-\overline a)\), with the full
\(SU(2)\) transition functions retained.
On the two cap pieces the first-to-second maps are
\(\lambda_M(F)=-\Sigma_{F^{-1}}\) and
\(\lambda_U(F)=\Sigma_{F^{-1}}\), as proved in
\cref{night:P3K.68}. Thus the computed characteristic difference
\(A_U=\int(4x^3-p_1x)/24\) gives physical class \(-A_U\).
The pair-of-pants endpoint maps (P3K.57.IE.14) identify this
relative difference with the fixed-scalar positive epsilon loop.
Its physical classes are therefore \(0\) for \((a,b)=(1,2)\)
and \(-1\) for \((a,b)=(2,1)\), on both specified vertical fan
objects. Every residue and Euler denominator above is retained;
the change is the explicitly proved cap/line transfer.

'''+t[b:]
change('night:P3K.57',k57_transfer,'Replace the false identification of the meridian-one Hopf lift with the physical lift by the full Hermitian/SU2 and first-to-second cap comparison.')
subst('night:P3K.37',[
 ("Its index is zero. K31's proved recurrence applies to the simultaneous Cox\nproduct just obtained, and substituting these two actual integers gives\n(P3K.37.3). The formula is integral because the physical cocharacter is primitive,\nso S is odd and \\((S-1)(S-3)\\) is divisible by eight.",
  'Its physical reference index is zero. The complete fan transport uses the actual outer maps in \\cref{night:P3K.77}; the reference fixed-star covering does not imply the rejected norm polynomial.')
 ],'Remove the remaining obsolete invocation of the old norm recurrence from the retained integer covering proof.')
subst('night:P3K.58',[
 ('(2,1,4p-1)&1 .','(2,1,4p-1)&-1 .'),
 ('Jin-to-\\(\\Theta_7\\) transfer of that excision.','dual-to-physical cap transfer of that excision, made explicit in \\cref{night:P3K.68}.')
 ],'Correct the intermediate fixed-scalar infinity table as well as the final cut-surface table; retain the actual scalar/endpoint relation.')
