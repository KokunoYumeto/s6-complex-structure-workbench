"""Exact checks for Section 27 (fixed-coupling analytic disk).

These are finite counting and rational-inequality checks only.  They do not
simulate the continuum and make no mass-gap claim.
"""

from fractions import Fraction


def check() -> None:
    for L in range(2, 31):
        m = 2 * L
        M_edges = 3 * m * m * (m + 1)
        M_closed = 12 * L * L * (2 * L + 1)
        assert M_edges == M_closed
        assert Fraction(3, 16 * M_closed) == Fraction(
            1, 64 * L * L * (2 * L + 1)
        )
        xi = Fraction(1, 4)  # g=1
        assert 2 * xi * M_closed == Fraction(M_closed, 2)
        assert (2 * xi * M_closed) / Fraction(3, 4) == Fraction(
            2 * M_closed, 3
        )

    for g in (1, 2, 10, 100):
        xi = Fraction(1, 4 * g**4)
        assert any(
            xi >= Fraction(1, 64 * j**4 * (2 * j**2 + 1))
            for j in range(1, 10000)
        )


if __name__ == "__main__":
    check()
    print("PASS: fixed-coupling analytic-disk obstruction checks")
