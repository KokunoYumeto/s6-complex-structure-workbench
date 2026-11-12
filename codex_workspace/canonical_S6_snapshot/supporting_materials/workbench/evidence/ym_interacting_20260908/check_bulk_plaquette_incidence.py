"""Exact full-open-box incidence and rational-coefficient diagnostics.

This enumerates the entire finite graph, not a two-face truncation.  It does
not approximate the vacuum, perform a continuum calculation, or use floating
point arithmetic.  The analytic argument is in BULK_PLAQUETTE_EXTENSION.md.
"""

from fractions import Fraction as F
from itertools import combinations, product


def shifted(vertex, axis):
    result = list(vertex)
    result[axis] += 1
    return tuple(result)


def oriented_boundary(face):
    vertex, (i, j) = face
    return (
        ((vertex, i), 1),
        ((shifted(vertex, i), j), 1),
        ((shifted(vertex, j), i), -1),
        ((vertex, j), -1),
    )


def edge_set(face):
    return {edge for edge, sign in oriented_boundary(face)}


q_face = ((0, 0, 0), (0, 1))
p_face = ((-1, 0, 0), (0, 1))
s_edge = ((-1, 0, 0), 1)
e_edge = ((0, 0, 0), 1)
expected_incident = {
    p_face,
    ((-2, 0, 0), (0, 1)),
    ((-1, 0, 0), (1, 2)),
    ((-1, 0, -1), (1, 2)),
}

assert dict(oriented_boundary(p_face))[e_edge] == 1
assert dict(oriented_boundary(q_face))[e_edge] == -1
assert dict(oriented_boundary(p_face))[s_edge] == -1
assert edge_set(p_face) & edge_set(q_face) == {e_edge}
assert len(edge_set(p_face) | edge_set(q_face)) == 7
assert len((edge_set(p_face) | edge_set(q_face)) - {e_edge}) == 6
assert s_edge not in edge_set(q_face)

box_results = []
for half_side in (2, 3, 4, 5):
    vertices = set(product(range(-half_side, half_side + 1), repeat=3))
    edges = {
        (vertex, axis)
        for vertex in vertices
        for axis in range(3)
        if vertex[axis] < half_side
    }
    faces = {
        (vertex, axes)
        for vertex in vertices
        for axes in combinations(range(3), 2)
        if all(vertex[axis] < half_side for axis in axes)
    }
    edge_count = 3 * (2 * half_side) * (2 * half_side + 1) ** 2
    face_count = 3 * (2 * half_side) ** 2 * (2 * half_side + 1)
    assert len(edges) == edge_count
    assert len(faces) == face_count
    assert all(edge_set(face) <= edges for face in faces)
    assert p_face in faces and q_face in faces

    incident = {face for face in faces if s_edge in edge_set(face)}
    assert incident == expected_incident
    intersections = {face: edge_set(face) & edge_set(q_face) for face in incident}
    assert intersections[p_face] == {e_edge}
    assert all(not common for face, common in intersections.items() if face != p_face)
    surviving_pairs = {
        (face, edge)
        for face in incident
        for edge in edge_set(face) & edge_set(q_face)
    }
    assert surviving_pairs == {(p_face, e_edge)}

    # Distinct elementary faces have an edge absent from the other face.
    # This is the incidence input to Haar orthogonality, checked without
    # quadratic pair enumeration by injectivity of the four-edge supports.
    assert len({frozenset(edge_set(face)) for face in faces}) == face_count

    # At the strict Neumann-radius boundary the norm bound is exactly one.
    radius = F(3, 16 * face_count)
    assert F(8, 3) * (2 * face_count) * radius == 1
    assert 2 * face_count * radius == F(3, 8)
    box_results.append((half_side, edge_count, face_count, radius))

# Haar mode norms and the actual dimensionless free electric eigenvalues.
norm_r = F(1)
norm_d = F(3, 4)
lambda_r = 6 * F(3, 4)
lambda_d = 6 * F(3, 4) + 2
assert lambda_r == F(9, 2)
assert lambda_d == F(13, 2)

g_r, g_d = -F(1, 4), F(1, 6)
h_r = g_r / (lambda_r + 1)
h_d = g_d / (lambda_d + 1)
assert h_r == -F(1, 22)
assert h_d == F(1, 45)
norm_g = g_r**2 * norm_r + g_d**2 * norm_d
i_coefficient = g_r * h_r * norm_r + g_d * h_d * norm_d
j_coefficient = h_r**2 * norm_r + h_d**2 * norm_d
improvement = i_coefficient + 4 * j_coefficient
assert norm_g == F(1, 12)
assert i_coefficient == F(7, 495)
assert j_coefficient == F(199, 81675)
assert improvement == F(1951, 81675)
assert improvement / 8 == F(1951, 653400)

for half_side, edges, faces, radius in box_results:
    print(f"L={half_side}: all {edges} links and {faces} faces; "
          f"unique surviving pair (P,e); Neumann radius {radius}")
print("PASS: exact orientation, whole-box incidence, Haar-support injectivity, "
      "free electric energies, and all correction coefficients.")
