"""Remove two paragraph breaks left by the alias-placement typesetting repair."""
from S6_SERIES_PUBLISH_c4_edit import *
import re
text=SOURCE.read_text()
blocks=[m[0] for m in re.finditer(r'\\begin\{equation\}[\s\S]*?\\end\{equation\}',text)
        if re.search(r'\n[ \t]*\n',m[0])]
assert len(blocks)==2
for n,old in enumerate(blocks,1):
    new=re.sub(r'\n[ \t]*\n','\n',old)
    sid='cdp:eq:C.EN.R7' if 'cdp:eq:C.EN.R7' in old else 'cdp:eq:C.WT.35'
    apply_edit(old,new,f'II-C4-MATH-PARAGRAPH-{n}',['D23'],sid,
        'Split display after the alias-placement repair',
        'Moving a standalone alias call left an empty source line inside each of two math displays. The rebuild detected Missing $ at the first; both are removed. Only the paragraph break introduced by that typesetting edit changes; every mathematical token and identifier is retained.',
        review='Root read both complete displays and confirmed the sole change is deletion of one empty line in each. The corrected source is rebuilt; this gives no mathematical-proof event.')
print('Removed the two math-mode paragraph breaks introduced by the alias relocation; all formulas and targets retained.')
