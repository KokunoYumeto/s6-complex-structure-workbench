#!/usr/bin/env python3
"""Apply the explicitly proved physical/dual-line dictionary to B6.17/20.

Only receiving authoring statements are changed. Original blocks and hashes
are preserved in the receipt. Re-running is safe after the metadata pass.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

P=Path(__file__).resolve().parents[2]
receipt=P/'analysis/continuation_IV/reference_line_statement_patch.json'
changes=[]
for rel in ['papers/IV/body.tex','papers/IV/body_source.tex']:
    path=P/rel;s=path.read_text()
    for label,env in [('maps:src:B.6.17','proposition'),('maps:src:B.6.20','theorem')]:
        i=s.index('\\label{'+label+'}')
        start=s.rfind('\\begin{'+env+'}',0,i)
        end=s.index('\\end{'+env+'}',i)+len('\\end{'+env+'}')
        before=s[start:end]
        if 'continuation: explicit physical/dual line' in before:continue
        after=before
        if label.endswith('17'):
            old='be the principal circle bundle, with Euler class $x$.'
            new=r'''be the principal circle bundle. We use the associated-line convention
\(U=M^{-1}\) of \cref{night:P3K.68}, where \(M\) is the genuine
physical nonzero-vector line, and put \(x=c_1(U)\).
The exact map on nonzero vectors sends \(v\in M\) to the unique
functional \(D(v)\in M^{-1}\) with \(D(v)(v)=1\); thus
\(D(cv)=c^{-1}D(v)\), so it inverts the physical circle character.
% continuation: explicit physical/dual line'''
            assert old in after,(rel,label,'Euler sentence missing')
            after=after.replace(old,new,1)
            old=r'''This computes the integer $\ell$ in \ref{maps:src:B.6.15}, with these
orientations.  It does not compute $k$ in $x^2=ky$ or the
relative Pontryagin number of the parametrized surgery trace.'''
            new=r'''This gives \(\ell_U=-4\) in \ref{maps:src:B.6.15}.
Keep the quotient orientation fixed. For the physical line put
\(x_M=-x\) and \(y_M=-y\). Then
\(\langle x_My_M,[Q]\rangle=\langle xy,[Q]\rangle=1\), and
\(p_1(Q)=4y_M\), so \(\ell_M=4\). These assertions follow from
the displayed dual-line map on the same oriented quotient.
The cup coefficient in \(x^2=k_Uy\) and the relative Pontryagin
number of the parametrized surgery trace are not computed here.'''
            assert old in after,(rel,label,'closing sentence missing')
            after=after.replace(old,new,1)
        else:
            old=r'''parameter mapping torus. Its primitive Euler class $e$ satisfies
$|\langle e^3,[Q]\rangle|=1$. In the oriented convention of \ref{maps:src:B.6.17},
$\ell=-4$, hence the spin congruence of \ref{maps:src:B.6.15} gives $k=-1$.'''
            new=r'''parameter mapping torus. In the explicit convention of
\cref{maps:src:B.6.17,night:P3K.68}, its primitive class is
\(e=c_1(U)\), where \(U=M^{-1}\) is the meridian-one dual of the
physical line. It satisfies \(|\langle e^3,[Q]\rangle|=1\).
Here \(\ell_U=-4\), and the spin congruence of
\ref{maps:src:B.6.15} gives \(k_U=-1\).
With the same quotient orientation, the dual-line morphism gives
\(x_M=-e\), \(y_M=-y\), and hence
\[
 (k_U,\ell_U)=(-1,-4),\qquad (k_M,\ell_M)=(1,4).
\]
Indeed \(x_M^2=e^2=-y=y_M\) and \(p_1(Q)=-4y=4y_M\).
Both pairs have index \((4k-\ell)/24=0\).
% continuation: explicit physical/dual line'''
            assert old in after,(rel,label,'statement sentence missing')
            after=after.replace(old,new,1)
        s=s[:start]+after+s[end:]
        changes.append(dict(file=rel,label=label,before=before,after=after,
          before_sha256=hashlib.sha256(before.encode()).hexdigest(),
          after_sha256=hashlib.sha256(after.encode()).hexdigest()))
    path.write_text(s)
if changes:
    payload=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
      checker='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation',
      scope='Exact dual-line statement dictionary; prior full geometric proof not independently rederived by this patch',
      evidence=['analysis/continuation_ledger/dual_line_prederivation.md','code/continuation_ledger/dual_line_and_B620_determinants.py','papers/IV/body.tex: night:P3K.68 PL.2a and PL.6'],changes=changes)
    receipt.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'blocks_changed':len(changes),'receipt':str(receipt)},indent=2))
