"""Main-group reuse diagrams from explicitly inspected body maps."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
EXPLICIT={
'I':[
 ('A','B','fam:src:C.2.3','ari:C.2.1','The exact parameter domain is used for the intrinsic Albanese nome.'),
 ('E','B','fam:src:B.4.1','mapsI:src:A.3.1','The automorphism group acts in the conjugacy classification of real involutions.'),
 ('D','E','inv:C1.1','inv:C3.1','The differential and Bott--Chern dimensions determine the Picard curvature statement.'),
 ('B','G','fam:src:A.1.1','push:src:D.1.3','The intrinsic multiplicity-four divisor supplies the Albanese continuation obstruction.'),
 ('G','A','push:src:D.2.1','ari:C.8.2','The half-period derivative identity supplies the theta-heat calculation.')],
'III':[
 ('A','B','mapsI:src:A.2.1','maps:src:B.1.2','The repaired quotient and its target/collar data fix the map whose framed regular inverse image is computed.')],
'V':[
 ('B','C','maps:src:F.2.5','maps:src:F.3.5','The exterior-square identity F.11 gives the explicit period representation for the stated integral matrices.'),
 ('A','D','maps:src:E.1.2','maps:src:F.3.7','The same marked Kuhn period-action proof supplies smoothness and properness for the nonsymmetric bounded cusp correction.'),
 ('B','D','maps:src:F.2.6','maps:src:F.4.1','The integral homology and middle form enter the oriented extended-form classification.'),
 ('C','D','maps:src:F.3.6','maps:src:F.3.7','The constructed preceding period family is conjugated on base and fibres to give precisely the specified homology monodromy.')]
}

def records(paper):
 if paper in EXPLICIT:return EXPLICIT[paper]
 if paper=='II':
  d=json.loads((ROOT/'audit_sign/frontmatter_II_dependency_edges.json').read_text())
  return [(x['source'],x['target'],x['source_body'],x['target_body'],x['used_conclusion']) for x in d['verified_edges']]
 d=json.loads((ROOT/'audit_corrections/IV_dependency_edges.json').read_text())
 pairs=set(map(tuple,d['suggested_transitively_reduced_main_edges']))
 return [(x['from_main'].split(':')[-1],x['to_main'].split(':')[-1],x['supplying_body_label'],x['using_body_label'],x['used_conclusion']) for x in d['edges'] if (x['from_main'].split(':')[-1],x['to_main'].split(':')[-1]) in pairs]

def organization(paper,data):
 edges=records(paper);pairs=list(dict.fromkeys((x[0],x[1]) for x in edges))
 letters=[x['letter'] for x in data['main_theorems']]
 pos={l:((i%3)*3.5,-(i//3)*1.25) for i,l in enumerate(letters)}
 if paper=='IV':pos={'A':(0,0),'B':(-3.6,-1.3),'C':(0,-1.3),'D':(3.6,-1.3),'E':(1.8,-2.6),'F':(5.4,-2.6),'G':(3.6,-3.9)}
 text=r'''\subsection{How the paper is organized}
The body gives the marked constructions, their integral and holomorphic
comparison maps, and the consequences grouped in Theorems '''+', '.join(letters[:-1])+' and '+letters[-1]+r'''.
The final part states each remaining question with its established
reduction. In the diagram an arrow records reuse of the particular
body argument identified below; a theorem group can contain several
arguments with different inputs. The statement headers give the full
local uses and the links to the corresponding outline steps.
\begin{figure}[htbp]\centering
\begin{tikzpicture}[>=stealth,every node/.style={font=\small}]
'''
 for l in letters:
  x,y=pos[l];text+=f'\\node[draw,rounded corners,minimum width=2.2cm,minimum height=.65cm] (T{l}) at ({x},{y}) {{\\hyperlink{{main-{paper}-{l}}}{{Theorem {l}}}}};\n'
 for a,b in pairs:
  style='bend left=18,' if paper=='I' and (a,b) in [('B','G'),('G','A')] else ''
  text+=f'\\draw[->,{style}semithick] (T{a}) to (T{b});\n'
 text+=r'''\end{tikzpicture}
\caption{Reuse of the indicated body arguments among the main theorem groups.}
\par\medskip
\begingroup\small
\begin{tabularx}{\textwidth}{@{}p{.10\textwidth}X@{}}
\toprule Arrow & Supplying and receiving arguments\\\midrule
'''
 seen=set()
 for a,b,s,t,reason in edges:
  if (a,b) in seen:continue
  seen.add((a,b))
  if paper=='IV':
   reason={('A','B'):r'The physical formula $A_M=d/2-1$ and the oriented gluing map give the primitive return.',
    ('A','C'):'The physical Hopf transfer converts the actual cover characteristic pair to the one-loop integer.',
    ('A','D'):'The physical normal-line comparison is composed with the displayed positive-cap spinor map.',
    ('D','E'):'The retained good-root and annular maps enter the source-line suspension.',
    ('D','F'):'The reference orbit and finite-cap comparisons retain the root characters in the infinity construction.',
    ('E','G'):'The translation, inverse-chord and identity-component maps give the analytic cap coefficients.',
    ('F','G'):'The full signed meridian arrows retain the ordinary generators and determinant sign.'}[(a,b)]
  text+=f'${a}\\to {b}$ & \\SeriesRef{{{s}}} $\\longrightarrow$ \\SeriesRef{{{t}}}. '+reason+r'\\'+'\n'
 text+=r'\bottomrule\end{tabularx}\endgroup\end{figure}'+'\n'
 (ROOT/f'analysis/dependency_figure_{paper}.json').write_text(json.dumps({'paper':paper,'arrows':[dict(source=a,target=b,supplying_body=s,receiving_body=t,used_conclusion=q) for a,b,s,t,q in edges],'scope':'Concrete reuse of the identified body arguments; no independence assertion for omitted arrows.'},indent=2))
 return text
