"""Assemble Paper II after the independently recorded Paper I completion gate.

All canonical CDP source blocks retain their preceding definitions and full
proofs. This initial assembly is not a proof check or a delivery pass.
"""
from pathlib import Path
import re,json,hashlib
from paper_ii_transform import expand,namespace,normalize_equations,cdp_wrapper,raw_refs,replace_external_I,common_cleanup,iref
from statement_dependencies import add_uses
from paper_ii_credit_annotations import annotate,KNOWN

ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'deliverables';SRC=ROOT/'sources'
ED=OUT/'editorial';W=OUT/'work/cdp_audit'
assert (OUT/'records/I_final_validation.json').exists(), 'Required Paper I gate has not passed'
routes=json.loads((W/'paperII_source_routing.json').read_text())
manifest=[];blocks={};all_ids=[r['source_id'] for r in routes]

for letter in 'ABCDE':
    source=SRC/'returns/S6_03_CDP/build/ordered'/(letter+'.tex')
    s=source.read_text()
    markers=list(re.finditer(r'^% ([A-Z][\w.]*) from ([^\n]+)\n',s,re.M))
    for i,m in enumerate(markers):
        end=markers[i+1].start() if i+1<len(markers) else len(s)
        block=s[m.end():end]
        block=re.sub(r'^\\(?:sub)*section\*?\{[^\n]*\}\s*\n?','',block,flags=re.M)
        blocks[m[1]]=block
        manifest.append({'source_id':m[1],'canonical_source':str(source.relative_to(ROOT)),
                         'original_fragment':m[2],'source_block_sha256':hashlib.sha256(block.encode()).hexdigest(),
                         'source_char_range':[m.end(),end]})
assert len(blocks)==239 and set(blocks)==set(all_ids),(len(blocks),set(all_ids)-set(blocks))

# Full corrected blocks replace only the original statement/proof interval;
# all definitions preceding that interval remain in the canonical block.
replacements={}
for file in ['corrected_A1_1_A2_6_full_proofs.tex','corrected_C4g_full_proof.tex','corrected_C2c_full_proof.tex','corrected_E6_full_proof.tex']:
    text=(W/file).read_text();starts=list(re.finditer(r'\\begin\{statement\}\{([^}]+)\}',text))
    for i,m in enumerate(starts):
        end=starts[i+1].start() if i+1<len(starts) else len(text)
        block=text[m.start():end]
        # Omit trailing source comments, never adjacent mathematical text.
        replacements[m[1]]=block
        original=blocks[m[1]];start=original.index('\\begin{statement}')
        blocks[m[1]]=original[:start]+block

# UN40 proves that the only compact curves for multiplicatively independent
# multipliers are the two axes. State explicitly the consequence used in UN41.
un41=blocks['C.2.UN.41']
closing=un41.rfind('\\end{proof}')
assert closing>=0
un41_addition=r'''The curve calculation in C.2.UN.40 leaves only the two axes when
the multipliers are multiplicatively independent. A nonconstant meromorphic
function would have infinitely many distinct nonempty generic level divisors,
which is impossible when the only compact curves are those two axes.
Consequently the Hopf component in this case has algebraic dimension zero.

'''
blocks['C.2.UN.41']=un41[:closing]+un41_addition+un41[closing:]

sections={}
for r in routes:
    sid=r['source_id'];group=r['proposed_section']
    if sid in KNOWN:group='A'
    if group=='I':continue
    s=expand(blocks[sid],'S6_03_CDP')
    s=namespace(s,'cdp')
    s,tags=normalize_equations(s,'cdp')
    s=cdp_wrapper(s)
    s=raw_refs(s,all_ids)
    s=common_cleanup(s)
    s=annotate(s,sid)
    sections.setdefault(group,[]).append((r,s))
    (ED/('II_cdp_'+sid.replace('.','_')+'.tex')).write_text(s)

body=[]
for group in [f'{n:02d}' for n in range(1,15)]:
    items=sorted(sections[group],key=lambda x:x[0]['section_local_order'])
    title=items[0][0]['section_title']
    if title.startswith('Unrestricted Euler topology, component covers'):
        title='Unrestricted Euler topology and component covers'
    body.append('\\section{'+title+'}\\label{sec:II:'+group+'}\n')
    body.extend(s for r,s in items)

push=(OUT/'work/root/push_E2_stability_for_II.tex').read_text()+'\n'+(OUT/'work/root/push_E5_for_II.tex').read_text()
def push_open(m):
    env,title=m[1],m[2];q=re.match(r'([A-F]\.\d+\.\d+)\s*\(([^)]+)\):?\s*(.*)',title)
    if not q:q=re.match(r'([A-F]\.\d+\.\d+);\s*([^;]+);\s*(.*)',title)
    if not q:return m[0]
    return '\\begin{'+env+'}['+q[3]+']\\label{push:src:'+q[1]+'}'
push=re.sub(r'\\begin\{(theorem|proposition|corollary|lemma|remark|problem)\}\[([^\]]+)\]',push_open,push)
push_ids=set(re.findall(r'\\label\{push:src:([^}]+)\}',push))
push_ids.update(re.findall(r'\\newlabel\{push:src:([^}@]+)\}',(OUT/'S6_09_PAPERS_I.aux').read_text()))
push=raw_refs(push,push_ids,'push:src:')
body.append('\\section{Connected deformation chains and two independent periods}\\label{sec:II:push-stability}\n'+common_cleanup(push))

inv=(SRC/'returns/S6_01_INVARIANTS/fragments/part_E.tex').read_text()
inv=re.sub(r'^\\section\{[^\n]+\}\n','',inv,flags=re.M)
# The tangent tuple is already stated in E15. Its distinct full computation
# remains here alongside the canonical, direct-image and Hodge conclusions.
inv=inv.replace(r'''Moreover
\[
 \boxed{h^\bullet(T_{X_m})=(2m+1,8m+1,6m+1,0).}       \tag{E.4}
\]
More precisely,''',r'''The tangent cohomology is that of Proposition~\ref{CDP-E15}.
The following proof gives a distinct calculation of those dimensions.
More precisely,''')
# Preserve (E.4) as a source-to-print reference to the single shared statement.
inv=inv.replace('(E.4)',r'Proposition~\ref{CDP-E15}')
known_start=inv.index(r'\begin{claim}{E2.1}')
known_end=inv.index(r'\begin{claim}{E2.2}',known_start)
inv_known=inv[known_start:known_end]
inv=inv[:known_start]+inv[known_end:]
inv=inv.replace(r'''its exact number of sections, or the obstruction map of the comb
member. These parts of E.2 are unfinished.''',r'''or its exact number of sections. This splitting calculation is unfinished.
The Kuranishi germ and its vanishing obstruction map are established by
Proposition~\ref{CDP-E15}.''')
inv=inv.replace(r'''The comb Kuranishi problem further requires
its actual bracket and higher obstruction maps; the dimensions in
Proposition~\ref{CDP-E15} do not determine those maps.''',r'''The tangent dimensions alone do not determine obstruction maps.
The complete period-section family and its tangent isomorphism in
Proposition~\ref{CDP-E15} establish that the Kuranishi ideal is zero.''')
inv=inv.replace(r'''section, together with that member's obstruction map.''',r'''section.''')
inv=inv.replace(r'''remaining calculation or for its Kuranishi bracket.''',r'''remaining bundle-splitting calculation.''')
inv=inv.replace('The remaining comb splitting and deformation calculations','The remaining comb bundle splitting')
def inv_convert(s):
    s=namespace(s,'inv')
    s=s.replace(r'\ref{inv:CDP-E15}',r'\ref{cdp:st:E15}')
    s=s.replace('\\begin{claim}{','\\begin{statement}{').replace('\\end{claim}','\\end{statement}')
    s=cdp_wrapper(s).replace(r'\label{cdp:st:E',r'\label{inv:E')
    s=raw_refs(s,['E1.1','E2.1','E2.2','E2.3','E2.4','D3.1','D1.1','D1.2','D1.3'],'inv:')
    s,_=normalize_equations(s,'invII')
    return s
inv=inv_convert(inv)
inv_known=inv_convert(inv_known)
# The source explicitly open Km question is separated, with its complete
# partial proof. The checked E15 result will correct its stale Kuranishi clause.
start=inv.index('\\begin{problem}')
end=inv.index('\\begin{proposition}',start)
openpart=inv[start:end]
inv=inv[:start]+inv[end:]
body.append('\\section{Comb invariants and the precise vector-field correction}\\label{sec:II:combs}\n'+common_cleanup(inv))

body.append('\\appendix\n\\section{Known source results re-derived}\\label{app:II:known}\n')
body.extend(s for r,s in sorted(sections['A'],key=lambda x:x[0]['section_local_order']))
body.append(common_cleanup(inv_known))
uniform=(OUT/'work/invariants_arithmetic/working_uniform_nontorsion_for_II.tex').read_text()
uniform=uniform.replace('wb:cor:picard-line-audit','inv:C3.1').replace('wb:thm:structure-direct-images-audit','inv:A1.0').replace('wb:lem:finite-normal-order-audit','wb:ffcert:thm:normal-trivialization')
uniform=re.sub(r'\\beta\b',lambda m:r'\beta_c',uniform)
uniform=uniform.replace('The marked period\nfunctions are',r'Here $\beta_c=\beta^{\rm part}+c$ for the fixed family member; the letters $a,b,c,d$ within the integral-class calculation are local integer coefficients. The marked period'+'\nfunctions are')
body.append(common_cleanup(uniform))
supplement=ED/'II_working_supplement.tex'
if supplement.exists():body.append(supplement.read_text())
for name in ['II_result_index','II_programs']:
    p=ED/(name+'.tex')
    if p.exists():body.append(p.read_text())
body.append('\\clearpage\\part{Questions not established by the present arguments}\n'+common_cleanup(openpart)+'\n'+(ED/'II_comb_remaining_analysis.tex').read_text())
joined=replace_external_I('\n'.join(body))
# Canonical statement aliases identify the shared statement, not a repeated proof.
if (W/'working_supplement_mapping.json').exists():
    mapping=json.loads((W/'working_supplement_mapping.json').read_text())
    for item in mapping['canonical_alias_insertions']:
        target=r'\label{'+item['insert_at']+'}'
        alias=r'\label{'+item['alias']+'}'
        assert target in joined, item
        if alias not in joined:joined=joined.replace(target,target+alias,1)
joined=add_uses(joined,'II')

pre=(ED/'shared_preamble.tex').read_text()
pre=pre.replace('S6_09_PAPERS_I','S6_09_PAPERS_II').replace('Paper I}','Paper II}')
pre=re.sub(r'% statement_plain:.*','% statement_plain: Cotangent torsion, corrected vanishing criteria, compact torus-fibred constructions and deformation stability.',pre)
pre=re.sub(r'% main_statements:.*','% main_statements: cdp:st:A.1.1, cdp:st:B1, cdp:st:C4a, cdp:st:E6, cdp:st:E15',pre)
pre=re.sub(r'% open_points:.*','% open_points: exact Km splitting of a specified smoothed comb section',pre)
pre=re.sub(r'% known_before:.*','% known_before: AC26 CDP20 contradiction; Greuel-Schulze inverse-Jacobian criterion; Viaclovsky comb and two-parameter constructions; classical surface and deformation inputs at exact cited scope.',pre)
pre=re.sub(r'% hard_step:.*','% hard_step: exact torsion connecting maps, actual compact analytic occurrence, full-fibre restrictions, and Artin-to-analytic stability over nonreduced bases.',pre)
pre=re.sub(r'% course_(?:continuation|prerequisite):.*\n','',pre)
pre=pre.replace(r'\fancyhead[L]{\small The $(3,4,\infty)$ family}',r'\fancyhead[L]{\small Torus-fibred compact complex threefolds}')
pre=pre.replace('pdftitle={The (3,4,infinity) family of complex structures on S6: periods, moduli and the ends of the disc}',
                'pdftitle={Torus-fibred compact complex threefolds: cotangent torsion, vanishing criteria and deformation stability}')
pre+='\n'+(ED/'II_extra_preamble.tex').read_text()
pre+=r'\renewcommand{\Uses}[1]{\par\smallskip\begingroup\raggedright\noindent\textit{Uses:} #1.\par\endgroup\smallskip}'+'\n'
front=(ED/'II_front.tex').read_text();back=(ED/'II_back.tex').read_text()
bp=ED/'II_bibliography.tex'
if bp.exists():back=re.sub(r'\\bibliographystyle\{[^}]+\}\s*\\bibliography\{[^}]+\}',lambda m:bp.read_text(),back)
text=pre+'\n\\begin{document}\n'+front+'\n'+joined+'\n'+back+'\n\\end{document}\n'
(OUT/'S6_09_PAPERS_II.tex').write_text(text)
(OUT/'work/root/II_assembly_manifest.json').write_text(json.dumps({'canonical_blocks':manifest,'full_replacement_ids':sorted(replacements),'source_ids':all_ids,'working_supplement_present':supplement.exists(),'stage':'complete-source assembly, mathematical and layout validation separate'},indent=2)+'\n')
print('Paper II candidate:',len(text),'characters;',len(blocks),'canonical blocks; supplement=',supplement.exists())
