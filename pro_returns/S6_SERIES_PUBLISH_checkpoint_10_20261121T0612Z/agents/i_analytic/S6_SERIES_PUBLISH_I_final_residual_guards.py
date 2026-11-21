from pathlib import Path
import csv, datetime, difflib, hashlib, json, re

ROOT = Path('/workspace/scratch/653608133b22')
OUT = ROOT/'work/agents/i_analytic'
SOURCE = ROOT/'work/S6_SERIES_PUBLISH_I.tex'
ORIGINAL = ROOT/'source/S6_SERIES_GRIND_I.tex'
COMPENDIUM = ROOT/'source/S6_GRIND_4_s6_09_compendium/S6_09_PAPERS_I.tex'
source = SOURCE.read_text()
original = ORIGINAL.read_text()
compendium = COMPENDIUM.read_text()
intake = json.loads((OUT/'S6_SERIES_PUBLISH_I_final_residual_intake.json').read_text())
groups = {g['current']['primary']:g for g in intake['groups']}
changes = {}
notes = {}

def add(key, old, new, reason='Remove a process epithet or defensive comparison while preserving the displayed mathematics.'):
    changes.setdefault(key, []).append((old,new,reason))

def full_block(text, key, envs=('cited','theorem','proposition','lemma','corollary','remark','definition')):
    k=text.index('\\label{'+key+'}')
    starts=[(text.rfind('\\begin{'+env+'}',0,k),env) for env in envs]
    a,env=max(starts)
    assert a>=0
    end=text.index('\\end{'+env+'}',k)+len('\\end{'+env+'}')
    proof=re.match(r'\s*\\begin\{proof\}',text[end:])
    if proof:
        end=text.index('\\end{proof}',end)+len('\\end{proof}')
    return text[a:end]

def expanded_proof(key):
    k=compendium.index('\\label{'+key+'}')
    a=compendium.rfind('\\subsection',0,k)
    p=compendium.index('\\begin{proof}',k)
    e=compendium.index('\\end{proof}',p)+len('\\end{proof}')
    return compendium[a:e]

add('ari:C.8.3',
    'This argument proves coverage of the $t$-disc, rather than\ninferring coverage merely from a boundary bound.',
    'Thus the stated $t$-disc is covered.')
add('ari:C.8.4','For every $k\\ge1$, not just these first three steps, define','For every $k\\ge1$, define')
add('ari:C.3.2','the actual stabilizer map is','the stabilizer map is')
add('ari:C.6.5','identity, rather than only numerical closeness.','identity.')
add('ari:C.6.5','For completeness, the singular-modulus certificate uses','The singular-modulus certificate uses')
add('fam:src:C.1.1',
    'For completeness the cusp value follows directly from the normally\nconvergent Fourier expansion, rather than from a quoted Eichler--Zagier\nconstant:',
    'The cusp value follows from the normally convergent Fourier expansion:')
add('fam:src:C.1.1','One can see the branch without a numerical convention:','The branch is determined as follows:')
add('fam:src:C.1.1','Inserting the actual transformed arguments gives','Inserting the transformed arguments gives')
add('fam:src:B.1.4','the actual period identifications','the specified period identifications')

add('inv:A1.1','the actual free cyclic quotient','the specified free cyclic quotient')
add('inv:A1.2',
    'We first compute the line bundle $\\OO_X(H)$,\nrather than a tensor product of two separately descended lattices.',
    'We compute the line bundle $\\OO_X(H)$.')
add('inv:A1.2','For clarity the relative duality map we use','The relative duality map we use')
add('inv:A1.3','We check the torsion cancellation, rather than discarding it.  At','At')
add('inv:A1.3','No Euler-characteristic identity is used to select a Hodge number.','')
add('inv:A2.4','a genuine invariant target\nframe','an invariant target\nframe')
add('inv:A2.4','the actual invariant\ntarget frame','the invariant\ntarget frame')
add('inv:A3.2','the actual pullback map','the pullback map')
add('inv:C3.2','its actual specialization','its specialization')

add('push:src:E.3.1',
    'Thus\n$\\bigwedge^2H^1(\\mathcal O_W)\\to H^2(\\mathcal O_W)$ is an\nisomorphism, including its product rather than just its dimensions.',
    'Thus cup product induces an isomorphism\n$\\bigwedge^2H^1(\\mathcal O_W)\\to H^2(\\mathcal O_W)$.')

for old,new in [
    ('The actual domains and their inverse maps.','The chart domains and their inverse maps.'),
    ('whose differences are the actual\nintegral periods','whose differences are the\nintegral periods'),
    ('Thus these are actual line factors.','Thus these factors satisfy the multiplicative cocycle identity.'),
    ('which gives exactly the previously displayed invariant fibre form.','which gives the invariant fibre form \\eqref{I:eq:fibre-eta-form}.'),
    ('The actual middle line.','The line on the middle piece.'),
    ('the\nactual quotient','the\nspecified quotient'),
    ('the actual affine map','the affine map'),
    ('the actual lattice action','the lattice action'),
    ('In the actual cusp frame','In the cusp frame'),
    ('The actual collar map','The collar map'),
    ('its actual line multiplier','its line multiplier'),
    ('the first $r$ actual affine\niterates','the first $r$ affine\niterates'),
    ('the actual line-coordinate map','the line-coordinate map'),
    ('For the actual étale map','For the étale map'),
    ('is the actual\nperiod factor','is the\nperiod factor'),
    ('The actual finite collar comparison','The finite collar comparison'),
    ('the actual finite root characters','the finite root characters'),
    ('Since the identities hold for every complex $z$, the $f_{ab}$\nsatisfy an exact additive cocycle, rather than one only modulo\nintegers.',
     'Since the identities hold for every complex $z$,\n$f_{ab}+f_{bc}=f_{ac}$ on each overlap component.'),
]:
    add('inv:C3.8',old,new)

add('wb:rem:bcpr-global-gauge-boundary','the actual Dolbeault coboundaries','the Dolbeault coboundaries')
add('inv:D4.1','its actual coherent torsion summand','its coherent torsion summand')
add('inv:D4.3','defines an actual twist for which','defines a twist $M_z$ for which')
add('inv:D4.4','the actual tangent-extension cocycle','the tangent-extension cocycle')
add('inv:D4.4','exact invariants compute the actual\nmultiple-fibre stalks','exact invariants compute the coarse\nmultiple-fibre stalks')
add('inv:D4.5','The actual cohomology jump loci','The cohomology jump loci')
add('inv:D4.5','each actual threshold exceeding','each threshold exceeding')
add('inv:D4.5','for the actual\ntwisted tangent bundle','for the\ntwisted tangent bundle')
add('inv:B3.3','the following actual matrices','the following matrices')
add('inv:B3.3','the two actual attachment cycles','the two attachment cycles')
add('fam:src:A.2.1','their actual $R_g$-action','their $R_g$-action')
add('fam:src:A.2.1','modulo an\nlattice vector','modulo a\nlattice vector','Correct the article; the lattice vector and the source-to-target map are unchanged.')
add('fam:src:A.4.2','the actual fibre class','the fibre class')
add('fam:src:A.4.2','For completeness write $a_A','Write $a_A')
add('ari:C.6.R2','summed with the actual\n','summed using the bound\n')
add('ari:C.6.R2','All points are nontorsion by Statement C.5.','All points are nontorsion by \\cref{ari:C.5.1}.','Replace a stale literal statement name by the CM non-torsion result actually used.')

add('ari:C.6.R5',
    'The coefficients are $\\pm1$, so this is an actual algebraic point,\nnot merely an element of a tensor product with $\\Q$.',
    'The sum is taken in $E_0(\\overline{\\Q})$ with coefficients\n$\\chi(\\mathfrak a)\\in\\{\\pm1\\}$, so $Y\\in E_0(\\overline{\\Q})$.',
    'State the exact integral sum in the displayed elliptic curve; preserve the point needed for the ensuing integer denominator argument.')
add('ari:C.6.R5',
    'up to rounding of the integer cutoff, with the actual $M$ used in\nthe tail bound. The actual integer $M$ enters every tail bound.',
    'up to rounding of the integer cutoff, with the displayed integer\n$M$ used in every tail bound.',
    'Remove repeated cutoff bookkeeping without changing the actual integer cutoffs, inequalities or tail constants.')
add('ari:C.6.R5',
    'The degree is selected to make the geometric factor small, but\nthe actual remainder is separately evaluated with upward rounding.',
    'Select the degree to make the geometric factor small, then evaluate\nthe displayed remainder bound with upward rounding.')
add('ari:C.7.1',
    'the signs in\n\\eqref{ari:eq:cp-periods} are for the exponential rather than the\nquasi-periods of $f_u$ itself.',
    'the signs in\n\\eqref{ari:eq:cp-periods} use the displayed exponential convention.',
    'Retain the exact exponential, rational trivialization and period signs; state the governing convention directly.')

add('ari:C.7.9','The actual point\n','The point\n')
add('ari:C.7.9','places the actual point $R_N','places the point $R_N')
add('ari:C.7.9','The division identity in C.4','The division identity in \\cref{ari:C.4.2}','Replace the stale literal section name by the exact division identity used.')
add('ari:C.7.9',
    'The input missing from this proposed use of the analytic\nsubgroup theorem is a proper Lie subspace defined over\n$\\overline\\Q$; the actual compact slope line is proved\nnot to have that property. The CM decomposition makes the\nsame obstruction visible as',
    'The line $\\ell_c$ containing this compact logarithm has the\ntranscendental slope proved above. Its CM decomposition is',
    'Replace a proposed-method narrative by the proved slope statement; retain the exact compact logarithm, algebraicity equivalence and Gaussian term.')

add('ari:C.7.10','the actual compact point $R_N$','the compact point $R_N$')
add('ari:C.7.10','The actual first compact logarithm','The first compact logarithm')
add('ari:C.7.10',
    'Next construct the compact point without assuming anything\nabout $N(P)$. The identities',
    'The identities')
add('ari:C.7.11',
    'which fails even for $\\lambda=0$. The actual geometry is\nless favorable: the $\\asymp N^4$ points obtained by bounding',
    'which fails even for $\\lambda=0$. Moreover, the $\\asymp N^4$\npoints obtained by bounding')
add('ari:C.7.12','For the actual values the same construction','For the values at $\\lambda=N_0$, the same construction',
    'Name the exact specialization already proved by N_{N_0}=N; retain the relative base field and open algebraicity scope.')
add('ari:C.7.12','its actual model value','its specified model value')
add('ari:C.7.12','no such inequality and assert no lower bound for the actual\ndegrees. For actual analytic samples the base field is the',
    'no such inequality and assert no lower bound for the degrees of the\nsampling fields. For samples at $\\lambda=N_0$, the base field is the',
    'Retain the upper-envelope qualification and identify the exact specialization; no degree lower bound or value-algebraicity assertion is introduced.')
add('ari:C.7.12','the actual logarithmic tangent','the logarithmic tangent')
add('ari:C.7.12','the period and the actual logarithm','the period and the logarithm')
add('ari:C.7.12','The period and the actual logarithm','The period and the logarithm')
add('ari:C.7.12',
    'We give the coefficient estimate needed here, so the height\nassertion does not rely on an unspecified division-polynomial\nbound.',
    'The following coefficient estimate proves the height bound.')

c5=full_block(source,'ari:C.5.1')
groups['ari:C.5.1']={'current':{'primary':'ari:C.5.1','text':c5},
    'original':{'text':full_block(original,'ari:C.5.1')},'candidates':[]}
add('ari:C.5.1','the actual equation\nand section','the equation\nand section')

# These obsolete narrative sentences are removed only when the exact full text
# is present in the assigned proof. No broad whole-source text substitution.
add('inv:A1.2',
    'This argument uses the vertical twist\n$\\OO(H)$ and duality; it does not use the workbench\'s filtration of\n$f_*\\mathcal E\\otimes G$.',
    '', 'Remove the workbench comparison; retain the full duality calculation, evaluation divisor and torsion scope.')

optional_absent={('ari:C.7.12','the period and the actual logarithm')}
# Root applied these two independently during preparation and owns their four
# exposed comparison rows. Their deltas were read; do not duplicate guards/events.
already_applied_by_root=['fam:src:C.1.1','push:src:E.3.1']
for key in already_applied_by_root:
    changes.pop(key,None)
prepared=[]
errors=[]
for key,items in changes.items():
    before=groups[key]['current']['text']
    if source.count(before)!=1:
        errors.append((key,'current full block no longer unique',source.count(before)))
    after=before
    actual=[]
    for old,new,reason in items:
        n=after.count(old)
        if n!=1:
            if n==0 and (key,old) in optional_absent:
                continue
            errors.append((key,old,n)); continue
        after=after.replace(old,new,1)
        actual.append({'old':old,'new':new,'reason':reason})
    prepared.append((key,before,after,actual))
if errors:
    print(json.dumps({'errors':errors},ensure_ascii=False,indent=2))
    raise SystemExit(1)

now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
guards=[]
archive=[]
preview=source
for key,before,after,items in prepared:
    if before==after: continue
    # Line-level hunks retain their exact context. Each emitted guard is checked
    # for uniqueness against the full source and sequential replay below.
    aa=before.splitlines(keepends=True); bb=after.splitlines(keepends=True)
    sm=difflib.SequenceMatcher(a=aa,b=bb,autojunk=False)
    for group in sm.get_grouped_opcodes(n=2):
        a0,a1=group[0][1],group[-1][2]
        b0,b1=group[0][3],group[-1][4]
        old=''.join(aa[a0:a1]); new=''.join(bb[b0:b1])
        assert preview.count(old)==1,(key,'nonunique guard',old)
        gid=f'IA-FRES-{len(guards)+1:03d}'
        reasons=list(dict.fromkeys(x['reason'] for x in items if x['old'] in old))
        guards.append({'id':gid,'statement_ids':[key],'old':old,'new':new,'expected_count':1,
                       'reason':' '.join(reasons)})
        preview=preview.replace(old,new,1)
    ori=groups[key].get('original')
    original_blocks=[]
    if ori:
        original_blocks.append({'path':str(ORIGINAL),'locator':key,'text':ori['text']})
    if key=='push:src:E.3.1':
        original_blocks=[{'path':str(ORIGINAL),'locator':'push:src:E.3.1','text':full_block(original,key)},
                         {'path':str(COMPENDIUM),'locator':'app:rederive:push-src-E.3.1','text':expanded_proof('app:rederive:push-src-E.3.1')},
                         {'path':str(ORIGINAL),'locator':'night:P5.2','text':ori['text']}]
    if key=='ari:C.5.1':
        original_blocks.append({'path':str(COMPENDIUM),'locator':'app:rederive:ari-C.5.1','text':expanded_proof('app:rederive:ari-C.5.1')})
    if key=='wb:rem:bcpr-global-gauge-boundary':
        k=original.index('These formulas identify the actual Dolbeault coboundaries')
        a=original.rfind('\\paragraph',0,k); e=original.index('\n\n',k)
        original_blocks=[{'path':str(ORIGINAL),'locator':key+' (original paragraph)','text':original[a:e]}]
    for main,alias in [('fam:src:A.2.1','wb:pshift:lem:centralizer'),('fam:src:A.4.2','wb:thm:retained-period-deformation')]:
        if key==main:
            original_blocks.append({'path':str(ORIGINAL),'locator':alias,'text':full_block(original,alias)})
    archive.append({'statement_id':key,'source_sha256':sha(source),'current_before':before,'proposed_after':after,
        'original_blocks':original_blocks,'edits':items,
        'comparison_method':'Exposed rereading: the complete current statement/proof was read, all original/current differences were read, and the resulting complete proof was compared with the proposed narrow wording changes. Identical spans were read once, not represented as two independent derivations.',
        'credit':'used and rechecked in this run; no targeted independent or fresh-computation credit'})

labels=lambda t:re.findall(r'\\(?:label|hypertarget|tag)\{[^}]*\}',t)
assert labels(source)==labels(preview),'label/tag sequence changed'
assert preview.count('\\begin{proof}')==source.count('\\begin{proof}')
assert preview.count('\\end{proof}')==source.count('\\end{proof}')
for key,before,after,items in prepared:
    assert preview.count(after)==1,(key,'preview mismatch')

payload={'created_utc':now,'base':str(SOURCE),'base_sha256':sha(source),
    'policy':'Root-owned TeX writes only. Exact scoped editorial guards. Complete exposed proof rereads; no new mathematical or computational claim.',
    'guards':guards,'validation':{'guard_count':len(guards),'affected_containers':len(archive),
      'sequential_exact_replay':'PASS','all_existing_labels_and_tags_preserved_in_order':'PASS',
      'proof_environment_count_preserved':'PASS','preview_sha256':sha(preview)}}
(OUT/'S6_SERIES_PUBLISH_I_final_residual_guards.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_final_residual_archive.json').write_text(json.dumps({'created_utc':now,'base_sha256':sha(source),'comparisons':archive},ensure_ascii=False,indent=2)+'\n')
(OUT/'S6_SERIES_PUBLISH_I_final_residual_preview.tex').write_text(preview)
print(json.dumps(payload['validation'],indent=2))
