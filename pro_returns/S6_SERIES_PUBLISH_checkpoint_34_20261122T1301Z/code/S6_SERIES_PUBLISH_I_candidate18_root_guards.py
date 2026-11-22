#!/usr/bin/env python3
"""Archive the four individually inspected Neron--Severi accent repairs."""
from pathlib import Path
import datetime, difflib, hashlib, json, re
from S6_SERIES_PUBLISH_I_candidate17_combined import block, math, displays, refs, write_stable
from S6_SERIES_PUBLISH_synctex_batch import Scanner

R=Path(__file__).resolve().parents[1]
O=R/'agents/i_cont_edits'
S=R/'S6_SERIES_PUBLISH_I.tex'
P=R/'build/I_candidate18/S6_SERIES_PUBLISH_I.pdf'
sha=lambda b:hashlib.sha256(b).hexdigest()
source='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
pdf='702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e'
text=S.read_text()
assert sha(S.read_bytes())==source and sha(P.read_bytes())==pdf
old_texts=[
 r'\section{Exceptional fibres, Neron--Severi classes, and compact subspaces}',
 'For every smooth fibre and every admissible \\(c\\), its Neron--Severi lattice',
 'Neron--Severi lattice $\\mathbb Z\\eta+\\mathbb ZE$, where the nonzero upper',
 'countable union gives the asserted exact Neron--Severi lattice.',
]
assert text.count('Neron--Severi')==4
guards=[]
with Scanner(P) as scanner:
 for n,old in enumerate(old_texts,1):
  assert text.count(old)==1
  pos=text.index(old)
  new=old.replace('Neron--Severi',r"N\'eron--Severi")
  if n==1:
   a=text.rfind('\n',0,pos)+1
   b=text.index('\n',pos)
   label='fam:section:D'
   kind='complete section heading with its permanent target and label'
  else:
   label,a,b,kind=block(text,pos)
  original=text[a:b]
  proposed=original
  for other in old_texts:
   if other in proposed:proposed=proposed.replace(other,other.replace('Neron--Severi',r"N\'eron--Severi"),1)
  assert math(original)==math(proposed)
  assert displays(original)==displays(proposed)
  assert refs(original)==refs(proposed)
  assert re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',original)==re.findall(r'\\(?:label|hypertarget)\{[^}]+\}',proposed)
  stem=O/f'S6_SERIES_PUBLISH_I_candidate18_root_review_block_{1 if n==1 else 2 if n==2 else 3:02}'
  pa,pb,pd=[Path(str(stem)+s) for s in ['_original.tex','_proposed.tex','.diff']]
  write_stable(pa,original);write_stable(pb,proposed)
  write_stable(pd,''.join(difflib.unified_diff(original.splitlines(True),proposed.splitlines(True),fromfile=label+'/candidate18',tofile=label+'/accent-proposal')))
  line=text[:pos].count('\n')+1
  pages=scanner.pages(S,line)
  assert pages
  guards.append({'id':f'I18-root-{n:02}','type':'D23','page':min(pages),'statement_id':label,'before':old,'after':new,
   'reason':"Restore the acute accent in Néron--Severi, consistently with the existing proposition title; the literal replacement carries each mathematical segment, label, target and reference by the identity.",
   'source_line':line,'source_sha256':source,'pdf_sha256':pdf,
   'original_full_block':str(pa.relative_to(R)),'original_full_block_sha256':sha(pa.read_bytes()),
   'proposed_full_block':str(pb.relative_to(R)),'proposed_full_block_sha256':sha(pb.read_bytes()),
   'full_block_contains_all_root_changes_for_this_block':True,'owning_context_kind':kind,
   'all_inline_and_display_mathematical_segments_identical':True,'reference_sequence_identical':True,
   'label_and_target_sequence_identical':True,'candidate18_synctex_pages':sorted(pages),
   'root_review':'Root read the complete section heading and both complete owning propositions with their attached proofs, including the integral-class, orientation and Hermitian-form calculation in D.1.4 and the exact period-locus/Pfaffian argument in D.1.7. This is a spelling repair with the identity map on every mathematical segment and reference; no new mathematical derivation is claimed.',
   'status':'approved by root, awaiting complete candidate18 reading and combined guarded application',
   'mathematical_events_added':0})
out=O/'S6_SERIES_PUBLISH_I_candidate18_root_guards.json'
write_stable(out,json.dumps(guards,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(R)),'sha256':sha(out.read_bytes()),'guards':len(guards),'complete_blocks':3,'source_sha256':source,'pages':sorted({p for g in guards for p in g['candidate18_synctex_pages']}),'canonical_source_changed':False}))
