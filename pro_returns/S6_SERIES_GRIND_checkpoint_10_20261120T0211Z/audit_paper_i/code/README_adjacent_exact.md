# Paper I adjacent exact calculations

Author: GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family.

Run with Python and SymPy 1.14.0:

    python adjacent_exact.py > adjacent_exact.output.json

The executed output records 55 passed named checks, all exact matrices, an integer inverse for the saturated lattice calculation, the original rational Hermitian example, the exact order-four fibre discriminant, and 481 complete root-count rows. The finite five-pair repetition checks and 481-integer counts corroborate the universal proofs; they do not prove an unrestricted assertion by sampling. The program does not certify analytic properness, extension, or coherent base change.

This is a fresh program written after reading the receiving proofs. It imports none of the absent historical programs. An initial local run caught a transcription of A2(2,1) as 6; comparison with the literal printed matrix corrected that entry to 0. The complete run then passed; no assertion was weakened. The supplement records this development history instead of claiming an inherited executable was recovered.

Guarded publication replacements are in ../I_adjacent_program_patches.json. Their removed sentences remain in that receipt. Mathematical equations and all statement scopes are retained.
