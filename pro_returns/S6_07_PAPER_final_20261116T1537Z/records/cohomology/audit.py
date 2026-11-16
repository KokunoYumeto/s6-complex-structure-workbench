from pathlib import Path
import json,re,hashlib

B=Path('/workspace/scratch/33c5206c0778')
O=B/'deliverables/records/cohomology'
records=json.loads((O/'records.json').read_text())
prior={
 'AC26':'original/AC26_transcription.tex',
 'E26':'papers/arXiv_2609.38442_Engel_src/S6.tex',
 'DGKX_v1':'papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex',
}
texts={k:(B/'inputs/context'/p).read_text() for k,p in prior.items()}
groups={
 'structure':['R^1f_*','R^2f_*','structure-direct-images','non-reduced','cup product','Proposition 9.13'],
 'cotangent':['Omega_X^1','Omega_X^2','logarithmic cotangent','cotangent direct','h^{1,2}','vertical-log-bundle'],
 'determinant':['6\\mu','E_4^2','E_4(\\tau)^2','mu_z','period determinant','quadratic differential'],
 'scalar':['mu_s','Gamma(1/4)','C_4','0.236609314','Ramanujan'],
 'rank':['kappa_1','R^1f_*E','a\\tau','mu_s','connecting map'],
 'hodge':['Hodge','h^{1,2}','h^{1,1}','h^{0,q}','Dolbeault'],
 'frolicher':['Frölicher','Fr\\"olicher','Frolicher','E_1','E_2','Corollary 9.22'],
 'bc':['Bott','Aeppli','square-zero','N^2','Stelzig'],
 'canonical':['3k','4l','k-1','3l-1','canonical','K_X','Proposition 9.11'],
 'cover':['universal cover','n-1','n+1','Betti','Theorem 7.22','character','dP_6'],
 'torsion':['Omega_{X/B}','relative differentials','torsion','Remark 9.21','xy','xyz'],
 'metric':['balanced','Gauduchon','pluriclosed','astheno','Hermitian-symplectic','locally conformal'],
 'twists':['M_n','T_X\\otimes','twist','-6,-3,-2','epsilon_n'],
 'tangent':['tangent-cohomology','Kuranishi','miniversal','1,1,1,0','3k','4l'],
 'algebraic':['algebraic dimension','a(X)','meromorphic field','small deformation','miniversal'],
}
mapping={
 'notation-cotangent':'cotangent','A1.0':'structure','A1.1':'cotangent','A1.2':'cotangent','A1.3':'cotangent',
 'notation-period-branch':'scalar','A2.1':'determinant','A2.2':'scalar','A2.4':'rank','A3.1':'hodge','notation-hodge-input':'hodge',
 'C1.1':'frolicher','C2.1':'bc','C3.3':'bc','B1.1':'canonical','B1.2':'hodge','B2.1':'canonical','B3.1':'cover','B3.2':'cover','B3.3':'cover',
 'C3.5':'metric','C3.7':'metric','A4.1':'torsion','A4.2':'torsion','A.5.2':'tangent','notation-integral-twists':'twists','C5b':'twists','E.2.1':'tangent',
 'F4 consequence of A.5.2; binding row 6d':'algebraic',
}

def search(g,key):
    lines=texts[key].splitlines()
    return [{'term':term,'count':len(hit:=[i for i,l in enumerate(lines,1) if term.casefold() in l.casefold()]),'line_numbers':hit} for term in groups[g]]

def found(verdict,locators,scope):return {'verdict':verdict,'locators':locators,'scope':scope}
credit={
 'notation-cotangent':{'AC26':found('notation and proposed calculation already described',['Remark 9.21, printed p. 81, line 4330'],'The logarithmic quotient E and divisor D are explicitly introduced; the new definition follows the supplied INV setup.')},
 'notation-hodge-input':{'AC26':found('formal Hodge constraints known; evaluation not established',['Theorem 9.1; Remark 9.21, lines 4307–4330'],'The formal h table and boundary vanishings are known; the separate evaluation h=1 is the INV input.')},
 'A1.0':{
  'AC26':found('same content',['Proposition 9.13, printed pp. 74–76, transcription lines 3858–3935','Lemma 9.12(ii)–(iv), printed pp. 72–74, lines 3707–3856'],'Coarse structure direct images, full-fibre invariant calculation, fixed gamma subline, cusp frame and cup product are already present.'),
  'DGKX_v1':found('same structural content',['Proposition 6.10, label p2:prop:structure-direct-images, lines 9150–9285','Proposition p2:prop:cusp-structure-cup, lines 8814–8880'],'Root direct images, fixed subline and product; coarse invariant exponents in the root-curve calculation. The source proof is retained as a new proof, not a new result.')},
 'A1.1':{'AC26':found('related inputs; full logarithmic statement not found',['Proposition 9.11, line 3643','Proposition 9.23 and proof, lines 4340–4365'],'Canonical line and the fixed vertical field are known inputs; the exact printed cotangent lemma is not present.'),'DGKX_v1':found('overlapping vertical and determinant calculation',['Proposition p2:prop:vertical-log-bundle, lines 8893–9010','Lemma p2:lem:log-tangent-sequence, lines 9015–9070'],'Root relative logarithmic vertical bundle and fixed subline, dual to part of the current source lemma.')},
 'A1.2':{'AC26':found('not found; calculation explicitly left open',['Remark 9.21, printed p. 81, lines 4307–4330'],'The source names the missing logarithmic cotangent direct-image calculation; it does not provide this table.'),'DGKX_v1':found('related root inputs only',['Proposition p2:prop:vertical-log-bundle, lines 8893–9010','Proposition p2:prop:structure-direct-images, lines 9150–9285'],'No printed coarse logarithmic cotangent direct-image table found.')},
 'A1.3':{'AC26':found('not found; calculation left open',['Remarks 1.3 and 9.21, printed pp. 5, 81; lines 270, 4307–4330'],'The absolute cotangent tables and value h12=1 are not established there.')},
 'A2.1':{'AC26':found('input transformations only; identity not found',['Definition 3.1, printed p. 14, lines 710–726','Theorem 3.4(i), printed p. 14, lines 750–752','Section 3.1 modular identities'],'The derivative identity and its determinant divisor were not located; the printed period transformations and modular facts are credited inputs.')},
 'A2.2':{'AC26':found('not found',['Section 3.1 and Remark 3.12 inspected; scalar searches recorded'],'No closed Gamma(1/4) value or mu_s scalar found.')},
 'A2.4':{'AC26':found('not found',['Remark 9.21, lines 4307–4330'],'This missing rank determination is part of the unresolved h12 computation in AC26.')},
 'A3.1':{'AC26':found('partly known',['Theorem 9.1(vi), lines 3248–3272','Proposition 9.13, lines 3858–3935','Proposition 9.20 and Remark 9.21, lines 4240–4330','Remark 1.3, line 270'],'Boundary Hodge numbers, vanishing holomorphic forms and h11=h12+1 are known. The evaluated h12=1 and hence complete numeric table were not proved there.')},
 'C1.1':{'AC26':found('partly known',['Corollary 9.22, lines 4332–4345'],'E1 nondegeneration and injectivity from H01 are already proved. All four ranks and E2 degeneration for the formal h table were not found.')},
 'B1.1':{'AC26':found('original-multiplicity inputs only',['Section 6 admissible fillings','Proposition 9.13, lines 3858–3935','Remark 9.21, line 4330'],'The all-(3k,4l) logarithmic cohomology comparison was not found.'),'DGKX_v1':found('standard (3,4) root inputs only',['Proposition p2:prop:vertical-log-bundle, lines 8893–9010','Proposition p2:prop:structure-direct-images, lines 9150–9285'],'No higher-multiplicity comparison found.')},
 'B1.2':{'AC26':found('partly known boundary data only',['Theorem 9.1 and Remark 9.21, lines 3248–3272, 4307–4330'],'No complete Hodge table even for the standard member; no all-(3k,4l) table found.')},
 'B2.1':{'AC26':found('standard-pair specialization known',['Proposition 9.11, printed pp. 70–71, lines 3643–3681'],'The canonical formula for k=l=1 is known; the all-coprime-(3k,4l) formula and announced middle Hodge values were not found.'),'DGKX_v1':found('standard-pair specialization known',['Relative canonical calculation, equation p2:eq:relative-canonical-bundle, lines 9030–9065','Section 7 anticanonical-pencil calculation, near lines 10040–10070'],'No higher-multiplicity formula found.')},
 'B3.1':{'AC26':found('fundamental group and cusp-topology inputs known',['Theorem 7.17, Section 7.5','Theorem 7.22, lines 3005–3049','Corollary 4.8; Lemma 9.12'],'The cyclic fundamental group is known. The stated cover-normalization and pullback comparison are not located as a combined theorem.'),'E26':found('related standard-collar fundamental-group calculation',['Proposition labelled fundamental-group and its proof, lines 1215–1231'],'The |p|=1 statement and presentation occur; the general n-component cusp/coherent comparison is not found.')},
 'B3.2':{'AC26':found('not found; only underlying topological inputs known',['Theorem 7.22, lines 3005–3049','Remark 9.21, line 4330'],'No cotangent direct-image or Hodge table of the finite universal cover found.')},
 'B3.3':{'AC26':found('partly known inputs',['Proposition 9.11, lines 3643–3681','Theorem 7.22, lines 3005–3049'],'Canonical formula for X and rational homology of X are already known. The Y-character/Hodge/Betti conclusion is not found as printed.'),'DGKX_v1':found('original-member anticanonical pencil known',['Section 7; Theorem p2:thm:intrinsic-fibration, source lines 10018–10069'],'Original-family pencil is known; all finite covers and their character cohomology not found.')},
 'A4.1':{'AC26':found('target assertion conflicts; these modules not printed',['Remark 9.21, printed p. 81, line 4330','Remark 1.3, printed p. 5, line 270'],'The target torsion wording was inspected; no corrected degree-one/degree-two local table found.')},
 'A4.2':{'AC26':found('correction target found',['Remark 1.3, printed p. 5, transcription line 270','Remark 9.21, printed p. 81, final paragraph, line 4330'],'Target prose is not reproduced. The source targets are paraphrased, and the corrected local assertion is credited to INV A4.2.')},
 'C3.7':{'AC26':found('fibre-form input known; metric conclusion not found',['Lemma 9.4 and its proof, Section 9.1, lines 3300–3490'],'The monodromy-invariant fibre form and indefinite Hermitian signature are known inputs. SKT/astheno-Kähler exclusion not found.'),'E26':found('fibre-form input only',['Remark after Section 8, lines 1723–1731'],'The invariant Hodge form and signature (1,1) are discussed, citing AC26; no stated metric exclusion.')},
 'A.5.2':{'AC26':found('partly known tangent inputs only',['Theorem 9.1(iv)–(v), lines 3248–3272','Proposition 9.23, lines 4340–4365'],'h0(T)=1 and chi(T)=1 are known, but the full tangent vector and Kuranishi line are not found.'),'DGKX_v1':found('known entire statement',['Theorem 1.3, label p2:thm:kuranishi-aut, lines 310–327','Theorem 6.12, label p2:thm:tangent-cohomology, lines 9445–9450','Proposition p2:prop:kuranishi-line, lines 9877–9923'],'The tangent vector, smooth reduced Kuranishi line and miniversality are already stated and proved.')},
 'notation-integral-twists':{'AC26':found('Picard normalization input known',['Section 10.6, lines 4770–4778','Theorem 10.5(b), lines 4550–4610'],'Pic(X)=C and the normalization L12=f*O(1) occur; the chosen integral generator is fixed by the marked source transgression.')},
 'C5b':{'AC26':found('nonvanishing input known; complete formula not found',['Theorem 10.5(a), printed pp. 88–89, lines 4547–4610','Lemma 10.3, Section 10.2'],'Nonzero R2f*(TX tensor L) for every Picard twist and the cusp-conormal obstruction are known. The full integral formulas and normalization-rank exception are not found.'),'DGKX_v1':found('untwisted specialization known',['Theorem p2:thm:tangent-cohomology, lines 9445–9450','Lemma p2:lem:ordinary-tangent-correction, lines 9374–9443'],'n=0 tangent vector and ordinary/logarithmic correction are known; all integral twists and their torsion/rank set are not found.')},
 'E.2.1':{'AC26':found('standard-pair inputs only',['Theorem 9.1(iv)–(v); Proposition 9.13'],'No coprime higher-multiplicity tangent result found.'),'DGKX_v1':found('standard-pair specialization known',['Theorem 1.3; Theorem p2:thm:tangent-cohomology'],'The all-(3k,4l) assertion is not found; the (3,4) specialization is already known.')},
 'F4 consequence of A.5.2; binding row 6d':{'AC26':found('memberwise input known',['Theorem 9.1(i), lines 3248–3255'],'Algebraic dimension one for each family member; no Kuranishi-neighbourhood statement found.'),'DGKX_v1':found('miniversality input known; explicit algebraic-dimension corollary not found',['Theorem 1.3, lines 310–327','Proposition p2:prop:kuranishi-line, lines 9877–9923'],'The corollary uses this known input and AC26; no broader stability theorem is imported.')},
}

historical={
 'A1.3':('F','Proof read in full; residue/skyscraper cancellation followed','status/INTAKE_S6_01.md, opening and §2'),
 'A2.1':('F','Statement and full proof read; no independent symbolic rerun claimed','status/INTAKE_S6_01.md, opening and §2'),
 'A2.2':('F,C','Full proof read; scalar independently checked to 40 digits by a different local expansion and separate program','status/INTAKE_S6_01.md, opening and §2'),
 'A2.4':('F','Full proof read; dependence of the global rank on the exact scalar described','status/INTAKE_S6_01.md, opening and §2'),
 'A3.1':('F,D','Hodge table recomputed by hand from the six direct images; stated consistency checks recorded','status/INTAKE_S6_01.md, §2'),
 'C1.1':('F','Full proof read; every spectral-sequence arrow followed, valid for formal h','status/INTAKE_S6_01.md, §2'),
 'C2.1':('F,D','Statement and first half of proof read; Bott–Chern/Aeppli tables recounted by hand from arrows','status/INTAKE_S6_01.md, opening and §2'),
 'C3.3':('F','Proof read, but dependence on unread C3.1 explicitly retained; binding status A','status/INTAKE_S6_01.md, §2 and §5'),
 'B2.1':('F,D','Proof read; canonical vanishing orders checked by hand; Hodge comparison B1.1–B1.2 unread','status/INTAKE_S6_01.md, §2'),
 'B3.2':('F','Proof read; cusp skyscraper mechanism inspected; supporting B3.1 unread','status/INTAKE_S6_01.md, §2'),
 'B3.3':('F','Statement and first half of proof read; Betti comparison to MAPS D.1 recorded','status/INTAKE_S6_01.md, opening and §2'),
 'A.5.2':('F,D','Every direct image and cohomology term recomputed; independent HRR index check; corrected to Known','status/REVIEW_S6_02_FAMILY.md, table A.5.2 and F4'),
 'C5b':('R,D','Bounded intake reads C5b; response records Euler characteristic 1 checked by hand at n=-1,0,12 only; no full independent proof read asserted','status/INTAKE_FINAL.md, opening and §2; status/RESPONSE_INTAKE.md, row 5b'),
}

audit=[]
for rec in records:
    sid=rec['source_id']; g=mapping[sid]
    if rec['paper_label']=='inv:B2.1-hodge':g='hodge'
    per={}
    for key in prior:
        q=search(g,key)
        default=found('not found in the searched file',[], 'No statement matching the full printed content was located; this is a bounded source comparison, not a priority claim.')
        if key=='E26' and g in ('structure','cotangent','scalar','hodge','frolicher','bc','twists','tangent','algebraic'):
            default=found('not found; Dolbeault computations expressly omitted',['Introduction, lines 215–277'], 'The introduction says Dolbeault calculations are omitted; the per-claim full-file terms below were also searched.')
        d=dict(credit.get(sid,{}).get(key,default))
        if rec['paper_label']=='inv:B2.1-hodge':
            d=found('standard-pair boundary constraints known; full table not found',['Theorem 9.1 and Remark 9.21, lines 3248–3272, 4307–4330'],'The original boundary Hodge constraints are known; neither the evaluated standard middle value nor the all-coprime-pair Hodge table is proved there.') if key=='AC26' else dict(default)
        d.update({'source_file':prior[key], 'source_archive':'S6_07_PAPER_context.zip','searched_terms':q,'inspection':'Claim-specific queries were executed across the full file; the relevant theorem/remark passages listed here were opened and inspected. Generic unrelated query hits are not treated as matching statements. No AC26 prose is copied into this record.'})
        rec['found_in_'+key]=d
        per[key]=d
    rec['source_archive']=rec.get('source_archive','S6_07_PAPER_sources.zip')
    rec['produced_by']=[{'model':'GPT-6 Astra','effort':'ChatGPT Pro mode','role':'source producing run'}]
    rec['human_understanding']='none'
    rec['formalization']='none'
    rec['checks'].append({'type':'S','by':'GPT-6 Astra','effort':'ChatGPT Pro mode','date':'2026-11-16','scope':'Source statement and retained proof opened; three prior-source files searched and matched at the claim-specific locators in this record.','verdict':'Source and credit match; no fresh independent proof verification is claimed.'})
    if sid in historical:
        ty,sc,so=historical[sid]
        if rec['paper_label']=='inv:B2.1-hodge':
            ty='R'
            sc='The Hodge clause was read, but its comparison inputs B1.1–B1.2 were explicitly unread. The source review’s canonical-order computation belongs to the separately printed canonical clause, not this Hodge announcement.'
        rec['checks'].append({'type':ty,'by':'Claude Fable 5.2','effort':'high','scope':sc,'source':so,'verdict':'Exactly the bounded review/intake report; not extended to unread dependencies.'})
    elif rec['source_run']=='S6_01_INVARIANTS':
        rec['checks'].append({'type':'source_status','by':'Claude Fable 5.2','effort':'high','scope':'Statement not included among the fully read proofs in the bounded intake.','source':'status/INTAKE_S6_01.md, opening','verdict':'Producing-run proof status only; no second-reader proof check claimed.'})
    if sid=='E.2.1':
        rec['checks'].append({'type':'source_status','by':'Claude Fable 5.2','effort':'high','scope':'Common tangent vector in PUSH E.2.1 and CDP E11','source':'status/RESPONSE_INTAKE.md, row 5c; status/INTAKE_FINAL.md, cross-run finding X3','verdict':'two runs, no second reader'})
    rec['credited_to'] = rec.get('credited_to',[]) + [key+': '+d['scope'] for key,d in per.items() if d['verdict'] not in ('not found in the searched file','not found; Dolbeault computations expressly omitted','not found','not found; calculation left open','not found; calculation explicitly left open') and not d['verdict'].startswith('not found; only')]
    if sid=='C1.1':rec['credited_to'].append('Ugarte00 Theorem 3.2 and Corollary 3.3: general conditional constraints; evaluated ranks use the current Hodge table.')
    if sid=='C2.1':rec['credited_to']+=['McHugh18 §7.1: conditional Bott–Chern/Aeppli formulas','Angella17 Figures 1–2 and §4: double-complex and Bott–Chern relations','Stelzig21 Theorem 3 and Proposition 6(1): load-bearing decomposition and rank interpretation']
    if rec['paper_label'] not in ('inv:B2.1-canonical','inv:B2.1-hodge','fam:A.5.2-corollary'):
        rec['wording_vs_source']['classification']='same content'
    if rec['paper_label']=='inv:B3.3':
        rec['wording_vs_source']['details'].append('In the imported valuation proof only, source x(weight 4),y(weight 3) are interchanged to the first-run x(weight 3),y(weight 4); its auxiliary line is L_root.')
    audit.append({'paper_label':rec['paper_label'],'query_group':g,'prior_source_inspection':per})

# Exact verbatim provenance of the two setup paragraphs, before notation changes.
partA=(B/'inputs/sources/returns/S6_01_INVARIANTS/fragments/part_A.tex').read_text()
partC=(B/'inputs/sources/returns/S6_01_INVARIANTS/fragments/part_C.tex').read_text()
for rec in records:
    if rec['source_id']=='notation-period-branch':
        st=partA.index('\n',partA.index(r'\subsection{A.2'))+1
        rec['source_statement']=partA[st:partA.index(r'\begin{claim}{A2.1}')].strip()
    if rec['source_id']=='notation-hodge-input':
        rec['source_statement']=partC[partC.index('In this section'):partC.index(r'\begin{claim}{C1.1}')].strip()

(O/'records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(O/'credit_search.json').write_text(json.dumps({'date':'2026-11-16','warning':'Search locators and paraphrases only; no AC26 prose is reproduced. Negative findings do not establish priority.','file_digests':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in texts.items()},'claims':audit},ensure_ascii=False,indent=2)+'\n')
(O/'historical_verification.json').write_text(json.dumps([{'paper_label':r['paper_label'],'checks':[c for c in r['checks'] if c.get('by')=='Claude Fable 5.2']} for r in records],ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(records),'three_source_checks':3*len(records),'all_printed_matched':all(r['statement_as_printed'] in (O/'sections.tex').read_text() for r in records)}))
