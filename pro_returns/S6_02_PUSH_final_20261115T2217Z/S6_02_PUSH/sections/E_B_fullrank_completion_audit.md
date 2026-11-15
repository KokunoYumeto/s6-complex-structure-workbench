# Full-rank monodromy and arbitrary analytic caps: source and bridge audit

Owner: classification_e. 15 November 2026. Uninput main-question attempt. B.4.24, B.4.26 and B.4.27 are separately proved at their stated scopes; this note does not enlarge those scopes.

## 1. What is now known

The actual Jacobian has an admissible, nondegenerate logarithmic pairing and proper analytic group models. The actual axial affine torsor nevertheless cannot extend locally trivially in that fixed log-torus category, even after finite coordinate roots and any finite sequence of point blowups over the origin. The decisive exceptional valuation block is diag(12ma,12ma+12nb), with a,b positive.

An arbitrary cap with a holomorphic fixed-bidisc map is subject to the independent finite-multisection argument: every component of its origin fibre must be a threefold. That statement does not require the cap itself to be a log torsor.

## 2. Why flattening does not finish the argument

A proper cap can be flattened after a base modification. Its resulting flat map admits local finite multisections. These local multisections are not automatically one finite multisection over a neighbourhood of the entire exceptional curve. Nor do their traces automatically extend as log-torus sections across the newly introduced exceptional divisor: the geometry over that divisor is the unknown cap, rather than either of the two prescribed fan models used in B.4.26.

This is the exact difference from the proved trace argument. There, every point of each punctured axis lies in a known fan model, and the pulled-back characters are explicitly t^k times units. On the exceptional divisor of an arbitrary flattened cap there is no established toric chart or multiplicative-character extension. Replacing this missing fact by the existence of the abstract Jacobian log torus would be circular.

The remaining possible bridges would be a theorem making every such full-rank two-torus cap a logarithmic torsor after modification, or a direct extension theorem for the difference of local multisection traces. Neither has been proved here. A graph closure of a punctured comparison is not assumed analytic or proper.

## 3. Primary-source scopes checked

1. Kajiwara, Kato, and Nakayama, *Logarithmic Abelian Varieties, Part I: Complex Analytic Theory*, J. Math. Sci. Univ. Tokyo15(2008),69–193, original PDF https://www.ms.u-tokyo.ac.jp/journal/pdf/jms150104.pdf. Theorems5.2.1 and5.3.2 construct proper models from a specified log torus. They do not classify arbitrary analytic completions. Example3.9.3 gives an unpolarized torus variation without a log extension, but its pairing is inadmissible; that example cannot obstruct the actual admissible pairing proved here.

2. Kajiwara, Kato, and Nakayama, *Analytic Log Picard Varieties*, Nagoya Math. J.191(2008),149–180, DOI10.1017/S0027763000025940, original publisher PDF opened. Definition7.1 imposes log de Rham comparison and Hodge goodness; Section8 additionally assumes a degree-one invariant-cycle isomorphism. Section9 supplies projective/log-Kähler sufficient conditions. These are not consequences of arbitrary properness with non-Kähler vertical components. Exact pages are recorded in B_log_torsor_references.bib and E_B_general_completion_attempt.md.

3. Kamenova, *Degenerations of 2-dimensional tori*, original author manuscript https://www.math.stonybrook.edu/~kamenova/homepage_files/degen.pdf. Theorem3.1 retains both a Kähler total space and trivial canonical bundle. Its rational-component/maximal-monodromy case therefore supplies no classification at the present unrestricted hypotheses. The original source was previously opened and its access metadata is retained in B_analytic_comparison_references.bib.

4. Nishiguchi, *Degeneration of K3 surfaces, II*, original MPI preprint88-48, https://archive.mpim-bonn.mpg.de/id/eprint/3390/1/preprint_1988_48.pdf, reopened for this audit. The title and introduction explicitly concern K3 surfaces. The source treats non-Kähler components and presents Conjectures1.9 and4.7 about the corresponding monodromy. It is not a proved full-rank TWO-TORUS comparison theorem. It is retained as a warning against silently transferring Kähler classification, not as an authority for the missing torus bridge.

5. Nakayama's original published elliptic extension criterion, Theorem7.1.3 on p.604 of PRIMS38(2002),451–649, has been visually read together with its flattening step on p.605. It genuinely allows arbitrary proper elliptic extensions, but its relative dimension is one. The actual two-parameter period matrix admits no analytic family of elliptic quotients on any open set, even after finite base change, as proved directly in E_B_general_completion_attempt.md. Thus that reduction is unavailable.

Broad searches also returned secondary and AI-generated summaries related to complex structures on spheres. Those were not used as authorities. Search metadata is in evidence/E_B_fullrank_search_log.json. The search outcome is not a claim that no relevant theorem exists; it records that none with the required hypotheses was found or verified in this attempt.
