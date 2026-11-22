# Independent derivation: cdp:st:D.1.8 (tag01G6)

The target proof has not been opened. I read the exact target/input packet and the empty supplement. Primary inputs are Ehresmann's fibre-bundle proposition, Hatcher's homotopy sequence and universal coefficient theorem, and Stacks tag09V6 proper topological base change (see the reading record). The argument below also works in the dimension of the manifold used later in D.1.9.

Fix a critical value c and a small disc V around it with no other critical value. Set W=f^{-1}(V), W*=f^{-1}(V minus {c}). A class in the stalk (R^1f_*Z)_c is represented by a class a in H^1(W;Z) after shrinking V. Proper base change identifies the stalk with H^1(f^{-1}(c);Z). The generization map is induced by restricting this representative to a nearby smooth fibre and then regarding the result as a monodromy-invariant class.

The map H_1(W*;Z)→H_1(W;Z) is onto: any finite collection of loops can be perturbed off the analytic divisor f^{-1}(c), whose real codimension is2; its singular strata have still larger codimension. Applying Hom(−,Z), and H^1=Hom(H_1,Z), gives an injection H^1(W;Z)→H^1(W*;Z).

Ehresmann supplies W*→V* as a bundle with connected fibre F. The punctured disc retracts to a circle. Its fundamental group is free cyclic, and lifting a generator splits the extension of fundamental groups. Therefore restriction to F fits in

0→H^1(V*;Z) --f^*→ H^1(W*;Z)→H^1(F;Z)^T→0.

In particular a class whose generization is zero restricts to k f^*eta, with k an integer and eta the positive generator of H^1(V*;Z).

Let f^{-1}(c)=sum m_iD_i as a divisor. At a regular point of D_i away from all other components choose a transverse analytic disc. The local function f−c has vanishing order m_i, so its restriction to the boundary circle has degree m_i. This proves the exact evaluation identity <f^*eta,mu_i>=m_i for the positive meridian mu_i. That meridian bounds the transverse disc in W, so <a,mu_i>=0. Consequently k m_i=0. Every m_i is a positive integer; k=0. The preceding injection then gives a=0. Taking the stalk proves injectivity of R^1f_*Z→j_*((R^1f_*Z)|_{C°}). No division by m_i or saturation assumption is involved.

Now take a nonzero global section alpha. Its image under the injective sheaf homomorphism is nonzero. The smooth locus C° is connected, and the restriction there is a section of a local system, so parallel transport shows that it is nonzero at every smooth point. At any c, a zero stalk alpha_c would have zero generization by the definition of the sheaf morphism, contradicting this nonzero nearby value. Thus alpha_c is nonzero for every fibre, with the stalk/fibre identification specified above. This proves both assertions integrally. There is no finite matrix or numerical computation.
