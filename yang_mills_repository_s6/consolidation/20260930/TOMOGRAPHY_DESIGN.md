# Exact minimal tomography matrices

This appendix supplies the finite calculations used in R7 of `MATHEMATICAL_NOTE.md`.  It uses the quaternion order $(1,\mathbf i,\mathbf j,\mathbf k)$ and changes no coordinate or covariance convention.

For

$$
A=\begin{pmatrix}
a_1&h_{12}&h_{13}\\
\bar h_{12}&a_2&h_{23}\\
\bar h_{13}&\bar h_{23}&a_3
\end{pmatrix}\in\operatorname{Herm}_3(\mathbb H),
$$

write $h_{ij}=h_{ij,0}+h_{ij,1}\mathbf i+h_{ij,2}\mathbf j+h_{ij,3}\mathbf k$ and order the real parameters as

$$
\theta_3(A)=(a_1,a_2,a_3,h_{12,0},h_{12,1},h_{12,2},h_{12,3},
h_{13,0},h_{13,1},h_{13,2},h_{13,3},
h_{23,0},h_{23,1},h_{23,2},h_{23,3})^T.
$$

For $q=(q_1,q_2,q_3)^T$, direct expansion gives

$$
q^*Aq=\sum_{i=1}^3 a_i|q_i|^2
+2\sum_{1\le i<j\le3}\operatorname{Re}(\bar q_i h_{ij}q_j).
$$

Take the six points

$$
\begin{aligned}
v_0&=(0,0,0),&v_1&=(1,0,0),&v_2&=(0,1,0),\\
v_3&=(0,0,1),&v_4&=(0,\mathbf i+\mathbf k,1+\mathbf i),
&v_5&=(1+\mathbf j,-\mathbf i,\mathbf j).
\end{aligned}
$$

Order their pairs by

$$
(01),(02),(03),(04),(05),(12),(13),(14),(15),(23),(24),(25),(34),(35),(45).
$$

The row for $(a,b)$ is the coefficient vector of $(v_a-v_b)^*A(v_a-v_b)$.  Quaternion multiplication in the stated frame gives

$$
M_3=\begin{pmatrix}
1&0&0&0&0&0&0&0&0&0&0&0&0&0&0\\
0&1&0&0&0&0&0&0&0&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0&0&0&0&0&0&0&0\\
0&2&2&0&0&0&0&0&0&0&0&2&2&-2&2\\
2&1&1&0&2&0&-2&2&0&-2&0&0&0&0&2\\
1&1&0&-2&0&0&0&0&0&0&0&0&0&0&0\\
1&0&1&0&0&0&0&-2&0&0&0&0&0&0&0\\
1&2&2&0&2&0&2&-2&2&0&0&2&2&-2&2\\
1&1&1&0&0&0&-2&2&0&0&0&0&0&0&2\\
0&1&1&0&0&0&0&0&0&0&0&-2&0&0&0\\
0&3&2&0&0&0&0&0&0&0&0&0&4&-2&2\\
2&2&1&-2&2&-2&-2&2&0&-2&0&0&0&2&2\\
0&2&1&0&0&0&0&0&0&0&0&2&0&-2&0\\
2&1&2&0&2&0&-2&0&0&-4&0&0&2&0&2\\
2&5&3&0&6&0&-2&0&2&-4&-2&4&2&-2&6
\end{pmatrix}.
$$

The fraction-free Bareiss recurrence replaces, after a needed row swap,

$$
a_{ij}^{(k+1)}=
\frac{a_{kk}^{(k)}a_{ij}^{(k)}-a_{ik}^{(k)}a_{kj}^{(k)}}{d_{k-1}},
\qquad d_{-1}=1,
$$

where $d_{k-1}$ is the preceding nonzero pivot.  Applied to the displayed integer matrix, every division is exact.  The successive pivots are

$$
1,1,1,-2,-4,8,32,-64,-64,128,-256,-512,1024,-2048.
$$

The required one-based row swaps are $(4,6),(6,12),(7,8),(10,14),(11,15)$.  The terminal entry is $4096$; the five swaps change its sign.  Therefore

$$
\det M_3=-4096=-2^{12}.
$$

If $y_{ab}=\frac12(v_a-v_b)^*A(v_a-v_b)$, then

$$
\theta_3(A)=2M_3^{-1}y.
$$

This is the exact reconstruction map used for $A=H^{-1}$.

For the observation-only design, write

$$
B=\begin{pmatrix}b_1&g\\\bar g&b_2\end{pmatrix}
\in\operatorname{Herm}_2(\mathbb H),
\qquad
\theta_2(B)=(b_1,b_2,g_0,g_1,g_2,g_3)^T,
$$

and take

$$
w_0=(0,0),\qquad w_1=(1,0),\qquad w_2=(0,1),
\qquad w_3=(-\mathbf i,-\mathbf j).
$$

In pair order $(01),(02),(03),(12),(13),(23)$, the coefficient matrix is

$$
M_2=\begin{pmatrix}
1&0&0&0&0&0\\
0&1&0&0&0&0\\
1&1&0&0&0&-2\\
1&1&-2&0&0&0\\
2&1&0&0&-2&-2\\
1&2&0&2&0&-2
\end{pmatrix}.
$$

Bareiss elimination uses pivots $1,1,-2,-4,8$, row swaps $(3,4),(4,6)$, and terminal entry $-16$.  Hence

$$
\det M_2=-16=-2^4,
\qquad
\theta_2(B)=2M_2^{-1}y_{\mathrm{obs}}.
$$

The script `verify_consolidation_v2.py` constructs both matrices again from quaternion multiplication, checks these determinants and exact reconstructions, and records its results.  The calculation in this appendix is the proof; the script is a reproducibility check.
