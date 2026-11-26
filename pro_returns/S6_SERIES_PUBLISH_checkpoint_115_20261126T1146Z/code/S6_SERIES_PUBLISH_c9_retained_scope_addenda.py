#!/usr/bin/env python3
"""Exact P15 addenda for already-read 02LC, 02LJ and 02S9 proofs.

Only proposals are written. Each complete baseline is the previously reviewed
and admitted candidate; both full-scope and complete-source reverses are checked.
"""
from pathlib import Path
import csv
from datetime import datetime, timezone
import difflib
import hashlib
import re
from S6_SERIES_PUBLISH_c9_backend_notation import Packet, sha

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents' / 'continuation9_retained_scopes'
TMP = ROOT.parents[1] / 'tmp' / 'c9_retained_scopes'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source_bytes = SOURCE.read_bytes()
source = source_bytes.decode()
packets = []

p = Packet('02LC', 'maps:src:D.2.36',
           'dc0bf6ca6667c65eb7ac9008c677f5864cc371e3653e1bdf8d491ffd17e148f4',
           '445–457', 'Retained-role reassessment after complete proof and actual-page reading.')
p.scope('upright-cap-choice-labels',
        'The divisor and component calculation gives the complete table below.',
        'There are $36$ patterns',
        p.literals([
            ('evaluation below. An original and a finite\nchoice at the same site are separate patterns.',
             'evaluation below. The cap labels $\\mathrm O$ and $\\mathrm F$\nmean original and finite choices, respectively; those choices\nat the same site are separate patterns.', 1),
            ('&O&', r'&\mathrm O&', 12), ('&F&', r'&\mathrm F&', 12)]),
        'The upright cap labels O and F retain exactly the original and finite options in the same twelve rows each. The identity on each site option, with the same site label and parameter values, gives both directions of the comparison. Every numeric table entry and all thirty-six patterns are preserved. The italic lifted line return F remains the same map with its displayed inverse.')
p.scope('fixed-curve-and-thom-maps',
        'For a fixed curve with normal characters', 'Localization now gives',
        p.literals([
            ('For a fixed curve with normal characters', 'For a fixed curve $F_{\\rm fix}$ with normal characters', 1),
            ('e_F', r'e_{F_{\rm fix}}', 5),
            ('i_F^*', r'i_{F_{\rm fix}}^*', 1),
            ('i_{F*}', r'i_{F_{\rm fix}*}', 1),
            ('|_F', r'|_{F_{\rm fix}}', 1)]),
        'F_fix is the same generic fixed component, specialized to the actual rational curve C or elliptic curve E. Identity on that component preserves its inclusion i_F, normal bundle, ordered characters and roots. The Euler class and both Thom maps are renamed together: i_Ffix^* i_Ffix,* is still multiplication by e_Ffix. The two concrete inverse summands i_C*(z_C/e_C) and i_E*(z_E/e_E), their orientations and the Pontryagin-root identity are unchanged. The bare F continues to denote the lifted line return.')
p.exact('bordism-representative',
        r'''The refined-class map in Theorem~\ref{maps:src:D.1.11} is, for
a group $A$ without two-torsion,
\[
 P_A([N,f])=\tfrac14 f_*(\operatorname{PD}_Np_1(TN)).
\]''',
        r'''The refined-class map in Theorem~\ref{maps:src:D.1.11}, for
a group $A$ without two-torsion, evaluates on the marked
spin-bordism representative $[N_{\rm bord},f_{\rm bord}]$ as
\[
 P_A([N_{\rm bord},f_{\rm bord}])
   =\tfrac14 (f_{\rm bord})_*(\operatorname{PD}_{N_{\rm bord}}p_1(TN_{\rm bord})).
\]''',
        'N_bord=N is the same closed spin representative and f_bord=f the same marked map to K(A,2). Identity on the manifold and equality of the maps preserve its tangent bundle, orientation, Poincare dual and pushforward, so the refined class is unchanged. The nodal pairing integer N=a nu_i/d_0^2, the nodal subscripts and the physical gauges keep their existing values and formulas.')
p.exact('bordism-fundamental-class-map',
        r' h([N,f])=f_*[N],',
        r' h([N_{\rm bord},f_{\rm bord}])=(f_{\rm bord})_*[N_{\rm bord}],',
        'This uses the same N_bord,f_bord representative as the refined-class formula, with coefficient group Z/p. Identity of its fundamental class and marking preserves h and the joint map (P,h); every injectivity and recognition assertion is unchanged.')
p.scope('classification-diffeomorphism',
        'injective. The marked Theorem~3 on p.~795,', 'For two zero classes',
        p.literals([("$F:X\\to X'$", "$F_{\\rm dif}:X\\to X'$", 1),
                    ('F_*', r'(F_{\rm dif})_*', 2),
                    ('F^{-1}', r'F_{\rm dif}^{-1}', 1)]),
        'F_dif=F is exactly the same orientation-preserving classification diffeomorphism X to X-prime. Its forward and inverse maps on the marked generator retain the ratios P_Xprime/P_X and P_X/P_Xprime; their composites are identity. Its marking equation is unchanged. The actual lifted line return F with its three coordinate components and reciprocal inverse keeps its own name.')
packets.append(p)

p = Packet('02LJ', 'maps:src:D.2.42',
           'cc27a7dbf4c99f34d019e32020d60e659617360b7bc8a012d218094b597a82ae',
           '484–500', 'Retained-role reassessment after complete proof and actual-page reading.')
p.exact('finite-site-index-set',
        r'''Finite orders
at different sites are pairwise coprime for a simply connected threefold,
and
\begin{equation}
                    c=b/\prod_{i\in F}q_i.''',
        r'''Finite orders
at different sites are pairwise coprime for a simply connected threefold.
Writing $\mathcal I_{\rm fin}$ for the set of finite additive sites gives
\begin{equation}
                    c=b/\prod_{i\in\mathcal I_{\rm fin}}q_i.''',
        'I_fin is exactly the finite additive site set formerly used as F in this product. The preceding paragraph gives each site its unchanged vertical index q_i. Identity on the site labels reindexes the same finite product, with inverse the identity; the integer c and fourteen-pattern selection are unchanged. This gives the index set a distinct printed name from the finite central surface and lifted line return.')
p.scope('finite-central-surface',
        'To check their integral scope, the finite central surface has',
        'There is at most one finite cap.',
        p.literals([
            ('the finite central surface has', 'the finite central surface \\(F_{\\rm fin}\\) has', 1),
            ('H_1(F)', r'H_1(F_{\rm fin})', 2),
            (r'H^2(F;\mathbb Z)', r'H^2(F_{\rm fin};\mathbb Z)', 1)]),
        'F_fin=F is the same finite central surface whose group has generators beta_0,ell,c_0 and relation m c_0=n ell+r q beta_0. Identity of that surface and its covering map preserves both Bezout basis substitutions, all Betti numbers, integral duality and the normal Chern class. The transfer sectors and full Thom subgroup retain their original maps and inverse chains. The actual lifted line return F remains unchanged.')
p.scope('two-primary-fixed-curve',
        r'For \(C_2\), the normal representation', r'On \(E_2\),',
        p.literals([
            ('on each fixed curve is complex', 'on each fixed curve \\(F_{\\rm fix}\\) is complex', 1),
            ('e_F', r'e_{F_{\rm fix}}', 1),
            (r'\nu_F', r'\nu_{F_{\rm fix}}', 3),
            ('TF)', r'TF_{\rm fix})', 1)]),
        'F_fix names the same fixed curve of the displayed C_2 action. Identity of its embedding preserves the tangent and normal bundles, complex orientations and sign characters. The two normal Chern classes and equivariant Euler class have the same values, and the Thom restriction and inverse remain the existing maps. The finite central surface F_fin and lifted line map F keep their separate objects.')
p.exact('odd-primary-fixed-curve-binding',
        r'''For \(p=3,5\), let the ordinary roots of the two normal eigenlines at
a fixed curve be \(x_1,x_2\), and their characters be \(\lambda,-\lambda\).''',
        r'''For \(p=3,5\), let the ordinary roots of the two normal eigenlines at
a fixed curve \(F_{\rm fix}\) be \(x_1,x_2\), and their characters be \(\lambda,-\lambda\).''',
        'Here F_fix is the same formal fixed-component argument for the indicated prime p, with its two existing normal eigenlines and ordered roots. Identity on that component preserves the restriction of TX and the normal Euler class used immediately below; the argument ranges over the same actual fixed components.')
p.exact('odd-primary-pontryagin-restriction',
        r'                         p_1(TX)|F=-2e_F.',
        r'                         p_1(TX)|F_{\rm fix}=-2e_{F_{\rm fix}}.',
        'The restriction is along the identical inclusion of the now explicitly named F_fix. Its normal Euler class is the same product of the two displayed roots; both sides still equal 2 lambda^2 t_p^2+2 lambda t_p(x_1-x_2). The actual root expansion, localization formula and marked refined coordinate retain every coefficient.')
packets.append(p)

p = Packet('02S9', 'night:P3F.32',
           'c94e773ba0222422471d823efd4650eebf4b0d91a7019a71a30f596311757dab',
           '578–583', 'Retained-role reassessment after complete proof reading; actual images belong to root.',
           image_reader='root')
p.scope('cap-angle-coefficient',
        r'For \(d=0\), let a be', 'At the cusp choose m norm shells',
        p.literals([
            ('let a be', r'let \(a_{\rm cap}\) be', 1),
            (r'2\pi ia', r'2\pi i a_{\rm cap}', 3),
            (r'2\pi ima', r'2\pi i m a_{\rm cap}', 1),
            ('Translation of a', r'Translation of \(a_{\rm cap}\)', 1),
            (r'\(ma=0\pmod1\)', r'\(m a_{\rm cap}=0\pmod1\)', 1),
            ('the same a translation', r'the same \(a_{\rm cap}\) translation', 1)]),
        'a_cap=a is the identical real coefficient along ell_0=e_gamma-e_u. The identity on that coefficient leaves S=sigma exp(2pi i a_cap), B=exp(2pi i m a_cap), t=S^m/B and both inverse root formulas unchanged pointwise. The same m root choices form the deck orbit, the same equation selects the m levels and the same angular collar translation is used. The ordered graph cochain a imported later retains its twelve-handle values and the equation b_old=2a.')
p.exact('radial-norm-logarithm',
        r'''For any other admissible norm the positive ratio is \(e^f\);
the interpolation \(e^{sf}\) and its reciprocal give the
source-preserving radial isotopy.''',
        r'''For any other admissible norm the positive ratio is \(e^{f_{\rm norm}}\);
the interpolation \(e^{s f_{\rm norm}}\) and its reciprocal give the
source-preserving radial isotopy.''',
        'f_norm is the same real logarithm of the positive norm ratio. The real exponential and logarithm are inverse, so f_norm=f pointwise and every interpolation factor and reciprocal is identical. This actual radial comparison function now has its own name throughout its two uses; all source-preserving maps and parameter bounds remain unchanged.')
p.scope('source-cubic-inversion-function',
        r'On a regular or type-II source fibre put \(f=x-t^2\).',
        r'At the \(I_2\) cusp',
        p.literals([
            (r'\(f=x-t^2\)', r'\(f_{\rm inv}=x-t^2\)', 1),
            (r'\operatorname{div}(f)', r'\operatorname{div}(f_{\rm inv})', 1),
            ('these sections are smooth and f\n', r'these sections are smooth and \(f_{\rm inv}\)'+'\n', 1),
            ('f(p)', r'f_{\rm inv}(p)', 3),
            ('f(-p)', r'f_{\rm inv}(-p)', 1)]),
        'f_inv=f=x-t^2 is the same rational function on the same regular or type-II source fibre. Its divisor G+(-G)-2O and equality f_inv(-p)=f_inv(p) are unchanged. The pairing sends s_D(p) tensor s_D(-p) to the same value, and the reciprocal line map sends a s_D(p) to the same (a f_inv(p))^(-1)s_D(-p); applying it twice is identity by the displayed evenness. The scalar a here is the formal argument of that line map. The final return diffeomorphism f and its isotopy f_t retain their actual point maps and mapping-torus composites.')
p.exact('return-name-math-mode',
        'An isotopy \\(f_t\\) from the identity to the return f,',
        'An isotopy \\(f_t\\) from the identity to the return \\(f\\),',
        'The final return retains the symbol f and the same isotopy f_t, endpoint arrows and mapping-torus identification. Printing its existing name in math mode binds it visibly to f(z) in the following quotient convention; no map or parameter changes.')
packets.append(p)

OUT.mkdir(exist_ok=True)
TMP.mkdir(exist_ok=True)
rows = []
events = []
stamp = datetime.now(timezone.utc).isoformat()
with (ROOT / 'CHECK_EVENTS.tsv').open(newline='') as handle:
    event_fields = next(csv.reader(handle, delimiter='\t'))
for p in packets:
    back = p.new
    for op in reversed(p.operations):
        assert back.count(op['new']) == 1, (p.tag,op['name'],'inverse')
        back = back.replace(op['new'],op['old'],1)
    assert back == p.old
    for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',
                    r'\\(?:[A-Za-z]*ref|cite[A-Za-z]*)\*?(?:\[[^]]*\])?\{[^}]+\}', r'\d+']:
        assert re.findall(pattern,p.old)==re.findall(pattern,p.new),(p.tag,pattern)
    for number,op in enumerate(p.operations,1):
        assert source.count(op['old'])==1,(p.tag,op['name'],'canonical old guard')
        row=dict(change_id=f'CLAUDE-III-C9-P15-RETAINED-{p.tag}-{number:03}',type='D20',
                 statement_id=p.sid,old_location=f'{p.tag}, retained-role scope {op["name"]}',
                 old_page=f'candidate02 physical {p.pages}',new_location='same complete theorem and proof',
                 new_page='pending rebuilt image review',old_text=op['old'],new_text=op['new'],
                 reason=op['reason'],review_status='Complete prior proof reading and current bounded-role reassessment; full original/proposed scope and all exact differences compared. Reversing every change recovers the baseline bytes. Root admission and rebuilt image review pending.')
        rows.append(row)
    (OUT / f'S6_SERIES_PUBLISH_c9_retained_{p.tag}.diff').write_text(''.join(
        difflib.unified_diff(p.old.splitlines(True),p.new.splitlines(True),
                            fromfile=p.tag+' admitted baseline',tofile=p.tag+' retained-role proposal',n=5)))
    (TMP / f'S6_SERIES_PUBLISH_c9_retained_{p.tag}_proposed.tex').write_text(p.new)
    event_id=f'publish:c9:III:{p.tag}:retained-role-readback'
    event={key:'' for key in event_fields}
    event.update(statement_id=p.sid,date='2026-11-26',
                 who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine',
                 type='used and rechecked in this run',
                 outcome=f'After the already recorded complete {len(p.old.splitlines())}-line proof reading, reread and compared the concrete retained naming roles required by prompt0.8. Prepared {len(p.operations)} exact reversible source fragments: '+', '.join(op['name'] for op in p.operations)+'. Identity maps on the same objects, complete affected-use counts, original inverse formulas and all assertions are preserved; the complete proposed proof reverses to the admitted baseline byte for byte. This is an exposed source-use readback, with no additional page-reading or independent-proof credit. Root admission and changed-page reading remain pending.',
                 event_id=event_id,phase='publication continuation 9',source_file='S6_SERIES_PUBLISH_III.tex',
                 source_row=f'{p.tag}: concrete retained roles in its complete proof',
                 source_event_type='used and rechecked in this run',evidence_group=event_id,
                 publish_input_file='../CLAUDE_READING_LOG_PAPER_III.md',
                 publish_input_row='P15; prompt0.8 whole-proof scope',date_utc=stamp,
                 where='code/S6_SERIES_PUBLISH_c9_retained_scope_addenda.py; agents/continuation9_retained_scopes/')
    events.append(event)
    print(p.tag,'baseline',len(p.old.splitlines()),sha(p.old),'candidate',len(p.new.splitlines()),sha(p.new))
    for op in p.operations:
        print(' ',op['name'])
        for count,old,new in op['details']:
            print('  count',count,repr(old),'->',repr(new))

forward=source
for row in rows:
    assert forward.count(row['old_text'])==1
    forward=forward.replace(row['old_text'],row['new_text'],1)
for row in reversed(rows):
    assert forward.count(row['new_text'])==1,(row['change_id'],'full new guard')
    forward=forward.replace(row['new_text'],row['old_text'],1)
assert forward==source
assert SOURCE.read_bytes()==source_bytes
for name,items,fields in [('S6_SERIES_PUBLISH_c9_retained_scope_defects.tsv',rows,list(rows[0])),
                          ('S6_SERIES_PUBLISH_c9_retained_scope_CHECK_EVENTS.tsv',events,event_fields)]:
    with (OUT/name).open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields,delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(items)
print(len(rows),'D20 fragments;',len(events),'used-only events; complete scope/full-source reverses, numeric literals and permanent identifiers passed. Canonical files unchanged.')
