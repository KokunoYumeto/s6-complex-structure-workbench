"""Apply audited K64/K65 counterexamples and precise legacy cross-references."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,re,shutil

root=Path(__file__).resolve().parents[1]
audit=json.loads((root/'records/scalar_cross_reference_audit.json').read_text())
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
saved=root/'records/attempts/scalar_cross_reference_repair'/stamp
saved.mkdir(parents=True)
changes=[]; originals={}

def preserve(path):
    rel=path.relative_to(root)
    if str(rel) not in originals:
        target=saved/rel
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,target)
        originals[str(rel)]=hashlib.sha256(path.read_bytes()).hexdigest()

aggregate=root/'notes/part3.tex'
assert hashlib.sha256(aggregate.read_bytes()).hexdigest()==audit['aggregate_sha256']
preserve(aggregate)
text=aggregate.read_text()
for row in audit['exact_proposed_replacements']:
    assert text.count(row['old'])==1,(row['statement'],text.count(row['old']))
    text=text.replace(row['old'],row['proposed_new'])
    changes.append({'file':'notes/part3.tex','statement':row['statement'],
                    'old':row['old'],'new':row['proposed_new']})
for name in ('part3_scalar_vertical_fans','part3_os49_corrected_returns'):
    line=r'\input{notes/'+name+'.tex}'
    assert line not in text
    text+='\n'+line+'\n'
aggregate.write_text(text)

# Repair matching source prose and hardcoded summaries without regenerating
# the manually typeset aggregate.
paths={row['file'] for row in audit['regeneration_sources']}
for name in sorted(paths):
    path=root/name
    old=path.read_text(); new=old
    for row in audit['exact_proposed_replacements']:
        pattern=re.escape(row['old']).replace(r'\ ',r'\s+')
        new,count=re.subn(pattern,lambda _:row['proposed_new'],new)
        if count:
            changes.append({'file':name,'statement':row['statement'],
                            'reflow_matches':count,'old':row['old'],'new':row['proposed_new']})
    if new!=old:
        preserve(path);path.write_text(new)

generator=root/'code/part3/render_part3_tex.py'
preserve(generator)
text=generator.read_text()
needle="source=(root/'notes/part3_family.md').read_text()"
assert text.count(needle)==1
text=text.replace(needle,
 "# Retain the complete independently authored include sequence on regeneration.\n"
 "existing_aggregate=(root/'notes/part3.tex').read_text()\n"
 "preserved_includes=re.findall(r'^\\\\input\\{notes/[^}]+\\}\\s*$',existing_aggregate,re.M)\n"+needle)
old="out.append(r'\\input{notes/part3_fourfold.tex}'+'\\n')"
assert old in text
text=text.replace(old,
 "for include in (preserved_includes or [r'\\input{notes/part3_fourfold.tex}']):\n"
 "    out.append(include.strip()+'\\n')")
generator.write_text(text)

scope=json.loads((root/'records/scalar_fan_correction_scope.json').read_text())
replacement={
'P3K.17':r'The asserted two-fan equality is false. P3K.65 constructs the full negative-to-positive native Cox comparison and gives classes -3k and 0 for the positive r-loop, and -k and 0 for the actual shorter w-loop. At k=1 the original negative fan has classes 25 and 27, respectively. The omitted second outer map has positive-normal determinant winding -2m; the first outer map is the identity. The local charged-cap construction is retained with its full outer marking.',
'P3K.25':r'The asserted all-shear equality is false. In the explicitly constructed primitive OS45 family of P3K.10/P3K.22, the actual scalar loop has J=1 and reference class -3. P3K.64 gives class -4 on T_2, whose directions are e_2,(1,2),(1,1). The direct initial/reflected C2 equality remains the narrow comparison proved in P3K.62. The outer C1 determinant has the previously omitted winding -2J.',
'P3K.29':r'The claimed simultaneous marked delta-equivariant plumbing product does not exist for nonzero scalar winding J: P3K.61 derives the incompatible determinant equation -J=0. In the actual native C1 product, P3K.62 gives the single free pair (J,-J), contradicting the stated zero right coefficient at J=1. The integral cells, common-exterior bases, dual maps, symmetry and exact local frame-change identity remain valid in their displayed markings.',
'P3K.31':r'The universal fan polynomial is false. The primitive OS45 family of P3K.10/P3K.22 has reference class -3 and scalar winding J=1. On the actual T_2 fan, delta has coordinates (0,1), so the displayed S formula still gives -3; P3K.64 constructs the full maps and proves the value -4. The single-star product-frame, boundary flop and complex normal reset maps are retained; the scalar initial data and universal formula are withdrawn.',
'P3K.34':r'The universal OS49 fan formula is false. For k=1 the original negative-diagonal fan has S=1 in its primitive H/K marking, so the displayed formula gives 0; P3K.65 proves the actual positive r-loop class -3. The independently constructed positive-fan page and its zero index are retained. P3K.65 also proves the actual shorter negative-fan class -k, with positive-fan class 0; no negative-fan integer is assigned.'
}
for sid,notice in replacement.items():
    path=root/scope['scope'][sid]['file']
    preserve(path)
    text=path.read_text()
    start=text.index(r'\begin{statement}{'+sid+'}')
    end=text.index(r'\end{statement}',start)
    block=text[start:end]
    assert '{Unresolved; scalar-fan audit correction}' in block
    block=block.replace('{Unresolved; scalar-fan audit correction}',
                        '{Refuted; corrected scalar-fan computation}',1)
    a=block.index(r'\par\noindent\textbf{Audit correction, 17 November 2026.}')
    b=block.index(r'\medskip',a)
    block=block[:a]+r'\par\noindent\textbf{Audit correction, 17 November 2026.} '+notice+' The earlier statement and argument below are preserved as the located prior claim.\n'+block[b:]
    text=text[:start]+block+text[end:]
    path.write_text(text)
    scope['scope'][sid]['status']='Refuted'
    scope['scope'][sid]['correction']=notice
    scope['scope'][sid]['repair_proofs']=['P3K.61','P3K.62','P3K.64','P3K.65']
    changes.append({'file':str(path.relative_to(root)),'statement':sid,
                    'new_status':'Refuted','new_notice':notice})
ledger=root/'records/scalar_fan_correction_scope.json'
preserve(ledger)
scope['updated_utc']=datetime.now(timezone.utc).isoformat()
scope['new_repair_scope']='K64 proves the signed vertical canonical scalar line of fans; K65 proves both actual OS49 diagonal returns, including the shorter parameter. Other arbitrary-fan assertions remain reopened.'
ledger.write_text(json.dumps(scope,indent=2)+'\n')

record={'status':'APPLIED','utc':datetime.now(timezone.utc).isoformat(),
 'changes':changes,'preserved_directory':str(saved.relative_to(root)),
 'preserved_sha256':originals,'new_includes':['P3K.64','P3K.65'],
 'unpromoted':'P3K.66 remains outside the master pending the actual Euler/meridian orientation comparison.'}
(root/'records/scalar_cross_reference_repair.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'APPLIED','changes':len(changes),
                  'preserved_files':len(originals),'refuted':list(replacement)},indent=2))
