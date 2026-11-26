"""Remove invalid blank paragraph breaks inside displayed mathematics only."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text();start=s.index('\\begin{document}')
patterns=[r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}[\s\S]*?\\end\{\1\}',r'\\\[[\s\S]*?\\\]']
edits=[]
for pattern in patterns:
    for m in re.finditer(pattern,s[start:]):
        old=m.group(0);new=old
        while re.search(r'\n[ \t]*\n',new):new=re.sub(r'\n[ \t]*\n','\n',new)
        if new==old:continue
        assert re.sub(r'\s+','',new)==re.sub(r'\s+','',old)
        pos=start+m.start()
        prior=list(re.finditer(r'\\StatementRecord\{([^}]+)\}',s[start:pos]))
        stmt=prior[-1].group(1) if prior else 'Paper II displayed mathematics'
        edits.append((pos,start+m.end(),old,new,stmt))
edits.sort()
for left,right in zip(edits,edits[1:]):assert left[1]<=right[0]
after=s
for a,b,old,new,stmt in reversed(edits):after=after[:a]+new+after[b:]
preserve_identifiers(s,after)
SOURCE.write_text(after,newline='\n')
rows=[]
for i,(a,b,old,new,stmt) in enumerate(edits,1):
    rows.append(dict(change_id=f'II-C3-MATH-PARAGRAPH-{i:03}',type='D23',statement_id=stmt,
      old_location='Displayed equation after manual-tag conversion',old_page='working build stopped at source line 31316; full concordance pending',
      new_location='Same displayed equation',new_page='working rebuild pending',old_text=old,new_text=new,
      reason='A blank source line becomes a forbidden TeX paragraph inside display math. Remove that blank paragraph break only; all mathematical tokens, labels and targets are identical after ignoring whitespace.',
      review_status='Every changed display compared at token level; integrated rebuild follows.'))
print('Blank-paragraph repairs',len(edits))
print('Defect rows',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
for _,_,_,_,stmt in edits:print(stmt)
add_event('Paper II displayed equations','II-C3-MATH-PARAGRAPH-REPAIR','used and rechecked in this run',
    f'The working build stopped at an invalid paragraph break inside E.2.15 equation eq:II:next-E-2-15-1. Removed {len(edits)} blank paragraph breaks in displayed-math blocks across the receiving source. Each full old/new display is logged and has identical nonwhitespace tokens, labels and targets. No mathematical assertion changes; integrated rebuild follows and final typography remains open.',
    'S6_SERIES_PUBLISH_II.tex: displayed equations',source='code/S6_SERIES_PUBLISH_c3_math_paragraph_repair.py')
