"""Reproduce the K55 inline-math typesetting repair from the preserved source."""
from pathlib import Path
import datetime, hashlib, json, re, shutil

ROOT=Path(__file__).resolve().parents[2]
ATT=ROOT/'records/attempts/k55_inline_math_before_repair'
ATT.mkdir(parents=True,exist_ok=True)
src=ROOT/'notes/part3_source_cusp_general_fan_product_working.md'
old=ATT/src.name
if not old.exists():
    files=[src,ROOT/'notes/part3_source_cusp_general_fan_product.tex',
           ROOT/'code/part3_root/export_source_cusp_general_fan_product.py',
           ROOT/'records/k55_standalone.pdf',ROOT/'records/k55_standalone.log',
           ROOT/'records/k55_standalone_build.out',ROOT/'records/k55_standalone_build2.out',
           ROOT/'records/export_k55.out',ROOT/'records/export_k55.err']
    for f in files:
        if f.exists():shutil.copy2(f,ATT/f.name)
text=old.read_text()
replacements=[
("Let P be an integral two-by-two matrix with determinant +1 or -1, and\nwrite R=P^{-1}.",r"Let \(P\) be an integral two-by-two matrix with determinant \(+1\) or \(-1\), and"+'\n'+r"write \(R=P^{-1}\)."),
("under P of OE.1",r"under \(P\) of OE.1"),
("lattice point n have vertices",r"lattice point \(n\) have vertices"),
("The homogeneous lattice map is (x,h) to (Px,h); its determinant is\ndet P,",r"The homogeneous lattice map is \((x,h)\) to \((Px,h)\); its determinant is"+'\n'+r"\(\det P\),"),
("rows of P.",r"rows of \(P\)."),
("Replace their basis by h'_j=h^{P_{1j}}B^{P_{2j}}, for j=1,2.",r"Replace their basis by \(h'_j=h^{P_{1j}}B^{P_{2j}}\), for \(j=1,2\)."),
("integral period change R",r"integral period change \(R\)"),
("The power of q in the i-th character of h'_j is (RP)_{ij}.",r"The power of \(q\) in the \(i\)-th character of \(h'_j\) is \((RP)_{ij}\)."),
("At q=0",r"At \(q=0\)"),
("ratio of kappa as exp(-6i theta) times exp(f_kappa), and write the\nbased ratios of alpha,g,eta as exp(f_alpha), exp(f_g), exp(f_eta).",r"ratio of \(\kappa\) as \(\exp(-6i\theta)\) times \(\exp(f_\kappa)\), and write the"+'\n'+r"based ratios of \(\alpha,g,\eta\) as \(\exp(f_\alpha)\), \(\exp(f_g)\), \(\exp(f_\eta)\)."),
("The four f's",r"The four \(f\)'s"),
("ratio A_ij/A_ij,*",r"ratio \(A_{ij}/A_{ij,*}\)"),
("put (a,b,c)=T^+_0 and\n(u,v,w)=T^-_0.",r"put \((a,b,c)=T^+_0\) and"+'\n'+r"\((u,v,w)=T^-_0\)."),
("Each triple product is q.",r"Each triple product is \(q\)."),
("use (u,A_22 v,A_11 w)",r"use \((u,A_{22}v,A_{11}w)\)"),
("transition matrices are zD_i",r"transition matrices are \(zD_i\)"),
("For the based loops K_i=D_i,*^{-1}D_i,",r"For the based loops \(K_i=D_{i,*}^{-1}D_i\),"),
("even winding -6, including matrices\nP whose",r"even winding \(-6\), including matrices"+'\n'+r"\(P\) whose"),
("For an integer d define",r"For an integer \(d\) define"),
("where vartheta is",r"where \(\vartheta\) is"),
("satisfy H_d(0,theta)=1,\nH_d(1,theta)=exp(id theta).",r"satisfy \(H_d(0,\theta)=1\),"+'\n'+r"\(H_d(1,\theta)=\exp(id\theta)\)."),
("At s=1 its two complex normal factors are exp(i l_i theta)\nand exp(i(-6-l_i)theta), respectively: left and right quaternion\nphases with exponents x,y give complex exponents x+y,x-y.",r"At \(s=1\) its two complex normal factors are \(\exp(il_i\theta)\)"+'\n'+r"and \(\exp(i(-6-l_i)\theta)\), respectively: left and right quaternion"+'\n'+r"phases with exponents \(x,y\) give complex exponents \(x+y,x-y\)."),
("the full K_i.",r"the full \(K_i\)."),
("At P=I the right factor on C_0 and C_2 is H_3, while OP.8 used\nH_{-3}^{-1}. We retain their exact comparison. Set a=sin vartheta,\nb=cos vartheta and n=a i-b k,",r"At \(P=I\) the right factor on \(C_0\) and \(C_2\) is \(H_3\), while OP.8 used"+'\n'+r"\(H_{-3}^{-1}\). We retain their exact comparison. Set \(a=\sin\vartheta\),"+'\n'+r"\(b=\cos\vartheta\) and \(n=ai-bk\),"),
("Conjugation by n fixes n and sends j to -j. Consequently\nn H_d^{-1}n^{-1}=H_{-d}.",r"Conjugation by \(n\) fixes \(n\) and sends \(j\) to \(-j\). Consequently"+'\n'+r"\(nH_d^{-1}n^{-1}=H_{-d}\)."),
("joins OP's right factor to H_3. It is fixed at s=0, where H=1,\nand at s=1, where n=i",r"joins OP's right factor to \(H_3\). It is fixed at \(s=0\), where \(H=1\),"+'\n'+r"and at \(s=1\), where \(n=i\)"),
("Send (z,n) to (z,K_i(s(|z|),theta)n)",r"Send \((z,n)\) to \((z,K_i(s(|z|),\theta)n)\)"),
("collar identity zD_i,*K_i=zD_i",r"collar identity \(zD_{i,*}K_i=zD_i\)"),
("normal rescaling R_t(z,n)=(z,tn)",r"normal rescaling \(R_t(z,n)=(z,tn)\)"),
("The first normal pairs are (a,c),(a,b),(b,c).",r"The first normal pairs are \((a,c),(a,b),(b,c)\)."),
("exactly z'=z^{-1}, n'=zn.",r"exactly \(z'=z^{-1}\), \(n'=zn\)."),
("has degree -6",r"has degree \(-6\)"),
("pure-left endpoint L^6.",r"pure-left endpoint \(L^6\)."),
("with L^6;",r"with \(L^6\);"),
("weights (xi,upsilon)^T=R e_2. At the first vertex its weights on\n(a,b,c) are (-xi-upsilon,xi,upsilon); at the second they are\n(xi+upsilon,-upsilon,-xi).",r"weights \((\xi,\upsilon)^T=Re_2\). At the first vertex its weights on"+'\n'+r"\((a,b,c)\) are \((-\xi-\upsilon,\xi,\upsilon)\); at the second they are"+'\n'+r"\((\xi+\upsilon,-\upsilon,-\xi)\)."),
("physical normal action on Q",r"physical normal action on \(Q\)"),
("by exp(-i w_i phi/2) and right multiplication by exp(i d_i phi/2).",r"by \(\exp(-iw_i\phi/2)\) and right multiplication by \(\exp(id_i\phi/2)\)."),
("z to exp(i w_i phi)z. On the positive radial path z=tan chi,\nwrite U=cos chi+j sin chi and E_i=exp(i w_i phi/2). The moved\nHopf representative is exactly E_i^{-1}UE_i. At q_H=1",r"\(z\) to \(\exp(iw_i\phi)z\). On the positive radial path \(z=\tan\chi\),"+'\n'+r"write \(U=\cos\chi+j\sin\chi\) and \(E_i=\exp(iw_i\phi/2)\). The moved"+'\n'+r"Hopf representative is exactly \(E_i^{-1}UE_i\). At \(q_H=1\)"),
("This includes w_i=0: its left A factors",r"This includes \(w_i=0\): its left \(A\) factors"),
("at phi=2pi",r"at \(\phi=2\pi\)"),
("At phi=2pi",r"At \(\phi=2\pi\)"),
("because w_i and d_i",r"because \(w_i\) and \(d_i\)"),
("periodic in theta",r"periodic in \(\theta\)"),
("theta-independent",r"\(\theta\)-independent"),
("For d=0 the map is constant. For d nonzero, the inverse images\nof -i under H_d i H_d^{-1} have vartheta=pi/4 and exp(id theta)=-1.\nThere are |d| of them. At each, H_d=j,",r"For \(d=0\) the map is constant. For \(d\) nonzero, the inverse images"+'\n'+r"of \(-i\) under \(H_diH_d^{-1}\) have \(\vartheta=\pi/4\) and \(\exp(id\theta)=-1\)."+'\n'+r"There are \(|d|\) of them. At each, \(H_d=j\),"),
("Since (k,j) is the positive outward tangent basis at -i, the\ndegree is -d. For H_d^{-1}iH_d the first derivative changes\nsign and the second remains -d j, giving degree d.\nThus the axes A i A^{-1} and B_i^{-1}iB_i have degrees\n3 and l_i+3. Conjugating the first by U preserves its degree\nthrough U_t=cos(t chi)+j sin(t chi);",r"Since \((k,j)\) is the positive outward tangent basis at \(-i\), the"+'\n'+r"degree is \(-d\). For \(H_d^{-1}iH_d\) the first derivative changes"+'\n'+r"sign and the second remains \(-dj\), giving degree \(d\)."+'\n'+r"Thus the axes \(AiA^{-1}\) and \(B_i^{-1}iB_i\) have degrees"+'\n'+r"\(3\) and \(l_i+3\). Conjugating the first by \(U\) preserves its degree"+'\n'+r"through \(U_t=\cos(t\chi)+j\sin(t\chi)\);"),
("The axis U i U^{-1}",r"The axis \(UiU^{-1}\)"),
("Factor (GF.15) into E_i^{-1}, exp(i w_i phi Ad_U(i)/2),\nexp(-i w_i phi Ad_{UA}(i)/2), and\nexp(i d_i phi Ad_{B_i^{-1}}(i)/2).",r"Factor (GF.15) into \(E_i^{-1}\), \(\exp(iw_i\phi\,\operatorname{Ad}_U(i)/2)\),\newline"+'\n'+r"\(\exp(-iw_i\phi\,\operatorname{Ad}_{UA}(i)/2)\), and"+'\n'+r"\(\exp(id_i\phi\,\operatorname{Ad}_{B_i^{-1}}(i)/2)\)."),
("volume gives degree a d for an axis of degree d and\nangle a phi/2, for every integer a.",r"volume gives degree \(ad\) for an axis of degree \(d\) and"+'\n'+r"angle \(a\phi/2\), for every integer \(a\)."),
("GL^+ and",r"\(GL^+\) and"),
("has stable degree deg(left)-deg(right).",r"has stable degree \(\deg(\mathrm{left})-\deg(\mathrm{right})\)."),
("the phi variable",r"the \(\phi\) variable"),
("(-1)^{w_i}, while",r"\((-1)^{w_i}\), while"),
("product is +1.",r"product is \(+1\)."),
("times D4",r"times \(D^4\)"),
("by D2_theta times S1_phi",r"by \(D^2_\theta\) times \(S^1_\phi\)"),
("in its D2 variable",r"in its \(D^2\) variable"),
("has class\nI_i m_i",r"has class"+'\n'+r"\(I_im_i\)"),
("graph loops gamma_j=a_j-a_0",r"graph loops \(\gamma_j=a_j-a_0\)"),
("two-chains x_j",r"two-chains \(x_j\)"),
("with weight w_i has degree -w_i",r"with weight \(w_i\) has degree \(-w_i\)"),
("identity is partial Delta=-Delta partial.",r"identity is \(\partial\Delta=-\Delta\partial\)."),
("Let V be the actual",r"Let \(V\) be the actual"),
("fan and delta its actual",r"fan and \(\delta\) its actual"),
("The matrix V is symmetric",r"The matrix \(V\) is symmetric"),
("generate\nH3",r"generate"+'\n'+r"\(H_3\)"),
("At P=I, (l_i)=(0,-6,0), (w_i)=(0,1,-1),\n(d_i)=(-2,-1,-1); the formulas give I=(-6,0,0) and W=(6,-6,6).",r"At \(P=I\), \((l_i)=(0,-6,0)\), \((w_i)=(0,1,-1)\),"+'\n'+r"\((d_i)=(-2,-1,-1)\); the formulas give \(I=(-6,0,0)\) and \(W=(6,-6,6)\).")
]
counts=[]
for a,b in replacements:
    count=text.count(a)
    if count==0:raise ValueError('Missing exact source phrase: '+a)
    text=text.replace(a,b);counts.append({'old':a,'new':b,'count':count})
src.write_text(text)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'APPLIED','scope':'Inline mathematical typesetting only; exact displayed formulas and proof substance retained.',
        'original_source':str(old.relative_to(ROOT)),'source':str(src.relative_to(ROOT)),
        'replacements':counts,'original_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
        'repaired_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(ROOT/'records/k55_inline_math_repair.json').write_text(json.dumps(record,indent=2)+'\n')
print(f'Applied {len(counts)} explicit inline-format repairs; original source, TeX, PDF, exporter and logs retained.')
