## Part E: the actual candidate, local fillings, and unresolved compact gluing

| Item | Statements | Outcome | Missing requested result |
| --- | --- | --- | --- |
| E.1 | E.1.1–E.1.5 | (c), unfinished | A compact equivariant two-parameter filling at infinity with the prescribed general Mumford fibre and the proposed central normalization. |
| E.2 | E.2.1–E.2.3 | (c), unfinished | A compact sphere-family filling, including the nonreduced finite-fibre neighbourhoods and descent of their actions. The smooth monodromy is reduced to the explicit invariant allowed by the prompt. |

We constructed the compact pushout Q by actual local analytic rings, proved that its normalization is the stated projective-line bundle, and computed its local smoothing sheaf. The resulting local plumbing exists over the entire finite part of the elliptic base, including the Kodaira fibres at 0 and 1. Its comparison with Engel's nonzero-parameter quotient is the explicit inverse bundle map in E.1.2.

At the node over infinity the joint germ is `xy=u*z*v`, with original elliptic-base coordinate `q=z*v`. This family is flat over u. For nonzero u its fibre has an ordinary double point. Blowing up `(x,z)` gives a projective small resolution on those fibres and remains flat, but one branch of the central normalization is blown up along a curve. The actual substitutions prove the alteration of that candidate. They do not prove that every equivariant construction must alter it. The two period actions and the complete periodic fan have not been glued across `(q,u)=(0,0)`.

We nevertheless computed the integral topology of the **constructed candidate**: pi1(Q)=Z, H_i(Q)=(Z,Z,Z^8,Z^7,Z^10,0,Z), and Euler characteristic 12. The two section inclusions give an explicit homology map. Its rank and primitivity are proved using a squarefree Gram determinant, and independently checked by exact Smith forms. The Euler characteristic is checked by both homology and stratification. These invariants are not assigned to an unconstructed limit of the compact sphere family.

The two reduced bielliptic surface families do have explicit semistable fillings after `w=s^6`. They are finite free quotients of a twelve-gon Tate curve times the fixed elliptic curve. The central surfaces have four and three ruled components. Their fundamental groups are Z^2 semidirect Z with rotations of orders three and four. Their integral homology is respectively `(Z, Z+Z/3, Z^5, Z^9, Z^4)` and `(Z, Z+Z/2, Z^4, Z^7, Z^3)`; both Euler characteristics vanish. We checked the full twisted cycle matrices as well as the independent two-by-two determinants.

The sphere family's smooth monodromy fixes integral cohomology. We gave an actual representative by parallel transport along `c(r)=c0-2r` followed by the coherent even-shift gluing. Its oriented two-disc clutching sphere has Eells–Kuiper residue `(p1^2-4 signature)/32 mod28`. This is the explicit invariant reduction permitted in E.2, with the orientation and denominator fixed from the original Eells–Kuiper formula. The characteristic numbers of a bounding eight-manifold for this particular clutching sphere have not been computed.

### Reading and exact computations

We read Engel Sections 2, 3, 7 and 8, in particular Lemma 2.1 and proof, Corollary 2.2, and Conjecture 8.2. We inspected the supplied period and finite-product presentations and compared the signs with the explicit first-page marking map. For the smooth monodromy comparison we opened Cerf's seven-page primary article, Theorem 1 and Corollaries 1–2, Smale's original paper, Theorems A, I and J, and visually inspected Eells–Kuiper Section 7, printed pages 100–103.

`code/e_degeneration.py` was executed and its output is retained. It verifies the translation matrix and its action on the intersection lattice, primitive homology maps, Smith normal forms, both local modification substitutions, and the integral cycle complexes. `code/e_registry.py` creates the eight statement rows and its output is also retained.

### Smallest undecided instances

For E.1 the smallest unresolved chart is one lift of the nodal point, with equation `xy=u*z*v`, equipped with both deck generators. The required construction must have the prescribed general-fibre small resolution, a proper periodic quotient, and the proposed central normalization. Our single explicit blow-up has the first local property and changes the last.

For E.2 the first unresolved finite-place chart is the order-three affine action over a simultaneous `(t,s)` plumbing with the original normal character and central multiplicity three, followed by descent from `s` to `w=s^6`. The order-four chart and the infinity chart must then be made compatible. Until this is done, there is no global central fibre whose topology has been established. The one remaining numerical monodromy instance is the residue for the loop based at `c0=-i(M+1)`.

