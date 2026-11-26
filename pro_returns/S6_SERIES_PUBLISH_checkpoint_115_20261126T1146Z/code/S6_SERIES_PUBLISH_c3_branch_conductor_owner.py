from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
assert 'tag-P251' not in s
lemma=r'''\begin{lemma}[Conductor ideals of hypersurface branches]\hypertarget{tag-P251}{}\label{lem:II:hypersurface-branch-conductor}
\StatementRecord{lem:II:hypersurface-branch-conductor}{proved}{P251}{}
Let $R$ be the local analytic ring of a smooth complex manifold and let $f_1,\ldots,f_r$ be pairwise nonassociate irreducible elements. Put
\[
 A=R/(\textstyle\prod_i f_i),\qquad A_i=R/(f_i),\qquad
 g_i=(\textstyle\prod_{j\ne i}f_j)|_{A_i},
\]
and let $B_i$ normalize $A_i$. Write $\mathfrak c_i=\{b\in B_i:bB_i\subset A_i\}$ for its intrinsic conductor. Under the normalization map $A\hookrightarrow B=\prod_i B_i$, the conductor is
\[
 \mathfrak c_{B/A}=\prod_i g_i\mathfrak c_i.
\]
The identification of its $i$th summand with $\mathfrak c_i$ is multiplication by the nonzero element $g_i$.
\end{lemma}
\begin{proof}
The ring $R$ is factorial. Thus $\bigcap_{j\ne i}(f_j)=(\prod_{j\ne i}f_j)$, and the elements of $A$ supported only on the $i$th branch have $i$th components exactly $g_iA_i$. An element $b=(b_i)\in B$ lies in the conductor precisely when multiplication by every element supported on one branch stays in $A$, namely when $b_iB_i\subset g_iA_i$ for every $i$. Taking the multiplier $1$ gives $b_i=g_i a_i$ with $a_i\in A_i$. Since $g_i$ is a nonzerodivisor in the domain $B_i$, division by $g_i$ identifies the preceding condition with $a_iB_i\subset A_i$, or $a_i\in\mathfrak c_i$. This proves the formula and both directions of its multiplication-map identification.
\end{proof}

'''
at=s.index('\\label{lem:II:conductor-duality}')
end=s.index('\\end{proof}',at)+len('\\end{proof}')
after=s[:end]+'\n\n'+lemma+s[end:]
old=r'''For a reduced hypersurface $\prod_i f_i=0$, the conductor on the normalized $i$th branch is its intrinsic conductor multiplied by $\prod_{j\ne i}f_j$ restricted to that branch. Indeed, an ambient function vanishing on every other branch is divisible by that product, since the $f_j$ are distinct irreducibles in the regular local ring. Dividing its $i$th component by this nonzerodivisor identifies the conductor condition with the intrinsic condition $bB_i\subset R_i$. On the quadratic branch the other factors pull back to $vu^2$, giving $v^2u^2B$. On $x=0$ their product is $zy^2$, and on $z=0$ it is $xy^2$. These ideals give the stated divisors; their reduced supports are normal-crossing pairs.'''
new=r'''Apply \cref{lem:II:hypersurface-branch-conductor} in $R=\mathbb C\{x,y,z\}$ to the three factors $x,z,y^2-x^2z$. On the quadratic branch its normalization map $(v,u)\mapsto(v,vu,u^2)$ sends the other-factor product $xz$ to $vu^2$. Multiplication by this element sends the intrinsic conductor $vB$ to $v^2u^2B$, exactly as in the lemma. On $x=0$ the other-factor product is $zy^2$, and on $z=0$ it is $xy^2$; these two branches are smooth, so their intrinsic conductors are their full local rings. These ideals give the stated divisors; their reduced supports are normal-crossing pairs.'''
assert after.count(old)==1;after=after.replace(old,new,1)
oldplane=r'''The conductor is the product of the ideals $(t_i^{c_i})$ in the normalization, so the second length is $\sum_i c_i$. Applying the same argument to the individual branch ring gives $c_i^{\rm int}=2\delta(C_i)$.'''
newplane=oldplane+r''' Apply \cref{lem:II:hypersurface-branch-conductor} in $R=\mathbb C\{x,y\}$ to these same factors $f_i$. Its multiplication map by $g_i=\prod_{j\ne i}f_j|_{C_i}$ adds $\operatorname{ord}_{t_i}g_i=\sum_{j\ne i}I(C_i,C_j)$ to the intrinsic conductor exponent, proving the branch formula.'''
assert after.count(oldplane)==1;after=after.replace(oldplane,newplane,1)
oldres=r'''The additional pole of $dx/h_y$ relative to $dx/(f_i)_y$ therefore has order $\sum_{j\ne i}I(C_i,C_j)$. The displayed conductor-module identity gives the claimed branch formula. Intersection multiplicities of distinct plane branches are positive integers.'''
newres=r'''Thus the residue generators realize the same multiplication by $g_i$ in the conductor formula, with the unit $u|_{C_i}$ invertible. Intersection multiplicities of distinct plane branches are positive integers.'''
assert after.count(oldres)==1;after=after.replace(oldres,newres,1)
preserve_identifiers(s,after)
for oldids,newids in zip(identifiers(s),identifiers(after)):
    for name,count in oldids.items():assert newids[name]==count,name
SOURCE.write_text(after,newline='\n')
rows=[]
for key,stmt,before,receiving,reason in [
 ('COMMON','lem:II:hypersurface-branch-conductor',old,lemma,'Extract the existing hypersurface branch-conductor multiplication proof at its exact dimension-independent local-ring scope. The inverse map is division by the displayed nonzerodivisor; every branch ring and normalization map is retained.'),
 ('SURFACE','ex:II:vanishing-cubic-aspherical',old,new,'Apply the common formula to the identical three factors and normalization coordinates, retaining every conductor ideal and divisor.'),
 ('PLANE','lem:II:plane-branch-conductor',oldplane+'\n'+oldres,newplane+'\n'+newres,'The same multiplication formula applies to the plane local ring and gives the branch exponent. The full finite-duality length proof and meromorphic-differential comparison remain, including the residue formula needed by later conormal calculations.')]:
    for i,kind in enumerate(['D12','D14'],1):
        rows.append(dict(change_id=f'II-C3-BRANCH-CONDUCTOR-{key}-{i:02}',type=kind,statement_id=stmt,
          old_location='Binary products and cubic jets; plane-branch conductor',old_page='working source; final concordance pending',
          new_location='Duality and normal surface geometry; exact local applications',new_page='integrated build pending',
          old_text=before,new_text=receiving,reason=reason,
          review_status='Root read complete receiving common lemma and both complete affected proofs against original text. Exposed comparison only.'))
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
add_event('lem:II:hypersurface-branch-conductor; ex:II:vanishing-cubic-aspherical; lem:II:plane-branch-conductor',
 'II-C3-ROOT-BRANCH-CONDUCTOR-TRANSFER','used and rechecked in this run',
 'Root read the complete old and receiving P231 and P282 proofs and the new common P251 proof. Verified A→product B_i, the i-supported submodule g_i A_i, multiplication and division by g_i, and the conductor condition on every branch. The surface application uses factors x,z,y²−x²z and the exact map (v,u)→(v,vu,u²); the plane application uses the same f_i and valuations equal to local intersection multiplicities. All length and finite-duality residue arguments remain. No independent credit; no unit migration or final rendering credit.',
 'S6_SERIES_PUBLISH_II.tex: common conductor and its two local applications',source='code/S6_SERIES_PUBLISH_c3_branch_conductor_owner.py')
print('Common branch-conductor multiplication map and two exact applications admitted.')
