"""Exact integer budgets in C.2.RAT.2 and C.2.RAT.4.

This checks the finite numerical consequences of the independently proved
geometric inequalities. It does not assume or certify an existence result.
"""
from fractions import Fraction


def smooth_budget():
    possible = []
    for a_degree in range(0, 9, 2):
        quartic_degree = 8 - a_degree
        if a_degree >= 2 and quartic_degree >= 6:
            possible.append((a_degree, quartic_degree))
    assert possible == [(2, 6)]
    return possible


def singular_attachment_budget():
    rows = []
    for singular_preimages in range(4):
        # Every singular preimage is a zero.  For s=3 the node+cusp
        # orders are at least 1+1+2.  No sharper s=1 order is needed.
        minimum_singular_order = (0, 1, 2, 4)[singular_preimages]
        for singular_branch_points in range(min(2, singular_preimages) + 1):
            regular_branch_points = 2 - singular_branch_points
            for a_degree in range(0, 9, 2):
                if a_degree < minimum_singular_order + regular_branch_points:
                    continue
                quartic_degree = 8 - a_degree
                parity_cost = 3 * regular_branch_points + singular_branch_points
                if quartic_degree < parity_cost:
                    continue
                quartic_double_bound = (quartic_degree - parity_cost) // 2
                # A regular nonbranch value with an attachment is a further
                # zero of a, distinct from the regular branch points.
                hessian_double_bound = (a_degree - minimum_singular_order
                                        - regular_branch_points)
                regular_double_bound = min(quartic_double_bound,
                                           hessian_double_bound)
                singular_double_bound = singular_preimages - singular_branch_points
                total_double_bound = regular_double_bound + singular_double_bound
                exact_algebraic_bound = Fraction(2 * singular_preimages + 2 - a_degree, 2)
                assert total_double_bound <= exact_algebraic_bound
                assert total_double_bound <= 1
                rows.append((singular_preimages, singular_branch_points,
                             a_degree, quartic_degree, total_double_bound))
    return rows


if __name__ == "__main__":
    print("C.2.RAT.2 smooth double cover: (Hessian degree, quartic degree)")
    print(smooth_budget())
    print("C.2.RAT.4 rows: (s, B_s, A, 8-A, maximum double attachments)")
    for row in singular_attachment_budget():
        print(row)
    print("All exact degree and attachment inequalities passed.")
