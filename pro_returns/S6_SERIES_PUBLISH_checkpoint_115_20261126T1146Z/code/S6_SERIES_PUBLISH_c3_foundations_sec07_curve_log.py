from S6_SERIES_PUBLISH_c3_foundations_sec07_helpers import *
from datetime import datetime,timezone

prefix='S6_SERIES_PUBLISH_sec07_curve'
path=OUT/(prefix+'_defects.tsv')
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
    row['review_status']='Complete original and receiving P282/P4.25/P4.34 statements and proofs read and compared; all four guards replay once; root admission pending.'
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
with (ROOT/'agents/continuation3_foundations/S6_SERIES_PUBLISH_foundations_CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields=next(csv.reader(f,delimiter='\t'))
now=datetime.now(timezone.utc).isoformat()
events=[]
for suffix,owner,outcome in [
 ('duality','lem:II:plane-branch-conductor','Read the complete original P282 and current P4.34 proof, and the complete receiving P282 and P4.34 proofs. Opened https://stacks.math.columbia.edu/tag/0A7M, source HTML SHA256 58dea7487efedc074e4e90f8332778e4083b8f9703bb49a79ca47b1ad90a45f8; read the normalized-complex convention and Lemmas47.16.1,47.16.4,47.16.7 with their complete proofs, including the depth/Ext argument in47.16.5. Apply them to the one-dimensional convergent Gorenstein plane ring A with normalized dualizing complex A[1], finite maximal Cohen–Macaulay normalization B, and finite-length Q=B/A. The explicit Hom/Ext sequence gives A/I=Ext1(Q,A), composition-series Matlis duality preserves delta, and the normalization exact sequence gives length(B/I)=2delta. Finite duality applies on each local finite map A→C{t_i}; the identity at the generic points identifies canonical modules inside the same meromorphic differentials. This gives both the intrinsic conductor exponent and the full residue/intersection formula. The full Hom/Ext proof and sum c_i=2delta move from P4.34 to P282, while P4.34 retains primitive derivative and ramification valuations, c_i=v_i−r_i, tau−r=4delta and every nonplanar defect argument. No surface-duality hypothesis is used for the curve.'),
 ('consumers','night:P4.25','Read the complete current and receiving P4.25 statements and all seven proof items. The generic transverse Cartier slice is the reduced plane curve of P282, with the same normalization branch exponents. Its exponent-one conclusion gives exactly two smooth transverse branches; only that repeated calculation is replaced. The log-canonical residue pullback, full component multiplicities, explicit coordinate changes, isolated-sphere and matching-sphere applications, boundary transports and final normalization maps remain unchanged. P282 now precedes P4.25 and P4.34; its previous P4.34 citation is removed. The already admitted IRR.1 and RAT.3 applications retain the identical branch formula and stable lemma label.')]:
    identity='publish:c3:foundations:sec07:curve:'+suffix
    event=dict.fromkeys(event_fields,'')
    event.update(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; continuation3 foundations',type='used and rechecked in this run',outcome=outcome+' In-memory replay matched all four exact guards once and preserved every old label and target multiplicity. The first source extraction attempt lacked bs4; a standard-library HTML parser then retrieved and exposed the complete cited loci. No independent check, required-check increment, original mathematical refutation or final PDF read is claimed.',event_id=identity,phase='publication proof and prerequisite comparison',source_file=str(path.relative_to(ROOT)),source_event_type='used and rechecked in this run',evidence_group=identity,date_utc=now,where='P282 before P4.25; bounded P4.25 and P4.34 consumer replacements')
    events.append(event)
with (OUT/(prefix+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=event_fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(events)

lines=['# Bounded plane-curve prerequisite transfer','',
 'Scope: P282 and its exact P4.25/P4.34 applications. This file records a prerequisite transfer within existing subsections; it does not declare completion of a new subsection or of either receiving subsection. The complete original and receiving proofs were read. All four guards preserve old labels and targets. P282 is retained; no new statement tag is allocated.','',
 '| Class | Bounded status | Reason |','|---|---|---|']
for kind in [f'D{i:02}' for i in range(1,26)]+['restructuring']:
    state='done'
    reason='The complete bounded receiving text was read for this class; no additional instance remains in this transfer.'
    if kind in ['D12','D17','D18','D25']:
        reason='One-dimensional duality is written at the single P282 owner and mapped to the exact opened Stacks statements. Both consumer ring and residue maps are explicit; their stronger conclusions remain at their original owners.'
    if kind in ['D10','D16']:
        reason='The titled P282 header, permanent P282 target, stable label and hidden dependency record remain; existing closure is preserved.'
    if kind=='D19':reason='No tagged equation is changed or introduced in this bounded transfer; every existing target multiplicity is preserved.'
    if kind=='D23':reason='The receiving proof and displays were read in source; root owns integrated compilation and page-reading gates.'
    if kind in ['D14','D24','restructuring']:
        state='open'
        reason='The exact proposed insertion puts P282 before its first P4.25 use and its P4.34 application. Root admission and final whole-paper placement remain; no relocation alone is counted as subsection progress.'
    lines.append(f'| {kind} | {state} | {reason} |')
(OUT/(prefix+'_status.md')).write_text('\n'.join(lines)+'\n',newline='\n')
print(f'{len(rows)} defect rows, {len(events)} exposed-reading events; bounded status only, no new subsection completion.')
