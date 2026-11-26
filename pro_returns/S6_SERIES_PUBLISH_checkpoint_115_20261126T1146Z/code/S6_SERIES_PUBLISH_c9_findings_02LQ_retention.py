#!/usr/bin/env python3
"""Complete current 02LQ retained-role comparison, with exact inverse guards."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re
from S6_SERIES_PUBLISH_c9_scoped_notation import ScopedReview, math_letters

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation9_findings'
source=(ROOT/'S6_SERIES_PUBLISH_III.tex').read_text()
stem='S6_SERIES_PUBLISH_c9_current02_02LQ_retention'
p=ScopedReview(source,
    r'\begin{theorem}[Canonical star logarithms]',
    r'\subsection{Vertical corrections}',
    '02LQ','maps:src:D.2.49','399--407; Theorem 14.7',
    'Used and rechecked in this run after exposure. Read Q201 and the complete current 02LQ statement/proof, including the admitted T-role changes; compared every affected binding, inverse and final difference. Scoped and full-source reversal, numeric literals, labels and targets passed. Genuine formal arguments and same-object redeclarations identified explicitly. No independent proof, new computation or image credit. Admission and changed rendering pending.')


def math_with_equations(t,mapping):
    t=math_letters(t,mapping)
    def equation(m):
        inner=math_letters(r'\['+m.group(1)+r'\]',mapping)[2:-2]
        return r'\begin{equation}'+inner+r'\end{equation}'
    return re.sub(r'\\begin\{equation\}([\s\S]*?)\\end\{equation\}',equation,t)


p.edit('For the sole-logarithm construction write',
       r'\end{theorem}',
       lambda t:math_with_equations(t,{'s':r's_{\rm ord}'}),
       'Name the integer N-2ke as s_ord in the statement, all cyclic orders and the simply connected example, preserving s as the analytic root-disc coordinate. Its integer value, absolute values, parity, coprimality and all homology groups are unchanged.',
       [r's_{\rm ord}'])


def global_coordinates(t):
    t=t.replace('s_0','ZZFIBREGEN')
    t=math_with_equations(t,{'s':r's_{\rm ord}',
                             'u':r'u_{\rm rel}',
                             'v':r'v_{{\rm inv},f}'})
    t=t.replace('ZZFIBREGEN','s_0')
    return t.replace(r'u_{\rm rel}_0',r'u_{0,\rm rel}')


p.edit(r'\emph{The global one-star calculation.}',r'\end{proof}',
       global_coordinates,
       'Propagate s_ord through the entire global order and fundamental-group calculation while preserving the exterior generator s_0. Name the reparametrized column u_rel=b-4ec and its halved coordinate u_{0,rel}; name the selected modular inverse v_{inv,f} for the indicated parity case. The three relation lattices, residue maps, inverse generators and all Smith factors retain exactly their original integer values. The persistent Bezout pair u,v used by h_ab and h_Gamma is preserved.',
       [r's_{\rm ord}',r'u_{\rm rel}',r'v_{{\rm inv},f}'])


def edge_displacement(t):
    t=math_letters(t,{'h':r'h_{\rm edge}'})
    return t.replace(r'^h_{\rm edge}',r'^{h_{\rm edge}}')


p.edit('On the target edge put $h=j-i$.',
       'Their product is',edge_displacement,
       'Name the target-edge displacement h_edge=j-i, preserving the positive integer h in k=2h and the formal function argument h in the averaging operator. The two root-of-unity powers retain their same integer exponents; their product remains zeta and both inverse chart maps remain the same.',
       [r'h_{\rm edge}'])


def torus_lattices(t):
    t=t.replace('L_0',r'\mathcal L_{0,\rm pair}')
    t=t.replace('L_i',r'\mathcal L_{i,\rm fix}')
    return t.replace('L(',r'\mathcal L_{\rm lat}(')


p.edit('At a paired vertex the residual torus lattice is',
       'Use the following integral change',torus_lattices,
       'Name the torus-lattice constructor mathcal L_lat and its paired/fixed instances mathcal L_{0,pair},mathcal L_{i,fix}, preserving L as the marked normal torus. Each is literally the same subgroup of the same real period plane; all lattice inclusions, indices, bases and inverse-on-image maps K_D^{-1}K_C and K_C^{-1}K_D are unchanged. The qualifiers also separate the paired label zero from a fixed vertex indexed zero.',
       [r'\mathcal L_{\rm lat}',r'\mathcal L_{0,\rm pair}',r'\mathcal L_{i,\rm fix}'])


def paired_basis(t):
    t=t.replace(r'\eta_0',r'\eta_0^{\rm lat}')
    return math_letters(t,{'u':r'u_{\rm pair}',
                           'v':r'v_{\rm pair}'})


p.edit('Choose $uN+vk=1$. A basis is',
       'Its ruled normalization is',paired_basis,
       'Name the paired-lattice Bezout choice u_pair,v_pair and its rational basis vector eta_0^{lat}, preserving the later abelian class eta_0 and the persistent uN+2kv=1 pair. The chosen integers satisfy the same equation, the vector has the same two rational coordinates, and both displayed inverse period equations retain every entry. The lattice map and its inverse are the identity on those original period vectors.',
       [r'u_{\rm pair}',r'v_{\rm pair}',r'\eta_0^{\rm lat}'])


def row_basis(t):
    t=t.replace("d'",'ZZROWCOORD')
    t=math_letters(t,{'d':r'd_{\rm row}',
                     'p':r'p_{\rm row}',
                     't':r't_{\rm row}'})
    return t.replace('ZZROWCOORD',"d'")


p.edit('For a row $(A,B)$ modulo $M$ put',
       'The full boundary image',row_basis,
       'Name the derived gcd and chosen Bezout coefficients d_row,p_row,t_row in the generic projected-kernel basis procedure. The formal input row A,B, modulus M and coordinate d-prime retain their input roles. The two unimodular coordinate maps, their inverse, kernel basis and recovered b coordinate have the same coefficients; the former surface-height d and flat translation t are preserved.',
       [r'd_{\rm row}',r'p_{\rm row}',r't_{\rm row}'])
p.edit('For $f=1$ choose $pk+t(2N)=1$',
       'Both expressions are integral',
       lambda t:math_letters(t,{'p':r'p_{{\rm lift},f}',
                                't':r't_{{\rm lift},f}',
                                'V':r'V_{\rm lift}'}),
       'Give the three case-indexed conductor-lift Bezout choices the names p_{lift,f},t_{lift,f}; name the resulting f=0 class V_lift. For each fixed value of f these are the same chosen coefficients and the same integral class. The lifts of D_0 or S, the formula D_0=-L+(1-R)V_lift/2 and the torsion inverse tau_2=w+kD_0 retain their exact coordinates. The earlier node-unit V and other Bezout choices remain unchanged.',
       [r'p_{{\rm lift},f}',r't_{{\rm lift},f}',r'V_{\rm lift}'])

p.edit('For $R=2r-j$ set $t_0=',
       'On the central infinite chain',
       lambda t:math_letters(t,{'F':r'F_{\rm hol}'}),
       'Name the holomorphic function F_hol in the root action, inverse action, node unit and conjugacy difference. It has the identical value of the original function at every root-disc point. Every analytic multiplier, exponent, collapsed power and reciprocal inverse is therefore unchanged, while F remains the later central homology generator.',
       [r'F_{\rm hol}'])
p.edit('With $Z=e^{2\\pi iz}$ this is',
       'The original translation',
       lambda t:math_letters(t,{'U':r'U_{\rm node}'}),
       'Name the nonzero node-unit function U_node, preserving U as the quotient cap. Its defining exponential, value at s,w, reciprocal, and both node-chart multipliers remain identical. Their product and full inverse chart map are preserved.',
       [r'U_{\rm node}'])
p.edit('put $\\mathcal T_{\\rm av}h(s)=',
       'Translation by $h_0$',
       lambda t:math_letters(t,{'c':r'c_{\rm av}'}),
       'Name the averaging input c_av=mathsf L^{-1}b, preserving the peripheral generator c in the final group presentation. The finite average has the same function values and coefficients; its coboundary identity, translation conjugacy and subtraction inverse remain exactly the same.',
       [r'c_{\rm av}'])
p.edit('Hermitian metric put $f_0=|s|^2$.',
       'The invariant construction',
       lambda t:math_letters(t,{'c':r'c_{\rm grad}'}),
       'Name the chosen positive gradient constant c_grad. It has the same numerical value in the lower bound and the reciprocal tail-length estimate; the gradient flow, limiting collapse and inverse on positive-radius collars are unchanged.',
       [r'c_{\rm grad}'])
p.exact('With $t$ boundary components the exterior\nhas $H_1$ rank $t$,',
        'With $t_{\\partial}$ boundary components the exterior\nhas $H_1$ rank $t_{\\partial}$,',
        'Name the number of boundary components t_partial, preserving t as the selected flat translation. It is the same integer count and the same H_1 rank; the following rank equality and zero-kernel argument are unchanged.',
        [r't_{\partial}'])


def layout_tokens(t):
    t=re.sub(r'\\(?:begin|end)\{gathered\}', '',t)
    t=t.replace(r'\\','').replace(r'\qquad','').replace(r'\quad','')
    return re.sub(r'\s+','',t)


def layout(old,new,markers):
    assert layout_tokens(old)==layout_tokens(new)
    p.exact(old,new,
            'Break the widened display into gathered rows. Removing only the gathered environment, row separators and spacing leaves the identical ordered mathematical tokens; all values, maps and cases remain unchanged.',
            markers)


layout(r'''\pi_1(X)=\mathbb Z/|s_{\rm ord}|,\qquad
 T=\operatorname{Tor}H_2(X)=
 \begin{cases}
 \mathbb Z/(2B|s_{\rm ord}|),&f=1,\\
 \mathbb Z/(B|s_{\rm ord}|),&f=2,\\
 \mathbb Z/2\oplus\mathbb Z/(2B|s_{\rm ord}|),&f=0.
 \end{cases}''',
       r'''\begin{gathered}
 \pi_1(X)=\mathbb Z/|s_{\rm ord}|,\\
 T=\operatorname{Tor}H_2(X)=
 \begin{cases}
 \mathbb Z/(2B|s_{\rm ord}|),&f=1,\\
 \mathbb Z/(B|s_{\rm ord}|),&f=2,\\
 \mathbb Z/2\oplus\mathbb Z/(2B|s_{\rm ord}|),&f=0.
 \end{cases}
\end{gathered}''',[r's_{\rm ord}'])
layout(r''' H_4=\mathbb Z^{\rho-1}\oplus\mathbb Z/|s_{\rm ord}|,\qquad H_5=0,
 \qquad H_0=H_6=\mathbb Z .''',
       r''' H_4=\mathbb Z^{\rho-1}\oplus\mathbb Z/|s_{\rm ord}|,\qquad H_5=0,\\
 H_0=H_6=\mathbb Z .''',[r's_{\rm ord}'])
layout(r'''g(s,z,w)=
\left(\zeta s,-z-w-jl(s)+F_{\rm hol}(s^m)-\frac{N\eta(s)}m,\ w+t_0\right)''',
       r'''\begin{gathered}
g(s,z,w)=\\
\left(\zeta s,-z-w-jl(s)+F_{\rm hol}(s^m)-\frac{N\eta(s)}m,\ w+t_0\right)
\end{gathered}''',[r'F_{\rm hol}'])
layout(r''' X'=\zeta^{h_{\rm edge}}U_{\rm node}Y,\qquad
 Y'=\zeta^{1-h_{\rm edge}}U_{\rm node}^{-1}X,\qquad w'=w+t_0 .''',
       r''' \begin{gathered}
 X'=\zeta^{h_{\rm edge}}U_{\rm node}Y,\\
 Y'=\zeta^{1-h_{\rm edge}}U_{\rm node}^{-1}X,\\
 w'=w+t_0 .
 \end{gathered}''',[r'h_{\rm edge}',r'U_{\rm node}'])
layout(r'''(x,y)\longmapsto
([x+Bv_{{\rm inv},f}Ry]_{2B|s_{\rm ord}|},[y]_2),\qquad
([z],[t])\longmapsto zs_0+tY_0 .''',
       r'''\begin{gathered}
(x,y)\longmapsto
([x+Bv_{{\rm inv},f}Ry]_{2B|s_{\rm ord}|},[y]_2),\\
([z],[t])\longmapsto zs_0+tY_0 .
\end{gathered}''',[r's_{\rm ord}',r'v_{{\rm inv},f}'])

assert p.new.count('s_0')==p.old.count('s_0')
assert p.new.count(r'\mathbb C')==p.old.count(r'\mathbb C')
assert p.new.count(r'\mathcal T_{\rm av}')==p.old.count(r'\mathcal T_{\rm av}')
assert p.new.count(r'T_{\rm W}')==p.old.count(r'T_{\rm W}')
assert r'^h_{\rm edge}' not in p.new
assert r'u_{\rm rel}_0' not in p.new
rows=p.finish(OUT,stem)
for row in rows:
    row['change_id']=row['change_id'].replace('-02LQ-','-02LQ-retention-')
(OUT/(stem+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (OUT/(stem+'_defects.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(rows)
print('All current affected roles compared; canonical source unchanged.')
event_id='ce:c9-iii-current02-02lq-retention-reconciliation'
event=dict(statement_id='maps:src:D.2.49',date='2026-11-26',
           who='GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode',
           type='used and rechecked in this run',
           outcome='Read Q201 and the complete current 711-line 02LQ statement/proof after the admitted T-role packet. Compared all 11 final fragments from 17 reversible operations, including five display token comparisons. Verified the root/node map and inverse, paired marked-period coordinates and lattice basis inverses, distinct selected Bezout families, generic row-coordinate matrix inverse, conductor-lift identities, all global quotient maps and unchanged normal D,L / T_W / h_ab,h_Gamma transports. Explicitly reconciled every old 02LQ retention, including formal central/row/angular coordinates and same-object redeclarations. Scoped/full-source reversal, ordered numeric literals, labels and targets passed. No independent proof, new computation or image credit. Admission and changed rendering pending.',
           event_id=event_id,phase='publication continuation 9',
           source_file='agents/continuation9_findings/'+stem+'_review.md',
           source_row='complete current Q201 and 02LQ statement/proof, all final differences and retained-coordinate decisions',
           source_event_type='used and rechecked in this run',evidence_group=event_id,
           publish_input_file='agents/continuation9_findings/'+stem+'_defects.tsv',
           publish_input_row='all 11 guarded fragments',
           date_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
           where='Paper III, tag02LQ / maps:src:D.2.49; complete current canonical-star statement and proof')
with (OUT/(stem+'_CHECK_EVENTS.tsv')).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(event),delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerow(event)
