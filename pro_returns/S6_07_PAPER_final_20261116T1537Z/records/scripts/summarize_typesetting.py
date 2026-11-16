from pathlib import Path
import json, re

R=Path(__file__).resolve().parents[1]
def read_stats(path,name):
    text=path.read_text()
    values=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',text)]
    pages=re.findall(r'Output written on .*?\((\d+) pages',text,re.S)
    undefined=len(re.findall(r'LaTeX Warning: (?:Reference|Citation)[^\n]*(?:\n[^\n]*){0,2}?undefined',text))
    return {'name':name,'log':str(path.relative_to(R.parent)),
            'pages':int(pages[-1]) if pages else None,'overfull_total':len(values),
            'overfull_above_2pt':sum(x>2 for x in values),'max_excess_pt':max(values,default=0),
            'missing_glyphs':text.count('Missing character:'),'underfull_total':text.count('Underfull \\'),
            'latex_warnings':text.count('LaTeX Warning:'),
            'undefined_references_or_citations':undefined,
            'fatal_error':bool(re.search(r'^! |Fatal error',text,re.M))}
logs=sorted(R.glob('build/master_pass[0-9][0-9].log'))
final=read_stats(logs[-1],'Final delivery build')
initial=read_stats(R/'build/master_initial_complete.log','First complete build')
intermediate=read_stats(R/'build/master_pass05.log','Intermediate audit-table rewrite')
result={'comparison':[initial,intermediate,final],'final':final,
        'initial_overflow_pages':[106,107,116,118,123,125],
        'all_complete_passes':[read_stats(p,p.stem) for p in logs]}
(R/'build/final_typesetting.json').write_text(json.dumps(result,indent=2))
print(json.dumps(final,indent=2))
