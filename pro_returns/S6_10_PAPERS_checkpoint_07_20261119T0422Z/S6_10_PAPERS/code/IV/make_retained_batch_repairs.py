from pathlib import Path
import json
W=Path(__file__).resolve().parents[2];A=W/'analysis/IV/retained_batch_9';edits=[]
def add(label,old,new,reason):
 s=(A/(label.split(':')[1].replace('.','_')+'.tex')).read_text();assert s.count(old)==1,(label,s.count(old),old[:90]);edits.append(dict(label=label,old=old,new=new,reason=reason))
l='night:P3F.53'
add(l,r'''in the literal
whole-fibre construction of E26 Remark~8.5''',r'''in the literal
whole-fibre construction of \cite[Remark~8.5, p.~24]{Engel2026}''','Attach the currently opened exact general-construction locator; this remark supplies the construction, not the new sphere classification.')
add(l,r'''We consider the literal whole-fibre construction in E26 Remark 8.5''',r'''We consider the literal whole-fibre construction of
\cite[Remark~8.5, p.~24]{Engel2026}''','Use the actual attached-source edition and printed page for the original generalization.')
add(l,r''' (k_{\rm Jin},\ell_{\rm Jin})&=(-3H,-24\chi),\\
 (m_{\rm rel},n_{\rm rel},A_M)&=''',r''' (k_U,\ell_U)&=(-3H,-24\chi),\\
 (k_M,\ell_M)&=(3H,24\chi),\\
 (m_{\rm rel},n_{\rm rel},A_M)&=''','Type both characteristic pairs. The explicit K68 extending line and cap maps carry the meridian-one dual pair to the physical pair; the native pair is retained.')
add(l,'''gives (SC.5). Finally K31's common-exterior
meridians, stable frame transitions and
explicit flop recurrence apply to that
simultaneous product and give (SC.6).
This derivation retains the maps used at
each source, cap, page and fan comparison.''',r'''gives the meridian-one pair in (SC.5).
The extending duality and exchanged-cap maps of
\cref{night:P3K.68} give its displayed physical pair.
For every transported fan, \cref{night:P3K.73}
uses the full target coefficient matrices, actual
orbit and derivative prisms, and directed native
reset maps. Its integral recursion starts from
these reference data and computes the return.
Thus every page and fan comparison retains its
own specified source, line, collar and cap maps.''','Remove the absent SC.6 and the invalid global application of the old K31 recurrence; use the complete actual prism construction.')
old=r'''\[
 [\Sigma_{\Phi,T}]
       =KL\frac{(S-1)(S-3)}8 \pmod {28}.
\]
The original \(K=L=1\) example with
\(v_1=(3,1),v_2=(-1,0)\) has
\(\delta=(0,1)=v_1+3v_2\), determinant
one and \(S=7\). Its return class is
three. The exact clutch transfer and
mapping-torus argument of F22--24 apply
to this explicit holomorphic family.'''
new=r'''the actual shorter parameter data
\[
 J=2KL,\qquad \widehat H=KL/3,\qquad
 \widehat\chi=KL/6.
\]
On the signed vertical seed \(T_n\),
\cref{night:P3K.73} therefore gives the integer
\(-KL\,n(n-1)\); its complete native prism
recursion computes every other basis fan.
For the previously displayed original basis
\[
 P=\begin{pmatrix}3&-1\\1&0\end{pmatrix},
 \qquad \delta=v_1+3v_2,
\]
the canonical word from \(T_1\) is \(C_0,C_1,C_1\).
The successive pairs
\((V_{ii},\delta_i)\) entering the update are
\((2,2),(-4,8),(-14,34)\), so its three
increments \((\delta_i-V_{ii})/4\) are
\(0,3,12\). The actual class is \(15\pmod{28}\).
The old norm polynomial gave \(3\) on this exact
basis, and is refuted by this comparison.
The basis \(\left(\begin{smallmatrix}1&-2\\0&1\end{smallmatrix}\right)\)
has word \(C_0,C_0\) from \(T_0\), increments
\(0,3\), and actual class \(3\). The complete
proof supplies all twenty-eight witnesses for
\(K=L=1\). The clutch transfer and mapping-torus
maps of \cref{night:P3F.22,night:P3F.24} apply
to these specified holomorphic families.'''
add(l,old,new,'Recompute the printed original fan through its exact actual prism word. Preserve the concrete old3/actual15 discrepancy and the actual class3 witness; do not reuse the refuted norm polynomial.')
add(l,r'''For
\(\lambda=r^{3k}\), its pair is
\((-6k,-24k)\), and its all-fan class
is \(3k(S-1)(S-3)/4\). The line,
period basis and mixed-angle maps
in that proof specify the comparison
with its page and each fan.''',r'''For
\(\lambda=r^{3k}\), its positive-fan dual pair
is \((-6k,-24k)\), and its physical pair is
\((6k,24k)\), with return zero. The complete
outer component-line comparison of
\cref{night:P3K.65} gives whole-loop class
\(-3k\) on the negative fan and shorter-loop
class \(-k\), while the positive-fan value
remains zero. Its native two-node maps retain
the actual unequal normal-line defects.
The all-fan computation is the full coefficient
and target-prism algorithm of
\cref{night:P3K.77}. The former norm polynomial
is retained only in the refutation record.''','Retain the positive reference and actual OS49 negative/positive outer comparison; remove the already refuted global norm polynomial.')
add(l,'''The separate
source-loop working proof records
the computed nodal branch exchange
and the uncomputed fan and cap
endpoint transport.''',r'''For the selected-cusp source family,
\cref{night:P3F.54,night:P3F.56,night:P3K.45,night:P3K.46}
construct the actual branch, line, cap and
half-source maps, and \cref{night:P3K.71}
computes its full fan transport.''','Replace the superseded unfinished-source notice by the specific completed source/cap and fan proofs.')
add(l,r'''characteristic pair is
\((-3H/b,-24\chi/b)\), and its
physical reference index is \(A_M/b\).''',r'''dual characteristic pair is
\((-3H/b,-24\chi/b)\); its physical
pair is \((3H/b,24\chi/b)\) and its
physical reference index is \(A_M/b\).''','Retain the actual shorter covering morphism and distinguish its two line conventions explicitly.')
add(l,'''The varying-source
loops still require the recorded
relative transport calculation.''','The construction just proved retains the fixed source and every stated scalar, cap, line and endpoint map.','Remove an obsolete broad working-status sentence from the completed fixed-source proof.')
add('night:P3K.41', 'All linear lattice maps are fixed. The physical delta field gives an', r'''All linear lattice maps are fixed. For the original family, the
physical scalar action and its connected automorphism group are
identified in \cite[Remark~8.3, pp.~22--23]{Engel2026}.
The full global group in the present marked cap construction is
computed from the root and cusp valuations in CP.3--4 below.
The physical delta field gives an''', 'Credit the exact known original-family scalar-action locus; retain the complete new root/cusp endpoint application.')
for lab in ['night:P3K.41','night:P3K.43','night:P3K.44']:
 s=(A/(lab.split(':')[1].replace('.','_')+'.tex')).read_text();old='A_{\nm short}';assert old in s
 edits.append({'label':lab,'old':old,'new':r'A_{\mathrm{short}}','reason':'Repair the literal malformed short-return subscript; no mathematical change.','replace_all':True,'expected_count':s.count(old)})
(A/'receiving_replacements.json').write_text(json.dumps(edits,indent=2)+'\n');print(len(edits),'exact receiving repairs staged')
