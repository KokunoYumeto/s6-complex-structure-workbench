"""Expose only specified statements/Uses for the prereading review protocol."""
from pathlib import Path
import argparse,re,json,hashlib
P=Path(__file__).resolve().parents[2]
def arg(s,a):
    assert s[a]=='{';d=1;i=a+1
    while d:
        if s[i]=='{' and s[i-1]!='\\':d+=1
        if s[i]=='}' and s[i-1]!='\\':d-=1
        i+=1
    return s[a+1:i-1],i
def strip_records(s):
    changes=[]
    for m in re.finditer(r'\\StatementRecord\s*\{',s):
        a=m.end()-1;v=[]
        for _ in range(4):
            while s[a].isspace():a+=1
            q,a=arg(s,a);v.append(q)
        changes.append((m.start(),a,'\\Uses{'+v[3]+'}\n'))
    for a,b,t in reversed(changes):s=s[:a]+t+s[b:]
    return s
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('labels',nargs='+');ap.add_argument('--save');args=ap.parse_args()
    path=P/args.source;s=path.read_text();out=[]
    envs=r'theorem|proposition|lemma|corollary|claim|statement|definition|remark|example|problem|question|auditrecord|test|conjecture|cited|refuted|computed|openq'
    for label in args.labels:
        p=s.index('\\label{'+label+'}')
        matches=list(re.finditer(r'\\begin\{('+envs+r')\}',s[:p]))
        m=matches[-1];end=s.index('\\end{'+m[1]+'}',p)+len('\\end{'+m[1]+'}')
        out.append({'label':label,'statement':strip_records(s[m.start():end]),'source':args.source,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    if args.save:(P/args.save).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    for r in out:print(r['statement']+'\n')
