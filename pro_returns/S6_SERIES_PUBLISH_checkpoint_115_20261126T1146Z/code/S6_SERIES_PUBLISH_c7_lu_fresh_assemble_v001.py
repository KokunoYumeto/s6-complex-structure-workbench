"""Assemble the complete LU fresh proof before individual original exposure.

This preserves the working note and every mathematical execution. It reads
only that note and the already reviewed fresh LS period/component support.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / 'agents/continuation7_iii_corrected_initial'
working = LANE / 'S6_SERIES_PUBLISH_III_02LU_fresh_additive_notes.md'
support = ROOT / 'agents/continuation7_iii_vertical_correction/S6_SERIES_PUBLISH_III_02LS_period_and_star_maps.md'
assert sha256(support.read_bytes()).hexdigest() == '3d0d822101f3f2d30b199ea7821689db5a51b387595b7cce017fa5fbe9c37b49'
raw = working.read_text()
parts = re.split(r'(?m)^## (\d+)\. ', raw)
assert [int(parts[i]) for i in range(1, len(parts), 2)] == list(range(1, 13))
sections = {int(parts[i]): parts[i+1] for i in range(1, len(parts), 2)}
header = '''# 02LU: complete fresh corrected-additive derivation

Root checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation seven,
25 November 2026. Numerical reasoning effort is not separately exposed.
This is the written proof before any LU original, old packet or historical
target program is opened. The original LT proof also remains closed.
The exact scoped dependencies and new executions are stated below.

'''
sections[1] = sections[1].replace('Inputs and the remaining finite marking question', 'Exact inputs and the resolved literal component marking', 1)
old = '''LN's complete frozen fresh
proof is a root-reviewed pending dependency, released for comparison
at08:20:46; no LN admission is claimed. LS's fresh vertical proof
is also unfinished and retains its explicitly recorded scope.'''
new = '''LN's entire theorem/proof and all auxiliaries were compared after its
fresh freeze and individually admitted at09:08:51.122973 UTC. Its full
integral maps are now admitted input. LS's local/global vertical argument
and the exact period/component support are attributed written fresh inputs;
this proof gives them their exact scope and claims no LS admission.'''
assert old in sections[1]
sections[1] = sections[1].replace(old, new)
start = sections[1].index('One finite marking question remains:')
sections[1] = sections[1][:start] + '''The literal IC8 marking is resolved in Section9 by d_can=-e0 and
the explicit component permutation with inverse. Its complete new source,
actual output and independent root readback are recorded in Section14.
The cone uses the actual forward-arrow permutation as specified there.

'''
sections[7] = '''The complete local input for global assembly

The h=1 additive input consists of the primitive area row and its Bezout
section, both literal fixed normals and their integral bounding chains,
the degree-one gamma quotient and inverse roof loop, and the free H4
component-orbit basis. Sections9--12 supply the corrected periods,
exhaustive all-height component choices and full global assembly.
All permitted remaining caps use their admitted full integral maps.

'''
sections[8] = sections[8].replace('identify the still-open literal IC8 ordering and does not replace the', 'supply the separate literal IC8 permutation of Section9 and does not replace the')
old = '''LI/LK and LN local calculations; the LN derivation is reviewed
fresh evidence here, not an admitted result by assertion.'''
new = '''LI/LK and LN local calculations. LN was individually admitted at
09:08:51.122973 UTC after whole-original and whole-receiver comparison.'''
assert old in sections[11]
sections[11] = sections[11].replace(old, new)
sections[12] = sections[12].replace('Literal optional corrections and the precise remaining gate', 'Literal optional corrections and complete proved scope', 1)
old = '''The written local and global mathematical derivation is now
complete at the stated scope. Its supporting LS final period
and literal-component readback, and the full combined fresh
proof readback, remain before the independent proof is frozen.
No LT/LU original or historical target has been opened, and
no implementation comparison or required-row admission is
claimed in this fresh completion section.'''
new = '''This proves the local and global mathematical result at the stated
scope. The following support and exact reading notes preserve the
actual period maps and computational evidence used in this proof.
The historical implementation is compared only after individual original
release. No LT/LU original or historical target is used in this proof,
and no receiving admission or canonical application is claimed here.'''
assert old in sections[12]
sections[12] = sections[12].replace(old, new)
period = support.read_text().split('## 2. The exact punctured tensor and arrow maps\n\n', 1)[1]
period = period.split('## 4. Literal IC8 ordering and the two distinct corrections', 1)[0]
period = period.replace('## 3. Unbounded integrality and all21 ordered products', '### Unbounded integrality and all21 ordered products')
tail = '''## 14. Exact fresh support reading and completion scope

The entire LS period_and_star_maps.md was read by root, SHA256
3d0d822101f3f2d30b199ea7821689db5a51b387595b7cce017fa5fbe9c37b49.
The literal logarithmic comparison in Section13 is attributed to that
fresh support, which expands the root's earlier vertical proof. Its
component permutation, inverse, divisor and eta maps are reproduced in
Section9. No independence beyond that attribution is claimed.

Root read the entire new star_order_v001 source and all five actual
stdout lines, including both full dense matrix records, plus the actual
empty separate stderr. Its one successful execution ran at
09:00:38.016734--09:00:38.021913 UTC. The source SHA256 is
2a691d08f73dbe0049c6ee465398952c5e6fddd6b6fefccad261803805b9fdf3;
the stdout SHA256 is
8debbe55995cd2973eb41f0c9281312616f5e21cb11d863412274c1c1d54a9a2.
The output checks the full two affine Cartan matrices, both literal
correction divisors, every permutation and inverse, both degree vectors,
the multiplicity vectors, all orbit lengths and the eta bounding chain.

The local cone's entire254-line source and33 actual stdout lines were
read by root and KS, with its actual empty stderr. KS's bounded review
also read every working-proof line and the period/IC8 maps. It corrected
one description of the multiplicative logarithm: z_G=(kappa/nu)v uses
the transverse period v with u^t J v=1. The displayed equation proves
the denominator claim. This prose clarification changes no cone
calculation or retained execution. No mathematical execution failed.

The root working proof was read in full before this assembly. The
assembled proof and the final peer-review scope are read before freeze.
The individual LU original remains closed until root records that
complete fresh review and its exact frozen hash and time.
'''
result = header + ''.join('## '+str(i)+'. '+sections[i] for i in range(1, 13))
result += '## 13. Attributed complete punctured tensor and period maps\n\n' + period + tail
destination = LANE / 'S6_SERIES_PUBLISH_III_02LU_fresh_derivation.md'
with destination.open('x', newline='\n') as stream:
    stream.write(result)
assert destination.read_text() == result
print('ASSEMBLED', datetime.now(timezone.utc).isoformat())
print('WORKING_SHA256', sha256(working.read_bytes()).hexdigest())
print('FRESH', destination.relative_to(ROOT), 'LINES', len(result.splitlines()), 'SHA256', sha256(result.encode()).hexdigest())
print('SCOPE complete written proof assembled; no original/history exposure, no mathematical rerun, no freeze or admission claimed by assembly.')
