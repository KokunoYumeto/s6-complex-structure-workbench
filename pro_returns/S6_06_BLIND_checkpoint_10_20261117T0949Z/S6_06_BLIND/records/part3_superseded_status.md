
# Status passages archived 2026-11-17T03:20:41.255637+00:00

## P3F.4 application completed by P3F.8 and P3K.6--9.

```text
Combining this construction with (P3F.3.1) computes the Hopf-glued sphere
for the numerical pair ((-1,-4)): its oriented class is zero. The
remaining application to the AC26 family consists of an actual geometric
identification of the family's clutched sphere with this Hopf gluing,
and a derivation of the numerical pair from its charts. Neither is
supplied by the abstract classification theorem, and neither is claimed
to have been completed in this file.
```

## Historical main-case status superseded by P3K.6--9 and P3F.25.

```text
For the family application the smallest undecided instance remains the
original ((3,4)\) sphere family: one must identify its positive parameter
return map, including the cusp collar, with a geometric representative
on the quotient model and evaluate the normal/relative characteristic
data. The direct images and full automorphism result in the independent
Part5 notes do not determine that isotopy class. The construction of
P3F.4 now supplies the explicit passage to an oriented standard sphere
for the classified pair ((-1,-4)\); it leaves the geometric evaluation
of that pair visible rather than assuming it.

Approaches pursued here are the exact rank-one table enumeration,
permutation-certified existence of every source, section-height and
component calculations, Jin's full integral classification in fixed
coordinates, explicit Hopf-lift extension over (D^4\times S^3\), and
Takase's corrected normal-Euler formula. The next geometric calculation
is the local-to-global comparison of the original toric cusp collar with
the Hopf-lift gluing. It must carry the phase of the linearization and
the finite logarithmic transformations, not only the fibre period
matrix.
```

## P3F.8 numerical application completed by P3K.6--9.

```text
The remaining numerical step in P3.1 is therefore exact: compute
k=integral_{M_f}x³ and ell=integral_{M_f}p1 x for this f, including the
finite-root and cusp collar contributions. Parent Statement P2.1
provides the actual sixfold descent

    H(t)delta, H(t)=-(4l1 log t+3l2 log(t-1))/(2pi i),

with cusp coefficient -p after carrying the collar integer l0. Its
circle quotient is a radial translation in the line-bundle direction.
The page/cap identification needed to turn that exact formula into
the values(-6,-24) for the sixth power has not yet been written. No
finite-group class is declared computed from that missing comparison.
```

## P3F.10 cap comparison completed by P3K.6--9.

```text
the closed T3 boundary gives additivity. These statements give the
page and its actual line and framing data. The further identification
of the annular return with a closed spin-six cap whose characteristic
pairings are3s_delta and p_rel remains a separate step; no value in
Theta7 is asserted merely from these two numbers.
```

## P3F.11 kernel membership completed by P3K.7--8.

```text
The numerical membership of the AC26 return in this kernel still
requires the annular collar calculation; P3F.11 supplies the exact
integer framework for that calculation and the reduction from six
parameter loops to one.
```

## P3F.14 index comparison completed by P3K.6--8.

```text
These are exact local index inputs. Turning them into an index of the
actual return still requires a global bordism or a proved relative
index excision at the corner; neither is inferred from the numerical
cancellation alone.
```

# Pullback-direction correction archived 2026-11-17T03:30:21.839564+00:00

The following sentence from the first draft of P3F.28 is superseded by
the explicit target-point formula \(M_{p+Q}\to M_p\). The suspended
translation is \(-Q\), while the pullback automorphism in this formula
is \(+Q\). No divisor, exact sequence, or computed value changes.

```text
**Proved.** For the actual OS49 source and line of P3F.26, let
\(T\) denote translation by \(-Q=-3G\), with the pullback
convention used there. Then
```


# Additional historical-status correction 2026-11-17T03:43:24.239466+00:00

## notes/part3_family.md

```text
The outstanding check is the full cyclic descent and its outer
boundary identification after resolving the source I12 charts. One
must match (P3F.13.2), including all exceptional charts, with the
actual circle line, and check that the remaining fixed cusp trace
has the chosen O(-1)² tubular framing. The local equations and the
numerical characteristic calculation do not by themselves prove
this global bordism. Consequently P3F.13 is an exact local clutch
calculation, not a declaration of the monodromy class.
```

## notes/part3_family.md

```text
This is a general calculation for the explicitly specified Hopf
boundary; it makes no assertion that the still-unfinished corner has
already supplied it as a global bordism boundary.
```

## notes/part3_family.md

```text
It does
not yet prove the outer contraction of the additional source I12
resolution charts, which remains the last issue specified in P3F.13.
```

## notes/part3_other_families.md

```text
These equations compute the page data. Identifying their combination
with the return-map invariant still requires the P3F.13 comparison.
```

## P3F.13 statement in the TeX export and converter

```text
The angular origin comparison is $\theta\gamma+6\theta(1-\theta)\delta$ and its full $Q$-deck line clutch has winding $-12$. The global corner bordism is not yet proved.
```

## 2026-11-17T04:25:52.564646+00:00 — P3F.31 audit completed

The following preliminary status was superseded by the independently audited positive-fan proof P3F.31, retaining the negative-fan return as unresolved:

> **Audit draft.** This statement concerns the positive-diagonal filling defined below. It leaves the negative-diagonal family of P3F.26 intact. The two fans have the common torus family and are related by the specified toric flop; they are not identified as the same family.

> The intended conclusion is that this positive-diagonal filling gives an actual sphere family over \(\lambda=r^3\), with zero positive-loop return index. The full construction and the line comparison are given below for independent audit before that conclusion is marked proved.

## 2026-11-17T04:32:37.473287+00:00 — P3F.32 audit completed

The preliminary label **Audit draft** in P3F.32 was replaced by **Proved** after independent root and fourfold audits of the origin, finite-cap line, page, regular bands, and cap. The negative-diagonal index remains unresolved.

The earlier P3F.29 wording “The mixed-circle return index of P3F.27 remains unassigned” is now explicitly restricted to its negative-diagonal filling; the positive-diagonal result is P3F.31–32.

## 2026-11-17T04:40:27.185112+00:00 — P3F.33 audit completed

The preliminary **Audit draft** label in P3F.33 was replaced by **Proved** after root independently audited every fixed-point congruence, the primitive quotient solvability, and the full deck/van Kampen presentation. The finite-sum conjugation for arbitrary affine sections is kept outside this statement.

## 2026-11-17T05:00:48.900692+00:00 — P3F.34 complete audit and CSV correction

The prior P3F.34 status was “Audit draft; working correction to the general-n CSV value.” Root independently audited all Gysin maps, the integral boundary basis including eta*h/3, the uniform n=1 exterior-lattice argument, the Smith invariants, and UCT/PD. The prior compound-row state is preserved below:

```json
{
  "run": "S6_04",
  "id": "D.2.11",
  "state": "The sphere assertion n=+/-1 for every order3k and twist is proved. P3F.33 now classifies every free explicit affine cap by gcd(k,n,d)=1 and (3 does not divide n or 3 divides k), and proves pi1=Z/abs(n) for all of them. P3F.29 proves H1 through H4=Z/abs(n) in the coprime sector gcd(n,3k)=1. The higher-homology formula for the additional non-coprime free caps (for example m9,n3,d1) has not yet been proved, so this compound row remains only partially compared.",
  "proof_ids": [
    "P3F.26",
    "P3F.29",
    "P3F.33"
  ]
}
```

## 2026-11-17T05:23:35.289267+00:00 — P3K.17 status integration

### part3_os49_component.md

Superseded passage:

```text
For the negative-diagonal filling fixed in P3F.26, this comparison
remains unresolved. P3F.31 constructs and computes the actual
page for the positive-diagonal filling through its line-complement
subfan; that result is not transferred across the flop here.
```

### part3_os49_component.md

Superseded passage:

```text
These numbers are checked, but are not assigned to the actual
mixed-circle return. A construction of the modified page, or a
calculation of this precise Euler-line correction, is still needed
to determine that return integer. The change of boundary marking
and the obstruction just stated are exact, not an assertion that
the two pages cannot be related.
```

### part3_os49_index_input.md

Superseded passage:

```text
These are exact statements about the sheaf morphisms in the actual
construction. They do not yet identify the spin-c symbol of the
mixed-circle return in P3F.27.
```

### part3_os49_index_input.md

Superseded passage:

```text
This proves equality of their Dolbeault indices by an explicit
exact sequence. The remaining question in P3F.27 is whether this
is the particular line comparison induced by the graph-normal
homotopies. No equality of return indices is deduced here before
that morphism is constructed.
```

### part3_os49_all_orders.md

Superseded passage:

```text
This statement determines topology. The mixed-circle return index
of the negative-diagonal filling of P3F.27 remains unassigned.
P3F.31--32 separately construct and compute the actual page and
return of the positive-diagonal filling.
```

### part3_os49_norm.md

Superseded passage:

```text
opposite base factors. Neither the norm map nor the vanishing
indices in P3F.28 yet identify their total correction with the
mixed-circle trace of P3F.27.
```

### part3_os49_positive_fan.md

Superseded passage:

```text
This calculation is for the explicit positive-diagonal family.
The negative-diagonal family in P3F.26 remains separately recorded
until its actual flop correction is computed.
```

### part3_os49_positive_orders.md

Superseded passage:

```text
mapping torus. The negative-diagonal filling is not changed by
this calculation.
```


## 2026-11-17T05:45:47.826815+00:00 — final historical-status cleanup; TeX export deferred until freeze release

### part3_os47.md

```text
The equality of this expression with the actual return-map invariant
has not yet been proved. Accordingly this statement does not assign a
class in \(\Theta _7\). It supplies a fully constructed sphere family
and the exact weighted case to which the missing comparison must be
applied.
```

### part3_other_families.md

```text
It does not replace the unresolved comparison in P3F.13 by a numerical
index identity. In particular, the scalar-parameter monodromy of the
Alpöge–Claude/Engel construction is still being investigated.
```

### part3_other_families.md

```text
\(P\cdot O=0\). Its component-permuting translation at \(I_2\) still
has to be carried through its actual circle quotient and monodromy
comparison; the page numbers alone do not perform that comparison.
```

### part3_family.md

```text
This calculation concerns the explicit compact elliptic pullback. It
does not yet identify its boundary modification with the page of a
threefold-family monodromy.
```

### part3_family.md

```text
and computes the nonzero weighted OS47 example. The remaining
component-supported OS49 page comparison is stated separately in
P3F.27.
```

### part3_family.md

```text
value t* and leads to the second map. The four-dimensional page still
requires its separate construction, including its boundary surgeries.
```

### part3_os49_component.md

```text
# P3F.27. The OS49 cusp circle and the remaining page comparison
```

