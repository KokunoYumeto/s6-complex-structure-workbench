"""Recompress closed independent dictionary blocks; preserve complete TAR bytes.

The checkpoint31 archive is immutable. Only checkpoint32's representation
changes. Each raw interval is recovered from a hash-locked original XZ block,
and every replacement is independently decoded and byte-compared before use.
The completed dictionary and shared TAR streams are compared byte for byte.
"""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor,wait,FIRST_COMPLETED
import hashlib,json,lzma,shutil,subprocess,time

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'checkpoint31_png_rows_candidate'
STAGE=ROOT.parent/'checkpoint32_png_repack'
BLOCKS=STAGE/'blocks';BLOCKS.mkdir(parents=True,exist_ok=True)
BUNDLES=STAGE/'bundles';BUNDLES.mkdir(exist_ok=True)
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def atomic(p,d):
    q=p.with_suffix(p.suffix+'.pending');q.write_text(json.dumps(d,indent=2)+'\n');q.replace(p)
helper=ROOT/'code/part3_fourfold/assemble_checkpoint31_xz_blocks.py'
prefix=helper.read_text().split('\nstart=time.monotonic()\n')[0]
namespace={'__file__':str(helper)}
exec(compile(prefix,str(helper),'exec'),namespace)
HEADER=namespace['HEADER'];footer=namespace['index_footer'];parse=namespace['parse']
N=5533013871;RAW_SHA='a1c39525e573980a1cc3b8e593f9d887ddf49997f338c4c4a70140bb7180daa1'
oldreceipt=ROOT/'records/checkpoint31_png_rows_xz_block_selection.json'
old=json.loads(oldreceipt.read_text())
assert old['status']=='PASS_FULL_MIXED_STANDARD_XZ_DICTIONARY_BYTE_COMPARISON'
oldcandidate=old['candidate'];oldstream=Path(oldcandidate['file'])
assert sha(oldstream)==oldcandidate['sha256']
original_rows=oldcandidate['blocks']
targets=sorted((r for r in original_rows if Path(r['source']).name=='png_filtered_rows.bin.xz'),key=lambda r:-r['total'])
start=time.monotonic()

def compress(row):
    dest=BLOCKS/f"raw_{row['uncompressed_offset']:012d}.xz";receipt=dest.with_suffix('.json')
    if receipt.exists():
        d=json.loads(receipt.read_text())
        assert d['status']=='PASS_EXACT_ORIGINAL_DICTIONARY_INTERVAL'
        assert sha(dest)==d['sha256'];return d
    with Path(row['source']).open('rb') as inp:
        inp.seek(row['offset']);block=inp.read(row['total'])
    assert len(block)==row['total'] and hashlib.sha256(block).hexdigest()==row['compressed_block_sha256']
    raw=lzma.decompress(HEADER+block+footer([row]))
    assert len(raw)==row['uncompressed']
    pending=dest.with_suffix('.pending')
    command=['xz','-T2','--memlimit-compress=1024MiB','--block-size=64MiB','--lzma2=preset=6,dict=32MiB','--stdout']
    with pending.open('wb') as out:
        run=subprocess.run(command,input=raw,stdout=out,stderr=subprocess.PIPE,check=True)
    assert lzma.decompress(pending.read_bytes())==raw
    pending.replace(dest)
    rr=parse(dest)
    assert len(rr)==1 and rr[0]['uncompressed']==row['uncompressed']
    rr[0]['uncompressed_offset']=row['uncompressed_offset']
    with dest.open('rb') as inp:
        inp.seek(rr[0]['offset']);bb=inp.read(rr[0]['total'])
    rr[0]['compressed_block_sha256']=hashlib.sha256(bb).hexdigest()
    d={'status':'PASS_EXACT_ORIGINAL_DICTIONARY_INTERVAL','original_block':row,
       'candidate_block':rr[0],'path':str(dest),'bytes':dest.stat().st_size,'sha256':sha(dest),
       'raw_bytes':len(raw),'raw_sha256':hashlib.sha256(raw).hexdigest(),
       'saving':row['total']-rr[0]['total'],'command':command,'stderr':run.stderr.decode(),
       'seconds':round(time.monotonic()-start,3)}
    atomic(receipt,d);return d

results=[];iterator=iter(targets);savings=0
with ThreadPoolExecutor(max_workers=2) as pool:
    active={pool.submit(compress,next(iterator)) for _ in range(min(2,len(targets)))}
    while active:
        done,active=wait(active,return_when=FIRST_COMPLETED)
        for future in done:
            d=future.result();results.append(d);savings+=max(0,d['saving'])
            print(json.dumps({'status':d['status'],'offset':d['original_block']['uncompressed_offset'],
                 'saving':d['saving'],'complete_saving':savings,'seconds':d['seconds']}),flush=True)
            if savings<30000000:
                row=next(iterator,None)
                if row is not None:active.add(pool.submit(compress,row))
assert savings>=20000000,('Insufficient completed dictionary savings',savings)
replacements={d['original_block']['uncompressed_offset']:d['candidate_block'] for d in results if d['saving']>0}
selected=[replacements.get(r['uncompressed_offset'],r) for r in original_rows]
position=0
for r in selected:
    assert r['uncompressed_offset']==position;position+=r['uncompressed']
assert position==N
newstream=STAGE/'png_filtered_rows.32.bin.xz';pending=newstream.with_suffix('.pending')
with pending.open('wb') as out:
    out.write(HEADER)
    for row in selected:
        with Path(row['source']).open('rb') as inp:
            inp.seek(row['offset']);block=inp.read(row['total'])
        assert len(block)==row['total'] and hashlib.sha256(block).hexdigest()==row['compressed_block_sha256']
        out.write(block)
    out.write(footer(selected))
digest=hashlib.sha256();amount=0
with lzma.open(pending,'rb') as a,lzma.open(oldstream,'rb') as b:
    while block:=a.read(1024*1024):
        assert block==b.read(len(block));digest.update(block);amount+=len(block)
    assert not b.read(1)
assert amount==N and digest.hexdigest()==RAW_SHA
pending.replace(newstream)

pngreceipt=ROOT/'records/checkpoint31_png_rows_exact_candidate.json'
png=json.loads(pngreceipt.read_text());original=png['png_dictionary'];oldtar=Path(original['local_path'])
assert sha(oldtar)==original['sha256'] and oldtar.stat().st_size==original['bytes']
with oldtar.open('rb') as inp:head=inp.read(4*1024*1024)
decoder=lzma.LZMADecompressor();prefix_decoded=decoder.decompress(head)
assert decoder.eof
prefix_bytes=len(head)-len(decoder.unused_data)
del head,prefix_decoded,decoder
dictionary_bytes=oldstream.stat().st_size
assert prefix_bytes+dictionary_bytes<oldtar.stat().st_size
# Confirm the middle stream is literally the previously verified dictionary.
dg=hashlib.sha256()
with oldtar.open('rb') as inp:
    inp.seek(prefix_bytes);left=dictionary_bytes
    while left:
        block=inp.read(min(left,1024*1024));assert block;dg.update(block);left-=len(block)
assert dg.hexdigest()==sha(oldstream)
candidate=BUNDLES/'checkpoint32_global_png_rows.tar.xz'
pending=candidate.with_suffix('.pending')
with pending.open('wb') as out,oldtar.open('rb') as inp:
    out.write(inp.read(prefix_bytes))
    with newstream.open('rb') as middle:shutil.copyfileobj(middle,out,1024*1024)
    inp.seek(prefix_bytes+dictionary_bytes);shutil.copyfileobj(inp,out,1024*1024)
dg=hashlib.sha256();amount=0
with lzma.open(pending,'rb') as a,lzma.open(oldtar,'rb') as b:
    while block:=a.read(1024*1024):
        assert block==b.read(len(block));dg.update(block);amount+=len(block)
    assert not b.read(1)
pending.replace(candidate)
record={'status':'PASS_IDENTICAL_UNCOMPRESSED_TAR','utc':datetime.now(timezone.utc).isoformat(),
 'original':original,'candidate':{'file':candidate.name,'local_path':str(candidate),
    'bytes':candidate.stat().st_size,'sha256':sha(candidate),'members':original['members']},
 'saving':original['bytes']-candidate.stat().st_size,'tar_bytes':amount,'tar_sha256':dg.hexdigest(),
 'dictionary_bytes':N,'dictionary_sha256':RAW_SHA,
 'complete_dictionary_byte_comparison':True,'complete_tar_byte_comparison':True,
 'prior_dictionary_selection_sha256':sha(oldreceipt),'prior_png_receipt_sha256':sha(pngreceipt),
 'helper_path':str(helper.relative_to(ROOT)),'helper_sha256':sha(helper),
 'script_sha256':sha(Path(__file__)),'recompressed_intervals':results,
 'dictionary_candidate':{'path':str(newstream),'bytes':newstream.stat().st_size,'sha256':sha(newstream)},
 'seconds':round(time.monotonic()-start,3),'scope':'Checkpoint32 transport only; all checkpoint31 archive bytes and every original TAR/member/content byte remain unchanged.'}
receipt=ROOT/'records/checkpoint32_png_dictionary_repack.json';atomic(receipt,record)
print(json.dumps({k:v for k,v in record.items() if k!='recompressed_intervals'},indent=2),flush=True)
