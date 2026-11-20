from pathlib import Path
import json,hashlib,re
P=Path(__file__).resolve().parents[1];W=P.parent
s=(W/'parts/IV.body.linked.tex').read_text();patches=[]
def add(label,old,new,reason):
 a=s.index('\\label{'+label+'}');b=s.index('\\end{proof}',a)+len('\\end{proof}');assert s[a:b].count(old)==1,(label,old[:80],s[a:b].count(old))
 patches.append(dict(label=label,old_text=old,new_text=new,reason=reason))
statements={
1:r'''For relatively minimal rational elliptic surfaces over \(\mathbb C\) with a chosen zero section, the torsion-free rank-one Mordell--Weil rows in the cited Oguiso--Shioda table are exactly eight. Their Kodaira refinements give exactly twenty-one realized configurations.''',
2:r'''For the sections of the rational elliptic surfaces in \cref{night:P3F.1}, use Shioda's height and local component corrections. The exact formula is
\[
 (P\mathbin{\cdot}O)=\frac{h(P)-2\chi(\mathcal O_S)+\sum_v\operatorname{contr}_v(P)}2.
\]
Every primitive Mordell--Weil generator in the eight torsion-free rank-one rows has \(P\mathbin{\cdot}O=0\).''',
5:r'''Retain the compact genus-three, degree-twelve elliptic pullback page of \cref{night:P3F.6}, with fibre class \(F\) and physical point line \(M=\mathcal O(P-O)\). Its canonical class is \(K=5F\). After removing a small ball disjoint from its section, the class \(w_2=F\bmod2\) remains nonzero and obstructs the specified even normal Euler class \(2c_1(M)\) in a spin six-manifold. The characteristic class \(K+2c_1(M)\) has square \(4c_1(M)^2\). The cited Haefliger formula uses an actual Seifert surface and its actual normal Euler class.''',
6:r'''Let \(C\) be the compact normalization of \(b^3=a^4+1\), put \(x=b^3\), and choose a regular binding value \(t_*\in\mathbb P^1\setminus\{0,1,\infty\}\). Pull back the marked original elliptic source, with fibres \(IV^*,III,I_1\) over \(0,1,\infty\), by the two maps
\[
 t=x,\qquad t=\frac{t_*x}{x+t_*-1}.
\]
After the displayed good-reduction minimalizations, the maps give respectively one \(I_{12}\) fibre and twelve \(I_1\) fibres. Both completed pages have \(\chi(\mathcal O)=1\), signature \(-8\), height \(h(P)=2\) for the pulled-back source section, and \((mP)\mathbin{\cdot}O=m^2-1\).''',
7:r'''Retain the AC26 reference sphere and its reference cusp fan, identified explicitly in \cref{iv:source_transports}, with the literal cocharacter \(e_2=\widehat\delta\). Its circle orbit pair is \((S^5,S^2)\); the fixed normal bundle is \(\mathcal O(-1)\oplus\mathcal O(-1)\) with weights \((-1,+1)\). The specified equivariant conifold replacement is free with quotient \(S^2\times S^3\).''',
8:r'''Retain the parameter loop and sixfold marking of \SeriesRef{night:P2.1}, the complex orientation, and the reference fan and \(e_2\)-circle of \cref{night:P3F.7}. The actual positive equivariant return \(\Phi\), trivialized on the fixed normal tube, descends to a Torelli map \(f\) of \(S^2\times S^3\). The explicit cut-and-reglue map in the proof identifies the oriented sphere clutched by \(\Phi\) with the Hopf gluing \(\lambda(f)\) of \cref{night:P3F.4}.''',
9:r'''For the reference cusp model and specified small resolution used in \cref{night:P3F.7}, retain the opposite physical-circle weights, the marked \(\gamma\)-circle and the prescribed outer stable framing. The resolved cusp orbit has a relative product comparison with a nodal elliptic neighbourhood times that marked circle, and the derivative of the comparison preserves the given stable outer framing up to the displayed relative homotopy.''',
10:r'''Retain the original sphere twists \((0,1,-1)\), the reference cusp fan, the marked \(\gamma\)-circle and stable boundary comparison of \cref{night:P3F.9}. Choose the regular binding over \(t_*\notin\{0,1,\infty\}\), with the physical circle line \(M=\mathcal O(P-O)\). The resulting page has twelve positive nodal fibres and boundary \(T^3\). Its circle-line square is \(s_\delta=-2\), and its relative Pontryagin pairing in this boundary framing is \(p_{\rm rel}=-24\).''',
11:r'''For the equivariant family and normal weight lines of \cref{night:P3F.7,night:P3F.8}, use the Jin coordinates of \cref{night:P3F.3} and the retained sixfold parameter marking. The integer \(A=(4k-\ell)/24\) is independent of the equivariant normal trivialization and is additive under actual collar concatenation. Six parameter loops give six times the integer of one loop.''',
12:r'''Let \(C\) be the compact normalization of the actual component cover \(y^{12}=t^4/(t-1)^3\) in \SeriesRef{night:P2.2}, with its specified \(I_{12}\) extension and pulled-back point \(P\). The compact fixed-sheet torsor is smoothly translation-trivial through that model. Under the displayed translation isomorphism, its physical circle line differs from \(\mathcal O(P-O)\) by the pullback of a line on \(C\), hence by an integral fibre class in its first Chern class.''',
14:r'''Let \(S\) be the compact complex fixed surface with normal lines \(L_+,L_-\) of circle weights \(+1,-1\), and put \(a=c_1(L_+)\), \(b=c_1(L_-)\), \(d=c_1(TS)\). For
\[
 \pi:B=\mathbb P(L_+\oplus\overline{L_-})\longrightarrow S,
\]
use the meridian-one hyperplane line \(U\), \(x=c_1(U)\), and the inherited spin\(^{c}\) determinant \(D=\pi^*(d+a+b)\). Its twisted index is
\[
 \int_B e^{D/2}e^x\widehat A(TB)=\chi(S,L_+).
\]
The physical-line application uses the extending map \(U=M^{-1}\) of \cref{night:P3K.68}.''',
16:r'''For the labelled comb smoothing of \cite[Section~7, equations~(7.1)--(7.3), pp.~23--24, Proposition~7.3 and Remark~7.4, pp.~25--26]{Viaclovsky2026Combs}, let \(s\) be its smoothing parameter. The actual glued smooth family over a sufficiently small punctured \(s\)-disc is a product by the single-valued radial trivialization constructed below. Its positive parameter loop therefore has identity smooth monodromy.''',
18:r'''Retain the two one-logarithmic constructions, source point lines \(M=P-O\), translations by \(2P\), scalar linearizations and order-four finite caps listed below from \cite{Viaclovsky2026Two,LiuRollenske2026}. Their regular-binding pages have degree-four covers of the source base. The Viaclovsky page has twelve \(I_1\) fibres; the Liu--Rollenske page has four \(II\) fibres and four \(I_1\) fibres. Both sectioned completions have \(\chi(\mathcal O)=1\), signature \(-8\), \(h(P)=2\) and \((P-O)^2=-2\).''',
21:r'''Use the explicit \(I_7+III+I_1+I_1\) rational elliptic surface and generator \(G=(1+4t,12\sqrt3\,t^2)\) in the proof, with the chosen nodal zero of its linearization. Retain its displayed primitive rank-one fillings, unit-square two-period cusp fan, and order-four affine cap. For the physical line \(M=\mathcal O(7G-O)\) and source translation by \(-Q=-2G\), the construction gives an actual holomorphic sphere family over \(\lambda=r^4\) in the stated strict contraction domain. Its regular-binding page has \(s_\delta=-14\) and \(p_{\rm rel}=-72\); the physical circle action is semifree through the entire \(I_7\) filling.''',
23:r'''Retain the source, physical line, chosen roots, affine cap and cusp marking of \cref{night:P3F.21}, with \(\lambda=r^4\). The positive \(r\)-loop has angular clutch \(\theta\gamma+2\theta(\theta-1)\delta\), hence one positive \(\gamma\)-turn. Its fourth-root cusp deck gauge has winding \(+4\), with the inverse closing evaluated in the displayed marked source coordinates.''',
24:r'''Let \(\Phi\) be an orientation-preserving diffeomorphism of the oriented six-sphere, with the boundary-identification convention in the proof. For the forward seam \((x,1)\sim(\Phi(x),0)\), the mapping torus is orientation-preservingly diffeomorphic to \((S^1\times S^6)\#\Sigma_\Phi\). Both spin structures have Eells--Kuiper invariant \(\mu(\Sigma_\Phi)\). A nonzero value excludes a diffeomorphism with the product in either orientation.'''
}
for n,new in statements.items():
 label=f'night:P3F.{n}';a=s.index('\\label{'+label+'}');b=s.index('\\end{theorem}',a);t=s[a:b]
 # The statement is the final paragraph after the apparatus and any dependency-scope paragraph.
 if '\\par\\noindent\\textit{Dependency scope.}' in t:old=t[t.rfind('\n\n\n')+3:].strip()
 else:
  lines=t.splitlines();start=next(i for i,line in enumerate(lines) if line.startswith('\\StatementRecord'))+1;old='\n'.join(lines[start:]).strip()
 assert old and '\\StatementRecord' not in old
 add(label,old,new,'State only the already proved source, parameter, line, fan and boundary hypotheses explicitly; no mathematical scope is enlarged.')
add('night:P3F.7',r'These identities are independently checked from the ray matrices in code/part3/orbit\_mv.py.',r'The two displayed transition equations give the stated normal degrees and circle weights. Substitution in the following coordinate map checks the conifold equation directly.','Keep the actual chart calculation and remove the unavailable historical program claim; no historical replay is asserted.')
add('night:P3F.7',r'All matrices and their Smith forms are printed in orbit\_mv.out.',r'The determinant, the conifold coordinate identity and the smooth \(SU(2)\) contraction are checked by \path{code/current_audits/audit_corrections/code/independent_IV_low_F_completion.py}, with exact output in \path{code/current_audits/audit_corrections/code/independent_IV_low_F_completion.json}.','Name the supplied fresh calculation at its exact matrix/conifold/clutch scope, without claiming new Smith-form files.')
add('night:P3F.7',r'C\_n\^{}q=0',r'\(C_n^q=0\)','Mathematical caret typography only.')
add('night:P3F.12',r'The program compact\_torsor.py prints this matrix, its determinant and Smith form; root\'s independent full Schreier enumeration is in torsor\_schreier.py.',r'The exact calculation in \path{code/current_audits/audit_corrections/code/independent_IV_low_F_completion.py} multiplies the literal matrices \(ABA^{-1}B^{-1}\), verifies that their cyclic-cover character is zero, and obtains \(\det(G-I)=-1\). Thus \((G-I)\Lambda_E=\Lambda_E\), which already kills the full integral coinvariant group. Its output is \path{code/current_audits/audit_corrections/code/independent_IV_low_F_completion.json}.','The direct commutator method supplies the needed integral surjectivity; no fresh full Schreier enumeration is claimed.')
add('night:P3F.12',r'q=Q\^{}12',r'\(q=Q^{12}\)','Restore the exact mathematical power.')
add('night:P3F.12',r'Q\^{}n times a unit',r'\(Q^n\) times a unit','Restore the exact mathematical power.')
add('night:P3F.12',r'sheaf A\^{}0',r'sheaf \(\mathcal A^0\)','Restore the translation-sheaf superscript.')
add('night:P3F.14',r'spin\^{}c determinant D=pi\^{}*\(d+a+b\)',r'spin\(^{c}\) determinant \(D=\pi^*(d+a+b)\)','Restore the determinant pullback and spin-c typography.')
add('night:P3F.14',r'degree-six spin\^{}c index',r'degree-six spin\(^{c}\) index','Restore spin-c typography.')
add('night:P3F.15',r'rho\^{}\(-1\)',r'\(\rho^{-1}\)','Restore the Laurent exponent.')
add('night:P3F.21',r'The complete nine-row coset table and its exact verification are in \texttt{os47\_topology.json}.',r'The program \path{code/current_audits/audit_corrections/code/independent_IV_OS47_topology.py} derives the nine-row table by Todd--Coxeter enumeration and checks its based bijection to these labelled permutations; the full table and bijection are saved in \path{code/current_audits/audit_corrections/code/independent_IV_OS47_topology.json}.','The fresh output actually contains the complete coset table, based bijection and displayed S,R,T permutations; no historical file is asserted.')
# Apply only to a private string for exact guards and preservation assertions.
out=s
for p in patches:
 a=out.index('\\label{'+p['label']+'}');b=out.index('\\end{proof}',a)+len('\\end{proof}');t=out[a:b];assert t.count(p['old_text'])==1;(None)
 t=t.replace(p['old_text'],p['new_text']);out=out[:a]+t+out[b:]
assert re.findall(r'\\tag\{([^}]+)\}',s)==re.findall(r'\\tag\{([^}]+)\}',out)
assert re.findall(r'\\label\{([^}]+)\}',s)==re.findall(r'\\label\{([^}]+)\}',out)
assert s.count('\\begin{proof}')==out.count('\\begin{proof}') and s.count('\\end{proof}')==out.count('\\end{proof}')
(P/'IV_low_F_scope_and_residual_patches.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
(P/'IV_low_F_scope_and_residual_receipt.json').write_text(json.dumps({'patches':len(patches),'statement_patches':len(statements),'input_sha256':hashlib.sha256(s.encode()).hexdigest(),'private_result_sha256':hashlib.sha256(out.encode()).hexdigest(),'all_guards_matched':True,'all_equation_tags_and_labels_preserved':True,'proof_balance_preserved':True,'shared_body_changed':False},indent=2)+'\n')
print(json.dumps({'patches':len(patches),'statement_patches':len(statements),'all_guards_matched':True}))
