#!/usr/bin/env python3
"""Check the LA receiver's complete identities and mathematical syntax.

No canonical source, global record or frozen fresh file is written.
The mathematical proof and comparison are read separately by root.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_weighted_engel'
BASE='S6_SERIES_PUBLISH_III_02LA_'
receiver=(LANE/(BASE+'receiving.tex')).read_text()
old='\n'.join((LANE/(BASE+'released_'+part+'.tex')).read_text()
              for part in ('statement','proof'))
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'):
    assert Counter(re.findall(pattern,receiver))==Counter(re.findall(pattern,old))
assert len(re.findall(r'\\label\{',receiver))==14
assert len(re.findall(r'\\tag\{',receiver))==13
assert receiver.count(r'\begin{theorem}')==receiver.count(r'\end{theorem}')==1
assert receiver.count(r'\begin{proof}')==receiver.count(r'\end{proof}')==1
assert r'\StatementRecord' not in receiver
stack=[]
for kind,name in re.findall(r'\\(begin|end)\{([^}]+)\}',receiver):
    if kind=='begin':stack.append(name)
    else:assert stack and stack.pop()==name,(kind,name,stack)
assert not stack
print('PASS one theorem/proof, all14 permanent labels/targets and all13 WE equation tags preserved.')
print('PASS all TeX environments balanced and machine statement record removed.')
total=0
for suffix in ('receiving.tex','post_exposure_derivation.md'):
    raw=(LANE/(BASE+suffix)).read_bytes()
    assert raw.endswith(b'\n') and b'\r' not in raw
    assert all(x>=32 or x in (9,10) for x in raw)
    text=raw.decode()
    for a,b in ((r'\(',r'\)'),(r'\[',r'\]')):
        assert text.count(a)==text.count(b)
    displays=re.findall(r'\\\[(.*?)\\\]',text,re.S)
    equations=re.findall(r'\\begin\{equation\}(.*?)\\end\{equation\}',text,re.S)
    rest=re.sub(r'\\\[.*?\\\]','',text,flags=re.S)
    rest=re.sub(r'\\begin\{equation\}.*?\\end\{equation\}','',rest,flags=re.S)
    assert len(re.findall(r'(?<!\\)\$',rest))%2==0
    inlines=re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$',rest,re.S)
    inlines+=re.findall(r'\\\((.*?)\\\)',rest,re.S)
    fragments=displays+equations+inlines
    cleaned=[]
    for f in fragments:
        f=re.sub(r'\\tag\{[^}]*\}','',f)
        f=re.sub(r'\\label\{[^}]*\}','',f)
        f=re.sub(r'\\hypertarget\{[^}]*\}\{\}','',f)
        cleaned.append(f.strip())
    result=subprocess.run(['pandoc','--from=markdown+tex_math_dollars','--to=html','--mathml'],
        input='\n\n'.join('$$\n'+f+'\n$$' for f in cleaned),
        text=True,capture_output=True,check=False)
    assert result.returncode==0 and not result.stderr.strip(),result.stderr
    assert len(re.findall(r'<math(?:\s|>)',result.stdout))==len(fragments)
    total+=len(fragments)
    print('PASS',suffix,len(displays)+len(equations),'display and',len(inlines),
          'inline fragments; complete MathML conversion, LF and delimiters.')
assert sha256((LANE/(BASE+'fresh_derivation.md')).read_bytes()).hexdigest()==\
    '31e15560f3107ae1edaed754edcd91d70685943a6e398647552a5ba338c89105'
print('PASS',total,'mathematical fragments; frozen fresh derivation unchanged.')
print('SCOPE syntax only; no TeX build, rendered-page reading or unit closure claimed.')
print('RECEIVER SHA256',sha256((LANE/(BASE+'receiving.tex')).read_bytes()).hexdigest())
