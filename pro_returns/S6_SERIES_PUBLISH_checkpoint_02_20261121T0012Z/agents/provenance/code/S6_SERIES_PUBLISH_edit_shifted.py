#!/usr/bin/env python3
"""Guarded editorial changes to V's shifted-product part; records every edit."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'S6_SERIES_PUBLISH_V_shifted_original.tex'
text = SOURCE.read_text()
original = text
changes = []

def location(s, pos):
    opening = re.match(r'\\begin\{(?:theorem|proposition|corollary|lemma)\}(?:\[[^\]]*\])?[^\n]*\\label\{(maps:src:[^}]+)\}', s[pos:])
    if opening:
        return opening.group(1)
    labels = list(re.finditer(r'\\label\{(maps:src:[^}]+)\}', s[:pos]))
    return labels[-1].group(1) if labels else 'sec:shifted'

def change(old, new, kind, reason):
    global text
    if text.count(old) != 1:
        raise ValueError(f'Expected one match, got {text.count(old)}: {old[:180]}')
    at = text.index(old)
    changes.append({'type':kind,'location':location(text,at),
                    'old_pdf_page':'root to fill from corrected baseline',
                    'new_pdf_page':'root to fill after final pagination',
                    'old_text':old,'new_text':new,'reason':reason})
    text = text.replace(old,new,1)

programs = []
for m in re.finditer(r'\\texttt\{([^}]*\.py)\}', original):
    name = m.group(1).replace(r'\_', '_')
    before = original[max(0,m.start()-650):m.start()]
    url = re.search(r'\\href\{([^}]+)\}\{$', before)
    programs.append({'filename':name,'location':location(original,m.start()),
                     'retained_url':url.group(1) if url else '',
                     'disposition':'program table/check record; proof retains inputs, method and mathematical result'})

# References to production activity are replaced by the mathematical operation.
edits = [
('$(1,1,1,1,1)$, as printed in the code, proving $G_{\\rm ab}=\\mathbb Z$.',
 '$(1,1,1,1,1)$ by integral row and column operations, proving $G_{\\rm ab}=\\mathbb Z$.','D09','State the exact Smith calculation without a production reference.'),
('To verify this without a matrix-size guess, the local invariant\npolynomials of the first factor are',
 'The local invariant polynomials of the first factor are','D02','Remove an unsupported contrast while retaining the displayed calculation.'),
('The exact program forms these matrices and takes their ranks.',
 'Row reduction of these exterior-product matrices gives the displayed ranks.','D09','Keep the computational inputs and method in mathematical form.'),
('proper smooth submersion: transversality was checked pointwise\nabove.',
 'proper smooth submersion by the pointwise transversality above.','D08','State the mathematical reason for the submersion.'),
('The identification follows by an\nrelative diffeomorphism',
 'The identification follows by a\nrelative diffeomorphism','D23','Correct the article without changing the assertion.'),
('The program \\texttt{fourfolds\\_shifted\\_integral.py} realizes\nthis as an eighteen-row integer presentation; its Smith form\nhas eleven unit factors and seven factors twelve.',
 'The eighteen-row integer presentation of these covering cokernels has\nSmith form with eleven unit factors and seven factors twelve.','D09','State the integer presentation and result; move its program to the index.'),
('This argument does not determine the extensions in the\nhigher integral Leray filtrations.\n',
 '','D02','Remove a limitation unrelated to the stated H2 result; the next theorem determines full homology.'),
('\\item The executable \\texttt{manifolds\\_shifted\\_mv.py} constructs\nthe exterior bases, the four adjoint maps \\eqref{maps:eq:E.MV6}, and the full\nmatrices \\eqref{maps:eq:E.MV7}--\\eqref{maps:eq:E.MV8}. Exact Smith reduction gives the table\nbelow.',
 '\\item In the exterior bases, exact Smith reduction of the four\nadjoint maps \\eqref{maps:eq:E.MV6} and the full matrices\n\\eqref{maps:eq:E.MV7}--\\eqref{maps:eq:E.MV8} gives the following table.','D09','Retain the exact computational procedure and table.'),
('An exponent $[r]$ records repetition, not an integer power.',
 'The notation $a^{[r]}$ denotes $r$ entries equal to $a$.','D02','Give the notation directly.'),
('These assertions and \\ref{maps:src:E.2.6} do not identify the complete smooth\nstructure from its ordinary homology and fundamental group.\n',
 '','D02','Remove a defensive claim outside the proposition; the smooth-type theorem is retained.'),
('\\item The program \\texttt{shifted\\_group\\_bordism.py} does the group-matrix and Euler calculations.\n',
 '','D09','Move this verification-only item to the check/program record; all preceding calculations stay.'),
('\\item The program \\texttt{maps\\_shifted\\_pi2.py} checks the simultaneous\ncontraction kernel, the three homological boundary coordinates,\nand the exact-order-twelve image certificate for all sixteen\nindependent boundary-adjoint sign choices in \\ref{maps:src:E.2.6}.\n',
 '','D09','Move the verification-only item to the program/check record; the contraction and image derivations stay.'),
(' The matrix computation is done by the program \\texttt{manifolds\\_cusp\\_alexander.py}.',
 '','D09','The displayed unimodular matrices already give the complete operation.'),
('Use the smooth map $c=(e_1,e_2):P\\to N$ in \\ref{maps:src:E.2.9},\nnot an arbitrary representative of its classifying homotopy\nclass.',
 'Use the smooth map $c=(e_1,e_2):P\\to N$ constructed in \\ref{maps:src:E.2.9}.','D02','Name the required smooth representative positively.'),
('\\item The circle Euler number can be fixed without an ambiguous\nSeifert sign convention.',
 '\\item We compute the circle Euler number in the following orientation convention.','D02','Retain the full connection form and orientation calculation.'),
('\\item The integral character, cone orders, primitive kernel basis and Euler calculation are computed by the program \\texttt{maps\\_shifted\\_circle.py}.\n',
 '','D09','Move verification metadata; the preceding derivation remains.'),
('All entries\nare computed by exterior products of \\eqref{maps:eq:E.S38} in\n\\texttt{maps\\_shifted\\_return.py}.',
 'These entries result from exterior products of \\eqref{maps:eq:E.S38}\nand row reduction of the induced contraction maps.','D09','State inputs, method and output in place of a program name.'),
('The program\n\\texttt{maps\\_shifted\\_cover.py} computes \\eqref{maps:eq:E.S41}--\\eqref{maps:eq:E.S43}\nover the exact cyclotomic fields, represented by rational\ncompanion matrices. It prints every local fixed dimension.',
 'For \\eqref{maps:eq:E.S41}--\\eqref{maps:eq:E.S43}, represent the\ncyclotomic fields by rational companion matrices and compute each local\nfixed space by exact row reduction.','D09','Keep the exact cyclotomic algorithm while removing implementation narration.'),
('This also\nindependently checks the direct variation ranks \\eqref{maps:eq:E.S39}.',
 'This agrees with the direct variation ranks \\eqref{maps:eq:E.S39}.','D08','State agreement of mathematical calculations.'),
('The full integer matrices and the exact\nHermite/Smith check are in\n\\texttt{maps\\_shifted\\_cover\\_integral.py}.',
 'The integer matrices are determined by the Hermite image bases in\n\\eqref{maps:eq:E.S53}; their Smith reductions give the displayed invariants.','D09','Replace a file citation by the reconstructible matrix procedure.'),
('These computations are performed, with the\nunimodular transforms verified, in\n\\texttt{maps\\_shifted\\_fibre\\_integral.py}.',
 'The reductions use the integral unimodular Smith transforms.','D09','Retain the integral change-of-basis requirement.'),
('Thus $72$ is the divisibility in the whole cohomology\ngroup, not just in a chosen sublattice.',
 'Thus the divisibility in the whole cohomology group is $72$.','D02','Keep the conclusion already justified by primitivity.'),
('Its entries and unit cancellations are computed exactly by the program \\texttt{maps\\_complement\\_module.py}, in the integral normal form $h^r$ times an alternating word in\n$a,a^2$ and $b,b^2,b^3$.',
 'Write its group-ring entries in the integral normal form $h^r$ times\nan alternating word in $a,a^2$ and $b,b^2,b^3$; exact unit\ncancellations use multiplication in that normal form.','D09','Retain the specified exact group-ring algorithm.'),
('exactly the coefficient2 in', 'exactly the coefficient $2$ in','D23','Repair missing whitespace and math delimiters.'),
('has deck image1.', 'has deck image $1$.','D23','Repair missing whitespace and math delimiters.'),
('Its remaining components are exactly (E.C19).',
 'Its remaining components are exactly \\eqref{maps:eq:E.C19a}--\\eqref{maps:eq:E.C19b}.','D06','Replace a literal equation number by the existing labels.'),
('The subsequent seven-generator\nblock changes therefore give',
 'The seven-generator block changes therefore give','D08','Remove editorial sequence wording; retain the same basis change.'),
('Formula \\eqref{maps:eq:E.T2}, not merely the induced map\nof zero sections, specifies the normal framing of each plumbing.',
 'The full coordinate map \\eqref{maps:eq:E.T2} specifies the normal\nframing of each plumbing.','D02','Specify exactly which morphism carries the framing.'),
('After three crossings the same coordinates return, not just\nthe same unframed planes.',
 'The threefold composition is the identity on the ordered coordinates.','D02','State the exact coordinate identity used in the next sentence.'),
('the normal meridian is $v_j-m_j\\rho_j$, not the base meridian.',
 'the normal meridian is $v_j-m_j\\rho_j$.','D02','Keep the explicit peripheral morphism.'),
('The expanded lists of all $76$ and $2432$ handles are produced by the program \\texttt{maps\\_ordinary\\_handles.py}.',
 'Expanding these polynomials gives $76$ handles in dimension six\nand $2432$ in dimension ten.','D09','State the polynomial computation rather than a program output.'),
('\\item For completeness the handle expansion rule is itself a\ngeometric equality.',
 '\\item The handle expansion rule follows from the product decomposition\nof the parameter circles.','D08','State the mechanism of the ensuing proof.'),
('This is an identification by explicit full-dimensional\nembeddings of ordinary handles.  \\item The exponent matrices, endpoint placements, angular rotations, sector seams, total linear monodromy and handle lists are checked by the program \\texttt{maps\\_ordinary\\_handles.py}; the handle counts give Euler numbers $2$ and $0$.',
 'The handle polynomials evaluated at $-1$ give Euler numbers $2$ and $0$.','D09','Move implementation verification to records while keeping the Euler conclusions.'),
('\\item We finish by stating precisely why these data determine the smooth\ntype, including its top handles.',
 '\\item The following relative uniqueness theorems determine the smooth\ntype from the full attaching embeddings.','D08','Remove a closing recapitulation and state the mathematical input.'),
('$S^{j-1}\\times D^{n-j}\\longrightarrow\\partial W$, not just\nthe attaching sphere or its homology class.',
 '$S^{j-1}\\times D^{n-j}\\longrightarrow\\partial W$.','D02','The preceding sentence already specifies the whole characteristic embedding.')
]
for old,new,kind,reason in edits:
    change(old,new,kind,reason)

# Longer passages with repository links: preserve the operation and move the link.
old = re.search(r'The program \\href\{[^}]+maps_splice_module\.py\}\{\\texttt\{[^}]+\}\} checks both\nperipheral chain equations and \$d_2d_3=0\$, cancels\nthe indicated unit pairs, and reduces \\eqref\{maps:eq:E.P14\} to\n16 generators and52 nonzero columns\. It computes\nin the amalgam',text).group(0)
change(old,'The peripheral chain equations and $d_2d_3=0$ hold by multiplication\nof their group-ring matrices. Cancelling the indicated unit pairs reduces\n\\eqref{maps:eq:E.P14} to $16$ generators and $52$ nonzero columns.\nThe calculation takes place in the amalgam','D09','Preserve the exact matrix calculation over the specified group ring.')
change('not in a finite quotient. To specify its normal\nform,','whose normal form is specified as follows:','D02','The exact group ring has already been specified.')
change('These elementary word\noperations are implemented exactly, including\nboth central exponents.','These word operations track both central exponents.','D09','Describe the algebraic operation directly.')
old=re.search(r'The other\ncoordinates vanish\.  The program\n\\href\{[^}]+maps_cusp_quadratic\.py\}\{\\texttt\{[^}]+\}\} checks these identities\nusing the identical integral group-ring cancellations as\n\\ref\{maps:src:E.2.16\}\.',text).group(0)
change(old,'The other coordinates vanish. These identities follow by applying\nthe integral group-ring cancellations of \\ref{maps:src:E.2.16} to\nthe displayed cusp-cycle columns.','D09','Retain the cusp-cycle map and its exact algebraic derivation.')
change('the quadratic image\nis then $-48q(v)$, consistent with the degree-two cup\nsquare evaluated on the normalization; this is a check,\nnot the proof of \\eqref{maps:eq:E.Q1}.',
       'the quadratic image\nis then $-48q(v)$, equal to the degree-two cup square evaluated\non the normalization.','D02','Retain the numerical comparison as mathematics.') if 'the quadratic image\nis then' in text else None
# In the supplied source the sentence begins with capital The after a period.
if 'this is a check,\nnot the proof' in text:
    change('The quadratic image\nis then $-48q(v)$, consistent with the degree-two cup\nsquare evaluated on the normalization; this is a check,\nnot the proof of \\eqref{maps:eq:E.Q1}.',
           'The quadratic image\nis then $-48q(v)$, equal to the degree-two cup square evaluated\non the normalization.','D02','Retain the numerical comparison as mathematics.')
old=re.search(r'The program \\href\{[^}]+maps_splice_quadratic\.py\}\{\\texttt\{[^}]+\}\} tracks the four cycles\n\$\(t_0,e_0,t_1,e_1\)\$ through every unit cancellation used in\n\\ref\{maps:src:E.2.17\}\.  In its sixteen-generator presentation they become four unit vectors\.',text).group(0)
change(old,'Carry the four cycles $(t_0,e_0,t_1,e_1)$ through the unit\ncancellations of \\ref{maps:src:E.2.17}. In the resulting\nsixteen-generator presentation they are four unit vectors.','D09','State the exact cycle transport replacing the program narrative.')
old=re.search(r'The six unimodular charts, all normal degrees, the plumbing\nJacobian and involution, both triple cycles and \\eqref\{maps:eq:E.T8\} are\nchecked exactly in \\href\{[^}]+maps_cusp_smooth_plumbing\.py\}\{\\texttt\{[^}]+\}\}\.',text).group(0)
change(old,'','D09','The preceding proof already supplies the coordinate identities; retain program metadata separately.')
old=re.search(r'    The seam, framing and meridian identities are checked exactly by the program \\href\{[^}]+maps_finite_cap_framings\.py\}\{\\texttt\{[^}]+\}\}\.',text).group(0)
change(old,'','D09','Move computational verification of the just-derived identities to records.')

# Number genuine definitions that were embedded in unnumbered prose.
intro='''In this part $X$ and $X'$ are two members of the family used in
Part~I, and $\\varphi\\in PGL_2(\\mathbb C)$ is chosen so that the three
exceptional values of $X'$ are disjoint from those of $X$.  The fibre
product $P=X\\times_B\\varphi^*X'$ is then a compact complex fivefold.  We
compute its fundamental group and integral homology, its stable tangent
bundle and framed bordism class, its second homotopy module, a circle
fibration with nine-dimensional fibre, and an explicit decomposition into
ordinary framed handles.  These results are not used in Part~II.'''
new_intro='''The same sphere fibrations give compact complex fivefolds by placing
their exceptional fibres over disjoint subsets of the base. Their topology
is governed by a torus-knot peripheral group and the integral cusp maps.

\\begin{definition}[Shifted fibre product]\\label{def:V:shifted-product}
Let $X$ and $X'$ be canonical marked members of the $(3,4,\\infty)$
family, and choose $\\varphi\\in\\operatorname{PGL}_2(\\mathbb C)$ so that
the exceptional values of $X$ and $\\varphi^*X'$ are disjoint.
Their \\emph{shifted fibre product} is $P=X\\times_B\\varphi^*X'$.
\\end{definition}'''
change(intro,new_intro,'D13','Number the shifted-product definition and explain the part by its mathematical connection.')

spin='''For a closed
submanifold $L\\subset\\operatorname{int}D^n$, its ordinary closed
spin is $L\\times S^1$ in
$D^n\\times S^1\\subset\\partial(D^n\\times D^2)=S^{n+1}$.'''
spin_start='\\begin{proposition}[the fibre complement and a spinning obstruction]'
definition='''\\begin{definition}[Ordinary closed spin]\\label{def:V:ordinary-closed-spin}
'''+spin+'''
\\end{definition}

'''
change(spin_start,definition+spin_start,'D13','Place the precise comparison construction in a numbered definition before its use.')
change('\\item We define the comparison construction precisely. '+spin,
       '\\item Use the ordinary closed spin of Definition~\\ref{def:V:ordinary-closed-spin}.','D13','Replace the duplicate definition in the proof by its numbered reference.')
change('\\cite[Section 3, immediately before Theorem 3.4]{mapsWinter08};\nno turning, twisting, or family of deformations is inserted.',
       '\\cite[Section 3, immediately before Theorem 3.4]{mapsWinter08}.','D02','The explicit product embedding in the numbered definition fixes the construction.')

quadratic='''For an abelian group $A$, let $\\Gamma(A)$ be Whitehead's universal
quadratic group, with quadratic generator $q(a)$ and symmetric
bilinear cross effect
$[a,b]=q(a+b)-q(a)-q(b)$.  In particular $[a,a]=2q(a)$.'''
anchor='\\begin{proposition}[the cusp quadratic attachment]'
change(anchor,'\\begin{definition}[Whitehead quadratic group]\\label{def:V:whitehead-quadratic}\n'+quadratic+'\n\\end{definition}\n\n'+anchor,'D13','Number the quadratic-group convention before its use in the result.')
# The replacement above introduces a second occurrence, so remove only the one
# in the proposition by guarding its preceding displayed module notation.
change(' \\qquad T=\\overline R^{\\,2}\\oplus L.\n\\]\n'+quadratic,
       ' \\qquad T=\\overline R^{\\,2}\\oplus L.\n\\]','D13','Use the preceding numbered convention without repeating it.')

# Short mathematical titles; the original permanent label and tag are untouched.
for m in list(re.finditer(r'\\begin\{(theorem|proposition)\}\[([^\]]+)\]', text)):
    title=m.group(2)
    cap=title[0].upper()+title[1:]
    if cap!=title:
        change(m.group(0),m.group(0).replace('['+title+']','['+cap+']'),'D16','Capitalize the mathematical title; retain statement number, label and permanent tag.')

# Additional exact prose repairs that preserve all displayed mathematical maps.
small=[('the original rank-two cusp','the rank-two cusp of the sphere fibration'),
       ('and retain $(\\gamma,u,w,\\delta)$','and use $(\\gamma,u,w,\\delta)$'),
       ('retain the\ntwo regular-torus markings','use the\ntwo regular-torus markings'),
       ('Retain the other factor\'s three covectors','Use the other factor\'s three covectors'),
       ('the homology of the retained three-torus','the homology of that three-torus'),
       ('coefficient of $E_1$ in the\nfree quotient is a generator of $A$, not merely a nonzero\nelement: it is a unit $\\pm h^n$.',
        'coefficient of $E_1$ in the\nfree quotient generates $A$ and hence is a unit $\\pm h^n$.')]
for old,new in small:
    change(old,new,'D08','Express the specified mathematical datum directly.')

before_labels=re.findall(r'\\label\{([^}]+)\}',original)
after_labels=re.findall(r'\\label\{([^}]+)\}',text)
assert set(before_labels)<=set(after_labels)
assert all(after_labels.count(x)==before_labels.count(x) for x in before_labels)
assert re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}',original)==re.findall(r'\\hypertarget\{tag-[^}]+\}\{\}',text)
assert re.findall(r'\\tag\{[^}]+\}',original)==re.findall(r'\\tag\{[^}]+\}',text)
assert not re.search(r'\\texttt\{[^}]*\.py\}',text)

result=ROOT/'S6_SERIES_PUBLISH_V_shifted_revised.tex'
result.write_text(text)
for name,rows in [('S6_SERIES_PUBLISH_V_shifted_edits.tsv',changes),('S6_SERIES_PUBLISH_V_shifted_programs.tsv',programs)]:
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'input_bytes':len(original.encode()),'output_bytes':len(text.encode()),
                  'edits':len(changes),'program_mentions_moved':len(programs),
                  'original_labels_preserved':len(before_labels),
                  'new_definition_labels':sorted(set(after_labels)-set(before_labels)),
                  'sha256':hashlib.sha256(text.encode()).hexdigest()},indent=2))
