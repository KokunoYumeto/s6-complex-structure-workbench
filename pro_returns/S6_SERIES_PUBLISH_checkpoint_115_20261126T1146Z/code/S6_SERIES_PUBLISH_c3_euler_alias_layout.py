"""Keep the transferred Euler alias inside the ordinary equation label scope."""
from S6_SERIES_PUBLISH_c3_edit import *
text=SOURCE.read_text()
pos=text.index(r'\hypertarget{tag-0193}{}\SsixEquationAliases{\label{cdp:eq:C.ZC.8}}')
a=text.rfind(r'\begin{equation}',0,pos)
b=text.index(r'\end{equation}',pos)+len(r'\end{equation}')
old=text[a:b]
assert old.count(r'\begin{split}')==1 and old.count(r'\end{split}')==1
new=old.replace(r'\begin{split}',r'\begin{aligned}').replace(r'\end{split}',r'\end{aligned}')
apply_edit(old,new,'II-C3-ROOT-EULER-ALIAS-LAYOUT',['D23'],
    'lem:II:blowup-topology;cdp:eq:C.ZC.8',
    'Shared full-inverse-image Euler equation C.VR.4 / C.ZC.8',
    'The integrated 801-page build exposed one unresolved reference: the new alias after split did not reach the equation label writer. The aligned environment keeps the identical two mathematical lines and their two labels in the ordinary equation scope.',
    'Exact complete equation compared; both formula lines and all identifiers are unchanged. Integrated rebuild will verify the alias.')
add_event('publish:II:build','II-C3-BUILD-HOPF-COLLAR-REFERENCE-OPEN',
    'used and rechecked in this run',
    'Three pdfLaTeX passes exited0 with shell escape disabled; the 801-page PDF has two overfull boxes, none above2pt, and no missing fonts/glyphs or duplicate labels/destinations. One undefined reference C.ZC.8 exposed its split-scope alias placement. The equation environment was repaired without changing its formula; the next build must verify resolution. This working build does not close the final build or page gates.',
    'build/II_c3_working/S6_SERIES_PUBLISH_II.log',source=__file__)
print('Identical Euler formula moved from split to aligned label scope.')
