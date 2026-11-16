# Bounded independent check of the cusp block argument

The six-manifolds worker independently checked the proposed actual
stratum blocks before the E.2.21 full root audit.

1. Two triple-point six-balls, three annulus blocks
   `S1 x D1 x D4`, and the dense block `T2 x D2 x D2` have the
   asserted ordinary handle counts `(2,3,4,2,1)`. These counts follow
   by literal circle cutting, not from the earlier CW counts.
2. Both complex normal lines over the double annuli are trivial.
   Their relative endpoint rotations must nevertheless be retained:
   `(z,a,b) -> (1/z,za,zb)`. The E.2.21 table retains both rotations.
3. On the compact free toric moment region, q itself is the normal
   coordinate up to a nowhere-zero toric factor. Consequently the
   exact truncated condition is `(T2 x P) x D2_q`, including its
   interface over the entire boundary of P. It preserves the q angle.
4. The annular `|ab|` and triple `|abc|` truncations are rounded
   star-shaped normal domains. Nested moment cuts can be chosen to
   meet that same boundary of P; no additional disk-bundle block is
   needed. The degree minus one twists occur in the attachments.
5. Changing to a smaller full tube changes only an exterior collar,
   where q has no critical point. Its radial lifting field is fixed
   in the prescribed real torus coordinates on the marked outer
   collar, so no additional boundary diffeomorphism is introduced.

This bounded check does not substitute for the parent's full audit
of E.2.21, the two global torus bands, finite caps and dual product.

## Final audits and integration

Root subsequently passed the complete geometric proof, independently
replayed the exact76/2432-handle certificate, and visually read the
original Milnor statements used for relative uniqueness: Theorem1.4
at printed p25, Theorem3.13 at p31, Theorem5.8 at pp63–64.
The scanned PDF pages are31,37,69–70, respectively. Fourfolds
independently passed an adversarial review of all full framed
attachments and the interpretation of the complete smooth-type
identification. The final comparison includes all top handles and
does not assume that an arbitrary sphere map extends over a disk.

E.2.21 was approved for registration and input by root on
2026-11-16, before checkpoint10. The proof is now in
sections/maps_ordinary_handles.tex, the complete inventory in
code/maps_ordinary_handles.out.json, and the local build logs in
records/maps_handles_build_1.log and maps_handles_build_2.log.
