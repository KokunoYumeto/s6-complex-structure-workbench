"""Select unchanged, closed XZ blocks on identical dictionary intervals.

Format authority: https://tukaani.org/xz/xz-file-format.txt, sections
2.1.2, 3.1, 3.3 and 4.  Compressed data/check bytes are copied literally.
The completed output is decoded with Python's independent liblzma wrapper
and compared byte for byte with the entire original dictionary.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,lzma,struct,sys,time,zlib

ROOT=Path(__file__).resolve().parents[2]
STAGE=ROOT.parent/'checkpoint31_png_rows_candidate'
RAW=STAGE/'png_filtered_rows.bin'
N=5533013871
RAW_SHA='a1c39525e573980a1cc3b8e593f9d887ddf49997f338c4c4a70140bb7180daa1'
HEADER=bytes.fromhex('fd377a585a000004e6d6b446')

def sha(path):
    with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def vli(n):
    assert 0<=n<2**63
    out=bytearray()
    while n>=128:out.append((n&127)|128);n>>=7
    out.append(n);return bytes(out)
def read_vli(b,i):
    n=0;shift=0;start=i
    while True:
        assert i<len(b) and i-start<9
        c=b[i];i+=1;n|=(c&127)<<shift
        if not c&128:
            assert i-start==1 or c!=0
            return n,i
        shift+=7
def crc(b):return struct.pack('<I',zlib.crc32(b)&0xffffffff)
def index_footer(rows):
    data=b'\0'+vli(len(rows))+b''.join(vli(r['unpadded'])+vli(r['uncompressed']) for r in rows)
    data+=bytes((-len(data))%4);index=data+crc(data)
    foot=struct.pack('<I',len(index)//4-1)+HEADER[6:8]
    return index+crc(foot)+foot+b'YZ'
def parse(path,complete=False):
    size=path.stat().st_size;rows=[];off=12;raw=0
    with path.open('rb') as f:
        assert f.read(12)==HEADER
        while off+4<=size:
            f.seek(off);first=f.read(1)
            if first==b'\0':break
            hsize=(first[0]+1)*4
            if off+hsize>size:break
            f.seek(off);h=f.read(hsize)
            assert h[-4:]==crc(h[:-4])
            flags=h[1];assert flags&0x3c==0 and flags&0xc0==0xc0
            cs,i=read_vli(h,2);us,i=read_vli(h,i)
            assert cs>0 and us>0
            for _ in range((flags&3)+1):
                fid,i=read_vli(h,i);ps,i=read_vli(h,i);i+=ps
                assert fid==0x21 and ps==1
            assert h[i:-4]==bytes(len(h)-4-i)
            unpadded=hsize+cs+8;padded=(unpadded+3)&~3
            if off+padded>size:break
            f.seek(off+hsize+cs);padding=f.read(padded-unpadded)
            assert padding==bytes(len(padding))
            rows.append({'source':str(path),'offset':off,'total':padded,'unpadded':unpadded,
                         'uncompressed_offset':raw,'uncompressed':us,'header_hex':h.hex()})
            off+=padded;raw+=us
        if complete:
            f.seek(off);tail=f.read()
            assert tail==index_footer(rows)
            assert raw==N
    return rows

def emit(row):print(json.dumps(row),flush=True)
def assemble(rows,path,expected_bytes):
    pending=path.with_suffix(path.suffix+'.pending');copied=[]
    with pending.open('wb') as out:
        out.write(HEADER)
        for row in rows:
            dg=hashlib.sha256();left=row['total']
            with Path(row['source']).open('rb') as inp:
                inp.seek(row['offset'])
                while left:
                    block=inp.read(min(left,1024*1024));assert block
                    out.write(block);dg.update(block);left-=len(block)
            copied.append(dict(row,compressed_block_sha256=dg.hexdigest()))
        out.write(index_footer(rows))
    digest=hashlib.sha256();amount=0
    with lzma.open(pending,'rb') as inp,RAW.open('rb') as original:
        while block:=inp.read(1024*1024):
            assert block==original.read(len(block))
            digest.update(block);amount+=len(block)
        assert amount==expected_bytes
        if expected_bytes==N:
            assert not original.read(1) and digest.hexdigest()==RAW_SHA
    pending.replace(path)
    return {'file':str(path),'bytes':path.stat().st_size,'sha256':sha(path),
            'uncompressed_bytes':amount,'uncompressed_sha256':digest.hexdigest(),
            'full_original_byte_comparison':True,'blocks':copied}

start=time.monotonic()
fast=STAGE/'png_filtered_rows.bin.xz'
fast_rows=parse(fast,True);all_rows=list(fast_rows);closed={fast.name:len(fast_rows)}
for name in ['png_filtered_rows.p6_32.bin.xz','png_filtered_rows.p5_32.bin.xz']:
    path=STAGE/name
    if path.exists() and path.stat().st_size>=12:
        rr=parse(path);all_rows+=rr;closed[name]=len(rr)
for receipt in sorted((STAGE/'targeted_blocks').glob('block_*.json')):
    r=json.loads(receipt.read_text());path=Path(r['path'])
    assert r['status']=='PASS_TARGET_INTERVAL_BYTE_EQUAL'
    assert path.stat().st_size==r['bytes'] and sha(path)==r['sha256']
    rr=parse(path);assert sum(x['uncompressed'] for x in rr)==r['raw_bytes']
    for x in rr:x['uncompressed_offset']+=r['offset']
    all_rows+=rr;closed[path.name]=len(rr)
by_start={}
for row in all_rows:by_start.setdefault(row['uncompressed_offset'],[]).append(row)
dp={N:(0,[])}
for off in sorted(by_start,reverse=True):
    opts=[]
    for row in by_start[off]:
        end=off+row['uncompressed']
        if end in dp:opts.append((row['total']+dp[end][0],[row]+dp[end][1]))
    if opts:dp[off]=min(opts,key=lambda x:x[0])
cost,selected=dp[0]
exact_size=12+cost+len(index_footer(selected))
total_with_allowance=176079208+1509556+exact_size+10000000
measure={'utc':datetime.now(timezone.utc).isoformat(),'closed_blocks':closed,
         'selected_blocks':len(selected),'dictionary_bytes':exact_size,
         'all_bundles_plus_10MB_allowance':total_with_allowance,
         'fits_512MiB_with_allowance':total_with_allowance<=536870912}
emit(measure)
if '--measure' in sys.argv:raise SystemExit(0)
if '--self-test' in sys.argv:
    first=next(r for r in all_rows if r['source']!=str(fast) and r['uncompressed_offset']==0)
    end=first['uncompressed'];extra=[r for r in fast_rows if end<=r['uncompressed_offset']<end+268435456]
    rows=[first]+extra
    result=assemble(rows,STAGE/'mixed_xz_self_test.xz',sum(r['uncompressed'] for r in rows))
    status='PASS_MIXED_STANDARD_XZ_PREFIX_BYTE_COMPARISON'
else:
    assert measure['fits_512MiB_with_allowance'],measure
    result=assemble(selected,STAGE/'png_filtered_rows.mixed.bin.xz',N)
    status='PASS_FULL_MIXED_STANDARD_XZ_DICTIONARY_BYTE_COMPARISON'
record={'status':status,'utc':datetime.now(timezone.utc).isoformat(),'measurement':measure,
        'candidate':result,'original_dictionary_sha256':RAW_SHA,
        'fast_source_sha256':sha(fast),'program_sha256':sha(__file__),
        'format_authority':'https://tukaani.org/xz/xz-file-format.txt',
        'seconds':round(time.monotonic()-start,3)}
dest=ROOT/'records'/('checkpoint31_png_rows_xz_self_test.json' if '--self-test' in sys.argv else 'checkpoint31_png_rows_xz_block_selection.json')
dest.write_text(json.dumps(record,indent=2)+'\n')
emit({k:v for k,v in record.items() if k not in ['candidate']})
