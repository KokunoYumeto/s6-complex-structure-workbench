"""Admit the complete elliptic-contraction comparison and its exact shared maps."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_foundations/sec07'
prefix='S6_SERIES_PUBLISH_sec07_elliptic_contraction_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
assert len(guards)==6
before=SOURCE.read_text();after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
    print('Applied',row['key'])
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
    if kind in ['D10','D16']:continue
    set_unit_status('night:P4.54',kind,row['status'],row['basis'],row['fragment'])
set_unit_status('night:P4.53','D22','done',
    'The exact weighted transport now acts directly on g_u with initial alpha P5 and level c=alpha. Its initial set is identically P5=1; the receiving level lies in Phi=(alpha epsilon^5)^m. All pairing comparisons use those same maps. P451 already proves the general unit flow, and P452 remains unchanged.',
    'CHECK_EVENTS.tsv: II-C3-ROOT-ELLIPTIC-CONTRACTION-ADMISSION')
add_event('night:P4.54;night:P4.53;lem:II:weighted-initial-monodromy;cdp:st:A.5.17',
    'II-C3-ROOT-ELLIPTIC-CONTRACTION-ADMISSION','used and rechecked in this run',
    'The assigned reviewer read the complete original and receiving A517/P322/P454 and complete admitted P451/P452/P453. Root read all receiving A517/P322/P454, the full comparison, P451 unit-flow proof, and the complete changed P453/P454 transport items. A517 states its already proved isolated-germ square-minus-two sphere construction before its full-root torus application. P322 retains its original compact transport and variation maps, and adds the exact real algebraic double, half projection/inverse, equivariant cellular trace and fixed-locus collar. P454 preserves the analytic formal-function ideals/completion, all three elliptic section rings, fixed-r coordinate changes and inverse blowdown map, weights6/7/9, every coarse/cover branch character and numerical gap. The degree6 polynomial is proved reduced before its nonfree character calculation. The receiving g-to-g_u application omission is repaired by applying transport directly to g_u with initial alpha P and c=alpha; the exact level lies in Phi=(alpha epsilon^D)^m. P452 already contains the P451 unit flow and is unchanged. The degree9 sphere and final R18 application retain their precise scopes. All identifiers survive; no statement is refuted, no independent or final-page credit.',
    'Complete P454 and shared A517/P322; exact P453 root-level application',source=__file__)

records=[
dict(source='Dolgachev1982 (third-continuation elliptic contraction)',
url='https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/weighted82.pdf',
version='Weighted projective varieties, LNM956(1982),34–71; DOI10.1007/BFb0101508; author PDF',
locus='Complete Theorem1.4.1 and proof, pp39–41; publication metadata verified by assigned foundations reviewer',
sha256='f93b558ac5ffe7420f5d64c8faac28587fb064b7a7b7cca5405e9b1d89410926',
own_word_summary='The cohomology of graded sheaves on weighted projective space identifies H0 with weighted polynomials, gives intermediate vanishing, and identifies top-degree dimensions by the shifted graded piece.',
use='Apply to S=C[u,v,w], weights(a,b,c), and the exact hypersurface sequence with twist−e. The long exact sequence gives h0(O_D)=1 and h1(O_D)=dim S_(e−a−b−c); ordinary weights(1,1,1) give the plane-cubic section ring.'),
dict(source='ParkSuh1996 (third-continuation finite weighted character)',
url='https://www.jstage.jst.go.jp/article/kyushujm/50/1/50_1_179/_pdf/-char/en',
version='Kyushu Journal of Mathematics50(1)(1996),179–205; DOI10.2206/kyushujm.50.179; primary publisher PDF',
locus='Rendered pp179–180, complete setup and Theorem1.2 read. Its later proof was not read and is not given proof-reading credit.',
sha256='50ff3fa390399ba302fc0f80c327aae0c7d2bd1a2fd6c3e3cc44b9e66c719165',
own_word_summary='The real algebraic group action in the stated domain admits an equivariant semialgebraic triangulation compatible with isotropy.',
use='The compact real algebraic double of {P=1,Rw≤R0}, t²=R0−Rw, has the finite mu_d×{±1} action. Its sign-fixed equator and closed halves are subcomplexes after subdivision. Projection and the explicit square-root inverse identify a half with the exact weighted core. Cellular traces then compute fixed-locus Euler numbers by the already opened Hatcher trace identity.'),
dict(source='Milnor1968 (third-continuation local-sphere locus)',
url='https://djvu.online/file/kCFrJq27uCPRi',
version='Singular Points of Complex Hypersurfaces, Annals of Mathematics Studies61, Princeton1968; online reproduction of primary text',
locus='Full Lemma6.1/proof pp55–56 and AppendixB pp111–114 read in primary-text OCR by foundations reviewer. No complete PDF download/hash or whole-book reading; two trial images at other printed pages receive no credit for these loci.',
sha256='',
own_word_summary='The local boundary-transversality and holomorphic-gradient degree arguments supply regular boundary tubes and positive local degree for the isolated critical point construction.',
use='A517 retains the fixed boundary ball, proper discriminant, finite-gradient perturbation, exact holomorphic Morse coordinates and oriented transport. The isolated-germ sphere clause is the same existing proof, now stated before its torus application.')]
for row in records:row['date_utc']=now()
print('Primary readings',append_rows(ROOT/'S6_SERIES_PUBLISH_c3_primary_readings.tsv',records,'source'))
print('P454 complete unit admitted; P453 exact-map row closed; P452 unchanged.')
