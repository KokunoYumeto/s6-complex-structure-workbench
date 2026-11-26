from pathlib import Path
import csv
import datetime as dt
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]
def bind(p):
    return {'path': p, 'sha256': hashlib.sha256((R / p).read_bytes()).hexdigest()}
def read(p):
    return json.loads((R / p).read_text())
def verify(o):
    if isinstance(o, dict):
        if 'path' in o and 'sha256' in o:
            assert bind(o['path'])['sha256'] == o['sha256'], o['path']
        for v in o.values():
            verify(v)
    elif isinstance(o, list):
        for v in o:
            verify(v)

p = 'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_WW_v3_20261122/S6_SERIES_PUBLISH_II_A2_WW'
index = p + '_admission_recommendation.json'
assert bind(index)['sha256'] == 'ac9e1e89e3faea9e9c54cbb67314680dfb372c48782f964b566d276416865e3d'
ar = read(index)
verify(ar)
verify(read(p + '_v3_manifest.json'))
at = ar['targets'][0]
proposal = read(ar['proposal']['path'])
original = (R / at['full_original_block']['path']).read_text()
proposed = (R / at['proposed_full_block']['path']).read_text()
work = original
for g in proposal['guards']:
    assert hashlib.sha256(work.encode()).hexdigest() == g['intermediate_before_sha256']
    assert work.count(g['literal_old']) == 1
    work = work.replace(g['literal_old'], g['literal_new'])
    assert hashlib.sha256(work.encode()).hexdigest() == g['intermediate_after_sha256']
assert work == proposed
for g in reversed(proposal['guards']):
    i = g['offset_before']
    assert work[i:i + len(g['literal_new'])] == g['literal_new']
    work = work[:i] + g['literal_old'] + work[i + len(g['literal_new']):]
assert work == original
assert original.count('\\item ') == proposed.count('\\item ') == 13
assert re.findall(r'\\\[(.*?)\\\]', original, re.S) == re.findall(r'\\\[(.*?)\\\]', proposed, re.S)
assert re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$', original, re.S) == re.findall(r'(?<!\\)\$(.*?)(?<!\\)\$', proposed, re.S)

review = 'records/S6_SERIES_PUBLISH_II_root_continuation2_batch52_review.json'
assert not (R / review).exists()
rd = dict(
    created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
    checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, root, second continuation; reasoning effort not separately exposed',
    actual_reading='Root read the entire seven-section frozen derivation, all thirteen original items and fifteen displays, all seven alternate v2 items, the full earlier comparison and omission map, both complete code/output pairs and source/program records. Root then read the complete final v3 thirteen-item proof, full v3 item-by-item comparison, all seven exact guards, display record, revision decision, events, Programs rows and scope. Guard hashes and all nested bindings are verified. No III/IV proof or closed I/V source was opened.',
    mathematical_review=[
        'The frozen derivation uses the actual finite map nu:T->S->Y. Saturation E of its rank-two differential image is locally free by the depth lemma over the regular surface local rings. The quotient is L tensor I_Z and ambient rational Chern vanishing gives c2(E)=c1(E)^2-length(Z)<=0. The intersection lattice of a k-fold blowup of a Hopf surface is minus the identity and c2(T)=k.',
        'Factor the inclusion T_T into E by E_(j+1)=E intersect E_j(C) along a smooth curve. Finiteness excludes two positive generic DVR elementary divisors, because that would annihilate the curve tangent derivative. The quotient is supported on C, has depth at least one and generic rank one, hence is i_*L_j with L_j a line bundle. The exact restricted sequence is L_j(-C)->E_j|C->E_(j+1)|C->L_j->0, with its first map injective. Put K_j=ker(E_(j+1)|C->L_j). The nonzero map T_C->K_j gives degree(K_j)>=2-2g(C)>=0. The Chern-character formula gives c2(E_(j+1))-c2(E_j)=degree(K_j), as checked symbolically. Therefore c2(E)>=k; comparison forces k=length(Z)=0. On each remaining elliptic conductor curve, the last modification has degree-zero tangent map, hence an isomorphism, and E is a subbundle of nu^*T_Y. Its curve differential is nowhere zero.',
        'The conductor is the finite canonical-duality ideal omega_T tensor nu^*omega_S^-1, with its exact common-ideal image relation. A finite conductor map factors through its normalized image; the nowhere-zero tangent differential makes that image branch smooth and unramified. Two distinct image germs at one point require distinct normalization surface branches. Their hypersurface ideals in a smooth threefold have an intersection curve germ, contained in both conductor images. Each normalization branch has its unique conductor germ, so the two image germs coincide. Riemann-Hurwitz makes the image elliptic. The normalization Euler decomposition therefore gives e(S)=0. This is the same conclusion on the identical T and S as the printed proof.',
        'The original proof passes through a degree-d unramified primary Hopf cover; pulling back each blowup gives k prime=d*k and the same finite-map setting. Khaled v2 supplies the exact contracting form F(z,w)=(alpha*z+lambda*w^n,beta*w), with lambda*(alpha-beta^n)=0. Adjunction makes every compact curve arithmetic genus one, while a rational normalization would lift to the punctured plane and be constant. The lifted invariant branch has a linearized contracting return map: the displayed rho^2/abs(eta)<1 estimate gives convergence and derivative one. Diagonal coefficient comparison gives monomial branches and the weighted invariant field. The resonant Jordan recurrence forces w=0 and gives the field(nz,w). These are complete original arguments, not replaced by the frozen route.',
        'Pulling back the foliation gives a line subbundle away from its simple saddles. The regular blowup has saturated generator(u,-v); a saddle(bx,-ay) gives the two displayed weights(b,-a-b) and(a+b,-a), each zero ideal(u,v) of length one. Each blowup adds one saddle. Pulling back the transverse form gives epsilon=0 at a regular centre and epsilon=1 at a saddle. Thus K prime=mu^*K+E, V prime=mu^*V+epsilon*E, K^2=-k and KV-V^2=0. The postrelease original-foliation program verifies the full chart, iterate and polynomial identities.',
        'The original L->B=nu^*T_Y has no divisorial zero by generic conductor tangency and finiteness. Its local cokernel has depth at least one and hence no point torsion, so Q is torsionfree. Over the regular two-dimensional local ring Q** is free. Dualizing the column presentation and Q->Q** identifies Ext1(Q,O) with Ext2(Q**/Q,O); finite-length duality gives z0 at least the number k of saddle zeros. The saturated differential image E_B contains L generically as a subbundle; its quotient has no added divisor in Q**, giving c1(J)=R-V and quotient class K-R with length z1.',
        'The two exact sequences give (-K+V)^2-z0=(R-V)(K-R)+z1. With the preceding invariants this is G(R)=R^2-KR-VR=k+z0+z1>=2k. The actual blowup intersection form gives Delta G=-c^2+(1+epsilon)c for integral c. It is at most epsilon, and the initial Hopf value is zero. Hence G<=k, forcing k=z0=z1=0. The final conductor argument is the exact branch-intersection and finite-cover argument described above; it descends through the primary cover. Every original mathematical step and formula is preserved in v3.'
    ],
    primary_readings=[
        dict(url='https://stacks.math.columbia.edu/tag/00LX', root_web_ref='turn238576568view0', scope='Complete depth-lemma statement and proof read; applies to the analytic regular local rings directly.'),
        dict(url='https://stacks.math.columbia.edu/tag/00O7', root_web_ref='turn238576568view1', scope='Complete regular-local-module locus and proof read in the earlier full review.'),
        dict(url='https://stacks.math.columbia.edu/tag/0B3N', root_web_ref='turn238576568view2', scope='Complete dimension-at-most-two regular-local reflexive-module result and proof read; the citation is applied to finite modules over C{x,y}.'),
        dict(url='https://arxiv.org/pdf/2310.05265v2', edition='arXiv2310.05265v2,4December2023', sha256='7ec7b5917163b8d11ca97866b76a67aa81d3db5e3b1876b3abf9d4cbdb210383', bytes=377475, root_scope='Official PDF retrieved directly after web-tool DisabledError. Complete extracted p3 Definition1.3, general contraction and formula1; p5 Theorem2.1 and Remark2.2 read. No whole-paper or image-reading claim.')
    ],
    chronology='The failed initial rank argument and root sign diagnostic remain uncredited. The corrected complete finite-normalization derivation was frozen before release. The original proof, v2 alternate proposal, source opening and original-foliation computation were compared after release. The original two event identities were proposed at05:42:33UTC; their same-group comparison was extended by the final v3 reread at the recorded05:55:01UTC revision. Root review adds no event or independent group. The original event date is its initial occurrence; the v3 extension timestamp is explicitly retained in the event-proposal revision record and this review.',
    revision_decision='No original mathematical error was found. Under prompt4.2 the alternate v2 proof is kept as check evidence; its admission request is superseded. The printed proof retains all13 original mathematical steps, all15 displays and all118 inline math spans. Seven guards only change title/header, exact citations and wording. The paper Programs table receives the original_foliation row only. The alternate chern_modification program and output remain in code and check evidence, with no additional printed proof or computation claim.',
    program_scope='Both code/output pairs have been fully read. The prefreeze modification code and postrelease foliation code check bounded exact algebra only. No historical replay or whole-proof formal certificate is claimed. New program URLs follow the established publication convention and are not claimed live.',
    statement_conclusions_and_domains_preserved=True,
    mathematical_steps_changed=0,
    existing_displays_labels_and_tags_preserved=True,
    independent_required_owners=1,
    independent_evidence_groups=1,
    proposed_events=2,
    publication_page_reading_credit=0,
    evidence=[bind(index), ar['comparison'], ar['revision_decision'], ar['display_preservation'], ar['program_scope']]
)
(R / review).write_text(json.dumps(rd, indent=2) + '\n')
with (R.parent / 'S6_SERIES_GRIND_tags.tsv').open() as f:
    pages = {x['tag']: x['page'] for x in csv.DictReader(f, delimiter='\t')}
target = dict(owner=at['statement_owner'], tag=at['tag'], old_page=pages[at['tag']],
              original=at['full_original_block'], proposed=at['proposed_full_block'],
              freeze=at['freeze_receipt'], release=at['release_receipt'], events=ar['event_proposals'],
              who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, continuation2_A; reasoning effort not separately exposed',
              guards=[dict(old=g['literal_old'], new=g['literal_new'], type=','.join(g['defect_types']), reason=g['reason']) for g in proposal['guards']],
              scope='Smooth Hopf normalization: minimality, exact smooth elliptic conductor image, unramified component maps and Euler number zero.',
              event_note='Complete frozen/original/alternate/final comparison. Original13-step proof and all mathematics retained under prompt4.2. Final v3 extension time05:55:01UTC; original event identities and one evidence group retained. Seven editorial guards, no mathematical repair, no further independent credit.')
s = (R / 'S6_SERIES_PUBLISH_II.tex').read_text()
a = s.index('\\section*{Programs}')
b = s.index('\\end{longtable}', a)
last = s[s.rfind('\n', a, b - 1) + 1:b]
assert last.strip()
rows = (R / proposal['program_row_path']).read_text().splitlines(keepends=True)
assert len(rows) == 2 and 'original_foliation.py' in rows[1]
extra = dict(old=last, new=last + rows[1], type='D09,D18',
             reason='List once the exact algebra program for the calculations in the retained Hopf foliation proof. The separate modification proof remains check evidence.', location='Programs')
scope = read(ar['program_scope']['path'])
copies = [dict(**{'from': c['output']}, to='code/' + Path(c['output']['path']).name)
          for c in scope['new_computations']]
cfg = dict(batch=52, root_review_complete=True,
           source_before_sha256=bind('S6_SERIES_PUBLISH_II.tex')['sha256'],
           ledger_before_sha256=bind('CHECK_EVENTS.tsv')['sha256'],
           review_evidence=[bind(review), bind(index), ar['comparison'], ar['proposal'], ar['sources'], ar['program_scope'], ar['revision_decision'], ar['display_preservation']],
           targets=[target], additional_source_edits=[extra], code_copies=copies,
           mathematical_repairs=[],
           scope='02WW admitted after full frozen finite-normalization derivation, original thirteen-item foliation proof, alternate proposal and final v3 comparison. No original mathematical error found. All original proof steps and formulas remain; only seven exact title/header/citation/wording guards are admitted. The original-foliation program receives one Programs row; both exact algebra programs and outputs remain check evidence. Two event associations, one independent group, no publication-page or global defect closure credit.')
assert cfg['source_before_sha256'] == '9458a7b8e6bc85127326e9cab0f215809f200fb65617f509a3d8d032bbdbbaa5'
assert cfg['ledger_before_sha256'] == '5c00232c270800d4ce8cc10cc2e0764c39e69b2756c1551fb69b24e153695b6a'
out = 'records/S6_SERIES_PUBLISH_II_continuation2_batch52_config.json'
assert not (R / out).exists()
(R / out).write_text(json.dumps(cfg, indent=2) + '\n')
print(json.dumps(bind(out), indent=2))
