"""Preserve build49 and include the four complete audited proofs K57--60."""
from datetime import datetime,timezone
from pathlib import Path
import ast,hashlib,json,shutil

root=Path(__file__).resolve().parents[1]
for file in ['records/qa_k57.json','records/k58_standalone_visual_qa.json',
             'records/qa_k59.json','records/k60_standalone_visual_qa.json']:
    data=json.loads((root/file).read_text())
    assert data.get('status')=='PASS' or data.get('visual_review')=='PASS',(file,data)
for file in ['records/root_audit_source_infinity_corrected_norm.json',
             'records/root_audit_source_zero_native_square.json',
             'records/k59_fourfold_audit.json']:
    data=json.loads((root/file).read_text())
    assert data.get('status')=='PASS',(file,data)
dest=root/'records/checkpoint15_prior_master49'
dest.mkdir(exist_ok=False)
names=['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log',
       'S6_06_BLIND_report.md','S6_06_BLIND_results.csv','code/update_report.py']
record={'utc':datetime.now(timezone.utc).isoformat(),'master_build':49,
        'reason':'Preserve the prior master and report before including K57--60.','files':{}}
for name in names:
    source=root/name
    target=dest/source.name
    shutil.copy2(source,target)
    record['files'][name]={'bytes':source.stat().st_size,
       'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
assert record['files']['S6_06_BLIND_paper.pdf']['sha256']=='b54d3bfc27df3460dc0e60374ad4ff41955d913daf65705c9a16b930f0585775'
(dest/'preservation.json').write_text(json.dumps(record,indent=2)+'\n')
parts=['source_infinity_return','source_global_groupoid',
       'source_cusp_mutation_staircase','source_zero_native_square']
p=root/'notes/part3.tex'
text=p.read_text()
for name in parts:
    path='notes/part3_'+name+'.tex'
    assert (root/path).is_file(),path
    include='\\input{'+path+'}'
    assert include not in text,include
    text+='\n'+include+'\n'
p.write_text(text)

p=root/'code/update_report.py'
text=p.read_text()
start='The source-infinity working construction now supplies'
end='Individual source-zero returns, the general source-loop fan formula beyond the proved vertical-edge sector, remaining source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under proof; no uncomputed loop is assigned a class.'
first=text.index(start)
last=text.index(end,first)+len(end)
old=text[first:last]
assert text.count(old)==2
new='P3K.57 supplies the complete source-infinity partial filling, relative excision, signed finite-isotropy residue calculation and actual Hopf-lift transfer. Its fixed-scalar positive epsilon return classes are0 and1 in the good and reduced branches, on the initial and reflected vertical-edge fans, for both norm signs. The analytic norm budget was corrected after checkpoint14: it includes the nodal metric and source-reindex losses, giving orders N-5 and N-6. The executed geometric orders N=8 and N=6 satisfy these bounds; the lower-order fan certificates are arithmetic only. The earlier wording is preserved with the explicit correction. P3K.58 constructs the full global source-loop groupoid and the exact infinity source/Cartier/root dictionary. Its paired source-zero sums are-1 and-2+2k(1-3p), with the original scalar root winding-2k and every cap closing arrow retained. P3K.59 proves the actual native Cox mutation and selected-coordinate update, then two infinite source-loop fan families by exact induction. For P_j=[[1,-j],[0,1]], j>=0, it gives the full variation matrix and derivative and the class1-3j(j+1); for R_j=[[j+1,-j],[-1,1]], it gives class-5-24j(j+1), least period7 and range{3,15,19,23}. Its active finite certificate uses only the proved initial seed and checks210 basis states and128 fan states; the earlier exploratory second seed is preserved and supplies no proof input. P3K.60 constructs the literal single native source-zero product, its exact doubled pullback, and the full Cox seam on both small resolutions. The actual relative square has native free pair(2-2a,2a), which determines the single pair(1-a,a) through the injective doubling map on the two integer coordinates. The single-loop flop therefore gives Z_JT-Z_T=a in Z/28. Combined with P3K.58, the actual pair is(-a+k*A_scalar+14e,k*A_scalar+14e), e in{0,1}, with A_scalar=0 or1-3p in the good or reduced branch. The common order-two ambiguity remains open and may depend on the retained family data. In the smallest good case the two allowed pairs are(27,0) and(13,14); for reduced p=k=1 they are(24,26) and(10,12). No individual return is selected. These four full proofs are included in the numbered master. The actual source-zero collision-to-cap central attachment, the remaining source-loop fan entries, source-moduli loops, added ordinary OS49 clutch sectors and additional unmarked endpoint symmetries remain under proof; no uncomputed loop is assigned a class.'
assert "'" not in new
text=text.replace(old,new)
text=text.replace('P3K.40–P3K.56','P3K.40–P3K.60')
ast.parse(text)
p.write_text(text)
print('Preserved build49 and included K57--60; report source updated. No archive created.')
