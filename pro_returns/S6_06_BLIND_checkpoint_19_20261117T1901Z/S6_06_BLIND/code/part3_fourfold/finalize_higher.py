#!/usr/bin/env python3
"""Record the higher-parameter certificate and its exact scope."""
from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[2]
path=Path(__file__).with_name('results_mapping.json')
data=json.loads(path.read_text())
entry={
 'id':'P3K.11','status':'Proved','item_of_prompt':'3.3',
 'statement':'The marked higher (3K,4L) family has exact c-period 2KL and closed parameter w_h=exp(-pi*i*c/(KL)); the positive-gamma sphere marking has descended rotating pair (-KL,-4KL).',
 'proof_file':'notes/part3_higher_parameter.md',
 'latex_file':'notes/part3_fourfold.tex',
 'own_value':'For a=4L*n0+3K*n1=+1: k=-KL, ell=-4KL. For either sphere sign a=±1: A=0 on the positive w_h-loop.',
 'parameter_dictionary':{'original_w':'exp(-pi*i*c)',
     'higher_w':'exp(-pi*i*c/(K*L))',
     'scalar':'u=kappa*w_h^(2*K*L)',
     'gamma_cover':'w_h=r^6',
     'ordinary_w':'w=w_h^(K*L)'},
 'H2_lattice_sheaf':'Z plus Z/(2*K*L)',
 'comparison':'agrees under the explicitly fixed higher parameter and descended rotating framing',
 'certificate':'code/part3_fourfold/higher_parameter.json',
 'symbolic_matrices':'Full cochain blocks, polynomial unimodular reductions, and exact image right inverse are exported.',
 'scope':'The torsor period is the marked translation period; it does not assert a classification of all unmarked automorphisms. The individual pair is assigned only to the a=+1 sphere marking; the signed angular identity and A=0 treat both signs.'}
key=next(k for k,v in data.items() if isinstance(v,list) and any(isinstance(x,dict) and x.get('id')=='P3K.10' for x in v))
data[key]=[x for x in data[key] if x.get('id')!='P3K.11']+[entry]
path.write_text(json.dumps(data,indent=2)+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'records/literature_fourfold.md').open('a') as f:
    f.write('\n## '+stamp+' — higher-order parameter certificate\n\n')
    f.write('Completed the previously logged read of the supplied Viaclovsky source, '
      '`../background/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex`. '
      'Material taken: good-reduction root orders 3K,4L; primitive finite logarithmic vectors; '
      'the literal logarithmic annulus maps; the fixed scalar u in the source translation lift. '
      'The source supplies a local deformation disc and does not itself specify the closed higher parameter used here.\n\n')
    f.write('Read current-team `code/part5/orbifold_lattice_complex.py` only for its integer lattice complex, '
      'finite invariant bases and norms, as requested by the parent; no prohibited tangent or full automorphism source was read. '
      'The parent supplied the established period identity and extending Cech construction of P5.6. '
      'Read current-team P3F.17 and the signed-loop paragraphs of `notes/part3.tex` to identify the proved higher page data. '
      'Material taken: degree12KL, line square -2KL, relative p1 -24KL, and actual gamma orientation.\n\n')
    f.write('Executed `higher_parameter.py`: symbolic d1*d0=d2*d1=0; twelve unimodular polynomial unit eliminations; '
      'exact two-sided image certificate to three relations; eight full-complex Smith checks. '
      'Derived the marked c-period2KL and explicit w_h coordinate, then the pair (-KL,-4KL) '
      'using the already proved real trace and normal-frame descent. Full proof exported as P3K.11.\n')
print('Recorded P3K.11, exact parameter dictionary, and source-use audit.')
