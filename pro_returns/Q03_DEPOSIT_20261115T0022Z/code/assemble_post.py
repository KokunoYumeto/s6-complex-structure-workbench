#!/usr/bin/env python3
"""Assemble the audited standalone post and its per-statement CSV.

Inputs: the supplied background beside this directory, revised mathematical
extracts and editorial fragments in work/, and the source concordance in code/.
No network calls or publication are performed.
"""
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BACKGROUND = ROOT.parent/'background'
WORK = ROOT/'work'


def tex(text):
    return ''.join({'&':r'\&','%':r'\%','_':r'\_','#':r'\#',
                    '^':r'\textasciicircum{}','~':r'\textasciitilde{}'}.get(c,c) for c in text)


def brace_argument(source, pos):
    assert source[pos] == '{'
    depth = 1
    j = pos+1
    while depth:
        if source[j] in '{}' and (j == 0 or source[j-1] != '\\'):
            depth += 1 if source[j] == '{' else -1
        j += 1
    return source[pos+1:j-1], j


def statement_records(proof):
    matches=list(re.finditer(r'\\begin\{(numbered|numberedup)\}\{([^{}]+)\}\{([0-9.]+)\}',proof))
    result=[]
    for i, match in enumerate(matches):
        title, start=brace_argument(proof, match.end())
        end=proof.index(r'\end{'+match.group(1)+'}', start)
        after=end+len(r'\end{'+match.group(1)+'}')
        usepos=proof.index(r'\uses{', after)+len(r'\uses')
        uses,_=brace_argument(proof,usepos)
        result.append({'id':match.group(3),'kind':match.group(2),'title':title,
                       'statement':proof[start:end].strip(),'uses':uses})
    return result


def make_record():
    record={
      'format':'hexagon-post-format/1','record_id':'Q03','version':1,'date':'2026-11-15',
      'title':'Polynomial-time unit-job scheduling for every fixed number of machines m >= 3',
      'kind':'generalization','claim_status':'proved',
      'statement_plain':'For every fixed integer m >= 3, explicitly listed unit jobs with arbitrary acyclic precedence on m identical machines admit exact deadline decision, witness construction and optimum construction in at most G(m)(L+2)^(60m^2+129m+2) deterministic fixed-multitape steps. A parsed canonical padded deadline with N=mT jobs uses at most A(m,12m+25)N^(60m^2+129m+1) steps. The description hierarchy has 12m+25 global leaves and 6m+16 relative-prefix leaves.',
      'statement_tex':r'For each fixed $m\geq3$, $Pm\mid\mathrm{prec},p_j=1\mid C_{\max}$ is solvable in deterministic multitape time $O_m((L+2)^{60m^2+129m+2})$; a parsed padded deadline uses $O_m(N^{60m^2+129m+1})$ steps, $N=mT$.',
      'extends':'OpenAI, preprint of 24 September 2026, Theorem 1.1 (three machines); all steps are proved here.',
      'known_before':'Two machines: Fujii-Kasami-Ninomiya with erratum, Coffman-Graham; variable-machine NP-completeness: Ullman; three machines: OpenAI; four-machine theorem code: drbh bbd3013; all-fixed-m theorem and linear budgets stated by Jansen arXiv:2611.09392v1.',
      'new_here':'Self-contained audited capacity-m proof and itemized costs of the supplied Q03 construction; no novelty or priority claim.',
      'main_statements':['Theorem A = Theorem 1.1 of the supplied return, established in 9.1-9.3','Theorem B = Theorem 8.5'],
      'statements_in_proof':44,
      'hard_step':'Lemma 5.5; Lemmas 6.2 and 6.5; Lemma 7.1; Lemma 8.4',
      'external_results':'none load-bearing',
      'produced_by':[
          {'role':'question','model':'Claude Opus 5.5','effort':'effort not recorded','date':'2026-10-22'},
          {'role':'proof return','model':'GPT-6 Astra','effort':'ChatGPT Pro mode','date':'2026-10-23'},
          {'role':'format text','model':'Claude Fable 5.2','effort':'high','date':'2026-11-14'},
          {'role':'conversion','tool':'pandoc 3.9.0.2','date':'2026-11-14'},
          {'role':'deposit-task author','model':'Claude Opus 5.5','effort':'max','date':'2026-11-15'},
          {'role':'current audit and editing','model':'GPT-6 Astra','effort':'ChatGPT Pro mode','date':'2026-11-15'}],
      'checks':[
          {'id':'H1','by':'Claude Opus 5.5','effort':'max, Message Batches API','date':'2026-10-23','type':'F,D','scope':'supplied return','verdict':'proved with fixable gaps'},
          {'id':'H2','by':'Claude Opus 5.5','effort':'max, Message Batches API','date':'2026-10-23','type':'D','scope':'supplied return','verdict':'proved as stated'},
          {'id':'H3','by':'Claude Opus 5.5','effort':'max, Message Batches API','date':'2026-10-23','type':'F','scope':'supplied return','verdict':'proved as stated'}],
      'checks_of_this_text':[{'by':'GPT-6 Astra (OpenAI)','effort':'ChatGPT Pro mode','date':'2026-11-15','type':'F,D,C,S','scope':'all 44 numbered statements in Sections 2-9; main theorems; rewritten proofs; costs; source attribution; finite checks; post consistency','verdict':'proved as stated','limits':'S-FKN original full text unavailable; S-L archival endpoint 404; historical prompt manifest discrepancy; no independent Lean build'}],
      'human_understanding':'none','text_origin':'primarily AI-generated','formalization':'none for this proof',
      'open_points':[
          'No mathematical gap found in Sections 2-9. The three original cost/source audit items are addressed by the recorded checks.',
          'Original FKN 1969 full text unavailable; publisher metadata/abstract and 1971 erratum opened.',
          'Course provenance.json endpoint returned HTTP 404; first-publication dates are unverified.',
          'Supplied original prompt is 9551 bytes; historical manifest lists an absent 9383-byte variant with a different hash. Supplied prompt preserved verbatim.',
          'Historical run dates, API mode and independence are supplied-record metadata; raw API logs absent.',
          'OpenAI/drbh Lean builds and Jansen/Giraudin full proofs were not independently replayed or audited; their declared scope was checked.'],
      'not_claimed':['a bound polynomial in m','a practical algorithm','release dates, individual deadlines, unequal machine speeds or unequal job lengths','formalization of this proof','novelty or priority','optimality of the displayed exponent'],
      'literature_search':{'date':'2026-11-15','scope':'arXiv; STOC, FOCS, SODA, ICALP, IPCO, ESA, APPROX; authors pages; GitHub; general web; Hexagon; title/citation searches for the OpenAI preprint','outcome':'found drbh four-machine code, Jansen all-fixed-m theorem statement and linear budgets, Giraudin three-machine exponent statement; no fixed-m>=4 hardness result located; no priority claim'},
      'licence':'CC0-1.0',
      'provenance':{'prompt':'anc/ai-provenance/Q03_PROMPT.txt','current_request':'anc/Q03_DEPOSIT_prompt.md','return':'anc/ai-provenance/Q03-solution.md','return_sha256':'3ebeb452d6f461c23b4f8fa6f04ba6ed15abac541b5d2562fa814ba77977e60c','reports':['anc/ai-provenance/Q03-check.md','anc/ai-provenance/Q03-b-check-b.md','anc/ai-provenance/Q03-c-check-c.md'],'current_report':'Q03_DEPOSIT_report.md','repository':'ancillary files supplied with this deposit package; no external publication by this audit'},
      'hexagon':{'subject':'cs.DS','cross_lists':['cs.DM','cs.CC','math.CO','math.OC'],'msc':['90B35','68Q25','68W40','06A07'],'tags':['scheduling','precedence constraints','unit jobs','identical machines','makespan','fixed number of machines','polynomial-time algorithm','dynamic programming','partially ordered sets'],'tools':['GPT-6 Astra, ChatGPT Pro mode','Claude Opus 5.5, effort max','Claude Opus 5.5, effort max, Message Batches API','Claude Opus 5.5, effort not recorded','Claude Fable 5.2, effort high','pandoc 3.9.0.2','Python 3','pdfLaTeX'],'comments':'Current text audited F,D,C,S by GPT-6 Astra, ChatGPT Pro mode; cost exponent corrected to 60m^2+129m+2. Source-access and archival qualifications stated. No human proof check or formalization of this text. No novelty/priority claim.','provenance_statement':'See the Provenance and Declarations parts of the post, reproduced in the accompanying form answers.'}}
    return record


def source_rows():
    descriptions=[
      ('S-P','Preprint [P], thirteen pinned files, all counterparts and constants','Proved as stated for the source attributions. Files are byte-identical; exact locators are in the source report.'),
      ('S-F','Scope file [F], target declaration and actual proof source','Proved as stated for the declared scope. Actual Model/Main source and target correspondence checked; comparator placeholder is identified. No independent Lean replay.'),
      ('S-D','drbh [D], exact commit, capacity, theorem and source diff','Proved as stated for source scope: complete four-machine release-theorem code. No Lean rebuild; no arbitrary-machine theorem in this commit.'),
      ('S-N','[N], Theorem 1.1 and SODA bibliography','Proved as stated for the attributed upper bound and bibliographic details.'),
      ('S-A','[A], Theorem 1 and ESA bibliography','Proved as stated for approximation guarantee and parameter-dependent time bound. The integer-makespan connection is displayed in Section 1.3.'),
      ('S-FKN','[FKN], publisher metadata/abstract; [FKN-e], full erratum','Incomplete for the original 1969 full proof; the stated metadata, abstract scope and 1971 erratum were compared.'),
      ('S-CG','[CG], original scan, Theorem 1, p.203 and p.202','Proved as stated for two-machine theorem scope and bibliographic details.'),
      ('S-U','[U], original article, Theorem 1, p.389; discussion p.392','Proved as stated for the variable-machine unit-job attribution and bibliography.'),
      ('S-GJ','[GJ], actual OPEN8 p.287 and SS9 p.239','Proved as stated for the historical entries and bibliographic details; relevant scan pages visually inspected.'),
      ('S-L','[L], metadata and eleven chapter sources','Proved as stated for bylines, content and first-eight byte equality; advertised archive endpoint unavailable.'),
      ('S-J','[J], Theorem 1.1 and Lemma 7.15','Proved as stated for scope attribution: existing fixed-machine result and linear budgets. Complete proof not independently re-derived.'),
      ('S-G','[G], Theorem 1 and dated Hexagon entry','Proved as stated for the three-machine exponent attribution. Complete proof not independently re-derived.'),
    ]
    rows=[]
    for check,scope,verdict in descriptions:
        display=check.replace('S-FKN','S-FKN / S-FKN-e') if check=='S-FKN' else check
        rows.append(tex(display)+r' & GPT-6 Astra, ChatGPT Pro mode; 15 Nov 2026 & S & '+tex(scope)+' & '+tex(verdict)+r' Report: \path{Q03_DEPOSIT_sources.md}, '+tex(check)+r'.\\[3pt]')
    return '\n'.join(rows)


def bibliography():
    source=(WORK/'C_bibliography.tex').read_text()
    # Supply an identifier for the book and give every entry its role/check attribution.
    source=source.replace('also Appendix A5.2, SS9, p.~239. [S-GJ]',
        r'also Appendix A5.2, SS9, p.~239. '+
        r'\url{https://books.google.com/books/about/Computers_and_Intractability.html?id=fjxGAQAAIAAJ}. [S-GJ]')
    roles={'P':'source of the construction; background','F':'formalization-scope background',
           'D':'prior four-machine code','L':'source of the construction and question'}
    parts=re.split(r'(?=\\bibitem)',source)
    for i,part in enumerate(parts):
        key=re.search(r'\\bibitem\[[^\]]*\]\{([^}]+)\}',part)
        if not key: continue
        role=roles.get(key.group(1),'background')
        part=re.sub(r'\[(S-[A-Za-z-]+)\]',lambda m:'['+role+'; opened and compared by GPT-6 Astra, ChatGPT Pro mode, 15 November 2026; '+m.group(1)+']',part)
        parts[i]=part
    return ''.join(parts)


def main():
    original=(BACKGROUND/'post/hexagon_post_example_Q03.tex').read_text()
    proof=(WORK/'B_proof_revised.tex').read_text()
    proof=proof.replace(r'\begin{proof}[Proof (step layout of the format; the argument is the answer\'s)]',r'\begin{proof}')
    proof=proof.replace("\\begin{proof}[Proof (step layout of the format; the argument is the answer's)]",r'\begin{proof}')
    section9=(WORK/'A_replacement.tex').read_text()
    # This explicit bijective renaming separates a numeric state bound from cutoff sets.
    section9=re.sub(r'\$[^$]*\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)', lambda match: match.group(0).replace('S', r'\mathcal{S}'), section9)
    proof=proof.replace(r'Every full schedule of \(J\) on \(m\) machines admits a hierarchy', r'For \(m\geq3\), every full schedule of \(J\) on \(m\) machines admits a hierarchy')
    section9=section9.replace('Run the dynamic program of Section 2', r'For $m\geq3$, run the dynamic program of Section 2')
    section9=section9.replace('For fixed $m$, deadline decision', r'For each fixed $m\geq3$, deadline decision')
    combined=proof+'\n'+section9
    statements=statement_records(combined)
    assert len(statements)==44
    source_map={x['q03_id']:x for x in json.loads((ROOT/'code/C_dependency_source_map.json').read_text())}
    deltas={}
    for line in original.splitlines():
        m=re.match(r'^(\d+\.\d+) (.+?) & (.+?) & (.+?) & (.+?) \\\\',line)
        if m: deltas[m.group(1)]=m.group(5)
    changed={'2.2','2.3','2.7','2.8','2.9','3.3','5.5','6.2','6.5','8.1','8.4','8.5','9.1','9.2','9.3','9.4'}
    table=[r'{\footnotesize',r'\begin{longtable}{@{}L{2.6cm}L{3.2cm}L{3.7cm}L{5.1cm}@{}}',
      r'\caption{All numbered proof statements, source counterparts and direct dependencies.}\label{tab:dep}\\',
      r'\toprule Statement & Source counterpart [P], S-P & Uses & Capacity transfer\\\midrule\endfirsthead',
      r'\toprule Statement & Source counterpart [P], S-P & Uses & Capacity transfer\\\midrule\endhead',
      r'\bottomrule\endfoot']
    for st in statements:
        sid=st['id']; counterpart=source_map[sid]
        loc=tex(counterpart['source_display'])
        if counterpart['source_label']:
            loc+=r'; \textsf{'+tex(counterpart['source_label']).replace(':',r':\allowbreak ').replace('-',r'-\allowbreak ')+r'}'
        else:
            loc+=' (prose)'
        delta=deltas.get(sid,'Definitions only.')
        if sid=='2.9': delta=r'Slot size $3$ becomes $m$; the hierarchy clauses are retained.'
        if sid=='8.1': delta=r'The same restriction identities use the capacity-dependent carry bound $A_m=6m+9$.'
        if sid=='9.2': delta=r'$B=K512^KN^{mK}$; $\mathcal{S}=BN^m$; every tape subroutine is counted.'
        if sid=='9.3': delta=r'$N\leq mL$ and at most $L$ trials give exponent $60m^2+129m+2$.'
        if sid=='9.4': delta=r'Explicit compact expansion $n\leq N<2m|E|$; decision output is bounded.'
        prefix='Changed: ' if sid in changed else 'Unchanged argument: '
        table.append(tex(st['kind']+' '+sid)+' & '+loc+' & '+st['uses']+' & '+prefix+delta+r'\\[3pt]')
    table+= [r'\end{longtable}}']
    dep='\n'.join(table)
    a=original.index(r'\subsection*{Notation}')
    b=original.index('% ======================= Proof:',a)
    notation=original[a:b]
    cut=notation.find(r'\noindent Two symbols')
    if cut>=0: notation=notation[:cut]
    notation=notation.replace('$B$, $S$ (Section 9 only)',r'$B$, $\mathcal{S}$ (Section 9 only)')
    notation+=r'''\noindent The numeric state bound is written $\mathcal{S}$ in Section 9; it is the quantity denoted $S$ there in the supplied return. Cutoffs retain $S$. The set variables $L,Z,R$ in state triples are local to those definitions; $L$ in complexity bounds is the encoded input length. The leaf budget $K$ and the indexed list entries $K_j$ are distinguished by their definitions.
'''
    record=make_record()
    header='%%% POST-RECORD v1 BEGIN\n'+'\n'.join('% '+k+': '+json.dumps(v,ensure_ascii=False) for k,v in record.items())+'\n%%% POST-RECORD v1 END\n'
    front=(WORK/'frontmatter.tex').read_text().replace('%%KNOWN_TABLE%%',(WORK/'known_table.tex').read_text()).replace('%%DEPENDENCY_TABLE%%',dep).replace('%%NOTATION_TABLE%%',notation)
    end=(WORK/'endmatter.tex').read_text().replace('%%SOURCE_CHECK_ROWS%%',source_rows()).replace('%%BIBLIOGRAPHY%%',bibliography())
    buildpath=WORK/'build_final/build_check.json'
    build=json.loads(buildpath.read_text()) if buildpath.exists() else {'pages':0,'overfull_count':0,'overfull_over_2pt':0}
    for marker,key in [('%%FINAL_PAGES%%','pages'),('%%FINAL_OVERFULL%%','overfull_count'),('%%FINAL_OVER_2%%','overfull_over_2pt')]:
        end=end.replace(marker,str(build[key]))
    final=header+front+'\n'+combined+'\n'+end
    assert not re.search(r'%%[A-Z_]+%%',final)
    assert 'demonstration:' not in final
    (ROOT/'Q03_DEPOSIT_post.tex').write_text(final)
    (WORK/'record.json').write_text(json.dumps(record,indent=2,ensure_ascii=False))
    (WORK/'dependency_table.tex').write_text(dep)
    (WORK/'notation_table.tex').write_text(notation)
    with (ROOT/'Q03_DEPOSIT_results.csv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=['id','statement','status','where_checked','depends_on','notes'])
        writer.writeheader()
        writer.writerow({'id':'Cited result 1','statement':re.search(r'\\label\{cit:base\}([\s\S]*?)\\end\{cited\}',final).group(1).strip(),'status':'source statement verified','where_checked':'Q03_DEPOSIT_sources.md, S-P','depends_on':'P Theorem 1.1','notes':'Background; the post proves its algorithm independently.'})
        writer.writerow({'id':'Theorem A / supplied-return 1.1','statement':re.search(r'\\label\{thm:A\}([\s\S]*?)\\end\{maintheorem\}',final).group(1).strip(),'status':'proved as stated','where_checked':'Q03_DEPOSIT_report.md, Parts A and B (9.1-9.3)','depends_on':'9.1;9.2;9.3','notes':'Input exponent corrected to 60m^2+129m+2. Padded bound begins after parsing.'})
        writer.writerow({'id':'Theorem B','statement':re.search(r'\\label\{thm:B\}([\s\S]*?)\\end\{maintheorem\}',final).group(1).strip(),'status':'proved as stated','where_checked':'Q03_DEPOSIT_report.md, Part B (8.5)','depends_on':'2.9;7.3;8.2;8.3;8.4','notes':'Same statement as 8.5; no priority claim.'})
        for st in statements:
            sid=st['id']; src=source_map[sid]
            audit='Part A, Section 9' if sid.startswith('9.') else ('Part B, Sections 2-5.4' if tuple(map(int,sid.split('.')))<(5,5) else 'Part B, Sections 5.5-8.5')
            writer.writerow({'id':sid,'statement':st['kind']+' '+sid+' ('+st['title']+').\n'+st['statement'],
                'status':'definition checked' if st['kind']=='Definition' else 'proved as stated',
                'where_checked':'Q03_DEPOSIT_report.md, '+audit+', '+st['kind']+' '+sid,
                'depends_on':st['uses'],'notes':'S-P source counterpart: '+src['source_display']+'; '+src['source_locator']+'. '+src['note']})
    print(json.dumps({'proof_statements':len(statements),'csv_rows':len(statements)+3,'proof_steps':len(re.findall(r'\\step\{',combined)),
                      'post_bytes':len(final.encode()),'state_bound_renaming':'S in original Section9 -> calligraphic S; identity of numeric value B*N^m'},indent=2))


if __name__=='__main__':
    main()
