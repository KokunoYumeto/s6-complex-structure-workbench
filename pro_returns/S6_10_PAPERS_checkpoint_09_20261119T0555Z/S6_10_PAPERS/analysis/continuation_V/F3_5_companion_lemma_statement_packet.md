# F.3.5 isolated rational companion lemma: statement and data only

Work over Q. Put f(T)=T^4+T^3+T^2+T+1 and g(T)=T^4+1. Let R,S be4x4 rational invertible matrices with characteristic polynomials f,g respectively and rank(R-S)=1. The claim is that the pair(R,S) is simultaneously conjugate over Q to the pair(Cf,Cg) below. More generally the printed step establishes uniqueness of the rational simultaneous conjugacy class from these data. Please derive this before opening the target proof.

```
Cf = [[0,0,0,-1],
      [1,0,0,-1],
      [0,1,0,-1],
      [0,0,1,-1]]
Cg = [[0,0,0,-1],
      [1,0,0,0],
      [0,1,0,0],
      [0,0,1,0]]
```

Known inputs allowed: f is irreducible over Q (the fifth cyclotomic polynomial), ordinary rational linear algebra, the characteristic polynomial definition and determinant identities. The geometric application has R=T1^-1,S=T2, where T1,T2 are the marked positive peripheral monodromies at infinity and zero, and their product differs from identity by rank one. Its integral marking is a separate result and is not asserted by this rational lemma. No proof, chosen basis, determinant expansion or covector computation is supplied here.
