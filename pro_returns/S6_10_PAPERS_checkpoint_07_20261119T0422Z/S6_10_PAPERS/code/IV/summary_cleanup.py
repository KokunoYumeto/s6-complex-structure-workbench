"""Keep the fixed-family summary as a numbered deduction; archive its history."""
def cleanup_b62(t):
 end=t.index(r'\end{theorem}')+len(r'\end{theorem}')
 archive=W/'analysis/IV/full_rederivations/B6_2_historical_apparatus.tex'
 archive.parent.mkdir(parents=True,exist_ok=True);archive.write_text(t[:end]+'\n')
 start=t.index('The original class')
 head=t[:start]
 head=head.replace('Definitions and the displayed constructions',
  r'\cref{maps:src:B.6.21}; \cref{maps:src:B.6.22}; \cref{maps:src:B.6.23}; \cref{maps:src:B.6.24}; \cref{maps:src:B.6.25}')
 statement=r'''The original class is \(a=0\). For every sphere-producing member
\(X_{3k,4l}\) with these retained reference data, its class for the
positive parameter loop of period \(2kl\) is also zero. Each resulting
mapping torus has the spin filling of \cref{maps:src:B.6.25}, with one
zero-handle and one one-handle.
\end{theorem}
\begin{proof}
\begin{enumerate}[label=\arabic*.]
\item The original reference-family calculation is
\cref{maps:src:B.6.21}, which uses the actual normal replacement,
oriented quotient cup form and spin trace of
\cref{maps:src:B.6.16,maps:src:B.6.17,maps:src:B.6.19,maps:src:B.6.20}.
It gives the original class zero with its specified positive loop.
\item For the general coprime pair, \cref{maps:src:B.6.22} constructs
the replacement with the same source fan, lattice basis and collars,
and gives \(\ell=-4kl\). The actual integral generator change and
cap calculation in \cref{maps:src:B.6.23} give
\(k_{\mathrm{cup}}=-kl\) for the positive period \(2kl\).
The complete torsion-generator and rank-one-sign comparison in
\cref{maps:src:B.6.24} applies to precisely these maps and integers;
its two rational characteristic contributions cancel. Hence this
member's original smooth sphere return is zero.
\item The isotopy and its actual mapping-torus identification in
\cref{maps:src:B.6.25} extend both parameter spin structures across
\(D^7\times S^1\), with the stated two handles. The earlier
unsuccessful approaches remain in the unchanged source compendium
and the archived apparatus; none is a premise of this deduction.
\end{enumerate}
\end{proof}
'''
 return head+statement+t[end:]
change('maps:src:B.6.2',cleanup_b62,
 'Apply the independent summary review: retain the exact reference-data conclusion and a short numbered deduction from B6.21–25; archive the historical failed approaches rather than treating them as an additional proof.')
