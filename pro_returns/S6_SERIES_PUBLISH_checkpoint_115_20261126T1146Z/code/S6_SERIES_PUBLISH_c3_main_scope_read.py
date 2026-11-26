"""Read current body statements for the final main-theorem scope comparison.

Read-only: this displays the selected owners and does not close any gate.
"""
from pathlib import Path
import re
import sys

groups={
 'A':['cdp:st:A.1.1','cdp:st:B1','cdp:st:A.4.7','cdp:st:A.4.9','cdp:st:C4f','cdp:st:E12','cdp:st:E17'],
 'B':['cdp:st:D.1.2','cdp:st:C.3.1','cdp:st:C.3.11','cdp:st:C.3.7','cdp:st:C.3.8','cdp:st:C.3.9','cdp:st:C.3.10','cdp:st:C.3.12','cdp:st:C.3.6','cdp:st:D.2.7'],
 'C':['night:P4.58','cdp:st:C.2.MH.2','cdp:st:C.2.INT.1','cdp:st:C.2.INT.2','cdp:st:C.2.INT.3','cdp:st:C.2.G.1','cdp:st:D.2.3','cdp:st:D.2.5','cdp:st:D.2.7'],
 'D':['cdp:st:C.2.UN.1','cdp:st:C.2.UN.4','cdp:st:C.2.UN.14','cdp:st:C.2.UN.2'],
 'E':['cdp:st:C5b','cdp:st:C5c','cdp:st:E8','cdp:st:E18'],
 'F':['cdp:st:E5','cdp:st:E6','cdp:st:E13','cdp:st:E14','cdp:st:E15','push:src:E.2.23','push:src:E.2.24','inv:E2.5','inv:E2.2'],
 'G':['ii:LR:covering'],
}
text=(Path(__file__).resolve().parents[1]/'S6_SERIES_PUBLISH_II.tex').read_text()
names=re.findall(r'\\newtheorem\{([^}]+)\}',text)
environments=list(re.finditer(r'\\begin\{('+ '|'.join(map(re.escape,names))+r')\}',text))

def without_hidden_record(block):
    pattern=r'\\StatementRecord\s*'
    while (m:=re.search(pattern,block)):
        p=m.end()
        for _ in range(4):
            while block[p].isspace():p+=1
            assert block[p]=='{'
            depth=1;p+=1
            while depth:
                if block[p]=='{' and block[p-1]!='\\':depth+=1
                if block[p]=='}' and block[p-1]!='\\':depth-=1
                p+=1
        block=block[:m.start()]+block[p:]
    return block

for group in sys.argv[1:]:
    assert group in groups
    print('Main theorem',group)
    for label in groups[group]:
        pos=text.index(r'\label{'+label+'}')
        env=next(m for m in reversed(environments) if m.start()<pos)
        end=text.index(r'\end{'+env[1]+'}',pos)+len(r'\end{'+env[1]+'}')
        print('OWNER',label,'line',text.count('\n',0,env.start())+1)
        print(without_hidden_record(text[env.start():end]))
