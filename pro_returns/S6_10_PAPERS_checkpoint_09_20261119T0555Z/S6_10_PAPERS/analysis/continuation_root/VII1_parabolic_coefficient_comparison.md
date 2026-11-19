# VII.1 step 2: exact comparison of the current coefficient argument

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

The root independently wrote `VII1_parabolic_coefficient_before_read.md`
from the isolated statement and the supplied parabolic-Inoue inputs.
It was saved before opening `VII1_printed_step2_only.tex`. No other
part of VII.1's printed proof was opened for this check.

The first part matches exactly: intersection with E gives coefficient
one, and the cycle intersection-matrix kernel makes all coefficients
of C equal. The exact canonical line-bundle relation then gives
O(K+D)=O((k-1)C). The prereading proof takes a tensor power
trivializing that line bundle, compares its meromorphic canonical
section with a trivialization, and obtains a meromorphic function with
divisor n(k-1)C. For k>1 compactness applied to the function is a
contradiction; for k=0 apply it to the reciprocal. This proves k=1.

The former printed ending used the degree of C under a Gauduchon
metric. That particular route was not written in the root prereading
derivation. It has now been replaced, at the root's request, by the
tensor-power meromorphic-function argument. The VI owner preserved
the former complete block and exact old/new paragraph in
`analysis/continuation_VI/VII1_coefficient_replacement_receipt.json`.
The active revision and both VI body files contain the replacement.
The new text agrees with the written prereading proof, under the
explicit variable conversion t=k-1. No fault in the former argument
is asserted and no prereading credit is assigned to its degree route.

This is a targeted independent proof of the full current coefficient
step. It uses the supplied canonical relation and intersection kernel
as cited inputs, and makes their actual line-bundle-to-function map
explicit. It claims no root re-proof of the other VII.1 steps, no new
computation certificate, and no independent review of the cited
classification theorem. Those scopes belong to the other reviewers.
