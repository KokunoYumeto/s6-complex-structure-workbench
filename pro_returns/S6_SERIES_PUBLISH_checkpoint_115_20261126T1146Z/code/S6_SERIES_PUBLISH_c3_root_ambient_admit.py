"""Admit the read exact root-chart transfers without changing theorem scope."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder=ROOT/'agents/continuation3_occurrence_root'
prefix='S6_SERIES_PUBLISH_c3_root_ambient_'
guards=json.loads((folder/(prefix+'guards.json')).read_text())
before=SOURCE.read_text(); after=before
for row in guards:
    assert after.count(row['old'])==1,row['key']
    after=after.replace(row['old'],row['new'],1)
assert identifiers(before)==identifiers(after)
SOURCE.write_text(after,newline='\n')
details=[
 ('lem:II:signed-root-fibration','Signed root fibrations',
  'The positive chart, cyclic action, local quotient and product inverse were repeated in UN6. Their four equation aliases and one cyclic-chart display now stand at the full P339 owner; each receiving object is identified by the identity on its coordinates. Both signs, all direct-image arguments and full hypotheses remain unchanged.'),
 ('lem:II:elliptic-root-surface','Elliptic root fillings: P336',
  'The repeated quotient/smoothness/properness argument is an exact application of P339 on B times a disc, positive divisor {0} times that disc, empty negative divisor and (m,q)=(m,beta). The displayed inverse product maps identify its entire quotient with P336 times the disc. Restriction to the zero slice preserves the free finite chart, complete fibre, elliptic quotient and product inverse. The full canonical, plurigenus and integral-pair proof remains.'),
 ('cdp:st:C.2.UN.6','Elliptic root fillings: UN6',
  'The repeated ambient root proof is replaced by P339 with the identical blown-up V, positive exceptional R, empty negative divisor, line, section, m and q. All tuple, cyclic-chart, deck, product and inverse maps are explicitly identical. ER3 and ER9–11 retain the blowup, Hopf component, intersection and full-fibre computations. The complete P336 application, persistence, non-bimeromorphism and compact realization remain unchanged.')]
rows=[]
for i,(guard,detail) in enumerate(zip(guards,details),1):
    statement,location,reason=detail
    rows.append(dict(change_id=f'II-C3-ROOT-AMBIENT-{i:02}',type='D12',statement_id=statement,
        old_location=location,old_page='current source before exact ambient transfer',
        new_location=location,new_page='integrated build pending',old_text=guard['old'],new_text=guard['new'],
        reason=reason,review_status='Root read complete current and receiving P339, P336 and UN6, including all unchanged proof portions; the final bounded connected-map wording was re-read. Both P336 and UN6 statement blocks are byte-identical. All labels and targets have identical multiplicities. Exposed used-and-rechecked comparison only.'))
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
comparison='''# Exact positive-root applications

Root read all complete current and receiving P339/P336/UN6 statements and
proofs. P336 and UN6 statement blocks are byte-identical. P339 retains the
same mathematical statement, proof and both signed charts; only the four
ER aliases and the displayed cyclic map move to their unique owner.

P336 is obtained from the unchanged surface-domain P339 by taking
V=B×Delta and D+={0}×Delta, with D− empty. The inverse holomorphic maps
[(v,y,ell,a)] <-> ([(v,ell,a)],y) prove the product identification.
The zero-slice base change proves properness on the same compact B and
restricts the identical cyclic and product charts. No extension of P339's
statement to a new dimension is used.

UN6 applies P339 to exactly its blown-up surface, positive exceptional
divisor, line, canonical section, m and q. Its chart, cyclic map and product
inverse agree by the identity in every displayed coordinate. ER4/5/7/8
are aliases at the corresponding P339 displays; ER6 is the same positive
cyclic chart in its proof. ER3 and ER9–11 stay in UN6. The entire elliptic
root pair, component cohomology, Kodaira dimension, noncontraction,
base-change persistence and compact realization remain unchanged.

Every original label and target has exact multiplicity. The two D12 rows
for signed-root-fibrations and elliptic-root-fillings now close after
their explicitly recorded pending comparison. Global placement, front
matter, final typography and every final page remain open. No independent
proof, new required-check count or mathematical error is claimed.
'''
(folder/(prefix+'comparison.md')).write_text(comparison,newline='\n')
event='II-C3-ROOT-AMBIENT-TRANSFER'
for unit in ['subsec:II:signed-root-fibrations','subsec:II:elliptic-root-fillings']:
    set_unit_status(unit,'D12','done',
        'The complete P339/P336/UN6 comparison is admitted. Their shared root-chart, free quotient, properness and product proof has one earlier owner. P336 uses the explicit B times disc product and zero-slice base change; UN6 uses the identical blown-up surface, exceptional divisor and tuple. Every specialized component and pair calculation remains. All25 local classes were read; other final integration gates remain open.',
        'CHECK_EVENTS.tsv: '+event)
add_event('lem:II:signed-root-fibration;lem:II:elliptic-root-surface;cdp:st:C.2.UN.6',event,
    'used and rechecked in this run',
    'Root read every complete original/current and receiving proof and the final bounded connected-map wording. P336 uses the exact P339 surface B times a disc and inverse quotient-product maps, followed by the zero-slice base change. UN6 uses the identical V, R, empty negative divisor, L, sigma, m and q; all chart, deck, quotient, product and inverse formulas are identities. ER4/5/7/8 move once to their P339 owner displays and ER6 to its same positive cyclic map. Both receiving statements are byte-identical, and all old identifiers have identical multiplicity. Every canonical, integral-pair, component, persistence, non-bimeromorphism and compact conclusion is preserved. The pending two D12 rows close. No independent proof, new required check, final-page credit or statement refutation.',
    'Signed root fibrations and elliptic root fillings',source=__file__)
print('Exact root applications admitted; the two pending D12 rows closed.')
