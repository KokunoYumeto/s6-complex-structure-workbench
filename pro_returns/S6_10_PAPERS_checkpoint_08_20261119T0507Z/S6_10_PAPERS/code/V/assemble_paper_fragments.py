"""Assemble full source proofs into the IV/V reader order.

This is a text/provenance operation. It does not award a proof check.
Current check records are supplied only by explicit check events.
"""
from pathlib import Path
import csv, json, re, hashlib

ROOT=Path(__file__).resolve().parents[4]
WORK=ROOT/'work/S6_10_PAPERS'
NIGHT=ROOT/'sources/newer_night/checkpoint30'
INDEX=json.loads((WORK/'analysis/inventory_source_index.json').read_text())
HISTORY=json.loads((WORK/'analysis/inventory_history_by_label.json').read_text())
NROWS={r['id']:r for r in csv.DictReader((NIGHT/'S6_06_BLIND_results.csv').open())}
# The current table registers both earlier supplemental exports and ICAP.
# Their former provenance stays in the separate exact source/event records.
assert all(sid in NROWS for sid in ['P3K.106','P3K.107','P3K.108'])
CHECKED={}
SCOPED_CHECKED={}
EXTERNAL_SCOPES={}
CONTEXTS=[]
for paper in ['IV','V']:
    eventfile=WORK/f'analysis/{paper}/current_check_events.json'
    if eventfile.exists():
        for event in json.loads(eventfile.read_text()):
            if event.get('type')=='D' and event.get('verdict')=='proved':
                for label in event['labels']: CHECKED.setdefault(label,[]).append(event['event_id'])
            elif event.get('type')=='D' and event.get('verdict')=='local construction checked; rejected compound assertion refuted':
                for label in event['labels']: SCOPED_CHECKED.setdefault(label,[]).append(event['event_id'])

# These are independently recorded current scopes. Loading them preserves the
# actual scope wording and never invents a second event or a whole-proof check.
independent_file=WORK/'analysis/IV_independent_reviews.json'
if independent_file.exists():
    for rec in json.loads(independent_file.read_text()):
        if rec['label']=='maps:src:B.6.9':continue
        scope=('the reference-family summary deduction checked' if rec['label']=='maps:src:B.6.2'
               else 'the complete receiving proof independently rederived')
        EXTERNAL_SCOPES.setdefault(rec['label'],[]).append(scope)
root_file=WORK/'analysis/IV/root_old_source_reviews.json'
if root_file.exists():
    for rec in json.loads(root_file.read_text()):
        if rec['type']=='targeted proof check':
            EXTERNAL_SCOPES.setdefault(rec['label'],[]).append('the complete displayed argument rederived; exact cited-source scopes recorded separately')
        elif rec['label']=='fam:src:E.2.3':
            EXTERNAL_SCOPES.setdefault(rec['label'],[]).append('the disposition and its exact companion uses reviewed')
root_caps=WORK/'analysis/IV/root_F36_40_reviews.json'
if root_caps.exists():
    for rec in json.loads(root_caps.read_text()):
        EXTERNAL_SCOPES.setdefault(rec['label'],[]).append('the complete source, cap, collar and integral topology argument rederived; computational executions recorded separately')
k107_review=WORK/'analysis/IV_K107/current_review.json'
if k107_review.exists():
    rec=json.loads(k107_review.read_text())
    assert rec['verdict']=='proved as stated',rec['verdict']
    EXTERNAL_SCOPES.setdefault(rec['label'],[]).append('the complete corrected main proof and nineteen supporting proofs independently rederived; exact dependency scopes and certificate executions recorded separately')
k107_delta=WORK/'analysis/IV_K107_cp30/current_review.json'
if k107_delta.exists():
    EXTERNAL_SCOPES.setdefault('night:P3K.107',[]).append('the complete checkpoint-30 delta and the twentieth supporting theta-unit proof independently rederived; the exact source and phase corrections and computational executions are recorded separately')
sign_reviews=WORK/'analysis/IV_sign_independent_reviews.json'
if sign_reviews.exists():
    for rec in json.loads(sign_reviews.read_text())['reviews']:
        EXTERNAL_SCOPES.setdefault(rec['labels'],[]).append('the complete displayed proof independently rederived in its explicit construction and reference-fan scope; the exact receiving repairs are recorded separately')
root_next=WORK/'analysis/IV/root_F47_56_reviews.json'
if root_next.exists():
    for rec in json.loads(root_next.read_text()):
        EXTERNAL_SCOPES.setdefault(rec['statement_id'],[]).append('the complete displayed argument independently rederived with its exact receiving corrections; primary-source readings and unchanged program executions recorded separately')
product_reviews=WORK/'analysis/IV_product_batch/current_reviews.json'
if product_reviews.exists():
    for rec in json.loads(product_reviews.read_text()):
        EXTERNAL_SCOPES.setdefault(rec['label'],[]).append('the complete displayed argument independently rederived with the full post-proof continuation where present; exact local dependency scopes and computations recorded separately')
root_later=WORK/'analysis/IV/root_K67_83_reviews.json'
if root_later.exists():
    for rec in json.loads(root_later.read_text()):
        EXTERNAL_SCOPES.setdefault(rec.get('statement_id',rec.get('label')),[]).append('the complete displayed argument independently rederived, including its exact integer-cover and finite-strip orientation maps; current receiving repairs and computations recorded separately')


peer_next=WORK/'analysis/IV_next_batch/current_reviews.json'
if peer_next.exists():
    for rec in json.loads(peer_next.read_text()):
        EXTERNAL_SCOPES.setdefault(rec['label'],[]).append('the complete displayed argument independently rederived with the exact group presentation and full native fan coefficients; current receiving repairs and unchanged computations recorded separately')


root_retained=WORK/'analysis/IV_root_retained/current_reviews.json'
if root_retained.exists():
    for rec in json.loads(root_retained.read_text()):
        EXTERNAL_SCOPES.setdefault(rec['statement_id'],[]).append('the complete corrected receiving argument independently rederived; retained local constructions and rejected global compound assertions remain explicitly distinguished in their scoped event')
sign_second=WORK/'analysis/IV_sign_second_reviews.json'
if sign_second.exists():
    for rec in json.loads(sign_second.read_text())['reviews']:
        EXTERNAL_SCOPES.setdefault(rec['labels'],[]).append('the complete displayed proof and its exact operative supporting scopes independently rederived; the actual current covariance repair and computational executions are recorded separately')
peer_retained=WORK/'analysis/IV_retained_batch/current_reviews.json'
if peer_retained.exists():
    for rec in json.loads(peer_retained.read_text()):
        EXTERNAL_SCOPES.setdefault(rec['labels'],[]).append('the complete corrected receiving argument independently rederived, including the isolated inner-model scope and the actual doubled ordinary seed; the rejected historical compound remains refuted, and computational replays and the typed interface repair have separate records')
sign_third=WORK/'analysis/IV_sign_third_reviews.json'
if sign_third.exists():
    for rec in json.loads(sign_third.read_text())['reviews']:
        EXTERNAL_SCOPES.setdefault(rec['labels'],[]).append('the entire corrected receiving local argument and its exact refutation scope independently rederived; the rejected historical compound remains refuted, and the two completed branch attachments retain their separately credited proofs')

def balanced(s,start):
    assert s[start]=='{'
    n=1;i=start+1
    while n:
        if s[i]=='{' and s[i-1]!='\\':n+=1
        if s[i]=='}' and s[i-1]!='\\':n-=1
        i+=1
    return s[start+1:i-1],i

def esc(s):
    return s.replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')

def remove_old_headings(s):
    s=re.sub(r'\\(?:sub)*section\*?\{[^\n]*\}', '',s)
    s=re.sub(r'\\input\{[^}]*\}', '',s)
    # A detached Uses belongs to the preceding indexed statement.
    while (m:=re.search(r'\\Uses\s*\{',s)):
        _,e=balanced(s,s.find('{',m.start()));s=s[:m.start()]+s[e:]
    return s.strip()

def source_context(item):
    text=(ROOT/item['file']).read_text()
    prior=[v['end'] for v in INDEX.values() if v.get('file')==item['file'] and v.get('found') and v.get('end',10**30)<=item['start']]
    start=max(prior,default=item['start']);raw=text[start:item['start']]
    CONTEXTS.append({'before':item['label'],'file':item['file'],'start':start,'end':item['start'],'text':raw})
    if item['label'].startswith('maps:src:F.'):
        # The other gaps in this source section are program provenance,
        # cross-reference notices, or repeated scope prose. Their full bytes
        # are recorded in the context manifest. This bridge and spectral
        # scope actually enter later arguments.
        if item['label'] not in {'maps:src:F.2.10','maps:src:F.2.16'}:return ''
    return remove_old_headings(raw)

def history(label):
    vals=[]
    for row in HISTORY.get(label,[]):
        for text in row.get('compact_named_checks','').split('; '):
            if text and text not in vals:vals.append(text)
    if label.startswith('night:') and label not in {'night:P3K.106','night:P3K.107','night:P3K.108'}:
        vals=['S6\_06\_BLIND: GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), recorded re-derivation in the checkpoint dated 18 November 2026']
    elif label in {'night:P3K.106','night:P3K.107','night:P3K.108'}:
        vals=['S6\_06\_BLIND checkpoint 30 registered export: source declaration ``Proved\'\'; the exported statement names no individual historical checker or checking date; its separate prior export and working-proof records are preserved']
    txt='; '.join(vals)
    txt=txt.replace('Claude Fable 5.2,','Claude Fable 5.2 (Anthropic),').replace('Claude Opus 5.5,','Claude Opus 5.5 (Anthropic),')
    if label in CHECKED:
        txt+=('; also checked in this writing by ' if txt else 'Checked only in this writing by ')+r'\CurrentChecker'
    if label in SCOPED_CHECKED:
        txt+=('; corrected local construction checked in this writing by ' if txt else 'Corrected local construction checked in this writing by ')+r'\CurrentChecker; the rejected compound assertion remains refuted'
    for scope in EXTERNAL_SCOPES.get(label,[]):
        txt+=('; ' if txt else '')+scope+r' in this writing by \CurrentChecker'
    if not txt:
        txt='The historical statement and its proof are retained; the statement-specific historical record is identified in the accompanying inventory'
    return re.sub(r"(?<!\\)_", r"\\_", txt)

def number_proof(s):
    pat=re.compile(r'\\begin\{proof\}(?:\[[^\]]*\])?')
    out=[];at=0
    for m in list(pat.finditer(s)):
        end=s.find(r'\end{proof}',m.end())
        if end<0:raise ValueError('Unclosed proof')
        out.append(s[at:m.end()]);body=s[m.end():end].strip()
        # Existing numbered proof structure is retained verbatim.
        if body.startswith(r'\begin{enumerate}'):
            out.append('\n'+body+'\n')
        else:
            parts=re.split(r'\n\s*\n',body)
            chunks=[];buf=[];depth=0
            for part in parts:
                begins=len(re.findall(r'\\begin\{',part));ends=len(re.findall(r'\\end\{',part))
                is_claim=bool(re.match(r'(?:[A-Z]|\\(?:noindent|textbf|paragraph|emph))',part))
                if buf and depth==0 and is_claim:
                    chunks.append('\n\n'.join(buf));buf=[]
                buf.append(part);depth+=begins-ends
            if buf:chunks.append('\n\n'.join(buf))
            out.append('\n'+r'\begin{enumerate}[label=\arabic*.]'+'\n')
            out.extend('\\item '+chunk+'\n\n' for chunk in chunks)
            out.append(r'\end{enumerate}'+'\n')
        out.append(r'\end{proof}');at=end+len(r'\end{proof}')
    out.append(s[at:]);return ''.join(out)

def flatten_night_inputs(s, seen=()):
    """Retain every companion proof before assigning its numbered steps."""
    def one(m):
        name=m.group(1)
        p=NIGHT/name
        if not p.suffix:p=p.with_suffix('.tex')
        if not p.exists():raise FileNotFoundError(p)
        if p in seen:raise ValueError(('recursive input',p))
        return '\n'+flatten_night_inputs(p.read_text(),seen+(p,))+'\n'
    return re.sub(r'\\input\{([^}]+)\}',one,s)

def source(label):
    if label in {'iv:rank_two_specialization','iv:i3_all_reduced_caps'}:
        name={'iv:rank_two_specialization':'rank_two_specialization.tex',
              'iv:i3_all_reduced_caps':'i3_all_reduced_caps.tex'}[label]
        path=WORK/'papers/IV'/name
        raw=path.read_text()
        assert raw.count(r'\StatementRecord{')==1
        return number_proof(raw),{'label':label,'origin':str(path.relative_to(ROOT)),
            'sha256':hashlib.sha256(raw.encode()).hexdigest(),
            'operation':'complete current authored proof; full file read'}
    rows=[v for v in INDEX.values() if v.get('label')==label]
    if not rows:raise KeyError(label)
    item=rows[0];text=(ROOT/item['file']).read_text()
    raw=text[item['start']:item['end']]
    if label in {'maps:src:B.6.20','maps:src:B.6.23'}:
        # These source blocks print their complete proof inside the theorem
        # as an emphatic paragraph. Separate it without altering the proof.
        marker=r'\emph{Proof.}'
        assert raw.count(marker)==1
        env=re.search(r'\\begin\{(theorem|proposition|lemma|corollary)\}',raw).group(1)
        ending='\\end{'+env+'}'
        a=raw.index(marker);b=raw.index(ending,a)
        proof=raw[a+len(marker):b].replace(r'\hfill$\square$','').strip()
        raw=raw[:a].rstrip()+'\n'+ending+'\n\\begin{proof}\n'+proof+'\n\\end{proof}\n'+raw[b+len(ending):]
    if label in {'iv:rank_two_specialization','iv:i3_all_reduced_caps'}:
        # This current supporting proof already carries its exact, scoped
        # current metadata and its two primary-source locators.
        assert raw.count(r'\StatementRecord{'+label+'}')==1
        return number_proof(raw),{'label':label,'origin':item['file'],'sha256':hashlib.sha256(raw.encode()).hexdigest()}
    um=re.search(r'\\Uses\s*\{',raw)
    uses='Definitions and the displayed constructions'
    if um:
        uses,end=balanced(raw,raw.find('{',um.start()));raw=raw[:um.start()]+raw[end:]
    lm=re.search(r'\\label\{'+re.escape(label)+r'\}',raw)
    if not lm:raise ValueError(label)
    status='proved'
    if re.search(r'\\begin\{(?:problem|question)\}',raw):status='open'
    if re.search(r'false as stated|counterexample|refuted',raw[:lm.end()+400],re.I):status='false as stated; correction proved'
    record='\n'+f'\\StatementRecord{{{label}}}{{{status}}}{{{history(label)}}}{{{uses}}}'+'\n'
    raw=raw[:lm.end()]+record+raw[lm.end():]
    context=source_context(item)
    return context+'\n\n'+number_proof(raw),{'label':label,'origin':item['file'],'sha256':hashlib.sha256(text[item['start']:item['end']].encode()).hexdigest()}

def night(id):
    if id=='P3K.108':
        block,record=source('iv:i3_all_reduced_caps')
        record.update(label='night:P3K.108',aliases=['iv:i3_all_reduced_caps'],
                      registered_source=str((NIGHT/'notes/part3_e6_selected_i3_all_caps.tex').relative_to(ROOT)),
                      included_source=str((NIGHT/'notes/part3_e6_selected_i3_all_caps_proof.tex').relative_to(ROOT)),
                      equivalence_review='IV-D-085; exact source/root/Cartier/sector/cap/characteristic maps')
        return block,record
    row=NROWS[id];file=NIGHT/row['where_proved'].split(';')[0].strip()
    if not file.exists():
        candidates=[p for p in (NIGHT/'notes').glob('*.tex') if f'\\begin{{statement}}{{{id}}}' in p.read_text()]
        if len(candidates)!=1:raise ValueError((id,candidates))
        file=candidates[0]
    text=file.read_text();m=re.search(r'\\begin\{statement\}\{'+re.escape(id)+r'\}\{([^}]*)\}',text)
    if not m:raise ValueError((id,file))
    pend=text.find(r'\end{proof}',m.end())
    nextm=re.search(r'\\begin\{statement\}',text[m.end():])
    if pend<0 or (nextm and pend>m.end()+nextm.start()):
        pend=text.find(r'\end{statement}',m.end())+len(r'\end{statement}')
    else:pend+=len(r'\end{proof}')
    if id in {'P3K.104','P3K.105'}:
        # Their signed/good-cap and odd-ideal companions are parts of the
        # same indexed theorem. Keep every complete proof, in source order.
        item=next(v for v in INDEX.values() if v.get('label')=='night:'+id)
        assert (ROOT/item['file']).resolve()==file.resolve()
        assert item['start']==m.start()
        pend=item['end']
    raw=text[m.start():pend]
    # Independent receiving repairs are applied to exact source text before
    # assigning numbered proof steps. Their files retain the original bytes.
    sign_replacements=WORK/'analysis/IV_sign_replacements.json'
    if sign_replacements.exists():
        for rep in json.loads(sign_replacements.read_text()):
            if rep['label']=='night:'+id:
                assert raw.count(rep['old'])==1,(id,rep['reason'])
                raw=raw.replace(rep['old'],rep['new'],1)
    product_replacements=WORK/'analysis/IV_product_batch/receiving_replacements.json'
    if product_replacements.exists():
        for rep in json.loads(product_replacements.read_text()):
            if rep['label']=='night:'+id:
                assert raw.count(rep['exact_old'])==1,(id,rep['reason'])
                raw=raw.replace(rep['exact_old'],rep['exact_new'],1)
    pends=[q.end() for q in re.finditer(r'\\end\{proof\}',text[:m.start()])]
    context_start=max(pends,default=0)
    context=text[context_start:m.start()]
    CONTEXTS.append({'before':'night:'+id,'file':str(file.relative_to(ROOT)),'start':context_start,'end':m.start(),'text':context})
    context=remove_old_headings(context)
    context=re.sub(r'\\paragraph\{Numerical record at the first checkpoint\.\}[\s\S]*','',context)
    context=context.replace('stmt:','night:')
    context=re.sub(r'\\HH\b',r'\\mathcal H',context)
    label='night:'+id;status={'Proved':'proved','Known':'proved; cited known result','Refuted':'false as stated; correction proved','Open':'open'}[row['status']]
    deps=[x.strip() for x in row['depends_on'].split(';') if x.strip() and x.strip()!=id]
    uses=', '.join('\\cref{night:'+x+'}' for x in deps) or 'Definitions and the displayed constructions'
    first=f'\\begin{{theorem}}\\label{{{label}}}\n\\StatementRecord{{{label}}}{{{status}}}{{{history(label)}}}{{{uses}}}'
    raw=first+raw[m.end()-m.start():]
    raw=raw.replace(r'\end{statement}',r'\end{theorem}').replace('stmt:','night:')
    # The source's Hodge symbol is transported explicitly to avoid the
    # shared quaternionic/upper-half-plane macro.
    raw=flatten_night_inputs(raw)
    raw=raw.replace('stmt:','night:')
    raw=re.sub(r'\\HH\b',r'\\mathcal H',raw)
    return context+'\n\n'+number_proof(raw),{'label':label,'origin':str(file.relative_to(ROOT)),'sha256':hashlib.sha256(text[m.start():pend].encode()).hexdigest()}

def extra_torsion():
    p=ROOT/'sources/s6_09/S6_09_PAPERS_III.tex';t=p.read_text()
    lm=t.index(r'\label{mapsaudit:order-four-torsion-transgression}')
    a=t.rfind(r'\begin{lemma}',0,lm);b=t.index(r'\end{proof}',lm)+len(r'\end{proof}')
    raw=t[a:b];u=re.search(r'\\Uses\{',raw);us,e=balanced(raw,raw.find('{',u.start()));raw=raw[:u.start()]+raw[e:]
    raw=raw.replace('Use the order-four filling and the marked matrices of MAPS Theorem \\ref{maps:src:F.2.6}.','Use the order-four filling and the marked matrices of \\cref{maps:src:F.2.5}.')
    label='mapsaudit:order-four-torsion-transgression';loc=raw.index('}',raw.index(r'\label{'))+1
    credit='GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro), S6\\_09 writing, 17 November 2026'
    if label in CHECKED:credit+=r'; also checked in this writing by \CurrentChecker'
    record=f'\n\\StatementRecord{{{label}}}{{proved}}{{{credit}}}{{\\cref{{maps:src:F.2.5}}; the displayed cellular and boundary maps}}\n'
    raw=raw[:loc]+record+raw[loc:]
    return number_proof(raw),{'label':label,'origin':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(t[a:b].encode()).hexdigest()}

MACROS=r'''% Additional notation transported from the night manuscript.
\providecommand{\LL}{\mathcal L}
\providecommand{\cT}{\mathcal T}
\providecommand{\HP}{\mathbb H\mathbb P}
\providecommand{\tr}{\operatorname{tr}}
\providecommand{\sgn}{\operatorname{sgn}}
\providecommand{\vir}{\mathrm{vir}}
'''

def main():
    for paper in ['V','IV']:
        before_context=len(CONTEXTS)
        rows=list(csv.DictReader((WORK/f'analysis/inventory_paper_{paper}_selection.tsv').open(),delimiter='\t'))
        selected={r['label']:r for r in rows if not r['in_compendium_only_because']}
        groups=[]
        if paper=='V':
            groups=[
                ('The marked cusp and preliminary lattice restrictions',['maps:src:'+x for x in ['F.1.1','F.1.4','F.2.1','F.2.2','F.2.3','F.3.1','F.3.2','F.2.4']]),
                ('The integral eight-manifold',['maps:src:F.2.5','night:P1.1','night:P1.3','mapsaudit:order-four-torsion-transgression','maps:src:F.2.6','night:P1.10','night:P1.11','night:P1.12','night:P1.19']),
                ('The genus-two pencil and the lifted period planes',['night:P1.4','night:P1.5','maps:src:F.3.5','night:P1.2','night:P1.7','maps:src:F.3.6','night:P1.8','night:P1.9','maps:src:F.3.7']),
                ('The oriented diffeomorphism type',['night:P1.13','maps:src:F.4.1']),
                ('The normalized connection and the exact parameter domain',['night:P1.15','night:P1.16','night:P1.18']),
                ('Cohomology, deformations and isomorphisms',['night:P1A.1','night:P1A.2','night:P1A.3','night:P1A.4','night:P1.17']),
                ('The boundary of the family',['night:P1A.5','night:P1A.6']),
                ('The effective integral input classification',['maps:src:F.2.'+str(i) for i in range(7,40)]+['night:P1B.1','night:P1B.2']),
                ('Source obstructions and the punctured-base period decision',['maps:src:F.3.'+str(i) for i in [3,4,8,9,10,11]])
            ]
        else:
            historical=[r['label'] for r in rows if not r['label'].startswith('night:') and r['label'] in selected and r['label'] not in {'iv:rank_two_specialization','iv:i3_all_reduced_caps'}]
            # Existing smooth/page results are kept together; the later night
            # groups separate geometric caps, free characteristic invariants,
            # and the corrected all-fan conclusions.
            proved=[r['label'] for r in rows if r['label'].startswith('night:') and r['label'] in selected and NROWS[r['source_id']]['status']=='Proved']
            geom=[l for l in proved if l.startswith('night:P3F.')]
            if 'iv:rank_two_specialization' in selected:
                geom.insert(geom.index('night:P3F.20'),'iv:rank_two_specialization')
            invariants=[l for l in proved if l.startswith('night:P3R.') or (l.startswith('night:P3K.') and int(l.split('.')[-1])<=32)]
            transport=[l for l in proved if l.startswith('night:P3K.') and 33<=int(l.split('.')[-1])<=67]
            corrected=[l for l in proved if l.startswith('night:P3K.') and 68<=int(l.split('.')[-1])<=74]
            completed=[l for l in proved if l.startswith('night:P3K.') and int(l.split('.')[-1])>=76]
            if 'night:P3K.108' in completed:
                completed.remove('night:P3K.108')
                completed.insert(completed.index('night:P3K.106')+1,'night:P3K.108')
            elif 'iv:i3_all_reduced_caps' in selected:
                completed.insert(completed.index('night:P3K.106')+1,'iv:i3_all_reduced_caps')
            false=[r['label'] for r in rows if r['label'] in selected and r['label'].startswith('night:') and NROWS[r['source_id']]['status']=='Refuted']
            opens=[r['label'] for r in rows if r['label'] in selected and r['label'].startswith('night:') and NROWS[r['source_id']]['status']=='Open']
            groups=[('The page and the reference return',historical),('The marked sources and finite caps',geom),('The free characteristic calculation',invariants),('The ordinary product and its complete transport maps',transport),('The physical transfer and the corrected scalar fan algorithm',corrected),('The completed source and two-cap return sectors',completed),('Corrections with their located counterexamples',false),('Results not yet established: the remaining attachments',opens)]
        pieces=[MACROS];manifest=[];emitted=set()
        for title,labels in groups:
            actual=[l for l in labels if (l in selected or l.startswith('mapsaudit:')) and l not in emitted]
            if not actual:continue
            pieces.append('\\section{'+title+'}\n')
            for label in actual:
                if label.startswith('night:'):block,record=night(label[6:])
                elif label.startswith('mapsaudit:'):block,record=extra_torsion()
                else:block,record=source(label)
                pieces.append(block+'\n\n');manifest.append(record);emitted.add(label)
                if label=='night:P3K.108':emitted.add('iv:i3_all_reduced_caps')
        missing=set(selected)-emitted
        if missing:raise ValueError((paper,'unplaced',sorted(missing)))
        out=WORK/f'papers/{paper}/body_source.tex';out.write_text('\n'.join(pieces))
        (WORK/f'analysis/{paper}/assembly_manifest.json').write_text(json.dumps({'paper':paper,'operation':'full-proof assembly; no check inferred','blocks':manifest,'printed_labels':sorted(emitted)},indent=2))
        (WORK/f'analysis/{paper}/interstitial_contexts.json').write_text(json.dumps(CONTEXTS[before_context:],indent=2))
        print(paper,len(emitted),'blocks',out.stat().st_size,'bytes')

if __name__=='__main__':main()
