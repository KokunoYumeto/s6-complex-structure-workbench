"""Prepare the renewed full-proof comparison edits for UN4 and INT2."""
from pathlib import Path
import datetime, hashlib, json
R=Path(__file__).resolve().parents[1]
O=R/'records/S6_SERIES_PUBLISH_II_root_recovery_edits_01'
source=(R/'S6_SERIES_PUBLISH_II.tex').read_text()
sha=lambda b:hashlib.sha256(b).hexdigest()
patches=[]
blocks={name:(O/(name+'_before.tex')).read_text() for name in ['INT2','UN4']}
owners={'INT2':'cdp:st:C.2.INT.2','UN4':'cdp:st:C.2.UN.4'}
def change(name,old,new,kind,reason):
 global source
 assert old!=new and blocks[name].count(old)==1,(name,old)
 assert source.count(old)==1,(name,source.count(old),old)
 patches.append(dict(old=old,new=new,type=kind,statement_id=owners[name],reason=reason))
 blocks[name]=blocks[name].replace(old,new,1)
 source=source.replace(old,new,1)
change('INT2','[Proved exclusion of Enoki components]','[Exclusion of Enoki components]','D16','The mathematical title states the exclusion; the status word is removed.')
change('INT2',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'+'\n'+r'\item Write the full fibre',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'+'\n'+r'\item Write the full fibre','D04','Remove the internal iteration marker. The eight proof steps and their order are unchanged.')
change('INT2','\\item We retain the geometric information in the actual\nblowups and normalization maps. Every topologically','\\item Every topologically','D08','Remove the production announcement; the integral Picard blowup formula and the exact conductor transformation follow immediately.')
change('INT2','intersection. Here is the needed resolution\ncomparison at possible exceptional points. Any','intersection. Any','D08','The resolution comparison is given by the immediately following adjunction calculation; the announcement is omitted.')
change('INT2','The colength-one ring comparison (C.VII.6)','The colength-one ring comparison \\eqref{cdp:eq:C.VII.6}','D06','The inherited display number is replaced by the exact existing equation label; its node-ring comparison is unchanged.')
change('INT2','by an actual biholomorphic change of variables.','by a biholomorphic change of variables.','D08','The explicit map Phi and invertible derivative prove the stated coordinate equivalence; the process modifier adds no hypothesis.')
change('INT2','of the actual local fibres.','of the local fibres.','D08','The exact equality f0 composed with Phi equals u f0 identifies these fibres; wording only.')
change('INT2','of the actual smooth fibre is','of the smooth fibre is','D08','The same smooth fibre and its explicit local equation remain.')
change('UN4','All the original positive full-fibre multiplicities are retained on\ntheir strict transforms. The construction requires no normal crossings\ncondition on the original support.','The positive full-fibre multiplicities are unchanged on\ntheir strict transforms.','D08','The proposition already quantifies over every reduced support of the stated smooth-ambient map, without a normal-crossings hypothesis. The proof keeps all blowup charts and the full inverse-image comparison.')
change('UN4',r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]'+'\n'+r'\item We first specify the comparison for a blowup whose centre meets'+'\n'+'singularities of the support. Let',r'\begin{enumerate}[label=\arabic*.,leftmargin=*]'+'\n'+r'\item Let','D04','Remove the internal iteration marker and proof announcement; the same arbitrary smooth centre and all eight steps remain.')
change('UN4','The equality of underlying sets is $S\'=\\pi_Z^{-1}(S)$, and the actual\nrestrictions of the blowup give','The equality of underlying sets is $S\'=\\pi_Z^{-1}(S)$, and the\nrestrictions of the blowup give','D08','The exact restriction isomorphism and exceptional projective bundle remain displayed.')
change('UN4','Thus \\eqref{cdp:eq:C.VR.4} retains any intersections of the centre with other\ncomponents or with the singular support. It makes no replacement of\nthe full inverse image by a strict transform.','Equation \\eqref{cdp:eq:C.VR.4} applies to the full inverse image, including\nintersections of the centre with other components and the singular support.','D02','State positively the scope already proved by the equality S prime equals the full inverse image, without the defensive alternative.')
change('UN4','In the chart $y=r$, $x=ru$, $z=rv$, the actual map is','In the chart $y=r$, $x=ru$, $z=rv$, the map is','D08','The displayed blowdown coordinate substitution is unchanged.')
change('UN4','For clarity, the four points of $C\\cap L$ introduce no singularities\nof the ambient space and do not alter this Euler comparison. Near any','The ambient blowup is smooth at the four points of $C\\cap L$. Near any','D02','The following two explicit coordinate charts prove smoothness and preserve the Euler calculation already established for the full inverse image.')
change('UN4','are simply retained.','are unchanged.','D08','The preceding restriction isomorphisms identify all other points exactly.')
change('UN4',r'\item We include the integral cohomology comparison giving \eqref{cdp:eq:C.VR.2}.'+'\n'+'For a smooth centre',r'\item For a smooth centre','D08','The complete integral cohomology homomorphism and proof remain; remove its introductory announcement.')
change('UN4','The actual blowup homomorphism is','The blowup homomorphism is','D08','The explicit pullback and Gysin homomorphism is unchanged.')
change('UN4',r'\item Finally \ref{cdp:st:C.2.UN.1} writes',r'\item Proposition~\ref{cdp:st:C.2.UN.1} gives','D08','Use the numbered mathematical input directly.')
change('UN4','fresh smooth point of a single component exists','smooth point of a single component exists','D08','Each successive support still has a dense smooth locus in every component; the quantified choice is unchanged.')
change('UN4','proves the asserted cofinality with its specified domination maps.','proves cofinality with the displayed domination maps.','D08','The domination maps are the explicit compositions of blowdowns already constructed.')
change('UN4','with one of the two-step decreasing operations, at fresh smooth\npoints.','with one of the two-step decreasing operations, at smooth\npoints.','D08','The same successive choices and Euler increments remain.')
change('UN4','actual maps remain the successive blowdowns already described.\nThe exact chart, quartic, Euler, and cohomology calculations are\nretained in \\path{code/E_vertical_refinements.py} and its output.','maps are the successive blowdowns.','D09','The universal chart, quartic, Euler and integral cohomology derivations remain in the proof. The pinned program citation is moved to the sole end Programs table; finite sample checks do not replace those derivations.')
for name,block in blocks.items():
 (O/(name+'_after.tex')).write_text(block)
 assert source.count(block)==1
anchor='\\end{longtable}}\n\n\\begin{thebibliography}{99}'
assert source.count(anchor)==1
entry='Euler and integral cohomology of vertical point and curve blowups (\\cref{cdp:st:C.2.UN.4}) & \\href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/\\SsixRepositoryCommit/pro_returns/S6_03_CDP_checkpoint_13_20261116T0136Z/S6_03_CDP/code/E_vertical_refinements.py}{\\nolinkurl{E_vertical_refinements.py}} \\\\[3pt]\n'
patches.append(dict(old=anchor,new=entry+anchor,type='D09',statement_id='tab:II:programs',reason='One pinned link for the program just removed from the proof. Root read the complete pinned source; its primary download and Git-blob hash are in opened_programs_02.'))
guard={'paper':'II','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_before_sha256':sha((R/'S6_SERIES_PUBLISH_II.tex').read_bytes()),'patches':patches,'recovery_scope':'New literal edits after the workspace reset. The whole original proofs have been reread; proposed proofs still await their actual final reread. No old guard hash or blind derivation is recreated.','visual_reading_credit':0}
(O/'guard.json').write_text(json.dumps(guard,indent=2)+'\n')
print(json.dumps({'guard':str((O/'guard.json').relative_to(R)),'patches':len(patches),'proposed_blocks':{n:sha((O/(n+'_after.tex')).read_bytes()) for n in blocks}},indent=2))
