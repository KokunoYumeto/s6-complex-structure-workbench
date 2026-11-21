from pathlib import Path
import re, csv, json, hashlib, datetime, argparse
from S6_SERIES_PUBLISH_editing import Editor

ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
r=Path(__file__).resolve().parents[1]
pin='83d76022bcd442278b760db9ff438afceed6c6ea'
raw='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
receipts=[
 'agents/i_analytic/S6_SERIES_PUBLISH_I_operative_program_receipt.json',
 'agents/i_analytic/S6_SERIES_PUBLISH_I_root_program_receipt.json',
 'agents/i_analytic/S6_SERIES_PUBLISH_I_A2_program_receipt.json',
 'agents/i_provenance/S6_SERIES_PUBLISH_I_family_program_receipt.json',
 'agents/i_provenance/S6_SERIES_PUBLISH_I_boundary_program_receipt.json']
authenticated={}
for rel in receipts:
    j=json.loads((r/rel).read_text())
    for x in j.get('programs',j.get('files',[])):
        assert x['http_status']==200
        authenticated[x['url']]={'receipt':rel,'sha256':x['sha256']}
toprows=list(csv.DictReader((r/'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_program_final_rows.tsv').open(),delimiter='\t'))
for x in toprows:
    authenticated[x['opened_source_url']]={'receipt':'agents/i_topology/editorial/S6_SERIES_PUBLISH_I_boundary_program_final_rows.tsv','sha256':x['source_sha256']}

rows=(r/'records/S6_SERIES_PUBLISH_I_root_program_rows.tex').read_text()
rows=rows.replace('Period determinants, integral parameter equations and tangent ranks',
 r'Period determinants, integral parameter equations and tangent ranks; cusp deck identities and finite actions; initial node blowup with saturated equation $bw=xy$')
rows=rows.replace(r'\cref{inv:A2.1,night:P5.1,night:P5.2,night:P5.6}',
 r'\cref{inv:A2.1,night:P5.1,night:P5.2,night:P5.6,night:P2.1,night:P2.2,night:P2.5,night:P2.8,night:P2.9,night:P2.10}')
rows+=(r/'agents/i_analytic/S6_SERIES_PUBLISH_I_analytic_program_rows.tex').read_text()

def row(scope,ids,url,name):
    assert url in authenticated,url
    return scope+r'\par \cref{'+ids.replace(';',',')+r'} &'+ '\n'+r'\href{'+url.replace(pin,r'\SsixRepositoryCommit')+r'}{\nolinkurl{'+name+r'}} \\[3pt]'+'\n'

family=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_family_program_receipt.json').read_text())['programs']
for x in family:
    scope=x['mathematical_scope']
    if x['filename']=='cd_torsion_independent.py':
        scope='Exact sixth- and fourth-division recurrences for the exceptional-fibre calculations'
    rows+=row(scope,x['statement_ids'],x['url'],x['filename'])

scopes={
 'e_push_completion_diagnostics.py':r'Two-period determinant, square-zero monodromies, root differences and exceptional-valuation identities',
 'e_push_log_blowup.py':r'Exceptional valuation matrices and intersection determinants for labelled point-blowup sequences through four exceptional curves',
 'e_push_forms_translation.py':r'Canonical-form coefficients in the small charts, multiplicative limits and horizontal derivatives',
 'e_degeneration.py':r'Normalization-lattice Gram and monodromy identities; integral Smith forms for the order-three and order-four cycle matrices',
 'ab_push_local_checks.py':r'Character--ray pairings, monoid relations, three affine chart maps, section doubling, normalization Smith forms and virtual Chern pushforward',
 'ab_push_normalization_algorithm.py':r'Breadth-first star examples and local substitutions for exponents $0,1,2$ and centre codimensions $2,3,4$',
 'd_push_exact.py':r'Real-period determinant, covector equation, nonseparation vector and rational-circle generators with denominators at most twelve',
 'd_push_gradient.py':r'Finite-series numerical comparison of the theta derivative and symmetric finite differences at three points',
 'd_push_equianharmonic.py':r'Exact degree-three endomorphism and kernel congruences; formal logarithmic coefficients and rational derivative coefficient',
 'd_push_equianharmonic_crossing.py':r'Finite-product numerical derivative comparisons at three displacements near the equianharmonic point',
 'd_push_global_loop_defect.py':r'Integral monodromy and common-fixed equations; root-norm examples for degrees $1$--$64$ and connector cancellation',
 'd_push_monodromy.py':r'Affine defects of the initial parameter lift and its twelve-shift comparison terms',
 'd_push_closing.py':r'Coherent affine composition, finite and cusp defects, period/scalar comparison and twelve-shift factor',
 'ab_push_all_refinements.py':r'Primitive-ray lists at heights $1,2,3$ for $n=1,2,12$; bounded determinant tests and eight successive point stars',
 'ab_push_monodromy.py':r'Integral $E_8$ and neck matrices, Smith form and the square-zero rank-six neck operator',
 'ab_push_all_fan_topology.py':r'Cone and orbit counts for $n=1,2,12$, eight point stars and five conductor stars',
 'ab_push_all_fan_homology.py':r'Normalization-chain Smith forms for $n=1,2,3,4,6,12$ and blowup-centre increments',
 'ab_push_central_pushforward.py':r'Local exceptional complexes, unit Smith factors and Gysin maps for centre codimensions $2,3,4$',
 'b_nc_degree_one.py':r'Augmented-simplex differentials and signed permutation chain maps for at most four branches',
 'ab_push_hopf_winding.py':r'Unipotent winding, common fixed cycles, coinvariant Smith form and the exact affine closing identity',
 'root_quadric_smoothing.py':r'Four affine smoothness calculations, Hilbert difference, normal-degree cancellations and intersection Smith form',
 'ab_push_kato_weights.py':r'Fixed-curve and node character identities, tangent weights and vector-field identities for $n=1,\ldots,12$',
 'ab_push_regular_cap_dual.py':r'Integral chain maps, elementary collapses and angular cocycles for $n=4,6,12,24$',
 'ab_push_corrected_cusp_overlap.py':r'Deck differences, twelve-step affine norm, commuting shears and thirty-six primitive-cone determinants',
 'ab_push_global_partial.py':r'Finite and cusp gauge identities; node substitutions and the additive fan cocycle on the punctured parameter domain',
 'ab_push_tate_interface.py':r'Cartier and Tate factors for $n=1,2,3,4,8,12$, local base-map differentials and the closing factor',
 'd_push_degree_one_repair.py':r'Point and curve blowup substitutions, node exponents, intersection degrees and finite collar-product identities',
 'ab_push_corner_resolution.py':r'Three local chart maps, triangular fans for $n=1,2,3,4,6,12$ and collar identities'
}
for x in toprows:
    rows+=row(scopes[x['filename']],x['statement_ids'],x['opened_source_url'],x['filename'])
a2=json.loads((r/'agents/i_analytic/S6_SERIES_PUBLISH_I_A2_program_receipt.json').read_text())['files']
fan=next(x for x in a2 if x['name']=='ab_push_fan.py')
rows+=row('Exact cone, ray and fan calculations','push:src:A.2.1',fan['url'],fan['name'])

# The final provenance-owned rows are appended after their complete source reading.
extra=r/'agents/i_provenance/S6_SERIES_PUBLISH_I_boundary_program_rows.tex'
if extra.exists(): rows+=extra.read_text()
elif args.apply: raise RuntimeError('Await the provenance-owned B1--B3 program rows before applying.')

rows=rows.replace('https://github.com/KokunoYumeto/s6-complex-structure-workbench/blob/',raw)
urls=re.findall(r'\\href\{([^}]+)\}',rows)
full=[u.replace(r'\SsixRepositoryCommit',pin) for u in urls]
assert len(full)==len(set(full)), 'Duplicate source URLs'
names=[u.rsplit('/',1)[-1] for u in full]
assert len(names)==len(set(names)), 'Duplicate source filename requires exact source comparison'
for u in full: assert u in authenticated,u

table=r'''\section*{Programs}
\addcontentsline{toc}{section}{Programs}
The following files contain the indicated computations at commit
\texttt{\SsixRepositoryCommit}. Each link identifies the complete repository path.

{\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.57\textwidth}>{\raggedright\arraybackslash}p{.39\textwidth}@{}}
\caption{Programs and their mathematical scope.}\label{tab:I:programs}\\
\toprule
Computation and statement & Source file \\
\midrule
\endfirsthead
\toprule
Computation and statement & Source file \\
\midrule
\endhead
\bottomrule
\endfoot
'''+rows+r'''\end{longtable}
}

\clearpage
'''
ed=Editor('I')
labels=set(re.findall(r'\\label\{([^}]+)\}',ed.text))
for refs in re.findall(r'\\cref\{([^}]+)\}',rows):
    assert set(refs.split(','))<=labels,set(refs.split(','))-labels
(r/'records/S6_SERIES_PUBLISH_I_program_table_preview.tex').write_text(table)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'programs':len(full),'links':[{'url':u,**authenticated[u]} for u in full],
 'table_sha256':hashlib.sha256(table.encode()).hexdigest(),
 'root_adjacent_extension':'Initial blowup and saturated node equation only for night:P2.10. The selected small resolution is proved by its printed corrected coordinate maps.',
 'new_verification_files':'Distributed with exact outputs as checking records. No uncommitted path is attributed to the historical pinned repository.',
 'mathematical_check_events_added':0,'applied':args.apply}
if args.apply:
    assert r'\label{tab:I:programs}' not in ed.text
    ed.replace(r'\begin{thebibliography}{99}',table+'\n'+r'\begin{thebibliography}{99}',
       'D09','Consolidate operative program citations into one end table with exact authenticated pinned raw links, one link per source, and bounded mathematical scopes. Current verification records remain distributed with their true provenance.','tab:I:programs')
    ed.save();receipt['source_sha256']=hashlib.sha256(ed.text.encode()).hexdigest()
(r/'records/S6_SERIES_PUBLISH_I_program_table_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['programs','table_sha256','applied']}))
