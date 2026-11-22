#!/usr/bin/env python3
"""Extract exact statements and embargoed proofs without displaying proof text.

This is a read-only operation on canonical source, candidates, and event records.
The safe metadata index contains counts/locators/dependencies, never proof prose.
"""
from pathlib import Path
import argparse, bisect, collections, csv, datetime, hashlib, importlib.util, json, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/ii_infra'
ENVIRONMENTS = {'theorem','proposition','lemma','corollary','claim','statement',
                'definition','remark','example','problem','question','auditrecord',
                'test','conjecture','cited','refuted','computed','openq','maintheorem'}
REF = re.compile(r'\\(?:ref|eqref|autoref|cref|Cref|pageref)\*?\s*\{([^}]+)\}')
CITE = re.compile(r'\\cite\w*\*?(?:\s*\[[^\]]*\])*\s*\{([^}]+)\}')
LABEL = re.compile(r'\\label\s*\{([^}]+)\}')

def sha(data):
    return hashlib.sha256(data if isinstance(data,bytes) else data.encode()).hexdigest()

def dump(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        raise FileExistsError(path)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def relative(p): return str(p.relative_to(ROOT))

def mask_comments(s):
    chars=list(s)
    for m in re.finditer(r'(?<!\\)(?:\\\\)*(%[^\n]*)',s):
        a,b=m.span(1)
        chars[a:b]=' '*(b-a)
    return ''.join(chars)

def argument(s,i,opening='{',closing='}'):
    assert s[i]==opening
    depth=1;j=i+1
    while j<len(s):
        if s[j]=='\\': j+=2;continue
        if s[j]=='%':
            j=s.find('\n',j)
            if j<0: raise ValueError('unterminated commented argument')
            continue
        if s[j]==opening: depth+=1
        elif s[j]==closing:
            depth-=1
            if depth==0: return s[i+1:j],j+1
        j+=1
    raise ValueError('unclosed argument')

def read_args(s,i,n):
    vals=[]
    for _ in range(n):
        while s[i].isspace():i+=1
        v,i=argument(s,i);vals.append(v)
    return vals,i

def safe_statement(s):
    """Omit provenance records; retain all mathematical statement bytes."""
    cuts=[]
    for m in re.finditer(r'\\StatementRecord\s*(?=\{)',mask_comments(s)):
        _,end=read_args(s,m.end(),4);cuts.append((m.start(),end))
    for a,b in reversed(cuts):s=s[:a]+s[b:]
    assert not re.search(r'\\begin\{proof\*?\}',mask_comments(s))
    return s

def refs(s):
    return sorted({x.strip() for m in REF.finditer(mask_comments(s)) for x in m[1].split(',')})

def cites(s):
    return sorted({x.strip() for m in CITE.finditer(mask_comments(s)) for x in m[1].split(',')})

def parse_source(path,paper):
    s=path.read_text();masked=mask_comments(s)
    newlines=[-1]+[m.start() for m in re.finditer('\n',s)]
    line=lambda n:bisect.bisect_left(newlines,n)
    document=masked.index(r'\begin{document}')
    stack=[];all_env=[]
    for m in re.finditer(r'\\(begin|end)\s*\{([^}]+)\}',masked[document:]):
        a,b=m.start()+document,m.end()+document
        if m[1]=='begin':stack.append((m[2],a,b,len(stack)))
        else:
            assert stack and stack[-1][0]==m[2],('environment mismatch',paper,line(a),m[2],stack[-1][0] if stack else None)
            name,start,opening_end,depth=stack.pop()
            all_env.append({'environment':name,'start':start,'opening_end':opening_end,'end':b,'depth':depth,
                            'start_line':line(start),'end_line':line(b-1)})
    assert not stack
    all_env.sort(key=lambda x:x['start'])
    statements=[];proofs=[]
    for env in all_env:
        if env['environment']=='proof':proofs.append(env.copy())
        if env['environment'] not in ENVIRONMENTS:continue
        a,b=env['start'],env['end'];seg=s[a:b]
        row=env.copy();row['labels']=LABEL.findall(masked[a:b]);row['record_ids']=[]
        for m in re.finditer(r'\\StatementRecord\s*(?=\{)',masked[a:b]):
            vs,_=read_args(seg,m.end(),4);row['record_ids'].append(vs[0])
        row['owner']=next(iter(row['record_ids'] or row['labels']),f'unlabelled:{paper}:{len(statements)+1}')
        i=env['opening_end']
        while masked[i].isspace():i+=1
        row['title']=argument(s,i,'[',']')[0] if s[i:i+1]=='[' else ''
        row['statement_sha256']=sha(seg);row['statement_chars']=len(seg)
        row['statement_refs']=refs(seg);row['statement_cites']=cites(seg)
        row['proofs']=[];statements.append(row)
    # A proof belongs to the closest preceding statement, unless it is inside
    # a statement, in which case the innermost containing statement owns it.
    ends=[x['end'] for x in statements]
    for idx,p in enumerate(proofs):
        containers=[x for x in statements if x['start']<=p['start'] and x['end']>=p['end']]
        if containers:owner=min(containers,key=lambda x:x['end']-x['start'])
        else:
            n=bisect.bisect_right(ends,p['start'])-1
            assert n>=0,('proof has no preceding statement',paper,p['start_line'])
            owner=statements[n]
        p['owner']=owner['owner'];p['proof_id']=idx+1
        p['sha256']=sha(s[p['start']:p['end']]);p['chars']=p['end']-p['start']
        p['refs']=refs(s[p['start']:p['end']]);p['cites']=cites(s[p['start']:p['end']])
        p['enumerated_items']=len(re.findall(r'\\item\b',masked[p['start']:p['end']]))
        p['displays']=len(re.findall(r'\\\[|\\begin\{(?:equation|align|gather|multline|split)',masked[p['start']:p['end']]))
        owner['proofs'].append(p)
    headings=[]
    for m in re.finditer(r'^\\(part|section|subsection|subsubsection)\*?\s*(?=\{)',masked,re.M):
        title,end=argument(s,m.end())
        headings.append({'level':m[1],'title':title,'start':m.start(),'end_title':end,'line':line(m.start())})
    for row in statements:
        row['heading_path']={}
        for h in headings:
            if h['start']>row['start']:break
            rank=['part','section','subsection','subsubsection'].index(h['level'])
            for k in ['part','section','subsection','subsubsection'][rank:]:row['heading_path'].pop(k,None)
            row['heading_path'][h['level']]=h['title']
        row['proof_chars']=sum(p['chars'] for p in row['proofs'])
        row['proof_lines']=sum(p['end_line']-p['start_line']+1 for p in row['proofs'])
        row['proof_refs']=sorted({x for p in row['proofs'] for x in p['refs']})
        row['proof_cites']=sorted({x for p in row['proofs'] for x in p['cites']})
    labels={m[1]:{'position':m.start(),'line':line(m.start())} for m in LABEL.finditer(masked)}
    statement_labels={x:row for row in statements for x in row['labels']+row['record_ids']}
    return {'paper':paper,'path':relative(path),'sha256':sha(s),'text':s,'masked':masked,'statements':statements,
            'proofs':proofs,'headings':headings,'labels':labels,'statement_labels':statement_labels,'all_env':all_env}

def input_for_label(label,sources,target,required_owners,held_statements):
    for src in sources.values():
        if label not in src['labels'] and label not in src['statement_labels']:continue
        row=src['statement_labels'].get(label)
        if row:
            if src['paper']=='II' and row['owner'] in held_statements:
                return {'label':label,'status':'statement_argument_split_pending','paper':src['paper'],'owner':row['owner']},None
            if src['paper']=='II' and row['owner']==target['owner']:
                return {'label':label,'status':'target_statement_or_self_reference','paper':src['paper']},None
            text=safe_statement(src['text'][row['start']:row['end']])
            return {'label':label,'status':'statement_input','paper':src['paper'],'owner':row['owner'],
                    'source_path':src['path'],'source_sha256':src['sha256'],'start_line':row['start_line'],
                    'end_line':row['end_line'],'sha256':sha(text)},text
        info=src['labels'][label];pos=info['position']
        inside_proof=next((p for p in src['proofs'] if p['start']<=pos<p['end']),None)
        if inside_proof and src['paper']=='II' and inside_proof['owner'] in required_owners:
            return {'label':label,'status':'required_target_proof_internal_reference_held','paper':src['paper'],'owner':inside_proof['owner'],'line':info['line']},None
        # Extract only a labelled displayed formula, never enclosing proof prose.
        mathenv=[x for x in src['all_env'] if x['environment'] in {'equation','equation*','align','align*','gather','gather*','multline','multline*'} and x['start']<=pos<x['end']]
        spans=[(x['start'],x['end']) for x in mathenv]
        a=src['masked'].rfind(r'\[',0,pos);b=src['masked'].find(r'\]',pos)
        if a>=0 and b>=0 and src['masked'].find(r'\]',a,pos)<0:spans.append((a,b+2))
        if spans:
            a,b=min(spans,key=lambda z:z[1]-z[0]);text=src['text'][a:b]
            return {'label':label,'status':'labelled_formula_input','paper':src['paper'],'source_path':src['path'],
                    'source_sha256':src['sha256'],'line':info['line'],'sha256':sha(text),
                    'inside_other_proof':bool(inside_proof)},text
        return {'label':label,'status':'locator_requires_statement_only_resolution','paper':src['paper'],'line':info['line']},None
    return {'label':label,'status':'external_or_unresolved_label'},None

def make_packets(source,candidates):
    sources={'II':parse_source(source,'II')}
    for p in ['I','III','IV','V']:
        path=ROOT/f'S6_SERIES_PUBLISH_{p}.tex'
        if path.exists():sources[p]=parse_source(path,p)
    src=sources['II'];rows=list(csv.DictReader(candidates.open()))
    assert len(rows)==197 and len({x['current_statement_owner'] for x in rows})==197
    required_owners={x['current_statement_owner'] for x in rows}
    held_statements={x for x in required_owners if not src['statement_labels'][x]['proofs']}
    index=[];proof_dir=OUT/'embargoed_proofs_v2';proof_dir.mkdir(exist_ok=True)
    packet_dir=OUT/'statement_packets_v2';packet_dir.mkdir(exist_ok=True)
    for candidate in rows:
        label=candidate['current_statement_owner'];row=src['statement_labels'].get(label)
        assert row is not None,('candidate missing',label)
        assert not any(p['start']<row['end'] for p in row['proofs']),('proof inside target statement',label)
        tag=candidate['tag'];stem=f'S6_SERIES_PUBLISH_II_{tag}'
        target_text=(safe_statement(src['text'][row['start']:row['end']]) if row['proofs'] else
            f'% TARGET HELD: {label}; no separate proof environment.\n% A safe statement/argument split or provenance-owner disposition is required before derivation.\n')
        proof_path=proof_dir/(stem+'_target_proofs.tex')
        proof_text=('\n\n'.join(src['text'][p['start']:p['end']] for p in row['proofs']) if row['proofs'] else src['text'][row['start']:row['end']])+'\n'
        assert not proof_path.exists();proof_path.write_text(proof_text)
        entries=[];texts=[];seen=set();queue=list(sorted(set(row['statement_refs']+row['proof_refs'])))
        while queue:
            dep=queue.pop(0)
            if dep in seen:continue
            seen.add(dep);meta,segment=input_for_label(dep,sources,row,required_owners,held_statements);entries.append(meta)
            if segment:
                texts.append((dep,segment))
                # Recursively supply assumptions explicitly named by input statements.
                if meta['status']=='statement_input':queue.extend(x for x in refs(segment) if x not in seen)
        packet='% Statement and cited-input packet. Target proof is separately embargoed.\n'
        packet+=f'% Frozen II source SHA256: {src["sha256"]}\n% Target owner: {label}; tag: {tag}\n\n'
        packet+=target_text+'\n\n'
        for dep,segment in texts:
            packet+=f'% Cited input {dep}; statement or labelled formula only.\n'+segment+'\n\n'
        assert not re.search(r'\\begin\{proof\*?\}',mask_comments(packet))
        packet_path=packet_dir/(stem+'_statement_inputs.tex')
        assert not packet_path.exists();packet_path.write_text(packet)
        candidate_out={**candidate,'source_sha256':src['sha256'],'statement_owner':row['owner'],
            'statement_start_line':row['start_line'],'statement_end_line':row['end_line'],
            'statement_sha256':row['statement_sha256'],'statement_chars':row['statement_chars'],
            'title':row['title'],'environment':row['environment'],'heading_path':row['heading_path'],
            'proofs':row['proofs'],'proof_chars':row['proof_chars'],'proof_lines':row['proof_lines'],
            'proof_refs':row['proof_refs'],'proof_cites':row['proof_cites'],
            'packet_path':relative(packet_path),'packet_sha256':sha(packet),'packet_bytes':len(packet.encode()),
            'target_proof_path':relative(proof_path),'target_proof_sha256':sha(proof_text),
            'referenced_inputs':entries,'check_events_added':0,'target_proof_read':False}
        candidate_out['packet_readiness']='statement_inputs_ready' if row['proofs'] else 'held_for_safe_statement_argument_split'
        dump(packet_dir/(stem+'_packet_metadata.json'),candidate_out);index.append(candidate_out)
    structure={k:v for k,v in src.items() if k not in {'text','masked','statement_labels','all_env'}}
    structure['sources']={p:{'path':x['path'],'sha256':x['sha256']} for p,x in sources.items()}
    dump(OUT/'S6_SERIES_PUBLISH_II_structure_metadata.json',structure)
    dump(OUT/'S6_SERIES_PUBLISH_II_packet_index.json',{'source_sha256':src['sha256'],'candidates':index,
         'method':'Frozen statement and cited statements/formulas only; exact target proof archives remain embargoed until a nonempty derivation is frozen and acknowledged by the checker.','events_added':0})
    # Safe complete first-section packet: narrative before main theorems, all seven
    # exact theorem statements, and conventions. Outline arguments are withheld.
    s=src['text'];heads=src['headings']
    first=next(h['start'] for h in heads if h['level']=='section')
    outlines=next(h['start'] for h in heads if h['title']=='The proofs in outline')
    common=next(h['start'] for h in heads if h['title']=='Common conventions')
    following=next(h['start'] for h in heads if h['level']=='section' and h['start']>common)
    front=s[first:outlines]+'\n% Printed outline arguments are embargoed until derivation freezes.\n'+s[common:following]
    front=safe_statement(front)
    front_path=OUT/'S6_SERIES_PUBLISH_II_front_main_statements_conventions.tex'
    assert not front_path.exists();front_path.write_text(front)
    summary={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':src['sha256'],
             'source_lines':len(s.splitlines()),'statement_environments':len(src['statements']),'proof_environments':len(src['proofs']),
             'required_rows':len(index),'distinct_owners':len({x['statement_owner'] for x in index}),
             'target_proof_chars':sum(x['proof_chars'] for x in index),'target_proof_lines':sum(x['proof_lines'] for x in index),
             'safe_front_packet':relative(front_path),'safe_front_packet_sha256':sha(front),
             'input_status_counts':dict(collections.Counter(d['status'] for x in index for d in x['referenced_inputs'])),
             'source_proofs_displayed':False,'events_added':0,'certified':False}
    dump(OUT/'S6_SERIES_PUBLISH_II_packet_extraction_receipt.json',summary)
    print(json.dumps(summary,indent=2))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--candidates',type=Path,required=True)
    ns=ap.parse_args();make_packets(ns.source.resolve(),ns.candidates.resolve())

if __name__=='__main__':main()
