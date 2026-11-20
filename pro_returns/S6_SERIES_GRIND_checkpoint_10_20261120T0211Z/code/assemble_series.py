"""Assemble five standalone, label-driven LuaLaTeX research papers.

The assembler changes presentation, exact reference transport, and explicitly
audited corrections. It does not award mathematical proof checks.
"""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,re,shutil
from tex_tools import argument,arguments,macros,replace_spans,tex_escape
from allocate_tags import base36
from layout_repairs import repair_layout

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15'
PAPERS=['I','II','III','IV','V']
csv.field_size_limit(10**9)
TITLES={'I':'Periods, moduli and the two ends','II':'Torus-fibred threefolds and the sign theorem',
        'III':'Maps and the resulting manifolds','IV':'Smooth monodromy in the group of homotopy seven-spheres',
        'V':'Complex fourfolds from the family'}
ABSTRACTS={
'I':r'''We study the holomorphic $(3,4,\infty)$ family through its normalized
elliptic periods, integral monodromy and cusp charts. The exact parameter
disc is $0<|w|<216$. The period norm determines its boundary, and the
marked classification gives the parameter equivalence, fibre strata,
automorphisms and real structures. We compute the differential-sheaf
and cohomological invariants with their explicit maps and compare the
two limiting regimes. At the puncture the deck and radial monodromies
give a proper-filling obstruction after every finite cover. At the
outer boundary the period calculations determine the limiting groups
and the failure of a global continuation. A credited appendix gives
our parameter-equivalence proof and the re-derived tangent and
deformation results in the source conventions. A holomorphic \v Cech
cocycle and a specified locally finite coordinate partition give global
Dolbeault representatives through all three special fibres. The
arithmetic period question is stated with its established reductions
and precise remaining exclusion.''',
'II':r'''We study compact complex threefolds fibred over curves, with vanishing
first and second Betti numbers. The conormal filtration retains a
cotangent-torsion connecting map omitted from a published vanishing
argument; an explicit nodal family computes the resulting
counterexample. We give the exact normalization-Picard criterion for
the corrected generic vanishing statement. For torus general fibre,
the Euler number is nonnegative for every degeneration, with
arbitrary multiplicities and support singularities; globally it is
zero or two. We describe the equality supports and the additional
equality forced by identity monodromy. The proof includes integral
component counts, local parity, conductor comparisons and explicit
compact occurrence constructions. We also compute tangent twists
and deformation spaces, retain the fibration in the stated families,
and determine the two-turn covering parameter of the retained
Liu--Rollenske family. An actual flat-kernel and conic two-jet
calculation gives a nonempty open family of twelve-tooth smoothings
with kernel $\mathcal O(-8)\oplus\mathcal O(-9)^2$ and Hodge numbers
$h^{1,1}=49$, $h^{1,2}=48$. The remaining general and special-member
comb splitting problem is stated with its precise scope.''',
'III':r'''We identify the homotopy classes of the maps supplied by the marked
$(3,4,\infty)$ construction. The repaired quotient to the three-sphere
represents the element of order two in $\pi_6(S^3)$, the holomorphic
algebraic reduction is null-homotopic, and the retained-angle cusp map
represents the nonzero element of $\pi_6(S^4)$. Actual frame and collar
maps give these identifications and a finite cell model. We determine
the global obstruction to extending a prescribed local Kummer cover
smoothly and construct its normal completion. Integral cusp products,
finite-coefficient evaluations and the published smooth classification
identify the cyclic universal covers. The same marked specialization
method determines the natural-line outputs for the retained elliptic
profiles, including the extra torsion of free OS49 caps. For the specified
weighted OS45 member, an embedded odd Hopf sphere and its explicit Borel
pair determine the refined characteristic class to be zero. Finally, an
explicit conifold transition produces the stated complex structure
on $S^3\times S^3$. The unestablished classification row is retained
with its exact remaining realization question.''',
'IV':r'''We compute smooth return classes of marked torus-fibred complex
six-spheres in $\Theta_7\simeq\Z/28$. Every construction retains its
source section, affine cap, ordinary boundary marking and cusp fan.
The physical circle bundle is the nonzero-vector bundle of $M$;
the Hermitian dual map transports its characteristic numbers to
those of $U=M^{-1}$ with the stated sign. Explicit source and cap
maps yield the return formula and a scalar algorithm for fan
changes. We determine the class sets in the retained original,
selected-infinity and selected-$I_3$ sectors, including constructions
reaching every class and the cover images of each return. Corrected
historical formulas are given with their counterexamples and the
precise replacement statements. The outstanding attachment problems
are collected with the proved arithmetic and geometric reductions.''',
'V':r'''We construct complex fourfolds from the marked torus-fibration data.
A small crepant resolution of the transverse elliptic fibre product
has explicitly computed canonical line, coherent cohomology and
integral characteristic pairings. A rank-six construction with finite
orders five and four gives compact complex fourfolds on
$3\mathbb{HP}^2\#(-\mathbb{HP}^2)$ with their complex orientation.
Its integral boundary maps kill the remaining torsion with
coefficient one. A genus-two pencil, its exterior-square lattice and
an explicit split lift supply the periods. In the algebraic
splitting the exact parameter domain is
$\operatorname{Im}\xi>c_*$, where
$c_*=1.0945402503114027801162682630549457037\ldots$ is specified by
the normalized Frobenius period expression. We give the family's
cohomology, deformations, automorphisms, endpoint obstruction and
integral input classification. Wall's extended-form theorem and
Kramer--Stolz's absorption theorem are the cited smooth
classification inputs. The fibre-product part also records the
explicit shifted constructions of complex dimension five.'''}

def all_cites(text):
    result=set()
    for m in re.finditer(r'\\(?:cite|citet|citep|citealp|citealt|citeauthor|citeyear|citeyearpar|nocite)\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^}]+)\}',text):
        result.update(k.strip() for k in m.group(1).split(','))
    return result

def bib_entries(text):
    result={}
    for m in re.finditer(r'@(\w+)\s*\{',text):
        content,end=argument(text,m.end()-1,comments=False)
        key=content.split(',',1)[0].strip()
        result[key]={'text':text[m.start():end],'kind':m.group(1)}
    return result

def prune_bbl(entry):
    status="Unverified" if re.search(r"\\newblock\s+Unverified",entry,re.I) else "Verified"
    blocks=re.split(r'\\newblock\s*',entry)
    kept=[]
    for n,block in enumerate(blocks):
        if re.match(r'(?:Verified in this (?:writing|continuation)|Unverified in this writing|Freshly reopened|Freshly opened|Author/title|Same identified|Verification applies|The current|Current verification|Opened and matched)',block.strip(),re.I):continue
        if n==0:kept.append(block)
        else:kept.append('\\newblock '+block)
    return '\n'.join(kept).strip()+'\n\\newblock \\emph{'+status+'}.\n'

def get_front(paper):
    choices={'I':[ROOT/'audit_paper_i/frontmatter_I.tex'],
             'II':[ROOT/'audit_sign/frontmatter_II.tex'],
             'III':[ROOT/'frontmatter/frontmatter_III.tex'],
             'IV':[ROOT/'audit_corrections/frontmatter_IV.tex'],
             'V':[ROOT/'frontmatter/frontmatter_V.tex']}[paper]
    for path in choices:
        if path.exists():
            mp=path.with_name(path.stem+'_map.json')
            if not mp.exists() and paper=='I':mp=path.with_name('main_index_I.json')
            if mp.exists():
                text=path.read_text().replace(r'\subsection{Proofs in outline}',r'\subsection{The proofs in outline}')
                text=text.replace(r'\subsection{The families, their constructions and their cover values}',r'\paragraph{The families, their constructions and their cover values.}')
                return text,json.loads(mp.read_text()),str(path.relative_to(ROOT))
    return None,None,None

def collect_refs(text):
    result=[]
    for m in re.finditer(r'\\(?:[cC]?ref|eqref|autoref|SeriesRef)\{([^}]+)\}',text):
        result.extend(x.strip() for x in m.group(1).split(','))
    return list(dict.fromkeys(result))

def add_labels(registry,labeltags,bodies,fronts,maps):
    nextnum=max([int(v,36) for v in registry.values()]+[0])+1
    for paper,text in list(bodies.items())+list(fronts.items()):
        for label in re.findall(r'\\label\{([^}]+)\}',text):
            if label in labeltags:
                labeltags[label]['paper']=paper
                if label=='night:P5.7':labeltags[label]['kind']='statement'
                continue
            if label not in registry:registry[label]=base36(nextnum);nextnum+=1
            labeltags[label]={'tag':registry[label],'canonical_label':label,'paper':paper,
                'kind':'main theorem' if label.startswith('series:') and label.rsplit(':',1)[-1] in list('ABCDEFG') else 'reference target'}
        for label in re.findall(r'\\StatementRecord\{([^}]+)\}',text):
            if label in labeltags and labeltags[label]['kind']!='main theorem':
                labeltags[label]['kind']='statement'
    for paper,data in maps.items():
        for m in data['main_theorems']:
            labeltags[m['label']]['kind']='main theorem'

def localize_refs(text,paper,labeltags):
    spans=[]
    for m in re.finditer(r'\\(?P<kind>[cC]?ref|eqref|autoref|pageref)\{(?P<labels>[^}]+)\}',text):
        labels=[x.strip() for x in m.group('labels').split(',')]
        if any(lab in labeltags and labeltags[lab]['paper']!=paper for lab in labels):
            spans.append((m.start(),m.end(),', '.join('\\SeriesRef{'+lab+'}' if lab in labeltags and labeltags[lab]['paper']!=paper else '\\'+m.group('kind')+'{'+lab+'}' for lab in labels)))
    return replace_spans(text,spans)

def letter_theorems(text,paper,data):
    # Agent fronts use paragraph headings. The theorem counter supplies A,...,G.
    for m in reversed(data['main_theorems']):
        needle=r'\paragraph{Theorem '+m['letter']+' ('
        start=text.index(needle)
        title_start=start+len(r'\paragraph')
        heading,end=argument(text,title_start)
        mechanism=text.index(r'\textit{Mechanism.}',end)
        segment=text[end:mechanism]
        label='\\label{'+m['label']+'}'
        assert label in segment,(paper,m['label'])
        record='\\StatementRecord{'+m['label']+'}{proved}{}{'+', '.join('\\SeriesRef{'+lab+'}' for lab in m['body_labels'])+'}'
        segment=segment.replace(label,label+'\n'+record,1)
        replacement='\\begin{maintheorem}['+m['title']+']'+segment+'\\end{maintheorem}\n\n'
        text=text[:start]+replacement+text[mechanism:]
    return text

def standardize_proofs(text):
    replacements=[];stats=Counter()
    for m in re.finditer(r'\\begin\{proof\}(?:\[[^\n]*?\])?',text):
        end=text.find(r'\end{proof}',m.end())
        if end<0:raise ValueError('unclosed proof')
        content=text[m.end():end]
        step_re=re.compile(r'(?:\\noindent\s*)?\\textbf\{Step(?:~|\s+)(\d+)\.?\}')
        markers=list(step_re.finditer(content))
        if len(markers)>=2 and len(markers)==len({x.group(1) for x in markers}):
            prefix=content[:markers[0].start()]
            items=step_re.sub(r'\\item',content[markers[0].start():])
            content=prefix+'\n\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n'+items+'\n\\end{enumerate}\n'
            stats['bold_step_proofs_converted']+=1
        elif r'\begin{enumerate}' in content:
            # Numbering is a presentation change; existing item reference labels persist.
            depth=0;spans=[]
            for en in re.finditer(r'\\(begin|end)\{enumerate\}(?:\[[^\n]*?\])?',content):
                if en.group(1)=='begin':
                    depth+=1
                    token=en.group(0)
                    if 'label=\\arabic*.' in token:
                        spans.append((en.start(),en.end(),token.replace('label=\\arabic*.','label={$\\langle'+str(depth)+'\\rangle$\\arabic*.}')))
                else:depth-=1
            content=replace_spans(content,spans);stats['enumerated_proofs']+=1
        else:
            # Preserve the entire argument as its explicit claim-and-reason block.
            content='\n\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n\\item '+content+'\n\\end{enumerate}\n'
            stats['single_argument_proofs_numbered']+=1
        replacements.append((m.end(),end,content))
    return replace_spans(text,replacements),dict(stats)

def metadata_and_tags(text,paper,labeltags,inventory,backlinks,dependencies):
    spans=[]
    for a,b,args in macros(text,'StatementRecord',4):
        label,status,oldcheck,uses=args
        info=labeltags[label];tag=info['tag']
        deps=[lab for lab in collect_refs(uses) if lab in labeltags and lab!=label]
        dependencies[label]=deps
        use_text=', '.join('\\SeriesRef{'+lab+'}' for lab in deps)
        cite_matches=[m.group(0) for m in re.finditer(r'\\cite[a-z]*(?:\[[^\]]*\]){0,2}\{[^}]+\}',uses)]
        if cite_matches:
            use_text+='; ' if use_text else ''
            use_text+='; '.join(cite_matches)
        if not use_text:use_text='the definitions and constructions stated in the proof'
        display={'false as stated':'false','proved under hypotheses H':r'proved(H)'}.get(status,status)
        spans.append((a,b,'\\StatementRecord{'+label+'}{'+display+'}{'+tag+'}{'+use_text+'}'))
    text=replace_spans(text,spans)
    # Place one named PDF destination for every permanent anchor group.
    spans=[];seen=set()
    for m in re.finditer(r'\\label\{([^}]+)\}',text):
        lab=m.group(1)
        if lab not in labeltags:continue
        tag=labeltags[lab]['tag']
        if tag in seen:continue
        seen.add(tag)
        spans.append((m.start(),m.start(),'\\hypertarget{tag-'+tag+'}{}'))
    text=replace_spans(text,spans)
    return text

def series_section(paper):
    text = r'''\subsection{The series and this paper}
We study the holomorphic families supplied by the marked
$(3,4,\infty)$ torus-fibred construction and the maps, degenerations
and manifolds obtained from its explicit periods and gluing data.
The source lattice, finite twists, cusp fan, line convention and
parameter normalization remain part of each construction. The five
papers form one series; the table gives their main conclusions and
their cross-paper inputs.
\begin{center}\small
\begin{tabularx}{\textwidth}{@{}lXl@{}}\toprule
Paper & Main result & Uses\\\midrule
I & Exact periods, moduli, fibre strata and the two ends & ---\\
II & Corrected cotangent argument and the sign for all degenerations & I, IV\\
III & Marked map classes, integral covers and their smooth outputs & I, II, IV, V\\
IV & Physical-circle return classes and the complete retained fan calculations & I, II, III, V\\
V & Resolved fibre products and the marked rank-six fourfold family & I, III, IV\\
\bottomrule\end{tabularx}\end{center}
'''
    if paper=='I':
        text += (ROOT/'frontmatter/whole_series_rung_zero.tex').read_text()
    return text

def methodology(paper,events):
    labels={e['statement_id'] for e in events}
    count=Counter(e['type'] for e in events)
    lines=[]
    names={'targeted proof check':'targeted proof checks','independent re-proof':'independent re-proofs',
           'computation or formal certificate':'computational or formal certificates',
           'used and rechecked in this run':'use or reconciliation events',
           'carried as background without fault found':'background-carry events',
           "refuted, with the refined statement's id":'refutation records'}
    for kind,n in count.items():lines.append(str(n)+' '+names.get(kind,tex_escape(kind)))
    return r'''\subsection{Methodology}
This mathematical text is AI-produced. GPT-5.6 Sol (OpenAI), in
Codex at reasoning effort ultra, produced the working edition during
24 August--9 September 2026. GPT-6 Astra (OpenAI), in ChatGPT Pro
mode at effort Pro, carried out the research runs of 12--16 November,
the S6\_06\_BLIND run of 16--18 November, the S6\_09\_PAPERS and
S6\_10\_PAPERS writing runs of 16--19 November, and this series run
on 19 November 2026. Claude Fable 5.2 (Anthropic), at effort high and
at effort max, and Claude Opus 5.5 (Anthropic), at effort max,
performed readings, intakes, sweeps and checks during 12--19 November
2026. Prompts specified the statements, marked inputs and requested
checks. Returned proofs and computations were read against those
inputs and the opened original sources. Corrections entered the next
prompt and the receiving statements with their explicit transports.

The recorded methods include derivation before reading the supplied
proof, independent re-proofs, exact and interval computations,
checks of special cases, and comparison of scope and conventions
with original sources. For this paper the received and current
record contains '''+', '.join(lines)+r'''.
Each event keeps its actual scope; an editorial reconciliation
contributes no proof verification. The linked entry for every
statement records the agreeing routes and remaining risk.
No human has checked the mathematics.

We dedicate our text to the public domain under
\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0 1.0 Universal}.
The earlier runs and check records are preserved in the
\href{https://github.com/KokunoYumeto/s6-complex-structure-workbench/tree/4e8b547874c2acff6b49713ca96f84b281ab5793}{pinned workbench archive};
the register sweep is in the
\href{https://github.com/KokunoYumeto/grothendieck-montpellier-archive/tree/96b2bcaec355870a8faa9457406673b7cd897654/raw/results_register/sweep1_s6}{pinned sweep archive}.
The current statement records are
\href{S6_SERIES_GRIND_checks_'''+paper+r'''.md}{the accompanying check file},
with the complete typed ledger in \href{CHECK_EVENTS.tsv}{CHECK\_EVENTS.tsv}.
'''

def further_table(paper,body,labeltags,mainmap):
    main_targets={x for m in mainmap.get('main_theorems',[]) for x in m.get('body_labels',[])}
    labels=[]
    for a,b,args in macros(body,'StatementRecord',4):
        label=args[0]
        if label not in main_targets and label not in labels:labels.append(label)
    text='\n\\paragraph{Further results.}\n\\begingroup\\small\n\\begin{longtable}{@{}ll@{\\hspace{1cm}}ll@{}}\n\\toprule Result & Tag & Result & Tag\\\\\\midrule\\endhead\n'
    split=(len(labels)+1)//2
    for i in range(split):
        cells=[]
        for j in [i,i+split]:
            if j<len(labels):
                lab=labels[j];cells += ['\\SeriesRef{'+lab+'}','\\texttt{'+labeltags[lab]['tag']+'}']
            else:cells+=['','']
        text+=' & '.join(cells)+r'\\'+'\n'
    return text+'\\bottomrule\n\\end{longtable}\\endgroup\n'

def known_new(front,data):
    rows=[]
    for n,m in enumerate(data['main_theorems']):
        start=front.index('\\hypertarget{main-'+data['paper']+'-'+m['letter']+'}')
        end=front.find('\\hypertarget{main-',start+1)
        if end<0:end=front.index('\\subsection{The proofs in outline}')
        section=front[start:end]
        at=section.find(r'\textit{Relation to literature.}')
        if at>=0:
            value=section[at+len(r'\textit{Relation to literature.}'):]
            value=value.split(r'\hyperlink{outline-',1)[0].strip()
        else:value='The exact source locators are recorded in the full statements and their linked check entries.'
        rows.append((m['letter'],value))
    text='\\subsection{Known and new}\n\\begingroup\\small\n\\begin{longtable}{@{}p{.10\\textwidth}p{.85\\textwidth}@{}}\\toprule Theorem & Exact source relationship\\\\\\midrule\\endhead\n'
    for letter,value in rows:text+=letter+' & '+value+r'\\'+'\n'
    return text+'\\bottomrule\\end{longtable}\\endgroup\n'

from dependency_figures import organization
from hierarchical_proofs import hierarchical_proofs

def main():
    registry=json.loads((ROOT/'analysis/permanent_tag_registry.json').read_text())
    labeltags=json.loads((ROOT/'analysis/label_tags.json').read_text())
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open() as f:inventory=list(csv.DictReader(f))
    with (ROOT/'CHECK_EVENTS.tsv').open() as f:events=list(csv.DictReader(f,delimiter='\t'))
    bodies={p:(ROOT/f'parts/{p}.body.linked.tex').read_text() for p in PAPERS}
    fronts={};maps={};front_sources={};missing=[]
    for p in PAPERS:
        front,data,path=get_front(p)
        if front is None:missing.append(p);continue
        fronts[p]=front;maps[p]=data;front_sources[p]=path
    if missing:
        print(json.dumps({'not_assembled':'waiting for complete frontmatter','papers':missing}));return
    # The conditional period row is part of the exact unresolved-period gate.
    old='\\clearpage\n\\part{Results not yet established}\n'
    marker=r'\section{Periods, compact subgroups, and the transcendence question}'
    if marker in bodies['I']:
        bodies['I']=bodies['I'].replace(old,'',1).replace(marker,old+marker,1)
    add_labels(registry,labeltags,bodies,fronts,maps)
    (ROOT/'analysis/permanent_tag_registry.json').write_text(json.dumps(registry,indent=2))
    (ROOT/'analysis/label_tags.json').write_text(json.dumps(labeltags,indent=2))
    (ROOT/'analysis/main_theorems.json').write_text(json.dumps(maps,indent=2))
    backlinks=defaultdict(list)
    for paper,data in maps.items():
        for m in data['main_theorems']:
            for step in m['steps']:
                for lab in step['body_targets']:backlinks[lab].append((paper,m['letter'],step['number'],step['anchor']))
    bibsource=json.loads((ROOT/'analysis/source_bibliography_entries.json').read_text())
    rawbib=bib_entries((SOURCE/'S6_10_PAPERS_references.bib').read_text())
    extra_bib=ROOT/'analysis/additional_references.bib'
    if extra_bib.exists():rawbib.update(bib_entries(extra_bib.read_text()))
    basepreamble=(SOURCE/'preamble.tex').read_text()
    # The reference macros in the original standalone file are outside preamble.tex.
    preamble=basepreamble[:basepreamble.index(r'\newcommand{\StatementRecord}')]
    preamble+=basepreamble[basepreamble.index(r'\newcommand{\RungZero}'):]
    preamble+=r'''
\usepackage{etoolbox}
\setmonofont[BoldFont=lmmonolt10-bold.otf,ItalicFont=lmmono10-italic.otf]{lmmono10-regular.otf}
\hypersetup{bookmarksnumbered=true,bookmarksdepth=2}
\setcounter{tocdepth}{2}
\makeatletter\renewcommand{\@pnumwidth}{2.5em}\renewcommand{\@tocrmarg}{3.5em}\renewcommand*{\l@subsection}{\@dottedtocline{2}{1.5em}{3.5em}}\makeatother
\newtheorem{maintheorem}{Theorem}
\renewcommand{\themaintheorem}{\Alph{maintheorem}}
\crefname{maintheorem}{theorem}{theorems}
\newcommand{\StatementRecord}[4]{\par\smallskip\begingroup\upshape\raggedright\noindent
\textbf{\texttt{[#3]} #2}\quad
\href{S6_SERIES_GRIND_checks_\CurrentPaper.md\#tag-#3}{checks}\quad
\href{S6_SERIES_GRIND_checks_\CurrentPaper.md\#uses-#3}{uses and used by}\par
\noindent\textit{uses:} #4.\par
\ifcsname SBack@#1\endcsname\noindent\csname SBack@#1\endcsname\par\fi
\endgroup\smallskip}
\newcommand{\ExternalPaperRef}[3]{#1#2 (Paper~#3)}
\newcommand{\CompendiumRef}[2]{\ifmmode\text{\upshape S6\_09, Paper~#1, label~\nolinkurl{#2}}\else S6\_09, Paper~#1, label~\nolinkurl{#2}\fi}
\newcommand{\SeriesRefText}[1]{\ifcsname SRef@#1\endcsname\csname SRef@#1\endcsname\else\textbf{UNRESOLVED}\fi}
\newcommand{\SeriesRef}[1]{\ifmmode\text{\SeriesRefText{#1}}\else\SeriesRefText{#1}\fi}
\AfterEndEnvironment{proof}{\par\begingroup\footnotesize\noindent\hyperref[sec:results]{Return to \S1.}\par\endgroup\smallskip}
'''
    dependencies={};stats={};allkeys=set();missingbib={};source_text={}
    for paper in PAPERS:
        front=localize_refs(fronts[paper],paper,labeltags)
        data=maps[paper]
        lit=known_new(front,data)
        extra_lit=ROOT/f'frontmatter/{paper}_literature_comparison.tex'
        if extra_lit.exists():lit+='\n'+extra_lit.read_text()
        front=letter_theorems(front,paper,data)
        outline_marker=r'\subsection{The proofs in outline}'
        front=front.replace(outline_marker,further_table(paper,bodies[paper],labeltags,data)+'\n'+outline_marker,1)
        body=localize_refs(bodies[paper],paper,labeltags)
        body,proofstats=standardize_proofs(body)
        body,hierarchy_stats=hierarchical_proofs(body,paper)
        proofstats.update(hierarchy_stats)
        per_events=[e for e in events if labeltags.get(e['statement_id'],{}).get('paper')==paper]
        article='\\title{The $(3,4,\\infty)$ family of complex six-spheres\\\\[.5em]'+paper+'. '+TITLES[paper]+'}\n\\author{AI-produced mathematical text}\n\\date{19 November 2026}\n\\maketitle\n'
        article+='\\begin{abstract}\n'+ABSTRACTS[paper]+'\n\\end{abstract}\n\\clearpage\n\\tableofcontents\n\\clearpage\n'
        article+='\\section{Results and their proofs in outline}\\label{sec:results}\n'+series_section(paper)+front+lit+methodology(paper,per_events)+organization(paper,data)+'\n\\clearpage\n'+body
        article=repair_layout(article,paper)
        article=metadata_and_tags(article,paper,labeltags,inventory,backlinks,dependencies)
        keys=all_cites(article);allkeys|=keys
        missingbib[paper]=sorted(keys-set(bibsource))
        if missingbib[paper]:
            print(json.dumps({'missing_bibliography':missingbib[paper],'paper':paper}));return
        entries=[prune_bbl(bibsource[key][0]['text']) for key in sorted(keys)]
        article+='\n\\clearpage\n\\begin{thebibliography}{99}\n\\providecommand{\\natexlab}[1]{#1}\n\\providecommand{\\doi}[1]{\\url{https://doi.org/#1}}\n'+'\n'.join(entries)+'\n\\end{thebibliography}\n'
        stats[paper]={'body_characters':len(body),'front_characters':len(front),'bibliography_entries':len(keys),'proof_format':proofstats,'front_source':front_sources[paper]}
        source_text[paper]=article
    (ROOT/'analysis/dependencies.json').write_text(json.dumps(dependencies,indent=2))
    (ROOT/'analysis/outline_backlinks.json').write_text(json.dumps(backlinks,indent=2))
    # Use previously compiled current page/number data when available.
    current={}
    for paper in PAPERS:
        path=ROOT/f'analysis/current_labels_{paper}.json'
        if path.exists():current[paper]=json.loads(path.read_text())
    for paper,article in source_text.items():
        defs='\\newcommand{\\CurrentPaper}{'+paper+'}\n'
        for lab,info in labeltags.items():
            owner=info['paper'];tag=info['tag'];meta=current.get(owner,{}).get(lab,{})
            number=meta.get('number','?');page=meta.get('page','?')
            if owner==paper:
                value='\\hyperlink{tag-'+tag+'}{'+paper+'.\\ref*{'+lab+'}}'
            else:
                value='\\href{S6_SERIES_GRIND_'+owner+'.pdf\\#nameddest=tag-'+tag+'}{'+owner+'.'+number+' (p.~'+page+')} '
            defs+='\\expandafter\\def\\csname SRef@'+lab+'\\endcsname{'+value+'}\n'
        for lab,steps in backlinks.items():
            if labeltags.get(lab,{}).get('paper')!=paper:continue
            phrases=[]
            for owner,letter,n,anchor in steps:
                if owner==paper:phrases.append('\\hyperlink{'+anchor+'}{proves step '+str(n)+' of Theorem '+letter+'}')
                else:phrases.append('\\href{S6_SERIES_GRIND_'+owner+'.pdf\\#nameddest='+anchor+'}{proves step '+str(n)+' of Theorem '+owner+'.'+letter+'}')
            defs+='\\expandafter\\def\\csname SBack@'+lab+'\\endcsname{'+ '; '.join(phrases)+'}\n'
        (ROOT/f'S6_SERIES_GRIND_{paper}.tex').write_text(preamble+'\n'+defs+'\n\\begin{document}\n'+article+'\n\\end{document}\n')
    (ROOT/'S6_SERIES_GRIND_references.bib').write_text('% Only entries cited by the five current papers. Verification scopes are retained verbatim.\n'+'\n\n'.join(rawbib[k]['text'] for k in sorted(allkeys) if k in rawbib)+'\n')
    (ROOT/'code/outputs/assembly.json').write_text(json.dumps(stats,indent=2))
    (ROOT/'analysis/abstracts.json').write_text(json.dumps(ABSTRACTS,indent=2))
    print(json.dumps({'papers':stats,'total_cited_keys':len(allkeys),'missing_bib_keys':sorted(allkeys-set(rawbib))}))

if __name__=='__main__':
    from pipeline_lock import pipeline_lock
    with pipeline_lock(ROOT):main()
