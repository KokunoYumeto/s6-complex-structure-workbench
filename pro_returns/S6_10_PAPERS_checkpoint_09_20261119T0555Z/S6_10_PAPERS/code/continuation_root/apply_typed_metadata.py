"""Apply the reviewed event-to-TeX map without awarding proof checks.

The original per-fragment record is preserved in the receipt. This changes
only the four-argument StatementRecord metadata, never a theorem or proof.
"""
from pathlib import Path
import hashlib,json,re
P=Path(__file__).resolve().parents[2]
A=P/'analysis/continuation_root'
M=json.loads((P/'analysis/continuation_ledger/printed_typed_check_prefixes.json').read_text())
by={}
for r in M:
    key=(r['paper'],r['label'])
    if key in by:assert by[key]['status']==r['status'],key
    by[key]=r
def arg(s,a):
    assert s[a]=='{'
    d=1;i=a+1
    while d:
        if s[i]=='{' and s[i-1]!='\\':d+=1
        if s[i]=='}' and s[i-1]!='\\':d-=1
        i+=1
    return s[a+1:i-1],i
marker=r'\emph{Recorded proof scope.} '
scope_markers=[marker,r'\emph{Pre-continuation recorded proof scope.} ',r'\emph{Continuation recorded proof scope.} ']
override_path=A/'printed_scope_overrides.json'
scope_overrides=json.loads(override_path.read_text()) if override_path.exists() else {}
receipt_path=A/'typed_metadata_application.json'
old=json.loads(receipt_path.read_text()) if receipt_path.exists() else {'original_records':{},'applications':[]}
counts={};unmapped=[];removed_repeated_prefixes=[]
for p in sorted((P/'papers').rglob('*.tex')):
    if p.parent==P/'papers':continue
    paper=p.relative_to(P/'papers').parts[0]
    s=p.read_text();replacements=[]
    for m in re.finditer(r'\\StatementRecord\s*\{',s):
        values=[];at=m.end()-1
        for _ in range(4):
            while s[at].isspace():at+=1
            v,at=arg(s,at);values.append(v)
        label,status,check,uses=values
        row=by.get((paper,label))
        if row is None:
            unmapped.append([str(p.relative_to(P)),label]);continue
        key=str(p.relative_to(P))+'::'+label
        old['original_records'].setdefault(key,{'status':status,'check_record':check,'uses':uses})
        scope=check
        present=next((m for m in scope_markers if m in scope),None)
        if present:scope=scope.split(present,1)[1]
        elif r'\CurrentChecker' in scope:
            # Historical-prefix clauses end at the explicit writing checker.
            # Preserve a nonhistorical prefix as part of its exact scope.
            cut=scope.index(r'\CurrentChecker')+len(r'\CurrentChecker')
            prefix=scope[:cut]
            tail=scope[cut:].lstrip(' .;')
            if prefix.startswith(('Historical records:',r'S6\_06\_BLIND:',r'S6\\_06\\_BLIND:')):
                scope=tail
            else:
                scope=scope.replace(r'\CurrentChecker',
                 'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, 18 November 2026')
        elif scope.startswith('Historical records:'):
            q=scope.find('Current-writing verification')
            if q>=0:scope=scope[q:]
        # A previous application with an empty detailed scope has no scope
        # marker. Its generated prefix must not become a new legacy scope.
        # Earlier applications that did so are repaired here; the exact text
        # remains in this receipt and every underlying event remains printed.
        if scope.startswith(('Historical events:','No earlier separately identified check is recorded.')):
            removed_repeated_prefixes.append({'path':str(p.relative_to(P)),'label':label,'repeated_prefix':scope})
            scope=''
        hist=row['historical_tex'];current=row['current_type_tex']
        declaration=row.get('writing_declaration_tex',('Also checked in this writing. ' if hist.startswith('Historical events:')
          else 'Checked only in this writing. '))
        newcheck=hist+declaration+current
        explicit=scope_overrides.get(label)
        if explicit is not None:
            scope=explicit['scope_tex']
            use_marker=row.get('continuation_scope_marker_tex',r'\emph{Continuation recorded proof scope.} ')
        else:use_marker=row.get('legacy_scope_marker_tex',r'\emph{Pre-continuation recorded proof scope.} ')
        if scope:newcheck+=use_marker+scope
        new=r'\StatementRecord'+''.join('{'+v+'}' for v in [label,row['status'],newcheck,uses])
        if new!=s[m.start():at]:replacements.append((m.start(),at,new))
    if replacements:
        before=hashlib.sha256(s.encode()).hexdigest()
        for a,b,t in reversed(replacements):s=s[:a]+t+s[b:]
        p.write_text(s)
        counts[str(p.relative_to(P))]={'records':len(replacements),'before':before,'after':hashlib.sha256(s.encode()).hexdigest()}
old['applications'].append({'files':counts,'unmapped':unmapped,'removed_repeated_prefixes':removed_repeated_prefixes,'scope':'Metadata only; no mathematical proof check.'})
receipt_path.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(counts),'records':sum(r['records'] for r in counts.values()),'unmapped':unmapped},indent=2))
