"""Lossless record-delta display of the first complete LS post readback.

All matrix/vector definitions remain literal.  Repeated structured records
use an earlier same-label record plus absolute path replacements, retaining
dictionary order and list length as explicit nodes.  This is a second exact
inverse display, not a mathematical rerun or a change to earlier evidence.
"""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

W=Path(__file__).resolve().parents[1]
source=W/'code/S6_SERIES_PUBLISH_c7_ls_post_readback_v001.out'
blob=source.read_bytes();lines=blob.decode().splitlines()
records={};labels={};restored=[]
def compact(x):return json.dumps(x,separators=(',',':'))
def flatten(x,path=(),out=None):
    if out is None:out={}
    if isinstance(x,dict) and not ('$matrix' in x or '$vector' in x):
        out[path]=['dict',list(x)]
        for key,value in x.items():flatten(value,path+(key,),out)
    elif isinstance(x,list):
        out[path]=['list',len(x)]
        for key,value in enumerate(x):flatten(value,path+(key,),out)
    else:out[path]=['value',x]
    return out
def expand(flat,path=()):
    kind,value=flat[path]
    if kind=='dict':return {key:expand(flat,path+(key,)) for key in value}
    if kind=='list':return [expand(flat,path+(key,)) for key in range(value)]
    return value
print('START',datetime.now(timezone.utc).isoformat(),flush=True)
print('INPUT_SHA256',sha256(blob).hexdigest(),'BYTES',len(blob),'LINES',len(lines),flush=True)
print('INVERSE: MATRIX/VECTOR lines are unchanged first-readback lines. For RECORD copy BASE flat path map; replace each [path,node] literally (null deletes). Nodes dict/list retain key order/length, value retains its exact scalar/reference. Expand from root, compact-serialize and prepend PREFIX to recover the original first-readback line.',flush=True)
for number,line in enumerate(lines,1):
    match=re.match(r'^(LINE \S+ \d+ )([A-Z_]+)=(.*)$',line)
    if not match:
        print('SOURCE_LINE',number,line,flush=True);restored.append(line);continue
    prefix,label,payload=match.groups();obj=json.loads(payload);current=flatten(obj)
    candidates=[('ZERO',{})]+[(name,records[name]) for name in labels.get(label,[])]
    options=[]
    for base,previous in candidates:
        changes=[[list(path),current.get(path)] for path in sorted(current.keys()|previous.keys(),key=lambda p:compact(list(p))) if current.get(path)!=previous.get(path)]
        options.append((len(compact(changes)),base,previous,changes))
    _,base,previous,changes=min(options,key=lambda x:(x[0],x[1]));decoded=previous.copy()
    for path,node in changes:
        if node is None:decoded.pop(tuple(path),None)
        else:decoded[tuple(path)]=node
    assert decoded==current and prefix+label+'='+compact(expand(decoded))==line
    ident='R'+str(len(records)+1);records[ident]=decoded;labels.setdefault(label,[]).append(ident)
    print('SOURCE_LINE',number,'RECORD',ident,'PREFIX',json.dumps(prefix+label+'='),'BASE',base,'REPLACE',compact(changes),flush=True)
    restored.append(prefix+label+'='+compact(expand(decoded)))
assert ('\n'.join(restored)+'\n').encode()==blob
print('EXACT_FIRST_READBACK_RECONSTRUCTION',len(lines),'lines, every byte identical; preceding reader reconstructs all three stdout streams and both historical JSON outputs.',flush=True)
print('RECORD_COUNT',len(records),flush=True)
print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
