"""Postrelease certificate for the actual quotient R0 -> H in 02YF.

This certifies the cellular homology maps only.  The independent mathematical
proof of the fundamental-group isomorphism is the van Kampen argument recorded
in the accompanying correction; an H1 calculation is not substituted for it.
"""
import json


def apply(columns, vector):
    return [sum(c[j] * x for c, x in zip(columns, vector))
            for j in range(len(columns[0]))]


records = []
for genus in (1, 2, 3, 7):
    for rational_components in (0, 1, 2, 6):
        # A genus-g surface has one 0-cell, 2g 1-cells and one 2-cell.
        # Each attached P1 supplies one further 2-cell.  Its attachment is
        # constant; the surface attaching word is the product of commutators.
        # Thus every cellular differential is zero.
        q2 = [[1]] + [[0] for _ in range(rational_components)]
        i2 = [[1] + [0] * rational_components]
        h2 = [1]
        assert apply(q2, apply(i2, h2)) == h2
        killed = []
        for j in range(1, rational_components + 1):
            fundamental_class = [int(k == j) for k in range(rational_components + 1)]
            image = apply(q2, fundamental_class)
            assert image == [0]
            killed.append({"P1_component": j, "q_H2_image": image})
        records.append({
            "genus": genus,
            "rational_components": rational_components,
            "R0_cell_counts": [1, 2 * genus, 1 + rational_components],
            "H_cell_counts": [1, 2 * genus, 1],
            "R0_euler": 2 - 2 * genus + rational_components,
            "q_H2_columns": q2,
            "i_H2_columns": i2,
            "q_after_i_H2": [1],
            "killed_fundamental_classes": killed,
        })
print(json.dumps({"timing": "postrelease supplement; no new prereading credit",
                  "records": records}, indent=2))
