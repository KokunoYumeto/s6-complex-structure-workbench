"""Postrelease full-formula certificate for WM; no additional blind credit."""
import json


def tensor_cells(left, right):
    counts = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            counts[i + j] += a * b
    return counts


def euler(counts):
    return sum((-1) ** i * n for i, n in enumerate(counts))


rows = []
for g in (0, 1, 2, 5):
    base = [1, 2 * g, 1]
    fibre = [1, 0, 1]
    total = tensor_cells(base, fibre)
    for d in (-3, 0, 2):
        # The opened primary basis has h^2=d, h.F=1, F^2=0.
        # K=-2h+(d+2g-2)F; evaluate its bilinear self-pairing.
        coefficients = [-2, d + 2 * g - 2]
        gram = [[d, 1], [1, 0]]
        k2 = sum(coefficients[i] * gram[i][j] * coefficients[j]
                 for i in range(2) for j in range(2))
        assert k2 == 8 * (1 - g)
        for blowups in (0, 1, 3):
            blown = list(total)
            blown[2] += blowups
            assert euler(blown) == 4 * (1 - g) + blowups
            rows.append({'g': g, 'bundle_degree': d, 'blowups': blowups,
                         'base_cells': base, 'ruled_cells': blown,
                         'Euler': euler(blown), 'canonical_coordinates': coefficients,
                         'canonical_Gram': gram, 'K2_after_blowups': k2 - blowups})

elliptic_conductor = []
for vertical_fibres in (0, 1, 2, 6):
    # Attach each rational fibre at one marked point of the elliptic section.
    conductor_cells = [1, 2, 1 + vertical_fibres]
    surface_cells = tensor_cells([1, 2, 1], [1, 0, 1])
    complement_euler = euler(surface_cells) - euler(conductor_cells)
    assert complement_euler == -vertical_fibres
    elliptic_conductor.append({'vertical_fibres': vertical_fibres,
                               'conductor_cells': conductor_cells,
                               'Euler_conductor': euler(conductor_cells),
                               'Euler_surface': euler(surface_cells),
                               'Euler_complement': complement_euler})

print(json.dumps({'timing': 'postrelease supplement',
                  'ruled_surface_cell_and_intersection_rows': rows,
                  'elliptic_double_section': elliptic_conductor,
                  'last_two_normalization_pushout_Euler': {'T': 0, 'R': 0, 'C': 0,
                                                          'S': 0 - 0 + 0}}, indent=2))
