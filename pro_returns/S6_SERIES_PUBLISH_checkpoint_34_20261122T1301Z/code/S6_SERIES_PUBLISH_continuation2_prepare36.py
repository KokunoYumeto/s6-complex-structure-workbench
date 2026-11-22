from pathlib import Path
import datetime as dt
import hashlib,json,re

R=Path(__file__).resolve().parents[1]
D=R/'agents/continuation2_root'
def bind(p):return {'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
now=dt.datetime.now(dt.timezone.utc).isoformat()
old=R/'agents/ii_infra/released_proofs/033P/0a92ff2ec417b8ca/S6_SERIES_PUBLISH_full_owning_block.tex'
text=old.read_text();original=text;guards=[]
def change(a,b,k,why):
 global text
 assert text.count(a)==1,(a,text.count(a))
 text=text.replace(a,b,1);guards.append(dict(old=a,new=b,type=k,reason=why,occurrences=1))
change('classification on the specified parameter domain','Biholomorphism classes in the two-parameter family','D16','Give a mathematical title identifying the classification.')
change('source construction, with its fixed logarithmic vector $\\ell$,','construction of \\cite[Proposition~6.4, pp.~19--20]{ViaTwo26push},\nwith its fixed logarithmic vector $\\ell$,','D06,D08','Resolve the construction to the opened primary proposition and pages.')
change('Every such biholomorphism covers the identity of the elliptic\nbase.','Every such biholomorphism covers the identity of the base $\\mathbb P^1$.','D13','The intrinsic map is to the P1 base of the elliptic surface, as stated and proved; spell out this identical base.')
change('$(0,\\lambda_0)$ in Theorem 1.1 of \\cite{ViaTwo26push}, choose','$(0,\\lambda_0)$ in \\cite[Theorem~1.1, p.~2]{ViaTwo26push}, choose','D06','Resolve the original bidisc theorem and page.')
change('Within that actual bidisc,','Within that bidisc,','D08','Remove the production-era intensifier; keep the exact bidisc scope.')
change('label={$\\langle1\\rangle$\\arabic*.}','label=\\arabic*.','D04,D23','Use ordinary proof-step numbering.')
change('The equations of Proposition 6.4 in \\cite{ViaTwo26push}','The equations of \\cite[Proposition~6.4, pp.~19--20]{ViaTwo26push}','D06','Use the opened primary locator.')
change('smoothness follows from the same free\nfinite action and unimodular charts.  We make no assertion\nabout continuation to arbitrary $\\mu$.','smoothness follows from the same free\nfinite action and unimodular charts.','D02','The positive stated mu-disc domain already supplies the scope.')
change('the needed input from Proposition 6.1 of the source, on the','the canonical formula of \\cite[Proposition~6.1, pp.~17--18]{ViaTwo26push},\non the','D06','Identify the canonical-bundle result and opened pages.')
change('invariant under the actual affine deck map','invariant under the affine deck map','D08','Keep the fixed affine map without an intensifier.')
change('an affine automorphism of\nthe elliptic base','an affine automorphism of\nthe base $\\mathbb P^1$','D13','Use the same explicitly identified base throughout.')
change('The first column then gives $h=c\'-c\\in\\mathbb Z$ and\nlattice map $\\alpha(I-hE_{41})$.',
 'The first column gives $h=c\'-c\\in\\mathbb Z$ and the\nlattice map $A=\\alpha(I-hE_{41})$, since\n$\\Pi_{\\mu,c+h}(I-hE_{41})=\\Pi_{\\mu,c}$.','D13','Show the exact period-column identity in the printed inverse-generator convention.')
change('Normalize after the actual fourth-root base change.  Its\naffine generator is the one with fourth power $\\ell$, not\nan arbitrary generator of its cyclic subgroup.  Summing the\ntranslation defect around this generator gives',
 'After the fourth-root base change, the oriented meridian\n$\\gamma$ satisfies $\\gamma^4=\\ell$, as in\n\\cite[equation~(3.14), p.~8]{ViaTwo26push}. A map over the\nidentity of the base sends it to $k\\gamma$ for $k\\in\\Lambda$.\nThus $A\\ell-\\ell=N_4k$; multiplication by $-\\alpha$ gives','D02,D13,D18','State the exact induced meridian homomorphism and recover the unchanged norm congruence.')
change('This proves necessity, including the multiple fibre\'s full\nnon-reduced structure.','The congruence uses the full multiple fibre through its oriented\nmeridian relation.','D08','Replace the recap by the precise full-fibre input.')
change('\\item We prove sufficiency with all four collar conditions.\nLet $h$ be even and put','\\item Let $h$ be even and put','D08','Begin the actual sufficiency construction directly.')
change('term for the change of the invariant translation\n$\\Pi\\ell/4$, not a logarithm used on the central chart.','term for the change of the invariant translation\n$\\Pi\\ell/4$; the central map is the holomorphic root-family\ntranslation just constructed.','D02,D13','Identify the punctured collar expression with the extending map positively.')
change('This criterion includes regularity of the remainder; membership\nof the defect in $K_j$ alone would not exclude an essential\nsingularity of a preassigned punctured translation.','The criterion requires both the specified integral winding and\nthe holomorphic unit remainder.','D02','Keep both analytic conditions explicitly and remove the unused counter-scenario.')
change('It holds as an exact integer identity, checked in the program.','Multiplication of the four displayed monodromy matrices gives\nzero on the left.','D09','Describe the exact input, operation and result in the proof; program references belong to its table.')
change('\\item We verify the vanishing of its analytic obstruction, including\nthe difference sheaf.  The root curve has just the order-four','\\item The root curve has the order-four','D08','Begin with the mathematical object, retaining the entire obstruction argument.')
change('The extension splits since\n$H^1(\\mathfrak C,\\mathcal O(1))=0$, by the same two-chart\nLaurent calculation with weights $1,4$.',
 'The extension $0\\to\\mathcal O\\to\\mathcal E\\to\\mathcal O(-1)\\to0$\nsplits since $H^1(\\mathfrak C,\\mathcal O(1))=0$.\nIn the two-chart Laurent calculation with weights $1,4$,\na first-cohomology monomial has both exponents negative and\nhence weighted degree at most $-5$. This gives\n$H^1(\\mathcal O(k))=0$ for $k=1,0,-1$.','D13','Give the exact extension group and the weighted Laurent argument for every cohomology vanishing used.')
change('\\item Finally choose a single logarithm of $\\lambda$ on the source\'s','\\item Choose a single logarithm of $\\lambda$ on the','D08','Use direct mathematical phrasing.')
new=D/'S6_SERIES_PUBLISH_II_033P_proposed.tex';assert not new.exists();new.write_text(text)
assert original.count('\\item ')==text.count('\\item ')==9
for marker in (r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}\{\}'):
 assert re.findall(marker,original)==re.findall(marker,text)
events=[]
for kind,outcome in [
 ('targeted proof check','Statement-led derivation frozen before the complete target proof. Uniform family, intrinsic pencil, cross-ratio rigidity, centralizer/norm necessity, explicit divisor half-translation and all four extensions derived. Postrelease marking disagreement settled by Pi_p=Pi_f S, H_f=S H_p S^-1 and ell_f=S ell_p; corrected printed-convention witness F_(c+2) J F_c^-1=Jprime. The theorem statement remains unchanged.'),
 ('used and rechecked in this run','Complete nine-item original and proposed proofs compared. Every collar identity, oriented-meridian map, determinant/difference bundle and weighted Cech vanishing checked. Exact primary locators supplied; separate bounded geometric review supports the independent half-translation route. No credit for pages or for an unseen primary PDF.'),
 ('computation or formal certificate','Fresh prerelease Fraction RREF and quotient-ring identities supplemented after release by independent sparse polynomial convolution, denominator cross multiplication and permutation determinant. Recomputed all four period covariance identities, period shift and exact basis transport, root conjugacy, full sphere relation, norm defect and cubic discriminant. Complete historical SymPy program read and rerun; its rerun receives no extra independent event. Analytic extension is established in the written derivation, not inferred from scalar arithmetic.')]:
 events.append(dict(statement_owner='push:src:E.5.3',event_type=kind,event_count=1,who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation',scope=outcome,
  where='agents/continuation2_root/S6_SERIES_PUBLISH_II_033P_comparison.md',evidence_group='S6_SERIES_PUBLISH_II_C2_033P_statement_led'))
ep=D/'S6_SERIES_PUBLISH_II_033P_event_proposals.json';ep.write_text(json.dumps(dict(created_utc=now,events=events),indent=2)+'\n')
proposal=dict(created_utc=now,tag='033P',owner='push:src:E.5.3',original=bind(old),proposed=bind(new),guards=guards,
 freeze=bind(R/'agents/ii_infra/derivation_freezes/033P/20261122T033003618192Z/S6_SERIES_PUBLISH_derivation_freeze_receipt.json'),
 release=bind(R/'agents/ii_infra/released_proofs/033P/0a92ff2ec417b8ca/S6_SERIES_PUBLISH_release_receipt.json'),
 comparison=bind(D/'S6_SERIES_PUBLISH_II_033P_comparison.md'),events=bind(ep),
 geometric_review=bind(R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_033P_geometric_review.md'),
 original_and_proposed_proof_items=[9,9],mathematical_statement_changed=False,final_proposed_reading_pending=True)
pp=D/'S6_SERIES_PUBLISH_II_033P_admission_proposal.json';pp.write_text(json.dumps(proposal,indent=2)+'\n')
source=R.parent/'S6_GRIND_6_literature/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex'
receipt=dict(created_utc=now,source_relative_to_base=str(source.relative_to(R.parent)),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 edition='arXiv:2609.33785v1, 27 September 2026; manuscript 26 September 2026',
 urls=['https://arxiv.org/abs/2609.33785','https://arxiv.org/html/2609.33785v1'],
 actual_loci=['Theorem 1.1 p2','Lemmas 2.1 and 2.2 pp3-4','Proposition 3.1 pp6-7','Lemma 3.2 p7','equations3.11-3.14 p8','Proposition6.1 pp17-18','Proposition6.4 pp19-20'],
 online_html_opened=True,public_pdf_opened=False,github_raw_or_blob_opened=False,
 failed_attempts='Public PDF and pinned Github raw/blob returned DisabledError; no opening credit. Verified attached source and program used.',
 publication_download_kept=False)
(D/'S6_SERIES_PUBLISH_II_033P_primary_reading.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(bind(pp),indent=2));print(text)
