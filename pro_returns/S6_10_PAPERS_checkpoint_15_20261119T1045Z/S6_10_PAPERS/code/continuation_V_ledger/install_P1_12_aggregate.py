#!/usr/bin/env python3
"""Install the explicitly reviewed P1.12 union; retain all old complement data."""
from pathlib import Path
from datetime import datetime,timezone
import csv,io,json,hashlib,re,sys
ROOT=Path(__file__).resolve().parents[2]
A=ROOT/'analysis/continuation_V_ledger'
RECEIPT=A/'P1_12_aggregate_installation_receipt.json'
BACKUP=A/'P1_12_aggregate_installation_before'
sha=lambda b:hashlib.sha256(b).hexdigest()
if '--revert' in sys.argv:
    rec=json.loads(RECEIPT.read_text())
    for c in rec['files']:
        p=ROOT/c['path'];assert p.exists()and sha(p.read_bytes())==c['after_sha256'],'Later changes prevent revert: '+str(p)
    for c in reversed(rec['files']):
        p=ROOT/c['path']
        if c['existed_before']:p.write_bytes((ROOT/c['backup']).read_bytes())
        else:p.unlink()
    print('Reverted exactly the unchanged installation outputs.');raise SystemExit
if RECEIPT.exists():raise SystemExit('Installation receipt already exists; refusing duplicate mutation.')

label='night:P1.12'
oldraw=(A/'P1_12_old_target_after_complement_freeze.tex').read_text()
assert sha(oldraw.encode())=='0db1d6ab083e4ee684f05bb21ca2383eaba9d02abec91db527e5931554b8e1d5'
oldproof=oldraw.strip()
staged=(ROOT/'papers/V/revisions/P1_12_marked_leray_proof.tex').read_text()
cut=staged.index('\nThese maps identify the finite attaching diagrams')
prefix=staged[:cut].rstrip()
tail=oldproof[oldproof.index(r'\item Write $L_k'):]
newproof=prefix+'\n\n'+tail
assert newproof.count(r'\item ')==10
assert newproof.endswith(tail)
assert 'maps:src:F.2.6'not in newproof
assert newproof.count(r'\tag{1.12.')==9
proofsha=sha(newproof.encode())

def block(s):
    key=r'\label{'+label+'}';assert s.count(key)==1
    at=s.index(key);starts=list(re.finditer(r'\\begin\{(?:theorem|lemma|proposition|corollary)\}',s[:at]));start=starts[-1].start()
    ps=s.index(r'\begin{proof}',at);end=s.index(r'\end{proof}',ps)+len(r'\end{proof}')
    return start,ps,end
def args(s):
    i=s.index(r'\StatementRecord')+len(r'\StatementRecord');out=[]
    for _ in range(4):
        while s[i].isspace():i+=1
        assert s[i]=='{';a=i+1;i+=1;depth=1
        while depth:
            if s[i]=='{'and s[i-1]!='\\':depth+=1
            if s[i]=='}'and s[i-1]!='\\':depth-=1
            i+=1
        out.append((a,i-1))
    return out
uses=r'\cref{night:P1.1,night:P1.9,night:P1.10,night:P1.11}; the actual marked evaluation and finite logarithmic collar maps; \cite[Theorem 4.1.1 and Lemmas 4.1.2--4.1.3, pp.~480--482]{ffAchingerOgus20}; \cite[Theorem 3.2, p.~195; Theorem 3.30, p.~241; Theorem 4.32, p.~366]{Hatcher2002}'
scope=(r'The complete current ten-step proof has renewed prereading coverage by an explicit union: root\textquotesingle s actual evaluation, transported complex structure and finite logarithmic collar isotopy were frozen at 08:15:08 UTC; the complement, exact boundary kernels, marked collapse and Mayer--Vietoris argument were independently derived by the ledger reviewer before the old proof at 08:48:08 UTC; VI separately rederived the based mapping-space and $\operatorname{Ext}(H_4,\mathbb Z)$ routes before their isolated targets. The Euler substitution is in the ledger reviewer\textquotesingle s frozen proof. The new complement program passed 444 exact checks before target reading; 177 cone-morphism and 145 exported-basis checks then compared every retained displayed matrix, including two-torsion. Root\textquotesingle s fresh program verifies the retained evaluation and collar maps. The old complement steps and their data are retained exactly for P1.19. No value is assumed for a higher cusp suspension map. The renewed source comparison remains at the stated constructed-family scope.')
updates={};blocks=[]
for rel in ['papers/V/body_source.tex','papers/V/body.tex','S6_10_PAPERS_V.tex']:
    p=ROOT/rel;s=p.read_text();start,ps,end=block(s)
    assert s[ps:end]==oldproof,rel+' old proof differs'
    oldblock=s[start:end];newblock=s[start:ps]+newproof
    a,b=args(newblock)[3];newblock=newblock[:a]+uses+newblock[b:]
    # The complete metadata scope is supplied by the exact owner override below;
    # historical typed prefixes are retained for the global metadata application.
    new=s[:start]+newblock+s[end:]
    _,ps2,end2=block(new);assert new[ps2:end2]==newproof
    updates[rel]=new.encode()
    preserved=A/('P1_12_'+Path(rel).name.replace('.tex','')+'_complete_block_before_aggregate.tex')
    assert not preserved.exists();preserved.write_text(oldblock+'\n')
    blocks.append({'path':rel,'preserved_block':str(preserved.relative_to(ROOT)),'old_block_sha256':sha(oldblock.encode()),'new_block_sha256':sha(newblock.encode()),'old_proof_sha256':sha(oldproof.encode()),'new_proof_sha256':proofsha})
updates['papers/V/revisions/P1_12_current_aggregate_proof.tex']=(newproof+'\n').encode()

gatepath='analysis/continuation_V_ledger/completed_row_gates.json'
gates=json.loads((ROOT/gatepath).read_text())if(ROOT/gatepath).exists()else{}
prior_gate=gates.get(label)
gates[label]={
 'proof_rederivation_before_reading':f'complete: exact current ten-step proof SHA256 {proofsha}. Root actual-map setup frozen08:15:08; ledger complete complement/MV derivation frozen08:48:08; VI based-map and Ext routes frozen09:02:04 and09:09:31 before their isolated targets. All retained old Steps2-9 are byte-for-byte unchanged and compared through explicit integral morphisms. Evidence analysis/continuation_V_ledger/P1_12_complement_current_comparison_receipt.json and P1_12_aggregate_installation_receipt.json. This is the explicit scoped union; no reviewer inherits another reviewer\'s proof scope.',
 'new_independent_computations':f'complete: current proof SHA256 {proofsha}. The root independently authored before-read evaluation/collar code covers current Steps1-2; ledger new complement code passed444 exact before-read checks, retaining all Smith transformations, integral boundary and collapse maps. Separate after-read programs passed177 cone-morphism plus145 basis/entry checks, verifying every retained printed matrix and its torsion column. Programs/outputs and scopes are named in the exact comparison and installation receipts; no higher cusp suspension value is inferred.'}
updates[gatepath]=(json.dumps(gates,indent=2)+'\n').encode()
sp='analysis/continuation_root/printed_scope_overrides.json';overrides=json.loads((ROOT/sp).read_text());prior_scope=overrides.get(label)
overrides[label]={'date':'2026-11-19','scope_tex':scope,'basis':'analysis/continuation_V_ledger/P1_12_aggregate_installation_receipt.json; analysis/continuation_V_ledger/P1_12_complement_current_comparison_receipt.json; analysis/continuation_root/P1_12_prereading_frozen_receipt.json; analysis/continuation_VI/P1_12_torus_mapping_spaces_comparison_receipt.json; analysis/continuation_VI/P1_12_duality_Ext_comparison_receipt.json; analysis/continuation_V/P1_12_renewed_credit_comparison.md'}
updates[sp]=(json.dumps(overrides,indent=2)+'\n').encode()

invpath='S6_10_PAPERS_inventory.csv';rows=list(csv.DictReader((ROOT/invpath).open()));fields=list(rows[0]);prior_rows=[]
for row in rows:
    if row['label']!=label:continue
    prior_rows.append(dict(row));row['uses']=uses
    try:notes=json.loads(row['notes'])
    except Exception:notes={'preserved_notes':row['notes']}
    if not isinstance(notes,dict):notes={'preserved_notes':notes}
    notes['continuation_P1_12_aggregate']={'current_proof_sha256':proofsha,'receipt':'analysis/continuation_V_ledger/P1_12_aggregate_installation_receipt.json','retained_complement_steps':'old Steps2-9 byte-for-byte','setup':'root preread actual evaluation and finite logarithmic collar only; the separate F2.6/Leray alternative is not inserted','source_scope':'Known local-cap mapping-cylinder theorem reopened at exact pp480-482; earlier rich credit preserved.'}
    row['notes']=json.dumps(notes,ensure_ascii=False)
assert len(prior_rows)==1
stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows);updates[invpath]=stream.getvalue().encode()

rec={'installed_at_utc':datetime.now(timezone.utc).isoformat(),'label':label,'authorization':'Root explicit message at09:17UTC to install exact aggregate and own proof/computation gate, retain oldSteps2-9, update canonical.','current_proof_sha256':proofsha,'current_steps':10,'old_retained_tail_sha256':sha(tail.encode()),'retained_tail_byte_exact':newproof.endswith(tail),'new_setup_source':'papers/V/revisions/P1_12_marked_leray_proof.tex','new_setup_sha256':sha(prefix.encode()),'excluded_route':'The staged F2.6/transgression and Leray argument is preserved in its prior revision but is not inserted in the current complement proof.','scope_union':['Root first two actual-map setup parts frozen08:15:08','Ledger complement full derivation and444-check computation frozen08:48:08','VI based mapping-space unit frozen09:02:04','VI Ext(H4) unit frozen09:09:31','Ledger frozen Euler substitution; VI does not claim it'],'comparison_receipt':'analysis/continuation_V_ledger/P1_12_complement_current_comparison_receipt.json','old_block_records':blocks,'prior_owner_gate':prior_gate,'prior_scope_override':prior_scope,'prior_inventory_rows':prior_rows,'files':[],'mathematical_status_changed':False,'new_source_credit_field_replaced':False}
for rel,newbytes in updates.items():
    p=ROOT/rel;exists=p.exists();before=p.read_bytes()if exists else b'';bp=BACKUP/rel
    if exists:bp.parent.mkdir(parents=True,exist_ok=True);bp.write_bytes(before)
    rec['files'].append({'path':rel,'existed_before':exists,'backup':str(bp.relative_to(ROOT))if exists else None,'before_sha256':sha(before)if exists else None,'after_sha256':sha(newbytes)})
for rel,newbytes in updates.items():
    p=ROOT/rel;entry=next(c for c in rec['files']if c['path']==rel)
    assert (sha(p.read_bytes())if p.exists()else None)==entry['before_sha256'],'Concurrent change: '+rel
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(newbytes)
RECEIPT.write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps({'installed':label,'current_proof_sha256':proofsha,'steps':10,'retained_old_steps_exact':True,'receipt':str(RECEIPT.relative_to(ROOT))},indent=2))
