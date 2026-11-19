from pathlib import Path
import json,hashlib,csv,datetime
root=Path(__file__).resolve().parents[1]
old=json.loads((root/'IV_closed_code_paragraphs.json').read_text())
endpoint=r'\path{code/current_audits/audit_corrections/code/independent_IV_endpoint_checks.py}'
endpointout=r'\path{code/current_audits/audit_corrections/independent_IV_endpoint_checks.json}'
joint=r'\path{code/current_audits/audit_corrections/code/independent_IV_joint_checks.py}'
jointout=r'\path{code/current_audits/audit_corrections/code/independent_IV_joint_checks.json}'
prism=r'\path{code/current_audits/audit_corrections/code/independent_IV_checks.py}'
new={}
new[0]=r'''The exact algebra is evaluated by factoring rational functions over the
displayed source equation, using symbolic matrix multiplication for the full
central cochain, and computing the determinant of the ten-class intersection
matrix. In particular the $M_6$ coefficient at $s=1$ is formed in the original
$x$ coordinate before its central limit is taken. The program
'''+endpoint+r''' and output '''+endpointout+r''' contain 25,796 exact
checks across \cref{night:P3K.109,night:P3K.110,night:P3K.113,night:P3K.114}.
The checks used here include the discriminant and marked-source inverse, the
$2G/3G$ chord identities, the full specialized $M_6$ coefficient, the section
lattice, and the symbolic period and dual equations. The Lie extension,
proper fixed-curve closure, covering and annular maps are proved above.'''
new[1]=r'''The source, root and reference inputs are the explicit constructions in
\cref{night:P3K.96,night:P3K.97} and the topology maps of
\cref{night:P3F.35,night:P3F.46}. The source equations, section and divisor
orders used throughout are those displayed in EF.1 and EF.18.'''
new[2]='';new[3]=''
new[4]=r'''The endpoint calculation retains the finite-source identity SEF.9,
both root Miller weights, the full $D$ commutator, both signed endpoint
squares and the three chronological root phases. The ordinary and cap
products use the full selected unit $h$. The divisor equations and finite
norm restriction then give the stated winding classification; the module,
properness and reference extensions are the maps constructed above.'''
new[5]=r'''\par\medskip\noindent\textbf{Exact endpoint arithmetic.}\par
The program '''+endpoint+r''' evaluates the source and whole-unit affine
inverse identities symbolically, checks the $M_2$ exponent and threefold
phase formulas for $1\leq l\leq30$ and both signs, and checks primitive
divisibility for $-4m\leq J\leq4m$. It also tests
$n+m\nu\ne0$ for $m=3l+2$, $0\leq l\leq30$,
$n=\pm1$ and $-25\leq\nu\leq25$. Its complete output is
'''+endpointout+r'''. The unbounded assertions use the displayed
integer divisibility identities and $n=\pm1$, $m\geq2$; they are also
proved by the actual source, root and annular maps above.'''
new[6]=r'''The fixed-source endpoint theorem \cref{night:P3K.109} supplies the
source identification used in this winding classification. The point-line
extensions, full annular reference restoration, finite characters and
single-valued lifts retain both signs and the unrestricted annular
integer $\nu$.'''
new[7]=''
new[8]=r'''For an arbitrary endpoint isomorphism we construct its induced
elliptic quotient before applying the Weierstrass invariant to fix the
source base. This treats the finite branch-permutation candidates left by
the auxiliary centroid polynomials in EF.'''
new[9]=old[9]['text'].split('The correction from')[0].strip()
new[10]=old[10]['text'].replace('This calculation is independently replayed from the translated\ncubic in the companion program.',
    'The translated-cubic computation is evaluated symbolically in '+endpoint+'.')
new[11]=r'\medskip\noindent\textbf{Intrinsic elliptic quotient and endpoint domain}'
new[12]=r'''The invariant calculation uses the original cubic and the displayed
marked-cover composites. The elliptic quotient and its inverse, the
primitive kernel and dual equations, the nonzero Lie class, and the
compact flow retain the original source, point line and annular reference.
The exact source and matrix identities are evaluated in '''+endpoint+'.'
new[13]=r'''At the base-rigidity step we use EBP.2--4's actual elliptic quotient
and invariant. EBP.1 and the maps above retain the original source,
Cartier module, roots, periods, references and endpoint-isomorphism
hypotheses throughout the stated noncollision locus.'''
new[14]=r'''\par\medskip\noindent\textbf{Source and endpoint inputs.}\par
The source/root extension and physical group are
\cref{night:P3K.109}; the scalar endpoints, full references and negative
lifts are \cref{night:P3K.110}. EBR.4 and EBP.5--6 give the source,
Cartier, root, finite-character, period and endpoint maps on the
noncollision locus stated here.'''
new[15]=r'''The program '''+endpoint+r''' derives the original cubic invariant,
the marked-node parameter and its inverse, the exact zero and pole
coefficients, the full symbolic central-cochain product, the dual-invariant
equations and the ten-class determinant. It retains the literal specialized
$M_6$ Miller ratios and whole-unit affine inverse. The output
'''+endpointout+r''' gives these identities and the finite signed
endpoint checks. These are the algebraic inputs to the elliptic quotient,
Lie extension, proper closure and compact comparison proved above.'''
new[16]=r'''The source map in R0E.1--3 extends through the complete marked-line
and tangential charts of R0E.4. R0E.5--10 give the full period module,
primitive source lattice, both root powers and characters, and the signed
endpoint and reference products. Compactness, module extension, covering
and single-valuedness are supplied by the explicit maps above.'''
new[17]=r'''\par\medskip\noindent\textbf{Exact source and endpoint algebra.}\par
The exact source invariant, primitive section lattice, full central-cochain
and dual equations, and whole-unit affine inverse are calculated by
'''+endpoint+r''', with output '''+endpointout+r'''.
The full odd-point Miller functions before the good-root limit, their
inverse-source coefficients, and the chronological norms are calculated
by '''+joint+r''', with output '''+jointout+r'''.
These computations supplement the displayed Cartier, graph, tangential
chart and analytic-extension arguments.'''
new[18]=r'\medskip\noindent\textbf{R0P.8. Exact source and endpoint identities}'
new[19]=r'''The polynomial identities are checked before specialization:
the finite good-root substitution is
$(x,y,t)=(w^2X,w^3Y,w^4)$, so the full normalized $f_2,f_3$ coefficients
are rational functions in $w,X,Y$. The program '''+joint+r'''
evaluates those expressions, their central values and their genuine
inverse-source coefficients. It also reduces the infinity source and
threefold norm identities modulo $Y^2-X^3-1$.
The full period/cochain identities are evaluated in '''+endpoint+r'''.'''
new[20]=r'''The analytic extension, compact topology, primitive invariant
quotient, actual source section and single-valued negative lifts follow
from the explicit maps in R0E.1--11 and R0R.1--4. The symbolic and finite
integer calculations above verify their algebraic inputs.'''
new[21]=old[21]['text'][old[21]['text'].index('The original source is'):]
new[22]=r'''The required inputs are the source and Cartier maps of R0E.1--4,
the whole point-theta period module of R0E.5--7, its full suspension
coefficient and nonzero Abel class in the identified Lie line. The
primitive invariant groups, affine source map and inverse, rational
source invariant, centralizer, actual cover lifts and integral
source-section lattice are retained with those maps.'''
new[23]=old[23]['text'].replace(' The earlier\nwording that identified this inverse coefficient with \\(-X(p)\\)\nwas located in the audit and preserved by the author before repair.','').replace('the corrected source-point evaluation is now literal.','the displayed coefficients are evaluated at their chronological source points.')
new[24]=r'\medskip\noindent\textbf{R0CP.5. Complete negative continuation}'
new[25]=r'''The complete negative continuation uses the actual central
source and inverse, both vertex inverses, full root and finite-character
exponents, unrestricted annular sector representative, three-divisor
equation and the entire negative annular word. The displayed extension,
covering and cochain arguments establish these maps on the stated domain.'''
new[26]=''
new[27]=r'''The endpoint classifications of EB and R0E are joined to the
scalar-family and fan maps of \cref{night:P3K.67,night:P3K.73}
by the displayed holomorphic family isomorphism and its inverse.'''
new[28]=r'''The argument retains the actual forward endpoint convention,
the physical line, both signs of the cap norm, every finite character
and the original annular reference throughout ES.1--6.'''
new[29]=r'''Exact rational row elimination solves the full nine-variable
target system from the displayed source characteristic inputs and each
chosen directed word. Substitution checks every original equation and
both native resets. For the $M_2$ row the equations are homogeneous in
$l$, so their unique solutions have the stated scaling. For an arbitrary
fan, its finite canonical word and this same unique-solution argument
apply at each step.'''
new[30]=r'''The source-domain, endpoint exhaustion, compact-family isotopy
and unbounded image arguments use both stated cap progressions, with
the inherited finite order-one, norm-zero filling, and are the
geometric constructions above.'''
new[31]=r'''\par\medskip\noindent\textbf{Exact page and target-prism calculation.}\par
The program '''+joint+r''' constructs the displayed source, signed
root and page inputs and solves the full target systems by exact
rational Gaussian elimination. It uses the solver in '''+prism+r'''.
Its output '''+jointout+r''' records 139,172 exact assertions across
the two scalar-return theorems \cref{night:P3K.115,night:P3K.118},
including 365 admissible two-cap profiles, 5,110 signed endpoint
representatives and 7,014 full prism steps. It records each named identity,
the tested word families and complete selected witnesses. The residue
arguments and terminating canonical-word construction above establish
the full integer and fan ranges.
\end{proof}'''
new[32]=''
new[33]=old[33]['text'].replace('This continuation retains K113-\\/-115 and the full F46 joint-cap construction.','We use \\cref{night:P3K.113,night:P3K.114,night:P3K.115} and the full joint-cap construction of \\cref{night:P3F.46}.').replace('This is the full primary continuation on the four actual two-cap\ndomains below.','We work on the four actual two-cap domains below.')
new[33]=new[33].split('The\nindependent full audit')[0].strip()
new[34]=old[34]['text'].split('Part3.4 remains')[0].strip()
new[35]=r'''The proof uses the source and Cartier construction of
\cref{night:P3F.46}, the shorter parameter family of
\cref{night:P3K.67}, the native products of \cref{night:P3K.73},
and the endpoint and scalar-family maps of
\cref{night:P3K.114,night:P3K.115}. Every source has its prescribed
reference. The additional ordinary total norm is zero.'''
new[36]=old[36]['text'].replace('The independent executable solves these complete\nsystems by Fraction row elimination, without importing the\nprimary or another fan program.',
    'Exact rational row elimination solves the complete systems; the implementation is '+joint+'.')
new[37]=r'\medskip\noindent\textbf{JFP.12. Mapping-torus orientations}'
new[38]=r'''The calculation in '''+joint+r''' evaluates the four displayed
page formulas on the recorded admissible profiles, the signed norm and
character identities, full finite good-root
Miller functions, genuine inverse-source coefficients and chronological
norms. From the displayed page inputs it solves 7,014 complete rational
nine-variable prism systems. The complete output '''+jointout+r'''
records 365 admissible profiles and 5,110 signed representatives, as
well as the exact residue witnesses. The program checks these finite
inputs; the source/cap/reference extensions, negative lifts, both
mapping-torus signs and unbounded image are established by the
displayed maps and integer arguments.'''
new[39]=r'''\par\medskip\noindent\textbf{Construction inputs.}\par
The point/zero graphs, normalized blowups, primitive cap generators
and integral sphere maps are those of \cref{night:P3F.46}.
The shorter-parameter family is \cref{night:P3K.67}; the native products
and full fan-prism comparison are \cref{night:P3K.73}.
The source and endpoint comparisons are
\cref{night:P3K.114,night:P3K.115}. The two-cap page and signed source
graph are explicitly constructed in RJC.10 and JFP.9.'''
new[40]=''
assert set(new)==set(range(len(old)))
patches=[]
for i,q in enumerate(old):
    patches.append({**q,'operation':'replace_exact_text','old_text':q['text'],
                    'new_text':new[i],'purpose':'Replace workflow/absent code-manifest prose by the actual mathematical method and current computation scope; preserve equations and geometric hypotheses.'})
for patch in patches:patch.pop('text')
(root/'IV_closed_computation_patches.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
receipts={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source':'parts/IV.body.tex as read at extraction time',
          'scope':'41 exact paragraph replacements in K109/110/113/114/115/118; old paths and historical counts retained as evidence, not represented as rerun.',
          'patches':patches}
(root/'IV_closed_code_provenance_receipts.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
verification=[]
for n in [109,110,113,114,115,118]:
    block=(root/f'IV_K{n}_current_block_snapshot.tex').read_text()
    tags_before=sorted(__import__('re').findall(r'\\tag\{([^}]*)\}',block))
    for p in patches:
        if p['label']==f'night:P3K.{n}':
            assert block.count(p['old_text'])==1,(n,p['paragraph_index'])
            block=block.replace(p['old_text'],p['new_text'])
    tags_after=sorted(__import__('re').findall(r'\\tag\{([^}]*)\}',block))
    assert tags_before==tags_after,n
    assert block.count(r'\begin{proof}')==block.count(r'\end{proof}'),n
    assert 'code/part3' not in block,n
    (root/f'IV_K{n}_proposed_computation_block.tex').write_text(block)
    verification.append({'label':f'night:P3K.{n}','equation_tags_preserved':len(tags_before),
                         'proof_environments_balanced':True,'absent_old_code_paths_remaining':0,
                         'proposed_sha256':hashlib.sha256(block.encode()).hexdigest()})
(root/'IV_closed_computation_patch_QA.json').write_text(json.dumps(verification,indent=2)+'\n')
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
path=root/'CHECK_EVENTS.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;events=list(reader)
for n in [109,110,113,114,115,118]:
    label=f'night:P3K.{n}'
    outcome='Reviewed every code/program/audit/manifest paragraph in the whole printed block. Prepared exact computational-method replacements in IV_closed_computation_patches.json, retaining all displayed equation tags and actual source/root/reference hypotheses. Old execution counts, notes and unavailable code paths remain in IV_closed_code_provenance_receipts.json. New executable references point to the actual 25,796-check endpoint run and/or 139,172-check joint/prism run at their recorded scopes; no reconstruction of the old finite atlases is claimed. All proof environments remain balanced and no old code/part3 path remains in the proposed block. This is a receiving-text/source-scope check, not an additional whole-proof re-derivation or a rendered-layout inspection.'
    event={'statement_id':label,'date':'2026-11-19','who':actor,'type':'targeted proof check','outcome':outcome,'phase':'S6_SERIES_GRIND'}
    event['event_id']='s6sg:'+hashlib.sha256((label+'|'+outcome).encode()).hexdigest()[:20]
    if not any(e['event_id']==event['event_id'] for e in events):events.append(event)
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(events)
print(json.dumps({'patches':len(patches),'blocks':verification,'events':len(events)},indent=2))
