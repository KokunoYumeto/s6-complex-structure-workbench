# Marked-base extension and the remaining axial comparison gap

Status: a re-audit of the proved B.4.4, with an elementary consequence for the location of nonflat fibres. This note makes no new assertion that an arbitrary completion is the prescribed axial model.

## 1. What B.4.4 proves for every r-only semistable filling

Let g: Z -> Delta_r be proper, with smooth four-dimensional total space and reduced normal-crossings centre, and suppose its punctured restriction is the actual six-sphere family after any finite parameter cover. The canonical formula audited in R1 gives K_X^(-2) = f^*O_P1(1) and h0 = 2 on every nonzero fibre. Coherent proper direct image of the relative bi-anticanonical line is torsion-free on the disc, hence locally free of rank two. A frame evaluates to two holomorphic sections on Z. It is not necessary to assume cohomology base change at the centre.

The resulting meromorphic pencil is the exact fibrewise complete bi-anticanonical pencil, up to a projective coordinate change. Its explicit analytic graph is locally the incidence hypersurface va-ub=0 after removal of common divisorial factors. Proper image of the graph's critical locus is an analytic subset of P1 times the disc. The three punctured critical values are intrinsically distinguished by fibre multiplicities 3 and 4 and by the reduced cusp fibre. The horizontal critical-value curve is finite over the disc. Each labelled branch has degree one, so each extends holomorphically through the centre. The cross-ratio normalizing these three branches consequently has meromorphic coefficients. Composing it with the pencil gives exactly the original marked f over the whole punctured disc and extends meromorphically over Z.

Thus B.4.4 is valid for every finite parameter cover, and does not require an extending affine origin or an extending comparison to an auxiliary torus model. This audit found no gap in that argument or in the previous E_B44_referee.md.

## 2. Resolving the graph gives a holomorphic base map

Resolve the reduced graph by a proper analytic resolution that is an isomorphism over its smooth punctured part. The complex-analytic existence and the fact that the modification is supported over the singular locus are supplied by Bierstone--Milman, Theorem 1.6 and the paragraph following it; local finiteness is enough, and properness over a smaller closed disc makes only finitely many operations relevant. The resulting smooth fourfold Z_tilde has a proper holomorphic map

    (f_tilde,r): Z_tilde -> P1 x Delta_r,

whose restriction over r != 0 is the exact marked original family. The composed map to the r-disc is flat: its local rings are domains and r is not identically zero, so they are torsion-free over the one-dimensional regular local base. The compactness/properness statement follows by composing the proper graph projection and the proper resolution with g; the graph of the holomorphic f_tilde in this proper family is closed.

The reduced normal-crossings property of the original r-centre is not automatically preserved. A blow-up of an intersection of central branches introduces an exceptional component with the sum of their multiplicities. One may resolve the total central support, but that alone gives normal crossings with possible multiplicities. No assertion of an unchanged semistable central fibre is made here.

## 3. The base nonflat locus is finite and central

The central divisor of Z_tilde has finitely many irreducible three-dimensional components, because it is compact. Each has either all of P1 or one point as its proper f_tilde-image. Away from the finitely many point images, every fibre of (f_tilde,r) has local dimension exactly two. Indeed every fibre has dimension at least two; a fibre germ of dimension at least three would contain a three-dimensional component of the Cartier divisor r=0, and that component would map to a single value of f_tilde.

The local flatness assertion can be checked by the regular sequence (r, f_tilde-a). The smooth local ring is Cohen--Macaulay; after dividing by the nonzero divisor r its associated primes are exactly the central components. At a fibre avoiding their constant f_tilde-values, f_tilde-a avoids these primes. The two base coordinates therefore form a regular sequence and the analytic miracle-flatness criterion applies. Over r != 0, the prescribed elliptic-base map has pure two-dimensional fibres and the same criterion applies.

In particular, after shrinking a cusp disc around f_tilde=infinity, the map is flat away from the bidisc origin: all other constant component values can be excluded. The standard analytic flattening operation can thus be taken over the origin. Its strict transform preserves the punctured family and is proper and flat over the modified base. A subsequent resolution may destroy this two-dimensional flatness, so it must not be silently interchanged with flattening in a proof that needs both properties.

## 4. What the reduction does not preserve

An arbitrary r-only filling is given only over r != 0. It has no prescribed r=0 model at regular values of f. Neither the coherent pencil argument nor the graph construction identifies its central rank-one two-torus degeneration with the actual partial filling of B.4.19. Graph resolution can additionally modify that axis, including at regular q values. The construction does preserve the actual q=0 cusp family over r != 0, because that lies in the unchanged punctured r-family.

The current two-section/logarithmic bridge, as stated by classification_e on 15 November 2026, uses the explicit B.4.19 completion on both punctured axes to extend finite traces into the same associated log-torus sheaf. New exceptional base divisors over the origin have full-rank monodromy; the strict r-axis has only rank-one monodromy and a surviving elliptic kernel. The full-rank argument therefore does not settle that strict axis.

Consequently an obstruction to completing the fixed B.4.19 partial family would not yet be an obstruction to every r-only semistable filling. The remaining implication requires a theorem controlling the rank-one axial completion, or a replacement obstruction independent of its choice. No arbitrary bimeromorphic comparison, extension of affine origins, or preservation of the specified axial fan model is inferred here.

## 5. Primary-source access and scope

- B.4.4 and E_B44_referee.md were read in full again. The original Grauert/direct-image and constant-h0 base-change sources are the already opened references used there.
- Bierstone and Milman, original author preprint https://arxiv.org/pdf/alg-geom/9508005, Theorem 1.6 and the following noncompact-analytic paragraph, were independently reopened. The existing key is BM95AB. The theorem covers reduced complex analytic spaces and permits a locally finite resolution. It is used for graph resolution, not for a comparison with a different completion.
- Nakayama's original author manuscript https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1322.pdf, Section 7.1, Step 3, printed manuscript p.141, was reopened to verify the exact use of analytic flattening of an arbitrary proper extension. His elliptic-fibration classification is not imported for two-dimensional tori.
- The original Hironaka 1975 flattening article was searched at DOI 10.2307/2373721; the direct JSTOR access failed. Its metadata is American Journal of Mathematics 97, 503--547. No assertion that the inaccessible scan was read is made. Flattening's standard role is recorded here, while the actual preservation and scope arguments above are explicit.

This is an audit note, not a newly numbered result or an unrestricted nonexistence theorem.
