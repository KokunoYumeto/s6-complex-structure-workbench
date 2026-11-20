"""Group existing mathematical proof headings and claims into numbered levels.

The map preserves every non-list token in its original order. Its inverse
at the level of mathematical text is checked by deleting list-format
tokens from both strings. No argument or heading is invented or shortened.
"""
from pathlib import Path
import re,json,hashlib
from tex_tools import argument,replace_spans

ROOT=Path(__file__).resolve().parents[1]
FORMAL=re.compile(r'^[A-Z][A-Z0-9]{0,8}\.\d+[a-z]?\.')
TOKENS=re.compile(r'\\(?P<edge>begin|end)\{(?P<env>enumerate|itemize|description)\}(?:\[[^\n]*?\])?|\\item\b|\\(?:textbf|emph)\{')
MARK='@@S6-PROOF-SUBITEM@@'
def scantext(s):
    return re.sub(r'(?<!\\)%[^\n]*',lambda m:' '*len(m.group(0)),s)
def headings(s,allowed=()):
    clean=scantext(s);stack=[];heads=[];lists=[];items=[]
    for m in TOKENS.finditer(clean):
        if m.group('edge')=='begin':
            node={'begin':m.start(),'begin_end':m.end(),'env':m.group('env'),'depth':len(stack),'items':[],'heads':[]}
            stack.append(node)
        elif m.group('edge')=='end':
            if not stack or stack[-1]['env']!=m.group('env'):raise ValueError('unbalanced original list')
            node=stack.pop();node.update(end=m.start(),end_end=m.end());lists.append(node)
        elif m.group(0)==r'\item':
            if stack:stack[-1]['items'].append((m.start(),m.end()))
            items.append((m.start(),m.end(),len(stack)))
        else:
            title,end=argument(s,m.end()-1)
            if (FORMAL.match(title) or title in allowed) and (not stack or (len(stack)==1 and stack[-1]['env']=='enumerate')):
                start=m.start()
                prefix=re.search(r'(?:(?:\\leavevmode|\\par|\\medskip|\\bigskip|\\smallskip|\\noindent)\s*)+$',s[:start])
                if prefix:start=prefix.start()
                h={'start':start,'macro_start':m.start(),'end':end,'title':title,'depth':len(stack)}
                heads.append(h)
                if stack:stack[-1]['heads'].append(h)
    if stack:raise ValueError('unclosed original list')
    return heads,lists,items
def projection(s):
    s=re.sub(r'\\leavevmode\s*\\par','',s)
    s=re.sub(r'\\(?:begin|end)\{enumerate\}(?:\[[^\n]*?\])?','',s)
    s=re.sub(r'\\item\b','',s)
    s=re.sub(r'\\leavevmode\s*\\par','',s)
    return re.sub(r'\s+',' ',s).strip()
def enum_open(level):
    margin='0pt' if level==1 else '1.3em'
    return '\n\\begin{enumerate}[label={$\\langle'+str(level)+'\\rangle$\\arabic*.},leftmargin='+margin+',labelsep=.5em]\n'
def subclaims(s):
    if MARK not in s:return s
    before,after=s.split(MARK,1)
    claims=[x for x in after.split(MARK) if x.strip()]
    if not claims:return before
    return before+enum_open(2)+'\n'.join(r'\item '+x for x in claims)+ '\n\\end{enumerate}\n'
def relabel(s):
    depth=0;spans=[]
    for m in re.finditer(r'\\(begin|end)\{enumerate\}(?:\[[^\n]*?\])?',scantext(s)):
        if m.group(1)=='begin':
            depth+=1;old=s[m.start():m.end()]
            new=re.sub(r'label=\{\$\\langle\d+\\rangle\$\\arabic\*\.\}',lambda _:r'label={$\langle'+str(depth)+r'\rangle$\arabic*.}',old)
            new=new.replace(r'label=\arabic*.',r'label={$\langle'+str(depth)+r'\rangle$\arabic*.}')
            if new!=old:spans.append((m.start(),m.end(),new))
        else:depth-=1
    if depth:raise ValueError('new list balance')
    return replace_spans(s,spans)
def transform(content,allowed=()):
    hs,ls,items=headings(content,allowed)
    minimum=3 if allowed else 4
    if len(content)<12000 or len(hs)<minimum:return content,None
    # Literal references to unqualified list numbers need a separate semantic
    # transport; those proofs are deliberately left for explicit review.
    literals=re.findall(r'(?<!\\)\b(?:[Ii]tem|[Ss]tep)\s+(?:~\s*)?\d+\b',content)
    if literals:return content,{'state':'manual numbering-reference review','literal_references':sorted(set(literals)),'headings':len(hs)}
    flat=[l for l in ls if l['depth']==0 and l['env']=='enumerate' and len(l['heads'])>=2]
    eligible=[h for h in hs if h['depth']==0 or any(h in l['heads'] for l in flat)]
    if len(eligible)<minimum:return content,None
    spans=[]
    for l in flat:
        spans.extend([(l['begin'],l['begin_end'],''),(l['end'],l['end_end'],'')])
        spans.extend((a,b,MARK) for a,b in l['items'])
    flattened=replace_spans(content,spans)
    # An original item immediately before a claim heading supplies that
    # heading's new first-level item. It must not leave an empty subitem
    # at the end of the preceding claim group.
    preliminary,_,_=headings(flattened,allowed)
    marker_spans=[]
    for h in preliminary:
        prefix=re.search(re.escape(MARK)+r'\s*$',flattened[:h['start']])
        if prefix:marker_spans.append((prefix.start(),prefix.start()+len(MARK),''))
    flattened=replace_spans(flattened,marker_spans)
    new_h,_,_=headings(flattened,allowed)
    # Every heading whose enclosing list was flattened is now at depth zero.
    new_h=[h for h in new_h if h['depth']==0]
    prefix=flattened[:new_h[0]['start']]
    pieces=[]
    for i,h in enumerate(new_h):
        end=new_h[i+1]['start'] if i+1<len(new_h) else len(flattened)
        pieces.append(flattened[h['start']:end])
    before='';body=[]
    if MARK in prefix:
        if not scantext(prefix.replace(MARK,'')).strip():before=prefix.replace(MARK,'')
        else:
            # Initial claims precede every formal heading. Each receives its
            # own first-level item; an empty enclosing item would print its
            # number on top of the nested list's first number.
            body.extend(x for x in prefix.split(MARK) if scantext(x).strip())
    else:before=prefix
    body.extend(subclaims(x) for x in pieces)
    # A separate first line prevents the run-in proof heading from sharing
    # the hanging top-level item label. This is only a paragraph boundary.
    result='\\leavevmode\\par\n'+before+enum_open(1)+'\n'.join(r'\item '+x for x in body)+'\n\\end{enumerate}\n'
    # The proof-level paragraph boundary already precedes the outer list.
    # An inherited copy immediately after an item would print its number
    # on a content-free line. Remove only that exact format-token pair.
    result=re.sub(r'(\\item\s*)\\leavevmode\s*\\par\s*',r'\1',result)
    result=relabel(result)
    if projection(content)!=projection(result):
        import difflib
        a,b=projection(content),projection(result)
        differences=[{'kind':tag,'old':a[i:j],'new':b[k:l]} for tag,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if tag!='equal']
        raise ValueError('mathematical-token projection changed: '+json.dumps(differences[:4]))
    headings(result,allowed) # balanced list verification
    receipt={'state':'grouped','formal_headings':len(new_h),'top_level_claim_groups':len(body),'original_flat_claims':sum(len(l['items']) for l in flat),
             'heading_map':[{'original_heading':h['title'],'new_level':1,'new_number':i+1+(len(body)-len(new_h))} for i,h in enumerate(new_h)],
             'mathematical_projection_sha256':hashlib.sha256(projection(content).encode()).hexdigest(),
             'inverse':'Delete enumerate delimiters/options and item tokens; all remaining non-format tokens, including every equation, heading and reference, occur in the identical order.'}
    return result,receipt
def hierarchical_proofs(text,paper):
    spans=[];receipts=[]
    named_path=ROOT/'analysis/proof_hierarchy_named_headings.json'
    named=json.loads(named_path.read_text()) if named_path.exists() else {}
    for m in re.finditer(r'\\begin\{proof\}(?:\[[^\n]*?\])?',text):
        end=text.find(r'\end{proof}',m.end())
        if end<0:raise ValueError('unclosed proof')
        content=text[m.end():end]
        labels=re.findall(r'\\StatementRecord\{([^}]+)\}',text[:m.start()])
        label=labels[-1] if labels else ''
        # A separately placed credited appendix proof names its theorem
        # in the subsection heading. That literal target owns the proof;
        # the preceding unrelated StatementRecord is not its owner.
        sections=list(re.finditer(r'\\subsection\{',text[:m.start()]))
        if sections:
            heading,_=argument(text,sections[-1].end()-1)
            if heading.startswith('Re-derivation of Theorem'):
                targets=re.findall(r'\\(?:ref|SeriesRef)\{([^}]+)\}',heading)
                if len(targets)==1:label=targets[0]
        allowed=named.get(label,{}).get('headings',[])
        try:new,rec=transform(content,allowed)
        except ValueError as error:raise ValueError(label+': '+str(error)) from error
        if rec:
            rec['statement_label']=label
            receipts.append(rec)
        if new!=content:spans.append((m.end(),end,new))
    (ROOT/f'analysis/proof_hierarchy_{paper}.json').write_text(json.dumps(receipts,indent=2)+'\n')
    return replace_spans(text,spans),{'hierarchical_proofs':sum(r['state']=='grouped' for r in receipts),'literal_reference_review':sum(r['state']!='grouped' for r in receipts)}
