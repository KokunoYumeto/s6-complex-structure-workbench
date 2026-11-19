"""Balanced-brace readers for the attached standalone LuaLaTeX files."""
from pathlib import Path
import re

PAPERS=['I','II','III','IV','V','VI']
ENVIRONMENTS={'theorem','proposition','lemma','corollary','claim','statement','definition','remark','example','problem','question','auditrecord','test','conjecture','cited','refuted','computed','openq'}

def argument(text, start, opening='{', closing='}', comments=True):
    assert text[start]==opening,(start,text[start:start+100])
    depth=1;i=start+1
    while i<len(text):
        if text[i]=='\\': i+=2;continue
        if comments and text[i]=='%':
            j=text.find('\n',i)
            i=len(text) if j<0 else j+1
            continue
        if text[i]==opening:depth+=1
        elif text[i]==closing:
            depth-=1
            if depth==0:return text[start+1:i],i+1
        i+=1
    raise ValueError(f'unclosed argument at {start}: {text[start:start+80]}')

def arguments(text,start,count):
    values=[]
    for _ in range(count):
        while text[start].isspace():start+=1
        value,start=argument(text,start);values.append(value)
    return values,start

def macros(text,name,count):
    pat=re.compile(r'\\'+re.escape(name)+r'\s*(?=\{)')
    for m in pat.finditer(text):
        values,end=arguments(text,m.end(),count)
        yield m.start(),end,values

def replace_spans(text,spans):
    last=len(text)+1
    for start,end,replacement in sorted(spans,reverse=True):
        assert end<=last,(start,end,last)
        text=text[:start]+replacement+text[end:];last=start
    return text

def remove_check_text(text):
    replacements=[]
    for start,end,values in macros(text,'StatementRecord',4):
        values[2]=''
        replacements.append((start,end,'\\StatementRecord'+''.join('{'+v+'}' for v in values)))
    return replace_spans(text,replacements)

def sections(text):
    result=[]
    for m in re.finditer(r'^\\section(\*?)\s*(?=\{)',text,re.M):
        title,end=argument(text,m.end())
        result.append({'start':m.start(),'title_end':end,'title':title,'starred':bool(m.group(1))})
    for n,row in enumerate(result):row['end']=result[n+1]['start'] if n+1<len(result) else len(text)
    return result

def bibliography(text):
    start=text.index('\\begin{thebibliography}')
    end=text.index('\\end{thebibliography}',start)+len('\\end{thebibliography}')
    block=text[start:end]
    matches=list(re.finditer(r'\\bibitem\s*(?:\[[\s\S]*?\])?\s*\{([^}]+)\}',block))
    entries={m.group(1):block[m.start():matches[n+1].start() if n+1<len(matches) else block.index('\\end{thebibliography}')].strip() for n,m in enumerate(matches)}
    return start,end,block[:matches[0].start()],entries

def aux_labels(text):
    result={}
    for start,end,args in macros(text,'newlabel',2):
        label,body=args
        vals=[];i=0
        try:
            while i<len(body):
                while i<len(body) and body[i].isspace():i+=1
                if i>=len(body):break
                val,i=argument(body,i);vals.append(val)
        except AssertionError: continue
        if len(vals)>=2:result[label]={'number':vals[0],'page':vals[1],'title':vals[2] if len(vals)>2 else '', 'destination':vals[3] if len(vals)>3 else ''}
    return result

def tex_escape(s):
    mapping={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(mapping.get(c,c) for c in s)
