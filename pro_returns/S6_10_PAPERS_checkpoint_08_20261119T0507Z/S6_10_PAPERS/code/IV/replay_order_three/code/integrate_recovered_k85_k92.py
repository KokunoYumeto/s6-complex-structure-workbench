"""Integrate the freshly reviewed post-recovery proofs without rewriting history."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    85: 'part3_os49_reduced_ii_return',
    86: 'part3_source_zero_normal_clutch',
    87: 'part3_os49_reduced_ii_all_fans',
    88: 'part3_source_zero_base_sector',
    89: 'part3_source_zero_vertical_pair',
    90: 'part3_source_zero_all_fans',
    91: 'part3_os49_reduced_ii_endpoints',
    92: 'part3_source_infinity_groupoid_all_fans',
}
CERTIFICATES = {
    85: 'code/part3/os49_reduced_ii_return.json',
    86: 'code/part3_fourfold/reconstructed_k86_ps_np_checks.json',
    87: 'code/part3/os49_reduced_ii_all_fans.json',
    88: 'code/part3_root/source_zero_base_sector.json',
    89: 'code/part3/source_zero_vertical_pair.json',
    90: 'code/part3_root/source_zero_all_fans.json',
    91: 'code/part3/os49_reduced_ii_endpoints.json',
    92: 'code/part3_fourfold/source_infinity_all_fans.json',
}
DESCRIPTIONS = {
    85: 'Reduced-II canonical positive-fan physical pair (2mh,24k(3l+1)) and integer 3kl, with both actual cap/Cartier maps and the full normal comparison.',
    86: 'Complete source-zero fixed-trace normal clutch, including both cap matrices and the source-coordinate collar terms: Gamma=0.',
    87: 'Every reduced-II canonical lattice-basis fan, its complete free integer seed/target algorithm, and 28 explicit witnesses for the smallest tuple.',
    88: 'Every fixed-scalar source-zero residue on each E7 branch, witnessed by actual fans and full source/Cartier/Cox/root maps.',
    89: 'Full source-zero vertical physical and native integer pairs, including coupled scalar windings, all cap/line corrections and native parameter composition.',
    90: 'Complete source-zero return algorithm on every GL2Z fan, constructed from the full vertical integer seed and unique integral target-prism solution.',
    91: 'Full reduced-II integral root groupoid, all marked ordinary clutches, every fixed-source holomorphic endpoint and the actual shortest scalar return.',
    92: 'Every-fan E7 infinity return from the actual compact four-boundary sphere family, with exact branch labels, finite-root endpoint scalar and transported period cochain.',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for n, stem in FILES.items():
    qa_path = ROOT / f'records/k{n}_standalone_visual_qa.json'
    qa = json.loads(qa_path.read_text())
    assert qa['status'] == 'PASS', (n, qa)
    assert (ROOT / f'notes/{stem}.tex').is_file()
    assert (ROOT / CERTIFICATES[n]).is_file()

archive = ROOT / 'records/checkpoint22_prior_master68'
assert not archive.exists()
for name in (
    'notes/part3.tex', 'notes/part3_remaining_return_obligations.tex',
    'notes/part3_source_global_groupoid.tex',
    'notes/part3_source_global_groupoid_working.md',
    'notes/part3_source_moduli_loops_working.md',
    'code/update_report.py', 'code/part3/results_mapping.json',
    'S6_06_BLIND_paper.pdf', 'S6_06_BLIND_paper.log',
    'S6_06_BLIND_paper.aux', 'S6_06_BLIND_paper.toc',
    'S6_06_BLIND_results.csv', 'S6_06_BLIND_report.md',
    'records/progress_check_21_hours.json',
):
    source = ROOT / name
    dest = archive / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)

part = ROOT / 'notes/part3.tex'
text = part.read_text()
for n, stem in FILES.items():
    include = r'\input{notes/' + stem + '.tex}'
    assert include not in text
    text += '\n' + include + '\n'
part.write_text(text)

current_register = r'''\subsection{The remaining return sectors after the complete source-zero and reduced-II calculations}
\begin{statement}{P3K.75}{Unresolved; exact remaining obligations}
P3K.71 computes the selected-cusp source return on every lattice-basis
fan. P3K.72--74 give the full corrected scalar-fan algorithms in their
specified whole-zero source scope. P3K.85--91 complete the following
additional sectors through their actual source, Cartier, root, normal
and inverse-closing maps.

For the source-zero E7 branches put
\[
 (a,b,m)=(1,2,4p)\quad\hbox{or}\quad(2,1,4p-1),\qquad
 N=km,\quad \mu=2-a+6pk.
\]
The scalar is \(\lambda=v^N\lambda_0\); the fixed-scalar case is
\(k=0\). For every vertical fan \(T_j\), P3K.89 proves
\[
\begin{aligned}
 A_j={}&2b\binom{j+1}{3}+(3-b)\binom{j+1}{2}
       +k(a-1)(3p-1)-km\binom j2,\\
 (k_M,\ell_M)={}&(\mu+6A_j,4\mu).
\end{aligned}
\]
The full normal clutch used here is computed in P3K.86.
P3K.90 transports these free integer data to every
\(P\in\mathrm{GL}_2(\mathbb Z)\) by the actual two-ruling maps and
the uniquely solved integral target-prism system. P3K.88 supplies
explicit fixed-scalar fan witnesses for every element of
\(\Theta_7\) on each branch.

For the component-supported OS49 source, P3K.77--79 complete all
one-cap lattice-basis fans, marked smooth order-one clutches and
fixed-source holomorphic endpoints. P3K.81 supplies the exact
integral obstructions for the additional smooth caps and good-II
caps treated there. P3K.84--85 construct the two actual finite caps
\(m=3k\), \(h=6l+1\) and their positive canonical return.
With the full ordinary-clutch integer \(\sigma\), P3K.91 proves
\[
 D=hn_A+mn_B+mh\sigma=\epsilon=\pm1,\qquad
 H^2(\mathcal H)=\mathbb Z\oplus\mathbb Z/k\oplus\mathbb Z/h.
\]
The class is \((D,d_A\bmod k,d_B\bmod h)\). Its complete
holomorphic endpoint group is the physical \(\mathbb C^*\).
The actual shortest parameter \(w=r^3\), \(\lambda=w^{kh}\), has
positive-fan physical pair \((2kh,8k(3l+1))\) and integer \(kl\).
P3K.87 and P3K.91 compute every fan and every admitted winding
\(Nkh\), with the endpoint and native covering maps constructed
before integral characteristic naturality is applied.

P3K.92 completes the infinity boundary of the marked E7
four-boundary parameter family on every fan. In its exact marking,
\[
 I_a(P)=-Z_a(P)-Z_a(JP)-C(P)\pmod {28},\qquad
 J=\operatorname{diag}(-1,1).
\]
The branch reflection and the infinity rescaling are given by
their full character maps. The infinity root endpoint retains
\(A^4D^{-4}=S_{r_0^{4n}}L^4\), its inverse scalar path on both
ordinary and cap charts, and the actual transported lattice
period \(-n(2\omega_1+2\omega_2)\). The two unselected
\(v=1/8\) discs have the P3K.53 extension.

The outstanding work is the remaining marked source-moduli
generators, singular-site sectors and endpoint scopes outside
the completed families just listed. In the E6 family
\[
 y^2=x^3+rx^2+tx+t^2,\qquad G=(0,t),
\]
the unselected \(r=0\) and \(r=1/4\) collision attachments are
being constructed with the actual section, line, root and norm
maps. The latter calculation retains the full selected-zero Hom
section \((t-t_{\rm sel})B_6/t^3\); its limiting factor
\(4(t-t_{\rm sel})/t\) and every component order remain in the
unfinished attachment. The other selected-node boundary
generators and their actual closing maps also remain to be
completed. The working notes assign no return to an unfinished
attachment. Part 3.4 therefore remains incomplete.
\end{statement}
\begin{proof}[Current reductions and preserved earlier attachment history]
The current reductions are the full proofs P3K.71--74 and
P3K.76--92 cited in the statement. The recovered P3K.85--91
sources have fresh mathematical and visual audits; their
reconstruction records identify the lost earlier bytes and the
newly verified files. P3K.92 is a new complete proof.

\par\medskip\noindent\textbf{Historical working record from checkpoint 19.}\par\nopagebreak[4]
The following retained paragraphs document the successive earlier
attachment attempts and their status at that time. The current
status and completed replacements are the statement above and
P3K.85--92. In particular their earlier unresolved source-zero
and reduced-II stages are preserved here as history. The exact
pre-update file is in
\path{records/checkpoint22_prior_master68/notes/part3_remaining_return_obligations.tex}.
'''
reg = ROOT / 'notes/part3_remaining_return_obligations.tex'
old = reg.read_text()
begin = old.index(r'\begin{proof}')
body = old[old.index('\n', begin) + 1:]
reg.write_text(current_register + '\n' + body)

# Keep the preceding global-groupoid proof's original bytes, and make its
# actual period-section and scalar conventions agree with the full K92 map.
for filename in ('notes/part3_source_global_groupoid.tex',
                 'notes/part3_source_global_groupoid_working.md'):
    p = ROOT / filename
    s = p.read_text()
    s = s.replace(r'4\log R-\log(4R)=2(1+i).',
                  r'4\log R-\log(4R)=2\omega_1+2\omega_2.')
    s = s.replace('The signed source part is multiplied by \\(n\\), and its line\npart is the actual Cartier factor of automorphy.',
                  'Here \\(\\omega_1,\\omega_2\\) are the actual transported period\nsections, with central values \\((1,i)\\). The signed source part\nfor \\(L=t_{-nR}\\) is multiplied by \\(-n\\), and its line\npart is the actual Cartier factor of automorphy.')
    marker = 'The latter extends and has identity central source translation'
    addition = ('For the actual fixed scalar \\(r_0\\), the full quotient\n'
                'representative is \\(A^4D^{-4}=S_{r_0^{4n}}L^4\\).\n'
                'P3K.92, equations (IFan.18a--b), supplies its exact\n'
                'endpoint-to-initial arrow on both ordinary and cap charts,\n'
                'including the retained scalar path and its endpoints.\n')
    assert marker in s
    s = s.replace(marker, addition + marker, 1)
    p.write_text(s)

p = ROOT / 'notes/part3_source_moduli_loops_working.md'
s = p.read_text()
separator = s.index('\n---\n')
notice = '''## Current-status notice — 17 November 2026

This file preserves the successive source-coordinate calculations.
P3K.71 completes the selected-cusp return on every lattice-basis fan.
P3K.80, P3K.83 and P3K.85–90 complete the source-zero attachments,
normal clutches, full vertical integers and every-fan algorithm.
P3K.92 completes the marked E7 infinity boundary with its full
source/Cartier/root/endpoint dictionary. Earlier unresolved stages
below describe their original date. The current remaining sectors
are recorded in P3K.75; all displayed coordinate maps retain their
stated uses. The preceding notice and full file are preserved in
records/checkpoint22_prior_master68.
'''
p.write_text(notice + s[separator:])

mapping_path = ROOT / 'code/part3/results_mapping.json'
mapping = json.loads(mapping_path.read_text())
new_entries = []
for n, stem in FILES.items():
    new_entries.append({
        'id': f'P3K.{n}', 'status': 'Proved', 'item_of_prompt': '3.4',
        'statement': DESCRIPTIONS[n],
        'proof': f'notes/{stem}_working.md',
        'latex_file': f'notes/{stem}.tex',
        'source_sha256': sha(ROOT / f'notes/{stem}_working.md'),
        'include_sha256': sha(ROOT / f'notes/{stem}.tex'),
        'certificate': CERTIFICATES[n],
        'visual_qa': f'records/k{n}_standalone_visual_qa.json',
        'provenance': ('Fresh mathematical reconstruction after checkpoint19 recovery; old hashes remain historical.'
                       if n < 92 else 'New full proof after verified checkpoint21.'),
    })
mapping['post_recovery_completed_return_results'] = new_entries
mapping_path.write_text(json.dumps(mapping, indent=2) + '\n')

summary = (
    'INCOMPLETE. P3K.85–91 have been reconstructed, mathematically reread, independently checked and freshly rendered. '
    'K85 gives the reduced-II positive physical pair (2mh,24k(3l+1)) and integer 3kl. '
    'K86 computes the complete source-zero normal correction Gamma=0. '
    'K87 computes every reduced-II canonical fan. K88 supplies all 28 fixed-scalar source-zero classes on each branch. '
    'K89 gives the full source-zero vertical physical pair (mu+6A_j,4mu), with mu=2-a+6pk and '
    'A_j=2b*binom(j+1,3)+(3-b)*binom(j+1,2)+k(a-1)(3p-1)-km*binom(j,2). '
    'K90 carries these full integers to every GL2Z fan; 65,040 exact inputs and the independently solved 1,020 target systems pass. '
    'K91 computes the reduced-II full root-groupoid class, every marked ordinary clutch and every fixed-source holomorphic endpoint. '
    'Its exact norm is D=h*n_A+m*n_B+mh*sigma; H2 is Z plus Z/k plus Z/h. '
    'The actual shortest parameter has pair (2kh,8k(3l+1)), integer kl and all-fan winding iterates. '
    'K92 completes every fan of the marked E7 infinity boundary: I_a(P)=-Z_a(P)-Z_a(JP)-C(P) modulo 28, '
    'with the full finite-root scalar, transported period and inverse closing. Vertical values are 1-a; Q0 squared gives 10 and 7. '
    'K71–74 and K76–84 retain their proved prior scopes and corrections. '
    'Remaining work comprises the other marked source-moduli generators, further singular-site sectors and endpoints outside these completed families. '
    'The E6 r=0 and r=1/4 actual source/root/Cartier attachments are advancing; unfinished attachments have no assigned return.'
)
up = ROOT / 'code/update_report.py'
s = up.read_text()
s = re.sub(r"^'3\.4':.*$", "'3.4':(" + repr('P3F.1–P3F.56, P3K.5–P3K.92') + ', ' + repr(summary) + '),', s, flags=re.M)
old_obligations = re.search(r"'INCOMPLETE\. K71 now computes.*?','',", s).group(0)
new_obligations = summary + (
    ' The current detailed obligation register is P3K.75. All superseded formulas and attempted attachments remain in their named history records. '
    'Parts 1, 2 and the original blind Part 5 retain their independently recorded proofs; the Part 5 hashes remain immutable. '
    'Part 4.2 is proved in the requested irreducible or normal-crossing scope. The broader supplied assertion about arbitrary non-normal-crossing supports remains separately undecided. '
    'The environment recovery is recorded in records/recovery_20261117. Every checkpoint19 byte was independently restored; '
    'post19 proofs were reconstructed and newly verified. The lost master70 PDF is not claimed to have been recovered. '
    'Checkpoint21 was independently restored in full and saved successfully, with 7,812 verified files. '
    'The current rebuilt manuscript has its own numbered build, hashes, logs and visual audit.'
)
s = s.replace(old_obligations, repr(new_obligations) + ",'',", 1)
up.write_text(s)

# Supply the existing report writer's complete progress-record schema while
# retaining every earlier field and the exact original record in the archive.
p = ROOT / 'records/progress_check_21_hours.json'
r = json.loads(p.read_text())
r.setdefault('checked_utc', r['utc'])
r.setdefault('reason', 'The main return problem advanced through complete recovered source-zero and reduced-II proofs; the E6 source attachments and E7 infinity groupoid calculation continued.')
r.setdefault('other_open_item_progress', ['Recovery restored and checked every checkpoint19 file; post19 reconstruction provenance and fresh reviews remain explicit.'])
r.setdefault('next_progress_check_due_utc', r['next_due_utc'])
p.write_text(json.dumps(r, indent=2) + '\n')

record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'status': 'INTEGRATED_PENDING_MASTER_BUILD_AND_VISUAL_REVIEW',
    'archive': str(archive.relative_to(ROOT)),
    'statements': new_entries,
    'retained_master68_sha256': sha(archive / 'S6_06_BLIND_paper.pdf'),
    'part5_sha256': {name: sha(ROOT / name) for name in ('notes/part5.tex', 'notes/part5_blind.md')},
}
(ROOT / 'records/recovery_20261117/master_integration.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'status': record['status'], 'statements': list(FILES), 'archive': record['archive']}, indent=2))
