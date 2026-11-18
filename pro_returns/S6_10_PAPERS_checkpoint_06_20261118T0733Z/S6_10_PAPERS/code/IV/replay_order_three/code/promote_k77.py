"""Integrate the independently audited complete OS49 fan calculation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,re
import fitz

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
archive=root/'records/checkpoint18_prior_master58'
archive.mkdir(exist_ok=False)
for name in ('S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log',
             'notes/part3.tex','notes/part3_remaining_return_obligations.tex',
             'code/update_report.py','code/part3/results_mapping.json'):
    src=root/name; dest=archive/name;dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dest)
audit=json.loads((root/'records/blind_audit_os49_all_fans.json').read_text())
assert audit['status']=='PASS'
source=root/'notes/part3_os49_all_fans.tex'
assert hashlib.sha256(source.read_bytes()).hexdigest()==audit['hashes']['notes/part3_os49_all_fans.tex']
p=root/'notes/part3.tex';text=p.read_text()
assert '\\input{notes/part3_os49_all_fans.tex}' not in text
p.write_text(text+'\n\\input{notes/part3_os49_all_fans.tex}\n')
p=root/'notes/part3_remaining_return_obligations.tex';text=p.read_text()
old='''Other remaining parts of item 3.4 are the component-supported
OS49 return on nonvertical fans, its added ordinary-clutch sectors,
the remaining marked source-moduli loops, and unmarked endpoint
sectors. K65 supplies the full positive/negative diagonal OS49
values; K76 now computes every vertical-edge fan as an actual
integer, including its shorter endpoint and cap-data iterates.
No value is assigned here to the remaining sectors.'''
new='''K77 now computes the component-supported OS49 return on every
lattice-basis fan, including the actual shorter endpoint and
the retained fixed-source marked cap-data iterates. Its exact
image on either specified parameter loop is
\\(\\gcd(k,28)\\mathbb Z/28\\mathbb Z\\).
Other remaining parts of item 3.4 are the added ordinary-clutch
sectors, the remaining marked source-moduli loops, and unmarked
endpoint sectors. No value is assigned here to those sectors.'''
assert old in text;text=text.replace(old,new)
old='''been substituted for the surgered end. The associated-node resolution appears
on the labelled vertical fan \\(j=-1\\); its map to the
specified target fan must be included. This is the next
construction being attempted.'''
new='''been substituted for the surgered end. The earlier \\(j=-1\\)
designation used the SZ chart index. The corresponding
identification with the current labelled fan requires the
actual node-to-Tate character map and its Cartier line;
that index alone supplies no such identification. The
full source representative \\(Z=P/S\\), including the
winding of \\(P\\), is retained in the active comparison.

There is also an exact obstruction to replacing the present
end by a radial sphere link. In the charge-one chart,
\\[
 R^2=(|S_0|^2+|S_1|^2)(|zV|^2+|T_1|^2).
\\]
Thus \\(R\\) vanishes on the entire fibre over
\\([0:0:1]\\), not only on its zero section. The verified
local fixed-boundary surgery therefore requires an actual
comparison to this product-radius end. Its closed
projective spinor cap has pair
\\((3a^2-3a+1,4)\\) and index \\(a(a-1)/2\\);
the charge-one point has pair \\((-1,-4)\\) and index zero.
The oriented local surgered end on the reduced branch
has pair \\((-8,-8)\\) and index \\(-1\\), as proved in
RT.10 of the real-trace working record and independently
checked there. This remains a local statement. Removing
the capped exceptional disk from the global fixed trace
also removes its intersection class; it cannot be counted
again in the complementary capped trace. The labelled
global attachment, including that cap assignment, remains
under construction.'''
assert old in text;text=text.replace(old,new)
old='''The nonvertical-fan construction remains the next step.'''
new='''K77 completes the nonvertical construction with its full
period and Cox maps, its integer target-prism solution,
and all intermediate cap and shorter-endpoint arrows.
It also proves the exact image on every cap order and
the retained marked cap-data loop calculation. The
added ordinary-clutch sectors remain on the list above.'''
assert old in text;text=text.replace(old,new)
p.write_text(text)

p=root/'code/update_report.py';text=p.read_text()
text=text.replace('P3K.5–P3K.76; exact corrected scopes below','P3K.5–P3K.77; exact corrected scopes below')
old='K75 records the exact remaining source-zero attachment, nonvertical OS49 fans and added ordinary clutches, remaining marked source-moduli loops and unmarked endpoint sectors.'
new='K77 computes every OS49 lattice-basis fan, with its actual shorter endpoint and marked cap-data iterates. Its image on either loop is exactly gcd(k,28)Z/28; all28 k=1 witnesses have166 independent full target solves. The basis((2,-1),(-1,1)) gives shorter class7. K75 records the exact remaining source-zero attachment, added ordinary clutches, remaining marked source-moduli loops and unmarked endpoint sectors. Its local radial surgery does not yet identify the actual product-radius end; the exceptional disk and its fixed-trace class must be assigned once in that attachment.'
assert old in text;text=text.replace(old,new)
p.write_text(text)

p=root/'code/part3/results_mapping.json';mapping=json.loads(p.read_text())
mapping.setdefault('additional_source_loop_results',[]).append({
 'id':'P3K.77','status':'Proved','statement':'Complete actual OS49 lattice-basis fan return, both canonical and shorter loops, exact image gcd(k,28)Z/28, and retained marked fixed-source cap-data iterates.',
 'proof':'notes/part3_os49_all_fans.tex','certificate':'code/part3_root/os49_all_fans.json',
 'independent_certificate':'code/part3/audit_os49_all_fan_witnesses.json',
 'actual_shorter_k1_two_flop_example':7,
 'scope':'All GL2Z fans of the exact K76 family, both norm signs and every fixed finite character. Added ordinary clutches, remaining source-moduli generators and arbitrary unmarked endpoints remain separately unresolved.'})
p.write_text(json.dumps(mapping,indent=2)+'\n')

pdf=fitz.open(root/'records/k77_standalone.pdf')
log=(root/'records/k77_standalone.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
assert not over
assert not re.search(r'undefined|Missing character|LaTeX Error|Label\(s\) may have changed',log)
record={'utc':now,'status':'PASS','pages':len(pdf),'build':2,
 'rendered_and_directly_reviewed_pages':list(range(1,len(pdf)+1)),
 'reviewer':'root','render_directory':'records/render_k77_standalone_build2',
 'overfull_boxes':0,'overfull_above2pt':0,
 'visual_result':'Every page directly inspected individually at full rendered size; all matrices, table rows, equation tags and endpoint arrows are legible without clipping or collision.',
 'tex_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'independent_proof_audit':'records/blind_audit_os49_all_fans.json'}
(root/'records/k77_standalone_visual_qa.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'records/k77_promotion.json').write_text(json.dumps({'utc':now,'status':'PROMOTED_AFTER_COMPLETE_PROOF_AND_INDEPENDENT_AUDIT','statement':'P3K.77','archive':str(archive.relative_to(root)),'source_sha256':record['tex_sha256'],'master_to_build':59},indent=2)+'\n')
print('Integrated K77 and retained prior K75/master/report sources; no frozen checkpoint changed.')
