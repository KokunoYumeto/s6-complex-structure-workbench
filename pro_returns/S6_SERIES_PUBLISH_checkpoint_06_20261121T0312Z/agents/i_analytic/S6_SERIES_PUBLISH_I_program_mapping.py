"""Create the analytic contribution to the single program table."""
from pathlib import Path
import csv,json,collections,hashlib
B=Path(__file__).parent
receipt=json.loads((B/'S6_SERIES_PUBLISH_I_operative_program_receipt.json').read_text())
programs=receipt['programs']
assert len(programs)==29
assert len({x['repository_path'] for x in programs})==29
cols=['filename','statement_ids','commit','path','bytes','sha256','verification_basis','url']
with (B/'S6_SERIES_PUBLISH_I_analytic_program_map.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
 for x in programs:
  w.writerow(dict(filename=Path(x['path']).name,statement_ids=x['statement_ids'],
   commit=x['commit'],path=x['repository_path'],bytes=x['bytes'],sha256=x['sha256'],
   verification_basis=x.get('verification_basis','Primary immutable I tree; matching Git blob hash/byte size'),
   url=x['url'].replace('raw.githubusercontent.com/','github.com/').replace('/'+x['commit']+'/', '/blob/'+x['commit']+'/')))
groups=collections.OrderedDict()
for x in programs:groups.setdefault(x['group'],[]).append(x)
lines=['% Analytic/arithmetic rows for the one final Paper I program table.']
for group,rows in groups.items():
 ids=','.join(dict.fromkeys(z for x in rows for z in x['statement_ids'].split(';')))
 title=rows[0]['mathematical_scope'].replace('Q(sqrt(3))',r'$\mathbb Q(\sqrt3)$')
 links=[]
 for x in rows:
  links.append(r'\href{https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/\SsixRepositoryCommit/'+x['repository_path']+r'}{\nolinkurl{'+Path(x['path']).name+'}}')
 lines.append(r'\hypertarget{prog:I:'+group+r'}{}'+title+r'\par \cref{'+ids+'} &\n'+r'\par '.join(links)+r' \\[3pt]')
(B/'S6_SERIES_PUBLISH_I_analytic_program_rows.tex').write_text('\n'.join(lines)+'\n')
record_only={
 'cd_numerics.py':'Duplicate decimal corroboration; exact finite-period corollary retained.',
 'cd_special_intervals.py':'Earlier decimal agreement/coarse enclosure moved to verification records.',
 'cd_bounds.py':'Preliminary bound superseded by the retained exact maximum proof.',
 'cd_local_bound.py':'Preliminary local bound superseded by the retained exact local theorem.',
 'f_interval_parallel.py':'Independent full-domain interval proof archived after selecting the division-ladder proof.',
 'f_interval_cert.py':'Independent full-domain interval proof archived after selecting the division-ladder proof.',
 'f_interval_verify.py':'Independent full-domain interval proof archived after selecting the division-ladder proof.',
 'e4_arb_certificate.py':'Duplicate interval proof archived with push E4.1/E4.2.',
 'e4_cover_and_local.py':'Duplicate interval proof archived with push E4.1/E4.2.',
 'Cspecial_torsion_numerics.py':'Numerical theta corroboration of the exact division values; full original retained in records.',
 'Cspecial_reflection.py':'Matrix corroboration of the full retained fam B4.2 proof; C2.2 now a corollary with unique correcting vectors retained.',
 'C_ladder_algebra.py':'Historical duplicate rational recurrence calculation. The authenticated Cspecial_division.py supplies the same psi_n recurrence through n=9, including the n=2,4,8 polynomials used in C8.4.',
 'C_ladder_estimates.py':'Original explicitly calls this numerical diagnostics; displayed rational estimates and remainder bounds are the proof.',
 'C_local_analytic_bounds.py':'Original explicitly calls this numerical diagnostics; displayed rational estimates and remainder bounds are the proof.',
 'ari_C2_C3_fresh.py':'Earlier checking program; no proof input in the selected body.',
 'C_cm_class_polynomials.gp':'Original independent class-polynomial crosscheck; reduced-form enumeration plus Fourier enclosures retained.',
 'cm_analytic_balls.py':'Numerical corroboration of the exact compact CM witness; exact algebraic program is the operative table entry.',
}
mapping={'receipt':'S6_SERIES_PUBLISH_I_operative_program_receipt.json',
 'operative_program_count':len(programs),'operative_groups':len(groups),
 'citation_policy':'One immutable link per program in the single end table, using the shared SsixRepositoryCommit macro. Body computational algorithms remain mathematical prose; no file paths reinstated there.',
 'scope_limit':'This mapping authenticates primary source files and assigns their operative mathematical tasks. It does not claim these historical programs were newly executed or independently verified in this run.',
 'record_only_programs':record_only,
 'own_new_check_programs':'All S6_SERIES_PUBLISH_I_* checking scripts remain in the check record/code deliverable. They do not become proof inputs merely because they were run.'}
(B/'S6_SERIES_PUBLISH_I_analytic_program_disposition.json').write_text(json.dumps(mapping,indent=2)+'\n')
print(json.dumps({'programs':len(programs),'groups':len(groups),'record_only_names':len(record_only),'one_link_each':True}))
