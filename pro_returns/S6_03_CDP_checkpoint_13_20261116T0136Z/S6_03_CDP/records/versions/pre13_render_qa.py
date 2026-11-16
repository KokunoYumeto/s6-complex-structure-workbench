"""Render distributed manuscript samples and the repaired overflow passages."""
from pathlib import Path
import json
import fitz

root = Path(__file__).resolve().parents[1]
pdf = fitz.open(root / 'S6_03_CDP_paper.pdf')
out = root / 'build' / 'visual_qa'
out.mkdir(exist_ok=True)
pages = {0, 1, 2, len(pdf)-1}
pages.update(range(8, len(pdf), 12))
terms = ['A.13', 'cyclic characters', 'C.5)', 'C.12)',
         'D.18', 'D.S.1', 'C.22b', 'A.J.1',
         'C.2.CR.4', 'C.2.CR.6', 'C.2.D4.1', 'C.2.D4.3',
         'C.2.RAT.6', 'C.2.RAT.7', 'C.2.RAT.8', 'C.2.RAT.9',
         'C.2.UN.1', 'C.2.UN.2', 'C.2.UN.3', 'C.2.UN.4',
         'C.2.UN.5', 'C.2.UN.6', 'C.2.UN.7', 'C.2.UN.8',
         'C.2.UN.9', 'C.2.UN.10',
         'C.2.UN.11', 'C.2.UN.12', 'C.2.UN.13',
         'C.2.UN.14', 'C.2.UN.15', 'C.2.UN.16',
         'C.2.UN.17', 'C.2.UN.18', 'C.2.UN.19',
         'C.2.UN.20', 'C.2.UN.21', 'C.2.UN.22', 'C.2.UN.23',
         'C.2.UN.24', 'C.2.UN.25', 'C.2.UN.26',
         'C.2.UN.27', 'C.2.UN.28', 'C.2.UN.29',
         'C.2.UN.30', 'C.2.UN.31', 'C.2.UN.32',
         'C.2.UN.33', 'C.2.UN.34', 'C.2.UN.35',
         'C.2.UN.36', 'C.2.UN.37', 'C.2.UN.38',
         'C.2.UN.39', 'C.2.UN.40', 'C.2.UN.41',
         'C.2.UN.42', 'C.2.UN.43', 'C.2.UN.44',
         'C.2.UN.45', 'C.2.UN.46', 'C.2.UN.47',
         'C.2.UN.48', 'C.HG.1', 'C.HG.8', 'C.HG.12', 'C.HG.16',
         'C.2.UN.49', 'C.2.UN.50', 'C.2.UN.51', 'C.2.UN.52',
         'C.2.UN.53', 'C.2.UN.54',
         'C.2.UN.55', 'C.2.UN.56', 'C.2.UN.57', 'C.2.UN.58',
         'C.2.UN.59', 'C.EW.6', 'C.EW.11', 'C.EW.15', 'C.EW.17', 'C.EW.20', 'C.EW.21',
         'C.2.UN.60', 'C.PR.2', 'C.PR.6', 'C.PR.12', 'C.PR.14', 'C.PR.18',
         'C.2.UN.61', 'C.PT.7', 'C.PT.8', 'C.PT.11', 'C.PT.14',
         'C.2.UN.62', 'C.QT.2', 'C.QT.6', 'C.QT.11', 'C.QT.13',
         'C.2.UN.63', 'C.WT.3', 'C.WT.13', 'C.WT.18', 'C.WT.23a', 'C.WT.30', 'C.WT.35', 'C.WT.42', 'C.WT.43',
         'C.2.UN.64', 'C.EL.1', 'C.EL.3', 'C.EL.5', 'C.EL.9', 'C.EL.11',
         'C.2.UN.65', 'C.CZ.5', 'C.CZ.9', 'C.CZ.10', 'C.CZ.12', 'C.CZ.14',
         'C.2.UN.66', 'C.MR.1', 'C.MR.8', 'C.MR.10', 'C.MR.14', 'C.MR.16',
         'C.2.UN.67', 'C.RH.3', 'C.RH.5', 'C.RH.8', 'C.RH.9',
         'C.2.UN.68', 'C.TC.5', 'C.TC.8', 'C.TC.10', 'C.TC.12',
         'C.2.UN.69', 'C.NM.2', 'C.NM.6', 'C.NM.10',
         'C.2.UN.70', 'C.NP.1', 'C.NP.4', 'C.NP.8',
         'C.2.UN.71', 'C.TG.4', 'C.TG.9', 'C.TG.14', 'C.TG.15',
         'C.2.UN.72', 'C.NT.1', 'C.NT.4', 'C.NT.6', 'C.NT.8',
         'C.2.UN.73', 'C.TX.6', 'C.TX.7', 'C.TX.10', 'C.TX.14',
         'C.2.UN.74', 'C.RC.1', 'C.RC.4', 'C.RC.7', 'C.RC.10', 'C.RC.12',
         'C.2.UN.75', 'C.KG.1', 'C.KG.4', 'C.KG.7', 'C.KG.10',
         'C.2.UN.76', 'C.WF.4', 'C.WF.8', 'C.WF.12', 'C.WF.13', 'C.WF.17', 'C.WF.21', 'C.WF.26', 'C.WF.28',
         'C.2.UN.77', 'C.HM.2', 'C.HM.5', 'C.HM.9', 'C.HM.10',
         'C.2.UN.78', 'C.RK.4', 'C.RK.7', 'C.RK.10', 'C.RK.15', 'C.RK.18', 'C.RK.21', 'C.RK.22',
         'C.TL.4', 'C.TL.6', 'C.TL.8', 'C.WM.3', 'C.WM.6',
         'C.AD.7', 'C.AD.8', 'C.AD.11', 'C.HT.4', 'C.HT.9', 'C.HT.12',
         'C.MX.1', 'C.MX.7', 'C.MX.10',
         'C.WH.0', 'C.WH.4', 'C.WH.9', 'C.WH.12', 'C.WH.17',
         'C.HR.2', 'C.HR.6', 'C.HR.8',
         'C.NS.4', 'C.NS.13', 'C.NS.18', 'C.NS.19', 'C.NS.20',
         'C.SN.4', 'C.SN.6', 'C.SN.10',
         'C.AS.1', 'C.AS.9', 'C.AS.13', 'C.AS.15', 'C.AS.18',
         'C.DH.14a', 'C.DH.14b', 'C.NH.8', 'C.NH.10',
         'C.SH.9', 'C.FG.19', 'C.RU.7', 'C.HC.2', 'C.PF.11',
         'C.CL.6', 'C.HB.3', 'C.HB.9',
         'C.EN.S2', 'C.EQ.1', 'C.EQ.8', 'C.KX.14',
         'C.2.MH.1', 'C.2.MH.2', 'C.2.MH.3', 'C.2.MH.4', 'C.2.G.1']
matches = {}
for i, page in enumerate(pdf):
    text = page.get_text()
    found = [term for term in terms if term in text]
    if found:
        pages.add(i)
        matches[str(i+1)] = found
manifest = {'pdf_pages': len(pdf), 'rendered_pages': sorted(p+1 for p in pages),
            'passage_matches': matches}
for i in sorted(pages):
    pdf[i].get_pixmap(matrix=fitz.Matrix(1.45, 1.45), alpha=False).save(
        out / f'page_{i+1:03d}.png')
(out / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(json.dumps(manifest, indent=2))
