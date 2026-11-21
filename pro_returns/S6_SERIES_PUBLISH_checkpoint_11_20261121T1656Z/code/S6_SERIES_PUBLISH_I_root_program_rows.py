from pathlib import Path
import csv,json,hashlib
r=Path(__file__).resolve().parents[1]
p=r/'agents/i_analytic/S6_SERIES_PUBLISH_I_root_program_map.tsv'
rows=list(csv.DictReader(p.open(),delimiter='\t'));d={x['filename']:x for x in rows}
groups=[
 ('integral-algebra','Period determinants, integral parameter equations and tangent ranks',r'\cref{inv:A2.1,night:P5.1,night:P5.2,night:P5.6}',['priority_rows_exact.py','adjacent_exact.py']),
 ('double-complex','Finite double-complex matrices and their cohomology',r'\cref{inv:C1.1,inv:C2.1}',['main_D_double_complex.py']),
 ('coefficient-atlas','Regular-chart identities, cusp Cartier factors and finite-collar first jets',r'\cref{inv:C3.8}',['exact_regular_atlas.py','cusp_and_finite_exact.py','finite_collar_jet_verifier.py']),
 ('koszul','Tangent-twist Smith modules and stabilizer-character jet ranks',r'\cref{inv:D4.4}',['d_koszul.py']),
 ('covers','Weighted section counts and rational boundary maps of finite covers',r'\cref{inv:B2.2,inv:B3.1,inv:B3.3}',['b_families.py','b_topology.py']),
 ('resonance','Division-polynomial factors at the marked elliptic section',r'\cref{inv:D4.3}',['d_division_polynomials.py']),
]
out=[]
for key,description,labels,files in groups:
 links=[]
 for f in files:
  x=d[f];assert x['commit']=='83d76022bcd442278b760db9ff438afceed6c6ea'
  links.append(r'\href{'+x['url'].replace(x['commit'],r'\SsixRepositoryCommit')+r'}{\nolinkurl{'+f+'}}')
 out.append(r'\hypertarget{prog:I:'+key+'}{}'+description+r'\par '+labels+' &\n'+r'\par '.join(links)+r' \\[3pt]')
q=r/'records/S6_SERIES_PUBLISH_I_root_program_rows.tex';q.write_text('\n'.join(out)+'\n')
print(json.dumps({'table_rows':len(groups),'unique_files':len(d),'path':str(q),'map_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Exact finite calculation scopes, authenticated source links only; no new execution or mathematical check event.'}))
