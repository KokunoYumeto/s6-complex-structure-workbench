#!/usr/bin/env python3
from pathlib import Path
import sys,json,hashlib,datetime,re,collections
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent;BLOCKS=OUT/'G3_G4_blocks';BLOCKS.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT/'code'));from S6_SERIES_PUBLISH_II_packets import parse_source
src=ROOT/'S6_SERIES_PUBLISH_II.tex';data=parse_source(src,'II');s=data['text'];sha=lambda b:hashlib.sha256(b if isinstance(b,bytes) else b.encode()).hexdigest()
G3=r'''\begin{proposition}[Two projective torus fibrations]\hypertarget{tag-01G3}{}\label{cdp:st:D.1.5}
\StatementRecord{cdp:st:D.1.5}{proved}{01G3}{\citet[Section~10.5, p.~91]{AC2026}}
Let $E_0=F_0=E'=\C/(\Z+i\Z)$ and $a=1/2\in E_0$.
The involution
\[
(e,z)\longmapsto(e+a,-z)
\]
acts freely on $E_0\times F_0$. Put
$S=(E_0\times F_0)/\langle(a,-1)\rangle$,
$Y=S\times E'$, and $C=E_0/\langle a\rangle$.
The induced map $Y\to C$ is a smooth torus fibration with fibre
$F_0\times E'$ and monodromy
$\operatorname{diag}(-I_2,I_2)$ around the nontrivial deck character.
Its integral homology coinvariants are
$\Z^2\oplus(\Z/2\Z)^2$. After removing $s\geq1$ fibres,
\[
H_1(U;\Z)=\Z^{s+3}\oplus(\Z/2\Z)^2.
\]
The sum of the first Betti numbers of the punctured base and the
fibre is $s+5$.

Let $\eta$ be the nontrivial order-two degree-zero line bundle on
$C$ associated to the double cover $E_0\to C$. The coherent direct
images are
\[
R^1f_*\OO_Y=\eta\oplus\OO_C,\qquad R^2f_*\OO_Y=\eta.
\]
The cohomology dimensions are $h^q(Y,\OO_Y)=(1,2,1,0)$.
Restriction from $H^1(Y,\OO_Y)$ to the two-dimensional
$H^1(F_0\times E',\OO)$ has image precisely the $E'$ direction
and has rank one. These homomorphisms are induced by the finite
\'etale quotient and projection, and $b_1(Y)=4$.

For an example over $\PP^1$, let
$h:R\to\PP^1$ be the relatively minimal elliptic surface with
Weierstrass equation
\[
y^2=x^3+(t^4+1)x+t^6.
\]
Its fundamental line bundle is $\OO(1)$ and its discriminant has
twelve simple zeroes. Moreover, $R^1h_*\OO_R=\OO(-1)$.
For $Y'=R\times E'\to\PP^1$, the product K\"unneth maps give
\[
R^1f_*\OO_{Y'}=\OO\oplus\OO(-1),\qquad
R^2f_*\OO_{Y'}=\OO(-1),
\]
and restriction in degree one again has rank one. This projective
threefold has $b_1=2$, $b_2=11$ and $a=3$.
\end{proposition}
\begin{proof}
The first construction specializes the bielliptic example of
\citet[Section~10.5, p.~91]{AC2026} to the displayed involution.
Translation by $a$ has no fixed point, so the quotient is smooth.
The map $[e]\mapsto([e,0],0)$ is a section of the fibration. Over
the punctured base its fundamental group is therefore the semidirect
product of the fibre lattice and the free base group of rank $s+1$.
The map $(k,q)\mapsto([q],[k])$ identifies its abelianization with
the direct sum of the base abelianization and the fibre coinvariants:
the relations are $\rho(q)k-k$, which here are twice the two
$F_0$ generators. The same section over the complete elliptic base
gives the stated value of the first Betti number.

On the covering product, the three antiholomorphic one-form
directions have signs $(1,-1,1)$. Descent of the fibre cohomology
gives the two direct images, and taking invariants in the exterior
algebra gives the stated cohomology dimensions. The base direction
restricts to zero on a fibre, while the invariant fibre direction is
exactly that of $E'$. This proves the description of the restriction
map.

For the Weierstrass surface, the coordinates $u=1/t$,
$x'=u^2x$, $y'=u^3y$ give
\[
y'^2=x'^3+(1+u^4)x'+1.
\]
The relative residue differential transforms by
$dx'/(2y')=u^{-1}dx/(2y)$, so the fundamental line is
$\OO_{\PP^1}(1)$. Its discriminant is
\[
-16P(t),\qquad P(t)=31t^{12}+12t^8+12t^4+4=Q(t^4),
\qquad Q(z)=31z^3+12z^2+12z+4.
\]
The identity
\[
\left(\frac5{36}-\frac{31z}{54}\right)Q(z)
+\left(\frac1{27}-\frac{7z}{324}+\frac{31z^2}{162}\right)Q'(z)=1
\]
shows that the roots of $Q$ are simple; its constant term is
nonzero. Thus $P$ has twelve simple zeroes. At infinity the
transformed discriminant is $-16\cdot31$, so the fibre there is
smooth. The twelve singular fibres are nodal cubics. Relative
duality gives the stated first direct image. Leray gives
$h^1(R,\OO_R)=h^2(R,\OO_R)=0$; the twelve nodal fibres give
$e(R)=12$, and hence $b_1(R)=0$ and $b_2(R)=10$.
K\"unneth now gives both direct images and the Betti numbers of
the product. Its degree-one coherent cohomology is the $E'$
summand, giving the restriction map. The product is projective
of dimension three, so its algebraic dimension is three.
\end{proof}'''
G4=r'''\begin{proposition}[Components in Wang's torus fibration]\hypertarget{tag-01G4}{}\label{cdp:st:D.1.6}
\StatementRecord{cdp:st:D.1.6}{proved}{01G4}{\SeriesRef{cdp:st:D.1.13}; \cite{Wang2026}}
Wang's threefold $X_2(\lambda)$ has integral homology
$H_0=H_6=\Z$, $H_2=H_3=\Z/2\Z$, and the other reduced
homology groups zero. Its integral cohomology satisfies
$H^1=H^2=0$. Its fibration has four exceptional values, over which
the reduced fibres are irreducible: the multiplicity-three
bielliptic fibre, two rank-one fillings, and the rank-two filling.
In the rank-one filling over the $I_2$ value, the primitive period
exponent is $(2,1)$ and the fibre has one component.

In its cohomology basis the four monodromies are
\[
\begin{aligned}
B_*&=\begin{pmatrix}1&0&-6&-2\\0&-1&-1&1\\0&1&0&-1\\0&0&0&1\end{pmatrix},&\qquad
B_2&=\begin{pmatrix}1&0&6&3\\0&1&2&1\\0&0&1&0\\0&0&0&1\end{pmatrix},\\
B_+&=\begin{pmatrix}1&0&0&0\\0&2&1&0\\0&-1&0&0\\0&0&0&1\end{pmatrix},&\qquad
B_-&=\begin{pmatrix}1&0&0&-1\\0&1&1&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
\end{aligned}
\]
Their product in the displayed order is the identity, and their
common invariant cohomology group has rank one. On homology the
matrices are $B_i^{-t}$; the Smith diagonal of their difference
matrix is $(1,1,1,0)$. Thus $t'=1$ and the component count is
$r=4-1+1=4$. The expression $s-1+b_1(F)$ equals seven.
The coherent direct images are given in \cref{cdp:st:D.1.13}.
\end{proposition}
\begin{proof}
The construction and its integral homology are
\citet[Theorems~1.1 and~3.1, pp.~2 and~8]{Wang2026}.
The rank-one, rank-two and logarithmic fillings are
\citet[Propositions~2.7, 2.8 and~2.10, pp.~4, 6 and~7]{Wang2026}.
The primitive period vector is given in
\citet[Lemma~2.6, p.~4]{Wang2026}: the monomial change
$(z,v)\mapsto(x,y)=(v,v^2/z)$, with inverse
$(x,y)\mapsto(x^2/y,x)$, sends the vector to $(1,0)$.
The integral universal coefficient sequence gives the asserted
cohomology vanishing, since
$\operatorname{Ext}(H_1,\Z)=\operatorname{Hom}(H_2,\Z)=0$.

The matrices are \citet[Proposition~4.4, equation~(20), p.~11]{Wang2026}.
Direct multiplication gives their ordered product. For a column
$(a,b,c,d)^t$, invariance under $B_-$ gives $c=d=0$, and invariance
under $B_+$ then gives $b=0$. Every matrix fixes the first basis
vector. Preservation of evaluation under transport gives
$B_i^tA_i=I$, so $A_i=B_i^{-t}$ on the homology lattice.
Put $D_i=A_i-I$. Their columns satisfy
\[
D_-e_1=e_4,\qquad D_-e_2=-e_3,\qquad
D_+e_2=-e_2-e_3.
\]
Every image column has first coordinate zero, and these three
columns generate its full kernel. The coinvariant quotient is
therefore identified with $\Z$ by first coordinate, with inverse
$n\mapsto[ne_1]$. This gives the Smith diagonal and the invariant
rank. The component formula of \cref{cdp:st:D.1.2} now gives four,
in agreement with the four irreducible reduced fibres.
\end{proof}'''
blocks=[];guards=[]
for tag,label,new in [('01G3','cdp:st:D.1.5',G3),('01G4','cdp:st:D.1.6',G4)]:
 st=data['statement_labels'][label];end=max([st['end']]+[x['end'] for x in st['proofs']]);old=s[st['start']:end];assert s.count(old)==1
 before=BLOCKS/f'S6_SERIES_PUBLISH_II_{tag}_before.tex';after=BLOCKS/f'S6_SERIES_PUBLISH_II_{tag}_after.tex'
 for p,b in [(before,old),(after,new)]:assert not p.exists();p.write_text(b)
 math=lambda x:re.findall(r'(?<!\\)\$([^$]*?)(?<!\\)\$',x,re.S)
 display=lambda x:re.findall(r'\\\[(.*?)\\\]',x,re.S)
 m0,m1=math(old),math(new);d0,d1=display(old),display(new)
 missing=list((collections.Counter(m0)-collections.Counter(m1)).elements())
 disp=[]
 for x in d0:
  if x not in d1:
   # G3 displayed H1 gains a terminal period; its mathematical content is unchanged.
   normalized=lambda y:y.strip().rstrip(',.')
   assert any(normalized(x)==normalized(y) for y in d1)
   disp.append({'before':x,'after':next(y for y in d1 if normalized(x)==normalized(y)),'map':'Terminal punctuation only; exact formula unchanged.'})
 b={'tag':tag,'statement_id':label,'before_path':str(before.relative_to(ROOT)),'before_sha256':sha(old),'after_path':str(after.relative_to(ROOT)),'after_sha256':sha(new),'source_start_line':st['start_line'],'source_end_line':st['end_line'],'source_sha256':data['sha256'],'missing_old_inline_literals':missing,'old_displays_preserved_verbatim_or_punctuation_only':True,'display_punctuation_maps':disp,'old_inline_math':m0,'new_inline_math':m1,'old_display_math':d0,'new_display_math':d1};blocks.append(b)
 guards.append({'id':f'II-infra-recovery-{tag}-full-statement-proof','statement_id':label,'tag':tag,'source_sha256':data['sha256'],'before':old,'after':new,'type':'D01/D03/D06/D08/D11/D13' if tag=='01G3' else 'D03/D04/D06/D08/D09/D11/D13','reason':'State both explicit constructions and all numerical conclusions, give the already independently derived complete proof in a proof environment, remove production-history/disclaimer language, and resolve external/internal citations.','original_full_block':b['before_path'],'original_full_block_sha256':b['before_sha256'],'proposed_full_block':b['after_path'],'proposed_full_block_sha256':b['after_sha256'],'comparison_record':str((OUT/'S6_SERIES_PUBLISH_II_G3_G4_comparison.json').relative_to(ROOT)),'preservation':'Every original display is retained exactly or with terminal punctuation only. Added mathematical arguments and explicit lattice/coefficient maps are proved in the frozen derivations and postrelease comparison; no assertion of global formula/reference-sequence identity.','literal_math_map':{'old_inline':m0,'new_inline':m1,'old_display':d0,'new_display':d1,'missing_old_inline_literals':missing},'reference_map':{'before':re.findall(r'\\(?:CompendiumRef|SeriesRef|ref|cref|cite\w*)[^\n]*',old),'after':re.findall(r'\\(?:CompendiumRef|SeriesRef|ref|cref|cite\w*)[^\n]*',new),'explanation':'G3 historical D.1.1 compendium pointer is replaced by the explicit semidirect-product abelianization proof; AC source locator remains and becomes visible in the proof. G4 raw source identifiers become verified v2 printed locators; the coherent receiver remains, and the same-series component formula is added after its exact hypotheses were checked.'}})
# Bind whole table while changing only the existing D_exact_checks scope cell.
i=s.index('D_exact_checks');a=s.rfind('\\begin{longtable}',0,i);b=s.index('\\end{longtable}',i)+len('\\end{longtable}');table=s[a:b]
old=r'Tangent index; integral monodromy; Kodaira and Hopf surfaces; 120 unit quaternions, 14,400 products and a surjective commutator map over $\Q(\sqrt5)$ represented by rational pairs (\cref{cdp:st:C.1.1,cdp:st:C.3.2,cdp:st:C.3.3})'
new=old.replace('integral monodromy;','integral monodromy, including Wang\'s four matrices and integral coinvariant quotient;').replace('cdp:st:C.3.3})','cdp:st:C.3.3,cdp:st:D.1.6})');assert s.count(old)==1
for suffix,t in [('before',table),('after',table.replace(old,new))]:(BLOCKS/f'S6_SERIES_PUBLISH_II_G4_program_table_{suffix}.tex').write_text(t)
guards.append({'id':'II-infra-recovery-01G4-program-table','statement_id':'tab:II:programs','source_sha256':data['sha256'],'before':old,'after':new,'type':'D09','reason':'Cite the existing pinned D_exact_checks source once in its existing table row, adding the now inspected Wang matrix scope; remove program narration from the proposition.','original_full_block':str((BLOCKS/'S6_SERIES_PUBLISH_II_G4_program_table_before.tex').relative_to(ROOT)),'original_full_block_sha256':sha(table),'proposed_full_block':str((BLOCKS/'S6_SERIES_PUBLISH_II_G4_program_table_after.tex').relative_to(ROOT)),'proposed_full_block_sha256':sha(table.replace(old,new)),'publication_evidence':{'path':str((OUT/'S6_SERIES_PUBLISH_II_G4_prior_program_slice.json').relative_to(ROOT)),'sha256':sha((OUT/'S6_SERIES_PUBLISH_II_G4_prior_program_slice.json').read_bytes())}})
m=re.search(r'\\bibitem(?:\[[^\]]*\])?\{Wang2026\}',s);end=s.find('\\bibitem',m.end());entry=s[m.start():end];newentry=entry.replace('https://arxiv.org/abs/2609.11541}','https://arxiv.org/abs/2609.11541v2}').replace(r'\newblock \emph{Verified}.',r'\newblock Cited edition: version~2, 8 November 2026; page and statement locators refer to this edition.')
for suffix,t in [('before',entry),('after',newentry)]:(BLOCKS/f'S6_SERIES_PUBLISH_II_Wang_bibliography_{suffix}.tex').write_text(t)
guards.append({'id':'II-infra-recovery-Wang-bibliography','statement_id':'bib:Wang2026','source_sha256':data['sha256'],'before':entry,'after':newentry,'type':'D08/D18','reason':'Pin the cited supplied source to byte-proved arXiv v2, state its verified date/page scope, and remove the workflow status marker. Citation key/authors/title retained.','original_entry':str((BLOCKS/'S6_SERIES_PUBLISH_II_Wang_bibliography_before.tex').relative_to(ROOT)),'original_entry_sha256':sha(entry),'proposed_entry':str((BLOCKS/'S6_SERIES_PUBLISH_II_Wang_bibliography_after.tex').relative_to(ROOT)),'proposed_entry_sha256':sha(newentry),'publication_evidence':{'path':str((OUT/'G3_G4_primary_inputs/S6_SERIES_PUBLISH_II_Wang_primary_inputs_receipt_v2.json').relative_to(ROOT)),'sha256':sha((OUT/'G3_G4_primary_inputs/S6_SERIES_PUBLISH_II_Wang_primary_inputs_receipt_v2.json').read_bytes())}})
# Exact forward/inverse transport of the complete proposed source, never written canonically.
x=s
for g in guards:assert x.count(g['before'])==1;x=x.replace(g['before'],g['after'],1)
for g in reversed(guards):assert x.count(g['after'])==1;x=x.replace(g['after'],g['before'],1)
assert x==s
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':data['sha256'],'guards':guards,'blocks':blocks,'guard_count':len(guards),'owner_count':2,'status':'prepared only; complete original/proposed manual comparison to follow before root approval','forward_inverse_exact':True,'events_added':0,'canonical_files_modified':False}
f=OUT/'S6_SERIES_PUBLISH_II_G3_G4_guards.json';assert not f.exists();f.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'path':str(f.relative_to(ROOT)),'sha256':sha(f.read_bytes()),'guard_count':len(guards),'missing_old_inline_literals':{b['tag']:b['missing_old_inline_literals'] for b in blocks},'source_sha256':data['sha256']}))
