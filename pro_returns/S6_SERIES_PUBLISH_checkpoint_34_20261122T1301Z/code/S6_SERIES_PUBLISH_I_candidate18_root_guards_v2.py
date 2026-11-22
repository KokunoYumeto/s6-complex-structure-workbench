#!/usr/bin/env python3
"""Extend the immutable four accent guards by two complete-proof recap repairs."""
from pathlib import Path
import datetime, difflib, hashlib, json, re
from S6_SERIES_PUBLISH_I_candidate17_combined import block, math, displays, refs, write_stable
from S6_SERIES_PUBLISH_synctex_batch import Scanner
R=Path(__file__).resolve().parents[1];O=R/'agents/i_cont_edits'
sha=lambda b:hashlib.sha256(b).hexdigest()
S=R/'S6_SERIES_PUBLISH_I.tex';P=R/'build/I_candidate18/S6_SERIES_PUBLISH_I.pdf'
source='3542f2632cad8f1eb78f0f30f8a64ca91998f3bd1d97010ca76d89297c4bffe7'
pdf='702aaa0abd1a4d8376e213ecaf03a0296592e22063f26db324d805502987e66e'
s=S.read_text();assert sha(S.read_bytes())==source and sha(P.read_bytes())==pdf
oldpath=O/'S6_SERIES_PUBLISH_I_candidate18_root_guards.json'
assert sha(oldpath.read_bytes())=='cd2fce3f086ccd379a45d56e0289efd4273af53297009e877064b4986ba17f05'
guards=json.loads(oldpath.read_text())
data=[
 (r' This proves every assertion in \eqref{pub:I:eq:D-2}.',
  'Delete the closing recap after the explicit vertical-bundle, determinant, cocycle and splitting calculations. The full equation, canonical map, tangent exact sequence, E/G identifications, generators and all proof steps remain. One duplicate equation-reference occurrence is removed with the recap; its exact target is retained.',
  [r'\label{pub:I:eq:D-2}',
   '$\\OO\\gamma\\subset G$ is a subbundle; its quotient is $\\OO(-1)$ by\nthe determinant just computed. Once again $H^1(\\OO(1))=0$ splits the\nextension.']),
 ('This proves every asserted properness and smoothness property\nfor the surface family.\n',
  'Delete the recap after the concrete global deformation and local blow-up construction. The statements and proofs of properness, smoothness, flatness, reducedness, both central components and smooth compact noncentral fibres remain explicitly in the preceding paragraph; all normal-line and Euler-characteristic arguments remain.',
  ['The resulting map $\\mathcal V\\to\\Delta$ remains proper.\nNear the exceptional divisor its local model is the smooth\nspace just computed; elsewhere it is unchanged and smooth.',
   'The other component is $Q$, and their intersection is the original\nmarked elliptic curve.  The local equation $t=\\xi z$ proves\nflatness and reducedness near the intersection; at a smooth\npoint of either component $t$ is a local coordinate.\nThe noncentral fibres are the smooth compact fibres of\n$\\mathcal Y$.'])
]
with Scanner(P) as scan:
 for n,(old,reason,wits) in enumerate(data,5):
  assert s.count(old)==1;pos=s.index(old);label,a,b,kind=block(s,pos)
  x=s[a:b];y=x.replace(old,'',1)
  assert math(x)==math(y) and displays(x)==displays(y)
  removed=[r'\eqref{pub:I:eq:D-2}'] if n==5 else []
  expected_refs=refs(x)
  if removed:
   q=refs(old);assert q==removed
   pfx=x[:x.index(old)];k=len(refs(pfx));assert expected_refs[k]==removed[0]
   expected_refs=expected_refs[:k]+expected_refs[k+1:]
  assert refs(y)==expected_refs
  stem=O/f'S6_SERIES_PUBLISH_I_candidate18_root_v2_review_block_{n:02}'
  pa,pb,pd=[Path(str(stem)+t) for t in ['_original.tex','_proposed.tex','.diff']]
  write_stable(pa,x);write_stable(pb,y);write_stable(pd,''.join(difflib.unified_diff(x.splitlines(True),y.splitlines(True),fromfile=label+'/candidate18',tofile=label+'/recap-proposal')))
  witnesses=[]
  for w in wits:
   assert x.count(w)==y.count(w)==1
   witnesses.append({'exact_text':w,'sha256':sha(w.encode()),'preserved_byte_identically':True})
  line=s[:pos].count('\n')+1;pages=sorted(scan.pages(S,line));assert pages
  guards.append({'id':f'I18-root-{n:02}','type':'D08','statement_id':label,'page':pages[0],'source_line':line,
   'before':old,'after':'','reason':reason,'source_sha256':source,'pdf_sha256':pdf,
   'original_full_block':str(pa.relative_to(R)),'original_full_block_sha256':sha(pa.read_bytes()),
   'proposed_full_block':str(pb.relative_to(R)),'proposed_full_block_sha256':sha(pb.read_bytes()),
   'full_block_contains_all_root_changes_for_this_block':True,'owning_context_kind':kind,
   'all_inline_and_display_mathematical_segments_identical':True,
   'removed_duplicate_reference':removed[0] if removed else None,
   'retained_witnesses':witnesses,'candidate18_synctex_pages':pages,
   'root_review':'Root read the complete current statement and its entire attached proof, including every retained computation and morphism, then compared the exact deletion and complete proposed block. The map is the identity on all mathematical segments and every retained source byte; only the specified pure recap is deleted.',
   'status':'approved by root, awaiting combined guarded application','mathematical_events_added':0})
out=O/'S6_SERIES_PUBLISH_I_candidate18_root_guards_v2.json'
doc={'paper':'I','candidate':18,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':source,'pdf_sha256':pdf,'guards':guards,'supersedes':{'path':str(oldpath.relative_to(R)),'sha256':sha(oldpath.read_bytes()),'scope':'Initial four exact accent guards and their archives remain unchanged; use this six-guard batch instead.'},'bounded_context_review':'The exact This proves every/all recap pattern has four hits in candidate18: two new root repairs, the peer B.4.18 p224 repair, and the peer B.4.32 p255 repair. Each was read in its complete owning proof; no keyword-absence inference supplies general type closure.','mathematical_events_added':0}
write_stable(out,json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(R)),'sha256':sha(out.read_bytes()),'guards':len(guards),'new_guard_pages':{g['id']:g['candidate18_synctex_pages'] for g in guards[4:]},'canonical_source_changed':False}))
