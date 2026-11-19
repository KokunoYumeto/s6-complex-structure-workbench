"""Audit actual current statement tags, citations, cross-pages and PDF names.

Run only after a complete build. This checks the referenced labels, rather
than counting all unused generated reference definitions as imports.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,re
import fitz
from tex_tools import macros
from assemble_series import all_cites,bib_entries
R=Path(__file__).resolve().parents[1]
PAPERS=['I','II','III','IV','V']
tags=json.loads((R/'analysis/label_tags.json').read_text())
current={p:json.loads((R/f'analysis/current_labels_{p}.json').read_text()) for p in PAPERS}
documents={p:fitz.open(R/f'S6_SERIES_GRIND_{p}.pdf') for p in PAPERS}
names={p:doc.resolve_names() for p,doc in documents.items()}
report={};mismatches=[];cross_count=0;allkeys=set();pdferrors=[]
for p in PAPERS:
    text=(R/f'S6_SERIES_GRIND_{p}.tex').read_text()
    refs=set(re.findall(r'\\SeriesRef\{([^}]+)\}',text))
    defs=dict(re.findall(r'\\expandafter\\def\\csname SRef@([^\n]*?)\\endcsname\{([^\n]*)\}\s*\n',text))
    records=[args for _,_,args in macros(text,'StatementRecord',4) if not args[0].startswith('#')]
    counts=Counter(x[0] for x in records)
    missing=[lab for lab in refs if lab not in tags or lab not in defs]
    for lab in refs:
        info=tags.get(lab)
        if not info:continue
        q=info['paper'];meta=current[q].get(lab) or current[q].get(info['canonical_label'])
        if not meta:
            missing.append(lab);continue
        dest='tag-'+info['tag']
        if dest not in names[q]:pdferrors.append({'from':p,'label':lab,'target':q,'missing_destination':dest})
        elif int(meta['page'])!=names[q][dest]['page']+1:
            pdferrors.append({'from':p,'label':lab,'target':q,'destination':dest,'expected_page':meta['page'],'actual_page':names[q][dest]['page']+1})
        if q!=p:
            cross_count+=1
            definition=defs.get(lab,'')
            expected=f"{q}.{meta['number']} (p.~{meta['page']})"
            if expected not in definition or f'S6_SERIES_GRIND_{q}.pdf\\#nameddest={dest}' not in definition:
                mismatches.append({'from':p,'label':lab,'expected':expected,'definition':definition})
    printed_tags=[args[2] for args in records]
    for tag in printed_tags:
        if 'tag-'+tag not in names[p]:pdferrors.append({'paper':p,'missing_printed_tag':tag})
    report[p]={'SeriesRef_targets':len(refs),'unresolved_target_labels':sorted(set(missing)),
      'printed_statement_records':len(records),'duplicate_statement_records':[k for k,v in counts.items() if v>1],
      'unknown_statuses':sorted(set(x[1] for x in records)-{'proved','open','false','proved(H)'}),
      'PDF_named_destinations':len(names[p]),'PDF_sha256':hashlib.sha256((R/f'S6_SERIES_GRIND_{p}.pdf').read_bytes()).hexdigest()}
    allkeys|=all_cites(text)
bib=bib_entries((R/'S6_SERIES_GRIND_references.bib').read_text())
report['references']={'cited_keys':len(allkeys),'entries':len(bib),'missing':sorted(allkeys-set(bib)),
 'missing_status_fields':[k for k,v in bib.items() if not re.search(r'verification\s*=\s*\{',v['text'],re.I)],
 'explicitly_unverified':[k for k,v in bib.items() if re.search(r'verification\s*=\s*\{\s*unverified',v['text'],re.I)]}
(R/'analysis/current_reference_integrity.json').write_text(json.dumps(report,indent=2)+'\n')
(R/'analysis/crosspaper_current_page_comparison.json').write_text(json.dumps({'distinct_crosspaper_targets_by_paper':cross_count,'mismatches':mismatches},indent=2)+'\n')
(R/'analysis/current_PDF_destination_integrity.json').write_text(json.dumps({'checked_referenced_and_printed_tags':True,'errors':pdferrors},indent=2)+'\n')
print(json.dumps({'papers':{p:report[p]['printed_statement_records'] for p in PAPERS},'crosspaper_targets':cross_count,'crosspaper_mismatches':len(mismatches),'PDF_destination_errors':len(pdferrors),'unresolved':sum(len(report[p]['unresolved_target_labels']) for p in PAPERS),'bibliography':report['references']}))
