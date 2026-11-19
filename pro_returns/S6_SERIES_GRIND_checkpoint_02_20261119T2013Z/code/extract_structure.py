"""Extract the immutable source structure and perform the requested 6-to-5 move.

Every removed check-record argument is retained verbatim in the JSON record.
Mathematical body text is retained. No proof status is promoted by this move.
"""
from pathlib import Path
import csv,json,re
from collections import Counter,defaultdict
from tex_tools import PAPERS,ENVIRONMENTS,macros,argument,arguments,replace_spans,bibliography,sections

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'
PARTS=ROOT/'parts'; PARTS.mkdir(exist_ok=True)
ANALYSIS=ROOT/'analysis'

def statement_blocks(text,paper):
    pattern=re.compile(r'\\(begin|end)\{('+'|'.join(sorted(ENVIRONMENTS))+r')\}')
    stack=[];blocks=[]
    for m in pattern.finditer(text):
        if m.group(1)=='begin':stack.append(m)
        else:
            if not stack:raise ValueError((paper,'unpaired end',m.start()))
            start=stack.pop()
            assert start.group(2)==m.group(2),(paper,start.group(2),m.group(2))
            segment=text[start.start():m.end()]
            records=list(macros(segment,'StatementRecord',4))
            labels=re.findall(r'\\label\{([^}]+)\}',segment)
            title=''
            i=start.end()
            while i<len(text) and text[i].isspace():i+=1
            if text[i:i+1]=='[':
                try:title,_=argument(text,i,'[',']')
                except ValueError:pass
            main_record=records[0][2] if records else None
            identifier=main_record[0] if main_record else (labels[0] if labels else f'generated:{paper}:{len(blocks)+1}')
            blocks.append({'source_paper':paper,'start':start.start(),'end':m.end(),'environment':start.group(2),
                           'label':identifier,'labels':labels,'title':title,
                           'record':main_record,'nested':bool(stack)})
    if stack:raise ValueError((paper,'unclosed statement'))
    return sorted(blocks,key=lambda r:r['start'])

def main():
    texts={p:(SOURCE/f'S6_10_PAPERS_{p}.tex').read_text() for p in PAPERS}
    structs={p:statement_blocks(t,p) for p,t in texts.items()}
    biblio={};oldfront={};bodies={};all_records=[]
    starts={'I':r'\section{Common conventions and the marked construction}',
            'II':r'\section{Common conventions}',
            'III':r'\section{Common conventions and the transport dictionary}',
            'IV':r'\section{The page and the reference return}',
            'V':r'\section{Geometric and characteristic conventions}',
            'VI':r'\section{The degeneration and its normalization maps}'}
    for p,t in texts.items():
        begin=t.index(starts[p]);bibstart,bibend,bibhead,entries=bibliography(t)
        end=bibstart
        oldfront[p]=t[t.index(r'\begin{document}')+len(r'\begin{document}'):begin]
        bodies[p]=t[begin:end].removesuffix('\\clearpage\n')
        for key,entry in entries.items():biblio.setdefault(key,[]).append({'paper':p,'text':entry})
        for a,b,vals in macros(t,'StatementRecord',4):
            all_records.append({'source_paper':p,'label':vals[0],'status':vals[1],'check_record_tex':vals[2],'uses_tex':vals[3]})
        (PARTS/f'{p}.source_front.tex').write_text(oldfront[p])
    move_start=bodies['III'].index(r'\section{The fourfold and transverse fibre products}')
    move_end=bodies['III'].index(r'\section{Local covers, global quotients and cusp carriers}',move_start)
    move=bodies['III'][move_start:move_end]
    movedlabels=set(re.findall(r'\\label\{([^}]+)\}',move))
    bodies['III']=bodies['III'][:move_start]+bodies['III'][move_end:]
    # The renamed VI labels are the only collisions in II and VI.
    vi_renames={'sec:II:08':'sec:II:all:08','sec:II:12':'sec:II:all:12'}
    for old,new in vi_renames.items():bodies['VI']=bodies['VI'].replace('{'+old+'}','{'+new+'}')
    iiopen=bodies['II'].index(r'\section{The remaining splitting problem}')
    splitting=bodies['II'][iiopen:]
    bodies['II']=bodies['II'][:iiopen]+'\n\\clearpage\n\\part{The sign theorem for every degeneration}\n'+bodies['VI']+'\n'+splitting
    bodies['V']='\\part{Resolved and transverse fibre products}\n'+move+'\n\\clearpage\n\\part{The marked rank-six construction and its family}\n'+bodies['V']
    bodies.pop('VI')
    # Put the mathematical unestablished-results part under the common title.
    for paper,marker in [('I',r'\section{Limits and open points: the coefficient atlas}'),
                         ('II',r'\section{The remaining splitting problem}'),
                         ('III',r'\section{Limits and open points}'),
                         ('IV',r'\section{Results not yet established: the remaining attachments}')]:
        assert marker in bodies[paper]
        bodies[paper]=bodies[paper].replace(marker,'\\clearpage\n\\part{Results not yet established}\n'+marker,1)
    bodies['V']+='\n\\clearpage\n\\part{Results not yet established}\nNo mathematical open row is assigned to this paper in the received inventory.\n'
    all_labels={};collisions={}
    for p,body in bodies.items():
        replacements=[]
        for a,b,vals in macros(body,'StatementRecord',4):
            vals[2]=''
            replacements.append((a,b,'\\StatementRecord'+''.join('{'+v+'}' for v in vals)))
        body=replace_spans(body,replacements)
        (PARTS/f'{p}.body.tex').write_text(body)
        labs=re.findall(r'\\label\{([^}]+)\}',body)
        repeated={k:v for k,v in Counter(labs).items() if v>1}
        if repeated:collisions[p]=repeated
        for lab in labs:
            if lab in all_labels:collisions.setdefault('across',{})[lab]=[all_labels[lab],p]
            all_labels[lab]=p
    outputs={'source_statement_structure.json':structs,'source_statement_records.json':all_records,
             'source_bibliography_entries.json':biblio,'label_owners.json':all_labels,
             'split.json':{'moved_III_to_V_labels':sorted(movedlabels),'renamed_VI_section_labels':vi_renames,'collisions':collisions}}
    for name,data in outputs.items():(ANALYSIS/name).write_text(json.dumps(data,ensure_ascii=False,indent=2))
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open() as stream:rows=list(csv.DictReader(stream))
    for row in rows:
        label=row['label'];owner=all_labels.get(label)
        if owner:
            row['paper']=owner;row['placement_state']='body or cited-input anchor migrated'
        elif row['in_compendium_only_because']:
            row['placement_state']='documented compendium disposition retained'
        else:row['placement_state']='source label reconciliation required'
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    report={'source_statement_environments':{p:len(v) for p,v in structs.items()},
            'statement_records':len(all_records),'moved_labels':len(movedlabels),
            'new_body_labels':len(all_labels),'collisions':collisions,
            'placement_counts':dict(Counter(r['placement_state'] for r in rows))}
    (ROOT/'code/outputs/structure_extraction.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report))

if __name__=='__main__':main()
