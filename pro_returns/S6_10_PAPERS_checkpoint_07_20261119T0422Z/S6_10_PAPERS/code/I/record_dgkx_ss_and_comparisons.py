"""Record the primary passages actually read, including edition-specific limits."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parents[2]
f=P/'analysis/I_sources/current_source_matches.json';data=json.loads(f.read_text())
rows={
'DGKXv1':('DGKXv1.pdf',
'arXiv2610.00250v1, Theorems1.3–1.4 p3; Lemma6.11 and full proof p81; Theorem6.12 and full proof pp81–82; Corollary6.13 and proof p82; Proposition6.16 and full proof p85; Proposition7.8 and full proof pp91–92; Theorem7.14 and full proof p95; PropositionsC.1–C.2 with full proofs p102; PropositionC.4 and full proof p103.',
'Matched the supplied TeX labels against the original107-page PDF. The branch-normal quotient, one-variable Kuranishi local-ring substitution, even-shift maps and quadratic composition correction were read at these loci. Earlier receiving-proof rederivation events remain separately scoped. Version1 Theorem1.4 is the exact2Z classification; the arXiv primary indexed record confirms23September2026. No complete reading of all107pages is claimed.',
'https://arxiv.org/pdf/2610.00250v1'),
'DGKXv2':('DGKXv2.pdf',
'arXiv2610.00250v2, title/abstract/contents p1 and full introduction pp1–3; complete supplied source section headings and term searches.',
'The30-page PDF and supplied source omit the version1 tangent, Kuranishi, automorphism and exact-period sections. This comparison records their absence and makes no inference about a reason. The Oka conclusions on pp1–3 were read as source statements, without a whole-proof reading claim.',
'https://arxiv.org/pdf/2610.00250v2'),
'SS00':('../II_independent_primary/SS2002.pdf',
'arXivmath/0001077v2, Definition2.1 p4; Propositions3.1–3.5 and full proofs pp6–10; Theorem3.7 and full proof pp10–11; Theorem4.4 and full proof p14; Theorem5.4 and full proof pp18–20; Proposition6.3 and full proof pp22–23.',
'Read the Hopf conductor maps, normal-line characters and toric quotient smoothings. The operative receiving comparisons use Section3. The printed final generator in Theorem4.4 is recorded separately: (Phi Psi)^w acts trivially on U/<Phi^w,Psi^w>, while Phi Psi has orderw; no use is made of the printed generator. Admissibility retains all Definition2.1 hypotheses. Author bibliography entry13 identifies the published chapter; the listed pages refer expressly to the25-page preprint.',
'https://arxiv.org/pdf/math/0001077v2'),
'Doi2009Root':('Doi2009Root.pdf',
'Published pp880–883: Theorem5.2 statement, Example5.3 in full, and Section5.3 through Theorem5.5 and following discussion.',
'Matched the dual holomorphic normal bundles, anticanonical double divisors and opposite residues. Theorem5.5 asserts a smooth real six-dimensional total manifold with a smooth map and fibre complex structures continuous off the double locus. The preceding gluing map and convergence expression5.1 were read. No complete PDE proof from the earlier sections is claimed.',
'https://www.jstage.jst.go.jp/article/jmath/61/3/61_3_853/_pdf/-char/en'),
'Nishiguchi1988IIRoot':('Nishiguchi1988IIRoot.pdf',
'MPI/88-48 original scan, introduction printedpp1–2 (PDF3–4); Theorem1.4 and its source explanation printedp7 (PDF9); Example2.1 in full printedp13 (PDF15), visually checked.',
'Read the K3 semistable-modification theorem with Hopf and CB components and the explicit diagonal Hopf quotient glued to an elliptic K3 fibre. Receiving citations to Sections2–3 are narrowed to these actual passages. This is a source statement/example reading, not an independent proof of the cited predecessor theorem.',
'https://archive.mpim-bonn.mpg.de/id/eprint/3390/1/preprint_1988_48.pdf'),
'Teleman2010AB':('Teleman2010AB.pdf',
'Published Introduction pp1750–1751, including the explicit Kato modification and spherical-shell gluing description and Theorem0.1.',
'Matched the concrete modification plus boundary identification construction used in the receiving Kato-family comparison. The general gauge-theoretic proof elsewhere in the54-page article was not read in this event.',
'https://annals.math.princeton.edu/2010/172-3/p06'),
'silverman2006heights':('silverman2006heights.pdf',
'Author MSRI lecture, printed slides21–22 (PDF26–27): Variation of the Canonical Height in Families I–II.',
'Read the uniform canonical-versus-Weil-height bound with base-height term and the section specialization limit. The operative bounded-remainder proof in the paper remains the separately opened DeMarco–Mavraki theorems; the inaccessible original Tate and1983Silverman articles retain their explicit background-only status.',
'https://slmath-production-assets.sfo3.digitaloceanspaces.com/attachments/workshops/301/HtSurveyMSRIJan06.pdf'),
'Johansson2016':('Johansson2016.pdf',
'arXiv1611.02831v1, Section2 pp2–4 and complete Section3 pp4–6, with Section2.2 exact-accuracy tests and Section3.2 radius arithmetic.',
'Matched midpoint-radius representation, arbitrary-precision dyadic midpoints, automatically upward-rounded magnitude bounds and the explicit compiler/elementary-operation assumptions. The received interval proof uses enclosure comparisons; this source reading adds no independent code-correctness or replay claim.',
'https://arxiv.org/pdf/1611.02831v1'),
'PythonFlint2026':(None,
'Official python-flint0.9.0 arb documentation, constructor; abs_lower,abs_upper; lower,upper; man_exp; mid_rad_10exp; str sections, accessed18November2026.',
'Matched exact binary tuple/rational-string construction, upward radius rounding and outward endpoint rounding. Decimal display is an enclosing output representation; exact finite endpoint extraction uses man_exp. These semantics were read against the replayed interval certificate and period script. Documentation reading grants no new numerical replay credit.',
'https://python-flint.readthedocs.io/en/latest/arb.html')
}
for key,(filename,locator,scope,url) in rows.items():
    row={'exact_locator':locator,'scope':scope,'date':'2026-11-18','checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro','verification':'opened and matched at listed scope','url':url}
    if filename:
        src=(P/'analysis/I_sources'/filename).resolve()
        row.update(source_path=str(src.relative_to(P)),sha256=hashlib.sha256(src.read_bytes()).hexdigest())
    data[key]=row
f.write_text(json.dumps(data,indent=2,ensure_ascii=False))
f=P/'analysis/bibliography_aliases.json';aliases=json.loads(f.read_text())
for version in [1,2]:
    canonical=f'DGKXv{version}'
    for alias in [f'DGKX2026v{version}',f'DGKX26v{version}',f'DGKXv{version}push',f'DuEtAl2026v{version}',f'DuGuoKusakabeXie2026v{version}']:
        aliases[alias]={'canonical':canonical,'identity_evidence':f'Identical four authors, version-specific title and arXiv2610.00250v{version}; original PDF matched the supplied TeX at the listed passages. Only those bounded readings are inherited.','additional_independent_reading_credit':False}
aliases['SchroeerSiebert2002Root']={'canonical':'SS00','identity_evidence':'Identical authors, chapter, published page range193–222 and author PDF URL; author bibliography entry13 identifies the chapter. Only explicitly preprint-page loci are inherited.','additional_independent_reading_credit':False}
f.write_text(json.dumps(aliases,indent=2,ensure_ascii=False))
print('Recorded',len(rows),'bounded source matches; root keys',len(data))
