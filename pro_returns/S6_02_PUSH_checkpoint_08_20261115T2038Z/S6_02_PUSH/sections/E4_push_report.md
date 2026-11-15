## E.4: completed independent certificate

All 19,701 boxes passed a new 192-bit Arb/acb implementation through python-flint 0.9.0. Only exact rational box endpoints were reused. No mpmath import, old radius, old preconditioner, old root, or old interval routine enters the new proof. The largest certified upper bound is enclosed by 1.999877571767410524070536478244687423578792301873142913 ± 9.26e-56, at zero-based input index 17866. Runtime was 49.0401 seconds. This is a rigorous enclosure, not a sample maximum.

An exact Fraction-based vertical sweep at 438 distinct vertical edges checks all 19,911 leaves: 19,701 norm boxes, 36 local boxes, 174 boxes outside the modular domain. Interiors are disjoint and the exact covered area is 23/40. The entire omitted square lies strictly in the independently treated analytic disc.

The analytic local proof was re-derived with all constants. Independent 256-bit Arb bounds give |G| < 18.372504033, |H| < 0.546229725, d in (10.03,10.04), g2(i)/4 in (47.26,47.30), Rouche lower bound >0.0321759437 and perturbation <0.0307366421, |tau-i|/|h|² <6.123343, |h|² <0.000044338219, and remainder coefficient <4399.024 <5000. The analytic cusp inequalities were also independently evaluated. Together these confirm R3's maximum and radius.

The program initially contained two dead, unreachable expressions while the half-integer theta sum was being entered; they were removed before the final rerun. They had no effect on the results. All operative calculations and final outputs are included. No input files are reproduced.

Literature: Johansson's Arb preprint (arXiv:1611.02831) and the python-flint 0.9.0 arb documentation were opened. This is independent evidence for the supplied return's maximum claim, not a claimed new mathematical result.
