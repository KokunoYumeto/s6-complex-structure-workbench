#!/usr/bin/env python3
"""Exact macro expansion and source-level apparatus census for Paper II."""
from pathlib import Path
import hashlib,json,re
MACRO=r'\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}'
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def argument(s,p):
 while s[p].isspace():p+=1
 assert s[p]=='{';a=p;depth=1;p+=1
 while depth:
  if s[p]=='\\':p+=2;continue
  if s[p]=='%':p=s.index('\n',p)+1;continue
  if s[p]=='{':depth+=1
  elif s[p]=='}':depth-=1
  p+=1
 return s[a+1:p-1],p
def records(s):
 out=[]
 for m in re.finditer(r'\\StatementRecord\{',s):
  p=m.end()-1;args=[]
  for _ in range(4):v,p=argument(s,p);args.append(v)
  out.append(dict(start=m.start(),end=p,line=s.count('\n',0,m.start())+1,owner=args[0],status=args[1],tag=args[2],uses=args[3],call=s[m.start():p]))
 return out
def mask_records(s):
 chars=list(s)
 for r in records(s):
  for i in range(r['start'],r['end']):
   if chars[i]!='\n':chars[i]=' '
 return ''.join(chars)
PATTERNS={
 'machine_header_text':r'proved\s+checks\s+uses|uses\s+and\s+used\s+by|proves\s+step\s+\d+\s+of\s+Theorem|Expansion\s*:|Proof\s+in\s+outline;\s*full\s+statements',
 'proof_navigation':r'Return\s+to\s+(?:\\(?:S|S1)|§|section\s*1)|(?:AfterEndEnvironment|AtEndEnvironment)\{proof\}',
 'depth_prefix':r'\\langle[12]\\rangle',
 'duplicate_first_marker':r'\\item\s*(?:\\noindent\s*)?\\textbf\{Step\s*1\.\}',
 'apparatus_invocation':r'\\(?:PrintUses|UsedBy|CurrentChecker|ProofChecks|SBack|RungZero|RungOne)\b',
 'printed_record_link':r'S6_SERIES_(?:GRIND|PUBLISH)_checks_[IV]+\.md|\\text(?:bf|it)\{(?:uses|checks|used by)\s*:',
 'false_header_description':r'statement\s+headers\s+give\s+the\s+full|headers\s+(?:print|contain)\s+(?:full\s+)?uses',
}
def census(s):
 start=s.index(r'\begin{document}');body=mask_records(s)[start:];hits=[]
 for name,pat in PATTERNS.items():
  for m in re.finditer(pat,body,re.I):
   pos=start+m.start();a=s.rfind('\n\n',0,pos);b=s.find('\n\n',pos);a=max(0,a);b=len(s) if b<0 else b
   hits.append(dict(kind=name,line=s.count('\n',0,pos)+1,match=m.group(),paragraph=s[a:b]))
 macros=re.findall(r'\\(?:re)?newcommand\{\\StatementRecord\}[^\n]*',s)
 all_records=records(s);assert all(re.fullmatch(r'[0-9A-Z]{4}',r['tag']) for r in all_records)
 return dict(only_minimal_record_macro=macros==[MACRO],all_record_tags_valid=True,record_calls=len(all_records),proof_ends=s.count(r'\end{proof}'),active_blocking_hits=hits,body_has_record_redefinition=bool(re.search(r'\\(?:re)?newcommand\{\\StatementRecord\}',s[start:])))
def valid(s):
 c=census(s);return c['only_minimal_record_macro'] and c['all_record_tags_valid'] and not c['active_blocking_hits'] and not c['body_has_record_redefinition']
def fingerprint(s):
 c=census(s)
 return sha(enc({k:c[k] for k in ['only_minimal_record_macro','all_record_tags_valid','active_blocking_hits','body_has_record_redefinition']}))
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('source');a=p.parse_args();s=Path(a.source).read_text();print(json.dumps(census(s),indent=2,ensure_ascii=False));print('fingerprint',fingerprint(s))
