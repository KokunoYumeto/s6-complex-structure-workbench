import io
p = "scripts/s10_gazette.py"
s = open(p, encoding="utf-8").read()
def rep(old_key, new_line):
    global s
    i = s.index(' ("' + old_key + '"')
    j = s.index("\n", i)
    s = s[:i] + new_line + s[j:]
rep("MAPS:B.5.1", ' ("MAPS:B.5.1", "A finite CW structure on X adapted to f (the T^4-bundle over the pair of pants and the three special fibres), with cell counts (5,20,45,56,42,17,3).", P),')
rep("MAPS:D.1.1", ' ("MAPS:D.1.11", "The universal covers of the members with pi_1 = Z/d (d > 1): Euler number 2d, b_2 >= d - 1, so not a connected sum of copies of S^3 x S^3 (Thm 4.1); their homology, cohomology ring and diffeomorphism type (Thms 4.4-4.9, A.4).", P),')
rep("MAPS:D.2.24", ' ("MAPS:D.2.28", "The other rational elliptic surfaces with Mordell-Weil rank one: the sphere question on all twenty-one natural profiles; with Thms 4.53-4.54 the minimal simply connected sector is classified up to diffeomorphism.", P),')
rep("MAPS:D.3.1", ' ("MAPS:D.3.3", "The conifold transition of Engel\'s Remark 8.5: the moving-zero family (Thm 4.63), whose smooth side is S^3 x S^3 (Thm A.6), with its complex invariants.", P),')
rep("MAPS:E.2.1", ' ("MAPS:E.2.1", "The fibre-product fourfold Z: K_Z = Pi^*L^(-5), a(Z) = 2, h^{0,q} = (1,1,0,0,0), not in class C, signature 2.", P),')
rep("MAPS:F.2.5", ' ("MAPS:F.2.6", "A closed 8-manifold glued from rank-six data (free affine fibres of multiplicity 5 and 4, one index-one cusp): simply connected, signature 2, lattice 3<1> + <-1> (Thm 6.8), with free integral homology and H_2 = H_3 = 0 (Thm 6.10).", P),')
rep("ARI:C.8.15", ' ("ARI:C.8.15", "Every critical point and level set of the norm: t = 1 is the unique global maximum and the only critical point on the t-plane; t = 0 is a non-critical C^1 point; no saddle.", P),')
rep("working_edition:cusp-null:thm", ' ("MAPS:B.3.1", "The retained-angle cusp collapse map H: X -> S^4 is eta_4 eta_5, non-zero in pi_6(S^4) = Z/2; the angle-forgetting maps to S^3 and S^2 are null (Thm 2.6).", P),')
open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
