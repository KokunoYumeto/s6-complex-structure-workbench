"""Integer-only replay of the printed finite-field Bezout identity."""
f = [39,85,79,93,67,20,38,98,26,56,8,25,28]
g = [1,87,96,7,76,88,75,93,53,73,64,41,16]
a = [4,60,31,59,74,31,34,18,59,97,95,96]
b = [46,85,47,5,14,36,38,21,35,48,34,53]
assert len(f) == len(g) == 13
assert len(a) == len(b) == 12
assert f[0] % 101 and g[0] % 101
assert 39 * 39 % 101 == 6
result = [0] * 24
for u, v in ((a, f), (b, g)):
    for j, uj in enumerate(u):
        for k, vk in enumerate(v):
            result[j+k] = (result[j+k] + uj * vk) % 101
assert result == [0] * 23 + [1], result
print("PASS: all 24 coefficients of a*f+b*g=1 in F_101[t], degrees preserved")
