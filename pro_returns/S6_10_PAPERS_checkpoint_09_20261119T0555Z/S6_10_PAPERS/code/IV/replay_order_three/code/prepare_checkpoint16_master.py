"""Assemble the actual physical-line correction and complete vertical returns."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,shutil
root=Path(__file__).resolve().parents[1]
archive=root/'records/checkpoint16_prior_master51';archive.mkdir(exist_ok=True)
for name in ['S6_06_BLIND_paper.pdf','S6_06_BLIND_paper.log','S6_06_BLIND_paper.aux','S6_06_BLIND_report.md','S6_06_BLIND_results.csv','code/update_report.py']:
 p=root/name;target=archive/name;target.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() and not target.exists():shutil.copy2(p,target)
p=root/'notes/part3.tex';text=p.read_text()
parts=['physical_line_corrigendum','source_shear_euler_cube','shorter_scalar_vertical_fans','physical_return_consequences']
for name in parts:
 path=root/('notes/part3_'+name+'.tex');assert path.is_file(),path
 line='\\input{notes/part3_'+name+'.tex}'
 if line not in text:text+='\n'+line+'\n'
notice=r'''\par\noindent\textbf{Current physical-line convention and correction.}
P3K.68 supplies the actual Hermitian dual, both cap maps and the
first-to-second Hopf-gluing arrows. The physical nonzero-vector line
is \(M\); the outward-meridian-one line is \(U=M^{-1}\).
The actual oriented sphere class is \(A_M=-A_U\pmod{28}\).
P3K.69 proves the corrected reference and source-fan consequences.
Earlier false physical-sign assertions are explicitly labelled
Refuted and retained as historical claims with precise correction
notices. Their source constructions and the separately identified
local Cox, topology and derivative maps retain their stated scope.
The full sign ledger is \path{records/physical_line_correction_scope.json}.
\par\medskip
'''
if notice not in text:text=notice+'\n'+text
p.write_text(text)
state=('INCOMPLETE. K68 proves the exact physical/dual line and Hopf-gluing morphism, including both cap maps and the inverse caused by exchanging gluing pieces. The physical sphere class is A_M=-A_U. K69 proves the corrected consequences; twenty earlier compound sign assertions are explicitly Refuted with their retained local proof scopes. The primitive OS45 reference class is3 and realizes every class by positive covers; its T2 class is2. K64 proves A_n=A_0-J*n(n-1)/2 on every actual canonical physical-vertical-edge scalar fan. K67 proves the same formula for the actual shorter endpoints and all intermediate cover seams; the original coprime family gives -KL*n(n-1). K65 proves OS49 negative-fan classes -3k on the r-loop and -k on the shorter w-loop, with positive-fan class0. The five earlier scalar product/fan claims K17,K25,K29,K31,K34 are Refuted, and nine broader compound all-fan assertions remain Open. K66 completes the source-shear integer calculation: (k_U,ell_U)=(6+18n(n-1),0), (k_M,ell_M)=(-6-18n(n-1),0), physical index -1-3n(n-1), native fixed pair(0,-6-18n(n-1)), V00=18n(n-1), delta0=-12-18n(n-1). K69 retains the actual source first-flop classes21,21,27, and corrects the two mutation sequences to -1-3j(j+1) and -7-24j(j+1), the latter with period7 and range{1,13,17,21}. The full infinity source/cap comparison gives physical returns0 and-1. The actual groupoid and single source-zero native pair leave exactly (k*A_scalar+14e,a+k*A_scalar+14e), e=0 or1, with A_scalar=0 or3p-1. The smallest good pair is(0,1) or(14,15); reduced p=k=1 gives(2,4) or(16,18). The unresolved order-two central attachment, arbitrary nonvertical scalar fans, remaining source-moduli loops, added ordinary OS49 clutches and unmarked endpoint sectors remain under proof. No order-two choice or uncomputed fan class is assigned.')
p=root/'code/update_report.py';s=p.read_text();lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith("'3.1':"):
  lines[i]="'3.1':"+repr(('P3F.3–P3F.15, P3F.22–P3F.24, P3K.5–P3K.9, P3K.67–P3K.69','Proved original reference class0. K68 retains the exact physical/dual line arrow; its sign leaves zero unchanged. K67 proves the original coprime shorter-family vertical-fan class -KL*n(n-1). Broader arbitrary-fan claims remain explicitly withdrawn.'))+','
 if line.startswith("'3.2':"):
  lines[i]="'3.2':"+repr(('P3F.5–P3F.6, P3F.9–P3F.14, P3K.5–P3K.7, P3K.68–P3K.69','Proved actual page and line-square inputs. K68 corrects K6: the meridian-one class restricts to the Hermitian dual of the source line. Its square and the zero reference index are retained.'))+','
 if line.startswith("'3.3':"):
  lines[i]="'3.3':"+repr(('P3F.2–P3F.3, P3K.7–P3K.9, P3K.68–P3K.69','Proved heights, reducible-fibre correction and rotating normal clutch. The displayed descended pair(-1,-4) is the meridian-one U pair; the physical M pair is(1,4). K68 proves the exact circle, orientation and gluing dictionary. The index is zero in both conventions.'))+','
 if line.startswith("'3.4':"):
  lines[i]="'3.4':"+repr(('P3F.1–P3F.56, P3K.5–P3K.69; corrected and reopened scopes identified below',state))+','
s='\n'.join(lines)+'\n'
start="The exact outstanding instances, attempted constructions and failures remain in the part notes, working proofs and code outputs."
a=s.index(start);b=s.index("','','## Reproduction and typesetting'",a)
s=s[:a]+state+" Parts1,2 and the original blind Part5 retain their independently recorded proofs and original hashes. Part4.2 is proved in the requested irreducible or normal-crossing scope; the broader arbitrary non-normal-crossing supplied extension remains undecided. Source and proof correction ledgers preserve every prior assertion and calculation, with exact scope notices. No unknown central class is treated as zero."+s[b:]
# Authoritative comparison overrides are applied after every legacy mapping load.
anchor='def expanded_ids(text):'
overrides="""# The actual Hermitian dual and physical Hopf transfer override historical sign labels.
put('S6_02_PUSH','C.3.10','Original reference-fan physical return0; exact dual-line dictionary in K68.','P3K.7; P3K.68','agrees')
"""
# Retain only verified source IDs; generic proof-based comparison handling below does not invent rows.
# Do not add the optional override until the supplied row identity has been independently inspected.
ast.parse(s);p.write_text(s)
now=datetime.now(timezone.utc).isoformat()
record={'checked_utc':now,'decision':'CONTINUE','reason':'The main monodromy question advanced by a completed actual line/cap/Hopf-transfer correction, complete integer source-shear calculation, corrected OS49 shorter return and actual shorter scalar fan morphisms. Remaining main instances have concrete next constructions.','main_question_progress':['K64 and K67 compute every signed vertical-fan scalar comparison with exact endpoint and all cover seams.','K65 completes the actual OS49 shorter return and identifies the omitted outer normal winding.','K68 proves the physical/dual line and inverse-clutch sign morphism; K69 records its exact consequences and preserves false prior assertions.','K66 completes the source-shear integer Euler cube, both line conventions, full Pontryagin pairing and native fixed-star free pair.'],'other_open_item_progress':['The source-zero order-two ambiguity is now (0,1)/(14,15) in the smallest good case and (2,4)/(16,18) in the smallest reduced case; no choice is assigned.'],'next_main_steps':['Construct the actual source-zero global central attachment and distinguish its two integral possibilities.','Extend the corrected scalar and source comparisons to further nonvertical fans with actual reset maps.','Complete the remaining OS49 ordinary-clutch and endpoint sectors.'],'next_progress_check_due_utc':'2026-11-17T16:49:44+00:00'}
(root/'records/progress_check_16_hours.json').write_text(json.dumps(record,indent=2)+'\n')
print('Assembled K64--69 and current physical-line report; prior master51 preserved.')
