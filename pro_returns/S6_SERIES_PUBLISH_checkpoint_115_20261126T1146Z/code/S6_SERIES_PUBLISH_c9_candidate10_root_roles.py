"""Stage exact 02LU/Q30X name transports; canonical source is never written."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import csv
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
EXPECTED = '5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187'
OUT = ROOT / 'agents/continuation9_candidate10_root_roles'
TMP = ROOT.parents[1] / 'tmp/c9_candidate10_root_roles'
STEM = 'S6_SERIES_PUBLISH_c9_candidate10_root_roles'
REVIEW = 'agents/continuation9_candidate10_root_roles/' + STEM + '_review.md'
OWNERS = {
    '02LU': ('maps:src:D.2.52', r'\begin{theorem}[Height-integral fillings]', '432–437; global/named actual readers'),
    'Q30X': ('mapsIII:lem:fixed-conical-metrics', r'\begin{lemma}[Conical metrics and their induced slice forms]', '668–672; root actual reader'),
}
DEFECT_FIELDS = ['change_id','type','statement_id','old_location','old_page','new_location','new_page','old_text','new_text','reason','review_status']
EVENT_FIELDS = ['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group','publish_input_file','publish_input_row','date_utc','where']

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def write_tsv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        for row in rows:
            writer.writerow({k: str(row[k]).replace('\\','\\\\').replace('\t','\\t').replace('\n','\\n') if k in ('old_text','new_text') else row[k] for k in fields})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record-compared', action='store_true')
    args = parser.parse_args()
    source = SOURCE.read_text()
    assert sha(source) == EXPECTED and '\r' not in source
    scopes = {}
    for tag, (owner, marker, pages) in OWNERS.items():
        assert source.count(marker) == 1
        a = source.index(marker)
        b = source.index(r'\end{proof}', a) + len(r'\end{proof}')
        scopes[tag] = source[a:b] + '\n'
    rows = []

    def add(tag, start, end, substitutions, reason):
        scope = scopes[tag]
        assert scope.count(start) == 1 and scope.count(end) == 1, (tag,start,end)
        a = scope.index(start)
        b = scope.index(end,a) + len(end)
        old = scope[a:b]
        new = old
        for before, after, count in substitutions:
            assert new.count(before) == count, (tag,before,count,new.count(before))
            new = new.replace(before,after)
        assert old != new and source.count(old) == 1 and new not in source
        inverse = new
        for before,after,count in reversed(substitutions):
            assert inverse.count(after) == count, (tag,after,inverse.count(after),count)
            inverse = inverse.replace(after,before)
        assert inverse == old
        owner,_,pages = OWNERS[tag]
        rows.append(dict(change_id=f'III-C9-CURRENT10-{tag}-ROOT-ROLE-{sum(r["statement_id"]==owner for r in rows)+1:02d}',type='D20',statement_id=owner,
            old_location=f'Complete {tag} owner; source line {source[:source.index(old)].count(chr(10))+1}',old_page=pages,
            new_location='Same complete construction, selected values, maps and inverses',new_page='pending accepted successor and actual changed-image reading',
            old_text=old,new_text=new,reason=reason,
            review_status='proposed; exact identity name transport; canonical source unchanged; complete proposed-proof reading and root admission recorded separately'))

    add('02LU','Let $B,g$ be the marked elliptic monodromy and cocycle of $G$,','The component order divides $d_0$, so $abz_G$ is integral.',[
        ('$B,g$','$B,g_{\\rm ell}$',1),
        ('=g$', '=g_{\\rm ell}$',1),
        ('ag^{\\mathsf t}', 'ag_{\\rm ell}^{\\mathsf t}',1)],
        'The selected elliptic cocycle is carried by the identity g_ell=g with inverse g=g_ell; its equation (B-I)z_G=g and the exact line row -a g^t J B are unchanged. The later free cokernel rank retains its own explicit g binding.')
    add('02LU','For an invariant orbit divisor $E$,','on the complement of the zeros and poles of $\\sigma_E$.',[
        ('divisor $E$','divisor $E_{\\rm orb}$',1),
        ('\\sigma_E','\\sigma_{E_{\\rm orb}}',4)],
        'Assign E_orb the original invariant orbit divisor and carry the same canonical section through multiplication, reciprocal division and the exact arrow ratio. Reversing the name assignment recovers every original divisor/section map.')
    add('02LU','For the unit-circle return $\\phi$, write','$\\mathcal T(\\phi)=(E\\times[0,1])/((x,1)\\sim(\\phi x,0))$.',[
        ('For the unit-circle return $\\phi$, write','For the unit-circle return $\\phi$, write $E_{\\rm circ}$ for its\ncircle-bundle fibre and put',1),
        ('=(E\\times','=(E_{\\rm circ}\\times',1)],
        'E_circ names exactly the circle-bundle fibre of the imported original cap. The mapping-torus relation, return-inversion map j and inverse j^-1 remain the same on each original point; the name transport and inverse are identities on that fibre.')
    add('02LU','The CRT coordinate map is','$\\sum_i M_it_i a_i\\bmod d_0$.',[
        ('M_i','M_{i,\\rm CRT}',3),('t_i','t_{i,\\rm CRT}',2)],
        'The selected CRT integers and inverse coefficients retain M_i=d0/n_i and M_i t_i=1 mod n_i. Qualify both families, including every term of the reconstruction; the residue map and reconstruction remain inverse. These are exact old-value/new-name identities.')
    add('02LU','The vertical normal closure is a terminating','quotient within the full fundamental-group presentation.',[
        ('$V=','$V_{\\rm vert}=',1),
        ('M_i','M_{i,\\rm vert}',6),
        ('|_V','|_{V_{\\rm vert}}',1),
        ('M_w','M_{w,\\rm vert}',1)],
        'V_vert is the original marked vertical lattice and M_i,vert is the original restriction T_i|V_vert. The same ordered word gives M_w,vert. Preserve the full ascending-lattice recurrence, characteristic polynomial, Cayley-Hamilton inverse, conjugate-word map and exponent-reading inverse; undoing the names recovers the entire block.')
    add('02LU','Let $\\mathcal B$ be the complete fibre-and-graph relation','every torsion factor of a nonsaturated local kernel.',[
        ('matrix. Keep the Smith transformations','matrix. Write $e_{j,\\rm in}$ and $e_{j,\\rm out}$ for the standard\ncolumns in its domain and codomain, respectively. Keep the Smith transformations',1),
        ('$U\\mathcal B V=\\Delta$','$U_{\\rm SNF}\\mathcal B V_{\\rm SNF}=\\Delta$',1),
        ('U^{-1}','U_{\\rm SNF}^{-1}',2),
        ('\\mathcal B V e_j','\\mathcal B V_{\\rm SNF} e_j',1),
        ('reads $U$','reads $U_{\\rm SNF}$',1),
        ('U_{\\rm SNF}^{-1}e_j','U_{\\rm SNF}^{-1}e_{j,\\rm out}',2),
        ('V_{\\rm SNF} e_j','V_{\\rm SNF} e_{j,\\rm in}',1)],
        'U_SNF and V_SNF are the identical two selected Smith transformations. The standard input and output columns now carry their actual domains: each coefficient insertion and its coefficient-reading inverse is unchanged. The quotient basis U^-1 e_j,out, exact relation B V e_j,in=Delta_jj U^-1 e_j,out and inverse coordinate U times the represented cycle are unchanged under these identity assignments.')
    add('02LU','At least one weight is positive, since $ab/d_0>0$.','This also\ncomputes the Euler-zero cases.',[
        ('result $E$','result $E_{\\rm ext}$',1),
        ('H_1(E)','H_1(E_{\\rm ext})',2),
        ('b_1(E)','b_1(E_{\\rm ext})',1),
        ('basis matrix $P$','basis matrix $P_{\\rm rel}$',1),
        ('matrix $M$ and solve $Mz=Pz\'$',"matrix $M_{\\rm disc}$ and solve $M_{\\rm disc}z_{\\rm disc}=P_{\\rm rel}z_{\\rm rel}$",1),
        ("Projection to $z$ has inverse recovering the unique $z'$","Projection to $z_{\\rm disc}$ has inverse recovering the unique $z_{\\rm rel}$",1),
        ('because $P$ is injective','because $P_{\\rm rel}$ is injective',1),
        ('\\mathbb Z^g\\oplus T$','\\mathbb Z^g\\oplus T_{\\rm tor}$',1),
        ('with $T,T_{H_1}$ finite.','with $T_{\\rm tor},T_{H_1}$ finite.',1),
        ('\\mathbb Z^{b_2}\\oplus T\\\\','\\mathbb Z^{b_2}\\oplus T_{\\rm tor}\\\\',1),
        ('\\mathbb Z^{b_3}\\oplus T\\\\','\\mathbb Z^{b_3}\\oplus T_{\\rm tor}\\\\',1),
        ('\\xrightarrow{d}','\\xrightarrow{d_{\\rm tor}}',1),
        ('modulo $d$','modulo $d_{\\rm tor}$',1)],
        'E_ext is the identical partially filled exterior, with unchanged root-disc injection and peripheral coefficient inverse. P_rel and M_disc are the original injective relation basis and lifted disc map; (z_disc,z_rel)=(z,z\') is the coordinate identity on their integer kernel, with the same unique recovery and closed-cycle splitting. T_tor is the identical finite summand of cokerB and retains both appearances in the homology table; the earlier local monodromy T remains unchanged. The torsion resolution uses the identical diagonal entry d_tor=d and residue inverse. Every rank, group, integer and pair-sequence map is preserved.')

    add('02LU','Its local coefficient\ncolumn $z$ is the present column $d$,','orbit-constant lattice, with its representative-coordinate inverse.',[
        ('Thus the identity coordinate maps','Write $\\varepsilon_j$ for the same ordered component basis.\nThus the identity coordinate maps',1),
        ('e_p','\\varepsilon_p',1),('e_0','\\varepsilon_0',1)],
        'The ordered component basis is unchanged under epsilon_j=e_j; coefficient insertion and reading are inverse. The component-column identity from02LS, C(I-S)d equation and its -I inverse retain the same entries. The physical elliptic basis e_1,e_2 remains unchanged.')
    add('02LU','For a normal image $(x,t)$','as in \\eqref{maps:eq:IC_local_46}; it includes every frame prism.',[
        ('$y=','$y_{\\rm pr}=',1),('0,y+','0,y_{\\rm pr}+',1),
        ('\\mathsf t}y)','\\mathsf t}y_{\\rm pr})',1)],
        'The selected normal-prism vector is exactly y_pr=Kx. On the displayed Rx=0 domain A0 Kx=x, so A0 is its coefficient inverse on imK. The complete chain d3(0,Kx+(t-c^tKx)eta)=(x,t) is unchanged; reverse the name to recover every original byte.')
    add('02LU','For the affine $D_5,D_7$ diagrams','Each original cap keeps its own supplied line and extending frame.',[
        ('They give the actual divisor','Use $\\varepsilon_i^{\\rm ch}$ and $\\varepsilon_i^{\\rm out}$ for the ordered\ncomponent columns in these two markings; the index-permutation matrices\nand their transposes give the inverse changes. They give the actual divisor',1),
        ('e_0','\\varepsilon_0^{\\rm ch}',3),('e_1','\\varepsilon_1^{\\rm ch}',3),
        ('e_2','\\varepsilon_2^{\\rm ch}',1),('e_4','\\varepsilon_4^{\\rm out}',1),
        ('\\eta','\\eta_{\\rm st}',1)],
        'Carry the identical component basis through the original chain/outer-first index maps and their inverses. The special odd-star choice eta_st=-epsilon_4^out retains its original selected vector and h=1 calculation; the general eta in the normal bounding chain keeps its original binding. The section, degree, divisor and inverse line multipliers are unchanged.')
    add('02LU','The algorithm forms $C(I-S)d$','it uses its given extending frame and the original\nmaps of \\ref{maps:src:D.2.46}.',[
        ('e_p','\\varepsilon_p',1),('e_0','\\varepsilon_0',1)],
        'The final component-equation caller uses the same qualified standard columns introduced at the start of02LU. Their coordinate identity and inverse preserve C(I-S)d, the degree/orbit computation, each admissible cap and its given frame.')
    add('02LU','At an uncorrected multiplicative site,','be fixed by the component translation.',[
        ('e_p','\\varepsilon_p',1),('e_0','\\varepsilon_0',1)],
        'The multiplicative component-class argument evaluates the same ordered component-basis family at that actual cap. Qualifying both columns preserves their coefficients, the unique negative entry, the component permutation and the resulting unchanged-cap identification.')

    add('Q30X','If \\(d_P(x,F)=\\delta>0\\),','\\(2(\\delta-\\eta)>2\\eta\\).',[
        ('\\delta','\\delta_{\\rm dist}',3)],
        'The qualified distance is exactly delta_dist=d_P(x,F), the original positive quotient-distance evaluation. The identity delta_dist=delta and its inverse preserve the same ball radius, both distance bounds and the local-isometry argument.')
    add('Q30X','keep \\(u=0\\) and take character-angle endpoints',' 2r_T\\sin(\\delta/2)<r_T\\delta.',[
        ('\\delta','\\delta_{\\rm ang}',5)],
        'The qualified angle is exactly the original selected character-angle separation. Preserve its interval, the same polar sector map, chord radius range, chord length and intrinsic arc length; the inverse name assignment recovers every old formula.')

    candidate = source
    for row in rows:
        assert candidate.count(row['old_text']) == 1
        candidate = candidate.replace(row['old_text'],row['new_text'],1)
        assert candidate.count(row['new_text']) == 1
    reverse = candidate
    for row in reversed(rows):
        reverse = reverse.replace(row['new_text'],row['old_text'],1)
    assert reverse == source
    tokens = r'\\(?:label|hypertarget|(?:c|C|eq|Series)?ref|cite)\{[^}]+\}|\\(?:begin|end)\{[^}]+\}|\\mathbb\{[^}]+\}'
    assert re.findall(tokens,source) == re.findall(tokens,candidate)
    assert re.findall(r'\d+',source) == re.findall(r'\d+',candidate)
    assert sha(SOURCE.read_text()) == EXPECTED
    OUT.mkdir(exist_ok=True)
    TMP.mkdir(exist_ok=True)
    scoped = {}
    for tag,(owner,marker,_) in OWNERS.items():
        a = candidate.index(marker)
        b = candidate.index(r'\end{proof}',a) + len(r'\end{proof}')
        proposed = candidate[a:b] + '\n'
        recovered = proposed
        for row in reversed([r for r in rows if r['statement_id']==owner]):
            assert recovered.count(row['new_text']) == 1
            recovered = recovered.replace(row['new_text'],row['old_text'],1)
        assert recovered == scopes[tag]
        original_path = TMP / f'{STEM}_{tag}_original.tex'
        proposed_path = TMP / f'{STEM}_{tag}_proposed.tex'
        original_path.write_text(scopes[tag],newline='\n')
        proposed_path.write_text(proposed,newline='\n')
        scoped[tag] = dict(statement_id=owner,original_lines=len(scopes[tag].splitlines()),proposed_lines=len(proposed.splitlines()),original_sha256=sha(scopes[tag]),proposed_sha256=sha(proposed),original_path=str(original_path),proposed_path=str(proposed_path))
    payload = dict(source_file=SOURCE.name,source_sha256=EXPECTED,proposed_source_sha256=sha(candidate),owner_scopes=scoped,proposals=rows)
    (OUT / (STEM+'.json')).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',newline='\n')
    write_tsv(OUT / (STEM+'_defects.tsv'),DEFECT_FIELDS,rows)
    (OUT / (STEM+'.diff')).write_text(''.join(difflib.unified_diff(source.splitlines(keepends=True),candidate.splitlines(keepends=True),fromfile='current10/'+SOURCE.name,tofile='proposed_root_roles/'+SOURCE.name,n=4)),newline='\n')
    if args.record_compared:
        review = (ROOT / REVIEW).read_text()
        assert 'Complete original/proposed readings finished' in review
        assert all(data['proposed_sha256'] in review for data in scoped.values())
        now = datetime.now(timezone.utc).isoformat()
        events = []
        for tag,(owner,_,pages) in OWNERS.items():
            group = f'publish:c9:III:{tag}:current10-root-role-comparison'
            events.append(dict(statement_id=owner,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine',type='used and rechecked in this run',outcome=f'Root read the complete current {tag} statement/proof and complete proposed scope, all exact differences and every actual direct caller context. Rechecked the identity name assignments, all affected forward/inverse maps, and all retained formal-input domains and evaluations documented in {REVIEW}. Full-source and complete-owner inverses recover every original byte; ordered numerical and permanent-identifier sequences are unchanged. This is exposed source comparison following the attributed current10 image findings; no independent derivation, new computation or additional image credit. Canonical admission and successor images remain pending.',event_id=group,phase='publication continuation9',source_file=SOURCE.name,source_row=f'{tag} complete owner and exact guarded roles',source_event_type='used and rechecked in this run',evidence_group=group,publish_input_file='../CLAUDE_READING_LOG_PAPER_III.md',publish_input_row='P15; prompt0.8 complete proof scope; actual current10 pages '+pages,date_utc=now,where=f'code/{STEM}.py; code/{STEM}.out; {REVIEW}; agents/continuation9_candidate10_root_roles/{STEM}_defects.tsv'))
        write_tsv(OUT / (STEM+'_events.tsv'),EVENT_FIELDS,events)
        print('Two exposed comparison events staged after the complete readback record; no canonical event written.')
    print(json.dumps({k:v for k,v in payload.items() if k!='proposals'},indent=2))
    print('Exact guard rows',len(rows))
    print('Whole-source and both complete-owner literal inverses: PASS')
    print('All ordered numbers, labels, targets, references, citations, environments and blackboard domains: unchanged')
    print('Canonical source/status/counts/defects/events unchanged; actual successor images remain pending.')

if __name__ == '__main__':
    main()
