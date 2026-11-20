"""Apply the root-reviewed current-program, scope and locator replacements once."""
from pathlib import Path
import datetime,hashlib,json,re
R=Path(__file__).resolve().parents[1]
changes=[]
for paper,rel in [('II','audit_sign/II_guarded_scope_source_patches.json'),('IV','audit_sign/K111_postintegration_locator_guard.json'),('V','audit_corrections/V_guarded_patches_06.json'),('V','audit_sign/V_P115_receiving_guard_06.json')]:
    p=R/f'parts/{paper}.body.linked.tex';s=p.read_text();before=hashlib.sha256(p.read_bytes()).hexdigest()
    patches=json.loads((R/rel).read_text())
    for x in patches:
        count=x.get('expected_count',x.get('matches',1))
        if paper=='IV':
            x['old_text']='The entire bounded Cox lift and its inverse\nare RFB.17.'
            x['new_text']='The entire bounded Cox lift and its inverse\nare RFB.16.'
        if rel=='audit_sign/V_P115_receiving_guard_06.json':
            x['new_text']=x['new_text'].replace(r'\texttt{audit\_sign/code/V\_P115\_extension\_independent\_06.py}',r'\path{code/current_audits/audit_sign/code/V_P115_extension_independent_06.py}').replace(r'\texttt{audit\_sign/V\_P115\_extension\_independent\_06.json}',r'\path{code/current_audits/audit_sign/V_P115_extension_independent_06.json}')
        if s.count(x['old_text'])==0 and s.count(x['new_text'])==count:
            x['integration_state']='Exact replacement was already present before this run; no new source edit.'
            continue
        assert s.count(x['old_text'])==count,(paper,x['label'],s.count(x['old_text']))
        s=s.replace(x['old_text'],x['new_text'])
    p.write_text(s)
    changes.append(dict(paper=paper,patch_file=rel,patch_sha256=hashlib.sha256((R/rel).read_bytes()).hexdigest(),before_sha256=before,after_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),patches=patches))
p=R/'parts/III.body.linked.tex';s=p.read_text();before=hashlib.sha256(p.read_bytes()).hexdigest();patches=[]
def replace(old,new,reason):
    global s
    assert s.count(old)==1,(reason,s.count(old))
    s=s.replace(old,new,1);patches.append(dict(old_text=old,new_text=new,reason=reason))
start=s.index('In the actual twenty-three-row relation matrix')
end=s.index('All columns of \\(M\\)',start)
replace(s[start:end],r'''We construct the twenty-three-row core matrix of
\ref{maps:src:D.2.46} in the integral graph basis embedded by
\(K:\mathbb Z^{17}\hookrightarrow\mathbb Z^{20}\), obtained from the
Smith form of \(D=(A_0-I,\ldots,A_4-I)\).
The program \path{code/III_OS45_core_independent.py} records this
embedding, its integral left inverse, and all sixty-four columns
with their exterior, cap or normal-prism origins. Thus its coordinate
map to the actual bar complex is the one in \ref{maps:src:D.2.46}.
For this \(23\)-by-\(64\) matrix \(M\), augment \(z\) by seventeen zeros.
With columns numbered from zero, a literal integer preimage is
\[
\begin{aligned}
&\begin{array}{c|rrrrrrrr}
j&0&2&4&9&10&12&13&14\\\hline
c_j&48&-16&2&8&2&-2&-52&-8
\end{array}\\[3pt]
&\begin{array}{c|rrrrrrr}
j&20&37&42&47&52&57&61\\\hline
c_j&2&10&10&10&10&10&10
\end{array}
\end{aligned}                                             \tag{D.OS8}\label{maps:eq:D.OS8}
\]
Direct multiplication gives \(Mc=(z,0)\).
''','Replace unavailable historical column indices with the actual reconstructed basis embedding and exact full null chain.')
start=s.index('Choose the integral cycle basis and the integral left inverse')
end=s.index('\\paragraph{A full boundary comparison',start)
replace(s[start:end],r'''Choose the integral cycle embedding \(K\) and its integral left
inverse \(K^+\) recorded in \path{code/III_OS45_core_independent.py}.
The ordinary degree-two cycles are the six fibre cells followed by
these seventeen graph cycles. Its actual relation matrix \(M\) is
the matrix used in \eqref{maps:eq:D.OS8}. The saved integral maps
\(U,V\) give \(UMV=\operatorname{diag}(1^{22},8)\), with the
remaining columns zero.

We specify a literal cochain on the twenty ambient graph coordinates,
ordered in five blocks \((e_1,e_2,\delta,\gamma)\). Put
\[
\begin{aligned}
\theta={}&(0,4,0,12;\ 0,0,0,0;\ 0,7,0,4;\ 5,0,0,4;\ 1,6,0,0),\\
r={}&(0,6,0,17;\ 0,0,0,0;\ 0,0,0,0;\ 0,0,0,0;\ 0,0,0,0),\\
\theta'={}&\theta+8r,\qquad
\varphi=((1,0,0,0,0,0),\theta'K).
\end{aligned}
\]
The program verifies every degree-three boundary column and gives
\[
\varphi M=0\pmod8,\qquad
\varphi|_{\Lambda^2\Lambda}=(1,0,0,0,0,0).              \tag{D.OF2}\label{maps:eq:D.OF2}
\]
For the negative Smith generator \(g=-U^{-1}e_{22}\), with zero-based
indices, it gives \(\varphi(g)=-1\pmod8\). Hence this cochain is
primitive on the order-eight core image.

The ambient graph row is \(\theta'\) itself: its restriction to the
integral cycle lattice is exactly \(\theta'K\). The fixed bar-prism
comparisons of \ref{maps:src:D.2.46} transport this literal cochain to
the actual torus bundle. Its finite-coefficient class is unchanged
by the displayed addition \(8r\), and its boundary restriction is
specified on all ambient generators, including the coefficient-extension
part arising from the core's degree-one torsion.

Let \(J_{\rm raw}\) be the actual rank-two cusp peripheral map into
the twenty graph coordinates, retained with its bar-prism comparison.
The explicit ambient row gives
\[
\theta'J_{\rm raw}=(0,52,0,148)
       \quad\hbox{on }(e_1,e_2,\delta,\gamma).             \tag{D.OF3}\label{maps:eq:D.OF3}
\]
The quadratic correction on each of these four basis loops is zero
at this cusp. The two long-strip constants are therefore
\[
                      (c_1,c_2)=(4,4)\quad\hbox{in }k.   \tag{D.OF4}\label{maps:eq:D.OF4}
\]
The complete matrices, integral cochain and all exact checks are in
\path{code/outputs/III_OS45_core_independent.json}.

''','Use the literal ambient cochain, its exact graph restriction and the explicitly oriented Smith generator; preserve the full finite-coefficient boundary map.')
replace(r'\path{records/maps_weighted_os45_mu.json}',r'\path{code/outputs/III_OS45_annulus_independent.json}','Name the reconstructed full component table.')
old=r'''\path{code/III/maps_weighted_os45_mu.py} checks the exact Smith
cochain, both full affine strip constants, all sixteen wall
restrictions, the full shifted annulus map, every primitive
mixed entry and the complete moduli in \eqref{maps:eq:D.OF18}.
The independent fourfolds programs check all primitive cubic
entries and all-character localization identities.'''
new=r'''The supplied program \path{code/III_OS45_core_independent.py}
reconstructs the full core matrix, its Smith maps, the critical null
chain and the literal boundary cochain.
\path{code/III_OS45_annulus_independent.py} computes the full shifted
annulus map by both rectangular paths, all sixteen component
restrictions and every primitive mixed entry.
\path{code/III_OS45_primitive_cubic_independent.py} computes all
primitive cubic entries and their exact component-basis transport;
\path{code/III_weighted_OS45_checks.py} checks the support, power and
all-character localization identities in their displayed moduli.
Each program's exact JSON output is in \path{code/outputs/}.'''
replace(old,new,'Match every computational claim to its actual supplied independently reconstructed program and full output.')
p.write_text(s);changes.append(dict(paper='III',before_sha256=before,after_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),patches=patches))
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),review='Root read all proposed replacements and relevant receiving statements/proofs. P1A6 explicitly states the proper smooth family scope used in its local miniversality and torsor proof. New III code is after-reading reconstruction, not a blind proof or replay of an unavailable historical program.',changes=changes)
(R/'analysis/current_certificate_integration_06.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'papers':[c['paper'] for c in changes],'guards':sum(len(c['patches']) for c in changes)}))
