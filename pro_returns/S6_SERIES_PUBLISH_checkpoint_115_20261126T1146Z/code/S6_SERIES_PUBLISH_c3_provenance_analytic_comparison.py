#!/usr/bin/env python3
"""Bounded exposed proof-comparison records; no shared files or census refresh."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import csv,json,re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation3_provenance/analytic_lr'
old=(ROOT.parents[1]/'tmp/c3_provenance_analytic_lr_old.tex').read_text()
new=(OUT/'S6_SERIES_PUBLISH_analytic_lr_proposed.tex').read_text()
main=(ROOT/'S6_SERIES_PUBLISH_II.tex').read_text()
status=json.loads((OUT/'S6_SERIES_PUBLISH_analytic_status.json').read_text())
assert status['receiving_complete_reading']
now=datetime.now(timezone.utc).isoformat()
notes={
'wbII:lem:curve-flatness':(
 'Nonconstant maps from a connected complex manifold to a curve, every vector bundle, all full fibres, and properness when the total space is compact.',
 'Read the complete local-ring proof. The identity theorem makes O_B,c→O_X,x injective; the target domain is torsion-free over the DVR, so the opened Stacks0AUW criterion gives flatness. The pulled-back parameter is a nonzerodivisor and defines the full Cartier fibre. All consumers use the same nonconstant map and full analytic fibre.'),
'wbII:thm:cartier-duality':(
 'Both old owners: compact full fibres in a compact smooth threefold, and arbitrary compact Cartier surfaces in an arbitrary smooth threefold; q=0,1,2, vanishing above2, naturality, perfect pairings and the normal-line choice.',
 'Read both complete old statements/proofs and the complete receiving cited owner. RR70 identifies i!ω_X[3]=ω_W[2]; locally free F gives Ext^(−q)(F,ω_W[2])=H^(2−q)(F∨⊗ω_W). Compact support equals ordinary cohomology. The full-fibre normal line O_B(b)|b is trivialized by the chosen nonzero vector, with its scalar rescaling retained. Both old tags and both labelled formulas remain accessible at the combined owner.'),
'wbII:prop:analytic-base-change':(
 'Proper complex-space map, coherent f-flat sheaf, fixed point c and H³(X_c,F_c)=0 imply the canonical degree-two fibre isomorphism.',
 'Read the complete old and receiving arguments and the opened BS76III3.4/3.5 statements/proofs. Apply Corollary3.5 with q=3 to the same canonical β_c²; the source theorem gives the exact isomorphism. Mark the known result cited. CDP98 Lemma1.5(c),p.80 is retained solely as its valid top-degree application, not as a premise asserting general local freeness.'),
'wbII:cor:surface-top-base-change':(
 'Proper flat map to a Riemann surface with pure two-dimensional full fibres; all vector bundles; Rq=0 for q>2 and degree-two base change even for nonreduced fibres.',
 'Read the complete finite-free-complex proof. BS76III4.1 supplies the bounded flat-family complex, and the displayed DVR Tor sequence is the canonical fibre map. Highest-degree fibre cohomology vanishing and Nakayama kill the higher sheaves; the remaining Tor₁(R³,k) vanishes. The whole-fibre scope is retained in the reduced-fibre criterion consumer.'),
'wbII:lem:torsion-identification':(
 'Reduced effective Cartier divisors in a smooth complex manifold; kernel of restriction to the smooth locus equals the nonzerodivisor torsion.',
 'Read the full minimal-prime/annihilator proof. Prime avoidance supplies a nonzerodivisor killing a section supported off all generic points; conversely local freeness on the smooth locus kills a torsion restriction. The conductor proof uses the resulting quotient-to-image isomorphism with its explicit inverse.'),
'wbII:prop:conductor':(
 'Possibly nonproper g and noncompact normal-crossing S; normalized trivialization e determines a unique nonzero ambient differential; intrinsic image torsion, zero image exactly for a descending nowhere-zero e; the H⁰(A)=0 clause alone assumes compact connected S and nontrivial A.',
 'Read every old and receiving proof step. Apply A.1.2 by [g]⊗(a_i)↦uΣ_i a_i∏_{j≠i}x_j dx_i and finite projection formula, preserving the conductor square, α/β maps, uniqueness, smooth-locus nonvanishing and restriction to the reduced conductor. AC26Lemma10.2 gives the double/triple conductor ideals, and Lemma10.3 is credited in its proper setup. The descent criterion and compact-connected constant-function argument remain because the stated g itself need not be proper. The kernel, standard-fibre and all-twist consumers were read with their exact e/A choices.'),
'wbII:cor:normal-crossing-kernel':(
 'The conductor setup plus the two endpoint vanishings gives a nonzero kernel of the cotangent connecting map.',
 'Read the complete statement and proof. The ambient nonzero s maps to ρ(s) and the conormal endpoint vanishing makes that map injective; its ambient lift kills δ_A. A.1.1 identifies exactly this section kernel. The only notation change replaces the undefined ambient X by the preceding theorem’s 𝓧 in both occurrences.'),
'wbII:prop:relative-local':(
 'The total-space modules for t=xy and t=xyz are torsion-free and not locally free at the origin; for t=s^m the torsion is R/(s^(m−1))ds.',
 'Read all presentations, maps, kernels and minimal-generator computations. The UFD argument gives the exact relation kernels of the two injections; the special-fibre generator dimension is3 while generic rank is2. The multiple-fibre relation m s^(m−1)ds=0 gives the displayed torsion summand. No numerical program or new theorem is substituted for these calculations.'),
'wbII:rem:relative-local-scope':(
 'The old orphan’s total-space versus fibre scope, nodal torsion, finite étale transport and ramified-quotient qualification.',
 'Read the full old orphan and new numbered remark. The map dx_j⊗1↦d(x_j|S) and its inverse identify M_i⊗R_i/(t) with Ω¹_S because both impose t=dt=0. The nodal torsion element and its two annihilators are supplied by the fully read B1. Flat pullback and faithful flatness transport the displayed multiple-fibre torsion; the ramified transitivity term is explicit. The old paragraph did not assert that the two fibre modules were unequal: this is a map/scope clarification, not a refuted theorem.'),
'def:II:analytic-picard-data':(
 'All formerly orphan marked-family data: standard period matrix, cohomology matrices, finite orders/vectors, overlap connector, zero cusp translation and normalization map.',
 'Read the complete old paragraph, attached pre-split A1.1/A1.2/A3.1 statements/proofs, current cross-paper metadata and the receiving definition. The exact transfer uses β=βpart+c, v=(ε,−ε′), the same Π_c, normalized y↦(q_j(y),s_j(y)) over t_j=s_j^m, the displayed R_j and covariance R_jΠ=Π(g_jz)A_j. PD7 is the finite deck and PD8 its connector; PD11 is the cusp action. This replaces the three obsolete compendium references without opening I or V manuscripts.'),
'wbII:prop:pic0-pullback':(
 'Zero Pic0 restriction to the normalized cusp, the exact all-Picard restriction homomorphism, and the displayed reduction for A_L.',
 'Read the full old/receiving proof. The unimodular toric charts and projectivity identify dP6; Demazure vanishing for O and the GAGA comparison identify H¹(O)=0, and the exponential sequence supplies the precise injective c1 and Pic0 map. The pullbacks along i and η are unchanged. The global conductor and actual-family consumers use these same maps, not a numerical-equivalence substitute.'),
'wbII:prop:analytic-ah-boundary':(
 'All global boundary-cocycle, finite-cap, cusp, nearby-cycle and specialization assertions under tags03IH/03IC/03IE/03ID, with every old equation target.',
 'Read the entire old and receiving long proof: exponential integral cocycle and real pushout; normalized vertical multiplication and crossed-cocycle equations; global product relation and coinvariant balance; filled logarithmic and linear groups, pullback extension, coefficient kernel and norm formula; both quotient squares and connector maps; lifted endpoints and fixed whiskers; central-cover restriction; cusp meridian change with determinant+1 and frame-invariant zero winding; proper-base-change/nearby-cycle square. The primary Schnell convention is introduced before its first use. The finite and cusp actions remain complete with inverses; removing process and defensive phrasing changes none of their equations.'),
'wbII:prop:local-cusp-picard-obstruction':(
 'Locally finite quadratic Cartier divisor, explicit Ψ-equivariant line bundle and descent, central hexagon degrees(−12,2,0,−12,2,0), nontrivial normalization restriction and generic Chern class−2q.',
 'Read the complete old and receiving proof including all six steps. Preserve local monomial Cartier equations, the signed Ψ*D−D character, symmetric PC, h_λχ^m cocycle, divisor-sheaf arrow, equivariant descent, hexagon intersection table, factor inverse and alternating exponential cocycle. The two tagged align blocks and the Chern-cocycle block now convert independently; the earlier untagged pullback calculation is preserved as its own align*. All signs and integer coefficients remain.'),
'wbII:lem:analytic-support-specialization':(
 'Every analytic M on the cusp neighbourhood; mixed Chern entries equal−B(B0λ,m), and zero generic Chern class forces trivial normalized central restriction.',
 'Read all fourteen proof steps. Preserve the integer-valued a(v), polarization B, all toric characters/support signs, exact degree detection in the blow-up basis, component-transitive descent, Stein ray charts and maximal-chart graph, normalized frames, adjacent-chart winding comparison and edge-path propagation. The inverse-dual line map has the required arrow. The residual factor and its horizontal winding give the mixed Chern entry; B0 unimodularity then kills each degree. The ratio’s exact common domain U0 is now stated positively, with the same extending-frame argument.'),
'wbII:thm:analytic-all-picard':(
 'For every global L: zero Leray edge class, zero smooth-fibre Chern class and trivial pullback to dP6; all three old statement tags and equation aliases.',
 'Read the complete proof. AC26 gives E=kq and the order-four specialization lattice; the exact contraction identities for v1,v2 force k even and yield boundary terms4n[δ] and−3n[δ]. Their balance with the proved cusp term forces k=0. Apply the support lemma with M=L|N0 and ν=η. The filtered-complex and proper-base-change square sends c1(L) to fibre Chern classes, and the source inclusion R²f*Z→j*L² detects the zero global edge. Credit the already-published normalized restriction at its exact theorem locus.'),
'wbII:rem:local-cusp-picard-obstruction':(
 'The nonzero local cusp restriction map and the failure of L_Q to extend from the cusp neighbourhood to the global threefold.',
 'Read the full factorization argument. Both maps are pullback along E0→W→N0→X; the explicit local degrees are nonzero while the global composite is zero. Its alternative obstruction uses the already-computed class−2q. The statement makes a concrete assertion about the image of this restriction map, with its full morphism displayed.'),
'wbII:thm:candidate-conductor':(
 'The four explicit hypotheses on compact smooth X, nonconstant f, full reduced normal-crossing fibre, dP6 normalization and H²(X,Z)=0 imply fibre H² and R² nonvanishing for every twist.',
 'Read all three proof steps. Set A_L=(L∨⊗ω_X)|W, use c1 and the exact Picard injection to trivialize η*A_L, apply the conductor owner, then compact Cartier duality to E=TX⊗L. Properness and flatness check the exact q=3 base-change hypotheses. The known compact conductor mechanism is credited to AC26; its generalized four-hypothesis application remains fully spelled out.'),
'wbII:cor:candidate-conductor-actual':(
 'All three nonvanishings for every L on the standard family, including Pic0, under both old statement tags03DR/03DS.',
 'Read the complete current construction and receiving application. The attached k=l=1 cusp charts give the full reduced Cartier fibre and η:dP6→W; the canonical divisor line is trivial near W because the other fibre is disjoint. Global Picard restriction identifies η*A_L. The last two conductor-theorem steps are applied with this E and this full W, retaining the trace, H³ vanishing and exact direct-image fibre map.'),
'wbII:lem:generic-endpoints':(
 'The original arbitrary irreducible reduced analytic parameter space with a Poincaré bundle, dualization stability, and the two specified zero-section points.',
 'Read the full statement/proof. The proper flat universal family gives the BS76 finite free complex; its two determinantal jump loci are proper by the two given points. Dualization takes Q0 to Q0∨ and Serre duality supplies the upper endpoint. Intersecting their complements preserves exactly the original parameter-space scope.'),
'wbII:lem:cdp-generic-endpoints':(
 'Every holomorphic vector bundle on a smooth connected compact Y with a nonzero effective Cartier D whose line lies in Pic0; generic degree-zero and top-degree vanishing on the whole Pic0.',
 'Read the old proof, the complete receiving E17 owner and this replacement. Smooth connected Y has one irreducible associated component and no embedded one, and D meets it; E17 gives V_k=0. Local universal line families and finite free complexes give the global analytic jump locus on Pic0, without assuming a global Poincaré bundle. Apply the same argument to B∨⊗ω_Y and inversion for the top degree. The stronger parameter-space hypothesis of the preceding lemma is not silently imposed.'),
'wbII:thm:corrected-cdp-global':(
 'Integral H¹=H²=0, smooth connected compact threefold with holomorphic algebraic reduction; one degree-two vanishing implies all stated generic endpoint vanishings and index/c3 inequalities.',
 'Read every old and receiving step and the complete C1.1 owner. Tensoring with Q gives b1=b2=0; its Picard-component map gives Pic=Pic0=H¹(O), with the same explicit exponential universal family. The fibre divisor supplies endpoint disappearance and the one vanishing point kills the degree-two jump locus. Apply C1.1 with Y=X,L=M and the complex orientation to χ=½∫c3. This replaces the repeated HRR proof while preserving every conclusion and equation alias.'),
'wbII:cor:corrected-cdp-relative':(
 'The same setting; existence of one L with R²f*(TX⊗L)=0 suffices for the global conclusions.',
 'Read the full short specialization and the published Proposition2.4,p.680. Projection formula with A^m on the compact base kills the R² term; Serre vanishing kills H¹(R¹⊗A^m); the two-column Leray sequence gives H² for L0=L⊗f*A^m. The exact twist and map are retained.'),
'wbII:thm:corrected-cdp-fibrewise':(
 'Every full fibre reduced; the two endpoint vanishings and injective connecting map on the whole reduced Cartier fibre imply all relative/global conclusions.',
 'Read the complete old and receiving proofs. A1.1 identifies the ambient group with kerδ_c using the two end groups. Apply the earlier curve-flatness owner and combined Cartier duality to E=TX⊗L and a nonzero normal vector, including singular reduced fibres. The uniform top-degree base-change owner and Nakayama kill every R² stalk. The multiplicity scope is not widened to reduction-only testing.'),
'rem:II:reduced-fibre-connecting-scope':(
 'The full content of the old scope paragraph: the reduced-fibre kernel equivalence and the need for nilpotent layers on a nonreduced full fibre.',
 'Read the old paragraph and the full receiving remark, plus A3.1/A3.3. The same two endpoints identify ambient sections with kerδ_c. For J=ker(O_W→O_Wred), local freeness gives graded pieces E_W⊗J^j/J^(j+1). For W=mS, A3.1 supplies exactly the conormal powers and extension maps, and A3.3 supplies finite Picard translations. Global/relative criteria retain their full-fibre scope.'),
'rem:II:invariant-lattice-spanning':(
 'The old final spanning condition, the consequence of trivial integral monodromy and the standard-family failure of the implied spanning conclusion.',
 'Read the old paragraph, complete D1.10/D1.7/C3.11 and the receiving remark. The map is H¹(F,Z)^π1→H¹(F,O_F). For a torus its complexification is the surjective Hodge projection; in the b1=q=1 branch a nonzero integral generator has nonzero coefficient image and spans. In the marked family T2v=v gives c=b,d=2b and T1’s first row gives2d=6c, hence invariants=Zγ, with nonzero one-dimensional image in q=2. The published proof’s final paragraph is correctly located on p.86.'),
'wbII:test:cdp-comparison':(
 'For every twist on the standard compact threefold, global H² and relative R² are nonzero; the separate conductor reason for R² remains.',
 'Read the complete old and receiving corollary. The exact standard-family inputs are integral H¹=H²=0, holomorphic algebraic reduction and c3=2. A single vanishing twist would contradict the proved global criterion; a vanishing R² would supply that twist by the relative criterion. The cusp owner independently constructs the direct-image fibre class. AC26 is credited for the published general-twist counterexample and positive index, with the all-twist consequence justified by these displayed maps.'),
'ii:LR:covering':(
 'The fixed scalar, good fourth root, logarithmic vector, every constant root-line character, periodic cusp fan and attachment maps; a proper logarithmic family, no one-turn biholomorphism, descent to u=w² and minimality.',
 'Read all old and receiving proof steps and the cited LRv2 loci. Preserve the central torus lattice, root deck/character, invariant lattice, τ-shift and mutually inverse Albanese coordinate maps; the exact SL2Z estimate excludes one-turn endpoints. Preserve the source Weierstrass maps and inverses, line and meridian transport, and sphere input; E1 then gives the identical pullback field isomorphism, replacing its duplicate divisor proof. Preserve the divisor-line square C²=tB0, good-root coordinate map/inverse, cap anticommutation, attachments, cusp unit maps with inverses, full norm identity and free parameter quotient. All source-dependent constants, all characters and all fan faces remain covered.'),
'night:P3K.36':(
 'The complete printed current remark: the fixed LR data have minimal cover u=w², followed by the unchanged IV references for return classes and source/cap calculations.',
 'Read the complete printed remark and the full receiving 01RO theorem/proof. Its fixed scalar, root, vector, character, fan and attachments are exactly the inputs of 01RO; its minimal-cover assertion is therefore a direct application, with every character retained. Correct only the hidden legacy status false→proved and add that dependency. The three IV reference keys and all printed scope remain byte-identical; no IV mathematical result was rederived or its manuscript opened.')
}
owners=[o for sec in status['structure'] for o in sec['owners']]
assert set(owners)==set(notes),(set(owners)-set(notes),set(notes)-set(owners))
labels=set(re.findall(r'\\label\{([^}]+)\}',main+new))
sref=set(re.findall(r'\\csname SRef@([^\\]+)\\endcsname',main))
unresolved=[]
for m in re.finditer(r'\\(ref|eqref|cref|Cref|SeriesRef)\{([^}]+)\}',new):
    for key in m.group(2).split(','):
        key=key.strip()
        if key not in labels and not(m.group(1)=='SeriesRef' and key in sref):unresolved.append((m.group(1),key))
assert not unresolved,unresolved
bib=set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',main))
for m in re.finditer(r'\\cite(?:t|p)?(?:\[[^\]]*\])?\{([^}]+)\}',new):
    assert all(k in bib for k in m.group(1).split(',')),m.group()
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{(tag-[^}]+)\}']:
    a=Counter(re.findall(pattern,old));b=Counter(re.findall(pattern,new))
    assert all(a[x]==b[x] for x in a),(pattern,a-b)

def tsv(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

events=[]
for owner in owners:
    events.append(dict(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 provenance',
        type='used and rechecked in this run',outcome=notes[owner][1]+' Exposed old/receiving comparison; no independent derivation or final rendered-page credit.',
        event_id='publish:c3:analytic:'+owner,phase='publication text and proof comparison',
        source_file='agents/continuation3_provenance/analytic_lr/S6_SERIES_PUBLISH_analytic_CHECK_EVENTS.tsv',source_row='',
        source_event_type='used and rechecked in this run',evidence_group='publish:c3:analytic:'+owner,
        publish_input_file='',publish_input_row='',date_utc=now,where='Complete bounded old/receiving owner and changed premise/consumer maps'))
alias='wbII:prop:cartier-duality-absolute'
events.append(dict(events[owners.index('wbII:thm:cartier-duality')],statement_id=alias,
    event_id='publish:c3:analytic:'+alias,
    outcome='Read the complete old absolute Cartier-duality statement/proof and the entire receiving combined cited owner. Its arbitrary smooth ambient threefold, compact effective Cartier surface, locally free E, perfect H²/H⁰ trace pairing, chosen normal vector and functoriality all remain. Tag03IJ is a co-located alias of that full scope; the proof applies the same RR70 dualizing-complex map. This shares the exposed duality comparison evidence, with no independent-check claim.'))
tsv('S6_SERIES_PUBLISH_analytic_CHECK_EVENTS.tsv',events)

evidence={
'D01':'Read the entire bounded source and receiving text; removed process introductions and the internal scope/correction titles. Published corrections retain exact locators.',
'D02':'Removed defensive contrast clauses only after retaining their precise quotient, domain, frame and winding maps in positive mathematical form.',
'D03':'No numbered statement addresses a private proposal. The local/global Picard image result names its actual morphism; the CDP consequence identifies the published theorem.',
'D04':'Resolved all changed local reference keys against current II labels or the existing SeriesRef dictionary. Every old label and target has the same multiplicity.',
'D05':'The marked family is defined through its periods and attachment maps; no prompt item is a mathematical input.',
'D06':'Replaced all three compendium references by current numbered construction owners and the exact normalized finite/root/cusp maps. No CompendiumRef remains.',
'D07':'No worker, run, model or private file name is in this body proposal.',
'D08':'Exact occurrence rows remove actual, retained, before-naming and literal process emphasis while preserving ordinary coordinate choices.',
'D09':'The bounded body contains no program path or bookkeeping. Matrix identities and divisor calculations retain inputs, method and exact outputs; no paper program is added.',
'D10':'The inherited tag-only renderer is untouched. All old target/label multiplicities are preserved; metadata changes print no machine header.',
'D11':'Scope is stated once in the numbered owners or the precise reduced/nonreduced and finite-base-change remarks; every old mathematical clause remains.',
'D12':'Both duality owners are consolidated with both complete scopes. The normal-crossing map, divisor-vanishing input, index calculation and LR field argument use their fully read earlier owners. Additional explicit boundary/descent proofs remain single owners.',
'D13':'Marked periods receive DefinitionP309; connecting-map and invariant-span consequences receive RemarksP311/P312; the former relative-scope paragraph becomes numbered Remark03IR.',
'D14':'Seven mathematical sections put all changed local premises before their consumers. Their final lengths, placement after sign development and whole-paper order remain root integration gates.',
'D15':'This proposal changes no front matter. Root must synchronize final summaries, outline and methodology/count claims after text-final admission.',
'D16':'Every receiving owner has a mathematical title. The inherited closed title/renderer status remains preserved.',
'D17':'Opened exact known-source loci and replaced the duplicate duality, normalization, index, divisor and field arguments by their precise applications. The generality beyond a source hypothesis is identified explicitly in the owner comparison.',
'D18':'The source table records exact versions, loci, hashes, application maps and reading limits. The CDP final-span page is86; LR’s root-action citation now gives Lemma2.7(ii)–(iii),p.6. Final bibliography sorting/rendering remains global.',
'D19':'All manual display numbers in this bounded region use section counters; old targets/labels stay exact and formerly bare LR references receive stable equation labels.',
'D20':'The exact period and root-coordinate maps retain all conversions. The relative fibre modules have an explicit canonical isomorphism/inverse, and the conormal ambient symbol agrees with the preceding owner.',
'D21':'Only exact mathematical identities and inequalities are stated. There is no theorem asserting numerical agreement or a check count.',
'D22':'The two monodromy equations now prove the invariant lattice at its use; root orders, divisor coefficients, character shifts and cusp degrees retain their explicit reasons.',
'D23':'The proposal passes balanced environment and no-blank-paragraph-in-display guards after a conversion error was caught and fixed during full reading. Final pdfLaTeX layout and page reading remain root gates.',
'D24':'The seven-section order and all receiving owners are recorded for the final §1.6/dependency figure. No final-structure closure is asserted.',
'D25':'Changed applications were read with their full hypotheses and exact maps. No theorem is declared refuted in this unit. The hidden02UH status now matches the full proved01RO scope; the earlier A2 metadata error has separate correction151.'}
unitrows=[]
for sec in status['structure']:
    for typ,text in evidence.items():
        state='source comparison complete; final integrated-page gate pending'
        if typ in {'D10','D16'}:state='inherited closed; preserved'
        if typ in {'D14','D15','D24'}:state='root final ordering/front-matter gate pending; bounded source pass complete'
        if typ=='D23':state='source display guards passed; integrated typesetting/page gate pending'
        unitrows.append(dict(unit=sec['section'],type=typ,status=state,evidence=text,owners='; '.join(sec['owners'])))
tsv('S6_SERIES_PUBLISH_analytic_unit_status.tsv',unitrows)

report=['# Complete exposed comparison: analytic duality through LR parameter covering','',
 'The full original 3501-line bounded region and every complete receiving statement and proof were read. The records credit only **used and rechecked in this run**. They claim no independent proof, source admission, final build, rendered-page completion or check-count recomputation.','',
 '## Order and scope','']
for sec in status['structure']:report.append('- '+sec['title']+': '+', '.join(sec['owners'])+'.')
report+=['','The combined fragment replaces the region beginning with Analytic duality and ending after night:P3K.36, before the following part. Its LR-only section is separately named analytic_lr_covering_proposed.tex, so it does not overwrite the combined file. P307/P308/P310/P315/P316 are section tags; P309 is the definition and P311/P312 are remarks. P280/P313/P314 remain unused.','',
 '## Complete owner comparisons','']
for owner in owners:
    report+=['### '+owner,'','**Preserved scope.** '+notes[owner][0],'','**Comparison and application.** '+notes[owner][1],'']
report+=['## Source and reference checks','',
 'The source table contains18 exact-locus records, with downloaded primary bytes outside the checkpoint and our paraphrases here. It distinguishes full proofs, complete statements and source-defined objects. The CLS hash is explicitly the hash of web-retrieved primary-text excerpts, not a fabricated PDF hash. The failed direct PDF fetch is excluded. Stacks source HTML was downloaded after the full tag-page reading and hashed.','',
 'All local reference keys resolve in the bounded proposal or current II labels; SeriesRef keys resolve through the existing dictionary. Final cross-paper regeneration remains a root gate. The complete old label/tag multiplicities are preserved. No CompendiumRef or manual equation tag remains.','',
 'The 03IR edit supplies the quotient and canonical fibre-differential isomorphism; its original prose did not assert that the two fibre modules were unequal. There is no refuted-theorem event for that clarification. The 02UH current printed minimal-cover assertion follows from the complete01RO theorem for precisely its fixed data, including every constant root-line character. Its IV reference sentences are unchanged and no IV manuscript was opened.','',
 'The receiving read caught and fixed an equation converter spanning an earlier untagged align* block. It now processes each complete align* block separately. It also avoids interpreting the second slash of a row-spacing command as a display opener and removes blank paragraphs left by manual-tag removal. The final bounded guards check balanced environments and the concrete display errors; they are editorial verification, not new mathematical computation checks.','',
 '## Integration boundaries','',
 'Root admits the source and records, merges29 exposed-comparison event rows (28 receiving physical owners plus the formerly separate absolute-duality owner sharing the same comparison evidence), and performs the integrated build and page reading. The seven per-section tables preserve D10/D16 as inherited closed and leave the final D14/D15/D23/D24 gates explicit. Unit creation itself is not claimed as movement. No main manuscript, central event file, register, records census, receipt or manifest was written.','',
 'Stable metadata proposals147–148 (Guillot),149 (Dloussky–Teleman),150 (D1.10 page86),151 (record-only A2 paraphrase correction) and152 (Ulmer–Urzúa) are separate. They do not change the unique records URL, commit or deferred deposit/count fields.']
(OUT/'S6_SERIES_PUBLISH_analytic_comparison.md').write_text('\n'.join(report)+'\n',newline='\n')
print(f'Prepared {len(events)} exposed-comparison events, {len(unitrows)} local class-status rows and complete owner report. No shared writes.')
