"""Recover printed Liu--Rollenske counters from the supplied exact TeX.

Their theorem environments share the section-reset equation counter.
This is a lexical audit of that explicit convention, not a TeX engine.
The source contains only equation and two two-row gathers as numbered
display environments, and has no tag/nonumber/notag/counter overrides.
The assertions below check these restrictions rather than guessing.
"""
import json
import re
from pathlib import Path

project=Path(__file__).resolve().parents[1]
background=project.parent/'background'
source=background/'papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex'
style=source.with_name('srollens-en.sty')
raw=source.read_text()
tex=re.sub(r'(?<!\\)%[^\n]*','',raw)
sty=re.sub(r'(?<!\\)%[^\n]*','',style.read_text())
assert r'\numberwithin{equation}{section}' in sty
shared=set(re.findall(r'\\newtheorem\{([^}]+)\}\[equation\]',sty))
assert not re.search(r'\\(?:tag|notag|nonumber|stepcounter|refstepcounter)\b',tex)
assert not re.search(r'\\setcounter\{(?:equation|section)\}',tex)
assert not re.search(r'\\begin\{(?:align|subequations)\}',tex)
section=counter=0
records=[]
token=re.compile(r'\\section(\*?)\{|\\begin\{([^}]+)\}|\\label\{([^}]+)\}')
skip_until=0
for match in token.finditer(tex):
    if match.start()<skip_until:
        continue
    section_star,env,label=match.groups()
    if section_star is not None:
        if not section_star:
            section+=1;counter=0
        continue
    if env in shared or env=='equation':
        counter+=1
        end=tex.find(r'\end{'+env+'}',match.end())
        labels=re.findall(r'\\label\{([^}]+)\}',tex[match.end():end])
        line=tex[:match.start()].count('\n')+1
        records.append({'line':line,'environment':env,'number':f'{section}.{counter}',
                        'labels':labels})
    elif env=='gather':
        end=tex.find(r'\end{gather}',match.end())
        body=tex[match.end():end]
        # Both supplied gathers are precisely two single-row tikzcd diagrams.
        diagrams=re.findall(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',body,re.S)
        assert len(diagrams)==2
        remainder=re.sub(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}','DIAGRAM',body,flags=re.S)
        assert len(re.findall(r'\\\\',remainder))==1
        for d in diagrams:
            counter+=1
            records.append({'line':tex[:match.start()].count('\n')+1,
                'environment':'gather-row','number':f'{section}.{counter}',
                'labels':re.findall(r'\\label\{([^}]+)\}',d)})
        skip_until=end+len(r'\end{gather}')

lookup={label:r['number'] for r in records for label in r['labels']}
wanted=['lem: product at 1','prop: monodromy and specialisation at 1',
        'prop: monodromy and specialisation at infinity','prop: global monodromy',
        'cor: local invariants common basis','prop: Leray differentials']
out={'source':str(source.relative_to(background)),'counter_rule':'theorems share equation; equation resets in section',
     'needed':{k:lookup[k] for k in wanted},'all_numbered_environments':records}
via=background/'papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex'
vtex=re.sub(r'(?<!\\)%[^\n]*','',via.read_text())
venvs=set(re.findall(r'\\newtheorem\{([^}]+)\}\[theorem\]',vtex))|{'theorem'}
vs=vc=0;vrecords=[]
for m in re.finditer(r'\\section\{|\\begin\{([^}]+)\}',vtex):
    if m.group(0).startswith(r'\section'):
        vs+=1;vc=0
    elif m.group(1) in venvs:
        vc+=1
        end=vtex.find(r'\end{'+m.group(1)+'}',m.end())
        labels=re.findall(r'\\label\{([^}]+)\}',vtex[m.end():end])
        vrecords.append({'environment':m.group(1),'number':f'{vs}.{vc}','labels':labels})
vlookup={label:r['number'] for r in vrecords for label in r['labels']}
out['viaclovsky_two_parameter']={'source':str(via.relative_to(background)),
    'needed':{k:vlookup[k] for k in ['mum','comp','mat','pi','inv','indices','d2','sphere']},
    'all_numbered_theorems':vrecords}
Path(__file__).with_suffix('.out.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
