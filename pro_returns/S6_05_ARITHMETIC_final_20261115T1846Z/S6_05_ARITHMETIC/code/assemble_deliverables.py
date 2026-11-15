#!/usr/bin/env python3
"""Assemble statement and bibliography fragments, rejecting omissions/duplicates."""
from pathlib import Path
import csv
import re
import json

ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id','statement','status','where_proved','depends_on','item_of_the_prompt','notes']
root_meta={
'C.6.1':('C.6; Lead 16(a)','normalized Neron local heights; C.4.1','All embeddings, complex multiplicities and local degrees included.'),
'C.6.2':('C.6; Lead 16(a)','division-polynomial local height identity','Exact rational coefficients of log(p), including nonidentity components.'),
'C.6.3':('C.6; Lead 16(a,b)','C.6.1; C.6.2','Eleven minimal CM models; theta and height evaluations independently agree beyond245 decimals.'),
'C.6.4':('C.6; Lead 16(a)','C.6.1; C.8.5; DeMarco-Mavraki Theorem1.1','Degree1/12 height variation and the global lower bound; height relative to(O).'),
'C.6.5':('C.6; Lead 16(a,b)','C.6.1-C.6.3; CM class-number theorem; explicit Fourier tails','All eleven heights rigorously enclosed with radius<1e-236; independent endpoint signs, exact CM identification.'),
'C.7.1':('C.7(a); Lead 16(c)','sigma and Legendre identities','Explicit extension logarithms, lattice periods and third-kind period.'),
'C.7.2':('C.7(a); Lead 16(c)','C.7.1','Algebraic compact-lift equivalence and real t>1 transformation.'),
'C.7.3':('C.7(b); Lead 16(d)','Bertolin-Philippon-Saha-Saha Construction3.4 and Lemma3.5','Includes conjugate, isogenous and independent elliptic factors and positive Rosati bracket.'),
'C.7.4':('C.7(b); Lead 16(d)','C.7.3; BPSS Conjecture1.1 or relative Conjecture4.7','Conditional theorem only; does not settle C.7(c).'),
'C.7.5':('C.7(c); Lead 16(c)','C.6 numerical data','200-digit prescribed linear tests and66 additional235-digit polynomial PSLQ calls on N and N^12 through degree12, maxcoeff1e12; no relation returned; no exhaustive exclusion or transcendence inference.'),
'C.7.6':('C.7(c); Lead 16(e)','sigma automorphy; Riemann-Roch descent','Squared CM multiplication law; unsquared quotient need not be rational; endomorphism orbit rank2.'),
'C.7.7':('C.7(c); Lead 16(e)','Waldschmidt1979; Huber-Wustholz Theorem6.1','Unconditional holomorphic statements do not remove the real Gaussian. See explicit normalization audit.'),
'C.7.8':('C.7(c); Lead 16(e)','Agboola-Howard2006 AppendixA TheoremA.1 and LemmaA.2; C.6.R1-R2','All standing assumptions retained; concrete application E361,p5; no complex-height conclusion.'),
'C.7.9':('C.7(c); Lead 16(e)','Ext1 classification of semiabelian extensions; analytic subgroup theorem','Exact obstruction to lifting CM endomorphisms to the fixed nontorsion extension; slope hypothesis is not supplied by algebraicity of N.'),
'C.8.1':('C.8; Lead 15(a)','theta product and Fourier majorants','Three analytic bounds for the elliptic norm, with explicit constants.'),
'C.8.2':('C.8; Lead 9; K3','C.3.1; explicit Fourier estimates','Larger local maximum disc; no modular grid or box enumeration.'),
'C.8.3':('C.8','C.8.2; modular-form estimates','Comparison of root and coarse discs with constants.'),
'C.8.4':('C.8; Lead 13','C.4.2; exact division-polynomial algebra','Explicit n=2,4,8 normalized ladder; algebraic computations attached.'),
'C.8.5':('C.8; R4','C.8.1-C.8.4','R4 by scalar analytic estimates and three duplication steps; independent of supplied certificates.'),
'C.8.6':('C.8; Lead 14','C.1.1; mean-zero Green function','Mahler identities, pushforward probability measure and exact centroid inequality.'),
'C.8.7':('C.8; Lead 14','complex beta integral evaluated by Gamma integrals','Square and hexagonal special values recovered with exact normalization.'),
'C.8.8':('C.8; Lead 15(a)','theta series and Poisson summation','Signed Gaussian identity; Fourier coefficients and area normalization explicit.'),
'C.8.9':('C.8; Lead 15(b,c)','C.3; local theta expansion; Betti-coordinate Jacobian','Correct form db wedge da; total mass1/12; local densities at0,1,infinity.'),
'C.8.10':('C.8; Lead 15(b)','C.8.9; DeMarco-Mavraki Theorem1.1 and Corollary1.2','Probability measure12m; n^-2 torsion divisors converge to m; bad-fibre multiplicities bounded.'),
'C.8.11':('C.8; Lead 15(c); K4; K7','theta heat equation; wp differential identities','Both derivative factorizations, including determinant, with all constants.'),
}

def declarations():
    found={}
    for path in sorted((ROOT/'sections').glob('*.tex')):
        txt=path.read_text()
        pats=[r'\\begin\{statement\}\[([ABC]\.[^\]]+)\]',
              r'\\paragraph\{Statement ([ABC]\.[^}]+)\}']
        for pat in pats:
            for m in re.finditer(pat,txt):
                title=m.group(1)
                sid=re.match(r'[ABC]\.(?:\d+|[A-Z]\d+)(?:\.(?:\d+|[A-Z]\d+))*',title).group()
                if sid in found:raise ValueError(('duplicate declaration',sid,path))
                found[sid]=(path.relative_to(ROOT).as_posix(),title)
    return found

decl=declarations()
rows={}
for path in sorted(ROOT.glob('results_*.csv')):
    with path.open(newline='') as f:
        reader=csv.DictReader(f)
        if reader.fieldnames!=FIELDS:
            if path.name=='results_Crank.csv':continue
            raise ValueError(('bad schema',path,reader.fieldnames))
        for row in reader:
            sid=row['id']
            if sid in rows:raise ValueError(('duplicate row',sid,path))
            if sid not in decl:raise ValueError(('row without statement',sid,path))
            rows[sid]=row
for sid,(path,title) in decl.items():
    if sid in rows:continue
    if sid not in root_meta:raise ValueError(('missing register metadata',sid,title))
    item,deps,note=root_meta[sid]
    status=('Known' if 'Known' in title else 'Refuted with corrected theorem' if 'Refuted' in title
            else 'Proved conditionally' if 'conditionally' in title else 'Proved')
    description=title.split(': ',1)[1] if ': ' in title else title
    rows[sid]=dict(zip(FIELDS,[sid,description,status,path+' '+sid,deps,item,note]))

def sortkey(s):
    # Follow the requested order: C.8 before C.7.
    parts=s.split('.')
    chapter=int(parts[1])
    if parts[0]=='C':chapter={7:8,8:7}.get(chapter,chapter)
    def sub(x):return (0,int(x)) if x.isdigit() else (1,x)
    return (parts[0],chapter,*[sub(x) for x in parts[2:]])
with (ROOT/'S6_05_ARITHMETIC_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
    w.writerows(rows[sid] for sid in sorted(rows,key=sortkey))

# BibTeX fragments contain complete entries. Parse balanced braces, preserving TeX.
entries={};sources={}
for path in sorted(ROOT.glob('references_*.bib')):
    txt=path.read_text();pos=0
    while True:
        m=re.search(r'@\w+\s*\{\s*([^,\s]+)\s*,',txt[pos:])
        if not m:break
        start=pos+m.start();opening=txt.index('{',start);depth=1;j=opening+1
        while depth and j<len(txt):
            if txt[j]=='{' and txt[j-1]!='\\':depth+=1
            elif txt[j]=='}' and txt[j-1]!='\\':depth-=1
            j+=1
        if depth:raise ValueError(('unbalanced bib',path))
        key=m.group(1);entry=txt[start:j]
        if key in entries:raise ValueError(('duplicate bib key',key,path,sources[key]))
        note=re.search(r'note\s*=\s*\{([^}]*)',entry,re.S)
        if not note:raise ValueError(('missing verification note',key))
        text=note.group(1)
        if not re.match(r'(?:verified|unverified)',text,re.I):
            prefix='unverified in full: ' if 'access barrier' in text.lower() else 'verified: '
            entry=entry[:note.start(1)]+prefix+entry[note.start(1):]
        entries[key]=entry;sources[key]=path.name;pos=j
(ROOT/'S6_05_ARITHMETIC_references.bib').write_text('\n\n'.join(entries.values())+'\n')
summary={'statement_count':len(rows),'bibliography_count':len(entries),
         'statement_ids':sorted(rows,key=sortkey),'bibliography_sources':sources}
(ROOT/'records/assembly_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print('STATEMENTS',len(rows),'BIBLIOGRAPHY',len(entries),'MISSING 0 DUPLICATES 0')
