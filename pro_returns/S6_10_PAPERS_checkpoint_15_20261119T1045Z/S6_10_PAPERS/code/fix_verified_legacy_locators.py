"""Restore labels for individually opened and matched S6_09 literal locators.

These changes repair references only and confer no new proof-check credit.
"""
from pathlib import Path
import argparse,hashlib,json,re
P=Path(__file__).resolve().parents[1]
M=json.loads((P/'analysis/inventory_legacy_numbers.json').read_text())
CONFIRMED={
 'I:5.5','I:23.4','I:23.6','I:23.2','I:23.3','I:21.17','I:23.7','I:21.36','I:23.5','I:Q.2','I:Q.1','I:B.2','I:B.11',
 'I:21.58','I:19.6','I:19.5','I:20.4','I:20.11','I:20.12','I:18.5','I:4.9','I:4.10','I:5.10','I:22.16','I:3.3','I:3.4',
 'I:3.8','I:4.5','I:4.6','I:4.7','I:4.8','I:23.1','I:20.1','I:20.2','I:20.3','II:9.5','II:9.7'
}
PATTERN=r'Paper[~ ]+([IV]+),\s*(Proposition|Theorem|Lemma|Remark|Corollary)~([A-Z0-9]+\.[0-9]+)'
SPECIAL=r'Paper I, Proposition~B.2, Theorem~B.6 and Proposition~B.9'
def fix_legacy_locators(text,source=''):
 changes=[]
 if SPECIAL in text:
  new=r'\cref{wb:prop:period-input-audit,wb:thm:candidate-cusp-geometry,wb:prop:candidate-finite-fillings}'
  changes.append({'source':source,'old':SPECIAL,'new':new,'scope':'All three original statements and actual calling construction opened and matched.'})
  text=text.replace(SPECIAL,new)
 # The doubled prefix is itself an inherited literal typo.
 text=text.replace('Paper~I, Paper~I, Theorem~21.58','Paper~I, Theorem~21.58')
 def sub(m):
  key=m[1]+':'+m[3]
  if key not in CONFIRMED:return m[0]
  t=M[key];new=r'\cref{'+t['label']+'}'
  changes.append({'source':source,'legacy_key':key,'old':m[0],'new':new,'target_source_file':t['file'],'target_source_line':t['source_line'],'scope':'Original complete target statement and every current calling passage opened and matched; I20.11/I20.12/I22.16 proof passages separately opened for the exact internal formulas used.'})
  return new
 return re.sub(PATTERN,sub,text),changes

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('paths',nargs='+');ap.add_argument('--record',required=True);a=ap.parse_args()
 logs=[]
 for rel in a.paths:
  f=P/rel;old=f.read_text();new,changes=fix_legacy_locators(old,rel)
  if new!=old:f.write_text(new)
  logs.append({'file':rel,'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(new.encode()).hexdigest(),'changes':changes})
 (P/a.record).write_text(json.dumps(logs,indent=2))
 print('Repaired',sum(len(r['changes']) for r in logs),'verified literal locators in',len(logs),'files; no mathematical check credit assigned.')
