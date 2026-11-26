"""Correct and record the full receiving conormal-owner comparison."""
from S6_SERIES_PUBLISH_c3_edit import *

apply_edit(chr(9)+'ext{two-by-two gradient minors}',r'\text{two-by-two gradient minors}',
 'II-C3-CONORMAL-MINOR-TEXT-TOKEN',['D23'],'lem:II:rational-conormal-defects','Gradient-minor display',
 'Repair a tab introduced in place of the TeX text macro during source construction; the named minors and their orders are unchanged.',
 'Complete receiving proof read; exact character repair checked.')
apply_edit(r'P_{\mathfrak p}^{,2}',r'P_{\mathfrak p}^{2}',
 'II-C3-CONORMAL-SQUARE-TOKEN',['D23'],'lem:II:triple-conductor-symbolic-square','Generic conductor localization',
 'Remove the malformed spacing comma in the exponent; the generic conductor is the ordinary square, as proved by the three branch vectors.',
 'Complete receiving proof read; the exponent is checked against the original (x,y)^2 calculation.')
apply_edit(r'$Q\subset(\nu_C)_*L\subset j_*K$',r'$Q\subset j_*L\subset j_*K$',
 'II-C3-CONORMAL-AMBIENT-PUSHFORWARD',['D22'],'lem:II:rational-conormal-defects','Gradient-lattice comparison',
 'Write both pushforwards on the same ambient Y through j=i nu_C, as already used by the definition of tau_p.',
 'The exact inclusion i and normalization nu_C in the lemma were compared with the old local proof.')
apply_edit(r'Apply \cref{lem:II:rational-conormal-defects} with this same $Y,C,E$ and $j=i\nu$.',
 r'Write $\nu:E\to C$ for normalization, $i:C\hookrightarrow Y$ for inclusion and $j=i\nu$. Apply \cref{lem:II:rational-conormal-defects} with these same $Y,C,E,j$.',
 'II-C3-CONORMAL-ELLIPTIC-MAPS',['D22'],'night:P4.30','Elliptic application',
 'Declare the exact maps before substituting the unchanged elliptic data into the common lemma.',
 'Original and receiving complete proofs compared.')
apply_edit('The sum is therefore nonpositive, with equality precisely when every normalization defect vanishes.',
 'Thus the displayed Euler characteristic is nonpositive, with equality precisely when every normalization defect vanishes.',
 'II-C3-CONORMAL-EULER-SIGN-WORDING',['D22','D25'],'night:P4.30','Conclusion of the elliptic application',
 'Specify that the nonpositive quantity is minus the sum of nonnegative defects, namely the displayed Euler characteristic.',
 'The sign is checked directly from chi=-sum d and the positive local singularity bounds; the theorem and numerical result are unchanged.')
add_event('lem:II:rational-conormal-defects; lem:II:triple-conductor-symbolic-square; night:P4.30; night:P4.31; night:P4.34; night:P4.35',
 'II-C3-ROOT-CONORMAL-OWNERS-RECEIVING','used and rechecked in this run',
 'Root read the entire original P4.30/P4.31/P4.34 proofs and entire receiving P254/P256/P4.30/P4.31 subsection. The original derivative kernel, torsion-free conormal injection, elementary-divisor minor calculation, plane residue/different equality, multiplicity-two ambient graph, semigroup gap argument and nonplanar two-branch bounds are retained. Riemann--Roch with degree K=2-2g+degR gives chi=5(1-g)-sum d, whose explicit g=0 and g=1 substitutions reproduce the old formulas. P256 retains all three quadratic branch vectors and their idempotent conductor test, then proves primary saturation for all local branches by the exact isolated-primary injection. P4.31 applies it to the same whole conductor and keeps all regularity and ambient coordinate maps. P4.34 aliases the unchanged stronger P4.35 on identical f,Y,mS,nu and resolution data; its full superseded special-case proof is preserved verbatim in the defect record. Two TeX character slips, the ambient pushforward notation and the Euler-sign wording found in the full receiving read were corrected in bounded rows. No independent or migration movement credit.',
 'S6_SERIES_PUBLISH_II.tex: conormal calculation and ordinary-triple equality',
 source='code/S6_SERIES_PUBLISH_c3_conormal_receiving.py')
set_unit_status('night:P4.30','D12','done',
 'Complete old and receiving subsection read. P254 owns the full conormal calculation, P256 the full primary triple-conductor calculation, and the unchanged equality statements apply these exact maps. All transferred material and cases were compared.',
 'CHECK_EVENTS.tsv: II-C3-ROOT-CONORMAL-OWNERS-RECEIVING')
print('Complete receiving conormal subsection compared; P4.35 still awaits its own graph-owner comparison.')
