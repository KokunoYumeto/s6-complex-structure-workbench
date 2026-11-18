"""Recover original shared theorem counters for explicit source comparisons.

The resulting map is a locator aid.  A caller must compare the original text
before replacing a literal reference; it is not a mathematical check.
"""
from pathlib import Path
import json,re
from inventory_reconcile import TexIndex,commands

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parents[1]

def letters(n):
    ans=''
    while n:
        n,k=divmod(n-1,26);ans=chr(65+k)+ans
    return ans

def generate():
    result={}
    for paper in ['I','II','III']:
        idx=TexIndex(ROOT/f'sources/s6_09/S6_09_PAPERS_{paper}.tex');s=idx.text
        events=[]
        for c in idx.sections:
            if not s[c['start']:].startswith(r'\section*'):
                events.append((c['start'],'section',c))
        for m in re.finditer(r'\\appendix\b',s):events.append((m.start(),'appendix',{}))
        for b in idx.blocks:events.append((b['start'],'block',b))
        section=0;theorem=0;appendix=False
        for position,kind,item in sorted(events,key=lambda x:x[0]):
            if kind=='appendix':appendix=True;section=0;theorem=0;continue
            if kind=='section':section+=1;theorem=0;continue
            theorem+=1
            sec=letters(section) if appendix else str(section)
            number=f'{sec}.{theorem}'
            exact=s[item['start']:item['statement_end']]
            labels=[x['value'] for x in commands(exact,'label')]
            result[paper+':'+number]={'paper':paper,'number':number,'environment':item['env'],
                'label':labels[0] if labels else None,'labels':labels,
                'file':str(idx.path.relative_to(ROOT)),'start':item['start'],'statement_end':item['statement_end'],
                'proof_end':item['end'],'source_line':s[:item['start']].count('\n')+1,
                'statement_prefix':exact[:700],
                'validation':'Counter reconstruction from original unstarred sections, appendix reset, and shared theorem environments; verify the displayed source statement before substitution.'}
    return result

def main():
    result=generate();p=OUT/'analysis/inventory_legacy_numbers.json';p.write_text(json.dumps(result,indent=2))
    for key in ['I:17.4','I:23.1','I:4.8','I:23.4','I:23.5','II:16.33','II:16.34','III:4.20']:
        v=result.get(key);print(key,v['label'] if v else 'missing',v['source_line'] if v else '')

if __name__=='__main__':main()
