from pathlib import Path
p=Path(__file__).resolve().parents[1]/'sections'/'AB_push.tex'
t=p.read_text()
start=t.index('\\subsection{A.4.')
stop=t.index('\\begin{theorem}[A.1.2;',start)
block=t[start:stop]
t=t[:start]+t[stop:]
t=t.rstrip()+'\n\n'+block.rstrip()+'\n'
p.write_text(t)
print('Moved A.4 after A.3; no passage removed.')
