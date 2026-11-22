"""Prepare exact YI source pairs and literal guards; never write canonical files."""
from pathlib import Path
import hashlib, json, re
from datetime import datetime, timezone

BASE=Path('agents/ii_checks_A/recovery_20261121T195642Z')
OUT=BASE/'group14_YI'
old_path=OUT/'S6_SERIES_PUBLISH_II_02YI_full_original.tex'
new_path=OUT/'S6_SERIES_PUBLISH_II_02YI_full_proposed.tex'
release=Path('agents/ii_infra/released_proofs/02YI/97a5d63e002e0753/S6_SERIES_PUBLISH_full_owning_block.tex')
original=release.read_text()
old_path.write_text(original)
proposed=new_path.read_text().rstrip('\n')
new_path.write_text(proposed)
sha=lambda s:hashlib.sha256(s.encode()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()

def statement_body(s):
    lo=s.index('\n\n',s.index('\\StatementRecord'))
    hi=s.index('\\end{proposition}')
    return s[lo:hi]
def proof_open(s):
    lo=s.index('\\begin{proof}')
    hi=s.index('\\item',lo)
    return s[lo:hi]
def items(s):
    lo=s.index('\\begin{proof}');hi=s.index('\\end{enumerate}',lo)
    starts=[m.start() for m in re.finditer(r'\\item\b',s[lo:hi])]
    starts=[lo+i for i in starts]+[hi]
    return [s[starts[i]:starts[i+1]] for i in range(len(starts)-1)]

specs=[
 ('[P4R.6]','[Conductor and exceptional pole divisor]',['D04','D16'],
  'Replace the run identifier in the title with the mathematical subject.',
  'The proposition tag, both labels, hypotheses and conclusions retain their identities.'),
 (statement_body(original),statement_body(proposed),['D04','D05','D20'],
  'Give the common standing torus-fibration domain and name the normalization-resolution composition; resolve the bare torsion reference.',
  'The source Part 4.2 setting is the exact standing_domain paragraph bound in the prerelease inputs. Its f, Y, B, mS and normalization are unchanged; π names the minimal resolution already required and ρ=ν∘π is the original composite. The displayed divisor identity, support, torsion and every coefficient/incidence conclusion are unchanged. The bare P4.12 maps to night:P4.12.'),
 (proof_open(original),proof_open(proposed),['D04'],
  'Use ordinary proof-item numbering.',
  'The four proof items retain their order and all mathematical content; the iteration prefix is a typographical marker.'),
]
oi,ni=items(original),items(proposed)
assert len(oi)==len(ni)==4
specs.extend([
 (oi[0],ni[0],['D02','D04','D11','D20'],
  'State the finite-duality and generic conductor maps directly and replace the defensive Q-Cartier sentence with the exact canonical-module construction.',
  'Evaluation φ↦φ(1) identifies Hom_A(B,A) with the conductor; ω_N=𝔠⊗ν*ω_S gives ρ*η=z^−c times a regular generator. Negative divisorial orders patch by the same pulled-back units and define the same integral divisor on T. No assumption on K_N is inserted or used.'),
 (oi[1],ni[1],['D08','D17','D18'],
  'Give the analytic connectedness argument, cite the opened Mumford locus, and display the row equation that proves the inverse signs.',
  'The local principal divisor H+Σn_iE_i gives Mn=−h exactly as before. The map v=diag(n_i)w identifies the displayed quadratic forms; d=diag(n_i)u gives b_i=h_i u_i+ΣM_ij n_j(u_i−u_j). Connected propagation proves the same negative-definiteness and strict positivity of −M^−1. Mumford p.6 is transported by the explicit local principal function replacing the source hyperplane difference.'),
 (oi[2],ni[2],['D20','D22'],
  'Name the strict conductor consistently and state why the pulled-back canonical line bundle has degree zero on each exceptional curve.',
  'D_h=D_str as the identical integral divisor on T. Restriction along E_i→{ρ(E_i)} gives degree zero, hence the identical Md=−b equation. The adjunction, nonnegative summands and connected zero-block argument give exactly the original smooth rational (−2)-curve conclusion.'),
 (oi[3],ni[3],['D04','D17','D18','D20','D22'],
  'Specify the quotient conductor locus and the exact unit, local-fibre and oriented-sphere maps, cite the opened primary inputs, and finish the torsion pullback explicitly.',
  'The conductor locus is Supp(O_N/𝔠), as used by the reflexive-ideal argument. The local morphism is h=exp((log u)/m)g with f=h^m, so h=δ includes into f=δ^m. Proper boundary-tangent transport carries the quadratic sphere of normal Euler number −2 into this local fibre. Its lift through C²→T⁴ forces zero global homology and contradicts that same normal Euler number. Thus every exceptional fibre meets D_str and b≠0; the already proved inverse signs give positive integral coefficients, the exact support equality and (ω_T(D))^m=ρ*(ω_S^m)=O_T. All four original item-4 conclusions are retained.'),
])

current=original;guards=[]
for i,(old,new,defects,reason,transport) in enumerate(specs,1):
    assert old!=new
    assert current.count(old)==1,(i,current.count(old))
    before=sha(current);at=current.index(old);current=current[:at]+new+current[at+len(old):]
    guards.append({'tag':'02YI','guard_id':f'A_REC_02YI_{i:03d}',
        'literal_old':old,'literal_new':new,'defect_types':defects,
        'reason':reason,'mathematical_transport':transport,'offset_before':at,
        'intermediate_before_sha256':before,'intermediate_after_sha256':sha(current),
        'full_original_path':str(old_path),'full_proposed_path':str(new_path)})
assert current==proposed
inverse=current
for g in reversed(guards):
    assert sha(inverse)==g['intermediate_after_sha256']
    at=g['offset_before'];assert inverse[at:at+len(g['literal_new'])]==g['literal_new']
    inverse=inverse[:at]+g['literal_old']+inverse[at+len(g['literal_new']):]
    assert sha(inverse)==g['intermediate_before_sha256']
assert inverse==original

canonical=Path('S6_SERIES_PUBLISH_II.tex').read_text()
bib=canonical[canonical.index('\\begin{thebibliography}'):canonical.index('\\end{thebibliography}')]
def entry(key):
    at=bib.index('{'+key+'}');lo=bib.rfind('\\bibitem',0,at);hi=bib.find('\\bibitem',at)
    return bib[lo:hi if hi!=-1 else len(bib)]
bibliography=[]
for key in ('Milnor1968','Mumford1961'):
    old=entry(key)
    if key=='Milnor1968':
        new=old.replace('Princeton University Press, 1968.','Princeton University Press and University of Tokyo Press, 1968.')
        new=new.replace('\\newblock URL \\url{https://djvu.online/file/kCFrJq27uCPRi}.\n\n','')
        reason='Use the two publishers on the opened 1968 title page and remove the third-party viewer URL from the manuscript bibliography.'
        transport='Same author, title, series, volume and 1968 edition. The title-image SHA is 3d398f31b38bbe67091e3b31f1f6a2f5e1078f7a4f08e736c94eeb19e02af1c4. Viewer access remains in the primary reading receipt. No unverified DOI is added.'
        defects=['D18']
    else:
        new=old.replace('\\newblock \\emph{Verified}.\n','')
        reason='Remove the workflow status marker from the bibliographic entry.'
        transport='All bibliographic data and both DOI and Numdam URL remain byte-identical; the source is the opened original 1961 journal article.'
        defects=['D08','D18']
    assert old!=new
    op=OUT/f'S6_SERIES_PUBLISH_II_YI_{key}_original.tex';np=OUT/f'S6_SERIES_PUBLISH_II_YI_{key}_proposed.tex'
    op.write_text(old);np.write_text(new)
    bibliography.append({'key':key,'literal_old':old,'literal_new':new,'old_sha256':sha(old),'new_sha256':sha(new),'defect_types':defects,'reason':reason,'mathematical_transport':transport,'original_path':str(op),'proposed_path':str(np)})

lo=canonical.index('\\section*{Programs}');hi=canonical.index('\\end{longtable}',lo)+len('\\end{longtable}')
table=canonical[lo:hi]
new_rows=''
for scope,filename in [
 ('Weighted intersection identities, sphere orientation and quadratic Hessian determinant','S6_SERIES_PUBLISH_II_A_02YI_interpolation_certificate.py'),
 ('Quadratic-fibre coordinate inverses and local intersection orientations','S6_SERIES_PUBLISH_II_A_02YI_A1_transport_postrelease.py')]:
    new_rows+=scope+r' (\cref{night:P4R.6}) & \href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\SsixRepositoryCommit/code/'+filename+r'}{\nolinkurl{'+filename+r'}} \\[3pt]'+'\n'
new_table=table.replace('\\end{longtable}',new_rows+'\\end{longtable}')
top=OUT/'S6_SERIES_PUBLISH_II_YI_programs_original.tex';tnp=OUT/'S6_SERIES_PUBLISH_II_YI_programs_proposed.tex'
top.write_text(table);tnp.write_text(new_table)
program_guard={'literal_old':table,'literal_new':new_table,'old_sha256':sha(table),'new_sha256':sha(new_table),
 'original_path':str(top),'proposed_path':str(tnp),'old_row_count':table.count('\\\\[3pt]'),'new_row_count':new_table.count('\\\\[3pt]'),
 'added_rows':new_rows,'defect_types':['D09'],
 'reason':'List the two complete YI programs and their mathematical scopes in the end table.',
 'mathematical_transport':'The interpolation program proves universal local edge/anchor/row identities and the explicit sphere orientation/cell and Hessian arithmetic; the geometric coefficient signs are proved in the text. The postrelease program proves the exact A1 coordinate and orientation maps to the previously checked n=1 compactification. No independent check is created by this listing; all existing rows are retained.'}

record={'created_utc':utc(),'checker':'ii_check_a','canonical_writes':0,'guards':guards,
 'blocks':[{'tag':'02YI','original_path':str(old_path),'proposed_path':str(new_path),
 'original_sha256':sha(original),'proposed_sha256':sha(proposed),'statement_unchanged':True,
 'statement_precision':'The full standing domain and π,ρ notation are made explicit; every original hypothesis and conclusion is retained.',
 'proof_repairs':[],'scope_repairs':[]}],
 'bibliography_guards':bibliography,'program_table_guard':program_guard,
 'note':'All four proof items remain. This file proposes edits only. The complete mathematical comparison and actual rereading are separate evidence; guard generation adds no check credit.'}
(OUT/'S6_SERIES_PUBLISH_II_A_YI_editorial_proposals.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
validation={'validated_utc':utc(),'tag':'02YI','guard_count':len(guards),'forward_complete_equality':current==proposed,'inverse_complete_equality':inverse==original,
 'original_sha256':sha(original),'proposed_sha256':sha(proposed),'original_proof_items':len(oi),'proposed_proof_items':len(ni),
 'bibliography_guard_count':len(bibliography),'program_table_rows':[program_guard['old_row_count'],program_guard['new_row_count']],
 'canonical_snapshot_sha256':sha(canonical),'canonical_writes':0,'validation_scope':'Exact literal application and inverse byte equality only; no mathematical assurance is generated by this script.'}
(OUT/'S6_SERIES_PUBLISH_II_A_YI_guard_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(validation,indent=2))
