"""Apply exact notation and inverse-map refinements after the whole950-line read."""
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r
df, ds = r.table(r.DEFECTS)
path = u.WORK / 'root/retained_angle.tex'
before = path.read_text()
after = before
specs = [
 ('PERIOD-PROSE', 'D01', r'\(C\) is holomorphic at \(t=0\), exactly as in the original source.', r'\(C\) is holomorphic at \(t=0\).', 'Keep the actual period hypothesis and remove the production-history phrase.'),
 ('PERIOD-NAME', 'D23', 'The subscript in \\(h_{\\rm per}\\) distinguishes that period function\nfrom the sphere-valued map below.  Write', 'Write', 'The explicit h_per=h input already gives the notation map and inverse; the old h-versus-H sentence no longer names the actual sphere-map notation.'),
 ('BOUND-NAME', 'D20', r'\(M=\sup\|R(t)\|<\infty\)', r'\(M_R=\sup\|R(t)\|<\infty\)', 'Name the real norm bound M_R; M is the actual regular inverse-image torus.'),
 ('BOUND-VALUE', 'D20', r'\(|\log r_0|>M\).  This chooses a point of the already specified map;' + '\nit does not change that map or the cutoff radius \\(\\epsilon\\).', r'\(|\log r_0|>M_R\), with the map $H$ and its cutoff $\epsilon$ fixed.', 'Use the named bound while keeping the precise fixed-map/radius scope.'),
 ('BOUND-INEQUALITY', 'D20', r'\geq (|\ell|-vM)|\xi|>0', r'\geq (|\ell|-vM_R)|\xi|>0', 'Use the same real bound in the full all-parameter norm inequality.'),
 ('BOUND-DOMAIN', 'D20', r'whenever \(|\ell|>M\).', r'whenever \(|\ell|>M_R\).', 'State the exact domain for the same invertibility inequality.'),
 ('THREE-CELL-INVERSE', 'D22', 'Each derivative in its own variable is strictly positive, and approach', r'''The inverse on $\mathbb R^3$ is
\[
 (v_\phi,v_1,v_2)\longmapsto
 \left(\pi+2\arctan v_\phi,
       \tfrac12+\frac1\pi\arctan v_1,
       \tfrac12+\frac1\pi\arctan v_2\right).
\]
The identities $-\cot(\pi/2+\arctan v)=v$ and the stated open
coordinate ranges verify both composites. Each derivative in its
own variable is strictly positive, and approach''', 'Give the actual inverse of the existing ordered cotangent chart, including its ranges and both composites.'),
 ('FOUR-CELL-INVERSE', 'D22', 'This fixes the target orientation.  Replacing \\(r\\) locally by', r'''Its inverse sends $(v_0,v_\phi,v_1,v_2)$ to
\[
 r=\epsilon\left(\tfrac12+\frac1\pi\arctan v_0\right),\quad
 \phi=\pi+2\arctan v_\phi,\quad
 u_i=\tfrac12+\frac1\pi\arctan v_i\quad(i=1,2).
\]
The same cotangent identities verify both inverse compositions.
This fixes the target orientation. Replacing \(r\) locally by''', 'Give the inverse including the exact radial scale epsilon; no source or target coordinate is changed.'),
 ('GAUGE-SCOPE', 'D02', 'across every coordinate divisor.  No period matrix is replaced by a\ndifferent matrix in this coordinate change.', 'across every coordinate divisor. Both coordinate descriptions use\nthe same base parameter $t$ and the same holomorphic period germ $C$.', 'Express the already verified product-preserving coordinate correspondence positively, retaining its complete parameter scope.'),
 ('ELL-ZERO', 'D20', 'The period matrix gives an explicit homotopy of this normal framing.  Put', 'The period matrix gives an explicit homotopy of this normal framing.\nPut $\\ell_0=\\log r_0$ and', 'Define ell0 at its actual first use, before the normal-frame homotopy and the orientation proof.'),
 ('SPIN-PROSE', 'D08', 'The intrinsic Lie-torus calculation is the known computation in \\cite[Example~3.8, p.~6]{DebrayGunningham2018Root}; we retain its direct derivation. For the intrinsic Lie framing on', 'For the intrinsic Lie framing, \\cite[Example~3.8, p.~6]{DebrayGunningham2018Root} gives the following quadratic values. On', 'Remove the editorial retention phrase while retaining the precise source and the complete direct computation.'),
 ('SMOOTHING-NAMES', 'D20', 'with inverse notation changes $H=f$, $M=N$ and $y_0=y$.\nIn the lemma\'s notation take its protected tube $T=U_1$;', 'with inverse notation changes $H=f$, $M=N$ and $y_0=y$.\nWrite $H_b=f_b$ for the first endpoint in that lemma, with inverse\n$f_b=H_b$. In its notation take the protected tube $T=U_1$;', 'Define the actual first-stage endpoint before using it in the compact positive-gap formula.')
]
for suffix, kind, old, new, reason in specs:
    assert after.count(old) == 1, (suffix, after.count(old))
    after = after.replace(old, new, 1)
    ident = 'III-C8-RETAINED-' + suffix
    assert not any(x['change_id'] == ident for x in ds)
    ds.append(dict(change_id=ident, type=kind, statement_id='mapsIII:def:retained-angle-cusp-data; maps:src:B.3.1',
        old_location='950-line staged retained-angle rewrite', old_page='pending page concordance',
        new_location='same complete owner after whole readback', new_page='pending final PDF',
        old_text=old, new_text=new, reason=reason,
        review_status='exact staged readback edit; changed-context reading and canonical application pending'))
u.check_permanent_identifiers(before, after)
path.write_text(after, encoding='utf-8', newline='\n')
qp = u.WORK / 'root/quotient_maps.tex'
qbefore = qp.read_text()
qold = r'\subsection{Retained-coordinate quotient maps}'
qnew = r'\subsection{Angle-forgetting and cusp-core quotient maps}'
assert qbefore.count(qold) == 1
qafter = qbefore.replace(qold, qnew, 1)
u.check_permanent_identifiers(qbefore, qafter)
ident = 'III-C8-RETAINED-QUOTIENT-TITLE'
assert not any(x['change_id'] == ident for x in ds)
ds.append(dict(change_id=ident, type='D16', statement_id='mapsIII:def:cusp-suspension-maps',
    old_location='earlier quotient_maps subsection', old_page='pending page concordance',
    new_location='same remaining complete Q011/J8/Q012/J9 subsection', new_page='pending final PDF',
    old_text=qold, new_text=qnew, reason='Name the two proved quotient-map classes after moving the complete J7 owner; all inputs and remaining proofs stay unchanged.',
    review_status='complete280-line remaining unit read; exact title edit staged'))
qp.write_text(qafter, encoding='utf-8', newline='\n')
r.write_table(r.DEFECTS, df, ds)
print('UTC', datetime.now(timezone.utc).isoformat())
print('EXACT_READBACK_EDITS', len(specs) + 1, 'RETAINED_LINES', after.count('\n'))
print('ALL_IDENTITIES_PRESERVED; STAGED_ONLY; FINAL_CONTEXT_READING_REQUIRED')
