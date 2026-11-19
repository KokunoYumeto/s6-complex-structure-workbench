from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[2]
A=ROOT/'analysis/continuation_V'
sha=lambda x:hashlib.sha256(x.encode()).hexdigest()
s=(ROOT/'papers/V/body.tex').read_text()
pos=s.index('\\label{maps:src:F.2.37}')
a=s.index('\\begin{proof}',pos); b=s.index('\\end{proof}',a)+len('\\end{proof}')
old=s[a:b]
starts=[m.start() for m in re.finditer(r'\\item\b',old)]
assert len(starts)==6
parts=[old[starts[i]:starts[i+1] if i<5 else old.index('\\end{enumerate}',starts[i])] for i in range(6)]
parts[1]=r'''\item The finite linear orders here are the already proved list of
\cref{maps:src:F.2.2}:
\[
 d\in\{1,2,3,4,5,6,8,10,12\}.
 \tag{F.CN1}\label{maps:eq:F.CN1}
\]
Taking these finitely many powers, checking the fixed kernel,
the product relation and the cusp Smith factors therefore gives
an exact admissibility test. The actual affine order is the
separate retained gluing datum; the construction in item1 gives
its exact relation to the chosen finite lift.

'''
parts[3]=r'''\item To compute the representative, enumerate heights
$1,\ldots,H(T)$ and all integer entries in the stated order.
There are at most
\[
 (2H(T)+1)^{36(k+1)}
 \tag{F.CN2}\label{maps:eq:F.CN2}
\]
integer lists in this box. Retain the invertible tuples satisfying
the ordered product relation and the stated maximal square-zero
primitive cusp condition, which are finite integer tests, and
apply the decision-and-witness algorithm of
\cref{maps:src:F.2.36} to each candidate and the supplied tuple.
Its general rank-three square-zero input permits precisely this
call. A positive answer transfers all finite-order, orientation
and admissibility conditions through its actual integral
conjugator. The supplied tuple itself occurs, with the identity
as a possible witness, so a positive answer is reached in
finitely many tests. The first one is the required representative.
Record the returned convention as
$P_T^{-1}T_iP_T=\operatorname{Can}(T)_i$.
The displayed candidate bound makes no assumption about entries
of $P_T$; the terminating witness construction is the stated
input from \cref{maps:src:F.2.36}.

'''
parts[4]=r'''\item Every simultaneous orbit has a least element in this order.
Its height is at most the height of each supplied member, so
\eqref{maps:eq:F.CN2} includes that global least element.
Equivalent inputs have exactly the same ordered orbit and
therefore the same representative. Conversely, if $T,T'$ have
the same representative, the actual matrix
$Q=P_TP_{T'}^{-1}$ satisfies $Q^{-1}T_iQ=T'_i$ for every slot.
The separate involution convention has the same property by
\cref{maps:src:F.2.38}, with the product of its actual returned
witnesses giving the corresponding map. Conjugation preserves
the ordered finite orders, so the involution sector is preserved
by those same maps. This proves the classification assertion
and its finite stopping rule.

'''
new=old[:starts[0]]+''.join(parts)+old[old.index('\\end{enumerate}',starts[-1]):]
revision=ROOT/'papers/V/revisions/F2_37_canonical_integral_algorithm.tex'
revision.write_text(new+'\n')
receipt={'installed_utc':datetime.now(timezone.utc).isoformat(),'label':'maps:src:F.2.37','new_proof_sha256':sha(new),'revision':str(revision.relative_to(ROOT)),'before_read':'analysis/continuation_V/F2_37_before_read.md','root_auxiliary':'analysis/continuation_root/F2_37_auxiliary_before_read.md','reason':'Use the frozen complete-box decision-and-witness route, cite the already proved finite-order input, and print the exact witness map. Root current items1and3 retained byte for byte. All former proof routes are preserved without an invalidity assertion.','files':[]}
for rel in ['papers/V/body.tex','papers/V/body_source.tex','S6_10_PAPERS_V.tex']:
 p=ROOT/rel; text=p.read_text(); pos=text.index('\\label{maps:src:F.2.37}'); lo=text.index('\\begin{proof}',pos); hi=text.index('\\end{proof}',lo)+len('\\end{proof}'); prior=text[lo:hi]
 out=A/('F2_37_superseded_'+rel.replace('/','_')); assert not out.exists(); out.write_text(prior+'\n')
 p.write_text(text[:lo]+new+text[hi:])
 receipt['files'].append({'path':rel,'old_proof_sha256':sha(prior),'preserved_path':str(out.relative_to(ROOT)),'new_proof_sha256':sha(new)})
(A/'F2_37_replacement_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'installed','sha256':sha(new)}))
