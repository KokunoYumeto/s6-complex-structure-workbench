from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

R = Path(__file__).resolve().parents[1]
P = 'agents/continuation2_root/01BW/S6_SERIES_PUBLISH_II_root_BW'
OLD = 'agents/ii_infra/released_proofs/01BW/cb2f1578c62bf37c/S6_SERIES_PUBLISH_full_owning_block.tex'
def bind(p):
    data = (R / p).read_bytes()
    return dict(path=p, sha256=sha256(data).hexdigest(), bytes=len(data))
original = (R / OLD).read_text()
assert sha256(original.encode()).hexdigest() == 'c2e320084582491a8b9d5e4f07ccc59b7f9d2a40eb32539cf33cf103471af223'
assert (R / 'S6_SERIES_PUBLISH_II.tex').read_text().count(original) == 1
work = original
guards = []
def guard(old, new, kind, reason):
    global work
    assert work.count(old) == 1, old
    before = sha256(work.encode()).hexdigest()
    offset = work.index(old)
    work = work.replace(old, new)
    guards.append(dict(old=old, new=new, type=kind, reason=reason, occurrences=1,
                       offset_before=offset, before_sha256=before,
                       after_sha256=sha256(work.encode()).hexdigest()))

guard('[Global exclusion of connected positive-genus triple covers over a rational image]',
      '[Connected triple covers over a rational image]', 'D08,D16',
      'Use a shorter mathematical title; the full statement and both conclusions remain byte-identical.')
header = next(line + '\n' for line in work.splitlines() if line.startswith('\\StatementRecord'))
guard(header, '', 'D10', 'Remove the production header and preserve all labels and permanent tags.')
guard('\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]',
      '\\begin{enumerate}[label=\\arabic*.,leftmargin=*]', 'D04,D23',
      'Keep all twelve proof items with ordinary sequential numbering.')
guard('We construct all comparison maps, including the map into the\nactual nearby fibre. Put',
      'Put', 'D08', 'Begin the proof with its geometric data; every comparison map follows unchanged.')
guard('therefore an actual homogeneous function', 'therefore a homogeneous function', 'D08',
      'State the defined normal jet directly.')
guard('\\paragraph{Comparison with the actual fibre.}', '\\paragraph{Comparison with a nearby fibre.}',
      'D08', 'Use the mathematical fibre designation.')
guard('gives an orientation-preserving embedding into the actual\nfibre',
      'gives an orientation-preserving embedding into the\nfibre', 'D08',
      'Retain the literal embedding and its target without the emphatic adjective.')
guard('This construction uses the actual function\n$f$ and its leading normal jet; it makes no assertion that\narbitrary changes of local equations preserve a Milnor fibre.',
      'The construction uses the function $f$ and its leading normal jet.',
      'D02,D08', 'State precisely which function defines the unchanged comparison.')
guard('Here is the precise torus obstruction we will use. For a map',
      'For a map', 'D08', 'Begin directly with the homology map being calculated.')
guard('This is a comparison of the actual homology maps.\n', '', 'D08',
      'The preceding covering lift and exterior-power inclusion already give these maps.')
guard('\\cite[Theorem 2.1.1 and Corollary 2.1.3]{MerleTeissier1977}',
      '\\cite[Theorem~2.1.1 and Corollary~2.1.3, pp.~11--13]{MerleTeissier1977}',
      'D18', 'Add the exact primary pages read in the official Numdam scan.')
guard('The following table records the result; all entries are\nalso computed with rational arithmetic in\n\\path{code/root_cubic_normal_cone.py}.',
      'The following table gives the counts.', 'D09',
      'Remove the internal program path; the complete monomial-count method remains and the verified program is listed once in Programs.')
guard('\\cite[\\S1 and Example 2.4(a)]{Nemethi1991Join}',
      '\\cite[\\S1, Theorem~L1 and Example~2.4(a), pp.~1--3]{Nemethi1991Join}',
      'D18', 'Give the exact opened tensor-product and join loci, including the disconnected-factor scope of Theorem L1.')
guard('This proves the column without replacing the actual\nexceptional divisor by an unspecified graph.',
      'This identifies the last column with the first Betti number of the exceptional divisor.',
      'D02,D08', 'State the established homology identification directly; its exact sequence remains.')
guard('These identities concern the actual classes in the indicated\ncyclic cover. They will also be used for the degree-two\nroot divisor below.',
      'These identities also apply to the degree-two root divisor below.',
      'D08', 'Keep the application and all displayed identities while removing the emphatic repetition.')
guard('The genus-zero cases with $v=1$ or $2$ are not\nasserted to be excluded by this argument.',
      'The remaining genus-zero cases have $v=1$ or $2$.',
      'D02', 'State the remaining cases positively, preserving the exact scope.')

proposed = P + '_proposed_v1.tex'
if (R / proposed).exists():
    assert (R / proposed).read_text() == work
else:
    (R / proposed).write_text(work)
assert original.count('\\item ') == work.count('\\item ') == 12
assert re.findall(r'\\\[(.*?)\\\]', original, re.S) == re.findall(r'\\\[(.*?)\\\]', work, re.S)
assert re.findall(r'\\begin\{(?:align|equation|gather)\*?\}.*?\\end\{(?:align|equation|gather)\*?\}', original, re.S) == re.findall(r'\\begin\{(?:align|equation|gather)\*?\}.*?\\end\{(?:align|equation|gather)\*?\}', work, re.S)
original_math = re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$', original, re.S)
proposed_math = re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$', work, re.S)
assert original_math.count('\\langle1\\rangle') == 1
original_math.remove('\\langle1\\rangle')
assert original_math == proposed_math
body = lambda s: s[s.index('Let $Y$'):s.index('\\end{proposition}')]
assert body(original) == body(work)
out = dict(created_utc=datetime.now(timezone.utc).isoformat(),
           original=bind(OLD), proposed=bind(proposed), guards=guards,
           mathematical_steps_changed=0, original_and_proposed_items=12,
           all_displays_preserved=True, all_inline_mathematics_preserved=True,
           inline_math_exclusion='Only the production enumerate-label token \\langle1\\rangle is removed; every mathematical inline expression remains in order.',
           preparation_attempt='The first preservation check included the production enumerate-label token as mathematical content and stopped before creating the proposal record. This version explicitly accounts for that already declared numbering guard; the prepared block is unchanged and no canonical source was touched.',
           statement_body_byte_identical=True,
           canonical_writes=0, final_reading_pending=True)
path = P + '_editorial_proposal_v1.json'
assert not (R / path).exists()
(R / path).write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(dict(proposal=bind(path), proposed=bind(proposed), guards=len(guards)), indent=2))
