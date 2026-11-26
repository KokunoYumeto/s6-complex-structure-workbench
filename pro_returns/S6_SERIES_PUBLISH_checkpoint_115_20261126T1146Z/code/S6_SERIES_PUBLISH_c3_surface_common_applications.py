from S6_SERIES_PUBLISH_c3_edit import *

s=SOURCE.read_text();after=s
changes=[]
def change(old,new,key,stmt,reason):
    global after
    assert after.count(old)==1,(key,after.count(old))
    after=after.replace(old,new,1)
    changes.append((key,stmt,old,new,reason))
def block(label,kind):
    i=s.index('\\label{'+label+'}',s.index('\\begin{document}'))
    a=s.rfind('\\begin{'+kind+'}',0,i);b=s.index('\\end{proof}',i)+len('\\end{proof}')
    return s[a:b]
owners=[block('lem:II:hopf-curves','cited'),block('lem:II:single-conductor-branch','lemma'),block('lem:II:irrational-ruled-boundary','lemma')]
for x in owners:
    assert after.count(x)==1;after=after.replace(x,'',1)
marker='\\begin{proposition}[Finite rank drop of a normalization]'
assert after.count(marker)==1
after=after.replace(marker,'\n\n'.join(owners)+'\n\n'+marker,1)

p=after.index('\\item Consider the two latter alternatives.')
q=after.index('\\item On a Hopf surface every irreducible curve',p)
old=after[p:q]
new=r'''\item Consider the minimal elliptic ruled alternative. Apply \cref{lem:II:irrational-ruled-boundary} with $T_0=T$, $\beta=\operatorname{id}_T$ and this same conductor divisor $D$. Its reduced-horizontal case already makes $R$ a disjoint union of smooth elliptic curves. Its other case has $D=2H+\sum_j a_jF_j$, with $H$ a smooth elliptic section and distinct rational fibres $F_j$ meeting it once. Writing $v$ for their number gives $e(R)=v$ and
\[
 e(S_{\rm reg})=e(T\setminus R)=e(T)-e(R)=-v.
\]
Proposition~\ref{night:P4.13} forces $v=0$. Thus $R$ consists of smooth elliptic curves in this case as well.

'''
change(old,new,'IMMERSIVE-RULED','night:P4.15','Apply the general numerical boundary owner to the identical minimal surface and divisor with identity blowdown; retain the v-count and e(Sreg) obstruction.')
p=after.index('\\item On a Hopf surface every irreducible curve')
q=after.index('\\item At a point of $C=\\operatorname{Sing}(S)',p)
old=after[p:q]
new=r'''\item In the Hopf alternative, \cref{lem:II:hopf-curves}, applied to this same $T$, makes the reduced conductor $R$ a disjoint union of smooth elliptic curves.

'''
change(old,new,'IMMERSIVE-HOPF','night:P4.15','Use the earlier cited curve classification on the identical Hopf surface, preserving the complete conductor conclusion.')
p=after.index('\\item At a point of $C=\\operatorname{Sing}(S)')
q=after.index('Globally the restriction $\\nu|_R:R\\to C$ is finite and unramified.',p)
old=after[p:q]
new=r'''\item Apply \cref{lem:II:single-conductor-branch} to the finite normalization $\nu:T\to S\subset Y$, with $A=R$ and $C=\operatorname{Sing}(S)_{\rm red}$. The preceding cases give its unique smooth conductor branch at each point of $T$. Since $j:T\to Y$ is immersive, each image branch is smooth and the curve map is a local isomorphism. The lemma identifies all image branches at each point of $C$, so $C$ is smooth there.
'''
change(old,new,'IMMERSIVE-IMAGE','night:P4.15','Apply the exact finite-normalization branch lemma after the immersion and conductor hypotheses have been proved; its unique image branch and the derivative give the same unramified conclusion.')

old=r'''In this latter case the generic transverse conductor
exponent of every normalization branch is one. The
exponent is its intrinsic conductor exponent plus the
intersection multiplicities with the other branches.
A singular branch has intrinsic exponent at least two.
Exponent one therefore means two smooth branches
meeting transversely.'''
new=r'''In this latter case the generic transverse conductor exponent of every normalization branch is one. Apply \cref{lem:II:plane-branch-conductor} to this same reduced transverse plane equation; its exponent-one conclusion gives two smooth transverse branches.'''
change(old,new,'RATIONAL-TRANSVERSE','night:P4.21','The original reduced transverse equation and its normalized branch exponents satisfy the earlier common conductor formula.')
p=after.index('The exact sequence\n\\[\n0\\longrightarrow T_T',after.index('\\label{night:P4.21}'))
q=after.index('The reduced nodal anticanonical conductor',p)
old=after[p:q]
new=r'''Apply \cref{night:P4.15} to the same finite normalization $\nu:T\to S$ and its immersion into $Y$. Its maximal-minor ideal is the unit ideal, so $\ell=0$. The rational alternative of that proposition gives $e(T)=6$.
'''
change(old,new,'RATIONAL-CHERN','night:P4.21','The exact differential map in P4.15 is this same everywhere-immersive map; its length is zero and its rational conclusion supplies the already proved Chern/Noether value.')
p=after.index('Triangulate the analytic pair $(T,D_{\\mathrm{red}})$ and the finite',after.index('\\label{night:P4.21}'))
q=after.index('Every component of $C$ has rational normalization',p)
old=after[p:q]
new=r'''Apply \cref{lem:II:proper-conductor-pushout} with $(X,Y,A,C,h)=(T,S,D_{\rm red},C,\nu)$. The finite normalization identifies the complementary open sets, the boundary is connected, and its inclusion is a cofibration by analytic triangulation. Both $\pi_1(D_{\rm red})$ and $\pi_1(T)$ are trivial, so the inclusion induces an isomorphism and the lemma gives $\pi_1(S)\simeq\pi_1(C)$ through $C\hookrightarrow S$.
'''
change(old,new,'RATIONAL-PUSHOUT','night:P4.21','Apply the common proper-map quotient and van Kampen result with the identical finite normalization and its complete conductor; both left groups are already proved trivial.')
old=r'''For $g\ge2$, the adjunction and
Riemann--Hurwitz argument in the proof of \cref{night:P4R.7}
excludes a coefficient-one horizontal component.'''
new=r'''For $g\ge2$, apply \cref{lem:II:irrational-ruled-boundary} to the same minimal ruling and the pushforward of $D$. Its adjunction and Riemann--Hurwitz inequalities exclude a coefficient-one horizontal component.'''
change(old,new,'EQUALITY-BOUNDARY','night:P4.32','Point to the precise earlier owner of the inequalities after the proper-resolution theorem was consolidated; the same divisor and ruling are identified.')
for phrase in ['The proofs of \\cref{night:P4R.7}','the proofs of \\cref{night:P4R.7}']:
    if phrase in after:
        new=phrase.replace('proofs','proof')
        assert after.count(phrase)==1
        change(phrase,new,'SINGULAR-PROOF-'+str(len(changes)),'night:P4.51; night:P4.57','The two retained labels now name one proof; correct the grammatical reference without changing its data.')
preserve_identifiers(s,after)
for before,current in zip(identifiers(s),identifiers(after)):
    for name,count in before.items():assert current[name]==count,name
SOURCE.write_text(after,newline='\n')
rows=[]
for key,stmt,old,new,reason in changes:
    for i,kind in enumerate(['D12','D18'] if 'SINGULAR' not in key else ['D11'],1):
        rows.append(dict(change_id=f'II-C3-SURFACE-COMMON-{key}-{i:02}',type=kind,statement_id=stmt,
          old_location='Normalization differential and rational/ruled applications',old_page='working source; final concordance pending',
          new_location='Earlier common owners and exact applications',new_page='integrated build pending',
          old_text=old,new_text=new,reason=reason,
          review_status='Complete original proofs read; complete receiving comparison follows; exposed root.'))
rows.append(dict(change_id='II-C3-SURFACE-COMMON-ORDER-01',type='D14',statement_id='lem:II:hopf-curves; lem:II:single-conductor-branch; lem:II:irrational-ruled-boundary',old_location='Later Hopf and higher-genus ruling subsections',old_page='working source; final concordance pending',new_location='Before the normalization-differential theorem',new_page='integrated build pending',old_text='\n\n'.join(owners),new_text='\n\n'.join(owners),reason='Move the complete unchanged prerequisites before their earliest differential-theorem application. All their dependencies already occur earlier. Every old label/target remains once.',review_status='Root read each complete owner before transfer.'))
print('Defects',append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id'))
set_unit_status('night:P4.14','D12','open','The differential theorem shared Hopf-curve, finite-image branch and ruled-boundary proofs; these are now exact earlier-owner applications. Full receiving reread follows.','code/S6_SERIES_PUBLISH_c3_surface_common_applications.py')
add_event('night:P4.15; night:P4.21; night:P4.32; lem:II:hopf-curves; lem:II:single-conductor-branch; lem:II:irrational-ruled-boundary',
 'II-C3-SURFACE-COMMON-TRANSFER','used and rechecked in this run',
 'Read the complete old finite-rank-drop and smooth rational proofs and all moved owners. Every replacement identifies the same surface, divisor, normalization, immersion and fundamental-group map. The rational Chern value is the ell=0 specialization of the identical earlier differential. The three prerequisites move unchanged before their first use. Complete receiving review follows; no independent or final-page credit.',
 'S6_SERIES_PUBLISH_II.tex: surface common owners',source='code/S6_SERIES_PUBLISH_c3_surface_common_applications.py')
print('Common surface inputs precede their first applications.')
