from S6_SERIES_PUBLISH_c3_edit import *

text=SOURCE.read_text()
a=text.index('\\subsection{Spherical classes at nonimmersive normalization points}')
b=text.index('\\subsection{',a+1)
moving=text[a:b]
new=text[:a]+text[b:]
insertion=new.index('\\subsection{The integral pole divisor on a normalization resolution}')
new=new[:insertion]+moving+new[insertion:]
preserve_identifiers(text,new)
SOURCE.write_text(new,newline='\n')
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',[{
    'change_id':'II-C3-SPHERICAL-EARLIER-OWNER','type':'D14',
    'statement_id':'night:P4.16; night:P4.17',
    'old_location':'After the unibranch-support subsection',
    'old_page':'checkpoint35 source; page concordance at final build',
    'new_location':'After the specialization-group subsection, before the integral pole divisor',
    'new_page':'integrated build pending','old_text':moving,'new_text':moving,
    'reason':'The complete common lattice proof is self-contained. Place it before the pole-divisor proof, which now uses its a=2,n=1 lattice through an explicit linear coordinate isomorphism instead of repeating the Morse-sphere intersection calculation.',
    'review_status':'Moved whole block byte-identically; all permanent identifiers retained.'}], 'change_id')

text=SOURCE.read_text()
a=text.index('At a critical point of $h_a$',text.index('\\label{night:P4R.6}'))
b=text.index('\nThus every exceptional block',a)
old=text[a:b]
new=r"""At a critical point of $h_a$, holomorphic Morse coordinates give
$h_a=c+w_1^2+w_2^2+w_3^2$. The invertible linear change
\[
 x=w_1,\qquad y=w_2+\mathrm i w_3,\qquad
 z=-w_2+\mathrm i w_3
\]
identifies $w_1^2+w_2^2+w_3^2$ with $x^2-zy$.
The lattice calculation in \cref{night:P4.16}, with $a=2$
and $n=1$, gives a compact spherical class of square $-2$
in a nearby fibre of $h_a$. Transport along a path avoiding
the finite critical values, followed by the parameter-family
identification above, puts this class in $h^{-1}(\delta)$.
Since $f=h^m$, that local fibre embeds in the smooth global
fibre $f^{-1}(\delta^m)$, a complex two-torus. The spherical
class lifts to its contractible universal cover $\mathbb C^2$,
so its image in torus homology is zero. Compact representatives
compute the same intersection before and after this open
inclusion, contradicting their square $-2$.
"""
apply_edit(old,new,'II-C3-POLE-SPHERICAL-APPLICATION',['D12'],
    'night:P4R.6','Conductor and exceptional pole divisor, item4',
    'The explicit linear isomorphism sends the Morse quadratic to x^2-zy, the a=2,n=1 case of the earlier common lattice calculation. The already established boundary/parameter transport, inclusion into the same torus fibre and intersection contradiction remain. No statement or hypothesis changes.')

text=SOURCE.read_text()
a=text.index('\\item Its nearby fibre contains the real vanishing sphere',text.index('\\label{night:P4.20}'))
b=text.index('\n\\end{enumerate}',a)
old=text[a:b]
new=r"""\item The linear coordinates
$x=w_1$, $y=w_2+\mathrm i w_3$ and $z=-w_2+\mathrm i w_3$
identify its Morse quadratic with $x^2-zy$.
By \cref{night:P4.16}, with $a=2$ and $n=1$, the nearby
fibre has a compact spherical class of square $-2$.
The boundary transport in the third item puts this class
in the original torus fibre, where its square must be zero.
Hence the original branch gradients are independent
everywhere, proving the normal-crossing assertion.
"""
apply_edit(old,new,'II-C3-DOUBLE-STRATA-SPHERICAL-APPLICATION',['D12'],
    'night:P4.20','Ordinary double strata and normal crossings, final item',
    'The same explicit invertible linear coordinate map identifies this Morse quadratic with the common lattice calculation. The full prior boundary-transport argument applies unchanged and yields the same contradiction.')

apply_edit(r'\StatementRecord{night:P4.19}{proved}{02WQ}{\SeriesRef{night:P4.16}, \SeriesRef{night:P4.18}}',
    r'\StatementRecord{night:P4.19}{proved}{02WQ}{}',
    'II-C3-RAMIFIED-CONDUCTOR-INPUTS',['D14'],'night:P4.19',
    'A ramified conductor with vanishing nearby homology, hidden input declaration',
    'The complete proof computes its conductor ideals and inverse affine-coordinate maps directly; it invokes neither of these declared propositions. Keep its actual self-contained proof and remove two unused dependency declarations. Printed formatting is unchanged.')

orphan="""P4.16 excludes the displayed pinching and ramification germs.
The subsequent arguments retain singular normalizations and
nonimmersive normalization maps and complete their classification
in P4.58."""
rows=[]
for kind in ['D04','D08','D11','D13']:
    rows.append({'change_id':'II-C3-SPHERICAL-ORPHAN-'+kind,'type':kind,
        'statement_id':'night:P4.16','old_location':'Between P4.16 and P4.17',
        'old_page':'checkpoint35 source','new_location':'Common spherical-lattice owner',
        'new_page':'integrated build pending','old_text':orphan,'new_text':'',
        'reason':'This process recap was removed with the two-owner consolidation. It introduces no additional mathematical conclusion; the exact normalization examples stay in the common proof and the later classification retains its own scope.',
        'review_status':'Entire old paragraph read; receiving common proof read in full.'})
append_rows(ROOT/'S6_SERIES_PUBLISH_defects_II.tsv',rows,'change_id')
print('Common lattice owner placed before all three local Morse/cross-cap applications.')
