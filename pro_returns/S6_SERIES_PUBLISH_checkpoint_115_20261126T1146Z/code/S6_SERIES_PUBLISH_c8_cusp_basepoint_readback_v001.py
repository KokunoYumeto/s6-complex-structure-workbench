"""Name the global cusp and its local zero in the marked input."""
import csv
import hashlib
from pathlib import Path
import S6_SERIES_PUBLISH_c8_integrate_units as units
root=Path(__file__).resolve().parent.parent
lane=root/'agents/continuation8_iii_weighted_units'
path=root/'agents/continuation8_iii_integration/units/root/cusp_nullbordism.tex'
before=path.read_text()
assert hashlib.sha256(path.read_bytes()).hexdigest()=='0f66d57062def564f5e54a258255f3ef0b8fa0390e05131793d3b0a60c3fdf84'
old='Write $f:X\\to B_{\\mathrm{base}}$ for its map to the base, $t$ for\nthe specified cusp coordinate, $W=f^{-1}(0)$, and choose $x_0\\in W$.'
new='Write $f:X\\to B_{\\mathrm{base}}$ for its map to the base and $p_0$\nfor the cusp. Let $t$ be its specified local coordinate, with\n$t(p_0)=0$, put $W=f^{-1}(p_0)$, and choose $x_0\\in W$.'
assert before.count(old)==1
after=before.replace(old,new,1)
units.check_permanent_identifiers(before,after)
table=lane/'S6_SERIES_PUBLISH_CUSP_NULLBORDISM_publication_defects.tsv'
with table.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
assert len(rows)==61
rows.append(dict(zip(fields,[
    'III-C8-CUSP-PUB-024-D20','D20','wb:def:marked-cusp-nullbordism-data',
    'root/cusp_nullbordism.tex Q258','pending page concordance',
    'root/cusp_nullbordism.tex Q258','pending final build',old,new,
    'Keep the original global cusp p_0 (the infinity fibre in the common marking) and explicitly identify its local coordinate zero by t(p_0)=0. Every later local t=0 equation, map, frame and basepoint bound is unchanged.',
    'whole410-line source and bounded final input correction read; source-local complete; canonical consolidation/global gates remain root'
])))
temporary=path.with_suffix('.tex.tmp');temporary.write_text(after,encoding='utf-8',newline='\n');temporary.replace(path)
temporary=table.with_suffix('.tsv.tmp')
with temporary.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
temporary.replace(table)
review=lane/'S6_SERIES_PUBLISH_CUSP_NULLBORDISM_unit_review.md'
text=review.read_text().replace('410 lines, SHA256','411 lines, SHA256').replace('0f66d57062def564f5e54a258255f3ef0b8fa0390e05131793d3b0a60c3fdf84',hashlib.sha256(after.encode()).hexdigest()).replace('records23 edits in61 categorized rows','records24 edits in62 categorized rows')
text=text.replace('The final locator change\nwas read','The final locator and global-cusp input changes\nwere read')
text=text.replace('base map f, cusp parameter t, central fibre W and arbitrary x0 in W.','base map f, global cusp p0, local parameter t with t(p0)=0, central\nfibre W=f inverse(p0) and arbitrary x0 in W. The local coordinate zero\nis explicitly distinguished by this map from the global base coordinate;\nall subsequent local t=0 formulas are identical.')
text=text.replace('The entire410-line candidate and final bounded locator correction were read','The entire410-line candidate and both final bounded locator/global-cusp corrections were read')
temporary=review.with_suffix('.md.tmp');temporary.write_text(text,encoding='utf-8',newline='\n');temporary.replace(review)
print('OLD',old)
print('NEW',new)
print('FINAL',len(after.splitlines()),hashlib.sha256(after.encode()).hexdigest(),'EDITS',24,'DEFECT_ROWS',len(rows))
print('IDENTITIES_PRESERVED; CANONICAL_AND_SHARED_WRITES 0; INDEPENDENT_CHECK_CREDIT 0')
