"""Create the shared bibliography; producer notes are not current verification."""
from pathlib import Path
import sys,json,re

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'deps/python'))
import bibtexparser
OUT=ROOT/'deliverables';SRC=ROOT/'sources'
files=[SRC/'returns'/r/(r+'_references.bib') for r in
 ['S6_02_FAMILY','S6_02_PUSH','S6_01_INVARIANTS','S6_05_ARITHMETIC','S6_03_CDP','S6_04_MAPS_MANIFOLDS']]
files += [SRC/'overleaf_working_edition/references.bib']
files += list((SRC/'previous_attempt').glob('*.bib'))
files += sorted((SRC/'returns').glob('*/sections/*.bib'))
files += sorted((OUT/'work').rglob('*.bib'))
entries={};provenance={};collisions=[];metadata_corrections=[]
for f in files:
    if not f.exists():continue
    library=bibtexparser.parse_string(f.read_text())
    for e in library.entries:
        fields={p.key:p.value for p in e.fields}
        key=e.key
        if key=='Brunella1999' and 'forms on compact' in fields.get('title',''):
            key='Brunella1999Forms'
            fields['doi']='10.1007/S000140050109'
            fields['url']='https://ems.press/content/serial-article-files/42850'
        if key=='Brunella1999':fields['doi']='10.4171/DM/64'
        record={'type':e.entry_type,'key':key,'fields':fields}
        if key=='HatcherSpectralSequences':fields['year']='n.d.'
        if key=='waldschmidt1988theta':
            record['type']='misc'
            fields['howpublished']=fields.get('booktitle','')+r', expos\'e 15, pp. 1--7'
            for old_field in ['booktitle','number','pages']:fields.pop(old_field,None)
        if key in entries:
            if entries[key]['fields'].get('title')!=fields.get('title'):
                collisions.append({'key':key,'retained':provenance[key],'other':str(f.relative_to(ROOT)),'other_title':fields.get('title')})
            # These metadata sets were checked against their original
            # publications in this writing; the preceding source records
            # remain in the correction log rather than silently winning.
            checked_override=(f==OUT/'work/invariants_arithmetic/maps_F_checked_references.bib' and key=='ffAchingerOgus20') or f==OUT/'work/invariants_arithmetic/push_C_checked_references.bib'
            if checked_override:
                old=entries[key]
                changes={k:{'before':old['fields'].get(k),'after':v} for k,v in fields.items() if k!='note' and old['fields'].get(k)!=v}
                if changes:metadata_corrections.append({'key':key,'original_source':provenance[key],'checked_metadata_source':str(f.relative_to(ROOT)),'changes':changes})
                entries[key]=record;provenance[key]=str(f.relative_to(ROOT))
            continue
        entries[key]=record;provenance[key]=str(f.relative_to(ROOT))
# Publication metadata checked against the actual cover/title pages. Preserve
# every superseded field, including type, in the audit record. The issue-only
# Zhubr journal has no invented volume; the exact serial citation is retained
# as howpublished so the APA BibTeX style does not invent a volume requirement.
final_metadata={
 'Poenaru1971':{'type':'article','set':{'title':r'Travaux de {J. Cerf} (isotopie et pseudo-isotopie)',
     'journal':r'S{\'e}minaire N. Bourbaki'},'remove':['booktitle'],
     'evidence':'Original NUMDAM PDF cover and article p155, opened 17November2026; expose373, volume12, pp155--176,1971.'},
 'manReiser24':{'set':{'volume':'2024'},'remove':[],
     'evidence':'Original published PDF p14115 header explicitly gives 2024(22),14115--14137.'},
 'ffPetersSterk':{'type':'misc','set':{'howpublished':r'Authors\textquotesingle{} June 2024 manuscript'},'remove':[],
     'evidence':'Author June2024 PDF and complete cited theorem checked in work/cdp_audit/maps_E/references_verified.json; no publisher is supplied.'},
 'ffZhubr13':{'type':'misc','set':{'howpublished':r'Izvestia Komi Science Centre of the Ural Division of the Russian Academy of Sciences, no.~4(16), pp.~4--10'},'remove':['journal','number','pages'],
     'evidence':'Original issue cover explicitly gives no4(16),2013, with no volume; complete article checked in the source ledger.'},
}
for key,fix in final_metadata.items():
    if key not in entries:continue
    entry=entries[key];before={'type':entry['type'],**entry['fields']}
    if fix.get('type'):entry['type']=fix['type']
    entry['fields'].update(fix['set'])
    for field in fix['remove']:entry['fields'].pop(field,None)
    after={'type':entry['type'],**entry['fields']}
    changes={k:{'before':before.get(k),'after':after.get(k)} for k in before.keys()|after.keys() if before.get(k)!=after.get(k)}
    if changes:metadata_corrections.append({'key':key,'original_source':provenance[key],'checked_metadata_source':fix['evidence'],'changes':changes})
verification={}
for p in (OUT/'work').rglob('*references_verified.json'):
    obj=json.loads(p.read_text())
    items=obj if isinstance(obj,list) else obj.get('references',obj)
    if isinstance(items,dict):items=[{'key':k,**v} if isinstance(v,dict) else {'key':k,'verification':v} for k,v in items.items()]
    for row in items:
        if not isinstance(row,dict):continue
        keys=row.get('keys',[]) or [row.get('citation_key',row.get('key',row.get('bibkey',row.get('id',''))))]
        if isinstance(keys,str):keys=[keys]
        aliases=row.get('aliases',[])
        if isinstance(aliases,str):aliases=[aliases]
        keys=list(dict.fromkeys(keys+aliases))
        for key in keys:
            if key:
                old=verification.get(key,{})
                status=str(row.get('status','')).lower()
                is_verified=status.startswith('verified') or status in ['opened and matched','pass','passed']
                old_verified=str(old.get('status','')).lower().startswith('verified')
                if is_verified or not old_verified:verification[key]=row
parts=[]
for key,e in sorted(entries.items()):
    fields=dict(e['fields'])
    old=fields.pop('note',None)
    if old:fields['source_note']=old
    state=str(verification.get(key,{}).get('status','')).lower()
    if state.startswith('verified') or state in ['opened and matched','pass','passed']:
        v=verification[key]
        fields['verification']='verified'
        fields['note']='Verified: original source opened and the cited statement and hypotheses matched in this writing; see the source verification record for the precise scope.'
    else:
        fields['verification']='unverified'
        fields['note']='Unverified in this writing at this assembly stage; no mathematical dependence is authorized by an earlier source-note alone.'
    parts.append('@'+e['type']+'{'+key+',\n'+',\n'.join('  '+k+' = {'+str(v)+'}' for k,v in fields.items())+'\n}\n')
(OUT/'S6_09_PAPERS_references.bib').write_text('\n'.join(parts))
(OUT/'records/bibliography_provenance.json').write_text(json.dumps({'sources':provenance,'collisions':collisions,'checked_metadata_corrections':metadata_corrections,'current_verified_keys':sorted(k for k,v in verification.items() if str(v.get('status','')).lower().startswith('verified')),'verification_records':verification},indent=2)+'\n')
print('Bibliography entries',len(entries),'verified keys',len(verification),'collisions requiring review',len(collisions))
