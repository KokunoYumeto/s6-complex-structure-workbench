"""Final local corrections found in the whole edited KK/KL reread."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e=Editor("elliptic_finite_multiplicities", "III-C8-FND-FINITE-FINAL-")
    e.replace("For the marked data of Definition~\\ref{mapsIII:def:yang-finite-data},\nFor integers $n_j,r_j$ with\n$\\gcd(n_j,m_j)=1$, choose the finite translation vectors",
              "For the marked data of Definition~\\ref{mapsIII:def:yang-finite-data},\nchoose integers $n_j,r_j$ with $\\gcd(n_j,m_j)=1$ and take\nthe finite translation vectors",
              "D23", "maps:src:D.2.10",
              "Correct the sentence join after the full input table was moved to its numbered definition.")
    e.replace("\\qquad P=(t^2,t^2),\n \\hypertarget{tag-01Y6}",
              "\\qquad P=(t^2,t^2).\n \\hypertarget{tag-01Y6}",
              "D23", "mapsIII:def:os49-component-zero",
              "End the defining model sentence before the next sentence of the numbered definition.")
    e.replace("For the coefficients $f,g$ of \\eqref{maps:eq:D.C1}, direct calculation gives\n\\[\n 4f^3+27g^2=27t^8(t-1)^2,\\qquad",
              "For the Weierstrass coefficients $a_4,a_6$ of\n\\eqref{maps:eq:D.C1}, direct calculation gives\n\\[\n 4a_4^3+27a_6^2=27t^8(t-1)^2,\\qquad",
              "D23", "maps:src:D.2.11",
              "Avoid reusing f, now the fibration map in the explicit line isomorphism, for a polynomial coefficient; the exact discriminant polynomial is unchanged.")
    e.replace("three for $Q$. Their product determines the third matrix;\nno local-narrowness hypothesis at $I_2$ is used.",
              "three for $Q$. Their product gives the displayed $I_2$ matrix\nfor the component divisor $C_0$.",
              "D02", "maps:src:D.2.11",
              "State the actual component-divisor matrix positively, preserving the previously calculated multidegrees and ordered product.")
    e.finish()


if __name__ == "__main__":
    main()
