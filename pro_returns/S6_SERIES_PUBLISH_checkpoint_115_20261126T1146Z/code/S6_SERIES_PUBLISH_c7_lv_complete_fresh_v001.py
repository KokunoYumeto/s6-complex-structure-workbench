"""Complete the written LV derivation from wholly read fresh components."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
lane = ROOT / 'agents/continuation7_iii_weighted_os45_fresh'
path = lane / 'S6_SERIES_PUBLISH_III_02LV_fresh_derivation.md'
graph = ROOT / 'agents/continuation7_iii_weighted_os45_graph/S6_SERIES_PUBLISH_III_02LV_global_sphere_and_critical_link.md'
circle = ROOT / 'agents/continuation7_iii_weighted_os45_graph/S6_SERIES_PUBLISH_III_02LV_circle_and_sphere_scope.md'
before = path.read_text()
assert sha256(before.encode()).hexdigest() == 'e409221734b60ecae060cdfc54f1ae05ab0f8df0ff4a735831919292ef96630e'
assert sha256(graph.read_bytes()).hexdigest() == '2fc3152486c11e60fb0fda4c2df40ba130ba957f8447e54636bc62da88cdf455'
assert sha256(circle.read_bytes()).hexdigest() == 'e1d9b0b2f247e3fd18d3828c8a943b5bcb6c4917bf8877f8a9a7038000bab1d8'
backup = lane / 'S6_SERIES_PUBLISH_III_02LV_fresh_derivation_before_global.md'
assert not backup.exists()
old_header = '''This document is being written from the clean statement, the admitted LN
marked integral gluing model, and the admitted LP toric, finite-coefficient
and relative-framing constructions. It is not yet a frozen complete proof.
The final source-line detector calculation remains to be supplied.
'''
new_header = '''This complete written derivation uses the clean statement, the admitted
LN marked integral gluing model, the admitted LP toric, finite-coefficient
and relative-framing constructions, and the admitted LL primitive-cusp
specialization chain. Section 7 includes the global source-line sphere,
its actual reference frame and the integral critical-chain intersection.
The target original and its historical auxiliaries remain closed.
'''
assert before.count(old_header) == 1
prefix, suffix = before.split('## 7. Remaining fresh proof obligation\n', 1)
assert 'have not yet been proved in this document' in suffix
prefix = prefix.replace(old_header, new_header)
old = '''coefficients. Zero energy makes every coefficient equal; that divisor
is a multiple of the principal whole fibre. Since H^2(X;Z) is free,
c1(X)=0. The same divisor pairings kill the free part of c2.
'''
new = '''coefficients. Zero energy makes every coefficient equal; the resulting
class is a multiple of the integral relation sum D_i=0 proved in Section 2.
Since H^2(X;Z) is free, c1(X)=0. The same divisor pairings kill
the free part of c2.
'''
assert prefix.count(old) == 1
prefix = prefix.replace(old, new)
body = graph.read_text().split('## 1. The two actual collapsing circles\n', 1)[1]
body = '## 1. The two actual collapsing circles\n' + body
inserted = re.sub(r'^## ([1-9])\.', r'### 7.\1.', body, flags=re.M)
inserted = re.sub(r'\bSection ([1-9])\b', r'Section 7.\1', inserted)
inverse = re.sub(r'^### 7\.([1-9])\.', r'## \1.', inserted, flags=re.M)
inverse = re.sub(r'\bSection 7\.([1-9])\b', r'Section \1', inverse)
assert inverse == body
assert len(re.findall(r'^### 7\.[1-9]\.', inserted, flags=re.M)) == 9
now = datetime.now(timezone.utc)
ending = f'''
## 8. Completion and reading scope

The complete fresh derivation was assembled at {now.isoformat()}.
The original LV proof and all historical target programs and outputs
were closed through this completion. The first six sections and their
two fresh mathematical sources/actual streams were wholly read by root.
The entire global sphere derivation and all its final changed hunks,
all 103 lines of its only mathematical source, all 21 actual stdout
lines, its actual empty stderr, and every one of the 2591 JSON lines
were read. The JSON display was untruncated. Its complete integral
solution, kernel and unsuccessful functional witnesses are retained.
The final global note is pinned at SHA256
2fc3152486c11e60fb0fda4c2df40ba130ba957f8447e54636bc62da88cdf455.
The explicit section-renumbering map above has an exact text inverse;
it changes no argument or equation. Every executed text editor, actual
output and failed patch diagnostic in that lane has also been read.

The separate 306-line circle-bordism derivation is checking evidence,
with SHA256 e1d9b0b2f247e3fd18d3828c8a943b5bcb6c4917bf8877f8a9a7038000bab1d8.
Root wholly read it and its local-cusp homology obstruction. Its value
P_ref=0 agrees with the direct sphere calculation in Section 7.9.
It supplies no replacement for that direct frame and intersection proof.
The exact input and execution note is the graph lane's 95-line
S6_SERIES_PUBLISH_III_02LV_graph_input_and_execution_scope.md,
SHA256 9ca456e3bd45109709c861301b40df394e6b10def0bc23a089cb62f330d070bd.
No canonical manuscript, required row or publication unit is changed
by this completed written derivation. Full original comparison follows
only after root's individual release.
'''
after = prefix + '## 7. Global source sphere, reference framing and critical link\n\n' + inserted + ending
backup.write_text(before, newline='\n')
path.write_text(after, newline='\n')
print('COMPLETED_FRESH_UTC', now.isoformat())
print('PRIOR', len(before.splitlines()), sha256(before.encode()).hexdigest())
print('COMPLETE', len(after.splitlines()), len(after.encode()), sha256(after.encode()).hexdigest())
print('EXACT_TEXT_INVERSE', 'Nine embedded graph subsections and every local cross-reference invert to the wholly read source.')
print('NEW_HEADER\n' + new_header, end='')
print('COHOMOLOGY_WORDING\n' + new, end='')
print('FINAL_SCOPE\n' + ending, end='')
