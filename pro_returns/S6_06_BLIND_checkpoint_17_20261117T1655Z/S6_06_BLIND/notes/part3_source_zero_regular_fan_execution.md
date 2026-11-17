# Exact finite regular fans for the two first safe source-zero cases

This is an execution record of ER.1–4 in
`notes/part3_source_zero_equivariant_resolution_audit.md`, after the
default negative-fan correction in PF.1–5. It retains the original
integer lattice in every sector. The two requested cases are
\((a,b,N)=(1,2,8)\) and \((2,1,6)\). No analytic filling or return
integer is assigned here.

## 1. The actual starting subdivisions

The lattice order is \((Z,V,r,s)\), where \(r\) and \(s\) are the
two base heights of the sector. Its physical circle generator is
\(\delta=(0,1,0,0)\). The three bottom matrices and common top matrix
are
\[
 I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
 W=\begin{pmatrix}1&b\\-a&-2\end{pmatrix},\quad
 E=\begin{pmatrix}0&0\\0&N\end{pmatrix},\quad
 H=\begin{pmatrix}2&b\\-a&N-1\end{pmatrix}.
\]
In sector \(P_0\in\{I,W,E\}\), the period action is literally
\[
 T_n(x,r,s)=(x+(rP_0+sH)n,r,s),\qquad n\in\mathbb Z^2.
\]
The raw staircase cones use the negative I/E basis
\((e_1,-e_2)\), and the W basis \((e_1,e_2-be_1)\).

For \(b=1\) the two H triangulations already agree. For \(b=2\),
the common overlay inserts the single midpoint orbit represented
in the inspection plane by \((0,1/2)\). Its actual primitive
four-dimensional ray is
\[
                      (2,N-1,0,2).
\]
The code stars the corresponding vertical edge in the I/E H fans
and the edge joining \(e_1\) to \(-e_1+e_2\) in the W H fan.
It verifies that no old cone contains two such edge translates.
This produces exactly the common overlay, keeping the height two.

Every raw length-N E boundary segment is then subdivided by the
literal rays \((0,j,1,0)\), and its subdivision is joined to the
unchanged opposite face. This keeps the full primitive E chain.
The I and W bottom fans remain unchanged. All three H boundary
triangle-orbit sets are checked to agree before proceeding.

The relative barycentric separator is then executed exactly as
ER.2: leave every face with \(s=0\) unchanged, and on every other
face use the primitive sum of its own rays and cone its subdivided
boundary. The protected I, W and E face-orbit sets are recorded
before this step and checked after both the separator and the
final resolution.

## 2. The actual integer resolution

The program selects a largest-determinant cone, constructs the
half-open lattice point from a nonintegral inverse-matrix column,
reduces it to its primitive generator, and stars every translate
of its minimal face. A face on H is indexed once across all three
sectors, so the identical star is applied on every incident sector.
Every changed determinant is checked against the exact formula
\(D_i=\alpha_iD\), with \(0<\alpha_i<1\). It also checks that
each affected cone receives only one translated centre.

The execution retains the ray-orbit separation assertion after
every inserted cone. It terminates only when every maximal cone
has determinant absolute value one. The exported column order is
then changed by one fixed transposition when necessary, so every
exported maximal-cone matrix has determinant **+1**.

| Case | I cone orbits | W cone orbits | E cone orbits | Orbitwise stars | Exact checks |
|---|---:|---:|---:|---:|---:|
| \((2,1,6)\) | 3,281 | 3,210 | 3,360 | 2,556 | 396,172 |
| \((1,2,8)\) | 14,181 | 14,168 | 13,553 | 11,163 | 1,691,143 |

These are the deliberately explicit relative barycentric
resolutions. No minimality of their number of charts is asserted.
The mathematical termination proof is ER.4, and the files are its
two requested finite executions.

## 3. Canonical representatives and their retained periods

For any nonprotected face, let \((X,Y,R,S)\) be the sum of its
primitive rays. Since \(S>0\), the matrix \(RP_0+SH\) is
invertible. The program sets
\[
 n=\left\lfloor (RP_0+SH)^{-1}(X,Y)^T\right\rfloor
\]
componentwise and translates the whole face by \(T_{-n}\).
It records \(n\), with the direction
\[
                  F_{\rm literal}=T_n F_{\rm canonical}.
\]
The same formula works on the I bottom boundary. On W the
canonical translation is \((\lfloor X/R\rfloor,0)\), and the
pointwise period stabilizer is \(\mathbb Z(-b,1)\). On E the
canonical translation is
\((0,\lfloor Y/(RN)\rfloor)\), and the pointwise period stabilizer
is \(\mathbb Z(1,0)\). These boundary kernels are recorded, not
erased. The analytic unit action of their elements remains part
of the source-zero quotient problem.

Every ray occurrence is retained as its literal primitive vector,
its orbit representative, and this recovered period. A cone is
never formed by independently replacing its four rays by their
orbit representatives.

## 4. Data schema and exact face gluing

The generator is `code/part3/source_zero_regular_fan.py`. Its two
full outputs are

- `code/part3/source_zero_regular_fan_2_1_6.json`;
- `code/part3/source_zero_regular_fan_1_2_8.json`.

Each file has these fields:

- `literal_rays`: per-sector primitive vectors and ray IDs, their
  canonical orbit IDs and recovered integral periods, boundary
  tags, and the actual source-parameter order. That order is
  \(s\) in I/W and \(r+s\) in E.
- `ray_orbits`: canonical primitive rays and all period-stabilizer
  basis vectors on the rank-one boundary.
- `maximal_cones`: sector and orbit labels, ordered literal ray
  IDs, and determinant +1. These are the actual matrices for
  calculating \(C^{-1}\delta\).
- `face_orbits`: **every** face of dimensions one, two and three,
  its canonical vectors, I/W/E/H boundary tag, every maximal-cone
  occurrence and local column list, its period from the canonical
  face, and the vertex permutation to that canonical face.
- `anchor_gluings` within each face: maps from its first occurrence
  to every other occurrence. If their recorded periods are
  \(n_A,n_B\), the literal map is \(T_{n_B-n_A}\), with the
  displayed vertex permutation. This includes common-H maps
  between sectors. Each vector equality is executed and checked.
- `resolution_trace`: every star centre and minimal face, its
  exact rational coefficients, every incident old determinant,
  every new determinant, and the corresponding historical cell
  IDs. This permits replay of the executed integer subdivision.

Lower-dimensional face maps are included because maximal-cone
weights alone do not determine how the fixed strata glue. In
particular no link multiplicity or compact fixed component is
inferred from the original determinant \(2N\).

`code/part3/source_zero_regular_fan_summary.json` records the
precise checks, chart/ray/face counts, file sizes and SHA-256
hashes. Captured output is stored in the matching `.out` files.

The completed program proves and records an actual regular
periodic fan with the prescribed boundary maps. The analytic
unit quotient, its source/cap comparison and any numerical return
remain separate obligations of the active K39 construction.
