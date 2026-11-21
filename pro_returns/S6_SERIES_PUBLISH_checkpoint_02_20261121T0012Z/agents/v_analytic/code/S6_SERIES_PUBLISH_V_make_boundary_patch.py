"""Guarded canonical-parameter corrections for the boundary section."""
from pathlib import Path
import json,hashlib
base=Path(__file__).resolve().parent.parent
source=base.parents[1]/'S6_SERIES_PUBLISH_V.tex'
original=source.read_text(); current=original; items=[]
def add(location,old,new,reason,kind='D08'):
 global current
 assert current.count(old)==1,(location,current.count(old))
 items.append(dict(type=kind,location=location,old_text=old,new_text=new,
                   expected_count=1,reason=reason,
                   old_pdf_page='root to fill from corrected baseline',
                   new_pdf_page='root to fill after final pagination'))
 current=current.replace(old,new,1)

add('boundary section setup',r'''Fix one splitting and write the complex parameter as $\xi$, so that
$F_\xi=(\sigma+\xi\alpha e)(P)$. Put
$c_*=-\min h$ and $\mathcal H=\{\operatorname{Im}\xi>c_*\}$.
The real family is $\xi=ic$, $c\in\mathbb R$.''',r'''We use the canonical splitting $\sigma_b$, height $h_b$, parameter
domain $\mathcal U$ and family $M_\xi$ of \cref{pub:V:parameter}.
The exact coordinate change for another splitting is
\cref{rem:V:splitting-change}.''',
'Use the single normalization; PV04 already proves the exact splitting-to-parameter transport.')
add('analytic-extension definition',
'restriction to the nonempty open part lying in $\\mathcal H$ is',
'restriction to the nonempty open part lying in $\\mathcal U$ is',
'Keep the parameter domain fixed by PV14.')
add('night:P1A.5 statement',
'point of $\\mathcal H$, or across infinity.',
'point of $\\mathcal U$, or across infinity.',
'Use the canonical parameter domain.')
add('night:P1A.5 proof item 5 period marking',r'''known open set it is the explicit graph
$F_\xi=(\sigma+\xi\alpha e)(P)$.  The identity theorem on the
connected cover identifies these two maps everywhere.''',r'''known open set it is
$\widehat F_\xi=K F_\xi$, by
\cref{rem:V:conjugation-parameter}. Applying the fixed real
integral change of marking $K^{-1}$ identifies it with the
canonical plane $F_\xi=(\sigma_b+\xi\alpha e)(P)$.
The identity theorem on the connected cover then identifies
these two maps everywhere.''',
'Transport the actual compact-family Hodge plane to the algebraic plane by the exact integral matrix before applying analytic continuation.')
add('night:P1A.5 proof item 6 height',r'''$\operatorname{Im}\xi_0=c_*=-\min h$.
The minimum may occur at a finite root point.  Continuity
there nevertheless gives regular $\lambda$ with $h(\lambda)$
arbitrarily close to $\min h$.''',r'''$\operatorname{Im}\xi_0=c_*=-\min h_b$.
The minimum occurs at $\lambda=\infty$ by \cref{night:P1.18}.
Continuity on its root chart gives regular $\lambda$ with
$h_b(\lambda)$ arbitrarily close to $\min h_b$.''',
'Use the proved minimum location and normalized height in the failure-locus argument.')
add('night:P1A.5 failure locus',
'\\operatorname{Im}\\xi+h(\\lambda)=0.',
'\\operatorname{Im}\\xi+h_b(\\lambda)=0.',
'Match the exact transversality criterion of the merged lift theorem.')
add('night:P1A.5 infinity failure locus',r''' \xi=R-i h(\lambda),\qquad
 u=\frac1{R-i h(\lambda)},\qquad R\in\mathbb R.''',r''' \xi=R-i h_b(\lambda),\qquad
 u=\frac1{R-i h_b(\lambda)},\qquad R\in\mathbb R.''',
'Use the same normalized height at infinity.')
add('night:P1A.6 statement domain',
'a holomorphic map of the full disc to $\\mathcal H$, and',
'a holomorphic map of the full disc to $\\mathcal U$, and',
'Use the canonical parameter domain.')
add('night:P1A.6 local classifying maps',
'$\\mathcal H$. \\Cref{night:P1A.4} makes this map unique',
'$\\mathcal U$. \\Cref{night:P1A.4} makes this map unique',
'Use the canonical parameter domain.')
add('night:P1A.6 glued classifying map',
'one holomorphic function $\\xi:\\Delta^*\\to\\mathcal H$.',
'one holomorphic function $\\xi:\\Delta^*\\to\\mathcal U$.',
'Use the canonical parameter domain.')
add('night:P1A.6 extended classifying map',
'$\\xi$ with value in $\\mathcal H$.',
'$\\xi$ with value in $\\mathcal U$.',
'Use the canonical parameter domain.')
add('night:P1A.6 external Cartan reference',
"Cartan's Theorem~\\ref{series:V:B}","Cartan's Theorem~B",
'Restore the external theorem name; the Paper V theorem reference is unrelated.','D12')

out=base/'S6_SERIES_PUBLISH_V_boundary_guarded_replacements.json'
out.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
receipt={'source_sha256':hashlib.sha256(original.encode()).hexdigest(),
         'sequential_replacements':len(items),'all_expected_counts':1,
         'main_source_written':False,
         'exact_transport':'sigma=sigma_b+z0 alpha e => xi_b=xi+z0; h_sigma=h_b+Im(z0); c_sigma=c_b-Im(z0)',
         'proof_scope':'Coordinate and marking corrections; no change to the analytic-extension definition or its permitted singular central spaces.'}
(base/'S6_SERIES_PUBLISH_V_boundary_guarded_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
