import sympy as s

z, e = s.symbols('z e')
for truncation in range(1, 13):
    ideal = s.groebner([z*e, e**2, z**truncation], z, e)
    assert ideal.reduce(e)[1] == e
    assert ideal.reduce(z*e)[1] == 0
    assert ideal.reduce(e**2)[1] == 0
    basis = [z**j for j in range(truncation)] + [e]
    assert len(basis) == truncation + 1
    assert all(ideal.reduce(mon)[1] == mon for mon in basis)
print('E17 square-zero local algebra: embedded section e survives all 12 truncations')
print('E17 h^q(O_Z(-kD)) = (max(1-k,0)+1, max(k-1,0), 0 for q>=2)')
for k in (-2, 0, 1, 2, 7):
    h0, h1 = max(1-k, 0)+1, max(k-1, 0)
    assert h0-h1 == 2-k
    print('  k =', k, ':', (h0, h1))

