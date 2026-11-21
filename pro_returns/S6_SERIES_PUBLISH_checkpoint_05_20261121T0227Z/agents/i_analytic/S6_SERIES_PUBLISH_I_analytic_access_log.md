# Paper I analytic check: access sequence

Source SHA256: d2e6c3bec1500144bfc0ef85e636ded534f2abc998cf58fdaf521b1e8a183169.

The first automatic statement extractor omitted the `cited` environment and therefore began at the preceding ordinary proposition. It exposed the following additional material before the derivations: the proof of ari:C.1.3 and the rational-model setup preceding ari:C.4.1; the proof of dependency ari:C.7.6; the source-scope and normalization discussion following ari:C.7.7 and ari:C.7.8, including their pointers to Waldschmidt Theorem1/Corollary1, the analytic subgroup theorem, and Rubin AppendixA TheoremA.1/LemmaA.2; and the proof of preceding inv:C3.5. The output was truncated and repeated some of that material.

No expanded proof of any of the four target results was opened in that extraction. The target body blocks are all `cited` statements followed by pointers to expanded proofs outside those blocks. The corrected extractor reads only each `cited` statement. The adjacent proof of ari:C.7.6 is a cited dependency input; the preceding numerical/metric propositions are not target steps. The access is not described as pristine statement-only reading. Targeted credit will be assigned only to target steps derived and recorded before their corresponding printed derivation is opened. Whole-result independence is not inferred from partial coverage.

The four target statements, exact source line spans and hash are saved separately. Their cited dependency statements have also been extracted without their proof bodies, except the already disclosed accidental ari:C.7.6 proof exposure. Primary literature statements are being opened before deriving the target applications.

Created UTC: 2026-11-21T00:43:37.460480+00:00
