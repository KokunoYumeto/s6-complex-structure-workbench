"""Reduce table strut padding after actually observing its isolated final row."""
import hashlib,json
from pathlib import Path
from S6_SERIES_PUBLISH_editing import Editor
root=Path(__file__).resolve().parents[1]
ed=Editor('I')
old='{\\footnotesize\n\\setlength{\\tabcolsep}{4pt}\n\\begin{longtable}'
new='{\\footnotesize\n\\renewcommand{\\arraystretch}{.9}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{longtable}'
ed.replace(old,new,'D23','Actual candidate12 page332 contains only the final program row. Reduce local row-strut padding while preserving every computation description and source link.','tab:I:programs')
ed.save()
p=root/'render/I_candidate12_layout/page_332.png'
r={'observed_pdf_sha256':'b60bcfdc298b2559c74dce4e8007e3b7ee611c9a51c2ed7e09b0ce48be276353','observed_page':332,'observed_image_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'actual_image_read':True,'finding':'One isolated final program row occupies page332; the row contains the section-equation/collinearity source link.','source_after_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'final_recheck_required':True,'mathematical_events':0}
(root/'records/S6_SERIES_PUBLISH_I_program_table_layout_receipt.json').write_text(json.dumps(r,indent=2)+'\n')
