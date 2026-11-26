"""Restore the two retained equation aliases before amsmath processes split."""
from S6_SERIES_PUBLISH_c3_edit import *

old = r'''\begin{equation}
 \begin{split}
 (z,w,x)\longmapsto\bigl(&
   \beta_i^{r_i}(z+d_i x^{R-r_i}w^R),\\
   &\beta_iw,\ \beta_i^{-1}x\bigr).
 \end{split}                                             \hypertarget{tag-00AP}{}\label{cdp:eq:C.AS.18}
\hypertarget{tag-0123}{}
\hypertarget{tag-00TK}{}
\SsixEquationAliases{\label{cdp:eq:C.SN.10}\label{cdp:eq:C.NS.19}}
\end{equation}'''
new = r'''\begin{equation}
\SsixEquationAliases{\label{cdp:eq:C.SN.10}\label{cdp:eq:C.NS.19}}
 \begin{split}
 (z,w,x)\longmapsto\bigl(&
   \beta_i^{r_i}(z+d_i x^{R-r_i}w^R),\\
   &\beta_iw,\ \beta_i^{-1}x\bigr).
 \end{split}                                             \hypertarget{tag-00AP}{}\label{cdp:eq:C.AS.18}
\hypertarget{tag-0123}{}
\hypertarget{tag-00TK}{}
\end{equation}'''
apply_edit(old,new,'II-C3-STAR-DECK-ALIASES',['D06','D22'],
 'cdp:eq:C.AS.18;cdp:eq:C.SN.10;cdp:eq:C.NS.19','Compact insertion of elliptic stars: deck transformation',
 'Install the existing equation-label alias hook before the split environment processes its equation label. The previous placement retained both alias tokens in the source but wrote neither to the auxiliary file. All three maps and targets are unchanged.',
 'Root read the complete old/new display, adjacent weighted-action argument and the receiving nonlinear-specialization paragraph. Integrated build verification follows separately.')
add_event('cdp:eq:C.AS.18;cdp:eq:C.SN.10;cdp:eq:C.NS.19',
 'II-C3-STAR-DECK-ALIASES','used and rechecked in this run',
 'The source retained SN.10 and NS.19, but the working auxiliary file wrote only AS.18. The same existing alias hook is moved before split; the deck map and all targets remain byte-identical. Root read both complete displays and their receiving specialization. A clean build and exact three-label auxiliary comparison are still required separately; no proof or final-page credit.',
 'Compact insertion display AS.18 and merged star specialization',source=__file__)
