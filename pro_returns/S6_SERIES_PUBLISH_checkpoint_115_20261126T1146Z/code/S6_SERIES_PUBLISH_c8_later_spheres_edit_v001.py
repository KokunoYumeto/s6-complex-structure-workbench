#!/usr/bin/env python3
"""Publication edits to wholly read sphere proofs and their final scope note."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv
import difflib
import re
import S6_SERIES_PUBLISH_c8_integrate_presentation as presentation
import S6_SERIES_PUBLISH_c8_integrate_units as units

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'agents/continuation8_iii_integration/units/later/elliptic_sphere_outputs.tex'
LIMITS = ROOT / 'agents/continuation8_iii_integration/units/later/limits_and_open_points.tex'
OUT = ROOT / 'agents/continuation8_iii_later'
old, limits_old = PATH.read_text(), LIMITS.read_text()
assert sha256(old.encode()).hexdigest() == '05af32cdacb747a98e80f51521a52953e1284c9204198c8db1f20a90f8194dd4'
assert sha256(limits_old.encode()).hexdigest() == '019c051106664ae432cb4366c321274c119ac2f6a95958c2d4675969d89d4055'

# These are exact extraction maps with inverses, not normalization.
folders = [('02KZ','star_exclusion'),('02L0','semistable'),('02L1','nonstar'),
           ('02L2','nonstar_specializations'),('02L3','profile_synthesis')]
for tag, folder in folders:
    p = ROOT / ('agents/continuation7_iii_' + folder) / ('S6_SERIES_PUBLISH_III_' + tag + '_receiving.tex')
    receiver = p.read_text().strip() + '\n'
    env = 'corollary' if tag == '02L3' else 'theorem'
    before = '\\end{' + env + '}\n\n\\begin{proof}'
    after = '\\end{' + env + '}\n\n\n\\begin{proof}'
    assert receiver.count(before) == 1
    mapped = receiver.replace(before, after, 1)
    if tag == '02L1':
        key_before, key_after = '{KervaireMilnor1963}', '{manKM63}'
        assert mapped.count(key_before) == 1
        mapped = mapped.replace(key_before, key_after, 1)
    a = old.index('\\hypertarget{tag-' + tag + '}')
    a = old.rfind('\\begin{', 0, a)
    b = old.index('\\end{proof}', a) + len('\\end{proof}')
    assert old[a:b] + '\n' == mapped
    inverse = mapped
    if tag == '02L1':
        assert inverse.count(key_after) == 1
        inverse = inverse.replace(key_after, key_before, 1)
    assert inverse.replace(after, before, 1) == receiver
    print('WHOLE_ADMITTED_RECEIVER_MAP', tag, len(mapped.splitlines()), sha256(p.read_bytes()).hexdigest())

new = old
rows = []
fields = ['change_id','type','statement_id','old_location','old_page','new_location',
          'new_page','old_text','new_text','reason','review_status']

def owner(text, pos):
    matches = list(re.finditer(r'\\(?:begin\{(?:theorem|corollary|definition)\}[^\n]*|hypertarget\{tag-[^}]+\}\{\})[^\n]*\\label\{([^}]+)\}', text[:pos+1]))
    return matches[-1][1] if matches else 'maps:src:D.2.24'

def record(kind, sid, before, after, reason, location, target='corresponding retained statement'):
    rows.append(dict(change_id=f'c8-III-spheres-{len(rows)+1:03}', type=kind,
        statement_id=sid, old_location=location, old_page='pending final page concordance',
        new_location=target, new_page='pending final build', old_text=before, new_text=after,
        reason=reason, review_status='whole repaired input and complete admitted comparisons read; exact final readback and root admission pending'))

def change(before, after, kind, reason, count=1, sid=None):
    global new
    assert new.count(before) == count, (before, new.count(before), count)
    for match in re.finditer(re.escape(before), new):
        pos = match.start()
        record(kind, sid or owner(new,pos), before, after, reason,
               'elliptic_sphere_outputs.tex sequential edit line ' + str(new[:pos].count('\n')+1))
    new = new.replace(before, after)

change(r'\begin{theorem}[exclusion of the two $I_3^*$ profiles]',
       r'\section{Sphere fillings of elliptic profiles}' + '\n' +
       r'\subsection{The $I_3^*$ homology obstruction}' + '\n' +
       r'\begin{theorem}[Homology obstruction for the two $I_3^*$ profiles]',
       'D14', 'Start a section with the positive local-homology obstruction, keeping the exact eight-candidate scope of the theorem.', sid='maps:src:D.2.24')
change(r'\begin{theorem}[The semistable classification]',
       r'\subsection{All-multiplicative profiles}' + '\n' +
       r'\begin{theorem}[Integral homology and spheres for multiplicative profiles]',
       'D14', 'Place the complete multiplicative calculation after the star obstruction, in its own actual subsection.', sid='maps:src:D.2.25')
pattern = r'''\subsection{Sixteen finite and multiplicative profiles}
\begin{definition}[Marked filling patterns]\hypertarget{tag-Q302}{}\label{maps:def:marked-filling-pattern}
{\normalfont\scriptsize tag Q302}\par
A marked filling pattern consists of a marked elliptic profile,
an ordered section pair, a zero position and a permitted additive
filling choice at each additive fibre. Logarithmic orders and affine
powers are parameters of the chosen fillings.
\end{definition}

'''
change(r'\begin{theorem}[Sphere fillings for sixteen elliptic profiles]',
       pattern + r'\begin{theorem}[Sphere fillings for sixteen elliptic profiles]',
       'D13', 'Give the mathematical pattern definition before its first use; the later projection to the same profile/section/zero tuple and all 59 patterns remain.', sid='maps:src:D.2.26')
change(r'\begin{theorem}[The three $I_1^*$ profiles give no natural sphere]',
       r'\subsection{The $I_1^*$ integral obstruction}' + '\n' +
       r'\begin{theorem}[Integral obstructions for the three $I_1^*$ profiles]',
       'D14', 'Place the torsion-sensitive star obstruction after its multiplicative and finite-cap prerequisites.', sid='maps:src:D.2.27')
change(r'\begin{corollary}[Sphere outputs over twenty-one elliptic profiles]',
       r'\subsection{The classification over twenty-one profiles}' + '\n' +
       r'\begin{corollary}[Sphere outputs over twenty-one elliptic profiles]',
       'D14', 'Keep the complete synthesis after its KZ, L0, L1 and L2 proofs; no dependency-driven reordering of L4/L6 is needed.', sid='maps:src:D.2.28')
change('A pattern consists of a marked initial section pair, zero position\nand additive filling choice. The complete profile classification is',
       'Use the marked filling patterns of\nDefinition~\\ref{maps:def:marked-filling-pattern}. The complete profile classification is',
       'D13', 'Refer to the preceding numbered definition; identity on the profile, ordered pair, zero and additive choice gives the exact old/new tuple map and inverse.', sid='maps:src:D.2.28')
for tag in ['02KZ','02L0','02L1','02L2','02L3']:
    before = {'02KZ':r'\textnormal{\small tag02KZ.}',
              '02L0':r'\textnormal{\small tag 02L0.}',
              '02L1':r'\textup{\small(tag 02L1)}',
              '02L2':r'\textnormal{\small tag 02L2.}',
              '02L3':r'\textup{\small(tag 02L3)}'}[tag]
    change(before, r'{\normalfont\scriptsize tag ' + tag + r'}\par',
           'D10', 'Print the existing small tag in the common form; retain its exact label and target.')

# Each phrase was read in its complete mathematical proof before editing.
phrases = [
 ('Here is a complete integral homology algorithm without a bound on\norders, number of sites, or translation coordinates.', 'The integral homology is determined as follows for all the stated\norders, numbers of sites and translation coordinates.'),
 ('If this group is trivial, let', 'For a simply connected member, let'),
 (r'\emph{Exact construction inputs and conventions.}', r'\emph{Period and orientation conventions.}'),
 ('The raw component coordinates are the negatives', 'The component coordinates used below are the negatives'),
 ('The four raw default rows have the following complete local data.', 'The four marked default profiles have the following local data.'),
 ('The component calculation produces an actual line map.', 'The component calculation gives the following line map.'),
 (r'\emph{Actual periods, normal meridians and local models.}', r'\emph{Periods, normal meridians and local models.}'),
 ('The actual four-period matrix is', 'The four-period matrix is'),
 ('Here is the geometric splitting, including its global relation.', 'The fixed-loop sweeps give a geometric splitting with the following global relation.'),
 ('Every stated generator is integral. For clarity the exact change of\nperipheral lift is', 'Every generator is integral. A change of peripheral lift is given by'),
 ('The cusp discs and their transported copies in the transported cusp-disc matrix kill exactly', 'The cusp discs and the right inverse of the matrix of transported loops kill exactly'),
 ('We now account for the remaining degree-two term.', 'The remaining degree-two term comes from the relative normal discs.'),
 ('Integral Poincar\\\'e duality and universal coefficients now give all the groups:', 'Integral Poincar\\\'e duality and universal coefficients give all the groups:'),
 ('Suppose the group in \\eqref{maps:eq:D.FG1} is trivial. Criterion', 'For a simply connected member, criterion'),
 ('Here is the complete consolidation into three generators. Define', 'Consolidate the generators by defining'),
 ('In the raw primitive short lattice', 'In the primitive short lattice'),
 ('We now work on the physical-fan representative obtained by', 'Work on the physical-fan representative obtained by'),
 ('For precision, the first resulting model is', 'The resulting model is'),
 ('Every inverse has been specified piecewise and matches on the\nsame collars.', 'The piecewise inverses match on the same collars.'),
 ('The auxiliary spin conclusion has already been proved for all\n\\(M\\). Also \\(p_1=0\\):', 'The quotient calculation proves spin for every \\(M\\). Moreover, \\(p_1=0\\):'),
 ('For each raw pair $(A_i,g_i)$ put', 'For each marked pair $(A_i,g_i)$ put'),
 ('Integer elimination on the raw tuples gives, for', 'Integer elimination on the marked tuples gives, for'),
 ('$172$ raw natural rows, hence on the $148$ used here.', '$172$ natural rows, hence on the $148$ used here.'),
 ('The normalization pushout now gives', 'The normalization pushout gives'),
]
for before, after in phrases:
    change(before, after, 'D08', 'State the marked construction or its mathematical consequence directly; all formulas, inverses and parameter scopes remain.')
change('This also proves that no torsion extension was omitted by the\nMayer--Vietoris cokernel. For a completely mechanical integral\ncoordinate map, make the columns of a matrix \\(R\\) the relations',
       'The closed lift splits the free extension of the Mayer--Vietoris\ncokernel. For integral coordinates, make the columns of a matrix \\(R\\) the relations',
       'D02', 'Use the explicit closed lift and inverse splitting positively; retain every Smith quotient coordinate and torsion factor.')
change('The residual term is periodic and deck\ninvariant; multiplying it by a radial cutoff extends the isotopy\nover the exterior. They give the literal positive normal class\n\\(d_i=m_i c_i-v_i\\), with no omitted radial or line-unit twist.',
       'The residual term is periodic and deck\ninvariant; multiplying it by a radial cutoff extends the isotopy\nover the exterior. These maps carry the positive normal to\n\\(d_i=m_i c_i-v_i\\), including the radial and line-unit factors.',
       'D02', 'State the exact collar transport and its factors positively; retain the displayed inverse map.')
change('Thus no\nunrecorded fibre summand is possible.',
       'Injectivity of multiplication by \\(m_i\\) determines the fibre coefficient uniquely.',
       'D02', 'State the injectivity argument already proved on the free exterior group directly.')
change('No replacement of\nthe underlying exterior or its marking is made.',
       'These maps use the specified punctured family and its marking.',
       'D02', 'Use the identity of the punctured complex family from the preceding period-coordinate maps positively; retain the actual fan replacements and global comparison.')
change('The oriented identification \\eqref{maps:eq:D.SC6}, including\nits even-M cases, was constructed before this stabilization.',
       '', 'D11', 'The complete unstabilized map, inverse and even-M spin proof already precede this surgery; remove only the repeated chronological closing sentence.')
count = new.count('Bezout')
assert count > 0
change('Bezout', r"B\'ezout", 'D23', 'Typeset the standard name with its accent in each wholly read occurrence.', count=count)
change(r'\cite[Section 2.4, equation (2.2)]{manUU21}',
       r'\cite[\S2.4, equation (2.2), p.~6]{manUU21}', 'D18',
       'Use the precise page-6 locator already admitted for this local-log source; no new primary reading is claimed.')

scope = '''The scope here is the natural section-line sphere question.
The optional vertically corrected catalogue of $226$ rows in
\\ref{maps:src:D.2.22} has not been substituted for it. Formula \\eqref{maps:eq:D.ST13} concerns the sphere outputs. The unrestricted
finite-log homology is supplied in \\ref{maps:src:D.2.29}--\\ref{maps:src:D.2.33}, and the entire specified
minimal simply connected smooth sector is completed by \\ref{maps:src:D.2.35}--\\ref{maps:src:D.2.36},
\\ref{maps:src:D.2.38}--\\ref{maps:src:D.2.39}, \\ref{maps:src:D.2.42} and \\ref{maps:src:D.2.44}--\\ref{maps:src:D.2.45}. The remaining weighted and
additional-regular-log smooth classification is scoped in \\ref{maps:src:D.2.4}.
'''
remark = r'''\begin{remark}[Natural sphere data and further classifications]\hypertarget{tag-Q301}{}\label{maps:rem:natural-sphere-sector-scope}
{\normalfont\scriptsize tag Q301}\par
The sphere table \eqref{maps:eq:D.ST13} concerns the natural line
$M_0=\mathcal O(P-O)$. In the vertically corrected family
$M_V=\mathcal O(P-O+V)$ of \ref{maps:src:D.2.22}, the specialization
$V=0$ is identity on this line bundle, its linearization and the
marked quotient with the same filling data; its inverse on that
subfamily is the same identity. The finite reduction for integral
vertical $V$ has $226$ marked rows, with the solution lattices
specified in that theorem.

The nontrivial fundamental-group obstruction at fixed-character
index $g>1$ in \ref{maps:src:D.2.30} preserves the sphere
classification of Corollary~\ref{maps:src:D.2.28} in the full
finite-lattice family.

The unrestricted finite-log homology is given in
\ref{maps:src:D.2.29}--\ref{maps:src:D.2.33}. The specified minimal
simply connected smooth sector is classified by
\ref{maps:src:D.2.35}--\ref{maps:src:D.2.36},
\ref{maps:src:D.2.38}--\ref{maps:src:D.2.39},
\ref{maps:src:D.2.42} and
\ref{maps:src:D.2.44}--\ref{maps:src:D.2.45}.
The remaining weighted and additional-regular-log smooth
classifications are included in Problem~\ref{maps:src:D.2.4}.
\end{remark}

'''
assert new.count(scope) == 1
scope_pos = new.index(scope)
before_scope_move = new
new = new.replace(scope, '', 1)
assert new[:scope_pos] + scope + new[scope_pos:] == before_scope_move
prefix, body = limits_old.split('\\begin{problem}', 1)
limits_new = prefix + remark + '\\begin{problem}' + body
assert limits_new.replace(remark, '', 1) == limits_old
record('D14','maps:src:D.2.28',scope,remark,
       'Move the orphan forward overview into a numbered final-part remark and give the V=0 inclusion explicitly. Deleting the exact new remark recovers the whole original limits fragment; reinserting the exact old paragraph at its former position recovers the former sphere suffix. The admitted LG Problem is byte-for-byte unchanged.',
       'elliptic_sphere_outputs.tex original closing scope paragraph',
       'limits_and_open_points.tex before the unchanged LG Problem')

numbered, display_edits, issues, aliases = presentation.remove_manual_equation_tags(new)
assert not issues, issues
for edit in display_edits:
    record(edit.kind, owner(new,edit.start),edit.old,edit.new,edit.reason,
           'elliptic_sphere_outputs.tex numbering stage line ' + str(new[:edit.start].count('\n')+1),
           'same retained equation label and target')
new = numbered
literal_issues = presentation.unresolved_literal_equation_references(new, aliases)
assert not literal_issues, literal_issues
units.check_permanent_identifiers(old+limits_old,new+limits_new,
    ['maps:def:marked-filling-pattern','maps:rem:natural-sphere-sector-scope'],['tag-Q302','tag-Q301'])
assert new.count(r'\begin{proof}') == new.count(r'\end{proof}') == 5
assert new.count(r'\begin{theorem}') == 4 and new.count(r'\begin{corollary}') == 1
assert new.count(r'\begin{definition}') == 1
assert limits_new[limits_new.index(r'\begin{problem}'):] == limits_old[limits_old.index(r'\begin{problem}'):]

with (OUT/'S6_SERIES_PUBLISH_III_spheres_publication_defects.tsv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fields,delimiter='\t',lineterminator='\n')
    writer.writeheader(); writer.writerows(rows)
for name, a, b in [('spheres',old,new),('sphere_scope_relocation',limits_old,limits_new)]:
    (OUT/('S6_SERIES_PUBLISH_III_'+name+'_publication.diff')).write_text(
        ''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile=name+'_input',tofile=name+'_publication')),newline='\n')
PATH.write_text(new,newline='\n')
LIMITS.write_text(limits_new,newline='\n')
print('UTC',datetime.now(timezone.utc).isoformat())
print('SPHERES',len(new.splitlines()),sha256(new.encode()).hexdigest())
print('LIMITS',len(limits_new.splitlines()),sha256(limits_new.encode()).hexdigest())
print('EXACT_LOCAL_EDITS',len(rows),'D19_OPERATIONS',len(display_edits),'UNRESOLVED_LITERAL_REFS',len(literal_issues))
print('NEW_IDENTITIES','Q301 maps:rem:natural-sphere-sector-scope','Q302 maps:def:marked-filling-pattern')
print('FIVE_SOLE_PROOFS; ALL_OLD_IDENTIFIERS_PRESERVED; LG_PROBLEM_UNCHANGED')
print('NO_SHARED_WRITES; NO_MECHANICAL_CRITERION_CREDIT')
