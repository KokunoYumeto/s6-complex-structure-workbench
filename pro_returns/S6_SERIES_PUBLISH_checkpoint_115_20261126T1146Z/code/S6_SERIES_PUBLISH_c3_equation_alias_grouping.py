"""Repair the two observed multiple-hook equation displays."""
from S6_SERIES_PUBLISH_c3_edit import *

source=SOURCE.read_text()
pattern=re.compile(r'\\SsixEquationAliases\{((?:\\label\{[^}]+\})+)\}')
changes=[]
for display in re.finditer(r'\\begin\{equation\}.*?\\end\{equation\}',source,re.S):
    old=display.group(); aliases=list(pattern.finditer(old))
    if len(aliases)<=1:continue
    payload=''.join(a.group(1) for a in aliases)
    cursor=0
    def substitute(match):
        global cursor
        cursor+=1
        return '\\SsixEquationAliases{'+payload+'}' if cursor==1 else ''
    new=pattern.sub(substitute,old)
    assert identifiers(old)==identifiers(new)
    assert pattern.sub('',old)==pattern.sub('',new)
    changes.append((old,new,re.findall(r'\\label\{([^}]+)\}',old)[0]))
assert len(changes)==2
for i,(old,new,label) in enumerate(changes,1):
    apply_edit(old,new,f'II-C3-ALIAS-GROUP-{i:02}',['D23'],label,
        'P333 fundamental-group display; marked-cycle transverse sign display',
        'The working build halted with TeX input-stack exhaustion because a second alias call overwrote the saved label hook with itself. One call now contains both existing aliases, so the original hook runs once and writes the same three equation labels. Mathematical display tokens and all identifiers are identical.',
        review='Root read both full old/new displays. Exact label/target counters and display payload equality checked; integrated rebuild follows. No mathematical-proof or final-page credit.')
    print(new)
add_event('cdp:eq:C.HC.7;cdp:eq:C.HG.4','II-C3-ALIAS-GROUPING','used and rechecked in this run',
    'The failed integrated build stopped at the first display with two separate equation-alias hooks. Both such displays in the current source were read and repaired by one hook containing their same alias labels. Formula payload and all identifiers are unchanged. A complete integrated rebuild is required; no final build/page or mathematical-check credit.',
    'P333 and marked-cycle criterion equation aliases',source=__file__)
