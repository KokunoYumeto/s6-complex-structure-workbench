#!/usr/bin/env python3
"""Express two proof domains positively and update only the associated check prose."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import difflib
ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_corrected_initial_receiving'
PREFIX='S6_SERIES_PUBLISH_III_02LU_'
rp=LANE/(PREFIX+'receiving.tex')
old=rp.read_text()
oldhash='f5eb57e9c7042d6fc4c0f561491cdc90f5241fc6edbe893ad7c7b32462403ea3'
assert sha256(rp.read_bytes()).hexdigest()==oldhash
changes=[(r'''specified base weights thus agree under this map, with no
extension across the zeros or poles of $\sigma_E$ being used.
''',r'''specified base weights thus agree under this map on the
complement of the zeros and poles of $\sigma_E$.
'''),('''then retained. This establishes the unsaturated closure
procedure without assuming that the final group is abelian
or that the intermediate vertical quotient injects into it.
''','''then retained. This gives the unsaturated normal-closure
quotient within the full fundamental-group presentation.
''')]
new=old
for a,b in changes:
    assert new.count(a)==1
    new=new.replace(a,b)
newhash=sha256(new.encode()).hexdigest()
print('START',datetime.now(timezone.utc).isoformat())
print(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='receiver-before',tofile='receiver-after')),end='')
rp.write_text(new)
print('RECEIVER_LINES',len(new.splitlines()),'SHA256',newhash)
for name,expected in [('comparison.md','72157c0c3f2e8d6b25ffb2b1bb20fa1eebff073a542398f89f46a3c52b31f050'),
                      ('source_checks.md','9f7ec21f597dc8bc5436b27010caf40fef670a75033293d362e56ee9adadd47c')]:
    p=LANE/(PREFIX+name);a=p.read_text()
    assert sha256(p.read_bytes()).hexdigest()==expected
    b=a.replace(oldhash,newhash).replace('653 lines','652 lines')
    if name=='comparison.md':
        b=b.replace('its two small assembly repairs','its three small assembly repairs')
        b=b.replace('All three sources, successful stdout and actual empty stderr are retained\nand read.',
                    'Version v004 states the punctured-map domain and the normal-closure\nconclusion positively, with unchanged mathematical maps. All four\nsources, successful stdout and actual empty stderr are retained and read.')
    else:
        b=b.replace('v002.py and v003.py, their separate .out and .err files, are retained.\nAll three ran once successfully.',
                    'v002.py, v003.py and v004.py, their separate .out and .err files, are\nretained. All four ran once successfully.')
        b=b.replace('environment, three accents and a closing recap. Their full source and',
                    'environment, three accents and a closing recap. Version v004 expresses\ntwo domains/conclusions positively, without changing their maps. Their full source and')
    assert b!=a
    print(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=name+'-before',tofile=name+'-after')),end='')
    p.write_text(b)
    print(name,'LINES',len(b.splitlines()),'SHA256',sha256(p.read_bytes()).hexdigest())
print('END',datetime.now(timezone.utc).isoformat())
