from pathlib import Path
from datetime import datetime,timezone
p=Path('S6_06_BLIND/notes/part3_family.md')
s=p.read_text()
changes=[]
def replace(old,new,reason):
 global s
 if old not in s:raise SystemExit('Missing status passage: '+old[:80])
 s=s.replace(old,new)
 changes.append((reason,old))
replace(r'''Combining this construction with (P3F.3.1) computes the Hopf-glued sphere
for the numerical pair ((-1,-4)): its oriented class is zero. The
remaining application to the AC26 family consists of an actual geometric
identification of the family's clutched sphere with this Hopf gluing,
and a derivation of the numerical pair from its charts. Neither is
supplied by the abstract classification theorem, and neither is claimed
to have been completed in this file.''',r'''Combining this construction with (P3F.3.1) computes the Hopf-glued sphere
for the numerical pair ((-1,-4)): its oriented class is zero.
P3F.8 supplies the actual geometric identification with the family,
and P3K.6--9 derive the characteristic numbers from its charts and
its specified descended rotating framing. The classification theorem
is used only after these geometric comparisons.''','P3F.4 application completed by P3F.8 and P3K.6--9.')
replace(r'''For the family application the smallest undecided instance remains the
original ((3,4)\) sphere family: one must identify its positive parameter
return map, including the cusp collar, with a geometric representative
on the quotient model and evaluate the normal/relative characteristic
data. The direct images and full automorphism result in the independent
Part5 notes do not determine that isotopy class. The construction of
P3F.4 now supplies the explicit passage to an oriented standard sphere
for the classified pair ((-1,-4)\); it leaves the geometric evaluation
of that pair visible rather than assuming it.

Approaches pursued here are the exact rank-one table enumeration,
permutation-certified existence of every source, section-height and
component calculations, Jin's full integral classification in fixed
coordinates, explicit Hopf-lift extension over (D^4\times S^3\), and
Takase's corrected normal-Euler formula. The next geometric calculation
is the local-to-global comparison of the original toric cusp collar with
the Hopf-lift gluing. It must carry the phase of the linearization and
the finite logarithmic transformations, not only the fibre period
matrix.''',r'''The initial main-case gap has been resolved by the actual orbit and
Hopf comparison P3F.7--13, the real trace P3K.6--7, the independent
analytic index calculation P3K.8, and the rotating-frame computation
P3K.9. These prove zero positive-loop class for the original family
and give ((k,\ell)=(-1,-4)\) in the stated descended framing.
P3F.25 applies the same actual trace to the further verified families
and computes the nonzero weighted OS47 example. The remaining
component-supported OS49 page comparison is stated separately in
P3F.27. The exact earlier status passages are preserved, with their
superseding proof identifiers, in
`records/part3_superseded_status.md`.''','Historical main-case status superseded by P3K.6--9 and P3F.25.')
replace(r'''The remaining numerical step in P3.1 is therefore exact: compute
k=integral_{M_f}x³ and ell=integral_{M_f}p1 x for this f, including the
finite-root and cusp collar contributions. Parent Statement P2.1
provides the actual sixfold descent

    H(t)delta, H(t)=-(4l1 log t+3l2 log(t-1))/(2pi i),

with cusp coefficient -p after carrying the collar integer l0. Its
circle quotient is a radial translation in the line-bundle direction.
The page/cap identification needed to turn that exact formula into
the values(-6,-24) for the sixth power has not yet been written. No
finite-group class is declared computed from that missing comparison.''',r'''The actual sixfold descent of P2.1 is

    H(t)delta, H(t)=-(4l1 log t+3l2 log(t-1))/(2pi i),

with cusp coefficient -p after carrying the collar integer l0.
P3K.6--7 constructs its real trace with the complete line clutch.
P3K.9 evaluates its characteristic pair as(-6,-24), including the
normal-frame comparison, and descends it to(-1,-4) for one parameter
loop. The forward geometric mapping-torus orientation and Jin's
reverse convention are both included in P3K.7.''','P3F.8 numerical application completed by P3K.6--9.')
replace(r'''the closed T3 boundary gives additivity. These statements give the
page and its actual line and framing data. The further identification
of the annular return with a closed spin-six cap whose characteristic
pairings are3s_delta and p_rel remains a separate step; no value in
Theta7 is asserted merely from these two numbers.''',r'''the closed T3 boundary gives additivity. These statements give the
page and its actual line and framing data. The required actual return
comparison is the real spin bordism P3K.6--7, and its normal-frame
term is computed in P3K.9. Thus the later finite-group conclusion
uses both the page calculation and that geometric comparison.''','P3F.10 cap comparison completed by P3K.6--9.')
replace(r'''The numerical membership of the AC26 return in this kernel still
requires the annular collar calculation; P3F.11 supplies the exact
integer framework for that calculation and the reduction from six
parameter loops to one.''',r'''P3K.7--8 proves that the AC26 return belongs to this kernel, by two
computations through the actual trace. The integral framework here
then gives the reduction from six parameter loops to one.''','P3F.11 kernel membership completed by P3K.7--8.')
replace(r'''These are exact local index inputs. Turning them into an index of the
actual return still requires a global bordism or a proved relative
index excision at the corner; neither is inferred from the numerical
cancellation alone.''',r'''These are exact local index inputs. P3K.6--8 subsequently constructs
the actual real bordism and identifies its spin-c symbol. The
resulting return index therefore follows through that comparison;
no analytic corner completion is asserted.''','P3F.14 index comparison completed by P3K.6--8.')
p.write_text(s)
h=Path('S6_06_BLIND/records/part3_superseded_status.md')
with h.open('a') as f:
 f.write('\n# Status passages archived '+datetime.now(timezone.utc).isoformat()+'\n\n')
 for reason,old in changes:f.write('## '+reason+'\n\n```text\n'+old+'\n```\n\n')
print('Archived and replaced',len(changes),'superseded status passages.')
