# Exact periods at the order-three exceptional p-infinity end

This is the actual period-coordinate calculation for the N=4 coupled
family of E81–85. The corner atlas and characteristic pairing remain
unassigned here.

Put u=P/R, retain the source coordinate R, and set
f=(1-u)^4 c with c=lambda_0 q K u_s^(-4). The full c is the original
extending unit from E85; it is retained with its phase. In the original
Tate coordinates (Z,V_T), the two actual period arrows are

\[
 h:(Z,V_T)\mapsto(u^2R^3Z,R^{-3}V_T),\qquad
 B:(Z,V_T)\mapsto(u^{-1}R^{-1}Z,R^4fV_T).
\]

On the punctured torus use the holomorphic character isomorphism
(Z,V_T) -> (X,Y)=(Z,Z^5/V_T), with inverse
(X,Y) -> (X,X^5/Y). The physical circle acts with weights (0,-1)
on (X,Y), as follows directly from its original weights (0,1).
Use the actual period arrows K=h B^2 and L=h^(-1) B^(-3), whose
inverses are literal inverse compositions. Their complete maps are

\[
 K:(X,Y)\mapsto(RX,f^{-2}Y),\qquad
 L:(X,Y)\mapsto(uX,R^9u^5f^3Y).
\]

The character and period matrices are respectively

\[
 C=\begin{pmatrix}1&0\\5&-1\end{pmatrix},\qquad
 J=\begin{pmatrix}1&-1\\2&-3\end{pmatrix},\qquad
 J^{-1}=\begin{pmatrix}3&-1\\2&-1\end{pmatrix}.
\]

Each determinant is -1. Both signs are part of the comparison. In
particular the factor u in the X component of L has its full divisor;
it must be carried by the corner chart. The calculation alone does not
replace that divisor by an extending unit or assert a compact filling.
The exact multiplication and inverse matrices are checked in
code/part3_root/e6_p_infinity_periods.py and its recorded output.
