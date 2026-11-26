#!/usr/bin/env python3
"""Read-only exact comparison of the admitted conifold proof inputs."""
from pathlib import Path
from hashlib import sha256
import difflib
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'agents/continuation8_iii_integration/units/later/conifold_constructions.tex'
text=path.read_text()
print('SOURCE',len(text.splitlines()),sha256(path.read_bytes()).hexdigest())
for tag,number in [('02M0','1'),('02M1','2'),('02M2','3'),('02M3','4')]:
    a=text.index('\\label{maps:src:D.3.'+number+'}')
    a=text.index('\\begin{proof}',a)
    b=text.index('\\end{proof}',a)+len('\\end{proof}')
    proof=text[a:b]+'\n'
    receiver=ROOT/'agents/continuation5_iii_root'/('S6_SERIES_PUBLISH_III_'+tag+'_receiving.tex')
    received=receiver.read_text();c=received.index('\\begin{proof}')
    d=received.index('\\end{proof}',c)+len('\\end{proof}')
    other=received[c:d]+'\n'
    print(tag,'PROOF_LINES',len(proof.splitlines()),'RECEIVER_LINES',len(other.splitlines()),
          'RECEIVER_SHA256',sha256(receiver.read_bytes()).hexdigest(),'IDENTICAL',proof==other)
    if proof!=other:
        print(''.join(difflib.unified_diff(other.splitlines(True),proof.splitlines(True),
          fromfile=tag+'_receiver',tofile='current_'+tag)),end='')
print('MK_REPAIRED_SOURCE_IS_EXPOSED_PUBLICATION_INPUT_PENDING_OWNER_TRACE')
