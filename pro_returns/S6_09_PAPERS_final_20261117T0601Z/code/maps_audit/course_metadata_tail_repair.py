"""Keep mathematical setup that shared a source line with producer metadata.

This emits a proposed conversion overlay; it does not mutate the sources or
the parent-owned converter. Every selected tail has been read individually.
"""
from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parents[3]
W=R/'deliverables/work/maps_audit'
moves=json.loads((W/'III_course_conversion_moves.json').read_text())
tails=[]
special={
 'the-exact-characteristic-two-coordinate-calculation.md':'This is a fully written algebraic prerequisite',
 'the-original-projective-coordinate-and-actual-cooperations.md':'The spectrum is the original',
}
for m in moves:
 if not m['reason'].startswith('raw'):continue
 s=m['text'];name=Path(m['source']).name
 if name in special:
  tail=s[s.index(special[name]):]
 else:
  q=re.search(r'New (?:teaching )?exposition CC0(?:-1\.0)?\.',s)
  tail=s[q.end():].strip() if q else ''
 tail=re.sub(r'New exposition CC0(?:-1\.0)?\.','',tail).strip()
 tail=tail.replace('No independent review or novelty claim.','').strip()
 tail=tail.replace('Author self-checks and 52 finite exact checks supplement the complete written arguments.','').strip()
 if tail:
  tails.append(dict(source=m['source'],source_line=m.get('source_line'),raw_line_sha256=hashlib.sha256(s.encode()).hexdigest(),
   raw_producer_line=s,keep_in_mathematical_text=tail,
   rationale='The producer line also contains mathematical definitions, conventions, or an explicit dependency/scope statement. Preserve this tail while moving only the producer metadata.',
   reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17'))
(W/'III_course_metadata_math_restore.json').write_text(json.dumps(tails,ensure_ascii=False,indent=2)+'\n')
print('Saved',len(tails),'individually reviewed mathematical setup tails.')
