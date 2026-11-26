"""Admit one complete construction unit and the exact primary adjugate maps."""
from S6_SERIES_PUBLISH_c3_edit import *
import hashlib

base=ROOT/'agents/continuation3_provenance'
specs=[('p205','S6_SERIES_PUBLISH_p205'),('de_jong','S6_SERIES_PUBLISH_djvs')]
before=SOURCE.read_text();after=before
for folder,prefix in specs:
 _,guards=read_tsv(base/folder/(prefix+'_guards.tsv'))
 for r in guards:
  assert hashlib.sha256(r['old_text'].encode()).hexdigest()==r['old_sha256'],r['change_id']
  assert hashlib.sha256(r['new_text'].encode()).hexdigest()==r['new_sha256'],r['change_id']
  assert after.count(r['old_text'])==1,r['change_id']
  preserve_identifiers(r['old_text'],r['new_text'])
  after=after.replace(r['old_text'],r['new_text'],1)
  print('Applied',r['change_id'])
preserve_identifiers(before,after)
SOURCE.write_text(after,newline='\n')
for folder,prefix in specs:
 for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
  _,rows=read_tsv(base/folder/(prefix+'_'+suffix));print(prefix,suffix,append_rows(ROOT/target,rows,key))
 _,sources=read_tsv(base/folder/(prefix+'_sources.tsv'));mapped=[]
 for i,r in enumerate(sources,1):
  mapped.append(dict(source='II-C3-'+folder.upper()+'-'+str(i)+'-'+r['source_key'],url=r['url'],version=r['version'],locus=r['locus_read'],date_utc=r['date_utc'],sha256=r['sha256'],own_word_summary=r['own_paraphrase'],use=r['exact_application']+' Reading attribution: continuation3 provenance. '+r.get('read_extent',r.get('limits',''))))
 print('Primary readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',mapped,'source'))
add_event('ii:three-doubled-nodal-fibres','II-C3-ROOT-THREE-DOUBLED-SUPPORTS-ADMISSION','used and rechecked in this run',
 'The provenance reviewer read the complete old and receiving P205 proof and its earlier P233/P294 owners, and reran the original finite algebra plus the three limiting logarithmic determinants. Root read the complete 640-line receiving construction and the full comparison. Every original construction map, integral marking, local action, affine descent, index-two restriction, primitive transgression and final Betti calculation is preserved; the two verification arrays are replaced by their exact linear equations and the determinant -16. Root checked the finite deck matrix, exterior derivation, explicit Hausdorff chain transition, invariant norms, same-tube inclusion and conductor amalgamation maps. The original example statement is unchanged. The unit retains its stable ledger identifier; its added subsection label is an alias destination. No independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: Three doubled nodal supports',source=__file__)
_,states=read_tsv(base/'p205/S6_SERIES_PUBLISH_p205_unit_status.tsv')
for row in states:
 kind=row['defect_type']
 if kind in ['D10','D16']:continue
 status='open' if kind in ['D14','D23','D24'] else 'done'
 set_unit_status('ii:three-doubled-nodal-fibres',kind,status,row['note']+' Whole-paper placement/front matter and final typography remain open.','CHECK_EVENTS.tsv: II-C3-ROOT-THREE-DOUBLED-SUPPORTS-ADMISSION')
add_event('night:P4.41; night:P4.47; night:P4.49','II-C3-ROOT-ADJUGATE-PRIMARY-APPLICATION','used and rechecked in this run',
 'The provenance reviewer freshly opened the primary de Jong-van Straten 1990 theorem and its complete printed proof, analytic conventions and setup, and read all three complete current and receiving proofs. Root read every bounded old/new guard and the full source-to-application comparison. The quotient P->R=P/(f) sends the ambient conductor I to c=I/(f), with inverse image I, and P222 gives its normalization multiplier duality. The primary adjugate criterion therefore yields exactly the ambient entries in I. At two generators the explicit matrix [[h,lambda],[-g,mu]] and its adjugate give lambda,mu in I and f in I^2. P449 uses the same quotient for both ideal forms. Statements and all subsequent full-multiplicity deformations are unchanged. Existing bibliographic identity and locator are confirmed. These source-application premises are resolved; whole-paper bibliographic and PDF gates remain open.',
 'S6_SERIES_PUBLISH_II.tex: P441/P447/P449 conductor source applications',source=__file__)
print('Complete P205 and four exact adjugate-application guards admitted.')
