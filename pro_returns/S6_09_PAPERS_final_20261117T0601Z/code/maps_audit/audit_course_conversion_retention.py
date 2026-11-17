"""Independent source/output retention checks; no mathematical verdict upgrade.

Extracts original selected ranges, accounts only for individually recorded
editorial moves, and compares every math expression with both conversion
stages. Raw mismatches are kept for manual classification. Also verifies all
249 placements and records hashes of the exact artifacts audited.
"""
from pathlib import Path
import json,re,hashlib,difflib,collections
R=Path(__file__).resolve().parents[3];D=R/'deliverables';W=D/'work/maps_audit'
M=json.loads((W/'III_course_conversion_manifest.json').read_text())
moves=json.loads((W/'III_course_conversion_moves.json').read_text())
placements=json.loads((W/'III_course_placements.json').read_text())
def sha(s):return hashlib.sha256(s.encode()).hexdigest()
pat=re.compile(r'\\begin\{equation\}.*?\\end\{equation\}|(?<!\\)\\\[.*?(?<!\\)\\\]|(?<!\\)\\\(.*?(?<!\\)\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$)[^$]*?(?<!\\)\$',re.S)
def canonical(s):
 s=re.sub(r'^\\begin\{equation\}|\\end\{equation\}$','',s)
 if s.startswith(('\\[','\\(')):s=s[2:-2]
 elif s.startswith('$$'):s=s[2:-2]
 elif s.startswith('$'):s=s[1:-1]
 s=re.sub(r'\\(?:label|tag)\{[^}]+\}','',s)
 s=re.sub(r'\\eqref\{[^}]*:eq:([^}]+)\}',lambda m:'('+m[1]+')',s)
 # The independently logged three source split environments with condition
 # columns are typeset as aligned; the mathematical tokens are identical.
 s=s.replace('\\begin{split}','\\begin{aligned}').replace('\\end{split}','\\end{aligned}')
 s=re.sub(r'(\\\\\s*)\{\}(?=\s*\[)',r'\1',s)
 return re.sub(r'\s+','',s)
def blocks(s):return [dict(raw=m[0],canonical=canonical(m[0]),start=m.start(),line=s[:m.start()].count('\n')+1) for m in pat.finditer(s)]
def prose(s):
 s=pat.sub(' ',s)
 s=re.sub(r'^#\s+.*$','',s,flags=re.M)
 s=re.sub(r'\\section\{[^\n]*','',s)
 s=s.replace('The following complete arguments are retained as re-derivations of their classical prerequisites. Source-specific calculations and their hypotheses are stated explicitly.','')
 s=re.sub(r'^#{2,4}\s+(?:\d+(?:\.\d+)*\.?\s+)?','',s,flags=re.M)
 s=re.sub(r'\{#[^}]+\}','',s)
 s=re.sub(r'\\(?:label|cref|path)\{[^}]*\}','',s)
 s=re.sub(r'\\eqref\{[^}]*:eq:([^}]+)\}',lambda m:'('+m[1]+')',s)
 s=re.sub(r'\\(?:eqref|ref)\{[^}]*\}','',s)
 s=re.sub(r'(?i)\bsection\s+\d+(?:\.\d+)*(?![\d.])','',s)
 s=re.sub(r'(?<!!)\[([^\]]*)\]\(([^)]*)\)',lambda m:m[1] if m[2].startswith('http') else '',s)
 s=re.sub(r'\\href\{[^}]*\}\{([^}]*)\}',lambda m:m[1],s)
 s=re.sub(r'<[^>]*>','',s)
 s=re.sub(r'\*\*(?:Theorem|Lemma|Corollary|Proposition)\s+[0-9.]+(.*?)\*\*',r'\1',s)
 s=re.sub(r'\\begin\{(?:theorem|lemma|corollary|proposition)\}(?:\[([^]]*)\])?',lambda m:m[1] or '',s)
 s=re.sub(r'\\(?:begin|end)\{[^}]*\}','',s)
 s=re.sub(r'\*\*Proof\.?\*\*','',s)
 s=re.sub(r'\\[A-Za-z@]+\*?','',s)
 return re.findall(r'[A-Za-z]+(?:[’\u0027][A-Za-z]+)?|\d+(?:\.\d+)*',s.lower().replace('’',"'"))
rows=[];differences=[];prose_differences=[]
for c in M:
 p=R/(c.get('retained') or c['source']);ls=p.read_text().splitlines();a,b=c['range'];raw='\n'.join(ls[a-1:b])+'\n'
 assert sha(raw)==c['source_sha256'],('Selected source range changed',c['source'])
 expected=raw;move_records=[]
 for m in moves:
  if m['source']!=c['source']:continue
  text=m['text']
  if text not in expected:continue
  if m['reason'].startswith('raw'):
   rep=m.get('mathematical_tail_retained','')
  elif m['reason'].startswith('external'):
   q=re.match(r'!\[(.*)\]\(',text)
   if q:rep=q[1]
   else:
    q=re.search(r'\balt="([^"]*)"',text);rep=q[1] if q else ''
  else:rep=''
  expected=expected.replace(text,rep,1);move_records.append(dict(reason=m['reason'],source_text_sha256=sha(text)))
 if c['category']=='duality':expected=expected.replace('The [squares chapter](DG-CHAR-05.html) proves the cochain operations, Cartan and the Thom definition of Stiefel–Whitney classes. ','')
 exp=blocks(expected);texp=D/c['converted'];mdp=texp.with_suffix('.md')
 row=dict(source=c['source'],range=c['range'],source_sha256=sha(raw),expected_math_expressions=len(exp),moves=move_records,stages={})
 for stage,pout in [('intermediate_markdown',mdp),('final_tex',texp)]:
  out=pout.read_text();got=blocks(out);seq=difflib.SequenceMatcher(None,[x['canonical'] for x in exp],[x['canonical'] for x in got],autojunk=False)
  diffs=[]
  for tag,i,j,k,l in seq.get_opcodes():
   if tag=='equal':continue
   d=dict(source=c['source'],stage=stage,opcode=tag,expected_indices=[i,j],output_indices=[k,l],
    expected=exp[i:j],actual=got[k:l]);diffs.append(d);differences.append(d)
  row['stages'][stage]=dict(path=str(pout.relative_to(R)),sha256=sha(out),math_expressions=len(got),mismatch_groups=len(diffs),identical_after_explicit_label_and_space_normalization=not diffs)
  et,ot=prose(expected),prose(out);pd=[]
  for tag,i,j,k,l in difflib.SequenceMatcher(None,et,ot,autojunk=False).get_opcodes():
   if tag in ('equal','insert'):continue
   d=dict(source=c['source'],stage=stage,opcode=tag,expected=' '.join(et[i:j]),actual=' '.join(ot[k:l]),context_before=' '.join(et[max(0,i-8):i]),context_after=' '.join(et[j:j+8]));pd.append(d);prose_differences.append(d)
  row['stages'][stage]['prose_source_token_deletion_groups']=len(pd)
 rows.append(row)
alltex='\n'.join((D/c['converted']).read_text() for c in M)
place=[]
for sid,label in placements.items():
 count=alltex.count('\\label{'+label+'}')
 place.append(dict(source_id=sid,label=label,actual_label_count=count,status='present exactly once' if count==1 else 'requires inspection'))
result=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17',
 converter_sha256=hashlib.sha256((D/'code/editorial/build_paper_iii_course.py').read_bytes()).hexdigest(),
 scope='Independent mathematical-expression retention, every selected source range and all inventory placements; manual prose/caption audit recorded separately.',chapters=rows,placements=place)
(W/'III_course_conversion_retention_raw.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(W/'III_course_conversion_math_differences.json').write_text(json.dumps(differences,ensure_ascii=False,indent=2)+'\n')
(W/'III_course_conversion_prose_differences.json').write_text(json.dumps(prose_differences,ensure_ascii=False,indent=2)+'\n')
print('Chapters',len(rows),'placements',len(place),'source math expressions',sum(r['expected_math_expressions'] for r in rows),'mismatch groups',len(differences))
for r in rows:
 if any(x['mismatch_groups'] for x in r['stages'].values()):print(Path(r['source']).name,{k:v['mismatch_groups'] for k,v in r['stages'].items()})
print('Placement exceptions',[r for r in place if r['actual_label_count']!=1])
print('Prose deletion/replacement groups',len(prose_differences))
