"""Keep the retained layout target as an alias of its one numbered equation."""
from S6_SERIES_PUBLISH_c4_edit import *
old=r'''\hypertarget{tag-00VL}{}\label{cdp:eq:C.PR.13}\label{layout:II:3}
\hypertarget{tag-0188}{}\SsixEquationAliases{\label{cdp:eq:C.WT.27}}'''
new=r'''\hypertarget{tag-00VL}{}\label{cdp:eq:C.PR.13}
\hypertarget{tag-0188}{}\SsixEquationAliases{\label{cdp:eq:C.WT.27}\label{layout:II:3}}'''
apply_edit(old,new,'II-C4-LAYOUT-LABEL-ALIAS',['D23'],
    'cdp:eq:C.PR.13','Core-period family equation',
    'The actual next build stopped at amsmath multiple-label error for the retained layout:II:3 target. The complete current equation scan found this sole multiple direct-label instance. Move only that layout target into the existing alias call for the very same numbered equation; every formula, label and permanent tag remains.',
    review='Root read the full receiving quotient-family display, its primary target and existing alias. The layout target has the same equation/page identity. This is typesetting repair with no proof event; final three-pass compilation and image inspection remain required.')
print('First final-build failure: recursive equation alias wrappers at C.SN.5; repaired by one alias call.')
print('Second final-build failure: two direct labels in C.PR.13; retained layout target now in the same alias call.')
print('No mathematical formula or target identifier was changed.')
