#!/usr/bin/env python3
"""Bounded source-to-source replacements of OS45 workflow/executable prose."""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
src=Path('/workspace/scratch/6c4e6df38b6d/S6_SERIES_GRIND_work/parts/IV.body.linked.tex')
s=src.read_text()
changes=[];missing=[]
def para(identifier,label,prefix,new):
    global s
    if s.count(prefix)!=1:
        missing.append({'id':identifier,'prefix_count':s.count(prefix)})
        return
    a=s.index(prefix);b=s.find('\n\n',a)
    if b<0:b=len(s)
    old=s[a:b]
    # Do not absorb a proof terminator that follows directly after a final paragraph.
    if '\\end{proof}' in old:
        old=old[:old.index('\\end{proof}')].rstrip()
    assert s.count(old)==1
    changes.append({'id':identifier,'statement_id':label,'operation':'replace_exact','old':old,'new':new,
                    'reason':'Replace obsolete workflow/absent-program prose by the actual displayed mathematical dependency or a present executable method/input/output statement. Historical source and check records are retained unchanged outside the paper.'})
    s=s.replace(old,new,1)

p116=r'\path{code/current_audits/audit_paper_i/iv_os45/code/k116_afterreading_exact.py}'
o116=r'\path{code/current_audits/audit_paper_i/iv_os45/output/k116_afterreading_exact.json}'
p117=r'\path{code/current_audits/audit_paper_i/iv_os45/code/k117_afterreading_exact.py}'
o117=r'\path{code/current_audits/audit_paper_i/iv_os45/output/k117_afterreading_exact.json}'
p119=r'\path{code/current_audits/audit_paper_i/iv_os45/code/k119_afterreading_exact.py}'
o119=r'\path{code/current_audits/audit_paper_i/iv_os45/output/k119_afterreading_exact.json}'

para('IV-K116-roadmap','night:P3K.116',r'\emph{Audit provenance.} The preparation-stage sentence in O45.7',r'''The three supporting arguments retain the original source,
Cartier modules, infinity period words and ordinary-cap reference.
They establish the joint disc family and its compactness,
then transfer its identity return through the actual scalar
and selected-fan morphisms.''')
para('IV-K116-execution-main','night:P3K.116',r'''The executable
\path{code/part3_fourfold/os45_marked_source_cover.py}''',r'''Exact rational arithmetic in
'''+p116+r'''
starts from the displayed source equation and the five literal
K10 matrices. Its 249 checks include the rational source and
translation inverses, chronological cusp Miller functions,
both point/O frames, original doubling at infinity,
the Hom-degree and Gram calculations, primitive period words,
a twelve-coset modular enumeration, and the integral
parabolic complexes for all four selected-zero choices.
The full matrices and results are in
'''+o116+r'''.
The joint chart maps and compactness argument above supply
the analytic disc extension and its return.''')
para('IV-K116-execution-peer','night:P3K.116',r'''The executable
\path{code/part3/os45_unselected_ii_blind_peer.py}''',r'''The source, Miller and integral-topology computations are
reproduced by
'''+p116+r'''.
The program uses exact rational functions, a full modular
coset enumeration, and Hermite and Smith normal forms;
the 249 checks and all four selected-site matrices are
recorded in
'''+o116+r'''.
The unrestricted fan extension and proper-disc conclusion
follow from the full character, ruling and compactness
maps proved above.''')
para('IV-K116-dependencies-heading','night:P3K.116',r'''\par\medskip\noindent\textbf{Completed construction and audit dependencies.}\par
The original K10 source construction''',r'''\par\medskip\noindent\textbf{Construction dependencies.}\par
The original K10 source is carried by its literal equation,
point line, selected whole zero and original ordinary cap.
The source and line morphisms above retain every cap and
period coefficient. The compact disc and scalar-interval
flows, with their inverses, give the physical return.''')
para('IV-K116-old-manifest','night:P3K.116',r'''The primary executable is
\path{code/part3_fourfold/os45_marked_source_cover.py}.''',r'''The exact arithmetic uses the displayed inputs and the
program and output named in O45.7 and O45P.7.
The two original Cartier frames, their overlap, the full
infinity theta shift, primitive period inverse, and cap
logarithm occur in the geometric arguments above.''')

para('IV-K117-review-notice','night:P3K.117','The original pending-review notice is retained below.',r'''The following source and line calculations feed the
compact trace, relative characteristic classes, physical
return and arbitrary-basis fan computation.''')
para('IV-K117-local-part-scope','night:P3K.117','This separate calculation uses the literal source and point-line maps',r'''SC45.1--4 constructs the selected-cusp source collar,
chronological Miller maps and full reflection arrows from
the literal source and point-line maps of O45.1--5.
C45.1--8 then constructs the compact trace, both normal-cap
comparison maps and the physical return.
The unselected-II disc theorem is \cref{night:P3K.116}.''')
para('IV-K117-source-reference','night:P3K.117','All SC45 formulas are retained. In particular the original height is',r'''All SC45 formulas are retained: the original height is
\(q=t-t_c\), the source chart is
\(y^2=X^2(X+c^2)+qH(q,X,c)\), and \(c=v/(2u)\).
The complete polynomial \(H\) is SC45.5.
The following argument supplies the compact trace,
full normal arrows, both cap framings, physical transfer
and fanwise products from those actual source functions.''')
para('IV-K117-main-checker','night:P3K.117','The exact local source checker SC45 and the accompanying completion',r'''The source and characteristic algebra is reproduced by
'''+p117+r'''.
It starts with the actual polynomial, chronological tangents,
coframes, period matrices and fan atoms. The output
'''+o117+r'''
records 288 named exact checks, 217 complete nine-variable
Gaussian prism solves and 868 full atom exponent round trips.
The complete geometric maps above establish the analytic
extension, orientations and unrestricted fan conclusion.''')
para('IV-K117-old-4514','night:P3K.117','The executed completion certificate passes 4,514 exact checks.',r'''The exact prism calculation in
'''+p117+r'''
solves 217 complete nine-variable systems on canonical paths
from \(j=-3,\ldots,3\) through word length five, and compares
their variations and derivatives with (C45.44).
Each nonvertical path starts with \(Q_0\).
The same output records 868 full atom exponent round trips
and the source, residue, quaternion, Chern and fifth-form
identities. These finite checks supplement the exact
terminating construction in C45.8, which proves the
unrestricted all-fan assertion.''')
para('IV-K117-local-peer-intro','night:P3K.117','The preceding independent local proof SCP45.1--4, in',r'''SCP45.1--4 gives the complete original polynomial,
chronological Miller maps, point and tensor frames,
inverse source translation and smooth-height theta reflection.
The following argument supplies the source disc, orbit,
normal, cap, relative-line and fan comparisons.
Every coefficient remains a function of the original height;
a central value is used only after its extending module map
has been established.''')
para('IV-K117-peer-program','night:P3K.117',r'''The independent checker is
\path{code/part3/os45_selected_cusp_completion_blind_peer.py}.''',r'''The exact program
'''+p117+r'''
uses the displayed source equations, conormal arrows,
period changes and complete fan atoms.
Its 288 named checks include the critical Jacobian,
both columns of the M\"obius differential, quaternion
and relative Chern identities, the full five-form collar,
native reset, and complete coefficient round trips.
Its 217 nine-variable Gaussian solves run from seven
signed vertical seeds through word length five.
The full results and matrices are in
'''+o117+r'''.''')
para('IV-K117-peer-history','night:P3K.117','The local 68-check proof is retained separately.',r'''The geometric proof retains the protected source and cap,
actual orbit pair, embedded link, point/O modules,
determinant and Hopf arrows, relative line and tangent maps,
and entire fan path. In particular the full
\(-2S\,dc\) column in (CP45.22) and the recovered-height
inverses (CP45.43), (CP45.46) are part of the maps.''')
para('IV-K117-final-manifest','night:P3K.117',r'''\par\medskip\noindent\textbf{Complete execution and provenance.}\par
The original local certificate''',r'''\par\medskip\noindent\textbf{Exact computational inputs and outputs.}\par
The 288 named checks, 217 full target solves and 868
atom coefficient round trips in
'''+p117+r'''
use the original source polynomial, integral period matrices,
complete atom exponent matrices, and relative characteristic
forms displayed above. Their exact output is
'''+o117+r'''.
The five supporting arguments give the source, compactness,
orientation and arbitrary-fan proofs in full.''')

para('IV-K119-local-stage-transition','night:P3K.119','The original five source matrices of K10\ngive a primitive image lattice',r'''The original five source matrices of K10 give
\(\sum_i\operatorname{im}(T_i^{-t}-I)=\ker\psi\)
as an integral lattice. OC45.6--11 realizes this equality
by explicit based preimages, extending source/point-line
arrows at all five fillings, a parameter-dependent Lie
cochain with its full logarithms, and the directed endpoint
square. Those maps carry the prescribed original cap
reference into the protected-cap family.''')
para('IV-K119-local-part-scope','night:P3K.119','This separate continuation preserves K116 and its complete unselected-II',r'''OC45.1--5 treats the original cap at \(t=0\) in the
OS45 source and constructs the local enlarged-cap filling
for the eighteen unselected points with its specified
extending period. OC45.6--11 supplies the integral and
analytic comparison for the complete prescribed reference
and all twenty-four points. OCP, OCGC and ORC give the
full lattice, global endpoint and proper-family arguments.''')
para('IV-K119-eighteen-part-scope','night:P3K.119','The current construction below treats the latter eighteen points.',r'''OC45.2--5 constructs the local enlargement for the
eighteen unselected-cap points. The six selected-cap
points retain the full rank-two selected/cap interaction
in OC45.2--4; OC45.6--11 treats both strata through the
protected-cap comparison.''')
para('IV-K119-OCP-intro','night:P3K.119','This independent calculation uses the five actual K10 matrices in',r'''Use the five original K10 matrices in the retained order
\((\psi,u,w,\delta)\). The following integral preimages
and directed analytic cochain map retain the full
parameter endpoint of the prescribed cap reference.''')
para('IV-K119-OCP-execution','night:P3K.119','The independent certificate re-inverts all twenty selected matrices,',r'''The exact program
'''+p119+r'''
re-inverts all twenty matrices for the four selected sites
and checks their products and primitive images.
It reconstructs the full 20-by-20 coordinate change and
inverse and the 20-by-36 mapping-cone boundary, including
the sign \(z_i=-t_i\). Together with the source, Miller,
Laurent and endpoint identities this gives 175 exact
checks, recorded in
'''+o119+r'''.''')
para('IV-K119-OCGC-intro','night:P3K.119','This is the complete geometric read of OC45.6-\\/-11 in',r'''The following argument proves the global source/line
comparison of OC45.6--11 and its full parameter endpoint.
It uses the local source and cap maps of OC45.1--5 and
the complete integral contraction of OCP.1--6.''')
para('IV-K119-ORC-intro','night:P3K.119','This independent root read covers all OC45.1-\\/-11, the complete original',r'''The following argument assembles the original source,
order-one positive-norm cap, full prescribed reference,
fixed scalar and selected integral fan.
The original five K10 matrices determine its integral
comparison; the displayed source, Cartier and endpoint
maps establish its extension and return.''')

# Headings carry mathematics, not the history of its checking.
for label,old,new in [
('night:P3K.116','O45.7. Independent exact execution','O45.7. Exact source and integral computations'),
('night:P3K.116','O45P.7. Independent exact execution and scope','O45P.7. Exact computations and geometric scope'),
('night:P3K.117','CP45.9. Independent execution and provenance','CP45.9. Exact source and fan computations'),
('night:P3K.119','OS45 prescribed-cap comparison: independent full global audit','OS45 prescribed-cap comparison: the full global maps'),
('night:P3K.119','OS45 ordinary-cap collisions: complete root geometric peer','OS45 ordinary-cap collisions: source, comparison and return')]:
    if s.count(old)==1:
        changes.append(dict(id='IV-OS45-heading-'+str(len(changes)),statement_id=label,operation='replace_exact',old=old,new=new,reason='Use the mathematical subject for the proof heading.'))
        s=s.replace(old,new,1)
    else:missing.append({'heading':old,'count':s.count(old)})

target=root/'execution_prose_patches.json'
target.write_text(json.dumps(changes,indent=2)+'\n')
(root/'execution_prose_receipt.json').write_text(json.dumps({
 'exact_changes':len(changes),'already_changed_or_missing':missing,
 'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'patch_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'scope':'Only the explicitly matched prose and headings; no statement, equation, chart or mathematical proof step deleted.',
 'history':'Original old/new paragraphs remain in this patch receipt and the immutable source; historical code counts are not attributed to the new execution.',
},indent=2)+'\n')
print(json.dumps({'exact_changes':len(changes),'already_changed_or_missing':missing},indent=2))
