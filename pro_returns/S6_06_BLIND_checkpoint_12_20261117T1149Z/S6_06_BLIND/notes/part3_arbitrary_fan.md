# P3F.35. Every one-vertex cusp fan and the prime fixed-set obstruction

**Proved.** The full argument has passed independent audit.

For the whole-zero \(I_1,e=1\) cusp, let the allowed triangulation
have vertex set \(\mathbb Z^2\), period group \(\Gamma=\mathbb Z^2\),
and unimodular triangles. Every such triangulation is the periodic
triangulation
\[
 T(v,w)=\{(0,v,v+w),(0,w,v+w)\}+\mathbb Z^2                 \tag{P3F.35.1}
\]
for an integral basis \((v,w)\). It is connected to the standard
vertical-edge triangulation by a finite sequence of the explicitly
described periodic diagonal flops. Each step preserves the integral
homology and fundamental group of the compact threefold, and therefore
preserves its status as the standard smooth six-sphere.

For every prime \(p\), the \(\mu_p\)-fixed subset inside this cusp
has total \(\mathbb F_p\)-Betti number exactly two, whether or not
the physical delta action is semifree. Consequently every separate
finite or logarithmic cap in a sphere member has free delta action.
This last assertion supplies the cap-freeness input to P3K.15 without
assuming semifreeness at the chosen cusp. The present statement does
not yet assign a return class to every fan.

**Proof: the exact form of the triangulation.**

The quotient torus has area one. Every triangle has area one half,
so there are exactly two triangle orbits. Translation fixes no
finite edge or triangle. Counting incidences gives three edge
orbits. Choose one triangle \((0,a,b)\); unimodularity says
\(\det(a,b)=\pm1\). Its three unoriented edge classes are
\(a,b,b-a\), which are distinct and exhaust all edge classes.
After the integral linear change \((a,b)\mapsto(e_1,e_2)\),
the only possible third vertices of a triangle incident to
\([e_1,e_2]\), using those edge classes, are \(0\) and
\(e_1+e_2\). The opposite-side condition selects the latter.
Likewise, across \([0,e_1]\) it selects \(e_1-e_2\), and
across \([0,e_2]\) it selects \(e_2-e_1\).
These are exactly the adjacent triangles of the periodic unit-square
triangulation. Propagating across edges determines the entire plane
triangulation. Taking \(v=a\), \(w=b-a\) gives (P3F.35.1).
This is an equality of the actual periodic fans after the stated
integral coordinate map, not a replacement by an unmarked abstract
triangulation.

The three edge classes of \(T(v,w)\) are
\(\{\pm v,\pm w,\pm(v+w)\}\). In the parallelogram
\((0,v,w,v+w)\), replacing the diagonal \(v+w\) by
\(v-w\) gives \(T(v-w,w)\). Conversely replacing the
edge class \(v\) by \(v+2w\) gives \(T(v+w,w)\).
Thus adding or subtracting one column of a basis from the other
is exactly one periodic diagonal flip. Interchanging columns
does not change the triangulation. Reversing one column changes
the sole diagonal class \(v+w\) to \(v-w\), again one flip.

For completeness, an explicit terminating reduction is available.
Write the two first coordinates as \((x,y)\). Repeatedly replace
the first column by the first column minus
\(\lfloor x/y\rfloor\) times the second, and interchange columns.
Each integer multiple is executed as its finite sequence of unit
column moves. Euclid's algorithm reaches \((\pm1,0)\), because
the determinant is \(\pm1\). Reverse the first column if
needed. The second column is now \((0,\pm1)\); reverse it if
needed and subtract its appropriate multiple from the first
column. The result is \((e_1,e_2)\). Every intermediate basis
and every flip have been specified, and the standard second edge
is the physical vertical delta direction.

**Proof: the actual local flop and its topology.**

For one selected edge orbit, each triangle contains exactly one
edge from that orbit. Distinct corresponding toric curves therefore
share no three-cone, hence no torus fixed point and no intersection.
Their lattice translates are disjoint. No nonzero lattice
translation fixes a finite edge, so in the quotient the center is
one embedded rational curve. The four height-one rays of either
adjacent parallelogram satisfy the actual integral relation
\(r_0+r_2=r_1+r_3\). Their determinant-one adjacent cones
give the normal bundle \(\mathcal O(-1)\oplus\mathcal O(-1)\).
Blowing up its zero section gives exceptional divisor
\(\mathbb P^1\times\mathbb P^1\), with normal line
\(\mathcal O(-1,-1)\). The two ruling contractions are the
two fan subdivisions just described. All maps commute with lattice
translation and agree with the identity off the compact center;
they therefore descend to the actual compact models.

The integral blowup decomposition adds precisely one free summand
in degrees two and four. Primitivity can also be read directly:
the exceptional divisor has degree minus one on either contracted
ruling. Thus the common blowup gives
\[
 H^j(\widetilde X;\mathbb Z)
   =H^j(X_-;\mathbb Z)\oplus H^{j-2}(\mathbb P^1;\mathbb Z)
   =H^j(X_+;\mathbb Z)\oplus H^{j-2}(\mathbb P^1;\mathbb Z).
\]
There is no torsion quotient hidden in the additional summands.
Removing a real codimension-four center preserves fundamental
groups by general position; its normal sphere bundle and disk
bundle are simply connected, so van Kampen also proves invariance
under the blowup and either contraction. Starting with a simply
connected integral homology six-sphere therefore gives the same
groups after every step. The smooth sphere identification is the
same Smale and \(\Theta_6=0\) argument used in P3F.26.

**Proof: the exact prime fixed sets.**

Let \(\delta\in\mathbb Z^2\) be the primitive physical circle
cocharacter, and write \(\delta=a v+b w\). On the three open
edge strata the finite isotropy orders are
\[
 |\det(\delta,v)|=|b|,\qquad
 |\det(\delta,w)|=|a|,\qquad
 |\det(\delta,v+w)|=|a-b|.                              \tag{P3F.35.2}
\]
Here order zero denotes the full circle stabilizer. The formula
comes from the exact quotient lattice
\(\mathbb Z^2/\mathbb Z e\) for an edge direction \(e\):
the delta cocharacter has image \(\det(e,\delta)\) in that
rank-one lattice. Since \(\gcd(a,b)=1\), any prime divides
at most one of the three numbers in (P3F.35.2), including zero.

In a determinant-one triangle chart with coordinates
\((z_0,z_1,z_2)\), the circle has integral weights
\((c_0,c_1,c_2)\) with
\(c_0+c_1+c_2=0\). Their greatest common divisor is one:
the triangle rays are an integral basis of the three-dimensional
toric lattice and delta is primitive. Thus modulo a prime no
two weights can vanish; if two did, the third would also vanish,
contradicting primitivity. The \(\mu_p\)-fixed locus in this
chart is therefore either the isolated origin or one coordinate
axis. Those axes are exactly the edge strata selected by
(P3F.35.2). If a prime divides one edge order, the two local axes
glue through that edge to its whole rational curve; both triangle
fixed points lie on it and there are no further fixed points.
If it divides none, the fixed set consists of the two triangle
points. Open toric surface strata have no finite stabilizer,
because their two-dimensional torus lattice is the original
\(\mathbb Z^2\) and delta is primitive.

On every regular fibre the delta action is primitive translation,
so no \(\mu_p\)-fixed component can leave the central cusp.
Consequently the compact cusp fixed set is exactly
\(\mathbb P^1\) or exactly two points. Both have total
\(\mathbb F_p\)-Betti number two. A nonfree delta action in
a separate cap has a point fixed by some prime subgroup.
Its nonempty compact fixed subset is disjoint from the cusp
fixed set and contributes at least one to the total Betti number.
Floyd's Theorem 4.4, applied to the order-\(p\) diffeomorphism
of the compact six-sphere, bounds that total by
\(\sum_i b_i(S^6;\mathbb F_p)=2\), a contradiction.
This proves cap freeness for every allowed fan.

The primary theorem was checked in E. E. Floyd, *On periodic maps
and the Euler characteristics of associated spaces*, Trans. AMS
72 (1952), Theorem 4.4, p.146; the coefficient convention is
stated on p.139. The exact elementary fan reduction is reproduced
in `code/part3/arbitrary_fan.py`.
