"""One-shot root findings from actual reading of candidate11 pages1--85."""
from pathlib import Path
import csv, datetime, hashlib, json, re
from S6_SERIES_PUBLISH_editing import Editor, block
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
assert hashlib.sha256(ed.before.encode()).hexdigest()=='eb211f10c397d8e764f561ce5edcf1e214edcb1f67d45513342e139f1b4e1431'
guards=[]
def add(old,new,kind='D02',reason='Remove the page-read process or defensive wording; retain every mathematical formula, hypothesis and comparison map.'):
    guards.append((old,new,kind,reason))

add('$(a-1,b-1)$ proves the $h^1$ formula without an additional duality\nassumption.', '$(a-1,b-1)$ proves the $h^1$ formula.')
add(r"Engel's \cite[Lemma~2.1, pp.~3--4]{Engel2026} identifies",r'\citet[Lemma~2.1, pp.~3--4]{Engel2026} identifies','D18','Remove duplicated author name in the exact primary citation.')
add(r"Engel's \cite[Corollary~2.2, p.~4]{Engel2026} now identifies",r'\citet[Corollary~2.2, p.~4]{Engel2026} identifies','D18','Remove duplicated author name in the exact primary citation.')
add('product. This also checks the precise normalization of the special-value calculation in Proposition~\\ref{push:src:D.4.5};\nits kernel, Laplacian and mean-zero argument are all valid.', 'product.','D08','Delete the check narration after the completed product proof.')
add('identity gives $N((1-i)/2,i)=\\sqrt2$ without a separate theta-constant\nevaluation.','identity gives $N((1-i)/2,i)=\\sqrt2$.')
add('so its argument at $i$ is zero. These checks supply the branch step\nused in R3. The Gaussian factors are respectively','so its argument at $i$ is zero. The Gaussian factors are respectively','D04','Remove the internal R3 pointer and check narration; the full analytic branch argument and Gaussian factors remain.')
add('One way to verify both normalizations without\na model convention is to form','Both the divisor and the leading Laurent coefficient follow from')
add('This supplies an explicit field, without a claim that it is minimal.\n','')
add('\\item Here is a polynomial relation involving only $t$ and $r=N^{12}$,\nif one prefers that form to positive radicals. Remove the factors','\\item Put $r=N^{12}$. Remove the factors','D08','State the resultant construction directly, retaining its input r and all polynomial steps.')
add('For clarity its closed form follows from','Its closed form follows from')
add('The division identity \\eqref{ari:eq:cs-division} and the\nmodular invariance in \\cref{I:logarithmic-lattice-norm}\nwill be used below.\n','','D08','Remove the forward announcement after the exact period-scale map.')
add('\\item We specify elementary arithmetic for all the scalar estimates in\nthis proof. One may use $314159/100000<\\pi<355/113$ and, for','\\item The scalar estimates follow from $314159/100000<\\pi<355/113$ and, for','D08','State the rational inputs to the Taylor estimates directly.')
add('bound follows by comparison of consecutive terms, not by numerical\nsampling. These inequalities verify each displayed rational bound;\nmuch shorter Taylor sums also suffice. ','bound follows by comparison of consecutive terms. These inequalities\ngive each displayed rational bound.')
add('For completeness these are scalar Fourier-series bounds, not\ninterval computations. At $T\\ge49/50$, upper bounds for','The scalar Fourier series give, at $T\\ge49/50$, upper bounds for')
add('bound for $A_2$ is positive there, so no division by a zero has\noccurred.','bound for $A_2$ is positive there.')
add('continuity, so the singular rational model causes no omitted\nmodulus.','continuity.')
add('apply to these root covers without changing a generator.','apply to these root covers, preserving the chosen generator.')
add('give $v=6x$ with $x\\in\\mathbb Z^2$.  There is no further condition on\nthe lower left entry $t$.','give $v=6x$ with $x\\in\\mathbb Z^2$. The lower left entry $t$\nvaries freely in $\\mathbb Z$.')
add('The exact division-polynomial recurrence is listed in\n\\cref{tab:I:programs}.','The division-polynomial recurrence is given in\n\\cref{ari:C.4.4}.','D09','Replace the program-table reference with Proposition4.9, whose proof displays the exact recurrence and initial values.')
add('which gives the formula. There are no missing intersection points at the\nthree special fibres. The computed rational functions','which gives the formula. The rational functions')
add('The exact division-polynomial calculation is recorded in\n\\cref{tab:I:programs}.\n','','D09','The division polynomial is displayed in full above; its program has the required single citation in the final table.')
add('\\item The real period matrix in \\ref{fam:src:C.3.1} has determinant \\(TD<0\\).','\\item The ordered real period matrix in \\cref{I:period-determinant} has determinant \\(TD<0\\).','D14','The earlier determinant lemma supplies exactly the same ordered real matrix and sign, avoiding the later rank-three quotient proposition.')
add('of a component of its finite inverse image, so that this procedure omits\nnone.','of a component of its finite inverse image.')
add('\\item The explicit Albanese lattice in \\ref{fam:section:A.4} is','\\item The explicit Albanese lattice in \\cref{fam:src:A.4.1} is','D06','Replace a misplaced section-label reference, printed as7.3, by the actual Albanese proposition7.6.')
add('For the normalization of \\ref{fam:src:C.1.1}, the three opposite-side identification','For the period normalization of \\cref{fam:src:C.1.1}, the three opposite-side identification','D20','Specify that the cited normalization is the period normalization; the surface normalization is a separate explicit map in the proof.')
add('The exact enumeration and sign transport are listed in\n\\cref{tab:I:programs}.\n','','D09','The proof retains the 36-pair enumeration, determinant/ray tests, exact transport equation and six resulting actions; program citation remains in the final table.')
add('The cotangent direct images and the decisive period scalar','Cotangent direct images and the period scalar','D16','Shorten the mathematical section title.')
add('The global rank and the decisive scalar','The global rank and the period scalar','D16','Remove the evaluative title modifier.')
add('\\item We check the kernel and surjectivity at every type of cusp point. At','\\item At','D08','State the cusp local-ring calculation directly.')
add('sequence of the smooth map to $s$, not the singular differential of\n$s^{m_j}$.','sequence of the smooth map to the root coordinate $s$.')
add('of the three double curves, including their endpoints; no simplicity\nof the global divisor is assumed.','of the three double curves, including their endpoints.')
add('claim downstairs.  This is not a replacement of $m_jS_j$ by $S_j$.','claim downstairs.')
add('nowhere zero in that bundle.  It can vanish as an ordinary tangent\nvector at a toric stratum; this does not imply vanishing in the\nlogarithmic bundle.  Hence evaluation is surjective and its kernel','nowhere zero in that bundle, including where its image in the\nordinary tangent fibre vanishes. Hence evaluation is surjective and its kernel','D02','Use the exact logarithmic-to-ordinary tangent map already defined by the local coordinate formulas; retain its nonzero logarithmic source vector.')
add('This is the explicit reduction of analytic relative duality needed\nhere; the scheme fibre is retained throughout.\n','','D08','Remove the proof-process recap after the complete displayed analytic trace comparison.')
add('Propositions~\\ref{fam:src:B.1.1} and \\ref{fam:src:B.1.3} with','Proposition~\\ref{fam:src:B.1.1} with','D06','Both labels identify Proposition2.11, whose full proof gives the section map and its sign. Cite it once.')
add('target frame; the uncorrected expression with $v=1$ need not be\ninvariant away from zero.  Cup product with $\\gamma$ gives at the','target frame. Cup product with $\\gamma$ gives at the')
add('and Serre duality gives column three.  Thus the numbers are outputs\nof the sheaf computation.  Replacing $\\beta$ by $\\beta+c$ leaves','and Serre duality gives column three. Replacing $\\beta$ by $\\beta+c$ leaves','D08','Remove the computational recap; all Leray inputs, output table and parameter-invariance argument remain.')
add('Specified associated-graded generators and a global Dolbeault lift','Associated-graded generators and a Dolbeault lift','D16','Shorten the title while retaining the associated-graded scope, allowing the tag to remain with its title.')
add(r'\cite[Lemma~6.1]{DuEtAl2026v1}',r'\cite[Lemma~6.1, p.~74]{DuEtAl2026v1}','D18','Primary v1 Lemma6.1 and full proof actually viewed; locator receipt preserved.')
add(r'\cite[Lemmas~6.2 and~6.7; Propositions~6.6 and~6.10]{DuEtAl2026v1}',r'\cite[Lemma~6.2, pp.~74--75; Lemma~6.7, p.~78; Proposition~6.6, p.~77; Proposition~6.10, pp.~79--80]{DuEtAl2026v1}','D18','Exact v1 primary pages from the archived full statement/proof readings.')

# Resolve printed generic statement references in the root-read pages only.
for old,new in [
 (r'For the period section identified in Statement \ref{fam:src:B.1.3}',r'For the period section identified in \cref{fam:src:B.1.3}'),
 (r'\item Statement \ref{fam:src:B.1.3}',r'\item \Cref{fam:src:B.1.3}'),
 (r'Statement \ref{ari:C.1.1}',r'\Cref{ari:C.1.1}'),
 (r'Statement \ref{ari:C.8.2}',r'\Cref{ari:C.8.2}'),
 (r'from Statement \ref{ari:C.4.2}',r'from \cref{ari:C.4.2}'),
 (r'covered by Statement \ref{ari:C.8.1}',r'covered by \cref{ari:C.8.1}'),
 ('covered by Statement\n\\ref{ari:C.8.3}',r'covered by \cref{ari:C.8.3}'),
 (r'and Statement \ref{inv:A1.0}',r'and \cref{inv:A1.0}'),
 (r'Statement \ref{inv:A1.0} gives column zero',r'\Cref{inv:A1.0} gives column zero')]:
    add(old,new,'D06','Use the actual numbered statement kind through cleveref; mathematical target unchanged.')

envpat=re.compile(r'\\begin\{(?:theorem|proposition|lemma|corollary|definition|remark|maintheorem|cited|computed)\}')
subjects={}
def parent(text,pos):
    heads=list(envpat.finditer(text[:pos+1]))
    if not heads:return None
    m=heads[-1];tail=text[m.start():]
    lab=re.search(r'\\label\{([^}]+)\}',tail)
    if not lab:return None
    try:
        b=block(text,lab[1]);return lab[1],b
    except ValueError:return None
for old,new,kind,reason in guards:
    assert ed.text.count(old)==1,(old,ed.text.count(old))
    pos=ed.text.index(old);p=parent(ed.text,pos)
    if p and p[0] not in subjects:subjects[p[0]]={'before':p[1]}
    ed.replace(old,new,kind,reason,p[0] if p else 'root candidate11 reading')

lab='fam:src:B.2.3';old=block(ed.text,lab)
subjects.setdefault(lab,{'before':old})
statement=old[:old.index(r'\begin{proof}')]
newproof=r'''\begin{proof}
Local inverse logarithms of $u$ give the proper local families of
\cref{fam:src:A.3.1}; its coherent even shifts give their global
family over the punctured $w$-disc.
Descent through $u=w^2$ would furnish an isomorphism between the
two pulled-back fibres at $w$ and $-w$, namely $X_c$ and $X_{c+1}$.
\Cref{fam:src:A.2.1} excludes that isomorphism by the nonzero class
of $d$ in $\Lambda^{A_2}/N_2\Lambda$. This class has exact order two
on the normalized finite cover. The same obstruction applies to
all sphere logarithmic data by \cref{fam:src:B.2.1}, because $r_2$ is odd.
\end{proof}'''
ed.replace(old,statement+newproof,'D12','Keep the integral order-two obstruction as the single proof. The alternate Laurent witness is already supplied by the Albanese proposition and is retained in full in this comparison archive; proper local realization and coherent double-cover descent remain.',lab)

ed.save()
for lab,data in subjects.items():data['after']=block(ed.text,lab)
rp=r/'records/S6_SERIES_PUBLISH_I_root_visual_candidate11_comparison.json'
rp.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_before_sha256':hashlib.sha256(ed.before.encode()).hexdigest(),'source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),
 'reading_evidence':'records/S6_SERIES_PUBLISH_I_final_candidate11_reading_root.json',
 'scope':'All root-assigned candidate11 pages1--85 actually read as full rendered images. Complete affected current proofs were read there; all exact replacement passages were read before applying. For the residue and coherent-family blocks, complete source replacements and old/current archives were also read. Alternate double-cover proof archived below. No derivation-before-exposure or new computation; all numerical inputs and exact maps unchanged.',
 'primary_locator_evidence':'agents/i_provenance/literature/S6_SERIES_PUBLISH_I_AC_DGKX_canonical_root_locator_receipt.json',
 'blocks':subjects},indent=2)+'\n')
rows=[]
for i,(lab,d) in enumerate(subjects.items(),1):
 if r'\begin{proof}' not in d['before']:continue
 rows.append({'statement_id':lab,'date':'2026-11-21','who':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited (no separate numeric setting exposed), S6_SERIES_PUBLISH root',
 'type':'used and rechecked in this run','outcome':'Complete exposed proof read in candidate11 and exact revised passages compared. Mathematical inputs, equations, scopes and maps retained. Duplicated Laurent proof for B.2.3 preserved in the archive and existing Albanese result. No targeted, independent or computational credit.',
 'event_id':f'ce:publish-I-root-visual-c11-{i}-20261121','phase':'final page-reading correction','source_file':str(rp.relative_to(r)),'source_row':lab,'source_event_type':'used and rechecked in this run','evidence_group':'eg:publish-I-root-visual-c11-20261121'})
with (r/'records/S6_SERIES_PUBLISH_I_root_visual_candidate11_CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'root_guards':len(guards)+1,'proof_associations':len(rows),'shared_evidence_groups':1,'independent_credit':0}))
