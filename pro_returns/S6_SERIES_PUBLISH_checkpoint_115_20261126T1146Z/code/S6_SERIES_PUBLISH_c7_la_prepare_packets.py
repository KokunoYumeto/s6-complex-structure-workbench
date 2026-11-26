#!/usr/bin/env python3
"""Stage the complete LA comparison; no canonical/global mutation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import io
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_weighted_engel'
BASE='S6_SERIES_PUBLISH_III_02LA_'
ID='maps:src:D.2.34'
canonical=ROOT/'S6_SERIES_PUBLISH_III.tex'
original_bytes=canonical.read_bytes()
assert sha256(original_bytes).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source=original_bytes.decode()
fresh=LANE/(BASE+'fresh_derivation.md')
assert sha256(fresh.read_bytes()).hexdigest()=='31e15560f3107ae1edaed754edcd91d70685943a6e398647552a5ba338c89105'

def released(kind,env):
    lines=(LANE/(BASE+'released_'+kind+'.tex')).read_text().splitlines()
    assert all(x.startswith('%') for x in lines[:5])
    text='\n'.join(lines[5:]).rstrip('\n')
    assert text.startswith('\\begin{'+env+'}') and text.endswith('\\end{'+env+'}')
    assert source.count(text)==1
    start=source[:source.index(text)].count('\n')+1
    return text,(start,start+text.count('\n'))

old_statement,sspan=released('statement','theorem')
old_proof,pspan=released('proof','proof')
assert pspan==(14840,15102)
assert sha256(old_proof.encode()).hexdigest()=='457ae5d9732040f26b15176c8810a04a1942dcda6c750586a2f41ea162c2ade7'
assert len(re.findall(r'\\item\b',old_proof))==14
new=(LANE/(BASE+'receiving.tex')).read_text().rstrip('\n')
new_statement,new_proof=new.split(r'\begin{proof}',1)
new_statement=new_statement.rstrip('\n')
new_proof=r'\begin{proof}'+new_proof

def identities(text):
    return tuple(sorted(re.findall(p,text)) for p in
        (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'))

assert identities(old_statement)==identities(new_statement)
assert identities(old_proof)==identities(new_proof)
assert len(identities(new)[0])==14 and len(identities(new)[2])==13
print('PASS frozen fresh proof and canonical source unchanged; all14 original proof items identified.')
print('PASS separate exact guards: statement',sspan,'proof',pspan)
print('PASS all14 permanent identities and13 WE equation tags preserved by their separate guards.')

def write_table(suffix,fields,rows):
    s=io.StringIO(newline='')
    w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
    (LANE/(BASE+suffix+'.tsv')).write_text(s.getvalue(),newline='\n')

reason=(
    'Whole703-line fresh proof, complete new program/output and two bounded reviews preceded '
    'the individual original release. All14 original proof items and every auxiliary were '
    'then read against the complete receiver. All WE1-WE13 formulas stand. D26 scope '
    'clarification: d=1 recovers the natural row by identity maps, while d>1 has Euler2d>2. '
    'The receiver supplies the scalar-adjusted actual cover, every toric/period inverse, '
    'primitive exterior and cusp relative maps, full finite/original kernels, exact '
    'meridian sign/order, integral pair-sequence sections, complete group and all Smith '
    'forms. All labels/targets retained. No original D25 or D27, historical execution, '
    'new primary reading, or extra independent-blind credit. Canonical and unit/build/page '
    'integration remain at their later gates.'
)
replacements=[]
for kind,before,after,span in (
    ('statement',old_statement,new_statement,sspan),
    ('proof',old_proof,new_proof,pspan)):
    replacements.append(dict(statement_id=ID,old_text=before,new_text=after,
        reason=f'Separate {kind} guard at canonical lines{span[0]}-{span[1]}. '+reason))
write_table('replacements',['statement_id','old_text','new_text','reason'],replacements)
trial=source
for row in replacements:
    assert trial.count(row['old_text'])==1
    trial=trial.replace(row['old_text'],row['new_text'],1)
for row in reversed(replacements):
    assert trial.count(row['new_text'])==1
    trial=trial.replace(row['new_text'],row['old_text'],1)
assert trial==source
print('PASS both exact replacements apply uniquely and their joint inverse restores the source.')

def between(text,start,end):
    i=text.index(start)
    return text[i:text.index(end,i+len(start))].rstrip('\n')

defects=[]
def defect(suffix,kind,before,after,why):
    hits=[(part,span) for part,span in ((old_statement,sspan),(old_proof,pspan)) if before in part]
    assert len(hits)==1,(suffix,'old-block ambiguity')
    part,span=hits[0]
    assert part.count(before)==1 and after in new,suffix
    line=span[0]+part[:part.index(before)].count('\n')
    newline=1+new[:new.index(after)].count('\n')
    defects.append(dict(change_id='c7-III-02LA-'+suffix,type=kind,statement_id=ID,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{line}',old_page='',
        new_location=str((LANE/(BASE+'receiving.tex')).relative_to(ROOT))+f':{newline}',
        new_page='',old_text=before,new_text=after,reason=why,
        review_status='proposed; root record admission, canonical application and final page review pending'))

defect('header','D10',next(x for x in old_statement.splitlines() if x.startswith(r'\StatementRecord')),
    r'\textup{\small(tag 02LA)}','Replace machine navigation by the small permanent printed tag.')
defect('title','D16',old_statement.splitlines()[0],new_statement.splitlines()[0],
    'Use a short mathematical title while preserving the permanent identity.')
defect('weight-one-scope','D26',
    'This gives an unbounded initial-weight family outside\nthe finite sphere-candidate catalogue.',
    'At $d=1$ this is the natural construction with $P=G$ and $Q=6G$.\nFor $d>1$ its Euler characteristic is $2d>2$; these weights extend\nthe construction beyond the sphere-candidate catalogue.',
    'Resolve the included endpoint by the identity suspension and toric maps; state the d>1 Euler conclusion at its exact range. Same theorem identity, all displayed formulas preserved; no broader refutation inferred from the ambiguity.')
defect('fixed-vectors','D20',
    'For logarithmic caps put\n\\[\n m_0=3k,\\quad m_1=4\\ell,\\qquad\n v_i=r_i\\delta+n_i u_i,\\qquad k,\\ell>0.\n\\]',
    between(new_statement,'In the marked period basis', 'The exact freeness conditions'),
    'Give the weight-dependent u0,u1 in their single marked period basis before their use in the statement.')
defect('cyclic-coordinates','D02',
    'These are direct-sum descriptions, not necessarily\nordered invariant factors.',
    'The displayed summands are the independent cyclic coordinates\nconstructed in the proof.',
    'State the proved positive coordinate interpretation of the direct sums.')
defect('one-complete-proof','D14',old_proof,new_proof,
    'Organize one complete proof through the construction, cusp/exterior maps, full local kernels, group, one global relative sequence and closed forms. The entire old and new proof were read; all original auxiliaries are proved at the same identities, with exact quotient maps and inverse sections.')
defect('machine-enumeration','D10',
    r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]',
    'We use the marked line, periods and toric charts of',
    'Remove machine-prefixed item labels in the connected mathematical proof.')
defect('cover-scope','D02',
    'It does not assume that the filled threefold is a\nfree cover of a weight-one finite quotient when $d$\nshares a factor with its multiplicities.',
    between(new_proof,'Over $S\\setminus I_1$',r'\smallskip'),
    'Give the precise zero-free suspension domain, actual toric extension and inverse sheet maps; the subsequent finite quotients have their own full construction.')
defect('certificate-minor','D09',
    'The common exterior-square relations likewise contain\na unit minor in the displayed primitive kernel of\n$\\xi_d$; the certificate gives its column indices\nas a polynomial identity in $d$.',
    'In the kernel basis\n$(s_1,s_2,s_3+6ds_4,s_5,s_6)$, columns $0,3,4,5,11$ of\n$(E_0\\ E_1\\ E_\\infty)$ have determinant $-1$.',
    'Replace a file-dependent assertion by the exact all-weight column indices and determinant, with the integral relation preimages already in the proof.')
defect('original-kernel-wording','D02',
    'These statements retain\nthe primitive Chern class rather than making a\nzero-degree approximation.',
    'The line degree stays\n$C_p^*-C_0^*$ throughout.',
    'State the actual line class positively; give its complete period/Wang/Gysin maps.')
defect('boundary-torsion-wording','D02',
    'It would\ntherefore be incorrect to reuse a free-boundary\nMayer--Vietoris splitting from weight one.',
    'The cusp boundary has $H_1=\\mathbb Z^3\\oplus\\mathbb Z/d$,\nwhere the last generator is $\\delta$. To retain that torsion,\nuse the full relative sequence',
    'State the boundary group and the full sequence directly, including the primitive relative image and component-disc section.')
defect('meridian-sign','D20',
    'Thus every disc has boundary the same class\n$x_0+x_1$, with the common boundary orientation;\nat an original site its $x_i$ is zero.',
    between(new_proof,'Positive cusp discs use the cut-base relation', 'The full relative map is'),
    'Give the exact -I_d coordinate map and inverse between the cut-base and inward E-boundary signs, then retain the original WE13 identity.')
defect('meridian-order','D22',
    'Its element $x_0+x_1$ has\ninfinite order precisely when $P\\ne0$.',
    between(new_proof,'For $P\\ne0$ the meridian has infinite order:', 'Its free quotient has rank'),
    'At the use, prove both the infinite-order coefficient and the exact finite order lcm(mbar0,mbar1), the full kernel basis/inverse and its actual bounding power chains.')
defect('group-convention','D20',
    'Thus the full group is abelian with that exact\ninteger presentation.',
    between(new_proof,'In a column-image convention', 'Put $C='),
    'Identify the row-relation group with the printed column cokernel by the exact Smith maps U^-1 V^t and V^-t U.')

fields=['change_id','type','statement_id','old_location','old_page','new_location','new_page',
        'old_text','new_text','reason','review_status']
write_table('defects',fields,defects)
assert len(defects)==14
assert sum(d['type']=='D26' for d in defects)==1
assert not any(d['type'] in ('D25','D27') for d in defects)
print('PASS all14 scoped defect rows; one D26 endpoint clarification, no D25/D27 refutation.')

fresh_where=[str((LANE/(BASE+x)).relative_to(ROOT)) for x in
    ('fresh_derivation.md','fresh_arithmetic.json')]
fresh_where += ['agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LA_fresh_root_review.md',
 'agents/continuation7_iii_multiplicative/S6_SERIES_PUBLISH_III_02LA_fresh_bounded_review.md',
 'code/S6_SERIES_PUBLISH_c7_weighted_engel.py','code/S6_SERIES_PUBLISH_c7_weighted_engel.out']
post_where=[str((LANE/(BASE+x)).relative_to(ROOT)) for x in
    ('released_statement.tex','released_proof.tex','post_exposure_derivation.md',
     'comparison.md','receiving.tex','replacements.tsv','defects.tsv')]
post_where += ['code/S6_SERIES_PUBLISH_c7_weighted_engel_auxiliary.py',
 'code/S6_SERIES_PUBLISH_c7_weighted_engel_auxiliary.out',
 'code/S6_SERIES_PUBLISH_c7_la_receiver_check.py','code/S6_SERIES_PUBLISH_c7_la_receiver_check.out']
assert all((ROOT/p).exists() for p in fresh_where+post_where)
now=datetime.now(timezone.utc).isoformat()
common=dict(statement_id=ID,date='2026-11-25',
 who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed',
 source_file='S6_SERIES_PUBLISH_III.tex',source_row=sspan[0],
 evidence_group='publish:c7:III:02LA:check-sequence',
 publish_input_file=str((LANE/(BASE+'comparison.md')).relative_to(ROOT)),
 publish_input_row=1,date_utc=now)
events=[dict(common,type='targeted proof check',
 outcome='Complete703-line proof and full new program/output read before original release; actual scalar-adjusted all-d cover and toric extension, complete cusp normalization and relative sequence with boundary Z/d, primitive graph/fibre inverse maps, unrestricted finite Thom and original kernels, full abelian group, integral bridge, all homology and Smith forms proved. Two bounded reviews have their stated scopes. Fresh completion00:22:52 UTC precedes release00:23:48 UTC. The 2376 finite instances and further endpoint/original checks support the separate unbounded proof. No historical algorithm or output used, no new primary reading, and no post-exposure work counted blind.',
 event_id='publish:c7:III:02LA:fresh-complete-derivation',phase='before whole original LA exposure',
 source_event_type='targeted proof check',where='; '.join(fresh_where)),
 dict(common,type='used and rechecked in this run',
 outcome='Whole original statement and all14 proof items/WE1-WE13 auxiliaries read against the complete receiver. New all-d auxiliary program proves exact graph/exterior minors, cusp quotient/section and original area/Wang kernels; full output read. Additive-first WE12, exact WE13 sign map, finite meridian order lcm(mbar0,mbar1), relative kernel inverse and actual bounding chains establish the full torsion-sensitive extension. D26 refinement at the same theorem identity: d=1 is the natural row via identity maps; d>1 has Euler2d>2. All displayed conclusions stand, no D25/D27. Separate exact guards and all14 defect rows checked; syntax earns no build/unit/page credit. Shared evidence group, no additional independent-blind credit. Root admission and canonical application remain separate.',
 event_id='publish:c7:III:02LA:whole-original-comparison',phase='after whole original LA exposure',
 source_event_type='used and rechecked in this run',where='; '.join(fresh_where+post_where))]
event_fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row',
 'source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']
write_table('CHECK_EVENTS',event_fields,events)
assert len({e['evidence_group'] for e in events})==1
assert canonical.read_bytes()==original_bytes
print('PASS two accurately scoped events share one evidence group; only the owning lane is written.')
print('RECEIVER SHA256',sha256((LANE/(BASE+'receiving.tex')).read_bytes()).hexdigest())
print('COMPARISON SHA256',sha256((LANE/(BASE+'comparison.md')).read_bytes()).hexdigest())
print('PACKET COMPLETE UTC',now)
