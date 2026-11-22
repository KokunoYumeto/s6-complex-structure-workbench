from pathlib import Path
import json,hashlib,csv,re
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OLD=ROOT/'agents/ii_checks_provenance';SOURCE=ROOT/'S6_SERIES_PUBLISH_II.tex'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'path':str(p.relative_to(ROOT)),'sha256':sha(p)}
def save(p,o):p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
source=SOURCE.read_text();now=datetime.now(timezone.utc).isoformat()
comparisons={
'01AP':'Complete printed proof agrees after correcting the frozen draft local-domain assertion. The printed nonzerodivisor/analytic-continuation argument, Krull intersection, Picard-component twists, semicontinuity, repeated Cartier layers and finite reducible-fibre intersection have all been read. The draft correction is explicit and is not a printed theorem defect.',
'01AQ':'The Chern restriction and exponential-sequence map on dP6, normalization differential injection, normal-crossing K identification and projection formula give both exact section groups. The standard six-sphere member is the source-bound scope; arbitrary finite affine twists are not certified. Existing AC2026 credit is retained.',
'01AR':'The product construction and constant trivial line family refute precisely the published Step 1 genus inference. Minimality follows because every rational curve maps constantly to the elliptic base and a ruling fibre has self-intersection zero. The printed Kunneth tuple is separately recomputed by HRR and Serre duality after release.',
'01AS':'The adjunction base-pullback isomorphism, relative cotangent sequence, and actual gluing equation alpha=lambda alpha identify the section space. Lambda=1 is exactly the condition that the same trivialization descends to A=O_S. All three printed proof steps were read.',
'01AT':'Canonical evaluation gives a vertical Cartier zero divisor, whose restriction to the irreducible reduced full fibre is trivial. Adjunction, Serre duality and divisor Riemann--Roch give (1,2,1). Both proof steps were read; the recovery edit is typography only.',
'01AU':'The critical-ideal calculation gives the exact d-semistable deformation module. SS2002 classification hypotheses and notation are transported explicitly. The rational, ruled and diagonal-Hopf differential arguments, projection formula and unitary maximum principle agree with the durable derivation. All five proof steps were read.',
'01AV':'All normalization/conductor/image counts and the global Euler sum were read and agree with the durable derivation. The independent computation method is the actual pair quotient and compact-support Thom cells, bound to SS2002 Proposition 2.6 and the actual conductor image; no arbitrary compactification is substituted.',
'01AW':'All seven printed steps were read: injective pullback, Stokes, zero periods on resolution neighbourhoods, normal descent, finite fibre-product agreement, continuous quotient descent, Cech class and its injectivity. The precise continuous/normal-holomorphic primitive regularity is retained.',
'01AX':'The integral and coherent Leray edge maps identify the unitary character. Koszul acyclicity, the actual surjection pi1(U*) to pi1(U), crossed-homomorphism injectivity and proper-base-change direct limit prove H1(S,A)=0. This postrelease argument supplies the exact comparison without relying on an unproved fixed-tube retraction claim in the draft. The signed exterior-basis isomorphism and an alternative rank-minor computation are bound separately.'}
targets=[]
for tag in comparisons:
    pointer_path=HERE/f'S6_SERIES_PUBLISH_II_{tag}_recovery_release_pointer.json'
    pointer=json.loads(pointer_path.read_text());release=pointer['new_release']
    original_path=ROOT/release['full_block'];original=original_path.read_text()
    assert source.count(original)==1,(tag,'not exact original in current source')
    proposed=original;guards=[]
    def change(suffix,typ,old,new,reason):
        global proposed
        assert old!=new
        n=proposed.count(old);assert n==1,(tag,suffix,n)
        proposed=proposed.replace(old,new,1)
        guards.append({'change_id':'II-REC03-'+tag+'-'+suffix,'defect_type':typ,'old':old,'new':new,'expected_occurrences_in_owning_block':1,'reason':reason,'new_recovery_proposal':True})
    enum=r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'
    if tag=='01AR':
        change('ENUMOPEN','D04,D23',enum+'\n'+r'\item '+'\n','',
               'Remove the one-item iteration wrapper while retaining the complete proof.')
        change('ENUMCLOSE','D04,D23','\n'+r'\end{enumerate}','',
               'Remove the corresponding one-item wrapper terminator.')
    else:
        change('ENUM','D04,D23',enum,r'\begin{enumerate}[label=\arabic*.,leftmargin=*]',
               'Remove the inherited iteration marker; preserve every numbered proof step.')
    if tag=='01AP':
        change('CLOSE','D08,D11',
          ' This proves the final consequence and resolves the unequal-multiplicity transfer in this case without any assertion about torsion-free differentials on individual components.',
          '', 'The full repeated-component filtration and finite intersection already supply the stated conclusion; remove the workflow closing sentence.')
    elif tag=='01AQ':
        change('TITLE','D16','Both fibre groups on the specified $W$',
          'Cotangent groups on the rational normalization fibre','Name the mathematical fibre calculation.')
        change('SCOPE','D22',
          r'For the reduced normal-crossings fibre $W$ with normalization $\eta:\operatorname{dP}_6\to W$ in the specified threefold $X$, and every $L\in\Pic(X)$, put',
          r'For the full reduced normal-crossings fibre $W$ in the standard $(3,4,\infty)$ six-sphere member $X$, with normalization $\eta:\operatorname{dP}_6\to W$, and every $L\in\Pic(X)$, put',
          'State the exact supplied standard-family/topological scope used in the prerelease derivation.')
        change('CREDIT','D02,D08',
          ' The present calculation sharpens the ambient section dimension to exactly one; that sharper equality and its proof are distinguished from the source nonvanishing.',
          '', 'Retain the preceding exact AC2026 credit and the theorem equality; remove the editorial comparison announcement.')
        change('INPUT','D11',
          r'The only global topological input is $H^2(X,\Z)=0$, and the only identification of the fibre used is its specified normalization as the blowup of $\PP^2$ at three points.',
          r'The standard member satisfies $H^2(X,\Z)=0$, and the normalization of $W$ is the blowup of $\PP^2$ at three points.',
          'Give the positive topological and normalization hypotheses with their exact mathematical scope.')
    elif tag=='01AR':
        change('TITLE','D16',
          'Counterexample: A specific implication in the printed proof of Proposition 7.3',
          'Constant twists on an elliptic ruled surface','Name the explicit mathematical construction.')
        change('STATEMENT','D18,D22',
          r'The implication that a ruled minimal surface $S_0$ with a one-parameter family of numerically trivial line bundles $M_t$ and nonzero sections of $\Omega^1_{S_0}\otimes M_t$ must be ruled over a curve of genus at least two is false when the family $M_t$ is allowed to be constant, as the printed proof explicitly allows.',
          r'For an elliptic curve $E$, the minimal ruled surface $S_0=E\times\PP^1$ and the constant family $M_t=\OO_{S_0}$ satisfy $H^0(S_0,\Omega^1_{S_0}\otimes M_t)\ne0$ for every parameter. The ruling has genus one. These data give a counterexample to the genus-at-least-two inference in \cite[Proposition~7.3 and Step~1, p.~693]{CDP20}, where the line-bundle family is permitted to be constant.',
          'Give the explicit counterexample and precise primary journal locus without extending its scope to the whole ambient threefold proposition.')
        change('STEP','D23',r'\noindent\textbf{Step 1.} ','','Remove the duplicate step marker.')
        change('MINIMAL','D22',
          r'Take $S_0=E\times\PP^1$ for an elliptic curve $E$ and take $M_t=\OO_{S_0}$ for every parameter.',
          r'Take $S_0=E\times\PP^1$ for an elliptic curve $E$ and take $M_t=\OO_{S_0}$ for every parameter. Every rational curve on $S_0$ maps constantly to $E$ by Riemann--Hurwitz, so it is a ruling fibre and has self-intersection zero. Thus $S_0$ has no exceptional curve of self-intersection $-1$ and is minimal.',
          'Supply the exact projection/curve argument already written in the durable prerelease derivation.')
        change('ACCENT','D23','Kunneth',r'K\"unneth','Restore the proper-name accent.')
        change('CLOSE','D08,D11',
          " This refutes the stated implication. It is a counterexample to that implication with its explicit data; it supplies no threefold satisfying all of Proposition~7.3's ambient hypotheses.",
          '', 'The statement now gives the precise journal inference and the proof displays the exact product and genus; remove the closing recap and negative scope announcement.')
    elif tag=='01AS':
        change('TITLE','D16','The omitted genus-one case for the standard rank-one fibre',
          'Twisted differentials on a ruled normal-crossings surface','Replace the historical omission heading by the mathematical subject.')
        change('VANISH','D08',
          r'This proves \eqref{cdp:eq:A.16} in that case by the injection into normalization differentials.',
          r'The injection into normalization differentials gives the vanishing in \eqref{cdp:eq:A.16}.',
          'Retain the exact injection and equation reference as the mathematical implication.')
        change('CLOSE','D08',' This proves both dimensions.','','The preceding descent criterion supplies the exact dimension conclusion.')
    elif tag=='01AU':
        change('TITLE','D16','The full torsion-free cotangent assertion for irreducible normal-crossings torus fibres',
          'Twisted cotangent groups of irreducible normal-crossings torus fibres','Name the actual twisted groups.')
        change('OPEN','D08','We check the hypotheses of the classification, including its deformation sheaf. ','','The following canonical-line and deformation-module calculations supply the classification hypotheses.')
        change('DEFINITION','D02,D11',
          'That definition imposes irreducibility, normal crossings, d-semistability and trivial dualizing sheaf; it does not require a prior smoothing to Kodaira surfaces.',
          'Its hypotheses are irreducibility, normal crossings, d-semistability and trivial dualizing sheaf.',
          'State the actual primary definition positively.')
        change('DEGREE','D11',
          r'No degree assumption on $P$ occurs in the cotangent calculation, and \ref{cdp:st:A.4.3} proves the required vanishing for every nontrivial $A$.',
          r'The cotangent calculation of \ref{cdp:st:A.4.3} applies to every $P\in\Pic(E)$ and gives the vanishing for every nontrivial $A$.',
          'Retain the universal line-bundle scope in positive form.')
        change('ACCENT','D23','Finite etale','Finite '+r"\'etale",'Restore the accent.')
        change('FINALLY','D08',r'Finally \ref{cdp:st:A.1.2}',r'Proposition~\ref{cdp:st:A.1.2}',
          'Retain the exact mathematical input without a process transition.')
        change('CLOSE','D08',' This proves the dimension statement.','','The preceding maximum-principle argument states both exact dimensions.')
    elif tag=='01AV':
        change('TITLE','D16','Euler numbers of these irreducible normal-crossings fibres',
          'Euler numbers of irreducible normal-crossings torus fibres','Make the fibre class explicit in the title.')
        change('ACCENT','D23','Poincare',r"Poincar\'e",'Restore the proper-name accent.')
    elif tag=='01AW':
        change('REGULARITY','D02',
          'The construction uses continuous local primitives that are holomorphic on the normalization; it does not assert that those primitives are holomorphic on a non-seminormal surface.',
          'The map is constructed from continuous local primitives whose pullbacks to the normalization are holomorphic.',
          'State the precise primitive regularity proved below; retain all required descent scope.')
        change('OPEN','D08',r'We prove the required local primitive assertion at a point $x\in S$.',
          r'Fix a point $x\in S$.','Retain the local point and all subsequent primitive construction steps.')
        change('ACCENT','D23','Cech',r'\v Cech','Restore the proper-name accent.')
        change('CLOSE','D08',
          r'Consequently $\alpha_Z=0$, and injectivity of pullback gives $\alpha=0$. This proves \eqref{cdp:eq:A.20}.',
          r'Consequently $\alpha_Z=0$, and injectivity of pullback gives $\alpha=0$ for every element of the kernel of \eqref{cdp:eq:A.20}.',
          'Retain both zero equations and the exact map reference in the positive kernel conclusion.')
    elif tag=='01AX':
        change('TITLE','D16','The torsion-free cotangent assertion for arbitrary singular supports in a torus fibration',
          'Cotangent vanishing for the transgression family','Name the exact line-bundle family and conclusion.')
        change('LITERATURE','D02,D18',
          'In particular this proves Equation~(11) of CDP20 for all singular reduced fibre supports in the torus case, with no assumption on their singularities or their scheme-theoretic multiplicities.',
          r'The second group is the torsion-free cotangent group in \cite[Equation~(11), p.~692]{CDP20}.',
          'Bind the exact journal group; arbitrary reduced supports and full-fibre multiplicities are already covered by the displayed universal statement and proof.')
        change('OPEN','D08',r'We specify all comparison maps used from \ref{cdp:st:D.1.9}.',
          r'Take the transgression section supplied by \ref{cdp:st:D.1.9}.',
          'State the actual mathematical input used to construct the character.')
        change('CLOSE','D08',
          r'This proves the first vanishing in \eqref{cdp:eq:A.21}. The second is exactly \ref{cdp:st:A.4.7}',
          r'The second vanishing in \eqref{cdp:eq:A.21} follows from \ref{cdp:st:A.4.7}',
          'The direct-limit equality already gives the first zero group; retain the exact input and equation for the second.')
    original_copy=HERE/f'S6_SERIES_PUBLISH_II_{tag}_recovery_original.tex';original_copy.write_text(original)
    proposed_copy=HERE/f'S6_SERIES_PUBLISH_II_{tag}_recovery_proposed.tex';proposed_copy.write_text(proposed)
    freeze_ref=pointer['durable_original_freeze'];fp=ROOT/freeze_ref['receipt'];assert sha(fp)==freeze_ref['sha256']
    frozen=json.loads(fp.read_text());dp=ROOT/frozen['frozen_derivation_path'];assert sha(dp)==frozen['derivation_sha256']
    owner=frozen['statement_owner']
    targets.append({'tag':tag,'statement_owner':owner,'freeze_receipt':ref(fp),'durable_frozen_derivation':ref(dp),
      'recovery_release_pointer':ref(pointer_path),'new_release_receipt':{'path':release['receipt'],'sha256':release['sha256']},
      'original_full_block':ref(original_copy),'proposed_full_block':ref(proposed_copy),
      'original_block_occurrences_in_current_source':source.count(original),'guards':guards,
      'actual_complete_original_proof_read_in_recovery':True,'actual_complete_final_proposed_proof_read_in_recovery':False,
      'mathematical_comparison':comparisons[tag],
      'frozen_draft_correction':tag=='01AP','source_application_pending':True,
      'proposed_targeted_proof_check_count':1,'proposed_editorial_reread_count':0 if tag=='01AT' else 1,
      'editorial_scope':('Only enumeration typography; excluded from an extra reread event.' if tag=='01AT' else 'Complete original and proposed proof comparison; actual edit scope is stated by the literal guards.'),
      'prior_exposure':'Related Paper I mathematics was read before this assignment. The durable freeze precedes the original II target-proof exposure. Recovery readings/programs occur after that historical exposure and supply no new blind derivation.',
      'events_added':0})

ledger=ROOT/'CHECK_EVENTS.tsv';selected=[]
with ledger.open() as f:
 for i,row in enumerate(csv.DictReader(f,delimiter='\t'),start=2):
  if row['statement_id'] in ['cdp:st:A.4.2','cdp:st:A.4.6','cdp:st:A.4.8']:
   selected.append({'ledger_line':i,'row':row})
search_path=HERE/'S6_SERIES_PUBLISH_II_B_group03_bounded_program_association_search.json'
save(search_path,{'created_utc':now,'ledger':ref(ledger),'selected_rows':selected,
  'scope':'Only the exact three selected statement associations in the restored canonical ledger were examined after their target releases.',
  'result':'No target program is identified in these rows; their displayed mathematical methods remain the comparison baseline. No global absence claim is made.','events_added':0})

program=HERE/'S6_SERIES_PUBLISH_II_B_group03_recovery_alternate_methods.py';output=program.with_suffix('.output.json')
assert json.loads(output.read_text())['all_assertions_passed']
preprograms=[]
for tag,stem in [('01AV','euler_incidence'),('01AX','koszul_contraction')]:
 p=OLD/'computations'/f'S6_SERIES_PUBLISH_II_{tag}_{stem}.py'
 preprograms.append({'tag':tag,'program':ref(p),'output':ref(p.with_suffix('.output.json')),'timing':'Restored original prerelease program and output; preserved byte hashes.'})
bundle={'schema_version':1,'paper':'II','allocation':'B','checker':'i_provenance','created_utc':now,
 'record_kind':'new post-reset recovery comparison and proposal; historical later bytes are not claimed restored',
 'canonical_source_at_review':ref(SOURCE),'targets':targets,
 'recovery_transports':ref(HERE/'S6_SERIES_PUBLISH_II_B_group03_recovery_transports.md'),
 'primary_retrieval':ref(HERE/'primary/S6_SERIES_PUBLISH_II_B_group03_primary_retrieval.json'),
 'bounded_prior_program_search':ref(search_path),
 'durable_prerelease_programs':preprograms,
 'new_postrelease_program':ref(program),'new_postrelease_output':ref(output),
 'program_methods':'AR uses HRR/Serre duality instead of product Kunneth; AV uses the actual compactified pair and Thom cells instead of normalization subtraction; AX uses nonzero minors and rank bounds instead of a contraction, with signed exterior chain isomorphisms for every possible pivot coordinate.',
 'proposed_event_counts':{'targeted proof check':9,'used and rechecked':8},
 'no_new_independent_credit_from_recovery':True,'canonical_mutations':0,'events_added':0,
 'status':'Final complete proposed proof rereading pending.'}
path=HERE/'S6_SERIES_PUBLISH_II_B_group03_recovery_proposals.json';save(path,bundle)
print(json.dumps({'proposal':ref(path),'guard_count':sum(len(t['guards']) for t in targets),'targets':len(targets)},indent=2))
