"""Smaller exact representations of closed TAR streams for checkpoint35 only.

Every candidate is compared byte-for-byte with the complete original decoded
TAR stream. The34 archive, immutable freezes, dictionary and original closed
bundles are read-only. No member name, content byte or codec is changed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, lzma, time

ROOT=Path(__file__).resolve().parents[1]; BASE=ROOT.parent
STAGE=BASE/'checkpoint35_encoding'

def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def atomic(path,value):
    tmp=path.with_suffix(path.suffix+'.pending')
    tmp.write_text(json.dumps(value,indent=2)+'\n');tmp.replace(path)

def compare_decoded(original,candidate):
    digest=hashlib.sha256();amount=0
    with lzma.open(original,'rb') as a,lzma.open(candidate,'rb') as b:
        while True:
            left=a.read(1024*1024);right=b.read(1024*1024)
            assert left==right,'Decoded TAR bytes differ'
            if not left:break
            digest.update(left);amount+=len(left)
    return amount,digest.hexdigest()

def repack_one(original,entry,destination):
    assert original.stat().st_size==entry['bytes'] and sha(original)==entry['sha256']
    receipt=destination.with_suffix(destination.suffix+'.json')
    if receipt.exists():
        result=json.loads(receipt.read_text())
        assert result['original']==entry
        assert destination.stat().st_size==result['candidate_bytes']
        assert sha(destination)==result['candidate_sha256']
        assert compare_decoded(original,destination)==(result['tar_bytes'],result['tar_sha256'])
        return result
    assert not destination.exists(),'Unreceipted candidate requires preservation before retry'
    tmp=destination.with_suffix(destination.suffix+'.partial')
    if tmp.exists():tmp.rename(tmp.with_name(tmp.name+'.interrupted_'+str(time.time_ns())))
    digest=hashlib.sha256();amount=0
    with lzma.open(original,'rb') as source,lzma.open(tmp,'xb',filters=[{
        'id':lzma.FILTER_LZMA2,'preset':9|lzma.PRESET_EXTREME,
        'dict_size':64*1024*1024}]) as target:
        while block:=source.read(1024*1024):
            digest.update(block);amount+=len(block);target.write(block)
    tmp.replace(destination)
    assert compare_decoded(original,destination)==(amount,digest.hexdigest())
    bundle=dict(entry,file=destination.name,bytes=destination.stat().st_size,sha256=sha(destination))
    result={'status':'PASS_IDENTICAL_UNCOMPRESSED_TAR','original':entry,
        'candidate_file':destination.name,'candidate_bytes':destination.stat().st_size,
        'candidate_sha256':sha(destination),'bundle':bundle,'tar_bytes':amount,
        'tar_sha256':digest.hexdigest(),'complete_byte_comparison':True,
        'dictionary_bytes':64*1024*1024,'saving':entry['bytes']-destination.stat().st_size,
        'use_candidate':destination.stat().st_size<entry['bytes']}
    atomic(receipt,result)
    return result

def main():
    measured=json.loads((STAGE/'checkpoint35_size_measurement.json').read_text())
    assert measured['over_limit_bytes']>0,'No measured overflow requires repair'
    freeze=STAGE/'frozen_manifest.json';priorpath=BASE/'checkpoint34_encoding/checkpoint34_transport_manifest.json'
    prior=json.loads(priorpath.read_text())
    frozenhash=sha(freeze);priorhash=sha(priorpath)
    destinations={'new':BASE/'checkpoint35_new_repack','extra':BASE/'checkpoint35_extra_repack'}
    manifests={};paths={}
    for kind,folder in destinations.items():
        folder.mkdir(exist_ok=True)
        path=folder/('new_repack_manifest.json' if kind=='new' else 'extra_repack_manifest.json')
        paths[kind]=path
        if path.exists():
            data=json.loads(path.read_text())
            assert data['frozen_manifest_sha256']==frozenhash
            assert data['prior_manifest_sha256']==priorhash
        else:data={'status':'PASS','frozen_manifest_sha256':frozenhash,
            'prior_manifest_sha256':priorhash,'dictionary_bytes':64*1024*1024,'entries':{}}
        manifests[kind]=data
    existing=sum(row['saving'] for data in manifests.values() for row in data['entries'].values() if row['use_candidate'])
    target=existing+measured['over_limit_bytes']+512*1024
    sources=[]
    for receipt in sorted(STAGE.glob('checkpoint35_new_content_*.tar.xz.json')):
        row=json.loads(receipt.read_text());sources.append(('new',row,STAGE/row['file']))
    folders=[BASE/f'checkpoint{k}_encoding' for k in range(34,23,-1)]
    folders+=sorted(p for p in BASE.glob('checkpoint*_repack') if p.is_dir())
    folders+=[BASE/'checkpoint33_final_encoding',BASE/'checkpoint33_member_repair',BASE/'checkpoint33_dictionary_rgb_complete',BASE/'checkpoint33_png_rows_candidate',BASE/'checkpoint33_zlib_complete_candidate',BASE/'checkpoint32_png_repack/bundles',BASE/'checkpoint34_png_repack/bundles',BASE/'checkpoint31_png_rows_candidate/bundles',BASE/'checkpoint24_content_preparation/bundles']
    dictionary=prior['dictionary_representation']['candidate']['file']
    protected_dictionaries={dictionary}
    outer=prior.get('checkpoint33_dictionary_outer_representation',{})
    if outer:protected_dictionaries.add(outer['selected_bundle']['file'])
    for row in prior['bundles']:
        if row['file'] in protected_dictionaries:continue
        source=next(folder/row['file'] for folder in folders if (folder/row['file']).is_file())
        sources.append(('extra',row,source))
    sources.sort(key=lambda x:(x[0]!='new','extreme' in x[1]['file'],-x[1]['bytes']))
    saving=existing
    for kind,row,source in sources:
        if saving>=target:break
        if row['file'] in manifests[kind]['entries']:continue
        out=destinations[kind]/('checkpoint35_p9_'+row['file'])
        result=repack_one(source,row,out)
        result['frozen_manifest_sha256']=frozenhash
        manifests[kind]['entries'][row['file']]=result
        atomic(paths[kind],manifests[kind])
        saving+=result['saving'] if result['use_candidate'] else 0
        print(json.dumps({'status':result['status'],'kind':kind,'file':row['file'],
            'saving':result['saving'],'complete_saving':saving,'target_saving':target}),flush=True)
    receipt={'status':'PASS_REQUIRED_SAVING' if saving>=target else 'ALL_EXACT_CANDIDATES_MEASURED',
        'utc':datetime.now(timezone.utc).isoformat(),'measured_archive_bytes':measured['candidate_archive_bytes'],
        'required_saving_with_margin':target,'verified_saving':saving,
        'manifests':{k:{'path':str(p),'sha256':sha(p)}for k,p in paths.items()if p.exists()},
        'inherited_dictionary_untouched':True,'prior_archive_untouched':True}
    atomic(ROOT/'records/checkpoint35_closed_stream_recompression.json',receipt)
    print(json.dumps(receipt,indent=2),flush=True)
    assert saving>=target,'Exact stream candidates exhausted; preserve all candidates and inspect next byte-reversible option'

if __name__=='__main__':main()
