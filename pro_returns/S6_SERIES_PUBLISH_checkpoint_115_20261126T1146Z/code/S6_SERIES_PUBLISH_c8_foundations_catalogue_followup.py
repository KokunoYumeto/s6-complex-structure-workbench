"""Resolve the two definition/remark joins found during catalogue rereading."""
from S6_SERIES_PUBLISH_c8_foundations_editing import Editor


def main():
    e = Editor("elliptic_catalogue", "c8-III-foundations-catalogue-joins-")
    e.replace(r"""{\normalfont\scriptsize tag Q110}\par
Write $\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$,
$\chi=\gamma^*$, $P=aG$, $Q=bG$ and
$\langle G,G\rangle=1/d$.""", r"""{\normalfont\scriptsize tag Q110}\par
For each of the twenty-one rational elliptic profiles in the tables,
let $f:S\to\mathbb P^1$ be its marked surface and let $G$ generate
its Mordell--Weil group. The ordered elliptic periods are $e_1,e_2$;
$\delta$ is the positive line circle and $\gamma$ is the forward
linearization period. Write
$\Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle$,
$\chi=\gamma^*$, $P=aG$, $Q=bG$ and
$\langle G,G\rangle=1/d$.""", "D05", "mapsIII:def:elliptic-marked-data",
              "The relocated definition now precedes KX, so explicitly introduce its surface, Mordell--Weil generator and all four marked periods instead of inheriting them from that later theorem.")
    e.replace(r"""vector $(0,0)$, and tensoring by $\mathcal O(C_1)$ gives the
map from the component line to this whole-fibre line; tensoring
by $\mathcal O(-C_1)$ is its inverse.""", r"""vector $(0,0)$. Multiplication of local meromorphic sections gives
$\mathcal O(C_0)\otimes\mathcal O(C_1)\simeq
\mathcal O(C_0+C_1)$. The tensor functors
$L\mapsto L\otimes\mathcal O(C_1)$ and
$L\mapsto L\otimes\mathcal O(-C_1)$ are inverse under the
evaluation identification
$\mathcal O(C_1)\otimes\mathcal O(-C_1)\simeq\mathcal O$;
they carry these two line bundles to each other.""", "D20", "mapsIII:rem:vertical-section-lines",
              "Specify the exact multiplication and inverse tensor functors relating the component and whole-fibre lines; do not suggest an unsupported isomorphism between the untensored line bundles.")
    e.finish()


if __name__ == "__main__":
    main()
