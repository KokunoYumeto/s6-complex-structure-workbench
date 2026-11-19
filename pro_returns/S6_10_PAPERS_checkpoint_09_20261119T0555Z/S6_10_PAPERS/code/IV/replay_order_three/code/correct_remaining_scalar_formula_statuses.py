"""Preserve and correct historical scalar-polynomial claim statuses."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil
root=Path(__file__).resolve().parents[1]
archive=root/'records/attempts/remaining_scalar_polynomial_claims'
archive.mkdir(parents=True,exist_ok=True)
rows={
 'P3K.33':('part3_original_cox_descent.tex','The actual original K=L=1 shorter loop on T_2 has physical class26; the displayed S=1 polynomial gives0.'),
 'P3F.53':('part3_canonical_scalar_catalogue.tex','The fully specified primitive OS45 reference loop has physical class3; the displayed reference value is-3=25.'),
 'P3K.35':('part3_weighted_shorter_loop.tex','The same primitive OS45 datum has b=1 and physical reference class3; its displayed formula gives25.'),
 'P3K.36':('part3_liu_rollenske_parameter.tex','The actual corrected u=w^2 Liu--Rollenske family on T_2 has physical class26; the displayed S=1 polynomial gives0.'),
 'P3K.37':('part3_os49_shorter_loop.tex','The actual shorter OS49 k=1 loop on the negative fan has class27 by K65; its displayed S=1 polynomial gives0.'),
 'P3K.41':('part3_fixed_source_cap_loops.tex','The primitive OS45 cap-data loop with N=1 on T_0 has class3; its displayed formula gives25.'),
 'P3K.43':('part3_moving_order_one_sites.tex','The same allowed OS45 loop with constant ordinary-site paths has class3; its displayed formula gives25.'),
 'P3K.44':('part3_os49_cap_loops.tex','The actual OS49 fixed-chart loop with k=N=1 on the negative fan has class27; its displayed formula gives0.')}
records=[]
for ident,(name,reason) in rows.items():
 p=root/'notes'/name; old=p.read_text(); target=archive/name
 if not target.exists():shutil.copy2(p,target)
 prefix=r'\begin{statement}{'+ident+'}'
 source=re.sub(re.escape(prefix)+r'\{[^}]*\}',lambda _:prefix+'{Refuted; exact counterexample P3K.74}',old,count=1)
 notice='\n\\par\\noindent\\textbf{Proved counterexample, 17 November 2026.} '+reason+' P3K.74 gives the actual data and proof. P3K.73 supplies the corrected complete scalar-fan algorithm in the whole-zero I1 scope. The earlier assertion and argument below are preserved as the false compound claim; their explicitly retained construction and comparison maps are identified in P3K.74.\n'
 pos=source.index('\n',source.index(prefix))
 if 'Proved counterexample, 17 November 2026.' not in source:source=source[:pos]+notice+source[pos:]
 p.write_text(source)
 records.append({'id':ident,'status':'Refuted','file':str(p.relative_to(root)),'counterexample':reason,'preserved':str(target.relative_to(root))})
p=root/'notes/part3_vertical_line_exhaustion.tex';target=archive/p.name
if not target.exists():shutil.copy2(p,target)
s=p.read_text()
s=s.replace(r'\begin{statement}{P3F.52}{Unresolved; scalar-fan audit correction}',r'\begin{statement}{P3F.52}{Proved; actual-return comparison corrected}')
start=s.index(r'\par\noindent\textbf{Audit correction, 17 November 2026.}')
end=s.index(r'\medskip',start)
s=s[:start]+r'''\par\noindent\textbf{Completed comparison, 17 November 2026.}
The actual invariant-divisor, root-evaluation and collar morphisms
below identify the constructed families and preserve their actual
returns. P3K.74 supplies the precise return-map conjugacy and
P3K.73 the corrected complete numerical algorithm. The former
appeal to the false P3K.31 recurrence is replaced; its exact prior
text is preserved in the correction archive.
'''+s[end:]
s=s.replace('characteristic pair, the relative index and the all-fan formula\nin the transported Cox product.','characteristic pair, the relative index and the actual return\ncomputed by P3K.73 in the transported native and ordinary products.')
s=s.replace(r'\begin{proof}[Preserved earlier argument; scope corrected above]',r'\begin{proof}')
s=s.replace('The K31 common-exterior recurrence\nthen retains the same fan integer.','The transported family connection has literally conjugate holonomy\nand specified inverse endpoint. The typed conjugacy in P3K.74\ntherefore preserves its physical sphere class. Each full period\nunit, native product and Cox ruling arrow of P3K.73 is carried by\nthis family isomorphism, so its exact algorithm gives that same\nactual value on the transported fan.')
p.write_text(s)
records.append({'id':'P3F.52','status':'Proved','file':str(p.relative_to(root)),
 'correction':'The actual family isomorphism and covariance are proved. The false imported numerical recurrence was a proof defect, not a counterexample to covariance; it is replaced by the literal return conjugacy and K73 algorithm.',
 'preserved':str(target.relative_to(root))})
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','claims':records,
        'proof':'notes/part3_scalar_formula_corrigendum.tex','certificate':'code/part3_root/refute_remaining_scalar_polynomials.json',
        'scope':'No unresolved source-zero, other OS49 fan, source-moduli or unmarked endpoint value is assigned by these status corrections.'}
(root/'records/remaining_scalar_formula_correction_scope.json').write_text(json.dumps(record,indent=2)+'\n')
print('Eight compound formulas refuted; F52 actual covariance reproved. All prior texts preserved.')
