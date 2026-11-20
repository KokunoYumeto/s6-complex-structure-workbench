"""Guarded relocation of the unreconstructed original K111 numerical atlas.

Writes only audit_sign. Every removed mathematical excerpt is retained
verbatim in the final-part alternative, and all original formula tags
must occur exactly as often across the two receiving files.
"""
from pathlib import Path
import re,json,hashlib,collections
root=Path(__file__).resolve().parents[1]
srcpath=root.parent.parent/'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_IV.tex'
src=srcpath.read_text();a=src.index(r'\label{night:P3K.111}');p=src.index(r'\begin{proof}',a);z=src.index(r'\subsection{The complete selected-I3 M2 return',p)
oldproof=src[p:z];end=oldproof.rfind(r'\end{proof}');inner=oldproof[oldproof.index('\n')+1:end]
rx=re.compile(r'\\par\\bigskip\\noindent\\textbf\{P3K\.111 supporting proof (\d+):[^\n]*')
heads=list(rx.finditer(inner));assert len(heads)==19
blocks={int(h.group(1)):inner[h.start():(heads[i+1].start() if i+1<len(heads) else len(inner))] for i,h in enumerate(heads)}
oldintro=inner[:heads[0].start()];archive=[];ops=[]
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
def record(n,title,old,new):
 archive.append((n,title,old));ops.append(dict(support=n,location=title,old_text=old,new_text=new,expected_count=1,old_sha256=sha(old),reason='Relocate original execution-specific construction and preserve its exact mathematics; active proof uses the newly supplied full atlas.'))
def swap(n,old,new,title):
 assert blocks[n].count(old)==1,(n,title,blocks[n].count(old));record(n,title,old,new);blocks[n]=blocks[n].replace(old,new,1)
def cut(n,start,stop,new,title):
 i=blocks[n].index(start);j=blocks[n].index(stop,i);swap(n,blocks[n][i:j],new,title)
record(0,'original assembly introduction',oldintro,'See new active introduction.')
for n in range(4,12):record(n,'complete original auxiliary support '+str(n),blocks[n],'');blocks[n]=''

swap(2,'E81 and the locked common/end atlases I2F and its actual endpoint parents and lifts. It establishes',
'E81 and the complete new common/end atlases of supporting proof 20. It establishes','I2P actual atlas input')
cut(2,'On a common/end chart all x,y,P,R are the explicit monomials and',
'The source translation, full coefficient, point graph and inverse',
'''On each localized exterior chart and on the thirty-six lower-source
charts used below, x,y,P,R are the full monomials and units of SI2.6
and I2M.  The exact cone inequalities and chart substitutions in
supporting proof 20 C give morphisms to I2P.1 and its resolution,
together with the complete line coefficients above.  The other
common/end interior charts form the independently constructed
regular toric filling; no additional graph blowup is inserted there.
The full I2P.8--9 maps carry every translated graph owner on the
regions where the exterior and lower-source comparisons use that
graph.  The complete boundary assembly is supplied in supporting
proof 20 F.

''','I2P exact exterior and lower-source graph scope')
swap(3,'arrows of I2I.1. For the translate',
'arrows of SI2.47. For the translate','I2M retained infinity period locator')

swap(13,'This proof uses the executed zero endpoint and its actual common lift,','This proof uses the new zero endpoint and its actual common lift in supporting proof 20,','native-star input scope')
cut(13,'They are the unchanged lower facets of the 420-chart source-compatible','The actual physical vector is',
'''They are exactly the pure-lower facets of the new 54,121-chart zero
endpoint.  Its entire P-invertible subfan is unchanged from the original
raw model.  The complete physical face extraction has thirty-one charts
in the single orbit represented by these two normal faces.  Supporting
proof 20 and its same-atlas certificate retain every original ray,
source band, normal character, canonical order and full period unit.

''','old zero atlas and eleven-chart extraction')
swap(13,'For every one of the eleven resolved moving-star charts, the\ncompanion exports the actual parent matrix and its inverse. Align',
'For each of the thirty-one new resolved moving-star charts, the\ncomplete certificate exports the actual matrix and its inverse. Align','native normal derivative chart count')
cut(13,'The quotient tangent rays of the eleven charts, in the aligned','\\par\n\n\\medskip\\noindent\\textbf{NS.4.',
'''The new quotient source fan and all thirty-one native normal charts
are the complete ones in supporting proof 20 E.  Its thirty compact
rays and two horizontal rays cover the marked half-plane once.  The
twenty-nine recorded ordinary sum-of-neighbor blowdowns, with their
reciprocal source and normal maps, end at the same original three-ray
fan of the native sphere times its P disc.

''','old eleven-chart source fan and nine blowdowns')

swap(14,'This construction uses the eleven actual native-star charts NS.1-\\/-6,','This construction uses the thirty-one actual native-star charts of supporting proof 20 and the protected native maps NS.1-\\/-6,','NC source-chart input')
swap(14,'On each of the eleven actual resolved moving-star charts let','On each of the thirty-one actual new resolved moving-star charts let','NC derivative chart count')
swap(14,'actual nine-fold blowup of \\(\\mathbb P^1_Z\\times \\mathbb P^1_{\\rm parameter}\\) given by the\nNS.23b fan and its recorded chronological coordinate blowup maps.\nAll nine centres lie in the original P disc.',
'actual twenty-nine-fold blowup of \\(\\mathbb P^1_Z\\times \\mathbb P^1_{\\rm parameter}\\) given by the\nnew source fan and its recorded chronological coordinate blowup maps in supporting proof 20.\nAll twenty-nine centres lie in the original P disc.','NC closed replacement source blowups')
swap(14,'among those units; their divisor orders stay in the eleven-chart\ncalculation.','among those units; their divisor orders stay in the thirty-one-chart\ncalculation of supporting proof 20.','NC unit/divisor scope')

mn3='\\medskip\\noindent\\textbf{MN.3. The actual RB moving reference and its own cap}'
i=blocks[15].index(mn3);old=blocks[15][:i];record(15,'original collision MN.1--2 and eleven-chart subtotal',old,'Retain MN.3--4 and use new collision computation in proof 20.')
blocks[15]=r'\par\bigskip\noindent\textbf{P3K.111 supporting proof 15: The actual fixed-source reference and ordered native bases}\par\nobreak'+'\n\n'+blocks[15][i:]
cut(15,'The finite whole-pair continuation can use the exact q-preserving','% End expanded verified cp36 input',
'''The full RFB source, Cox, line, reference and cap continuation below
compares the actual complete references in their specified native fans.
The collision own-cap bundle used in the present assembly is the new
thirty-one-chart bundle computed in supporting proof 20 E; MN.14 is
its unchanged fixed-source own reference.

''','MN old collision-subtotal cross-reference')
swap(15,'MN.2, and their remaining local factors are nonzero.',
'NS.17, and their remaining local factors are nonzero.','MN retained actual-frame locator')

cut(16,'The twelve surfaces here are the actual \\texttt{lower\\_source\\_boundary} face',
'\\par\n\n\\medskip\\noindent\\textbf{IL.1.',
'''The twelve surfaces used here are the complete minimal three-chart
lower source stars of the new one endpoint in supporting proof 20.
They are closed against the actual twelve RB scalar-source pieces by
the full source, line, cube-frame and cap maps retained below.  Their
normal pairings and physical pair are evaluated in supporting proof 20 E.

''','old IL.1 numerical declaration')
swap(16,'\\((0,1)\\) and \\((1,0)\\). These rows are retained for all 3,888 charts.',
'\\((0,1)\\) and \\((1,0)\\). These rows are retained on all thirty-six new lower charts.','IL normal row execution scope')
cut(16,'\\medskip\\noindent\\textbf{IL.2. All source charts, normal walls and ordinary blowdowns}',
'\\medskip\\noindent\\textbf{IL.4. Exact point/O and source maps to the fixed reference}',
'''The new lower stars have the complete minimal source cycle, with
normal degree vectors \\((-1,0,1)\\) and \\((-1,1,0)\\).
On the marked two-component relative basis set
\\[
 I=\\begin{pmatrix}-2&1\\\\1&-2\\end{pmatrix}.
\\]
The actual relative lifts are \\(I^{-1}(0,1)^t\\) and
\\(I^{-1}(1,0)^t\\), giving the pairings
\\((-2/3,-1/3,-2/3)\\).  All three original source charts, their
full period closure and normal rows are in the new certificate.
The following source and frame morphisms are retained in full.

''','old IL.2--3 ordered array, 321 blowdowns and collision subtotal')
cut(16,'Glui' if False else 'Gluing through\nIL.30, using the cube connections and the retained fibre',
'On the fixed surface \\(s=A_lB_l=0\\),',
'''Gluing through IL.30, using the same cube connections and retained
fibre gauges, subtracts the reference pairings IL.37 from the minimal
collision pairings above.  The resulting closed normal pairings are
\\((0,-1,0)\\).  The entire minimal collision source is carried to
the reference body by the displayed source flow; its derivative and
inverse match the boundary tangent connections.  The identical
opposite-collar interpolation cancels, and the tangent Pontryagin
pairing of these new minimal doubles is zero.  No source blowup is
inserted into these lower stars.

''','old IL.39--40 closed numerical pairings and tangent subtotal')
swap(16,'the complex fixed-surface orientation already used in\nIL.10--40.','the original complex fixed-surface orientation and the complete\nsource, normal and cap maps just displayed.','IL residue orientation reference')
cut(16,'Substitution of the three complete normal pairings and',
'The whole scalar-reference fan comparison RFB changes',
'''For the new minimal doubles the complete pairings are
\\((0,-1,0)\\) and the tangent pairing is zero.  The displayed
physical Euler expansion therefore gives \\((1,-2)\\) for each of the
twelve actual labels, as verified in supporting proof 20.

''','old IL.42 lower totals and absent execution provenance')
swap(16,'by \\((-72,0)\\). IL.1 uses the actual RB \\(T_1\\)\nreference pieces and its own cap maps.','by \\((-72,0)\\). The new lower computation uses the actual RB \\(T_1\\)\nreference pieces and their own cap maps.','IL final reference scope')

cut(19,'Take precisely the executed common I2F fan and its proper zero,','The actual base maps are',
'''Use the complete new common fan and its zero, one and infinity
endpoints constructed in supporting proof 20.  Their common boundary
has 1,926 primitive regular three-cones.  The endpoint counts are
54,121, 2,022 and 2,381.  The complete original-lattice semigroup maps,
full character inverses, paired period facets and source cuts are all
retained in that construction and its exact certificates.  Each
subdivision is proper over the same original convex raw cells.
''','ASI2 old common and endpoint execution input')
cut(19,'The fixed-face inventory examines every regular','From the actual physical Euler denominator,',
'''The complete new fixed-face inventory and its exact ownership are
those of supporting proof 20 D.  It contains 35,908 compact physical
components, the twelve complete lower source owners and the single
zero moving owner.  Every endpoint chart belongs to exactly one
generic, compact-corner or separately capped piece.  The actual
physical face and period maps, all finite slice weights and the
same-atlas SHA certificate are retained.

The compact physical pair is \\((895,139)\\); the twelve lower
pairs sum to \\((12,-24)\\).  For the new moving surface the
full NC.19--20 bordism carries its actual cap to the closed
replacement with roots \\(x=h+D_-\\), \\(y=-h-D_+\\).
The thirty-one-chart derivative, complete divisor matrix and all
twenty-nine chronological source blowups give
\\(c_1(E)^2=-1200\\), \\(c_2(E)=-294\\), \\(p_1(TF)=-87\\).
The original RB reference roots remain \\(h-12u,-h-12u\\),
and its own cap still has \\(c_1^2=c_2=p_1=0\\).
''','ASI2 old fixed inventory and moving collision roots')
cut(19,'Hence the moving collision-minus-',
'\\par\n\n\\medskip\\noindent\\textbf{ASI2.5.',
'''Hence the actual new moving-minus-own-reference pair is
\\((-906,-111)\\).  The complete new inner ledger with the same
RB \\(T_1\\) reference is
\\[
 (895,139)+(12,-24)+(-906,-111)=(1,4).
\\]
This uses the new collision atlas for every collision contribution
and includes the actual original fixed-source reference exactly once.

''','ASI2 old moving pair and old inner ledger')
swap(19,'finite covering factor in CFL and IL.','finite covering factor in the new complete fixed-face certificate and IL.','ASI2 finite slice scope')
swap(19,'fixed-surface orientations used in CFL, IL and\nMN.','fixed-surface orientations used in supporting proof 20, IL and\nthe retained native/cap maps.','ASI2 orientation scope')
patches=json.loads((root.parent/'audit_corrections/K111_inherited_scope_patch_05.json').read_text())
for x in patches:
 old=x['old_text'].replace('\\\\','\\');new=x['new_text'].replace('\\\\','\\')
 # The JSON contains literal LaTeX, already decoded by json.loads.
 if blocks[19].count(x['old_text'])==1:old=x['old_text'];new=x['new_text']
 assert blocks[19].count(old)==1,'exact receiving inherited-source guard'
 record(19,'ASI2.7 exact inherited-map clarification',old,new);blocks[19]=blocks[19].replace(old,new,1)

intro=r'''\noindent\textbf{Original source, complete new filling and directed physical transfer.}\par\smallskip
The source, full Miller and theta coefficients, point/O modules and
period dictionary are the retained SI2, I2P and I2M maps below.  Supporting
proof 20 constructs a complete auxiliary atlas directly from their
original convex period cells.  Its 1,926-cone common fan and all three
endpoint atlases retain the entire original source, physical circle,
period functions, selected native star, scalar root and outer marking.

RB retains the whole fixed-source scalar reference.  NS and NC give
the actual protected native maps and the directed Hopf cap with its
full normal derivative.  The retained MN reference and IL source,
Cartier, cube-frame and cap maps are used with the new moving and
minimal lower stars.  RFB carries the entire reference fan change;
ASI2 retains compactness, the original finite-cap square, the exterior
cylinder, all four parameter edges and the physical inverse clutch.

The complete new compact pair is $(895,139)$, the twelve lower doubles
sum to $(12,-24)$, and the actual moving-minus-own-reference pair is
$(-906,-111)$.  Their sum is $(1,4)$.  The entire positive reference
change is $(72,0)$, and the explicit Jin interval reversal gives
$(71,-4)$.  The unchanged physical line and held quaternion give
$(\mu,\nu)=(-1,72)$ and the original oriented sphere class $12$.

The earlier auxiliary execution is retained separately in
\cref{iv:open:K111:original_auxiliary_arrays}, with its missing ordered
arrays and replay requirement stated there.  The construction and
numerical parts used here are exactly the new complete atlas and the
retained original geometric maps.

'''
new20=(root/'K111_new_auxiliary_proof.tex').read_text()
active='\\begin{proof}\n'+intro+''.join(blocks[n] for n in range(1,20))+new20+'\n\\end{proof}\n'
final=r'''\begin{problem}[Original selected-I3 auxiliary-array reconstruction]
\label{iv:open:K111:original_auxiliary_arrays}
\StatementRecord{iv:open:K111:original_auxiliary_arrays}{open}{}{the original common and endpoint arrays, ordered lower source chains, period maps, normal bundles and caps reproduced below; \cref{night:P3K.111} and its complete new auxiliary construction}
Reconstruct the originally reported 136,442-cone common atlas, its
three complete endpoint arrays and the ordered 324-chart lower source
chains, retaining all original period words, point/O modules, normal
derivatives and boundary caps.  The complete original files and their
ordered execution histories were not present in the supplied source.
The following preserved alternate construction therefore remains
unestablished at that exact numerical scope.  Its reported compact
pair $(2723,19124)$, lower total $(-2712,-19092)$ and nine-blowup
moving subtotal are not used in the proved construction of
\cref{night:P3K.111}.  That theorem uses the complete new atlas and
the actual source/exterior/cap maps of its supporting proof 20.

The required reconstruction includes the immutable zero upper
triangulation and the original ordered common-edge chain: the printed
support and band restrictions admit the explicitly exhibited diagonal
flip and do not determine those arrays.  Replaying them must recover
the whole fixed-owner partition and every original curve, surface,
point, normal and relative tangent contribution.  Each text below is
preserved with its original formula tags, at this stated unestablished
alternate-construction scope.
\end{problem}

'''
for n,title,text in archive:
 final+='\n\\par\\bigskip\\noindent\\textbf{Preserved alternate construction: '+title.replace('&',r'\&')+'}\\par\n'
 final+=text+'\n'
tags=lambda s:collections.Counter(re.findall(r'\\(?:tag|label)\{([^{}]*)\}',s))
oldtags=tags(oldproof);newtags=tags(active+final);newtags.pop('iv:open:K111:original_auxiliary_arrays',None)
assert oldtags==newtags,dict(missing=oldtags-newtags,extra=newtags-oldtags)
for obsolete in ['136,442','143,270','149,774','2723','19124','2712','19092','3,888','324 source charts','321 rays','eleven actual','actual nine-fold blowup']:
 assert obsolete not in active,obsolete
(root/'K111_active_proof_replacement.tex').write_text(active)
(root/'K111_final_alternate_construction.tex').write_text(final)
manifest=dict(statement='night:P3K.111',source=str(srcpath),source_sha256=hashlib.sha256(srcpath.read_bytes()).hexdigest(),original_proof_sha256=sha(oldproof),active_file='K111_active_proof_replacement.tex',active_sha256=sha(active),final_file='K111_final_alternate_construction.tex',final_sha256=sha(final),guards=ops,original_formula_tag_count=sum(oldtags.values()),preserved_formula_tag_count=sum(newtags.values()),retained_supports=[n for n in blocks if blocks[n]],relocated_supports=list(range(4,12)),integration_recipe=['Locate night:P3K.111 and replace only its whole outer proof environment by active_file after checking the original source proof SHA or exact ordered original tag list.','Insert final_file exactly once in the final open/problem part. Do not copy the moved excerpts elsewhere; their original formula tags are preserved there.','The corrections inherited-scope patch has already been applied inside active_file; do not apply it twice.','Retain theorem statement and its source/line/scalar/fan hypotheses; update confidence from the independently received new-atlas proof.','Rebuild hierarchical proof rendering and resolve all actual labels; then visually inspect the new proof20 and final alternate-record boundary.'],scope='No shared paper source changed. All removed original mathematical text and all original formula tags are preserved across active and final receiving blocks.')
(root/'K111_guarded_integration.json').write_text(json.dumps(manifest,indent=2)+'\n')
(root/'K111_final_alternate_inventory.json').write_text(json.dumps({'label':'iv:open:K111:original_auxiliary_arrays','placement':'final open/problem part','status':'open','confidence_state':'unestablished original alternate numerical construction; exact arrays absent','confidence_line':'Every relocated original formula and map is retained. The absent immutable upper array, full original common/endpoint arrays and ordered324-chart source chains prevent a complete fresh replay of the originally reported subtotals. A separate complete new atlas now proves K111.','remaining_risk':'Reconstruct exact ordered original arrays, original fixed-owner partition and every full normal/tangent/cap contribution before assigning the old numerical execution fresh proof credit.','inventory_reason':'Preserves the original alternate construction without presenting its unavailable execution under the proved new K111 argument.'},indent=2)+'\n')
print(json.dumps({'active_lines':active.count('\n'),'final_lines':final.count('\n'),'guards':len(ops),'formula_tags_preserved':sum(oldtags.values()),'active_sha256':sha(active),'final_sha256':sha(final)},indent=2))
