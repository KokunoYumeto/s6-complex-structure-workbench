"""Assemble editable II/VI proof fragments from the exact preserved source.

This program does not certify a proof.  It retains source labels, moves
metadata ahead of the statement, and records the current check scope from
sign_events.tsv.  Mathematical revisions live in papers/*/revisions.
"""
from pathlib import Path
import csv, json, re
from fix_verified_legacy_locators import fix_legacy_locators

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[1]
SOURCE = BASE / 'sources/s6_09/S6_09_PAPERS_II.tex'
INDEX = json.loads((ROOT/'analysis/inventory_source_index.json').read_text())
HISTORY = json.loads((ROOT/'analysis/inventory_history_by_label.json').read_text())
ROWS = list(csv.DictReader((ROOT/'S6_10_PAPERS_inventory.csv').open()))
EVENTS = {r['label']:r for r in csv.DictReader((ROOT/'records/sign_events.tsv').open(),delimiter='\t')}
INDEPENDENT_EVENTS = ROOT/'records/II_independent_events.tsv'
if INDEPENDENT_EVENTS.exists():
    for r in csv.DictReader(INDEPENDENT_EVENTS.open(), delimiter='\t'):
        for label in r['labels'].split(';'):
            label=label.strip()
            if not label or label in EVENTS:
                continue
            scope=(r['verdict']+'. '+r['scope']+' '+r['derivation']+
                   ' Review provenance: '+r['independence'])
            if label=='cdp:st:A.3.4':
                scope+=' The receiving statement now expressly restricts the multiple-fibre and simultaneous-generic clauses to multiplicity at least two.'
            elif label=='cdp:st:C.3.1':
                scope+=' The receiving wording now explicitly states that the surface-type list concerns the very general fibre. The exact external-locus readings on C.3.7--12 are separately recorded.'
            elif label=='night:P4.39':
                scope+=' The receiving adjunction calculation now uses arithmetic genus until its equality proves that the exceptional curve is smooth elliptic.'
            elif r.get('remaining_gates'):
                scope+=' Remaining source gates: '+r['remaining_gates']
            EVENTS[label]={'label':label,'type':'D','scope':scope,
                           'verdict':r['verdict'],'who':r['who'],'date':r['date']}
SOURCE_TEXT = SOURCE.read_text()
ROOT_REVIEW_FILE = ROOT/'analysis/II_root_seven_review.json'
if ROOT_REVIEW_FILE.exists():
    for r in json.loads(ROOT_REVIEW_FILE.read_text()):
        label=r['label']
        if label not in EVENTS:
            EVENTS[label]={'label':label,'type':'D','scope':r['outcome'],
                           'verdict':'full argument review at the stated scope',
                           'who':r['checker'],'date':r['date']}
ROOT_REPLACEMENTS_FILE=ROOT/'analysis/II_root_replacements.json'
ROOT_REPLACEMENTS=(json.loads(ROOT_REPLACEMENTS_FILE.read_text())
                   if ROOT_REPLACEMENTS_FILE.exists() else {})
ALL_SOURCE_STARTS = sorted(set(e['start'] for e in INDEX.values()
                              if e.get('found') and e.get('file')=='sources/s6_09/S6_09_PAPERS_II.tex'
                              and e.get('start') is not None))

def tex_escape(s):
    table={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','_':r'\_',
           '#':r'\#','^':r'\textasciicircum{}','{':r'\{','}':r'\}',
           '$':r'\$','~':r'\textasciitilde{}'}
    table.update({'≥':r'\ensuremath{\geq}', '≤':r'\ensuremath{\leq}',
                  '≠':r'\ensuremath{\neq}', '⊂':r'\ensuremath{\subset}',
                  '⊗':r'\ensuremath{\otimes}', '⊕':r'\ensuremath{\oplus}',
                  '∈':r'\ensuremath{\in}', '→':r'\ensuremath{\to}',
                  '↦':r'\ensuremath{\mapsto}', '∩':r'\ensuremath{\cap}',
                  '∪':r'\ensuremath{\cup}', '∞':r'\ensuremath{\infty}',
                  '′':r'\ensuremath{{}^{\prime}}'})
    table.update({c:r'\textsuperscript{'+str(n)+'}'
                  for n,c in enumerate('⁰¹²³⁴⁵⁶⁷⁸⁹')})
    table.update({c:'\\ensuremath{\\'+name+'}' for c,name in {
        'α':'alpha','β':'beta','γ':'gamma','δ':'delta','ε':'epsilon',
        'ζ':'zeta','η':'eta','θ':'theta','ι':'iota','κ':'kappa',
        'λ':'lambda','μ':'mu','ν':'nu','ξ':'xi','π':'pi','ρ':'rho',
        'σ':'sigma','τ':'tau','υ':'upsilon','φ':'phi','χ':'chi',
        'ψ':'psi','ω':'omega','Γ':'Gamma','Δ':'Delta','Θ':'Theta',
        'Λ':'Lambda','Ξ':'Xi','Π':'Pi','Σ':'Sigma','Υ':'Upsilon',
        'Φ':'Phi','Ψ':'Psi','Ω':'Omega','ℓ':'ell','∧':'wedge',
        '∏':'prod','≅':'cong','∑':'sum','∂':'partial','∫':'int',
        '≃':'simeq','∼':'sim','∗':'ast','∅':'varnothing'}.items()})
    return ''.join(table.get(c,c) for c in s)

def braced(s, start):
    assert s[start]=='{'
    depth=1; i=start+1
    while depth:
        if s[i]=='{' and (i==0 or s[i-1]!='\\'): depth+=1
        if s[i]=='}' and (i==0 or s[i-1]!='\\'): depth-=1
        i+=1
    return s[start+1:i-1],i

def remove_uses(block):
    values=[]
    while True:
        m=re.search(r'\\Uses\s*\{',block)
        if not m: return block,values
        value,end=braced(block,block.index('{',m.start()))
        values.append(value); block=block[:m.start()]+block[end:]

def record(label, aliases, uses, status='proved'):
    named=[]
    for alias in aliases:
        for h in HISTORY.get(alias,[]):
            for c in h.get('named_historical_checks',[]):
                who=c['who']
                if who.startswith('Claude') and '(Anthropic)' not in who: who+=' (Anthropic)'
                t=who
                if c.get('effort'): t+=', effort '+c['effort']
                if c.get('date'): t+=', '+c['date']
                if c.get('record_kind') and c['record_kind']!='proof check':
                    t+=' ('+c['record_kind']+')'
                if t not in named: named.append(t)
    check=('Historical records: '+tex_escape('; '.join(named))+'. ') if named else ''
    event=EVENTS.get(label)
    if event and event['type']=='D':
        check+=('Also checked in this writing by ' if named else 'Checked only in this writing by ')+r'\CurrentChecker. '
        check+=tex_escape(event['scope'])
    elif event:
        check+=r'Current review by \CurrentChecker: '+tex_escape(event['scope'])
    else:
        check+=r'Current-writing re-derivation is in progress; no new proof check is created by this transcription.'
    return '\\StatementRecord{'+label+'}{'+status+'}{'+check.rstrip('. ')+'}{'+(uses or 'definitions stated here')+'}\n'

def numbered_proof(block):
    # Retain meaningful numbered source headings.  A prose proof with no
    # source division is a single numbered derivation, pending editorial
    # subdivision at its actual mathematical steps.
    def sub(m):
        heading=m.group(1) or ''
        inner=m.group(2)
        if re.search(r'\\(?:textbf|emph)\{(?:Step\s*)?\d+[.)]',inner) or re.search(r'\\begin\{enumerate\}',inner):
            return m.group(0)
        heads=list(re.finditer(r'(?m)^\\(?:textbf|emph)\{([^{}\n]+)\}',inner))
        if len(heads)>=2:
            for n,h in reversed(list(enumerate(heads,1))):
                inner=inner[:h.start()]+r'\noindent\textbf{Step '+str(n)+'. '+h.group(1)+'}'+inner[h.end():]
        else:
            chunks=re.split(r'\n\s*\n',inner.strip())
            step=0; depth=0; display=0; result=[]
            for chunk in chunks:
                if depth==0 and display==0 and (step==0 or re.match(r'(?:[A-Z]|\\(?:textbf|emph)\{)',chunk)):
                    step+=1; chunk='\\noindent\\textbf{Step '+str(step)+'.} '+chunk
                result.append(chunk)
                depth+=len(re.findall(r'\\begin\{',chunk))-len(re.findall(r'\\end\{',chunk))
                display+=chunk.count('\\[')-chunk.count('\\]')
            inner='\n'+'\n\n'.join(result)+'\n'
        return '\\begin{proof}'+heading+inner+'\\end{proof}'
    return re.sub(r'\\begin\{proof\}(\[[^\]]*\])?(.*?)\\end\{proof\}',sub,block,flags=re.S)

def prose_scope_notes(text):
    def sub(m):
        if '\\StatementRecord' in m.group(0): return m.group(0)
        title=m.group(1) or 'Scope'
        body=m.group(2)
        body=body.replace('This is a conditional extension criterion, not a general\npurity theorem for proper flat maps.',
                          'This extension criterion has precisely the displayed hypotheses. The proof does not establish purity for every proper flat map.')
        return '\\paragraph{'+title+'}\n'+body
    return re.sub(r'\\begin\{remark\}(?:\[([^\]]*)\])?(.*?)\\end\{remark\}',sub,text,flags=re.S)

def exact_receiving_locators(text):
    text=text.replace(r'Satz~6.2, pp.~336--337',r'Satz~6.2, pp.~337--338')
    # These replacements follow direct openings of the original editions and
    # the complete legacy-number source statement, not numerical guesswork.
    text=text.replace(r'4.10.7--4.10.9',r'4.10.7--4.10.8')
    text=text.replace(r'\cite[p.~958]{Kulikov1977}',
                      r'\cite[original Russian ed., pp.~1008--1009]{Kulikov1977}')
    text=text.replace(r'\cite[p.958]{Kulikov1977}',
                      r'\cite[original Russian ed., pp.~1008--1009]{Kulikov1977}')
    text=text.replace(r'\cite[\S4.10.8, pp.980--982]{Kulikov1977}',
                      r'\cite[\S4.10.8, original Russian ed., pp.~1032--1035]{Kulikov1977}')
    text=text.replace(r'Paper~I, Theorem~3.9',r'\cref{fam:src:A.5.2}')
    text=text.replace(r'Paper~I, Proposition~3.1',r'\cref{fam:src:A.1.1}')
    text=text.replace(r'\cite[Chapter~I, \S5]{Brown1982}',
                      r'\cite[Chapter~III, \S1, Exercise~2, p.~60; Chapter~IV, \S2, pp.~88--89]{Brown1982}')
    text=text.replace(r'\cite[Theorem~3.1]{Peters1990}',
                      r'\cite[Chapter~1, Theorem~3.1, p.~10]{Peters1990}')
    text=text.replace(r'Paper~I, Theorem~B.6',r'\cref{wb:thm:candidate-cusp-geometry}')
    text=text.replace(r'Paper~I, Proposition~10.5',r'\cref{inv:C3.1}')
    text=text.replace(r'Paper~I, Proposition~8.1',r'\cref{inv:A1.0,mapsI:top:thm:p0-integral-specialization}')
    text=text.replace(r'Paper~I, Theorem~C.15',r'\cref{wb:ffcert:thm:normal-trivialization}')
    # Each statement was reopened at the exact literal formulas, and its
    # complete text and SHA256 are in sign_wb_legacy_exact_mappings.json.
    for old,label in {
        'Proposition~D.2':'mapsI:top:prop:leray-e2',
        'Lemma~D.4':'mapsI:top:lem:higher-transgressions',
        'Proposition~C.1':'wb:prop:monodromy-certificate',
        'Theorem~C.3':'wb:thm:coinvariants',
        'Proposition~C.4':'wb:prop:finite-indices',
        'Proposition~B.9':'wb:prop:candidate-finite-fillings',
        'Lemma~B.10':'wb:lem:finite-filling-stalk-map',
        'Theorem~D.1':'mapsI:top:thm:p0-integral-specialization',
        'Proposition~D.6':'mapsI:top:prop:geometric-pi1',
    }.items():
        text=text.replace('Paper~I, '+old,'\\cref{'+label+'}')
    return fix_legacy_locators(text, 'build_sign_bodies.exact_receiving_locators')[0]

def format_block(start,end,entries):
    raw=SOURCE_TEXT[start:end]
    # The source-index interval for inv:E2.4 also encloses the following
    # unregistered appendix proof.  Keep its own counterexample intact.
    if '\\appendix' in raw: raw=raw.split('\\appendix',1)[0]
    aliases=[]
    for e,r in entries:
        if r['label'] not in aliases: aliases.append(r['label'])
    canonical=next((x for x in aliases if x.startswith('cdp:')),aliases[0])
    row=next(r for e,r in entries if r['label']==canonical)
    revision=ROOT/'papers'/row['paper']/'revisions'/(canonical.replace(':','_')+'.tex')
    if revision.exists(): raw=revision.read_text()
    for change in ROOT_REPLACEMENTS.get(canonical,[]):
        if change['old'] in raw:
            raw=raw.replace(change['old'],change['new'])
        elif change['new'] not in raw:
            raise ValueError('Unmatched exact receiving repair for '+canonical)
    raw,us=remove_uses(raw)
    uses=us[0] if us else row.get('uses','')
    # Remove a source's prose-only status marker; retain explicit open/false status.
    st=row['status'].lower()
    status='open' if st.startswith('open') else ('false as stated; corrected statement and counterexample below' if 'refuted' in st else 'proved')
    # These displayed propositions assert the counterexamples themselves.
    # The inventory also preserves the rejection of the earlier claims;
    # that rejection does not negate the present counterexample statement.
    if canonical in {'inv:E2.4','cdp:st:D.1.6','cdp:st:D.1.13','cdp:st:E10'}:
        status='proved counterexample; the rejected printed claim remains refuted'
        raw=raw.replace(r'\begin{proposition}[Refuted]\label{cdp:st:D.1.6}',
                        r'\begin{proposition}[A second count counterexample]\label{cdp:st:D.1.6}')
    m=re.search(r'\\label\{'+re.escape(canonical)+r'\}',raw)
    if m: raw=raw[:m.end()]+'\n'+record(canonical,aliases,uses,status)+raw[m.end():]
    return numbered_proof(raw)

def collect():
    groups={}
    for row in ROWS:
        if row['paper'] not in ('II','VI') or row['in_compendium_only_because'] or row['source_run']=='S6_06_BLIND': continue
        key=row['source_run']+':'+row['source_id']; e=INDEX.get(key)
        if not e or not e.get('found') or e['file']!='sources/s6_09/S6_09_PAPERS_II.tex': continue
        groups.setdefault((e['start'],e['end']),[]).append((e,row))
    # Reconciled allocation takes precedence over an out-of-date generated TSV.
    for entries in groups.values():
        labels=[r['label'] for e,r in entries]
        if any(x in labels for x in ['cdp:st:C2d']+['cdp:st:C.2.NC.'+str(i) for i in range(2,6)]):
            for e,r in entries: r['paper']='II'
    return groups

def main():
    groups=collect()
    sections=list(re.finditer(r'(?m)^\\section(?:\*)?\{',SOURCE_TEXT))
    source_ranges={}
    for i,m in enumerate(sections):
        z=sections[i+1].start() if i+1<len(sections) else len(SOURCE_TEXT)
        title=SOURCE_TEXT[m.start():SOURCE_TEXT.find('\n',m.start())]
        source_ranges[m.start()]=(z,title)
    outmap=[]
    for paper in ('II','VI'):
        chosen=[(key,es) for key,es in groups.items() if es[0][1]['paper']==paper]
        chosen.sort()
        out=[]; last_section=None
        if paper=='II':
            out.append(SOURCE_TEXT[SOURCE_TEXT.index('\\section{Common conventions}'):SOURCE_TEXT.index('\\section{Index, Picard')])
        else:
            out.append('\\section{The degeneration and its normalization maps}\n'
                       'Throughout this paper, $f:Y\\to B$ is a proper holomorphic map with connected fibres from a smooth compact complex threefold. '
                       'The sign theorem assumes $b_1(Y)=b_2(Y)=0$ and a smooth general fibre that is a complex two-torus. '
                       'Local comparison constructions state their own hypotheses; they are used with precisely the displayed maps. '
                       'A full fibre is its Cartier scheme. Its reduced support is denoted $S$, its normalization by $\\nu:T\\to S$, '
                       'and a resolution by $\\pi:Z\\to T$. Euler characteristic means topological Euler characteristic unless $\\chi(\\mathcal O)$ is written.\n')
        for (start,end),es in chosen:
            section=max(k for k in source_ranges if k<=start)
            if section!=last_section:
                title=source_ranges[section][1]
                known_appendix='Known source results re-derived' in title
                if known_appendix:
                    title='\\section{Uniform non-torsion on every full fibre}\\label{sec:II:uniform-nontorsion}'
                title=title.replace('Additional local proofs, analytic duality and Picard restrictions','Analytic duality and the exact Picard restriction maps')
                title=title.replace('Programs, certificates and reproducible commands','The remaining splitting problem')
                out.append('\n'+title+'\n')
                first_start=min((k for k in ALL_SOURCE_STARTS if section<=k<source_ranges[section][0]),default=start)
                prelude=SOURCE_TEXT[SOURCE_TEXT.find('\n',section)+1:first_start]
                # The old appendix's unregistered standard-pencil stability
                # reproof is a known result.  It stays in the compendium.
                if known_appendix: prelude=''
                if section>2200000: prelude=''
                out.append(prelude)
                last_section=section
            text=format_block(start,end,es)
            out.append(text+'\n\n')
            # Retain mathematical paragraphs between registered blocks.  In
            # particular the open comb row has a substantial proved-bounds
            # expansion outside its first proof environment.
            next_starts=[k for k in ALL_SOURCE_STARTS if k>=end]
            next_start=min(next_starts,default=len(SOURCE_TEXT))
            gap_end=min(next_start,source_ranges[section][0])
            gap=SOURCE_TEXT[end:gap_end]
            gap=gap.replace('\\appendix','')
            # Do not import the source's generated appendices or bibliography.
            if '\\begin{longtable}' not in gap and '\\begin{thebibliography}' not in gap:
                out.append(gap)
            outmap.append({'paper':paper,'label':es[0][1]['label'],'source_start':start,'source_end':end,'aliases':[r['label'] for e,r in es]})
        (ROOT/'papers'/paper/'body_source.tex').write_text(exact_receiving_locators(prose_scope_notes(''.join(out))))
    (ROOT/'analysis/sign_body_source_map.json').write_text(json.dumps(outmap,indent=2)+'\n')
    print(json.dumps({p:len((ROOT/'papers'/p/'body_source.tex').read_text()) for p in ('II','VI')}))

if __name__=='__main__': main()
