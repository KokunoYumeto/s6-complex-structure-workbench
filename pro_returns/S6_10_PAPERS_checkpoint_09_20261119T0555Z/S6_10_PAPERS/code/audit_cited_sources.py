"""List exact cited-key source gates; a key match confers only its recorded scope."""
from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1]
PREVIEWS={'I':'build/I_preview','II':'build/sign_II','III':'build/III_preview','IV':'analysis/IV/preview','V':'analysis/V/preview','VI':'build/sign_VI'}
verified=json.loads((P/'analysis/current_bibliography_verification.json').read_text())
known=set(verified['matched_keys'])
dispositions_path=P/'analysis/final_source_gate_dispositions.json'
nonoperative=json.loads(dispositions_path.read_text()).get('unverified_nonoperative',{}) if dispositions_path.exists() else {}
bib=(P/'S6_10_PAPERS_references.bib').read_text();available=set(re.findall(r'^@\w+\{([^,]+),',bib,re.M));out={}
for paper,folder in PREVIEWS.items():
 s=(P/folder/'preview.tex').read_text()+'\n'+(P/'papers/common_declarations.tex').read_text();keys=set()
 for m in re.finditer(r'\\(?:no)?cite\w*\*?\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}',s):keys.update(k.strip() for k in m[1].split(','))
 out[paper]={'cited_keys':sorted(keys),'bounded_reading_keys':sorted(keys&known),'pending_keys':sorted(keys-known),'missing_bib_entries':sorted(keys-available),'scope':'Cited-key identity audit only. Every bounded reading retains the precise statement, edition, hypothesis and proof-reading scope recorded in its source event.'}
 out[paper]['unverified_nonoperative_keys']=sorted((keys-known)&set(nonoperative)) if paper=='I' else []
 out[paper]['operative_pending_keys']=sorted((keys-known)-set(out[paper]['unverified_nonoperative_keys']))
 out[paper]['nonoperative_disposition_record']='analysis/final_source_gate_dispositions.json' if out[paper]['unverified_nonoperative_keys'] else ''
(P/'analysis/cited_source_audit.json').write_text(json.dumps(out,indent=2))
for p,r in out.items():print(p,len(r['cited_keys']),'cited;',len(r['bounded_reading_keys']),'with bounded current readings; pending',','.join(r['pending_keys']),'missing',','.join(r['missing_bib_entries']))
