#!/usr/bin/env python3
"""Reconcile concrete 02LD retention cases against the actual current source."""
from pathlib import Path
import csv
import json
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
p=ScopedReview(source, r'\begin{theorem}[Weighted natural profiles]',
    r'\begin{remark}[Finite weighted-profile calculations]',
    '02LD','maps:src:D.2.37','338–358',
    'Used and rechecked in this run after exposure. Current complete affected cap, component-permutation, attachment and enumeration contexts reread against the earlier full-proof review. All final differences, exact maps and inverses compared. Scoped/full-source reversal, numeric literals, labels and targets checked. No independent proof credit; admission and changed rendering pending.')
assert r'[p(t)]\mapsto[p(t_{\rm cyc})]' in p.old

p.edit('orbit length dividing $q$. Choose a positive $E$ such that',
       r'At a multiplicative site \(I_\nu\)',
       lambda t: math_letters(t, {'E':r'E_{\rm perm}'}).replace(
           r'^E_{\rm perm}',r'^{E_{\rm perm}}'),
       'Name the positive inverse exponent E_perm. It is the identical integer with E_perm d congruent to one modulo q; all permutation powers, index bijections and integral relation-subgroup identities use the same exponent. The reverse name assignment is its inverse.',
       [r'E_{\rm perm}'])

def additive(t):
    t=t.replace(r'\beta_0',r'\beta_{0,\rm add}').replace('k_d',r'k_{d,\rm add}')
    t=t.replace(r'\(c=C_p^*-C_0^*\)',r'\(c_{\rm Ch}=C_p^*-C_0^*\)')
    t=t.replace(r'\ker(c:',r'\ker(c_{\rm Ch}:')
    return t

p.edit(r'\emph{Nonzero-Chern original additive caps.}',
       r'\emph{Multiplicative caps with nonzero Chern class.}',additive,
       'Qualify the additive period vector beta_{0,add} and its primitive mixed class k_{d,add}; they are exactly the displayed B_d(v_0,0) and its wedge with ell_d. The integral section, forgetful map, area coefficient -db/q, sign-reversal inverse and complete kernel columns retain the same vectors. The Chern functional c_Ch is the identical C_p^*-C_0^* row and kernel, distinguished from the later core generator c.',
       [r'\beta_{0,\rm add}',r'k_{d,\rm add}',r'c_{\rm Ch}'])
p.edit(r'\emph{Multiplicative caps with nonzero Chern class.}',
       r'\emph{Zero-Chern multiplicative caps and all rank-one models.}',
       lambda t:t.replace(r'\beta_0',r'\beta_{0,\rm mult}').replace('k_d',r'k_{d,\rm mult}'),
       'Qualify the multiplicative period vector beta_{0,mult} and its class k_{d,mult}. The vector xu+z delta, unit equation, unimodular basis and inverse short matrix are unchanged. Its mixed class, Gysin projection, zero original-cap image, coefficient -db/nu and all normal-kernel columns remain identical.',
       [r'\beta_{0,\rm mult}',r'k_{d,\rm mult}'])
p.exact(r'the additive value \(\omega_d(k_d)=-db/q\) and the multiplicative value \(\omega_d(k_d)=-db/\nu\).',
        r'the additive value \(\omega_d(k_{d,\rm add})=-db/q\) and the multiplicative value \(\omega_d(k_{d,\rm mult})=-db/\nu\).',
        'Propagate both qualified mixed classes into the explicit global-column summary, preserving the two existing area values and the same positive sign-reversal generators.',
        [r'k_{d,\rm add}',r'k_{d,\rm mult}'])
def attached(t):
    t=math_letters(t,{'E':r'E_{\rm att}'})
    # The full exact sequence uses an equation environment, so retain
    # its actual codomain explicitly as well as the inline groups.
    return t.replace('H_1(E)',r'H_1(E_{\rm att})').replace('H_2(E)',r'H_2(E_{\rm att})')


p.edit('Attach the $k$ finite or regular logarithmic caps to $V$ and call the',
       r'\emph{The full group, the unrestricted ranks, and every homology group.}',
       attached,
       'Name the partially filled exterior E_att, retaining E_perm for the inverse integer and E(M) for the circle-bundle construction. Identity on the same attached space preserves every H_1/H_2 group, boundary inclusion, Thom quotient, component-disc map, integer kernel algorithm and explicit splitting inverse.',
       [r'E_{\rm att}'])
p.edit('At a nonzero-Chern multiplicative site, the primitive',
       'At an additive site the original',
       lambda t:t.replace('k_d',r'k_{d,\rm mult}'),
       'Propagate the multiplicative class k_{d,mult} into its original-versus-Mumford comparison. It is the same primitive class with coefficient -db/nu; both cap images and the asserted marked-kernel difference are unchanged.',
       [r'k_{d,\rm mult}'])
p.edit('Here $R$ is the natural-row count,',
       r'\begin{center}',
       lambda t:math_letters(t,{x:r'\mathrm '+x for x in 'RKPSA'}),
       'Print the five count labels upright in their prose definition, matching the already upright table headers. Each label denotes exactly the same count and same column; the label bijection and inverse preserve every enumerated number. This distinguishes them from the finite operator R, graph kernel K, marked section P, short lattice S and monodromy A.',
       [r'\mathrm R',r'\mathrm K',r'\mathrm P',r'\mathrm S',r'\mathrm A'])

old=r''' \ell_d=\gamma-(db\kappa/\nu)r_{\rm per},\quad
 p_0=\nu u-a\kappa\delta,\quad
 \beta_{0,\rm mult}=xu+z\delta,\quad a\kappa x+\nu z=1 .'''
new=r''' \begin{gathered}
 \ell_d=\gamma-(db\kappa/\nu)r_{\rm per},\quad
 p_0=\nu u-a\kappa\delta,\\
 \beta_{0,\rm mult}=xu+z\delta,\quad a\kappa x+\nu z=1 .
 \end{gathered}'''
import re
def layout_tokens(t):
    t=re.sub(r'\\(?:begin|end)\{gathered\}', '',t)
    t=t.replace(r'\\','').replace(r'\quad','')
    return re.sub(r'\s+','',t)
assert layout_tokens(old)==layout_tokens(new)
p.exact(old,new,
        'Place the multiplicative basis definitions on two gathered rows. Removing only the gathered environment, row separator and spacing recovers the same ordered mathematical tokens; every vector and Bezout equation is unchanged.',
        [r'\beta_{0,\rm mult}'])

assert r'\beta_0' not in p.new
assert 'k_d' not in p.new
assert 'H_1(E)' not in p.new and 'H_2(E)' not in p.new
assert r'^E_{\rm perm}' not in p.new
assert p.new.count(r'[p(t)]\mapsto[p(t_{\rm cyc})]')==p.old.count(r'[p(t)]\mapsto[p(t_{\rm cyc})]')
rows=p.finish(OUT,'S6_SERIES_PUBLISH_c9_current02_02LD_retention')
for row in rows:
    row['change_id']=row['change_id'].replace('-02LD-','-02LD-retention-')
stem='S6_SERIES_PUBLISH_c9_current02_02LD_retention'
(OUT/(stem+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print('Canonical manuscript unchanged; t_cyc imports retained.')
