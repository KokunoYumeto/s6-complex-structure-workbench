"""Lossless readable display of every post-exposure LS computation field.

Matrices/vectors are defined once by exact earlier-base replacements.
The inverse recursively substitutes references, then restores the original
JSON separators/order.  Every original stdout byte and both historical
pretty-printed JSON outputs are verified by equality, not by a digest alone.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

W=Path(__file__).resolve().parents[1]
LANE=W/'agents/continuation7_iii_vertical_correction_receiving'
names=['post_local_v001','post_relations_v001','post_obstructions_v001']
matrices={};matrix_ids={};vectors={};vector_ids={};objects={};rows={}

def isint(x):return isinstance(x,int) and not isinstance(x,bool)
def numeric_vector(x):return isinstance(x,list) and x and all(isint(y) for y in x)
def numeric_matrix(x):return isinstance(x,list) and x and all(numeric_vector(y) for y in x) and len({len(y) for y in x})==1
def compact(x):return json.dumps(x,separators=(',',':'))

def encode(x):
    sparse=isinstance(x,dict) and list(x)==['shape','entries'] and isinstance(x['shape'],list) and len(x['shape'])==2
    dense=numeric_matrix(x)
    if sparse or dense:
        shape=tuple(x['shape']) if sparse else (len(x),len(x[0]))
        vals={(i,j):v for i,j,v in x['entries']} if sparse else {(i,j):v for i,row in enumerate(x) for j,v in enumerate(row) if v}
        key=(shape,tuple(sorted(vals.items())))
        if key not in matrix_ids:
            ident='M'+str(len(matrices)+1);matrix_ids[key]=ident
            candidates=[('ZERO',{}),('IDENTITY',{(i,i):1 for i in range(min(shape))})]
            candidates.extend((name,previous) for name,(sh,previous) in matrices.items() if sh==shape)
            options=[]
            for base,previous in candidates:
                changes=[(i,j,vals.get((i,j),0)) for i,j in sorted(vals.keys()|previous.keys()) if vals.get((i,j),0)!=previous.get((i,j),0)]
                options.append((len(changes),base,previous,changes))
            _,base,previous,changes=min(options,key=lambda q:(q[0],q[1]))
            decoded=previous.copy()
            for i,j,v in changes:
                if v:decoded[i,j]=v
                else:decoded.pop((i,j),None)
            assert decoded==vals
            matrices[ident]=(shape,decoded)
            print('MATRIX',ident,'SHAPE',str(shape[0])+'x'+str(shape[1]),'BASE',base,'REPLACE',';'.join(f'{i},{j}:{v}' for i,j,v in changes),flush=True)
        return {'$matrix':matrix_ids[key],'form':'sparse' if sparse else 'dense'}
    if numeric_vector(x):
        key=tuple(x)
        if key not in vector_ids:
            ident='V'+str(len(vectors)+1);vector_ids[key]=ident
            candidates=[('ZERO',[0]*len(x))]+[(n,v) for n,v in vectors.items() if len(v)==len(x)]
            options=[(sum(a!=b for a,b in zip(x,v)),n,v) for n,v in candidates]
            _,base,previous=min(options,key=lambda q:(q[0],q[1]))
            changes=[(i,a) for i,(a,b) in enumerate(zip(x,previous)) if a!=b]
            decoded=previous.copy()
            for i,a in changes:decoded[i]=a
            assert decoded==x;vectors[ident]=decoded
            print('VECTOR',ident,'LENGTH',len(x),'BASE',base,'REPLACE',';'.join(f'{i}:{a}' for i,a in changes),flush=True)
        return {'$vector':vector_ids[key]}
    if isinstance(x,list):return [encode(y) for y in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

def decode(x):
    if isinstance(x,dict) and '$matrix' in x:
        shape,vals=matrices[x['$matrix']]
        if x['form']=='sparse':return dict(shape=list(shape),entries=[[i,j,v] for (i,j),v in sorted(vals.items())])
        return [[vals.get((i,j),0) for j in range(shape[1])] for i in range(shape[0])]
    if isinstance(x,dict) and '$vector' in x:return vectors[x['$vector']].copy()
    if isinstance(x,list):return [decode(y) for y in x]
    if isinstance(x,dict):return {k:decode(v) for k,v in x.items()}
    return x

print('START',datetime.now(timezone.utc).isoformat(),flush=True)
print('INVERSE: copy the named earlier base (ZERO/IDENTITY as specified), replace exactly the listed entries, recursively substitute references retaining dict/list order and sparse/dense form, then JSON-serialize with compact separators. No field is omitted.',flush=True)
for name in names:
    path=W/'code'/('S6_SERIES_PUBLISH_c7_ls_'+name+'.out');blob=path.read_bytes();lines=blob.decode().splitlines();restored=[];rows[name]=[]
    print('INPUT',name,'SHA256',sha256(blob).hexdigest(),'BYTES',len(blob),'LINES',len(lines),flush=True)
    for i,line in enumerate(lines,1):
        if '=' in line:
            label,payload=line.split('=',1)
            try:obj=json.loads(payload)
            except json.JSONDecodeError:obj=None
            if obj is not None:
                encoded=encode(obj);decoded=decode(encoded)
                assert decoded==obj and label+'='+compact(decoded)==line
                print('LINE',name,i,label+'='+compact(encoded),flush=True)
                rows[name].append((label,obj));restored.append(label+'='+compact(decoded));continue
        print('LINE',name,i,line,flush=True);restored.append(line)
    assert ('\n'.join(restored)+'\n').encode()==blob
    print('EXACT_STDOUT_RECONSTRUCTION',name,len(lines),flush=True)
local_rows=[x for label,x in rows['post_local_v001'] if label=='HISTORICAL_LOCAL_EXACT']
global_rows=[x for label,x in rows['post_local_v001'] if label=='GLOBAL_EXACT']
scope=next(x for label,x in rows['post_local_v001'] if label=='HISTORICAL_SCOPE')
recovered=dict(local_component_pair_cases=local_rows,global_profile_residue_cases=global_rows,integral_height_criterion_discrepancies=[],example_I4_P2_Q2=next(x for x in local_rows if (x['kind'],x['p'],x['q'])==('I4',2,2)),scope=scope)
path=LANE/'S6_SERIES_PUBLISH_root_vertical_corrections.json'
assert (json.dumps(recovered,indent=2)+'\n').encode()==path.read_bytes()
print('EXACT_HISTORICAL_JSON_RECONSTRUCTION',path.name,'SHA256',sha256(path.read_bytes()).hexdigest(),'WRAPPER local_component_pair_cases=HISTORICAL_LOCAL_EXACT in printed order; global_profile_residue_cases=GLOBAL_EXACT in printed order; integral_height_criterion_discrepancies=[]; example_I4_P2_Q2=the printed I4,p2,q2 row; scope=HISTORICAL_SCOPE.',flush=True)
relation_rows=[x for label,x in rows['post_relations_v001'] if label=='EXACT_PRESENTATION_COMPARISON']
path=LANE/'S6_SERIES_PUBLISH_fourfolds_corrected_Mumford_examples.json'
assert (json.dumps([x['checked_historical_row'] for x in relation_rows],indent=2)+'\n').encode()==path.read_bytes()
print('EXACT_HISTORICAL_JSON_RECONSTRUCTION',path.name,'SHA256',sha256(path.read_bytes()).hexdigest(),'WRAPPER checked_historical_row from each EXACT_PRESENTATION_COMPARISON in printed order.',flush=True)
path=LANE/'S6_SERIES_PUBLISH_III_02LS_post_relation_data_v001.json'
assert (json.dumps(relation_rows,indent=2)+'\n').encode()==path.read_bytes()
print('EXACT_RELATION_JSON_RECONSTRUCTION',path.name,'SHA256',sha256(path.read_bytes()).hexdigest(),flush=True)
print('OBJECT_COUNTS matrices',len(matrices),'vectors',len(vectors),flush=True)
print('COMPLETE',datetime.now(timezone.utc).isoformat(),flush=True)
