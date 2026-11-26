"""Allow the unchanged ordered cup-product basis to break after its commas."""
from S6_SERIES_PUBLISH_c3_edit import *
add_event('II','II-C3-BUILD-OCCURRENCE-OVERFLOW','used and rechecked in this run',
    'Three integrated pdfLaTeX passes completed with shell escape disabled: 805 pages,5339745bytes. No undefined reference/citation, font/glyph issue, duplicate label/destination or rerun request. Three overfull boxes were found; one is2.78159pt in the unchanged ordered cup-product basis paragraph of P321, exceeding the2pt gate. The other two are1.7175pt and0.629pt. The layout gate remains open; no final-page credit.',
    'Integrated working build after occurrence, junction and Hopf adjacency admission',source=__file__)
old=r'In the ordered basis $(f_1g_1,f_1g_2,f_2g_1,f_2g_2)$,'
new=r'In the ordered basis $(f_1g_1,\allowbreak f_1g_2,\allowbreak f_2g_1,\allowbreak f_2g_2)$,'
apply_edit(old,new,'II-C3-CUP-BASIS-LAYOUT',['D23'],'prop:II:comb-cup-duality',
    'Ordered frame immediately before the row(b,-a,d,-c)',
    'The integrated build reports2.78159pt overflow in this paragraph. Permit a line break after each comma of the unchanged ordered basis; the vector order, row and morphisms are identical.',
    'The complete P321 proof was already compared; this bounded source paragraph was read again. Pure line-break change; no new mathematical-check or page-reading credit.')
