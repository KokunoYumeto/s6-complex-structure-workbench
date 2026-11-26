"""Record root's complete old/receiving comparison of the class-VII consolidation."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
import subprocess
import sys

apply_edit(
 r'''Conductor pole blowups and curve Euler identities (\cref{night:P4.23})''',
 r'''Conductor pole blowups and curve Euler identities (\cref{cdp:st:C.2.VII.1})''',
 'II-C3-CLASS-VII-PROGRAM-LOCATOR',['D22','D24'],'cdp:st:C.2.VII.1; night:P4.23',
 'Programs table','The pole coefficients and boundary Euler identity now have their single full owner in VII.1; retain the program path unchanged.',
 'Complete old and receiving owner, stronger theorem and program-table context read by root; no independent credit.')

entries=[
 ('night:P4.23','II-C3-ROOT-CLASS-VII-BOUNDARY-UNIT-READ',
  'The original complete VII.1/P4.23 unit and the receiving VII.1 unit were read. VII.1 remains byte-identical under the guarded edit; the full old P4.23 special case is included in the moved P4.37 through N=T and sigma=id. Every pole coefficient, torsion line, reduced boundary, curve count and group application was compared. The program locator now names its actual owner. D14/D23 and final structure remain open.'),
 ('night:P4.37','II-C3-ROOT-CLASS-VII-EXCLUSION-UNIT-READ',
  'The entire original and receiving P4.37 proofs were read, together with complete original P4.23 and the exact R6, P4.25, P4.15, P244, P250 and Hopf inputs. The receiving positive-Betti alternatives use the identical resolution and residue divisor. The two saddle chart pushforwards reproduce beta*x and -alpha*y, retaining positive-real weights. The saturated-sheaf identity, K*V-V^2 invariant, unrestricted integer increment, strict quadratic completion and zero-Betti Hopf endpoint remain complete. No dependency on P4.26 remains. All labels and target multiplicities are preserved. No independent credit.'),
 ('night:P4.26','II-C3-ROOT-IRREDUCIBLE-EULER-UNIT-READ',
  'The entire original and receiving P4.26 statement and proof were read. Its statement is unchanged. Every rational minimal-boundary case and blowup transfers through the same D and beta; the proper pushout includes contracted curves and specifies both group maps and the inverse. P4.21 is applied only after P4.25 has identified N=T as the smooth rational normalization. The class-VII positive-Betti case is excluded by the earlier stronger P4.37 on identical data; the old positivity conclusion follows on its empty domain. The normal torus cover and global Euler/index arguments retain their exact maps, hypotheses and parity calculation. No independent credit.')]
for unit,event,outcome in entries:
    data=dict(unit=unit,event_id=event,complete_original_and_receiving_read=True,
      outcome=outcome,unit_detail='Complete class-VII consolidation and its unchanged-domain consumers compared; protected E.5.2/E.5.3 statements untouched.')
    subprocess.run([sys.executable,str(ROOT/'code/S6_SERIES_PUBLISH_c3_read_unit.py')],
      input=json.dumps(data),text=True,check=True)

# P4.21 shares its unit with the elliptic case, whose whole-unit reading is
# already recorded; only the newly exposed, already-proved conclusion changed.
set_unit_status('night:P4.21','D12','done',
 'Root reread the entire P4.21 proof before admission and its unchanged receiving proof after the guarded statement edit. The statement now exposes e(S)=2 for its already-proved normal-crossing case; the elliptic companion is unchanged and retains its recorded whole-unit reading.',
 'CHECK_EVENTS.tsv: II-C3-ROOT-IRREDUCIBLE-EULER-UNIT-READ')
add_event('night:P4.21','II-C3-ROOT-RATIONAL-EULER-CONCLUSION-READ','used and rechecked in this run',
 'The full P4.21 proof was read with its old and receiving statements. The only new sentence exposes exactly the e(S)=2 endpoint already proved in step 4. Normal crossings gives reduced nodal conductor, and the written normalization charts give the immersion used for e(T)=6; the 3t, 2e(C)+t, e(S)=t equations give t=e(S)=2. No hypothesis changes, and the companion P4.22 is unchanged.',
 'S6_SERIES_PUBLISH_II.tex: smooth rational normalization',source='code/S6_SERIES_PUBLISH_c3_class_vii_receiving.py')
print('Complete receiving comparison recorded; final placement and page reading remain open.')
