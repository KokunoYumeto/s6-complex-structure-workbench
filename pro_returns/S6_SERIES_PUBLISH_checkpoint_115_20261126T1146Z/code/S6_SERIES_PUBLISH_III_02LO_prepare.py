from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import csv,io,re

root=Path(__file__).resolve().parents[1]
folder=root/'agents/continuation6_iii_root'
stem='S6_SERIES_PUBLISH_III_02LO'
label='maps:src:D.2.47'
raw=(root/'S6_SERIES_PUBLISH_III.tex').read_text()
assert sha256(raw.encode()).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
statement=(folder/(stem+'_released_statement.tex')).read_text()
statement=statement[statement.index('\\begin{theorem}'):].rstrip()
proof=(folder/(stem+'_released_proof.tex')).read_text()
proof=proof[proof.index('\\begin{proof}'):].rstrip()
start=raw.index(statement)
end=raw.index(proof,start)+len(proof)
old=raw[start:end]
new_statement=statement.replace('[the general triangular-cusp component intersection form]','[Component intersections in a triangular cusp]')
new_statement=new_statement.replace('\\StatementRecord{maps:src:D.2.47}{proved}{02LO}{\\SeriesRef{maps:src:D.2.43}}\n','')
new_statement=new_statement.replace('They are not replaced by a simple graph or a simplicial\ncomplex with distinct labels.\n','')
new_statement=new_statement.replace('It is not zero for arbitrary period lattices: for\n$L=2\\mathbb Z^2$ and its four vertices,','For $L=2\\mathbb Z^2$ and its four vertices,')
new_statement=new_statement.replace('This is the component part of the cohomology ring and\nthe indicated characteristic pairings. It is not asserted\nto determine torsion products, the full fundamental-class\ninvariant, or a global diffeomorphism type.','These formulas give the component products in the cohomology ring\nand their indicated characteristic pairings.')
new_statement=re.sub(r'\n{3,}','\n\n',new_statement)
new=new_statement+'\n\n'+(folder/(stem+'_proof_new.tex')).read_text().rstrip()
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'):
    assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,new))
assert raw.count(old)==1
(folder/(stem+'_receiving.tex')).write_text(new+'\n',newline='\n')

def write(suffix,fields,rows):
    out=io.StringIO(newline='')
    w=csv.DictWriter(out,fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
    (folder/(stem+suffix)).write_text(out.getvalue(),newline='\n')
write('_replacements.tsv',['statement_id','old_text','new_text'],[dict(statement_id=label,old_text=old,new_text=new)])
fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
rows=[]
for kind,typ,oldtext,newtext,reason in [
 ('header','D10','\\StatementRecord{maps:src:D.2.47}{proved}{02LO}{\\SeriesRef{maps:src:D.2.43}}','','Remove the machine record while preserving its permanent identifiers.'),
 ('scope','D02',statement,new_statement,'State the component-product scope positively; retain every formula and every allowed lattice.'),
 ('proof','D02',proof,'\\begin{proof}'+new.split('\\begin{proof}',1)[1],'Give exact quotient, line-bundle, relative-cohomology and characteristic maps; replace defensive comparisons by their explicit identities.'),
 ('program','D09',proof[proof.index('\\item \\emph{Exact verification and bounds.}'):],'','Move program paths, execution counts and saved-matrix bookkeeping to the records and final programs table.')]:
    row=dict.fromkeys(fields,'')
    row.update(change_id='c6-III-02LO-'+kind,type=typ,statement_id=label,
      old_location=f'S6_SERIES_PUBLISH_III.tex:{raw[:start].count(chr(10))+1}--19517',
      new_location=str((folder/(stem+'_receiving.tex')).relative_to(root)),
      old_text=oldtext,new_text=newtext,reason=reason,
      review_status='complete comparison; root admission and source/page application pending')
    rows.append(row)
write('_defects.tsv',fields,rows)
with (root/'CHECK_EVENTS.tsv').open(newline='') as f: fields=csv.DictReader(f,delimiter='\t').fieldnames
now=datetime.now(timezone.utc).isoformat();event=dict.fromkeys(fields,'')
event.update(statement_id=label,date=now[:10],date_utc=now,
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, sixth continuation root',
 type='targeted proof check',event_id='publish:c6:III:02LO:targeted',
 phase='fresh all-lattice derivation followed by complete original/receiving comparison',
 source_file='S6_SERIES_PUBLISH_III.tex',source_row=str(raw[:start].count('\n')+1),
 source_event_type='targeted proof check',evidence_group='publish:c6:III:02LO:targeted',
 publish_input_file=str((folder/(stem+'_CHECK_EVENTS.tsv')).relative_to(root)),publish_input_row='2',
 where='; '.join(str((folder/(stem+s)).relative_to(root)) for s in ('_fresh_derivation.md','_comparison.md','_replacements.tsv')),
 outcome='Derived every02LO assertion from the height-one toric cover before original-proof exposure: exact divisor restrictions with self-gluings, all-lattice integral form, cell multiplicities, characteristic evaluations and both special lattices. Entire original proof and receiver compared; all conclusions survive. New pre-exposure tensor/cell computation and post-comparison seven-value polarization agree, the latter on all127 original Hermite forms and23276 basis triples. Preserved the relative-to-absolute map and boundary winding class explicitly. No pending02LK conclusion used; no refutation; manuscript/unit application remains pending.')
write('_CHECK_EVENTS.tsv',fields,[event])
out=f'Prepared exact02LO guard, receiving theorem/proof, four defect rows and one event at{now}.\n'
Path(__file__).with_suffix('.out').write_text(out,newline='\n')
print(out,end='')
