#!/usr/bin/env python3
"""Root's exact one-line grammatical readback correction."""
from pathlib import Path
from hashlib import sha256
p=Path('agents/continuation7_iii_general_initial_receiving/S6_SERIES_PUBLISH_III_02LN_receiving.tex')
s=p.read_text()
assert sha256(s.encode()).hexdigest()=='d0e0e185f0380c2e1dfc0e3b941cc3984a1f37fb5a4ea2a869625641d4f06d7e'
old='This is an closed integral two-cycle.'
new='This is a closed integral two-cycle.'
assert s.count(old)==1
s=s.replace(old,new)
p.write_text(s)
print('EXACT_DIFF',old,'=>',new)
print('RECEIVER',p,'LINES',len(s.splitlines()),'SHA256',sha256(s.encode()).hexdigest())
