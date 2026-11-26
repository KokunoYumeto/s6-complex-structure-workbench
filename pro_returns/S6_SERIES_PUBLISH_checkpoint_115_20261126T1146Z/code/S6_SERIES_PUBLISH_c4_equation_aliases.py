"""Repair three alias invocations in one display after the actual TeX error."""
from S6_SERIES_PUBLISH_c4_edit import *

old=r'''\hypertarget{tag-00TL}{}
\SsixEquationAliases{\label{cdp:eq:C.NS.2}}
\hypertarget{tag-00VV}{}
\SsixEquationAliases{\label{cdp:eq:C.PR.6}}
\hypertarget{tag-017U}{}\SsixEquationAliases{\label{cdp:eq:C.WT.15}}'''
new=r'''\hypertarget{tag-00TL}{}\hypertarget{tag-00VV}{}\hypertarget{tag-017U}{}
\SsixEquationAliases{\label{cdp:eq:C.NS.2}\label{cdp:eq:C.PR.6}\label{cdp:eq:C.WT.15}}'''
apply_edit(old,new,'II-C4-EQUATION-ALIAS-RECURSION',['D23'],
    'cdp:eq:C.SN.5','Marked elliptic-star definition, product coordinate map',
    'The first final-build pass hit TeX input-stack recursion at this display. Each alias invocation resets the saved label macro; three in the same equation recursively capture its wrapper. One invocation with the same three labels uses the existing intended macro once. All formula bytes, labels and permanent tag multiplicities are preserved.',
    review='Root read the exact display and macro definition, verified that this is the sole numbered display with multiple alias invocations, and combined only these calls. No mathematical proof or independent event is added; clean rebuild and actual page inspection remain required.')
print('Combined three equation-alias calls; all exact targets and formula bytes retained.')
