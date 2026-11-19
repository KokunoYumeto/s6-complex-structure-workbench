# The meridian-line / physical-line change of variables

GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

This derivation was written after reading the statements of maps:src:B.6.17,
maps:src:B.6.20 and night:P3K.68 and before reading the printed proof steps of
B.6.17 or B.6.20. It checks this change of variables only; it neither proves
the geometric line identification supplied by K68 nor rereads the entire
Pontryagin-class calculation.

K68 specifies the actual duality arrow U = M^{-1}, with U the
outward-meridian-one Thom line and M the line carrying the physical positive
delta circle. Hence c_1(M) = -c_1(U). Keep the orientation of the quotient Q
fixed. Write x_U = c_1(U) and choose y_U by <x_U y_U,[Q]> = 1. For the
physical generator x_M = -x_U, the corresponding normalized generator is
y_M = -y_U: their cup product still evaluates to 1.

For the meridian-one equations x_U^2 = k_U y_U and p_1(Q) = ell_U y_U,

    x_M^2 = x_U^2 = k_U y_U = -k_U y_M,
    p_1(Q) = ell_U y_U = -ell_U y_M.

Thus k_M = -k_U and ell_M = -ell_U. The actual reference values
(k_U,ell_U)=(-1,-4) therefore give (k_M,ell_M)=(1,4). Moreover

    A_M = (4 k_M - ell_M)/24 = -(4 k_U - ell_U)/24 = -A_U.

For these values both numerators vanish. The parameter and quotient
orientation are unchanged in this calculation; only the dual line and its
normalized degree-four generator are changed by the displayed arrows.

Proposed receiving wording for both B.6.17 and B.6.20:

“Here the Euler class is x_U=c_1(U) for the meridian-one line U=M^{-1}
of K68. Keeping the quotient orientation, x_M=-x_U and y_M=-y_U preserve
<x_M y_M,[Q]>=1. Consequently the displayed meridian pair (-1,-4)
corresponds to the physical pair (1,4).”

The global geometry, the definition of the actual free-circle quotient,
and the K68 line/endpoint maps remain the responsibility of the full Paper IV
renewed proof check.
