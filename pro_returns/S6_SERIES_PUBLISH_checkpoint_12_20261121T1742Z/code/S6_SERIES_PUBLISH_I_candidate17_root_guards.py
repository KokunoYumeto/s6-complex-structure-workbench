#!/usr/bin/env python3
"""Archive exact root candidate17 repairs after full page/context/proof reading."""
from pathlib import Path
import hashlib,json,re,datetime
R=Path(__file__).resolve().parents[1]; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=R/'S6_SERIES_PUBLISH_I.tex'; expected='5b74359a048b1eab3e478a65eab35f35b45474c4c65aadaedd639315c19a9379'; assert sha(p)==expected
s=p.read_text()
items=[
(1,138,'D23',r'of the canonical evaluation in \cref{fam:src:A.1.1}, gives',r'of the canonical evaluation in \cref{fam:src:A.1.1} gives','Remove the comma separating the exact subject from its verb; preserve the numbered input and every canonical-bundle formula.'),
(2,140,'D08','We give the full limiting-group argument in \\ref{push:src:D.3.1}; its formula also\napplies to the fixed boundary family with \\(c=c_*\\), \\(h\\ne0\\).','The limiting-group formula in \\ref{push:src:D.3.1} also\napplies to the fixed boundary family with \\(c=c_*\\), \\(h\\ne0\\).','Replace the announcement by the same cited formula application on the exact fixed-family domain. The ray, dual covector, annihilator limits and quotient proof remain.'),
(3,143,'D02','; no nonclosed group is used as a Chabauty\npoint.','.','The preceding positive application already states the real vector space and closed full lattices. Remove its repeated defensive tail; retain the cited annihilator homeomorphism and all hypotheses and maps.'),
(4,198,'D08','We identify each surface explicitly.  ','','Remove the empty introduction to the exact scalar Hopf surface identifications; the lattice basis, homomorphism, cyclic kernel and product comparison remain.'),
(4,199,'D08','Here are the integral topology maps.  ','','Remove the empty introduction while retaining the full Hopf diffeomorphism, integral inclusion matrices, pushout and homology exact sequence.'),
(4,199,'D08','For completeness, the two scalar Hopf surfaces','The two scalar Hopf surfaces','Remove the completeness qualifier while preserving the full nonisomorphism and nonbimeromorphism argument and external credit.'),
(5,208,'D08','We first identify the analytic neighbourhood.  ','','Remove the empty introduction to the exact Kato gluing and cone-neighbourhood construction.'),
(5,209,'D08','For completeness, a holomorphic one-form','A holomorphic one-form','Remove the completeness qualifier; retain the entire Stokes/de Rham argument proving the needed vanishing.'),
(5,209,'D08','We compute the one possible local higher direct image explicitly.\n','','Remove the empty calculation announcement; retain the Atiyah extension, its Chern class, formal-functions theorem and explicit direct-image isomorphism.'),
(7,224,'D08','We describe the root-cover model to verify the finite\naction and properness. In cocharacter coordinates\n$(y_1,y_2,h_z,h_r)$, its two period shears are','In the root-cover model, the two period shears in cocharacter coordinates\n$(y_1,y_2,h_z,h_r)$ are','State the same root-cover shears directly. Preserve the root-cover input, four coordinates, finite deck, unit factors, invariant fan and properness proof.'),
(8,241,'D08','We first prove the finite-multisection consequence of\nthe log-torsor obstruction of Proposition~\\ref{push:src:B.4.24}.\nMake the normalized finite base change $q=Q^{12}$.','Use the log-torsor obstruction of Proposition~\\ref{push:src:B.4.24}\nafter the normalized finite base change $q=Q^{12}$.','Replace the roadmap by the concrete cited obstruction and unchanged exact base change. Every finite multisection hypothesis, trace/norm calculation and dimension argument remains in the complete proof.'),
(8,241,'D08','We show that they\nextend as log-torus sections on $B_q$ and $B_r$.','They extend as log-torus sections on $B_q$ and $B_r$.','State the same extension claim positively; its full ramification, norm, overlap and period proof is unchanged.'),
(9,255,'D08','We construct the comparison at every point. ','','Remove the empty introduction; retain every ordinary, finite-root and cusp comparison map and the connecting-map argument.'),
(10,258,'D08','We first establish the required section algebra for every integer\npower of $\\mathcal L$. If a meromorphic function represents a section\nof $\\OO(aS_1+bS_2)$, it is holomorphic','For every integer\npower of $\\mathcal L$, a meromorphic function representing a section\nof $\\OO(aS_1+bS_2)$ is holomorphic','Integrate the existing integer-power scope into the positive section statement. The meromorphic-function set, valuation inequalities, pushforward identity and graded multiplication remain identical.'),
(11,259,'D08','We first derive the fundamental-group presentation from the fillings.\n','','Remove the empty announcement; retain the exact affine-generator powers, cusp meridian, van Kampen presentation, Smith matrix and connected-cover maps.'),
(12,294,'D08','We make the period identification explicit. ','','Remove the empty announcement; retain the sigma expression, third-kind differential, extension cocycle/exponential, sign and all relative periods.'),
(13,322,'D08','We must determine its connecting map when $k>1$.\nThe dual logarithmic sequence','For $k>1$, the dual logarithmic sequence','Keep the exact k>1 scope as the input to the same dual logarithmic sequence. The connecting map is identified by the unchanged Serre-dual residue calculation immediately below.'),
(14,326,'D08','We compute all components of the translation group.  ','','Remove the empty announcement; retain the complete translation sheaf, exponential sequence, cusp/finite lattice extension and full group calculation.'),
(15,245,'D08',' We spell out the\nconsequences for the reduced anticanonical pairs here.','','Remove the empty announcement after the exact minimal-model alternatives. All rational/ruled/class-VII pair arguments and their source locators remain.'),
(15,247,'D08','Here is the exact marking needed. ','','Remove the empty announcement; retain the complete Oda locator, unit-action matrix, mapping torus, Clifford-torus marking and all transport maps.'),
(16,226,'D08','For clarity, on the unfolded node chart write','On the unfolded node chart write','Remove the clarity qualifier; retain the exact node coordinates, chart-index shift and plumbing automorphisms.'),
(16,227,'D08','For completeness the branch identities are','The branch identities are','Remove the completeness qualifier; retain the full branch identities, deck contribution and descent proof.'),
(17,254,'D08','For completeness, the connecting map is','The connecting map is','Remove the completeness qualifier; retain the endpoint-period definition, finite-root summation formula, normalized class and all transport identities.'),
]
blocks={}; guards=[]
for n,page,typ,before,after,reason in items:
 original=R/f'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_review_block_{n:02}_original.tex'
 block=original.read_text();assert s.count(block)==1;assert block.count(before)==1;assert s.count(before)==1,(n,before)
 blocks[n]=block
for n,block in blocks.items():
 proposed=block
 for k,_,_,before,after,_ in items:
  if k==n:proposed=proposed.replace(before,after,1)
 math=r'(?<!\\)\$.*?(?<!\\)\$|\\\[.*?\\\]|\\\(.*?\\\)'
 assert re.findall(math,block,re.S)==re.findall(math,proposed,re.S),n
 assert re.findall(r'\\[A-Za-z@]+',block)==re.findall(r'\\[A-Za-z@]+',proposed),n
 assert re.findall(r'\\(?:label|hypertarget|ref|cref|eqref|cite[a-z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}',block)==re.findall(r'\\(?:label|hypertarget|ref|cref|eqref|cite[a-z]*)\*?(?:\[[^\]]*\])*\{[^}]*\}',proposed),n
 a=block.index('\\end{',block.index('\\StatementRecord'))
 # All these changes occur in the proof, strictly after the complete statement.
 proof=block.index('\\begin{proof}')
 assert block[:proof]==proposed[:proof]
 out=R/f'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_review_block_{n:02}_proposed.tex';assert not out.exists();out.write_text(proposed)
for k,(n,page,typ,before,after,reason) in enumerate(items,1):
 original=R/f'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_review_block_{n:02}_original.tex';proposed=original.with_name(original.name.replace('_original.tex','_proposed.tex'))
 block=original.read_text();label=re.findall(r'\\label\{([^}]+)\}',block)[0]
 guards.append({'id':f'I17-root-{k:02}','type':typ,'page':page,'statement_id':label,'before':before,'after':after,'reason':reason,'source_line':s.count('\n',0,s.index(before))+1,'source_sha256':expected,'pdf_sha256':sha(R/'build/I_candidate17/S6_SERIES_PUBLISH_I.pdf'),'original_full_block':str(original.relative_to(R)),'original_full_block_sha256':sha(original),'proposed_full_block':str(proposed.relative_to(R)),'proposed_full_block_sha256':sha(proposed),'full_block_contains_all_root_changes_for_this_block':True,'all_mathematical_segments_and_commands_identical':True,'statement_byte_identical':True,'root_review':'Root actually read the complete current owning statement and proof, the assigned whole pages or exact printed context, and the literal proposed maps. Mathematical data are carried by the identity on all inline/display segments and unchanged control/reference sequences; all remaining source bytes outside the recorded replacements are retained.','status':'approved by root, awaiting combined guarded application','mathematical_events_added':0})
out=R/'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate17_root_guards.json';assert not out.exists();out.write_text(json.dumps(guards,indent=2)+'\n');assert sha(p)==expected
print(json.dumps({'guards':len(guards),'full_blocks':len(blocks),'path':str(out.relative_to(R)),'sha256':sha(out),'source_unchanged':True}))
