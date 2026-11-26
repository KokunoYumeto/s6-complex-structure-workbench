from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime,timezone

prefix='S6_SERIES_PUBLISH_sec07_contracted_duality'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
    row['review_status']='Complete current and receiving P293, CR.1, CR.2 and UN.10 proofs read and compared; all five guards replay once; root admission pending. Bounded transfer only.'
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
data=[
 ('owner','lem:II:contracted-section-duality','Read and compared all of CR.1, CR.2 and UN.10 before extraction, then the complete receiving P293 and all three receiving consumer proofs. P293 uses exactly the local proper-map, full-fibre, normalization, minimal-resolution and effective-divisor data of UN.10. Its finite-duality map is the multiplication/conductor map of P222, whose entire current statement and proof were read. The proper-map restriction preserves S,T,Z,C,V; P281 supplies the same torsion canonical comparison. The formal-functions transitions are surjective on H1 because their kernels have dimension at most one, and the finite-length completion equals the stalk. The coherent Leray bound and section restriction give length g entirely at p0. P234 was read in full and applied to the exact point blowdowns of the ruling for H1(Z,R)→H1(C,R). The residue quotient and all vertical vanishing orders are retained. The new explicit proper-ideal paragraph supplies q in Gamma before the inherited Nakayama step, without using the later global support-equality proof. P228 was read in full and applied only to the delta-one branch-budget subcase.'),
 ('cr1','cdp:st:C.2.CR.1','Read the complete current and receiving CR.1 statements and proofs. The first two proof items move to P293, with C.CR.4 at that owner. Restriction of the original compact proper fibration to a disc leaves its central surface and normalization, resolution, ruling section and divisor unchanged, so every local premise of P293 is present. CR.1 retains its full global hypotheses and all stronger tree, coefficient-gcd, support, fundamental-group, conductor Euler/coherent, and surface Euler conclusions. Its remaining repeated topology and blowup calculations are deliberately still open for the complete contracted-boundary subsection pass.'),
 ('cr2','cdp:st:C.2.CR.2','Read the complete current and receiving CR.2 statements and proofs. The full finite-duality, derived-defect, residue, maximal-ideal, Nakayama and genus-two conductor argument moves to P293 with C.CR.10–14. The CR.2 statement remains a proposition in the precise CR.1 global situation, so its later CR.3 consumer is not silently broadened to the local domain. The receiving proof applies P293 with p0=p and otherwise identical S,T,Z,C,V. Its unique point over q, smooth reduced full conductor ideal (x,y), and generic node/cusp conclusions all remain.'),
 ('un10','cdp:st:C.2.UN.10','Read the complete current and receiving UN.10 statements and proofs. Its first three proof items are now the P293 application with explicit data g, p=pi(C), q=eta(p). No compact ambient threefold, Betti hypothesis or nonzero transgression class enters the common proof. C.UNCR.3 aliases C.CR.12 through exactly the same ideal I_p, canonical pushforward J and residue map to H0(C,omega_C); its alias hook is immediately after begin{equation}. The complete node and cusp local-normalization contradictions and the conclusion g=1 remain. The later bounded consolidation with CR.5/MH.3 remains for the enclosing subsection pass.')
]
source_note=(' Fresh primary source: https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/DvS-Publikationen/DvS_1987_weakly%20normal%20Surface%20Singularities%20and%20their%20improvements.pdf, SHA256 583d6e337304958cb3dfb6519cb8c82901928667ccacfeae74d0e03a19d1e906. Printed pp.60–61 were rendered and opened as images, resolving the obscured extracted duality formulas: Sections2.2.2/2.2.3 and2.2.5(5) give the proper analytic duality, Grauert–Riemenschneider vanishing and isolated-normal-surface canonical quotient used here. This records an exact-locus theorem/application reading; the thesis cites the general theorems and no full-thesis or original-general-theorem proof reading is claimed. All five guards replay once and all old label/target multiplicities are retained. No independent-check credit, required-check increment, integrated compilation or final page reading is claimed.')
events=[]
for suffix,owner,outcome in data:
    event=dict.fromkeys(event_fields,'')
    event.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome=outcome+source_note,event_id='publish:c3:foundations:sec07:contracted_duality:'+suffix,phase='publication local duality consolidation',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group='publish:c3:foundations:sec07:contracted_duality',date_utc=now,where='P293 before CR.1; bounded CR.1/CR.2/UN.10 applications')
    events.append(event)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(events)
lines=['# Bounded contracted-section duality consolidation','',
 'Scope: P293 before CR.1, the CR.1 first-two-item application, the complete CR.2 proof application and the UN.10 first-three-item application. All original/current and receiving proofs were read completely. This is a bounded common-proof transfer inside the still-open contracted ruled boundaries subsection, not a new completed subsection or statement-unit credit.','',
 '| Class | Bounded status | Reason |','|---|---|---|']
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done';reason='The complete bounded receiving text was read for this class; no additional instance remains in this transfer. The enclosing subsection remains open.'
    if kind=='D10':reason='P293 has a titled numbered owner, stable label, permanent tag and exact dependency record; the original statement identifiers and tags remain.'
    if kind=='D12':reason='One proof now owns the repeated finite-duality, formal-functions, residue and genus calculation. Each of the three applications identifies the unchanged spaces, divisors, section and morphisms. The remaining subsection duplication is still open.'
    if kind=='D16':reason='Existing premise and proof closures remain; no statement is removed or reduced to a conditional assertion.'
    if kind in ['D17','D18']:reason='The exact analytic source Sections2.2.2–2.2.5 pp.60–61 was freshly opened and read, with formula images. The full parameter-specific finite-length/residue comparison stays in the common proof; P228 owns the already proved delta-one ring calculation.'
    if kind=='D19':reason='C.CR.4 and C.CR.10–14 use section equation numbering. C.UNCR.3 is the exact C.CR.12 residue-map alias, placed immediately after begin{equation}; all permanent labels and targets remain.'
    if kind=='D25':reason='The common local scope is the already proved UN.10 scope. The ideal inclusion and properness needed before Nakayama are established from the exact residue subsheaf; CR.2 retains its stronger global domain for CR.3. Every original and receiving proof was compared.'
    if kind in ['D14','D24','restructuring']:
        state='open';reason='The bounded proposal orders P293 before its three consumers. Root admission and the complete contracted-boundary subsection consolidation remain; whole-paper placement is not credited by this transfer.'
    if kind=='D23':
        state='open';reason='Source prose, display syntax and all alias placements were read; integrated compilation and rendered page checks remain with root.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')
print(f'{len(rows)} defect rows, {len(events)} exposed-reading events; P293 allocated, bounded status only.')
