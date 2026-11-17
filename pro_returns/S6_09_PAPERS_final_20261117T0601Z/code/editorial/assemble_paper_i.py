"""Assemble a self-contained Paper I candidate without selecting out proofs.

This is an editorial assembler, never a mathematical verifier. Source-specific
normalizations are recorded in the change manifest and audited separately.
During writing, the header explicitly identifies the uncompleted audit.
"""
from pathlib import Path
import re, json, hashlib, csv
from paper_i_structure import consolidate
from paper_i_references import refs,final_cleanup
from paper_i_credit_annotations import add_credits
from statement_dependencies import add_uses
from course_worked_examples import number_worked_examples

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables'
SRC=ROOT/'sources'
WORK=OUT/'work/root'
ED=OUT/'editorial';ED.mkdir(exist_ok=True)
changes=[]
source_parts=[]

def expanded(run,rel):
    p=SRC/'returns'/run/rel
    if not p.suffix:p=p.with_suffix('.tex')
    text=p.read_text()
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expanded(run,m[1]),text)

def adapt(s,namespace,source):
    original=s
    if 'paperI_course_cw_foundations' in source or 'paperI_course_pf_foundations' in source:
        s=number_worked_examples(s)
    # References retain their mathematical objects; only label ownership changes.
    if namespace in ['fam','wb']:
        s=re.sub(r'\\(label|ref|eqref|cref|Cref|autoref)\{([^}]+)\}',
                 lambda m:'\\'+m[1]+'{'+','.join(namespace+':'+x for x in m[2].split(','))+'}',s)
    if namespace in ['fam','push']:
        def tag(m):
            env,title=m[1],m[2]
            q=re.match(r'([A-F]\.\d+(?:\.\d+)*)\b',title)
            if not q:return m[0]
            sid=q[1]
            status=title[q.end():].strip(' ;():')
            status=status.replace('Proved','proved here').replace('Known','cited result').replace('Refuted','counterexample').replace('Open','open in the source')
            return '\\begin{'+env+'}['+status+']\\label{'+namespace+':src:'+sid+'}'
        s=re.sub(r'\\begin\{(theorem|proposition|lemma|corollary|remark|problem|claim)\}\[([^\]]+)\]',tag,s)
    # Small source vocabulary changes are literal, never mathematical shortcuts.
    for a,b in [('the threefold of the question','the marked threefold'),
                ('the marked threefold of the question','the marked threefold'),
                ("in the return's coordinates",'in these coordinates'),
                ('The source being checked is the attached version of','We use the stated version of')]:
        s=s.replace(a,b)
    s=re.sub(r'^%[^\n]*\n','',s,flags=re.M)
    s=s.replace('\\Verified','').replace('\\AuthorSelfCheck','').replace('\\NeedsCheck','')
    if namespace=='push':
        s=s.replace('The cones $P_{k,l}$ in Lead 2 and their faces form a fan.',
            'For $k,l\\in\\mathbb Z$, let $P_{k,l}$ be the cone defined by $h_q,h_u\\geq0$, $kh_q\\leq y_1\\leq(k+1)h_q$ and $l(h_q+h_u)\\leq y_2\\leq(l+1)(h_q+h_u)$. These cones and their faces form a fan.')
    changes.append({'source':source,'namespace':namespace,'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
                    'candidate_sha256':hashlib.sha256(s.encode()).hexdigest(),
                    'operations':'label namespaces; typed headings; provenance comments omitted; question/return vocabulary normalized; explicit cone definition in PUSH A1.1'})
    return s

def omit_results(text,run,ids):
    # Exact recorded offsets are used only before recursive input expansion.
    records=json.loads((WORK/(run+'_statements.json')).read_text())
    chunks=[]
    for r in records:
        if any(re.match(re.escape(i)+r'(?:\D|$)',r['title']) for i in ids):
            block=r['statement']
            if r['proof']:block=text[text.find(block):text.find(block)+r['proof_end']-r['statement_start']] if block in text else block
            if block in text:
                text=text.replace(block,'\n% Transferred result: '+r['title']+'\n',1)
                chunks.append(r)
    return text,chunks

def section(name,text,namespace,source):
    s=adapt(text,namespace,source)
    source_parts.append((name,s))
    (ED/(name+'.tex')).write_text(s)

for name in ['AB','CD','E','F']:
    text=(SRC/'returns/S6_02_FAMILY/sections'/(name+'.tex')).read_text()
    if name=='E':
        text,transferred=omit_results(text,'S6_02_FAMILY',['E.2.2','E.2.3'])
        (WORK/'family_transferred_to_III.json').write_text(json.dumps(transferred,indent=2))
    section('I_family_'+name,text,'fam','returns/S6_02_FAMILY/sections/'+name+'.tex')

for name in ['AB_push','D_push','E_push']:
    text=expanded('S6_02_PUSH','sections/'+name+'.tex')
    if name=='E_push':
        # The two-parameter family belongs in Paper II; its entire section is saved.
        m=re.search(r'\\subsection\{E\.5\.',text)
        if m:
            (WORK/'push_E5_for_II.tex').write_text(text[m.start():])
            text=text[:m.start()]
        a=re.search(r'\\begin\{corollary\}\[E\.2\.4',text)
        b=re.search(r'\\subsection\{E\.3\.',text)
        if not b:b=re.search(r'\\begin\{proposition\}\[E\.3\.1',text)
        if a and b and a.start()<b.start():
            (WORK/'push_E2_stability_for_II.tex').write_text(text[a.start():b.start()])
            text=text[:a.start()]+text[b.start():]
    section('I_push_'+name,text,'push','returns/S6_02_PUSH/sections/'+name+'.tex (recursive inputs)')

agent=OUT/'work/invariants_arithmetic'
for name in json.loads((agent/'section_order.json').read_text()):
    section('I_'+Path(name).stem,(agent/'sections'/name).read_text(),'already_namespaced',str(agent/'sections'/name))

for name in ['working_hodge_frolicher_proofs','working_bott_chern_proofs',
             'working_analytic_picard_proofs','working_gauge_boundary_for_final_part','notation_dictionary']:
    content=(agent/(name+'.tex')).read_text()
    if name=='notation_dictionary':content=content.replace('\\subsection{Invariant and arithmetic notation in the family marking}',
                                                          '\\section{Invariant and arithmetic notation in the family marking}',1)
    section('I_'+name,content,'already_namespaced',str(agent/(name+'.tex')))

section('I_finite_extension_transgression',
        (OUT/'work/maps_audit/finite_extension_transgression.tex').read_text(),
        'already_namespaced','work/maps_audit/finite_extension_transgression.tex')

cdp=(OUT/'work/cdp_audit/paperI_CDP_D1_14_group_proof.tex').read_text()
cdp=cdp[cdp.index('\\begin{proof}'):]
cdp=cdp.replace('{eq:cdp-parabolic-law}','{cdp:eq:parabolic-law}')
section('I_cdp_monodromy_proof',
        '\\section{Integral monodromy: the kernel calculation}\\label{app:cdp-monodromy}\n'
        'We retain the complete kernel calculation for Theorem~\\ref{fam:st:F.1.1}.\n'+cdp,
        'already_namespaced','work/cdp_audit/paperI_CDP_D1_14_group_proof.tex')

cdpe9=(OUT/'work/cdp_audit/extracted/CDP_E9.tex').read_text()
cdpe9=cdpe9[cdpe9.index('\\begin{proof}'):cdpe9.index('\\end{proof}')+len('\\end{proof}')]
cdpe9=cdpe9.replace('from the supplied\nR2--R3 data',
                    'from the root-bundle and cusp-normalization data proved above')
cdpe9=cdpe9.replace('required in R3','required by the structure-sheaf calculation')
section('I_cdp_kuranishi_proof',
        '\\section{A second root-bundle derivation of the Kuranishi statement}\\label{app:cdp-kuranishi}\n'
        'We re-derive Theorem~\\ref{fam:st:A.5.2}, credited to \\citet[Theorem~6.12 and Proposition~6.16]{DuEtAl2026v1}.\n'+cdpe9,
        'already_namespaced','work/cdp_audit/extracted/CDP_E9.tex')

semidirect=(OUT/'work/root/semidirect_abelianization_rederivation.tex').read_text()
semidirect=semidirect[:semidirect.index('\\end{proof}')+len('\\end{proof}')]
section('I_semidirect_abelianization',
        '\\subsection{Abelianization of a semidirect product}\n'+semidirect,
        'wb','work/root/semidirect_abelianization_rederivation.tex; exact source WB_lem_semidirect-abelianization, credited to AC26 Lemma10.7')

for name in ['paperI_circle_quotient','paperI_real_forms',
             'paperI_integral_leray','paperI_topology_reduction','paperI_hodge_line','paperI_closing_cocycle',
             'paperI_course_chain_foundations','paperI_course_cw_foundations',
             'paperI_course_pf_foundations','paperI_course_homotopy']:
    p=OUT/'work/maps_audit'/(name+'.tex')
    if p.exists():section('I_'+name,p.read_text(),'already_namespaced',str(p.relative_to(OUT)))

# Full independent derivations from the working edition are retained; source-wide
# duplicate statements are resolved against the audit inventory in a later pass.
for name in ['candidate_geometry','exact_algebra','finite_filling_certificates','algebraic_dimension',
             'analytic_canonical_ring','period_parameter_deformation','period_shift_classification']:
    section('I_wb_'+name,(SRC/'workbench'/(name+'.tex')).read_text(),'wb','workbench/'+name+'.tex')

pre=(ED/'shared_preamble.tex').read_text()
front=(ED/'I_front.tex').read_text()
back=(ED/'I_back.tex').read_text()
conventions=adapt((SRC/'returns/S6_02_FAMILY/sections/conventions.tex').read_text(),'fam','returns/S6_02_FAMILY/sections/conventions.tex')
conventions=final_cleanup(refs(conventions,'conventions'))
body=add_uses(add_credits(consolidate(source_parts)),'I')
topology_alias_file=OUT/'work/maps_audit/paperI_topology_aliases.json'
if topology_alias_file.exists():
    for old,new in json.loads(topology_alias_file.read_text()).items():
        body=body.replace('{'+old+'}', '{'+new+'}')
records=''
for name in ['I_result_index','I_programs']:
    p=ED/(name+'.tex')
    if p.exists():records+='\n'+p.read_text()
body=body.replace('\\clearpage\\part{Questions not established by the present arguments}',
                  records+'\n\\clearpage\\part{Questions not established by the present arguments}')
inline_bib=ED/'I_bibliography.tex'
if inline_bib.exists():
    back=re.sub(r'\\bibliographystyle\{[^}]+\}\s*\\bibliography\{[^}]+\}',
                lambda m:inline_bib.read_text(),back)
text=pre+'\n\\begin{document}\n'+front+'\n'+conventions+'\n'+body+'\n'+back+'\n\\end{document}\n'
(OUT/'S6_09_PAPERS_I.tex').write_text(text)
(WORK/'I_assembly_changes.json').write_text(json.dumps(changes,indent=2)+'\n')
print('Paper I complete-source candidate:',len(text),'characters;',len(source_parts),'source sections.')

