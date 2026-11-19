"""Exact receiving clarifications from the complete K10/K22 local reviews."""
legacy_local_edits=[]
def legacy_exact(t,label,old,new,reason):
 assert t.count(old)==1,(label,old[:80],t.count(old))
 legacy_local_edits.append(dict(label=label,old=old,new=new,reason=reason))
 return t.replace(old,new,1)

def local_k10(t):
 t=legacy_exact(t,'night:P3K.10',
 r'''The resulting construction of Engel's Remark 8.5 gives a proper
holomorphic family''',
 r'''Use the canonical whole-zero reference cusp filling of
\cref{night:P3K.69}(1), with its standard vertical-edge fan,
chosen lattice and the page collars constructed below.
The resulting construction of Engel's Remark 8.5 gives a proper
holomorphic family''',
 'Name the actual reference fan and collars used by the proved page calculation; no all-fan assertion is added.')
 t=legacy_exact(t,'night:P3K.10',
 r'''For an independent local chain verification, use the actual
dual-moment-cell quotient and blowup-collapse comparison of P1.11
in rank two, with \(G=3I_2-\mathbf1\mathbf1^t\).''',
 r'''The complete integral specialization and its full unit-preserving
family map are constructed in \cref{iv:rank_two_specialization}.
Its explicit character map \((z_1,z_2,q)\mapsto(z_1,z_2^{-1},q)\),
together with inversion of the second period generator, identifies
the two unit-square diagonals. Its forwards and backwards flows
carry the actual holomorphic period units and the entire
specialization diagram. In that marked rank-two dual-moment-cell
model use \(G=3I_2-\mathbf1\mathbf1^t\) for the following
independent integral chain computation.''',
 'Supply the actual all-degree rank-two specialization morphism and both fan/unit maps, rather than relying on an implicit specialization of the rank-three P1.11 statement.')
 t=legacy_exact(t,'night:P3K.10',
 r'''The double cusp
deck changes this angular difference by \(2\theta\delta\),
so the retained line gauge has winding two.''',
 r'''The double cusp
deck changes this angular difference by \(2\theta\delta\).
This is the actual transition of the varying family gauge;
at \(\theta=1\) its integral endpoint winding is \(2\delta\).
The displayed intermediate transition is retained throughout
\(0\leq\theta\leq1\).''',
 'Keep the full varying boundary gauge and distinguish its computed integral endpoint from its intermediate real parameter values.')
 return add_uses(t,r'\cref{night:P3K.68,night:P3K.69,iv:rank_two_specialization}; only the retained trace, page and collar maps of \cref{night:P3K.6,night:P3K.7}, transported by the physical duality')
change('night:P3K.10',local_k10,
 'After complete rederivation of the retained source, line, topology and corrected physical return, state the exact reference fan, complete rank-two specialization map and endpoint gauge scope.')

def local_k22(t):
 t=legacy_exact(t,'night:P3K.22',
 r'''The exact orbit Mayer--Vietoris computation
below gives, whenever its first-homology gluing matrix is unimodular,
\[
        H_2(Y;\mathbb Z)=\bigoplus_i(\mathbb Z/m_i)^2.       \tag{P3K.22.1}
\]
Consequently a sphere member with only such smooth-site modifications
has \(m_i=1\) at every site.''',
 r'''For all these primitive data, the actual orbit Mayer--Vietoris
maps below give the exact sequence
\[
 0\longrightarrow\bigoplus_i(\mathbb Z/m_i)^2
 \longrightarrow H_2(Y;\mathbb Z)
 \longrightarrow\ker D_1\longrightarrow0,                \tag{P3K.22.1}
\]
where \(D_1\) is the fully displayed first-homology gluing matrix.
The left map is induced by the exterior rim cycles after the
specified cap relations, and the right map is the actual
Mayer--Vietoris boundary. A sphere member has surjective square
matrix \(D_1\), hence \(\ker D_1=0\); its degree-two group
is exactly the displayed torsion group. Consequently every such
sphere member has \(m_i=1\) at every site.''',
 'State the actual unconditional Mayer--Vietoris exact sequence for all primitive cap data, then derive the sphere restriction from its maps.')
 t=t.replace('P3K.10 and P3F.25.',r'\cref{night:P3K.10,night:P3F.24}.',1)
 t=t.replace(r'\cref{night:P3F.25}',r'\cref{night:P3F.24}',1)
 old='This proves (P3K.22.1), including its torsion.'
 new=r'''The Mayer--Vietoris boundary gives the exact sequence
\(0\to\operatorname{coker}D_2\to H_2(Y)\to\ker D_1\to0\).
The displayed rim presentation identifies its first term with
\(\bigoplus_i(\mathbb Z/m_i)^2\): multiplication by an inverse
of \(n_i\) modulo \(m_i\) eliminates \(C_i\), leaving the
two independent residues of \(A_i,B_i\). The inclusion is the
one induced by those actual exterior cycles. This proves the
entire exact sequence (P3K.22.1), including its torsion.'''
 t=legacy_exact(t,'night:P3K.22',old,new,
                'Identify both maps of the all-data exact sequence and the explicit residue elimination, without assuming an open hypothesis.')
 return add_uses(t,r'\cref{night:P3K.68,night:P3K.69,night:P3F.24}; the actual retained source, cap and page comparisons in the stated fixed reference fan')
change('night:P3K.22',local_k22,
 'Retain the complete primitive-source proof with its corrected physical sign, replace the obsolete F25 detection reference by the proved F24 map, and state the all-data degree-two exact sequence explicitly.')
(W/'analysis/IV/K10_K22_receiving_reconciliation.json').write_text(json.dumps(legacy_local_edits,indent=2)+'\n')
