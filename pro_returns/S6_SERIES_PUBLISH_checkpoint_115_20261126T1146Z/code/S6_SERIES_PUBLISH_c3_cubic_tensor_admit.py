"""Admit cubic normal tensors and the separate proved affine calculation."""
from S6_SERIES_PUBLISH_c3_edit import *
import json
folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_cubic_tensor_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==1
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
preserve_identifiers(before,after)
for old,new in zip(identifiers(before),identifiers(after)):
    assert all(new[k]==v for k,v in old.items())
    assert all(new[k]==1 for k in new-old)
SOURCE.write_text(after,newline='\n')
for suffix,target,key in [('defects.tsv','S6_SERIES_PUBLISH_defects_II.tsv','change_id'),('CHECK_EVENTS.tsv','CHECK_EVENTS.tsv','event_id')]:
    _,rows=read_tsv(folder/(prefix+suffix))
    if suffix=='CHECK_EVENTS.tsv':
        for row in rows:
            if 'effort' not in row['who']:row['who']+='; effort setting not separately exposed'
    print(suffix,append_rows(ROOT/target,rows,key))
_,statuses=read_tsv(folder/(prefix+'unit_progress.tsv'))
for row in statuses:
    kind='structure' if row['row']=='restructuring' else row['row']
    if kind not in ['D10','D16']:
        set_unit_status('night:P4R.19',kind,row['status'],row['basis'],row['fragment'])
add_event('night:P4R.19;rem:II:two-direction-affine-fibres',
    'II-C3-ROOT-CUBIC-TENSOR-ADMISSION','used and rechecked in this run',
    'The assigned reviewer read complete old/current and receiving R19 and its exact earlier inputs; root read every receiving paragraph and the full comparison. The complete P314 global domain, nonzero tensor, smooth generic D4 branch and arbitrary other transverse types remain. The preparation and inverse depression preserve the normal ideal. Each weighted face retains its coefficients and gaps. The P297 application has the explicit inverse Z_h/X_B maps; finite proper pullbacks have degrees2k,3l,r and squares−4k,−6l,−2r. Connectedness and the balanced double-factor case remain proved. P322 acts on the full-function root f_V with initial cP, c=alpha0 U(0), and the exact receiving level embeds into Phi=(c epsilon^d)^m. P324 states the existing affine equations, inverse coordinate maps, pole divisor and radial-product zero pairing. The unsupported inference from that affine calculation to a global counterexample is removed; the global R19 statement is unchanged. All identifiers remain; no independent or final-page credit.',
    'Complete cubic tensor subsection, including the separate affine remark and proof',source=__file__)
append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',[
dict(source='Demailly2012E (third-continuation cubic tensor)',
url='https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf',
version='Complex Analytic and Differential Geometry; author version21June2012',
locus='Complete ChapterII §2.A preparation setup/proof pp79–80 and Theorem2.1 p80; division Theorem2.3 and proof pp80–81; read by foundations reviewer',
date_utc=now(),sha256='d7c7654a7417e8322e5dcf8fe8ec818b4c1a18cf280b41f2df5a871b776d89a1',
own_word_summary='Weierstrass preparation expresses a holomorphic germ of the specified regular order as a holomorphic unit times a monic polynomial in its distinguished coordinate; the analytic division construction proves the factorization.',
use='R19 takes distinguished x, remaining coordinates(y,z), and order3. The full equality with U, coefficient divisibilities and exact inverse depression map are written explicitly.'),
dict(source='Hatcher2002 (third-continuation finite pullback and fixed character)',
url='https://pi.math.cornell.edu/~hatcher/AT/AT.pdf',
version='Algebraic Topology(2002), author PDF',
locus='Full proof2C.3 pp180–181, including cellular/homology alternating-trace identity, read for P322. Proper-map compact-support setup, direct-limit duality map and complete Theorem3.35 statement p245 read for R19; no later full proof of3.35 claimed.',
date_utc=now(),sha256='bebb3032bf9021b956da3bd070eb6c67dc662cf849be9cdf6679f677560e5618',
own_word_summary='The alternating trace is unchanged on passage from finite cellular chains to homology. Compactly supported cohomology is identified with ordinary homology by the oriented duality map in the stated manifold scope.',
use='P322 applies the trace identity to the exact finite equivariant core triangulation. R19 pulls a compactly supported two-class through its explicit finite proper maps; oriented degree multiplies the square and compact-support duality yields the compact homology class.')
],'source')
print('R19 and P324 admitted; stable original R19 unit identity retained.')
