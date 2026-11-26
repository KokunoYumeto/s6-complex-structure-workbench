from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime,timezone

prefix='S6_SERIES_PUBLISH_sec07_pushout'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:row['review_status']='Complete current and receiving P210/R3/R7 statements and proofs read and compared; complete P294 proof read; all seven guards replay once; root admission pending.'
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
events=[]
data=[
 ('owner','lem:II:proper-conductor-pushout','Read the complete repeated quotient and cylinder arguments in current P210, R3, R7 and CR1, the first complete P294 proof including both explicit cylinder homotopies, and the complete shortened receiving P294 proof. Freshly opened the primary Hatcher Cornell PDF, SHA256 bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618. Read Proposition0.16 and full proof p.15, Proposition0.18 and full proof p.16, Lemma1.15 and full proof p.35, Theorem1.20 and full proof pp.43–46, Mayer–Vietoris and its chain-complex derivation pp.149–150, Proposition4G.1 and full proof p.458, and the exact canonical HEP pushout statement in the first paragraph p.459. Also read the graph construction and examples pp.92–93; the narrower injective graph-group theorem is not invoked. The standard HEP/cylinder and van Kampen proofs are replaced by those exact primary applications. The retained comparison identifies the quotient X disjoint-union C→Y fibre by fibre and shows that the canonical cylinder collapse restricts to h on X and to inclusion on C. Its group inverse remains k_*j_*^−1 on pi1(X) and identity on pi1(C). For disconnected A/C the actual edge homomorphisms may be noninjective: edge-path transport gives the displayed conjugacy relation. With connected X its graph has 1+s vertices and r edges, giving r−s stable letters and the stated free quotient. The statement assumes the finite CW/subcomplex data and makes no general triangulability assertion. This is an exact-locus source reading, not a full reading of the book.'),
 ('p210','prop:II:minimal-boundary-complements','Read the complete current and receiving P210 proof, all six items and each minimal-boundary case. Its substitution is (X,Y,A,C,h)=(Z,S,Dred,Gammared,eta pi), with the actual full inverse-image equality and complement isomorphism from A5.16. Both Z and Dred are simply connected in these two negative-boundary cases, so the same inclusion-induced isomorphism follows. A.RT.18 and A.RT.19 retain their exact displayed maps, labels and permanent targets. All plane-cubic cases, Hirzebruch intersection calculations, chosen blowup count, endpoint universal-cover argument and stronger e(Gammared)≥2 bound remain. The rational-curve graph step applies the already proved P245.'),
 ('r3','night:P4R.3','Read the complete current and receiving R3 statements and seven-item proofs. The minimal-bundle coordinate basis, adjunction and Riemann–Hurwitz exclusion, coefficient comparison and section-with-trees construction remain. The smooth finite normalization makes its nonisomorphism locus exactly the singular curve C, so (X,Y,A,C,h)=(T,S,Dred,C,nu) satisfies P294. Its connected edge map j_* is the isomorphism already proved by the ruling and P246. The inverse on the source group is explicitly (nu|Dred)_* j_*^−1. The virtually abelian curve consequences, e(C)≥0, equality exclusion and strict positivity e(S)>0 remain.'),
 ('r7','night:P4R.7','Read the complete current and receiving R7 statements and two-item proofs. The effective resolved divisor, higher-genus adjunction, blowup incidence operations and commuting P246 maps remain. R6 supplies A=rho^−1(C) and the complement isomorphism for rho=nu pi, including every contracted exceptional component. The connected P294 application uses exactly (T,S,A,C,rho); the original inverse identity on pi1(C) and (rho|A)_* j_*^−1 on pi1(T) is retained. All virtual-abelian, curve-normalization and nonnegative-Euler conclusions remain. The repeated connectedness sentence is stated once before the application.')
]
for suffix,owner,outcome in data:
    identity='publish:c3:foundations:sec07:pushout:'+suffix
    event=dict.fromkeys(event_fields,'')
    event.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome=outcome+' Freshly opened Lojasiewicz1964 original Numdam PDF, SHA2565efc756a499a43f542f782a0fa565d30e9adf083786f8e778a8133bd55a8f203; read Theorem1 conditions pp463–464 and Theorem2 with its Grauert-embedding deduction p464. These apply to each smooth real analytic source surface and its compact analytic boundary. This is an exact theorem/application reading, not a full reading of the separate Section4 triangulation proof. All seven guards replay once and every existing label/target has unchanged multiplicity. No independent check, required-check increment or final PDF reading is claimed.',event_id=identity,phase='publication topology proof consolidation',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group='publish:c3:foundations:sec07:pushout',date_utc=now,where='P294 before P210; bounded P210/P4R.3/P4R.7 applications')
    events.append(event)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(events)
lines=['# Bounded conductor-pushout consolidation','',
 'Scope: new P294 before P210 and the exact P210/P4R.3/P4R.7 consumer replacements. Complete original/current and receiving proofs were read. This package does not declare completion of a new subsection or of any whole receiving subsection. Root will apply the disconnected clause in its separate Hopf calculation. CR.1/UN.7 applications will be included in their later subsection packages.','',
 '| Class | Bounded status | Reason |','|---|---|---|']
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done';reason='The complete bounded receiving text was read for this class; no additional instance remains in this transfer.'
    if kind in ['D12','D17','D18','D25']:reason='The quotient and cylinder construction has one complete owner. Its standard HEP/pushout and van Kampen steps apply the freshly opened exact Hatcher loci; the short retained comparison identifies the actual proper quotient maps, inclusion-induced group inverse and disconnected stable-letter count. Every application verifies the identical spaces and support maps; the cited triangulation hypotheses were checked at the primary locus.'
    if kind in ['D10','D16']:reason='P294 has a titled numbered owner, permanent tag, stable label and hidden dependency record. Every existing statement/equation identifier is retained; existing closures remain.'
    if kind=='D19':reason='All existing numbered equation payloads, labels and targets remain; P294 has no new tagged equation.'
    if kind=='D23':reason='The receiving displays and whole source proofs were read; root owns integrated compilation and final page-reading gates.'
    if kind in ['D14','D24','restructuring']:
        state='open';reason='The proposal places P294 before its first P210 use and resolves the repeated R3/R7 constructions. Root admission, disconnected Hopf application and final whole-paper placement remain; no movement alone is counted as subsection progress.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')
print(f'{len(rows)} defect rows, {len(events)} exposed-reading events; P294 allocated, bounded status only.')
