from pathlib import Path
import json
from tex_tools import PAPERS,bibliography
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'
result={}
for paper in PAPERS:
    text=(SOURCE/f'S6_10_PAPERS_{paper}.tex').read_text()
    a,b,header,entries=bibliography(text)
    for key,value in entries.items():result.setdefault(key,[]).append({'paper':paper,'text':value})
(ROOT/'analysis/source_bibliography_entries.json').write_text(json.dumps(result,indent=2,ensure_ascii=False))
print(json.dumps({'source_bibliography_keys':len(result)}))
