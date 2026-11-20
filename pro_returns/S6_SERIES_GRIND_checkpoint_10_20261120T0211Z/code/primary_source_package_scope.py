"""Keep downloaded third-party full texts as reading inputs, with receipt provenance.

User-supplied exact copies and our own paper snapshots remain packageable.
No source file is deleted or altered by this classification.
"""
from pathlib import Path
import hashlib,json

def third_party_reading_assets(root):
    base=root.parent/'S6_SERIES_GRIND_source'
    attached={hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*.pdf')}
    excluded=set();records=[]
    for audit in root.glob('audit_*'):
        for p in audit.rglob('*.pdf'):
            if p.name.startswith('S6_SERIES_GRIND_'):continue
            sha=hashlib.sha256(p.read_bytes()).hexdigest()
            if sha in attached:continue
            rel=str(p.relative_to(root));excluded.add(rel)
            records.append({'path':rel,'sha256':sha,'bytes':p.stat().st_size,
                'scope':'Third-party primary text downloaded for reading; URL/version/locator/opening receipts remain. Full text is not a deliverable.'})
            for q in p.parent.glob(p.stem+'*'):
                if q.is_file() and q.suffix.lower() in {'.txt','.html','.htm','.xml','.ps','.eps'}:
                    excluded.add(str(q.relative_to(root)))
    for audit in root.glob('audit_*'):
        for p in audit.rglob('*'):
            if p.is_file() and any(x in {'primary_sources','literature'} for x in p.parts) and p.suffix.lower() in {'.html','.htm','.xml'}:
                excluded.add(str(p.relative_to(root)))
    report={'scope':'Exact user-supplied primary PDFs remain eligible. New external full texts are retained as local reading inputs; source provenance and authored comparison receipts remain in the checkpoint. No original input, current proof, code, output or opening receipt is deleted.',
            'external_primary_PDFs':records,'excluded_canonical_paths':sorted(excluded)}
    (root/'analysis/primary_source_package_scope.json').write_text(json.dumps(report,indent=2)+'\n')
    return excluded
