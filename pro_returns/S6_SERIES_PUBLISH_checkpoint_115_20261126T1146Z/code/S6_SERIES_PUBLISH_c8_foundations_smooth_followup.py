"""Exact wording and relocation follow-ups found in the full readback."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_smooth_logs", "C8-FND-SMOOTH-FOLLOW-")
    e.replace("and the displayed affine cocycle map give exactly the admitted\nadditive tuples; reversing the moves supplies the five-place marking.\n",
              "and the displayed affine cocycle map give exactly the additive\ntuples of Theorem~\\ref{maps:src:D.2.12}; reversing the moves\nsupplies the five-place marking.\n",
              "D08", "maps:src:D.2.13",
              "Replace the workflow qualifier by the exact preceding mathematical owner of the additive tuples.")
    e.replace("$\\sum_Ia_I\\det K_I=1$, the map\n",
              "$\\sum_Ia_I\\det K_I=1$. The map\n",
              "D23", "maps:src:D.2.13",
              "Close the coefficient-choice sentence before stating the inverse-map identity.")
    e.replace(r"""$H_2(X;\mathbb Z)=G$. We use the marking
$\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$ of that
theorem, and write $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
""", r"""$H_2(X;\mathbb Z)=G$. We use the period marking of
Definition~\ref{mapsIII:def:smooth-logarithmic-data} and write
$J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
""", "D20", "maps:src:D.2.14",
              "Point the suspension proof to the now unique numbered period definition instead of the relocated theorem input.")
    e.finish()


if __name__ == "__main__":
    main()
