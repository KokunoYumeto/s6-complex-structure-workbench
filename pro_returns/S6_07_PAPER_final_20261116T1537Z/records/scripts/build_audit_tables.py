from pathlib import Path
import csv, json, re, hashlib, difflib

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables'; R=D/'records'; C=ROOT/'inputs/context'
AGENTS=['root','periods','cohomology','geometry_ends']
RUNS={'S6_02_FAMILY':'FAM','S6_02_PUSH':'PUSH','S6_01_INVARIANTS':'INV','S6_05_ARITHMETIC':'ARI','S6_03_CDP':'CDP','S6_04_MAPS_MANIFOLDS':'MAPS'}
FIELDS=['paper_label','statement_as_printed','status','source_run','source_id','source_file','wording_vs_source','found_in_AC26','found_in_E26','found_in_DGKX_v1','credited_to','checks']

def flat(x):
    if x is None:return ''
    if isinstance(x,(list,dict)):return json.dumps(x,ensure_ascii=False)
    return str(x)

def tex(s):
    s=flat(s)
    protected=[]
    def protect(m):
        val=m.group(0); tail=''
        while val and val[-1] in '.,;':tail=val[-1]+tail;val=val[:-1]
        name='ZXPROTECTED'+str(len(protected))+'XZ'
        protected.append(('\\url{' if val.startswith('http') else '\\path{')+val+'}')
        return name+tail
    s=re.sub(r'https?://[^\s<>]+',protect,s)
    s=re.sub(r'\b[A-Za-z0-9_./-]+\.(?:md|py|json|csv|tex|pdf|bib)\b',protect,s)
    escapes={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_\allowbreak{}','~':r'\textasciitilde{}','^':r'\textasciicircum{}',':':r':\allowbreak{}','/':r'/\allowbreak{}'}
    s=''.join(escapes.get(c,c) for c in s)
    s=s.replace('–','--').replace('—','---').replace('∂̄',r'\ensuremath{\bar\partial}')
    s=re.sub(r'\b[A-Za-z0-9]{20,}\b',lambda m:r'\allowbreak{}'.join(m.group(0)[j:j+10] for j in range(0,len(m.group(0)),10)),s)
    for i,val in enumerate(protected):s=s.replace('ZXPROTECTED'+str(i)+'XZ',val)
    return s

def identifier(s):
    return tex(s) if re.search(r'\s',flat(s)) else r'\nolinkurl{'+flat(s)+'}'

def md_tex(source):
    """Render the limited Markdown in the four notation ledgers as real tables."""
    output=[]; lines=source.splitlines(); i=0
    def cells(line):
        # Split pipes only outside inline code spans.
        out=[]; buf=''; code=False
        for ch in line.strip().strip('|'):
            if ch=='`':code=not code;continue
            if ch=='|' and not code:out.append(buf.strip());buf=''
            else:buf+=ch
        out.append(buf.strip());return out
    while i<len(lines):
        line=lines[i].strip()
        if not line:i+=1;continue
        if line.startswith('# '):i+=1;continue
        if line.startswith('##'):
            output.append(r'\paragraph{'+tex(line.lstrip('#').strip())+'}');i+=1;continue
        if line.startswith('|'):
            table=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=cells(lines[i]);i+=1
                if not all(re.fullmatch(r'[: -]+',v or ' ') for v in row):table.append(row)
            n=len(table[0]);widths={2:[.28,.66],3:[.24,.25,.45],4:[.17,.21,.22,.34]}.get(n,[.94/n]*n)
            output.append(r'\begingroup\small\setlength{\tabcolsep}{3pt}\begin{longtable}{@{}'+''.join('L{'+str(v)+r'\linewidth}' for v in widths)+r'@{}}\toprule')
            output.append(' & '.join(tex(c) for c in table[0])+r'\\\midrule\endhead')
            for row in table[1:]:
                if len(row)!=n:raise ValueError(('notation table column mismatch',row,n))
                output.append(' & '.join(tex(c) for c in row)+r'\\')
            output.append(r'\bottomrule\end{longtable}\endgroup');continue
        para=[line];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('#','|')):
            para.append(lines[i].strip());i+=1
        output.append(tex(' '.join(para).replace('`','')))
    return output

def load_records():
    rows=[]
    for a in AGENTS:
        for name in ['records.json','prose_records.json']:
            p=R/a/name
            if p.exists():
                for r in json.loads(p.read_text()):
                    r['_agent']=a
                    r['source_run']=RUNS.get(r.get('source_run'),r.get('source_run'))
                    additional=[x['source_file'] for x in r.get('additional_sources',[]) if x.get('source_file')]
                    source_paths=[x.strip() for x in r.get('source_file','').split(';')]
                    r['source_file']='; '.join(dict.fromkeys(source_paths+additional))
                    rows.append(r)
    return rows

def statement_blocks(s):
    envs='theorem|proposition|lemma|corollary|cited|computed|announcement|definition|remark|refuted|openq|example'
    blocks={}
    for m in re.finditer(r'\\begin\{('+envs+r')\}(?:\[[^\n]*?\])?',s):
        env=m.group(1);end=s.find('\\end{'+env+'}',m.end())
        if end<0:continue
        full=s[m.start():end+len('\\end{'+env+'}')]
        labels=re.findall(r'\\label\{([^}]+)\}',full)
        if labels:
            body=s[m.end():end]
            body=re.sub(r'^\s*\\label\{[^}]+\}\s*','',body).strip()
            blocks[labels[0]]={'env':env,'full':full,'body':body,'line':s.count('\n',0,m.start())+1}
    return blocks

rows=load_records()
kind_aliases={'Announcement':'Theorem','Known result re-derived':'New proof','Corollary':'Theorem','Counterexample target':'Counterexample','Counterexample replacement':'Counterexample'}
for r in rows:
    r['kind']=kind_aliases.get(r.get('kind'),r.get('kind'))
    if r['paper_label']=='inv:A3.1':
        r['credited_to']=flat(r.get('credited_to'))+'; INTAKE_S6_01.md Section 4 also credits the numerical Hodge table to the workbench (GPT-5.6 Sol, Codex reasoning effort ultra), using a degree count for the scalar. That Hodge proof was not supplied or freshly opened here; INV supplies the displayed determinant identity and closed scalar.'
ROOT_SUMMARIES={
 'fam:A.1.1':'Intrinsic pencil, canonical ring and base preservation.',
 'fam:B.1.1':'Elliptic-surface quotient and Mordell--Weil generator.',
 'fam:B.1.2':'The exact admissible domain for the reference quotient.',
 'fam:B.1.3':'The distinguished elliptic logarithm is a zero of the Weierstrass function.',
 'fam:B.1.4':'The transported reference and the square relation between parameters.',
 'fam:B.2.3':'Correction of the global descent claim in Engel Remark 8.1.',
 'fam:A.5.1':'The known exact identification for the standard data.',
 'fam:B.2.1':'Complete invariants for all admissible discrete data.',
 'fam:B.2.2':'Two classes at a fixed Engel parameter.',
 'fam:B.3.1':'Identification subgroup for the stated higher-multiplicity model.',
 'push:E.1.1':'The coordinate and primitive-circle dictionary.',
 'push:E.1.2':'The higher-multiplicity parameter dictionary.',
 'fam:A.1.2':'Normalized finite base changes and product covers.',
 'fam:A.2.1':'Centralizer, finite norms and the parity obstruction.',
 'fam:A.3.1':'Coherent even shifts and the proper quotient family.',
 'fam:A.4.1':'Albanese lattices and the generic two-invariant comparison.',
 'fam:A.4.2':'Nonvanishing of the Kodaira--Spencer class.',
 'pshift:thm:classification':'Exact global identification of the retained period parameter.',
 'pshift:lem:centralizer':'Complete rational centralizer and middle-family linear parts.',
 'fam:C.1.1':'Theta formula, distinguished Weierstrass zero and special values.',
 'fam:C.1.2':'Special-value evaluations and the period formula.',
 'fam:C.2.3':'The exact maximum and the radius of the parameter disc.',
 'inv:C1.1':'The complete Frölicher differential in terms of h.',
 'inv:C2.1':'Bott--Chern and Aeppli tables as functions of h.',
 'inv:C3.3':'The complete Bott--Chern algebra, for every h.',
 'inv:C3.5':'Metric obstructions that do not require h.',
 'inv:C3.7':'The fibre obstruction to SKT and astheno-Kähler metrics.'}
for r in rows:
    if r['paper_label'] in ROOT_SUMMARIES:r['summary']=ROOT_SUMMARIES[r['paper_label']]
allfrags='\n'.join((R/a/'sections.tex').read_text() for a in AGENTS)
allfrags+='\n'+'\n'.join(p.read_text() for a in AGENTS for p in (R/a).glob('appendix_*.tex'))
# Match the standalone manuscript's typography and macro aliases exactly.
allfrags=allfrags.replace('{DGKX26v1}','{DGKXv1}').replace('{DGKX26v2}','{DGKXv2}').replace('{ViaclovskyLog26}','{VL26}')
allfrags=re.sub(r'\\dh\b',r'\\dhat',allfrags)
allfrags=allfrags.replace('–','--').replace('—','---').replace('’',"'").replace('‘','`').replace('“','``').replace('”',"''")
blocks=statement_blocks(allfrags)
comparisons=[]
for r in rows:
    lab=r['paper_label'];b=blocks.get(lab)
    if b:
        recorded=flat(r.get('statement_as_printed'))
        recorded=recorded.replace('{DGKX26v1}','{DGKXv1}').replace('{DGKX26v2}','{DGKXv2}').replace('{ViaclovskyLog26}','{VL26}')
        recorded=re.sub(r'\\dh\b',r'\\dhat',recorded)
        recorded=recorded.replace('–','--').replace('—','---').replace('’',"'").replace('‘','`').replace('“','``').replace('”',"''")
        printed=b['body']
        if recorded.startswith('\\begin{'):
            recblock=statement_blocks(recorded).get(lab)
            if recblock:recorded=recblock['body']
        comparisons.append({'paper_label':lab,'fragment_line':b['line'],'record_matches_final_body':recorded.strip()==printed.strip(),'record_to_fragment_diff':list(difflib.unified_diff(recorded.splitlines(),printed.splitlines(),lineterm='')),'source_to_print_diff':list(difflib.unified_diff(flat(r.get('source_statement')).splitlines(),printed.splitlines(),fromfile='source statement',tofile='printed statement',lineterm=''))})
        r['statement_as_printed']=printed
    else:
        comparisons.append({'paper_label':lab,'prose_row':True,'record_matches_final_body':None})
    r['statement_sha256']=hashlib.sha256(r['statement_as_printed'].encode()).hexdigest()
    r['checks']=flat(r.get('checks'))+'; Assembly comparison: records/statement_comparisons.json; final printed-body SHA-256 '+r['statement_sha256']

labels=[r['paper_label'] for r in rows]
audit={'number_of_rows':len(rows),'number_of_formal_statements':len(blocks),'missing_source_rows':sorted(set(blocks)-set(labels)),'duplicate_source_rows':sorted({x for x in labels if labels.count(x)>1}),'empty_required_fields':[{r['paper_label']:k} for r in rows for k in FIELDS if not flat(r.get(k))],'metadata_fragment_mismatches':[x['paper_label'] for x in comparisons if x.get('record_matches_final_body') is False]}
(R/'source_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
(R/'statement_comparisons.json').write_text(json.dumps(comparisons,ensure_ascii=False,indent=2))
(R/'all_records.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
with (D/'S6_07_PAPER_source_table.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader()
    for r in rows:w.writerow({k:flat(r.get(k)) for k in FIELDS})

# The exact statements are printed once in the main text and the appendices.
# This readable concordance points to them; the companion CSV keeps their full TeX.
out=[r'\subsection{Per-result source and status concordance}\label{app:source-status}',
r'The complete statement text is in the referenced result and, verbatim as TeX, in \path{S6_07_PAPER_source_table.csv}. The table below gives one row per printed statement or explicitly recorded setup. T, K and A are the binding statuses; \emph{text} denotes definitions or setup. The credit checks and precise wording changes are retained per row in that CSV, with the full source-to-print diffs in the accompanying records. Source filenames are relative to the supplied bundles.']
out += [r'\begingroup\small\setlength{\tabcolsep}{3pt}',r'\begin{longtable}{@{}L{.18\linewidth}L{.48\linewidth}L{.29\linewidth}@{}}',r'\toprule Result / status & Statement locator and source & Kind / proof\\\midrule\endhead']
for r in rows:
    lab=r['paper_label']; summary=r.get('summary') or r.get('one_line') or ''
    # Use only a short source title in this locator table, never a strengthened summary.
    summary=re.sub(r'^[A-Z]\.?\d+(?:\.\d+)*[; ]*\(?Proved\)?[;:, ]*','',summary)
    summary=summary.replace('Proved: ','').replace('Proved, with interval certificate','Interval certificate').replace('Refuted sign and normalization, with the corrected current identity proved','Corrected sign and measure normalization').replace('R4 by','Maximum by')
    if len(summary)>210:summary=summary[:207]+'...'
    ref=('Statement~\\ref{'+lab+'}') if lab in blocks else identifier(lab)
    source_paths=r'\newline '.join(r'\path{'+x.strip()+'}' for x in flat(r.get('source_file')).split(';'))
    out.append(tex(r.get('source_run',''))+' '+identifier(r.get('source_id',''))+'\\newline '+tex(r.get('status',''))+' & '+ref+'. '+tex(summary)+'\\newline '+source_paths+' & '+tex(r.get('kind',''))+'\\newline '+tex(r.get('proof_location',''))+r'\\')
out += [r'\bottomrule\end{longtable}\endgroup']

credit_rows=[
('1','AC26 Main Theorem; Theorem 3.4; Remark 3.12; DGKXv1 Theorems 7.1--7.2; E26 Section 2.','Construction, canonical bundle, standard intrinsic pencil, factorization and elliptic-logarithm interpretation are known. FAM gives the explicit transported-reference dictionary and corrects E26 Remark 8.1. Its wp-zero geometric reading is credited to AC26.'),
('2','DGKXv1 Theorem 1.4 and bare-period corollary; AC26 Remark 6.4; Viaclovsky Proposition 4.7.','The standard-data 2Z statement is known. The all-discrete-data invariants and two classes at fixed u are the selected FAM results. The 2klZ theorem retains its stated model; the Viaclovsky coordinate dictionary is A.'),
('3','AC26 Theorem 3.4 and Remark 3.12; Eichler--Zagier p.399; Duke--Imamoglu Section 2; Shioda Theorem 8.6.','Finite period values and the elliptic-logarithm interpretation have their source credits. The normalized beta formula, exact nomes, division evaluations and specified integrals are the selected run results. The general division identity is classical local-height quasi-quadraticity, re-derived here; it is not credited as a new general theorem.'),
('4','DGKXv1 Corollary p2:cor:bare-period; E26 Proposition 2.4.','The abstract punctured disc and sufficiently small geometric parameter are known. The maximum, unique maximizer, exact radius 216 and normalized unit-disc nome are the selected new evaluations. Certificate scope and missing files are explicit.'),
('5','AC26 Proposition 9.13; Theorem 9.1; Remarks 1.3 and 9.21; DGKXv1 Proposition 6.10; Ugarte Theorem 3.2; McHugh Section 7.1; Stelzig Theorem A.','The structure-sheaf direct images, h0q, hp0 and h11=h12+1 are known. The selected cotangent calculation determines h12=1. INTAKE_S6_01 Section 4 also credits the numerical Hodge table to the workbench (GPT-5.6 Sol, Codex reasoning effort ultra), with a degree-count argument; INV supplies the closed scalar and determinant identity. Conditional background formulas for a hypothetical complex S6 are credited where applied; exact Frolicher ranks, evaluated Bott--Chern/Aeppli tables and specified cover calculations have their run proofs. Product and metric statements remain A.'),
('6','DGKXv1 Theorem 1.3 and tangent-cohomology theorem; standard proper base change and relative duality.','The tuple (1,1,1,0), Kuranishi line and miniversality are known and re-derived. Integral twists are CDP C5b and INV D4.1. Higher multiplicities carry the two-runs, no-second-reader qualifier. The nearby a=1 corollary is the specified consequence.'),
('7','AC26 Proposition 9.23 and Corollary 9.24; DGKXv1 full-automorphisms theorem.','Aut0 and its action are AC26; the full group is DGKXv1. The conjugate-parameter and real-nome criterion are the selected T results. Fixed loci and classes of real involutions are A.'),
('8','AC26 period monodromies; E26 Remark 8.4.','The construction matrices and Klingler question have source credit. The explicit index-12 subgroup, maximal proper-action open set and period embedding are the selected FAM results.'),
('9','AC26 Lemmas 9.2--9.4, Proposition 9.5, Corollary 9.8, Proposition 4.6; E26 Lemma 2.1; Shioda and Appell--Humbert theory.','The NS equation, independence, generic indefinite class and generic NS rank are already in AC26; the normalization and conductor geometry of W are also there. These results are credited as known content despite the binding T/proof placement. The selected torsion-point calculations, all-curve/surface statements and special-parameter examples retain their stated scope.'),
('10','E26 Conjecture 8.2; Buchdahl Theorem 11; Grauert base-change and analytic flatness results; analytic specialization sources.','The outer-boundary obstruction and virtual Euler count refute the stated target in their exact source scope. The candidate centre has virtual Euler number zero whereas the smooth sphere fibre has Euler number two. Corrected fillings are A.'),
('11','The supplied PUSH and MAPS returns, with the bounded intake checks.','Zero-end non-filling, trivial Theta7 monodromy and unions of components are A. Two runs use different methods for the monodromy value. The interpretation J=epsilon P.O is an unverified reader remark.'),
('12','INTAKE_FINAL Section 6; RESPONSE_INTAKE; RESPONSE_EXPERT.','The four open question groups are retained as questions, with the MAPS B.6.24 announced scope distinguished from the other families.')]
out += [r'\subsection{Known and new, by section}\label{app:credits}',r'This table incorporates the source openings of AC26 that the supplied expert table had not performed. \emph{Selected run results} identifies the supplied proof source, not an assertion of absence from all literature.',r'\begingroup\small\setlength{\tabcolsep}{3pt}\begin{longtable}{@{}L{.05\linewidth}L{.34\linewidth}L{.56\linewidth}@{}}',r'\toprule § & Known source and locator & Scope and credit\\\midrule\endhead']
for a,b,c in credit_rows:out.append(tex(a)+' & '+tex(b)+' & '+tex(c)+r'\\')
out += [r'\bottomrule\end{longtable}\endgroup']

out += [r'\subsection{Dependency concordance}\label{app:dependencies}',r'The fixed section order retains the source arguments. A pointer to Appendix B is a dependency on its printed re-derivation. Forward references within the selected source order are retained and disclosed in Limits and open points. Every A row points to its repository proof rather than contributing a printed proof.',r'\begingroup\small\begin{longtable}{@{}L{.21\linewidth}L{.73\linewidth}@{}}',r'\toprule Result & Uses / dependence\\\midrule\endhead']
for r in rows:
    lab=r['paper_label']; ref=('\\ref{'+lab+'}') if lab in blocks else identifier(lab)
    uses=flat(r.get('uses') or 'Definitions and the source setup.')
    # Uses fields are editorial TeX, retained as supplied for readable references.
    uses=uses.replace('{DGKX26v1}','{DGKXv1}').replace('{ViaclovskyLog26}','{VL26}')
    out.append(tex(r['source_run'])+' '+identifier(r['source_id'])+' ('+ref+') & '+uses+r'\\')
out += [r'\bottomrule\end{longtable}\endgroup']

out += [r'\subsection{Notation concordance}\label{app:notation}',r'The standing conventions are those of FAM. The companion notation sheet gives every retained label and the scoped symbol substitutions; the mathematical signs and normalizations are unchanged unless the source explicitly compares two conventions.']
for a in AGENTS:
    p=R/a/'notation.md'
    if p.exists():
        out.append(r'\paragraph{'+tex(a.replace('_',' '))+'}')
        out.extend(md_tex(p.read_text()))

# Citation checks from this assembly, all sourced to actual opened-reference ledgers.
citations=[]
for a in AGENTS:
    p=R/a/'citation_checks.json'
    if p.exists():
        for x in json.loads(p.read_text()):
            x['key']=x.get('key') or x.get('citation_key','')
            x['matched']=x.get('matched') or x.get('match','')
            x['type']=x.get('type') or x.get('check_type','S')
            if not x.get('source') and x.get('local_source'):x['source']=x['local_source']
            if x.get('effort') and x['effort'] not in x.get('by',''):
                x['by']=x.get('by','')+', '+x['effort']
            x['_ledger']='records/'+a+'/citation_checks.json'
            citations.append(x)
(R/'all_citation_checks.json').write_text(json.dumps(citations,ensure_ascii=False,indent=2))

hist=[]
def check(by,date,typ,scope,independence,verdict,findings,report):
    hist.append(dict(by=by,date=date,type=typ,scope=scope,independence=independence,verdict=verdict,findings=findings,report=report))
fh='Claude Fable 5.2, effort high';fm='Claude Fable 5.2, effort max';om='Claude Opus 5.5, effort max'
review=(C/'status/REVIEW_S6_02_FAMILY.md').read_text()
selected={r['source_id'] for r in rows if r.get('source_run')=='FAM'}
for line in review.splitlines():
    if not re.match(r'\| [A-F]\.\d+\.\d+ \|',line):continue
    cols=[x.strip() for x in line.strip('|').split('|')]
    sid,returned,verdict,findings=cols[:4]
    if sid not in selected:continue
    if sid=='A.5.1':findings='Assembly checked; the review identifies Theorem 1.4 of DGKXv1 and notes its absence in v2. No date comparison is carried into the paper.'
    findings=findings.replace('first run','FAM run').replace('earlier','supplied')
    typ='F'
    if any(k in findings.lower() for k in ['by hand','rederived','re-derived','redone','recomputed']):typ+=',D'
    if any(k in findings.lower() for k in ['program','numerical','digits','rerun','re-run','brute force']):typ+=',C'
    check(fh,'2026-11-12',typ,'FAM '+sid,'Given the return, bibliography and programs; one AI reader.',verdict,findings,'status/REVIEW_S6_02_FAMILY.md, Section 3, '+sid)
for prog in ['ab_exact','ab_geometry','ab_deformation','cd_bounds','cd_exact','cd_local_bound','cd_multiples_initial','cd_periods','cd_special_intervals','cd_torsion_independent','f_exact']:
    check(fh,'2026-11-12','C',prog,'Rerun of the shipped program in a scratch copy.','identical','Python 3.13.9; sympy 1.13.1; mpmath 1.3.0. The review identifies the complete outputs as identical.','status/REVIEW_S6_02_FAMILY.md, Section 2')
for scope,verdict,findings in [
('cd_numerics','identical apart from last platform digits','Two double-precision grid cross-checks differed only in their last digits.'),
('f_interval_verify','identical','19,911 leaves; exact area 23/40; 19,701 norm boxes; 36 local boxes; 174 outside the unit circle.'),
('all 19,701 norm boxes','all recertified','Own recertify_all.py runner called the supplied certify routine; identical upper-bound strings; 73 seconds, 12 processes. Same mpmath interval library, not a new implementation.'),
('independent exact lattice calculations','checked','v1_exact.py used the AC26 matrices for FAM A.2, A.3, B.2, B.4, F.1 and F.2.'),
('independent period numerics','checked as numerical evidence','v2_numeric.py: 6,651 grid points, the modular arc and circles around i; independent mpmath theta evaluation.'),
('independent elliptic arithmetic','checked','v3_ec.py recomputed the D.1 arithmetic and C.2.2 constants.'),
('independent special values','checked as numerical evidence','v4_closed_forms.py evaluated the closed forms listed in Section 4.9; proofs were not supplied by that numerical check.')]:
    check(fh,'2026-11-12','C',scope,'Methods exactly as recorded by the review.',verdict,findings,'status/REVIEW_S6_02_FAMILY.md, Section 2')
check(om,'2026-11-12','S','DGKXv1 three theorem statements and v2 contents','Both supplied TeX sources opened by the main session.','known labels confirmed','The Kuranishi, exact-period and tangent-cohomology statements were matched in v1; their absence in v2 was checked.','status/REVIEW_S6_02_FAMILY.md, added main-session note')
check(fm,'2026-11-16','R,S','DGKXv1 and v2 scope','Expert had the TeX and the status discussion.','matched statements; proofs not read','Abstract and introduction; 17 statements in Sections 6--7; three Appendix C propositions; Appendix D opening; full term counts. For v2: abstract, introduction statements and section list.','status/RESPONSE_EXPERT.md, Section 1')
check(fm,'2026-11-13, recorded 2026-11-16','D,C','ARI C.8.6 and C.8.7','Expert derivations reported in the supplied response.','derived and numerically tested','Mahler-measure identity and two beta integrals derived by hand and tested to seven digits. This is not a claim of a fresh line-by-line read of the source proof.','status/RESPONSE_EXPERT.md, Section 4')
check(fh,'2026-11-15','D','ARI C.4.2','Bounded arithmetic intake and its recorded hand checks.','checks agree','Hand checks at t=1, 32/5 and 0; no code rerun.','status/INTAKE_S6_05_FINAL.md, Section 1; INTAKE_FINAL.md, Section 4')
check(fh,'2026-11-15','F,D','ARI C.8.5 displayed inequalities','Given the source proof and intake notes.','displayed inequalities agree','Every displayed inequality and the size of the three uniform bounds were checked. C.8.1--C.8.3 were not read line by line. Code and PDF were not read.','status/INTAKE_S6_05_FINAL.md, Section 1')
check('GPT-6 Astra, ChatGPT Pro mode','PUSH producing run','C','PUSH E.4 Arb certification','Separate interval library; same rational box endpoints.','all boxes certified as reported','19,701 boxes; largest upper enclosure below 1.999877571767410525. The intake reports this result and did not rerun the code. Detailed precision is in the source certificate block.','status/INTAKE_FINAL.md, Section 1, item 4; PUSH E.4')
for sid,scope,findings in [
('A1.3','direct images','Proof read; A1.1--A1.2, which supply local freeness and direct images, were not read.'),
('A2.1','period determinant identity','Statement and full proof read.'),
('A2.2','the fourth-root scalar','Statement and full proof read; separate scalar computation is listed below.'),
('A2.4','nonzero Kodaira--Spencer scalar','Statement and full proof read.'),
('A3.1','Hodge table','Table recomputed from the six direct-image sheaves; Serre duality, Euler characteristic and the AC26 relation checked.'),
('C1.1','Frolicher sequence','Every arrow followed; no higher differential has both nonzero source and target; middle rows exact.'),
('C2.1','Bott--Chern and Aeppli numbers','First half of proof read; numbers recounted from the double-complex arrows. Remaining proof was not fully read.'),
('C3.3','square-zero product','Proof read and Leibniz argument followed; it uses C3.1, which was not read. Binding status remains A.'),
('B2.1','higher-multiplicity canonical divisor','Proof read; the two orders and the fibre degree checked. Higher-multiplicity Hodge inputs were not read.'),
('B3.2','degree-n covers','Proof read; the cusp residue mechanism and Betti agreement identified. B3.1 was not read.'),
('B3.3','cover cohomology','Statement and first half of proof read; not a complete proof check.')]:
    check(fh,'2026-11-16','F'+(',D' if sid in ['A3.1','C2.1','B2.1'] else ''),'INV '+sid+'; '+scope,'Bounded intake; precise read limits retained.','no error found in the portion read',findings,'status/INTAKE_S6_01.md, opening and Section 2')
check(fh,'2026-11-16','C','INV A2.2 scalar','Independent numerical route using the local period expansion and j second derivative.','40 digits agree','s601_scalar_check.py reproduced 0.2366093140807852246877051134504496062943 and j second derivative -162 Gamma(1/4)^8/pi^4.','status/INTAKE_S6_01.md, Section 2')
for sid,findings in [('A.3.1','Full proof read; virtual Euler count redone as 24-(12+12)+0=0.'),('A.3.2','Full proof read; the specified candidate cannot smooth to the sphere fibre.'),('D.1.1','Full proof read; Albanese modular invariant natural boundary argument.'),('D.1.2','Full proof read; base change on the curve and Buchdahl input checked in the argument.'),('D.1.3','Opening read, not its whole proof.'),('B.4.4','Marked-map extension proof read.'),('B.4.27','Log-torus sheaf cohomology proof read.'),('B.4.30','Base modification and extension-of-differences proof read.'),('B.4.31','Global-meridian proof read.'),('B.4.32','Global-loop defect proof read.'),('B.4.33','Proof read; explicit objects B.4.9, B.4.18 and B.4.19 were not independently re-derived.'),('C.3.21','Actual delta-square proof read.'),('C.3.22','Signed-cap comparison proof read.'),('C.3.23','Equivariant integer proof read.'),('C.3.24','Monodromy-value proof read; C.3.10, C.3.14 and C.3.18 were not read in this intake.'),('C.3.27','Second determination proof read.'),('E.2.21','Disc-completion proof read.'),('E.2.22','Connected-base propagation proof read; E.2.5--E.2.20 remain unread inputs.'),('E.2.24','Continuous-deformation proof read; the Kuranishi theorem is an external input.')]:
    check(fh,'2026-11-16','R' if sid=='D.1.3' else ('F,D' if sid=='A.3.1' else 'F'),'PUSH '+sid,'Bounded intake with earlier notes and source text.','no gap found in the portion read',findings,'status/INTAKE_FINAL.md, opening and Section 1')
check(fh,'2026-11-16','F','MAPS A.3.1','Bounded intake.','no conflict found','Full proof read. A.3.2 was read only as statement and setup; fixed-locus conclusions retain A status.','status/INTAKE_FINAL.md, opening and Sections 3,5')
check(fh,'2026-11-16','F','ARI C.2.2','Bounded intake.','agrees with the real-parameter criterion','Full proof read; compared with FAM B.4.2 and MAPS A.3.','status/INTAKE_FINAL.md, opening and Section 5')
check(fh,'2026-11-16','D','CDP C5b at n=-1,0,12','Hand substitution, not a full independent proof.','Euler characteristic agrees','The supplied response records the three values; INTAKE_FINAL gives the n=0 tuple (1,1,1,0).','status/RESPONSE_INTAKE.md, Section 2; INTAKE_FINAL.md, Section 2')
check(fh,'2026-11-16','R','PUSH E.2.1 and CDP E11','Cross-run comparison of separate producing sessions.','same higher-multiplicity tangent tuple','Two runs, no second reader of these proofs; this qualifier remains attached to the T statement.','status/INTAKE_FINAL.md, Section 5 X3; RESPONSE_INTAKE.md, Section 2')
check(om,'Recorded 2026-11-16','D','special norm and phase calculation','Main-session calculation as evaluated by the intake.','n=3 division case checked by intake','The intake records NOTES Section 33(a) as a valid derivation of the special norm and phases, and Section 34 as the exact nome-ratio calculation. No unseen notes are asserted to have been opened here.','status/INTAKE_FINAL.md, Section 5, NOTES Sections 33--34 discussion')

for x in citations:
    check(x.get('by','GPT-6 Astra, ChatGPT Pro mode'),x.get('date','2026-11-16'),'S',x.get('key','')+'; '+x.get('locator',''),x.get('independence','Assembly with supplied source and review context; not an independent proof review.'),'opened and matched',x.get('matched',''),x.get('_ledger','')+'; '+x.get('url',x.get('source','')))
for i,x in enumerate(hist,1):x['check_id']='V'+str(i).zfill(3)
(R/'verification_record.json').write_text(json.dumps(hist,ensure_ascii=False,indent=2))
out += [r'\subsection{Verification record, one row per check}\label{app:verification}',r'R: statement read without following its proof. F: proof or explicitly delimited proof portion followed. D: steps re-derived. C: numerical or exact recomputation. S: source opened and matched. No L check is recorded. A producing-run computation is identified as such. The historical records do not constitute a fresh check of this assembly.',r'\begingroup\footnotesize\setlength{\tabcolsep}{3pt}\begin{longtable}{@{}L{.08\linewidth}L{.31\linewidth}L{.56\linewidth}@{}}',r'\toprule Check & By / date / type / scope & Verdict, findings, independence and report\\\midrule\endhead']
for x in hist:
    who=tex(x['by'])+'\\newline '+tex(x['date'])+'; '+tex(x['type'])+'\\newline '+tex(x['scope'])
    detail=tex(x['verdict'])+'. '+tex(x['findings'])+'\\newline '+tex(x['independence'])+'\\newline '+tex(x['report'])
    out.append(tex(x['check_id'])+' & '+who+' & '+detail+r'\\')
out += [r'\bottomrule\end{longtable}\endgroup',r'No human has checked any part of the mathematics. No formalization was supplied. No new execution of the missing mathematical programs is claimed. Gray is not a mathematical input; the public repository link was supplied but could not be fetched. Source comparisons and build checks are recorded separately from mathematical verification.']
(R/'root/appendix_c.tex').write_text('\n'.join(out)+'\n')

notes=['# S6_07_PAPER notation sheet','The paper follows FAM conventions. This sheet distinguishes global symbols, local chart variables, source equation tags, and retained statement labels. A scoped local variable does not change a global parameter. Mathematical signs are unchanged except where the supplied source explicitly converts conventions.']
for a in AGENTS:
    p=R/a/'notation.md'
    if p.exists():notes.append(p.read_text())
notes+=['## Complete retained-label concordance','| Run | Source ID | Paper label | Status |','|---|---|---|---|']
for r in rows:notes.append('| '+r['source_run']+' | '+r['source_id']+' | '+r['paper_label']+' | '+r['status']+' |')
notes+=['## Source equation and ancillary labels','The following labels are used in the assembled fragments. Prefixes identify the source run; the unchanged source ID or descriptive tail is retained.','\n'.join('- `'+x+'`' for x in sorted(set(re.findall(r'\\label\{([^}]+)\}',allfrags))))]
(D/'S6_07_PAPER_notation_sheet.md').write_text('\n\n'.join(notes)+'\n')
print(json.dumps(audit,ensure_ascii=False,indent=2));print('Verification rows',len(hist))
