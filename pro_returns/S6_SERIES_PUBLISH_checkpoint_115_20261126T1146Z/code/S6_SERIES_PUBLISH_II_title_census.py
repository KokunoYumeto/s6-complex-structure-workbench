#!/usr/bin/env python3
"""Read-only complete theorem-environment header projection for the D16 gate."""
from pathlib import Path
import hashlib,json,re
def sha(b):return hashlib.sha256(b).hexdigest()
def encode(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def headers(source):
 envs=re.findall(r'\\newtheorem(?:\*?)\{([^}]+)\}',source)
 assert len(envs)==len(set(envs))
 pattern=re.compile(r'\\begin\{('+ '|'.join(re.escape(x) for x in envs)+r')\}(?:\[([^\n]*)\])?')
 out=[]
 for m in pattern.finditer(source):
  line_start=source.rfind('\n',0,m.start())+1
  assert not re.search(r'(?<!\\)%',source[line_start:m.start()]),'Commented environment needs explicit parsing'
  stop=source.index('\\end{'+m[1]+'}',m.end())
  body=source[m.end():stop]
  tags=re.findall(r'\\hypertarget\{tag-([^}]+)\}',body)
  labels=re.findall(r'\\label\{([^}]+)\}',body)
  out.append(dict(index=len(out)+1,environment=m[1],title=m[2],tags=tags,labels=labels,
    source_line=source.count('\n',0,m.start())+1,header=m[0],header_sha256=sha(m[0].encode())))
 return envs,out
def projection(source):
 envs,rows=headers(source)
 return dict(declared_environments=envs,headers=[{k:x[k] for k in ['environment','title','tags','labels']} for x in rows])
def fingerprint(source):return sha(encode(projection(source)))
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('--start',type=int,default=1);p.add_argument('--end',type=int,default=10000);a=p.parse_args()
 s=Path(a.source).read_text();envs,rows=headers(s)
 print('SOURCE',sha(s.encode()),'HEADERS',len(rows),'FINGERPRINT',fingerprint(s))
 for x in rows:
  if a.start<=x['index']<=a.end:print(str(x['index'])+' | '+','.join(x['tags'])+' | '+x['environment']+' | '+str(x['title']))
