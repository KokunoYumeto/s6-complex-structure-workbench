"""Apply exact, reviewed statement corrections and the missing source comparison."""
from pathlib import Path
import csv,json,re
from tex_tools import macros,replace_spans
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'S6_SERIES_GRIND_source'
csv.field_size_limit(10**9)

def main():
    history_path=ROOT/'analysis/applied_patches.json'
    previous=json.loads(history_path.read_text()) if history_path.exists() else []
    applied=[]
    files=[ROOT/'audit_corrections/proposed_patches.json',ROOT/'audit_sign/proposed_patches.json',ROOT/'audit_paper_i/proposed_patches.json']
    for file in files:
        if not file.exists():continue
        data=json.loads(file.read_text())
        if isinstance(data,dict):data=data.get('patches',[])
        for patch in data:
            paper=patch['paper'];paper='II' if paper=='VI' else paper
            path=ROOT/f'parts/{paper}.body.linked.tex';text=path.read_text()
            old,new=patch['old'],patch['new']
            n=text.count(old)
            if n==0 and new in text:status='already applied'
            elif n==1:text=text.replace(old,new,1);path.write_text(text);status='applied'
            else:raise ValueError((file,patch.get('label'),n,'exact patch did not match once'))
            applied.append(dict(patch,paper=paper,status=status,source_patch_file=str(file.relative_to(ROOT))))
    file=ROOT/'audit_paper_i/patches.json'
    if file.exists():
        path=ROOT/'parts/I.body.linked.tex';text=path.read_text()
        for raw in json.loads(file.read_text()):
            patch=dict(raw,paper='I',label=raw['statement_id'])
            if raw['operation']=='replace_exact':old,new=raw['old'],raw['new']
            elif raw['operation']=='insert_after_exact':old,new=raw['anchor'],raw['anchor']+raw['text']
            else:raise ValueError(raw['operation'])
            if new in text:status='already applied'
            elif text.count(old)==1:text=text.replace(old,new,1);status='applied'
            else:raise ValueError((raw['id'],'patch match',text.count(old)))
            applied.append(dict(patch,status=status,source_patch_file=str(file.relative_to(ROOT))))
        path.write_text(text)
    path=ROOT/'parts/I.body.linked.tex';text=path.read_text()
    insertion=ROOT/'audit_corrections/P5_7_insertion.tex'
    if insertion.exists() and r'\label{night:P5.7}' not in text:
        marker=r'\section{Credited proofs of parameter equivalence and deformation results}'
        assert marker in text
        content=insertion.read_text()
        # Current prose checks belong in the external record, exactly as with inherited records.
        spans=[]
        for a,b,args in macros(content,'StatementRecord',4):
            args[2]='';spans.append((a,b,'\\StatementRecord'+''.join('{'+v+'}' for v in args)))
        content=replace_spans(content,spans)
        text=text.replace(marker,marker+'\n\n'+content,1);path.write_text(text)
        applied.append({'paper':'I','label':'night:P5.7','status':'inserted','reason':'Missing version-specific source comparison with exact a=c+delta period transport.'})
    # The three omitted night rows each receive a distinct inventory disposition.
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open() as f:rows=list(csv.DictReader(f))
    with (BASE/'S6_GRIND_3_night_run_cp36/S6_06_BLIND_results.csv').open() as f:night={r['id']:r for r in csv.DictReader(f)}
    for identifier,paper,reason in [
        ('P1.6','V','Known homotopy-sphere absorption input, cited through maps:src:F.4.1. The attached night register and report record its independent derivation; notes/part1.tex is not attached.'),
        ('P1.14','V','Independent night-run derivation of the conclusion of maps:src:F.4.1. Its conclusion and full receiving proof occur there; the separately reported night route is retained as check provenance.'),
        ('P5.7','I','')]:
        label='night:'+identifier
        existing=next((r for r in rows if r['label']==label),None)
        source=night[identifier];row=existing if existing is not None else {k:'' for k in rows[0]}
        prior_record=row.get('check_record','')
        prior_notes=row.get('notes','')
        row.update(paper=paper,label=label,source_run='S6_06_BLIND',source_id=identifier,kind='Remark' if identifier=='P5.7' else 'Cited result',
            status='proved',main_or_supporting='supporting',uses=source.get('depends_on',''),
            check_record=prior_record or json.dumps({'received_night_register':source},ensure_ascii=False),
            credited_to='Du–Guo–Kusakabe–Xie, versions 1 and 2, exact locators in the credited appendix.' if identifier=='P5.7' else 'Wall extended-form classification and Kramer–Stolz Theorem A; locators in maps:src:F.4.1.',
            in_compendium_only_because=reason,notes=prior_notes or source['statement'],source_paper=paper,
            source_inventory_row=row.get('source_inventory_row') or 'night-cp36:'+identifier,placement_state='printed source-comparison remark' if identifier=='P5.7' else 'known input or independent re-proof mapped to maps:src:F.4.1',
            writing_state='scope and source comparison inserted' if identifier=='P5.7' else 'receiving proof already retained',
            confidence_state='source comparison checked; current global review pending' if identifier=='P5.7' else 'reported historical re-proof retained; receiving proof targeted review recorded',
            completion_state='pending',check_summary='See incoming night-register provenance and this run correction audit.',
            confidence_line='Exact receiving scope is recorded; no additional independent proof is inferred from importing the register.')
        if existing is None:rows.append(row)
    # Retain every absent arithmetic A source row with its supplied editorial disposition.
    missing=ROOT/'audit_corrections/missing_ari_A_rows.csv'
    if missing.exists():
        with missing.open() as f:extra=list(csv.DictReader(f))
        (ROOT/'analysis/missing_ari_A_raw.json').write_text(json.dumps(extra,indent=2,ensure_ascii=False))
        for source in extra:
            identifier=source['source_id'];label='ari:'+identifier
            if any(r['source_run']==source['source_run'] and r['source_id']==identifier for r in rows):continue
            row={k:'' for k in rows[0]}
            row.update(paper='I',label=label,source_run=source['source_run'],source_id=identifier,
                kind='Source-coverage disposition',status={'Proved':'proved','Refuted':'false as stated'}.get(source['source_status'],source['source_status']),
                main_or_supporting='supporting',notes=source['statement'],source_inventory_row='coverage:'+source['source_run']+':'+identifier,
                source_paper='I',in_compendium_only_because='Editorial omission: the quadratic-form counting branch A.1–A.5 is outside the five-paper selection specified here. Its complete source remains in '+source['source_proof']+'. This disposition follows '+source['scope_evidence']+'.',
                placement_state='documented editorial omission; source retained in base archive',writing_state='disposition recorded',confidence_state='no new mathematical review; source status retained',completion_state='disposition recorded; source comparison pending',
                check_record=json.dumps(source,ensure_ascii=False),check_summary='Source-register coverage comparison only.',confidence_line='The original source status is retained; this editorial decision supplies no new mathematical check.')
            rows.append(row)
    with (ROOT/'S6_SERIES_GRIND_inventory.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    history={p.get('id',p.get('label','')+'|'+p.get('old','')):p for p in previous}
    for p in applied:
        key=p.get('id',p.get('label','')+'|'+p.get('old',''))
        if key not in history or p['status']!='already applied':history[key]=p
    history_path.write_text(json.dumps(list(history.values()),indent=2,ensure_ascii=False))
    print(json.dumps({'patches':len(applied),'inventory_rows':len(rows),'details':[(p['label'],p['status']) for p in applied]}))

if __name__=='__main__':main()
