"""Resume only the source-record phase after already-admitted Guillot guards."""
from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text()
def statement(text,label):
    i=text.index('\\label{'+label+'}',text.index('\\begin{document}'))
    a=text.rfind('\\begin{',0,i)
    env=re.match(r'\\begin\{([^}]+)\}',text[a:]).group(1)
    b=text.index('\\end{'+env+'}',i)+len('\\end{'+env+'}')
    return text[a:b]
protected={x:statement(s,x) for x in ['push:src:E.5.2','push:src:E.5.3']}
path=ROOT/'code/S6_SERIES_PUBLISH_c3_analytic_lr_admit.py'
program=path.read_text()
tail=program[program.index("base=ROOT/'agents/continuation3_provenance'"):]
exec(compile(tail,str(path)+' [source-record phase]','exec'))
print('The 205 defects, 29 events, seven-section migration and 18 primary readings had already succeeded; they were not replayed.')
