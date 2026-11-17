"""Make source checkers portable, preserving all mathematical checks verbatim."""
from pathlib import Path
import hashlib, json, shutil
ROOT=Path(__file__).resolve().parents[3]
SRC=ROOT/'sources/codex_workspace/courses/CG-S6'
OUT=ROOT/'deliverables/code/maps_audit/course/stable'
OUT.mkdir(parents=True,exist_ok=True)
OLD=OUT/'original_context';OLD.mkdir(exist_ok=True)
spec=[('verify_coefficient_rings.py','coefficient-rings-and-the-original-degree-six-class.md'),('verify_degree_six_cobar.py','the-degree-six-milnor-cobar-calculation.md')]
records=[]
for name in ['calculate_original_coefficient_h28.py','calculate_degree_six_cobar.py']:
 src=SRC/'checks'/name;shutil.copyfile(src,OLD/name);shutil.copyfile(src,OUT/name)
 records.append(dict(program=name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),portable_sha256=hashlib.sha256((OUT/name).read_bytes()).hexdigest(),changes='None. Original already writes beside __file__.',mathematics_unchanged=True))
for name,chapter in spec:
 src=SRC/'checks'/name;shutil.copyfile(src,OLD/name);text=src.read_text()
 original_hash=hashlib.sha256((SRC/'src'/chapter).read_bytes()).hexdigest()
 text=text.replace('W=Path(__file__).resolve().parents[1]','W=Path(__file__).resolve().parent\nimport sys\nSOURCE_ARG=Path(sys.argv[1]) if len(sys.argv)>1 else None\nSOURCE_HASH_RECOMPUTED=bool(SOURCE_ARG and SOURCE_ARG.is_file())\nSOURCE_SHA256=hashlib.sha256(SOURCE_ARG.read_bytes()).hexdigest() if SOURCE_HASH_RECOMPUTED else '+repr(original_hash))
 text=text.replace("W/'checks/calculate_original_coefficient_h28.py'","W/'calculate_original_coefficient_h28.py'")
 text=text.replace("W/'checks/COEFFICIENT_RING_CHECKS.json'","W/'COEFFICIENT_RING_CHECKS.json'")
 text=text.replace("W/'checks/DEGREE_SIX_COBAR_CHECKS.json'","W/'DEGREE_SIX_COBAR_CHECKS.json'")
 text=text.replace('hashlib.sha256(note.read_bytes()).hexdigest()','SOURCE_SHA256').replace('hashlib.sha256(src.read_bytes()).hexdigest()','SOURCE_SHA256')
 # The original source variable is used only for a name/hash, never for a test.
 if name=='verify_degree_six_cobar.py':
  text=text.replace("result=dict(passed=", "result=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17', source_hash_recomputed=SOURCE_HASH_RECOMPUTED, passed=")
 else:
  text=text.replace("report=dict(passed=", "report=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17', source_hash_recomputed=SOURCE_HASH_RECOMPUTED, passed=")
 (OUT/name).write_text(text)
 records.append(dict(program=name,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),portable_sha256=hashlib.sha256((OUT/name).read_bytes()).hexdigest(),source_chapter=chapter,recorded_original_source_sha256=original_hash,changes='Path and metadata only: output beside __file__, sibling helper import/run, optional first source-path argument for recomputing the provenance hash; otherwise the recorded original hash with source_hash_recomputed=false. Added exact current-reader metadata. Original-context copy retains original bytes. All mathematical definitions, ranges, assertions and check names unchanged.',mathematics_unchanged=True))
(OUT/'portable_preparation.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(prepared=len(records),output=str(OUT.relative_to(ROOT)))))
