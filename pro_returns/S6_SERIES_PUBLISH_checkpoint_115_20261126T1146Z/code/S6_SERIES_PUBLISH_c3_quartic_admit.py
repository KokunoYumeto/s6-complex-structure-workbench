"""Admit the complete quartic unit and its exact shared divisor comparisons."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_quartic_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==5
before=SOURCE.read_text();after=before
for row in guards:
 assert after.count(row['old'])==1,row['key']
 after=after.replace(row['old'],row['new'],1)
 print('Applied',row['key'])
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
 for name,count in old.items():assert new[name]==count,name
 for name,count in (new-old).items():assert new[name]==1,name
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
 _,rows=read_tsv(folder/(prefix+suffix));print(suffix,append_rows(ROOT/target,rows,key))
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
for row in statuses:
 kind='structure' if row['row']=='restructuring' else row['row']
 if kind in ['D10','D16']:continue
 set_unit_status('night:P4.52',kind,row['status'],row['basis'],row['fragment'])

add_event('cdp:st:A.5.3;lem:II:proper-conductor-divisor;lem:II:weighted-initial-monodromy;night:P4.52;lem:II:elliptic-map-minimal-model',
 'II-C3-ROOT-QUARTIC-UNIT-ADMISSION','used and rechecked in this run',
 'Root read the complete original and receiving A53, P300 and quartic subsection, including all three clauses and full proof of P322, plus the full application/source comparison. A53 is the single general compact-hypersurface divisor owner, with Md=-b positivity, zero-block and positive-genus refinements and all original ruled/Picard conclusions. P300 applies it on identical normalization/resolution/generator maps and retains its proper-torus support proof. P452 maps D1.9 to P451 first clause on the same full fibre, keeps the exact unit root/local-level inclusion, and applies P322 to the same weighted scaling and homogeneous quartic. All bounds M<=5, 4(7-M), 3(7-M), gap21-4M and coefficient2=(d-2)n+a are retained. The point-blowup residue factors are explicit. Popescu-Pampu analytic domination/factorization applies to the exact smooth-surface modifications in P452 and P318. The agent read the complete old/new P318 context and cited source statements. No independent proof check or final-page reading is claimed.',
 'Complete quartic subsection and exact A53/P300/P318 guards',source=__file__)

sources=[dict(source='Popescu-Pampu 2016 (third-continuation analytic surface modifications)',
 url='https://www.numdam.org/item/10.5802/wbln.14.pdf',version='Winter Braids Lecture Notes3(2016),CourseIII,1–74; DOI10.5802/wbln.14',
 locus='Complete printed p20, analytic surface setup and Propositions3.10/3.12; statements and setup read by foundations reviewer, not unprinted proofs',
 sha256='3c2190b5fa1e2bf94e2605b41ac6c75dabb1d629139380e67c8bdfdaa811efbd',
 own_word_summary='Every analytic resolution of a normal surface singularity dominates its unique minimal resolution. A proper holomorphic modification between smooth complex surfaces factors into point blowups.',
 use='P452: the normalization-resolved strict transform dominates the old minimal resolution, and the resulting smooth-surface modification factors. P318: factor the stated rho:X to Z.'),
 dict(source='Siersma 1991 (third-continuation weighted monodromy owner)',
 url='https://webhomes.maths.ed.ac.uk/~v1ranick/papers/siersma.pdf',version='Topology30(3)(1991),445–469; journal PDF',
 locus='Sections1.2,3.4–3.6,5.3,6.2–6.5,7.1, printed pp445,451–452,457–458,460–462; diagrams452/462 also viewed by foundations reviewer',
 sha256='a1e17e14cc0052271b1d6f8a875aedbae34a08cf1b456046c888420a22904595',
 own_word_summary='The variation maps satisfy the displayed relation with the absolute-to-relative maps. The dimension-two boundary Wang sequence bounds the kernel by the transverse first homology, and the isolated case has the stated kernel comparison.',
 use='P322: the exact j,j2,VARII,T and transverse F_i/A_i give rank(T-I)<=sum mu_i when the intersection form is zero. P452 applies this to the same homogeneous quartic.'),
 dict(source='Hatcher 2002 (third-continuation free monodromy character)',
 url='https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',version='Algebraic Topology(2002), author PDF',
 locus='Theorem2C.3 and compact-manifold/finite-complex setup, printed p179; reopened by foundations reviewer; no complete proof or whole-book reading claimed',
 sha256='bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618',
 own_word_summary='A nonzero Lefschetz number forces a fixed point in the stated finite-complex setting, which includes the compact manifold core used here.',
 use='P322: every nonidentity free weighted scalar element on the invariant compact Milnor core has zero Lefschetz number; the character identity gives the rank lower bound.')]
for row in sources:row['date_utc']=now()
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',sources,'source')
print('Quartic unit admitted with stable unit id night:P4.52; D14/D23/D24/structure remain open.')
