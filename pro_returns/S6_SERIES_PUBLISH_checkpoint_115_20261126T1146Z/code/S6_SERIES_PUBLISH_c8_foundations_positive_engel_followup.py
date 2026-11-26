"""Precise notation and wording follow-ups from the full edited Engel reading."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("positive_engel_weights", "C8-FND-POSITIVE-ENGEL-FOLLOW-")
    e.replace("Over $R=\\mathbb Z[t]/(t^d-1)$ their degree-two restriction matrix is\n",
              "Over $\\mathcal A_d=\\mathbb Z[t]/(t^d-1)$ their degree-two restriction matrix is\n",
              "D20", "maps:src:D.2.34",
              "Give the coefficient ring a distinct name from the group-presentation matrix R. The renaming is the identity on every polynomial class; the displayed matrix and module operations are unchanged.")
    e.replace("degree-four row is $R$. The augmented branch-simplex complexes\n",
              "degree-four row is $\\mathcal A_d$. The augmented branch-simplex complexes\n",
              "D20", "maps:src:D.2.34",
              "Carry the identical coefficient-ring name to its only remaining module-row use; the identity on polynomial classes is the inverse renaming.")
    e.replace("There are useful closed forms. If both sites are\nlogarithmic and $\\gcd(m_i,n_i)=1$, put\n",
              "For two logarithmic caps with $\\gcd(m_i,n_i)=1$, put\n",
              "D08", "maps:src:D.2.34",
              "State the exact coprime parameter sector directly, retaining both rank endpoints and every closed-form group.")
    e.replace("four use the dual free coordinates; the orientation generators\nagree in degrees zero and six.\n",
              "four use the dual free coordinates. Send the unit generator in\ndegree zero and the complex-orientation generator in degree six\nto their counterparts; in degrees one and five use the unique maps\nof the zero groups.\n",
              "D20", "mapsIII:rem:positive-engel-specializations",
              "Complete the explicit graded homology-coordinate map, distinguishing the H0 unit from the H6 orientation generator and specifying both zero degrees; no geometric or smooth map is inferred.")
    e.finish()


if __name__ == "__main__":
    main()
