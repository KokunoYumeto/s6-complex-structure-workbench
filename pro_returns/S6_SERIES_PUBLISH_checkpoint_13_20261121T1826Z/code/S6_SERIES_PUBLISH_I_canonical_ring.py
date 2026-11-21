from pathlib import Path
import json,datetime,re
from S6_SERIES_PUBLISH_editing import Editor,block
r=Path(__file__).resolve().parents[1];ed=Editor('I')
body=block(ed.text,'fam:src:A.1.1')
wb=block(ed.text,'wb:thm:canonical-ring-recovery')
begin=ed.text.index(r'\subsection{The canonical divisor and the exact anticanonical ring}')
end=ed.text.index(r'\subsection{The retained period constant is an effective deformation parameter}',begin)
whole=ed.text[begin:end]
proof=wb[wb.index(r'\begin{proof}'):]
proof=proof.replace('Retain the explicit base identifications','Use the explicit base identifications')
proof=proof.replace('On the actual finite cover','On the finite cover')
proof=proof.replace(r'By \cref{inv:A1.0}, a section of',
    r'Connected compact fibres give $f_*\mathcal O_X=\mathcal O_B$ by \cite[Proposition~9.13, pp.~74--76]{AC2026}. A section of')
needle=r'Tensoring evaluation with \(f^*\eta_B\), and multiplying the'
proof=proof.replace(needle,r'''These local canonical transitions hold for every admissible affine
translation and cusp collar with the fixed fan. A translation
$\zeta\mapsto\zeta+a(s)$ contributes only $ds$ terms to its
differential, which vanish after wedging with the base differential.
A cusp multiplier $x_j\mapsto h_j(t_c)x_j$ adds
$(h_j'/h_j)dt_c$ to $dx_j/x_j$, with the same cancellation.
Thus the determinant characters and evaluation divisor are unchanged.
Tensoring evaluation with \(f^*\eta_B\), and multiplying the''')
proof=proof.replace(r'\end{enumerate}',r'''\item A biholomorphism preserves the anticanonical graded ring and
its complete degree-two system, so it induces a projective
automorphism of $B$. The reduced singular cusp fibre and the
finite fibres of multiplicities three and four distinguish the
three values: the pullback identity for a fibre divisor preserves
its multiplicity, and smoothness of its reduction is preserved
under the induced fibre isomorphism. Hence each of $0,1,\infty$
is fixed. A projective automorphism fixing these three points is
the identity.
\end{enumerate}''',1)
statement=wb[:wb.index(r'\end{theorem}')+len(r'\end{theorem}')]
statement=statement.replace(r'\begin{theorem}[Canonical bundle and recovery of the original fibration]',
 r'\begin{proposition}[The canonical bundle and anticanonical pencil]')
statement=statement.replace(r'\end{theorem}',r'\end{proposition}')
statement=statement.replace(r'\hypertarget{tag-03DM}{}\label{wb:thm:canonical-ring-recovery}',
 r'\hypertarget{tag-01PZ}{}\label{fam:src:A.1.1}\label{fam:st:A.1.1}\hypertarget{tag-03DM}{}\label{wb:thm:canonical-ring-recovery}')
statement=statement.replace(r'\StatementRecord{wb:thm:canonical-ring-recovery}{proved}{03DM}{the definitions and constructions stated in the proof}',
 r'\StatementRecord{fam:src:A.1.1}{proved}{01PZ}{\cite[Lemma~9.10(ii), p.~70; Proposition~9.11, pp.~70--71]{AC2026}}')
statement=statement.replace('The evaluation map',
 'For the standard marked $(3,4,\\infty)$ family, including every admissible\nchoice of its affine translations and cusp collar with the fixed fan,\nthe evaluation map',1)
statement=statement.replace('the actual direct image','the direct image').replace('the original $f$','the map $f$')
statement=statement.replace('The degree-one system consists of the single divisor $2S_2$.',
 'The degree-one system consists of the single divisor $2S_2$.\nEvery biholomorphism between two such threefolds induces the identity\non $B$.')
remark=r'''\begin{remark}[Divisor classes in the Picard coordinate]
\hypertarget{tag-PI09}{}\label{I:canonical-Picard-classes}
In the additive coordinate of \cref{I:def:Picard-coordinate},
the identification in \eqref{inv:eq:C-factor12} gives
\[
 \mathcal O_X(S_1)=L_4,\qquad \mathcal O_X(S_2)=L_3,
 \qquad \omega_X=L_{-6},\qquad \omega_X^{-2}=L_{12}.
\]
\end{remark}
'''
ed.replace(whole,'','D12','Move the full canonical-divisor and graded-ring argument to its first body statement. Preserve the evaluation divisor, meromorphic subsheaf identity, all graded basis maps and base coordinate changes.','wb:thm:canonical-ring-recovery')
ed.replace(body,statement+'\n'+proof+'\n\n'+remark,'D12',
 'Use one complete proof of the stronger combined statement. Preserve arbitrary admissible affine/collar scope by the explicit differential cancellation and retain the intrinsic-base conclusion by its multiplicity and singular-fibre argument.',
 'fam:src:A.1.1')
orphan='The canonical pencil is due to \\citet[Theorem~9.1]{AC2026}. A complete re-derivation is given in \\CompendiumRef{I}{app:rederive:fam-src-A.1.1}.'
ed.replace(orphan,'','D06','The operative proof and exact credited primary inputs now appear at the statement; remove the inaccessible compendium pointer.','fam:src:A.1.1:source-pointer')
heading=r'\subsection{Canonical sections and the finite covers}\hypertarget{tag-01PA}{}\label{fam:section:A.1}'
ed.replace(heading,heading+'\n'+r'\hypertarget{tag-03CU}{}\label{wb:sec:canonical-ring-recovery}',
 'D14','Keep the canonical-ring section anchor at the unique body proof.','wb:sec:canonical-ring-recovery')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_canonical_ring_comparison.json').write_text(json.dumps({
 'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'read_scope':'Complete original A1.1 statement, source pointer, WB canonical statement and all three proof steps plus following Picard paragraph read before integration.',
 'exact_correspondence':{'A1.1 canonical/direct-image/ring assertions':'WB CR1–4, same divisor, pullback subsheaf, chosen generators and graded basis.',
  'A1.1 arbitrary affine/collar scope':'The differential of an affine translation contributes base differentials; wedging with the base form kills them. The cusp unit gives the same displayed map.',
  'A1.1 identity on B':'Complete degree-two ring gives a projective base map; fibre multiplicities and singular reduction fix 0,1,infinity individually.',
  'Picard paragraph':'One numbered remark with the existing exact additive coordinate.'},
 'scope':'Consolidation and explicit proof details; no independent preread check claimed.'},indent=2)+'\n')
