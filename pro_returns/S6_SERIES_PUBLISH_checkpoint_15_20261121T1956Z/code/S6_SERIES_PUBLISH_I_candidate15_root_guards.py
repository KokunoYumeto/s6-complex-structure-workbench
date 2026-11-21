#!/usr/bin/env python3
"""Archive root's contextual findings from the actual candidate15 page reading.

Writes exact guarded proposals only; the canonical manuscript is unchanged.
The ten etale accents use the spelling already established elsewhere in the
paper. The positive divisor wording retains the same effective multiplicities.
"""
from pathlib import Path
import hashlib
import json
import re
import fitz

ROOT=Path(__file__).resolve().parents[1]


def main():
    source=ROOT/'S6_SERIES_PUBLISH_I.tex'; text=source.read_text()
    expected='45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8'
    assert hashlib.sha256(source.read_bytes()).hexdigest()==expected
    proposals=[
        ('D02',251,
         'The central support has\nnormal crossings; its multiplicities need not be one.',
         'The central divisor has normal-crossings support and positive integral\ncomponent multiplicities.',
         'State the component multiplicities positively. In the stated smooth model the central divisor is div(r): its coefficients are the positive integral orders of the nonzero holomorphic parameter along its components. Both wordings leave those orders unrestricted; all modifications, maps and the conclusion are unchanged.'),
        ('D02',252,
         'The proof of \\ref{push:src:B.4.4}\nrequires no reducedness or normal-crossings condition at the\ncentre: its torsion-free coherent bi-anticanonical pencil and\nlabelled critical-value argument apply to this smooth model.',
         'The torsion-free coherent bi-anticanonical pencil and labelled\ncritical-value argument of \\ref{push:src:B.4.4} apply to this smooth model.',
         'The two actual mechanisms and their cited source are already explicit. Preserve them as the positive application sentence and delete the negative reminder about additional central conditions.'),
        ('D02',265,
         'exact also at $2$ and $3$; it does not use a formula restricted\nto residue characteristic at least five.',
         'exact also at $2$ and $3$.',
         'The preceding argument tests reduction to the nonsingular locus and states exactness at2and3. Keep that positive mathematical scope and remove its redundant contrast with another formula.'),
        ('D11',268,
         'constant $\\frac12\\log2$; the general bounded-variation\nstatement alone does not supply that constant.',
         'constant $\\frac12\\log2$.',
         'The preceding positive sentence states the explicit archimedean constant; step1 already derives it by applying the analytic maximum theorem. Preserve that content and remove the repeated negative scope comparison.')]
    guards=[]
    for kind,page,old,new,reason in proposals:
        assert text.count(old)==1
        offset=text.index(old)
        guards.append({'id':f'I15-root-{len(guards)+1:02}', 'type':kind,'page':page,
                       'before':old,'after':new,'reason':reason,
                       'source_line':text.count('\n',0,offset)+1,
                       'source_sha256':expected,'status':'proposed, not applied',
                       'mathematical_events_added':0})
    # Accented TeX spellings already present are excluded explicitly.
    hits=list(re.finditer(r"(?<!\\')\betale\b",text))
    assert len(hits)==10
    for match in hits:
        start=text.rfind('\n',0,match.start())+1
        end=text.find('\n',match.end())
        old=text[start:end]; new=old[:match.start()-start]+r"\'etale"+old[match.end()-start:]
        assert text.count(old)==1
        guards.append({'id':f'I15-root-{len(guards)+1:02}','type':'D23',
                       'before':old,'after':new,'source_line':text.count('\n',0,start)+1,
                       'source_sha256':expected,'status':'proposed, not applied',
                       'reason':'Restore the acute accent in etale, consistently with the already accented theorem statements and terminology elsewhere. Only the word spelling changes; every mathematical segment and construction map remains.',
                       'mathematical_events_added':0})
    out=ROOT/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate15_root_guards.json'
    out.write_text(json.dumps(guards,indent=2)+'\n')
    pdf=ROOT/'build/I_candidate15/S6_SERIES_PUBLISH_I.pdf'
    with fitz.open(pdf) as doc:
        # Inspect the actual item number at higher resolution; the PDF text
        # and source both identify this as item3, not a missing proof item.
        assert doc[268].get_text().startswith('3. The product formula')
        crop=doc[268].get_pixmap(matrix=fitz.Matrix(3,3),clip=fitz.Rect(45,55,540,100))
        crop_path=ROOT/'render/I_candidate15/page269_item3_detail.png'
        crop.save(crop_path)
    reading=ROOT/'records/S6_SERIES_PUBLISH_I_final_candidate15_reading_root.json'
    saved=json.loads(reading.read_text())
    resolution=' Subsequent source/PDF-text comparison and actual enlarged-image inspection show item3 clearly present at the first line; the visual suspicion is cleared and no edit is needed.'
    row=next(row for row in saved['pages'] if row['page']==269)
    if resolution not in row['finding']:
        row['finding']+=resolution
        reading.write_text(json.dumps(saved,indent=2)+'\n')
    print(json.dumps({'proposals':len(guards),'types':{k:sum(x['type']==k for x in guards) for k in ['D02','D11','D23']},
                      'guard':str(out),'source_unchanged':hashlib.sha256(source.read_bytes()).hexdigest()==expected,
                      'item3_detail':str(crop_path)},indent=2))


if __name__=='__main__':
    main()
