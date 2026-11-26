from S6_SERIES_PUBLISH_c3_edit import *

for serial,main in enumerate(['cdp:eq:C.UI.2','cdp:eq:C.UI.3','cdp:eq:C.MH.12'],1):
    source=SOURCE.read_text()
    at=source.index('\\label{'+main+'}',source.index('\\begin{document}'))
    start=source.rindex('\\begin{equation}',0,at)
    end=source.index('\\end{equation}',at)+len('\\end{equation}')
    old=source[start:end]
    match=re.search(r'\\SsixEquationAliases\{((?:\\label\{[^}]+\})+)\}',old)
    assert match and '\\begin{split}' in old
    aliases=match.group(0)
    new=old.replace(aliases,'',1).replace('\\begin{equation}\n','\\begin{equation}\n'+aliases+'\n',1)
    apply_edit(old,new,f'II-C3-SPLIT-ALIASES-{serial:02}',['D23'],main,'Local numerical and conductor criteria',
      'The working-build auxiliary file omitted aliases installed after a split display. Place the unchanged alias hook before split so amsmath captures it when constructing the equation tag. Every identity, permanent target and label is preserved.')
add_event('II:equation-aliases','II-C3-SPLIT-ALIAS-REPAIR','used and rechecked in this run',
 'The current 791-page working build was scanned for all19 equation-alias uses. Four aliases in three split equations were absent from the auxiliary file; two were used and warned undefined. A minimal document with the identical preamble and no shell escape confirmed that installing the hook before split writes both the main and alias labels at the same equation number and destination. All three source placements were repaired. Other alias labels already existed. Integrated verification remains pending; no final build/page row is closed.',
 'S6_SERIES_PUBLISH_II.tex: P281 and P289 numerical displays',source='code/S6_SERIES_PUBLISH_c3_split_aliases.py')
print('Repaired three split-equation alias placements.')
