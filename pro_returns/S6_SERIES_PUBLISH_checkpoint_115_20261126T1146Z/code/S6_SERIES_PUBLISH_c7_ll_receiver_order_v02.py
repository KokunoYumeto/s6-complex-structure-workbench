#!/usr/bin/env python3
"""Complete the LL assembly; v01 and its failed check output are retained.

Version01 found two missing escapes on environment-end commands before
writing. This version also repairs those exact new-prefix commands.
"""
from pathlib import Path
from hashlib import sha256
import re
lane=Path('agents/continuation7_iii_residual_two_primary')
p=lane/'S6_SERIES_PUBLISH_III_02LL_receiving.tex'
s=p.read_text()
start=s.index(r'\item\emph{The integral critical-cycle calculation')
end=s.index(r'\end{proof}',start)+len(r'\end{proof}')
suffix=s[start:end]
assert r'\item \emph{The reference frame' in s[end:]
s=s[:start]+s[end:]
s=s.rstrip()+'\n\n'+suffix+'\n'
s,n=re.subn(r'(?<!\\)\b(q?quad)\b',lambda m:'\\'+m[1],s)
s,m=re.subn(r'(?<!\\)end\{(cases|pmatrix)\}',lambda m:'\\'+m[0],s)
assert m==2
original=''.join((lane/f'S6_SERIES_PUBLISH_III_02LL_released_{q}.tex').read_text()
                 for q in ['statement','proof'])
for command in ['label','hypertarget']:
    pattern=r'\\'+command+r'\{([^}]*)\}'
    old=re.findall(pattern,original)
    new=re.findall(pattern,s)
    assert sorted(old)==sorted(new),(command,old,new)
    assert len(new)==len(set(new))
    print(command,'permanent_identities',len(new),'exactly_preserved')
assert s.count(r'\begin{proof}')==s.count(r'\end{proof}')==1
assert s.rstrip().endswith(r'\end{proof}')
depth=0
for brace in re.findall(r'(?<!\\)[{}]',s):
    depth += 1 if brace=='{' else -1
    assert depth>=0
assert depth==0
stack=[]
for kind,env in re.findall(r'\\(begin|end)\{([^}]*)\}',s):
    if kind=='begin':stack.append(env)
    else:
        assert stack and stack.pop()==env,(kind,env,stack)
assert not stack
p.write_text(s)
print('ORDER_FIXED spacing_commands_repaired',n,'environment_escapes',m)
print('BALANCED braces and environments; theorem/proof blocks each one')
print('RECEIVER_LINES',len(s.splitlines()))
print('RECEIVER_SHA256',sha256(p.read_bytes()).hexdigest())
