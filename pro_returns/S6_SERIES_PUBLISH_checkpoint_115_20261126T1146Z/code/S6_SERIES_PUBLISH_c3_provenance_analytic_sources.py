#!/usr/bin/env python3
"""Record exact primary loci and our application maps; no source bytes in cp35."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import csv
import hashlib
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT.parents[1]/'tmp/c3_provenance_primary'
OUT=ROOT/'agents/continuation3_provenance/analytic_lr'
now=datetime.now(timezone.utc).isoformat()
tags=['0AUW','012O','012U','012W','011N','011O','09V6']

def fetch(tag):
    p=TMP/f'Stacks_{tag}.html'
    if p.exists():return tag,'cached exact HTML after opened-page reading'
    try:
        with urlopen('https://stacks.math.columbia.edu/tag/'+tag,timeout=25) as response:
            data=response.read()
        assert tag.encode() in data
        p.write_bytes(data)
        return tag,'primary HTML downloaded after full tool-page reading'
    except Exception as exc:return tag,type(exc).__name__+': '+str(exc)

with ThreadPoolExecutor(max_workers=7) as pool:downloads=dict(pool.map(fetch,tags))
rows=[]
def source(sid,url,version,locus,files,scope,application,extent):
    paths=[TMP/x for x in files]
    assert all(p.is_file() for p in paths),files
    rows.append(dict(source_id='II-C3-ANALYTIC-S'+sid,url=url,version=version,
        exact_locus=locus,source_sha256='; '.join(p.name+':'+hashlib.sha256(p.read_bytes()).hexdigest() for p in paths),
        bytes='; '.join(p.name+':'+str(p.stat().st_size) for p in paths),
        established_scope=scope,exact_application=application,reading_extent=extent,date_utc=now))

source('01','https://www.numdam.org/item/PMIHES_1970__38__77_0.pdf',
 'Ramis–Ruget, Publications Mathématiques IHÉS38 (1970),77–91',
 '§4 Theorem2 and proof pp.82–84; §7 Proposition2 and the complete-intersection calculation p.91',
 ['RamisRuget1970.pdf'],
 'Trace duality identifies the dual of compactly supported coherent cohomology with the appropriate Ext group against the analytic dualizing complex; the complete-intersection computation identifies that complex for a hypersurface.',
 'For i:W→X a compact Cartier surface in smooth X, the complex is ω_W[2]. With F=E|W locally free, Ext^(−q)(F,ω_W[2])=H^(2−q)(F∨⊗ω_W); Hc=H by compactness. For W=f^−1(b), a nonzero vector in O_B(b)|b trivializes the extra adjunction factor. This combines both old duality scopes without restricting X to be compact.',
 'Complete cited statements and proofs read, including the p.91 Koszul identification. Lemma9, used in the source proof, is itself stated without proof there; no independent derivation credit.')
source('02','https://djvu.online/file/2hQiOnz8WuoQk',
 'Bănică–Stănăşilă, Algebraic Methods in the Global Theory of Complex Spaces (1976), primary book facsimile',
 'ChapterIII §3 Theorem3.4 pp.116–120 and Corollary3.5 pp.120–121; §4 Theorem4.1 p.124',
 [f'BS76_p{n}.webp' for n in [116,117,118,119,120,121,124]],
 'Proper coherent flat families have the canonical base-change equivalences; degree-q fibre vanishing yields the degree-(q−1) base-change isomorphism. Theorem4.1 gives a finite free local complex, bounded for a flat sheaf, compatible with coefficient tensor products.',
 'The cited base-change owner applies Corollary3.5 with q=3 to exactly β_c². The top-degree owner applies the local complex to a curve DVR and its Tor exact sequence, including nonreduced full fibres. The Picard endpoint arguments apply the bounded complex to proper flat universal line families and the minors of its differentials.',
 'Complete Theorem3.4 statement and proof, Corollary3.5 statement and proof, and all seven page images read. Theorem4.1 complete statement read; its general proof is not claimed read. The hashed objects are primary page images, not the bot-response HTML.')
source('03','https://alpo.ge/s6.pdf',
 'Author PDF downloaded and opened in continuation3; exact bytes identified by hash',
 'Definition10.1 p.86; Lemma10.2 proof p.87; Lemma10.3 pp.87–88; Theorem10.5 and Corollary10.6 statements/full proofs pp.88–89',
 ['AC26.pdf'],
 'The conductor construction on a compact normal-crossing fibre supplies its ambient section, image/triviality criterion and conormal obstruction. The standard threefold has normalization-trivial restrictions of all global line bundles; every twist has nonzero cusp H² and nonzero R². The source proves global H² nonvanishing for general twists and the positive-index counterexample.',
 'The arbitrary local conductor owner keeps its more general noncompact setup and confines its compact H0 clause to connected compact S; its compact construction is credited exactly. The actual standard-family corollary uses the same cusp and twist A=(L∨⊗ω_X)|W. The all-twist global consequence follows here by the proved one-vanishing criterion plus c3=2, with the source counterexample credited at its proved scope.',
 'Complete listed statements and proofs read, including all five Theorem10.5 proof steps and the Corollary10.6 proof. No source text is copied to checkpoint records.')
source('04','https://alpo.ge/s6.pdf',
 'Same AC26 author PDF and hash as S03',
 'Proposition7.26 pp.61–62; §7.7 standing hypotheses p.61; (A.5) p.95; LemmaA.4 pp.99–100; TheoremB.1 pp.101–105, especially (N1)–(N2) p.101',
 ['AC26.pdf'],
 'The invariant degree-two class, order-four specialization lattice and the integral nearby-cycle/restriction maps are computed for the marked translations used in the standard family.',
 'The global Picard proof first writes E=kq, uses π₂*H²(S₂)={aγη₂+bq:a≡b mod2} to force k even, contracts q with the exact v1,v2, and then applies the boundary balance. The same source inclusion R²f*Z→j*L² detects the zero edge class. The nearby-cycle square uses exactly the (N1)–(N2) maps.',
 'Complete Proposition7.26, LemmaA.4 and TheoremB.1 statements/proofs read; exact vector equation and surrounding standing hypotheses opened. These uses do not invoke a general integral invariant-cycle theorem.')
source('05','https://www.math.stonybrook.edu/~cschnell/mat615/lectures/lecture3.pdf',
 'Author lecture3, dated February4; no year printed in the document',
 'Equations(3.3)–(3.10) pp.3–7; Example3.5 p.4',
 ['SchnellLecture3.pdf'],
 'The exponential cocycle and crossed-cocycle factor of automorphy give the line-bundle quotient and its alternating first Chern form.',
 'The boundary proof fixes the same exponential convention c(g,h)=g_g(hz)+g_h(z)−g_gh(z). Its central extension and cusp mixed winding use that convention, with the explicit normalization and sign equations retained in full.',
 'All cited equations, Example3.5 and surrounding argument pp.3–7 read. The general Appell–Humbert classification proof continues in another lecture and is not claimed read or used as a substitute for the boundary proof.')
source('06','https://www.numdam.org/article/BSMF_1957__85__77_0.pdf',
 'Cartan, Bulletin SMF85 (1957),77–99',
 '§2 fundamental theoremB, p.80',
 ['Cartan1957.pdf'],
 'Coherent analytic sheaves on a Stein space have vanishing positive-degree cohomology.',
 'For the annulus-times-two-discs cusp neighbourhood and the maximal-chart graph Sσ, the proof explicitly establishes Steinness and the retract/contractibility. Exponential cohomology then gives Pic(U)=H²(U,Z), allowing the extending frame whose winding is computed.',
 'Complete statement and surrounding setup at p.80 read. This source states the fundamental theorem there; no full proof at that locus is claimed.')
source('07','https://www.college-de-france.fr/media/jean-pierre-serre/UPL1698785858825941763_Serre_GAGA.pdf',
 'Serre, Annales Institut Fourier6 (1956),1–42; author archive facsimile',
 '§11 comparison homomorphism pp.18–19; §12 Theorem1 p.19; §13 complete proof pp.20–22',
 ['Serre1956GAGA.pdf'],
 'The algebraic-to-analytic comparison maps identify coherent cohomology on projective varieties.',
 'Apply the comparison to the projective toric dP6 and O; combine with toric H¹(O)=0 to identify its analytic Pic0 and show that c1 is injective. The proof retains the precise exponential-sequence map.',
 'Complete theorem, comparison definition and complete proof read from this exact PDF. Its hash is not confused with the older different Numdam download.')
source('08','https://pi.math.cornell.edu/~tsh/cornell-only/cox-little-schenck-toric.pdf',
 'Cox–Little–Schenck author2010 text, preface September2010; published book2011',
 'Example1.2.21 p.31; Propositions4.1.1–4.1.2 p.171; Theorems4.2.8 p.181 and4.2.12 p.184; Theorem9.2.3 p.410',
 ['CLS2010_opened_web_loci.json'],
 'The loci give smooth affine toric charts, principal character divisors, Cartier/support-function equivalence and Demazure vanishing.',
 'The proof uses the unimodular basis (e1,0),(e2,0),(v,1) for Δ×(C*)², takes ray coefficients a(v) with support values −a(v), and evaluates the explicit hexagon intersection degrees. Demazure vanishing applies to D=0 on projective dP6.',
 'Complete Example1.2.21, both propositions and all three theorem statements/proofs read through the successful web rendering. The example refers its proof to an exercise. Direct PDF fetch returned403. The listed hash is explicitly a hash of retrieved primary-text excerpts saved outside checkpoint, not a PDF hash; the failed274-byte PDF-named HTML is excluded.')
source('09','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/79BEA1EB6CF23BB9AEBCF4677C82B108/S0010437X98000360a.pdf/the-algebraic-dimension-of-compact-complex-threefolds-with-vanishing-second-betti-number.pdf',
 'Campana–Demailly–Peternell, Compositio Mathematica112 (1998),77–91, publisher PDF',
 'Proposition1.1 p.78 and proof; Corollaries1.2–1.3 p.79 and proofs; Lemma1.5 pp.79–80; Theorem3.1 setup, Lemmas3.2–3.4 and full proof pp.84–86',
 ['CDP98.pdf'],
 'The source states divisor-twist disappearance for compact spaces and local freeness of all higher direct images of a locally free sheaf on a smooth compact threefold over a curve. Its final restriction-span argument is on printed p.86, after the diagram on p.85.',
 'E17 supplies the correct associated-component hypothesis for the smooth connected divisor application. The valid top-degree base-change step in Lemma1.5(c) is credited separately from its false full local-freeness assertion. P312 and D1.10 use the actual integral invariant-domain coefficient map and identify the final complex-span condition; no restriction-surjectivity claim is inferred from a group splitting.',
 'Complete listed statements and proofs read. Metadata correction151 removes an erroneously added lower-direct-image-vanishing hypothesis from the earlier source-scope paraphrase; it changes no counterexample or manuscript theorem.')
source('10','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDF2D04CFB35CEE105E10B188D97D68A/S0010437X19007802a.pdf/algebraic_dimension_of_compact_complex_threefolds_with_vanishing_second_betti_number.pdf',
 'Campana–Demailly–Peternell, Compositio Mathematica156 (2020),679–696, publisher PDF',
 'Theorem2.2 and Proposition2.4, p.680; their surrounding reduction/application',
 ['CDP2020.pdf'],
 'The source asserts tangent-cohomology/index conclusions for the stated integral-cohomology and algebraic-reduction setting; Proposition2.4 supplies the R²-direct-image criterion.',
 'The relative corollary uses exactly E=TX⊗L and L0=L⊗f*A^m with the Leray two-column map. P312 uses the actual integral cohomology, algebraic reduction and nonidentity monodromy of the standard family as its counterexample to an implication of those hypotheses.',
 'Complete cited statements and surrounding application read. Proposition2.4 has no separate proof at this locus; the manuscript retains the short exact Leray specialization.')
source('11','https://arxiv.org/pdf/2609.33826v2',
 'Liu–Rollenske, arXiv:2609.33826v2',
 'Proposition2.1 and equation(2.3) pp.3–4; Propositions2.4–2.5 pp.4–5; Lemma2.7 and Corollary2.8 pp.6–7; Proposition2.12 and Definition2.13 pp.7–8; Proposition3.6 pp.9–10; Definition3.7 p.10; Proposition3.9 proof pp.10–11',
 ['LR_v2.pdf'],
 'These loci fix the elliptic source, its line complement and good-root quotient, line character, logarithmic attachment and integral monodromy.',
 'The proof transports the source through the displayed mutually inverse Weierstrass coordinate maps, identifies the good-root lattice and the inverse of the published monodromy, and uses β/4 for the cap. It separately proves the intrinsic Albanese obstruction after one turn and the complete two-turn line/fan closing; the degree-two minimality result is not attributed to these source propositions.',
 'Complete specified statements and proofs read, including the full proof of Proposition3.9. The definition loci were read as definitions, not counted as independent checks.')

scopes={
'0AUW':('Lemma15.22.11 and proof','Torsion-free modules over a DVR are flat.','The analytic local map O_B,c→O_X,x is injective by the identity theorem; the target domain is torsion-free over the DVR. This supplies flatness and vector-bundle flatness.'),
'012O':('Lemma12.24.4 and surrounding morphism construction','A filtered-complex morphism induces the compatible spectral-sequence morphism.','The Leray edge square is the map induced by pullback to a point.'),
'012U':('Definition12.24.9 and convergence context','The convergence notation identifies the limiting page with the cohomology filtration.','The zero-column edge image consists of permanent cycles and lies in the kernel of d2.'),
'012W':('Lemma12.24.11 and proof','A finite filtration gives the asserted spectral-sequence convergence.','The bounded Leray filtration permits the edge-image/permanent-cycle conclusion.'),
'011N':('Definition12.20.1','Morphisms of spectral sequences commute with their differentials.','The comparison used in the edge square respects the d2 kernel.'),
'011O':('Definition12.20.2 and limiting terms','The limiting page records cycles surviving the differentials.','The global degree-two edge class is a surviving zero-column cycle.'),
'09V6':('Theorem20.18.2 and proof','Topological proper base change identifies stalks of the derived direct image with fibre cohomology.','For proper f and {b}→B, the right vertical map is H²(X_b,Z), giving ev_b e(c1L)=c1(L|X_b).')}
for i,tag in enumerate(tags,12):
    p=TMP/f'Stacks_{tag}.html'
    if not p.exists():
        rows.append(dict(source_id=f'II-C3-ANALYTIC-S{i:02d}',url='https://stacks.math.columbia.edu/tag/'+tag,version='Stacks Project, opened22November2026',exact_locus=scopes[tag][0],source_sha256='Unavailable: HTML fetch failed; successful tool reading is recorded, no invented byte hash.',bytes='',established_scope=scopes[tag][1],exact_application=scopes[tag][2],reading_extent='Complete tag page read through the web tool earlier in this bounded pass; '+downloads[tag],date_utc=now))
    else:
        source(f'{i:02d}','https://stacks.math.columbia.edu/tag/'+tag,'Stacks Project, opened22November2026',scopes[tag][0],[p.name],scopes[tag][1],scopes[tag][2],'Complete tag statement and its displayed proof, where present, read through the web tool. The referenced proofs of subsidiary tags were not all opened. '+downloads[tag])

with (OUT/'S6_SERIES_PUBLISH_analytic_sources.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Prepared',len(rows),'source-locus records. Primary bytes remain outside checkpoint.')
for tag,status in downloads.items():print(tag,status)
