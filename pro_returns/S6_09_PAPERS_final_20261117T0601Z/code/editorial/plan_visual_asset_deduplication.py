"""Plan exact-byte PNG deduplication for a size-limited final ZIP.

No source asset is modified or removed. Required papers, code and all textual
records keep their ordinary paths; only identical PNG copies share stored
bytes. The restoration program recreates every original path losslessly.
"""
from pathlib import Path
import collections, hashlib, json
D=Path(__file__).resolve().parents[2]
groups=collections.defaultdict(list)
for p in sorted(D.rglob('*.png')):
    if p.is_file():groups[hashlib.sha256(p.read_bytes()).hexdigest()].append(p)
preferred=['validation/I_ca65774256bf/','validation/II_f48505e66a68/','validation/III_3da988a3aeb1/']
def rank(p):
    rel=str(p.relative_to(D))
    return (0 if any(rel.startswith(x) for x in preferred) else 1, len(rel), rel)
aliases=[];unique=[]
for digest,paths in sorted(groups.items()):
    paths=sorted(paths,key=rank);canonical=paths[0];name=str(canonical.relative_to(D))
    unique.append({'path':name,'bytes':canonical.stat().st_size,'sha256':digest,'original_path_count':len(paths)})
    for p in paths[1:]:
        assert p.read_bytes()==canonical.read_bytes()
        aliases.append({'original_path':str(p.relative_to(D)),'retained_path':name,'bytes':p.stat().st_size,'sha256':digest,'reason':'Byte-identical visual asset copy; physically superseded in the final ZIP by the exact retained path. The restoration script recreates this original path and verifies its full SHA256.'})
record={'scope':'Only exact-byte duplicate PNG assets. No resizing, recompression, pixel alteration, discarded page, changed proof, omitted output or lost historical version. The source workspace and original checkpoints remain unchanged.','reason':'The immutable sixth checkpoint exceeded the actual Library per-file limit of536870912bytes. Lossless deduplication keeps the single final ZIP below that limit without discarding any byte content.','source_png_paths':sum(map(len,groups.values())),'unique_png_payloads':len(groups),'duplicate_png_paths':len(aliases),'bytes_saved_before_zip_compression':sum(x['bytes'] for x in aliases),'retained_current_final_images_preferred':preferred,'restore_command':'python3 code/editorial/restore_duplicate_visual_assets.py --restore','aliases':sorted(aliases,key=lambda x:x['original_path']),'unique_payloads':sorted(unique,key=lambda x:x['path'])}
(D/'records/visual_asset_deduplication.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k in ['source_png_paths','unique_png_payloads','duplicate_png_paths','bytes_saved_before_zip_compression']}))
