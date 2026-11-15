"""Record the completed semicomplete-field proof and the canonical support audit."""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).isoformat()
(root / 'records/root_research_semicomplete.md').write_text(f'''# Semicomplete specialization and canonical support

UTC: {stamp}

The root read UN15 in full and accepted its proof after the same independent Chow-stratum precision was identified by E. The final source uses countably many locally closed strata of reduced irreducible invariant curves. Their incidence images are constructible. Baire applied to their closures produces a dominating stratum; uniqueness of the regular leaf gives a parameter curve and a generically one-to-one incidence map. Compactification, normalization and resolution give the actual first integral. The generic compact fibre carries a nonzero semicomplete meromorphic field, so the time-primitive branch calculation excludes every pole; its genus is at most one. Restriction of pluricanonical systems to that fibre excludes general type directly.

The other leaf case uses Guillot2019 MainTheorem precisely as printed, allowing a maximal single-valued solution with any domain, not only an entire solution. The root opened and read the primary arXiv1603.02288v2 theorem, Definition5, and following clarification. The actual family reduction is a normalized targeted cyclic base change t=s^m, followed by resolution, with a multiplicity-one component E mapping generically finitely to the chosen original normalization. The Jacobian divisor proves general type would pass to E. A coherent relative holomorphic field is divided by its generic order along E. It is complete on the punctured torus fibres. Guillot2024 Theorem3.3, read with its proof, gives semicompleteness on the ambient holomorphic locus. Invariance of E and a second use of closedness remove any extra deleted curves where the ambient poles cancel after restriction. This gives the required nonzero semicomplete meromorphic field on E. Root, A and E independently checked these maps. UN15 therefore proves that every normalization component has Kodaira dimension at most one, without an ambient Kähler assumption.

This settles the torus-specific general-type component obstruction recorded at checkpoint06. Kollár's broader conjecture was never invoked as a theorem. Its earlier appearance in the records describes the research state at that time; UN15 supersedes that particular undecided step. The unrestricted reducible zero-Euler classification remains incomplete because component occurrence and gluing have not been exhausted.

The root also audited UN17 in full. Its canonical evaluation gives K_U=O(sum a_i S_i); the full-fibre principal divisor and the intrinsic conductor give the exact identity m_i(K_Zi+D_i)=sum [m_i a_j-m_j(a_i+1)]E_ij. Pushing an actual meromorphic pluricanonical section to the minimal model retains the required supported signed divisor. In classVII the negative-definite blocks force nonpositive coefficients, while a positive kernel vector on a singular block forces that block's divisor class to vanish. This yields an effective rational numerically anticanonical divisor. Clearing denominators and integral torsion, then using the exact constant/holomorphic exponential comparison, supplies the complex-flat twist required by Dloussky's theorem. The root opened arXivmath/0406387v3, Theorem0.2, its exact flat-twisted hypothesis and the intersection facts in Section1. The proof is accepted. The b2zero curve criterion remains the previously checked Dloussky–Teleman comparison. A stronger two-translation-field restriction is being developed independently as UN16.
''')
p = root / 'S6_03_CDP_report.md'
s = p.read_text()
s = s.replace('C.2.UN.1–14; A.5.18–21', 'C.2.UN.1–15,17; A.5.18–21')
s = s.replace('The main remaining question is unrestricted reducible zero-Euler geometry.',
              'The remaining question is unrestricted reducible zero-Euler geometry; the general-type component obstruction recorded at six hours is now excluded by UN15.')
marker = '## General-type components excluded by actual translation limits'
if marker not in s:
    s += '''
## General-type components excluded by actual translation limits

C.2.UN.15 proves that every normalization-resolution component of an arbitrary proper torus-surface degeneration has Kodaira dimension at most one. Its proof retains the non-Kähler total space: a targeted cyclic base change makes the chosen covering component multiplicity one; a relative translation field, divided by its generic vanishing order, restricts nontrivially to it. The closed-univalence theorem makes the resulting meromorphic field semicomplete. Guillot's surface theorem handles a dense solution leaf, and the explicit invariant-curve incidence construction handles the algebraic-leaf case. Both exclude general type. The root and two independent agents accepted the exact maps and final proof. This settles the precise general-type component issue that was undecided at checkpoint06; the broader Kollár conjecture is not used.

C.2.UN.17 independently proves the canonical-support identity for every component, including the interface multiplicities and intrinsic conductor. A classVII minimal normalization has a curve; with b2zero it is Hopf. With positive b2 the supported canonical class yields a flat-twisted numerically anticanonical divisor through a complete semidefinite-matrix argument, and Dloussky's proved theorem gives a global spherical shell. This is a necessary component restriction with no assertion that every such surface occurs.

The exhaustive reducible zero-Euler classification is still unfinished. The next work concerns the stronger restrictions imposed by both torus translation fields, their finite-cover descent, and occurrence and gluing among the remaining Kodaira-dimension-zero and one components.
'''
p.write_text(s)
print(json.dumps({'utc': stamp, 'accepted': ['C.2.UN.15', 'C.2.UN.17'],
                  'settled_obstruction': 'general-type normalization component',
                  'remaining': 'exhaustive unrestricted reducible zero-Euler geometry'}, indent=2))
