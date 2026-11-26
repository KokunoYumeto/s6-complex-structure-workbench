"""Final exact notation scopes identified in the complete LI readback."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("weighted_integral_homology", "C8-FND-INTEGRAL-WEIGHTS-NOTATION-")
    owner = "maps:src:D.2.41"
    e.replace("For $u,v\\in\\Lambda$ set\n", "For $A\\in\\{A_0,\\ldots,A_r\\}$ and $u,v\\in\\Lambda$, set\n", "D05", owner,
              "Specify the exact already defined weighted matrix domain of D_A and f_A at first use; their formulas and used scope are unchanged.")
    contexts = [
        (r"$\tau=2\rho$, so $2\rho-\tau=h\circ\operatorname{graph}$.", r"$\tau=2\rho$, so $2\rho-\tau=\mathfrak h\circ\operatorname{graph}$."),
        ("$h(k_j)=2z(k_j)+\\sum_t s_{t-1}\\wedge v_t$.\nThe maps $(c,k)\\mapsto(c-h(k)/2,k)$", "$\\mathfrak h(k_j)=2z(k_j)+\\sum_t s_{t-1}\\wedge v_t$.\nThe maps $(c,k)\\mapsto(c-\\mathfrak h(k)/2,k)$"),
        (r"$(c,k)\mapsto(c-h(k)/2,k)$ and its addition inverse constructed", r"$(c,k)\mapsto(c-\mathfrak h(k)/2,k)$ and its addition inverse constructed"),
    ]
    for old, new in contexts:
        e.replace(old, new, "D20", owner,
                  "Name the graph-to-fibre comparison homomorphism mathfrak-h separately from the finite linear order h. Identity on its values and every displayed inverse is the exact renaming map.")
    e.finish()


if __name__ == "__main__":
    main()
