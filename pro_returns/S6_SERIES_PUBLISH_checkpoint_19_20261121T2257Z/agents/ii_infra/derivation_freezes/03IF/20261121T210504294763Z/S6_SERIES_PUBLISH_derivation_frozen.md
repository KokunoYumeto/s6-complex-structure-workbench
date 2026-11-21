# Independent derivation before target-proof release

Checker: i_provenance_recovery. Created: 2026-11-21T21:04:53.862060+00:00. The target printed proof, its historical check outcomes, and other agents’ argument records have not been opened. Related Paper I mathematics and already released Paper II inputs were previously read; those exposures do not include this target proof. Inputs below are exact statement-only packets and their supplements. The proofs here are my own current derivations. No source, event ledger or canonical defect record is changed.

Owner: wbII:lem:torsion-identification.

Let R be a local ring of the reduced Cartier divisor and M its finite analytic cotangent module. The multiplicative set U of nonzerodivisors consists of the elements avoiding the finitely many minimal primes. The total quotient ring U^{-1}R is the finite product of the function fields of the irreducible local branches: the map is r/s -> (r mod p_i)/(s mod p_i). Reducedness makes this injective, and localization at each minimal prime supplies the corresponding field. The kernel of M -> U^{-1}M is precisely the set of m killed by some u in U, by the definition of localization.

A torsion differential restricts to zero on the regular locus. Indeed u*m=0 with u avoiding every branch, and on each smooth branch the cotangent sheaf is locally free over a domain. The restricted u is a nonzero germ and multiplication by it is injective on this free module, including at its zeros. Thus m is zero there.

Conversely a germ of a differential whose restriction to the regular locus is zero has zero image in the differential module over every branch function field. Each irreducible branch has a dense regular open set; the local presentation of analytic differentials by the Jacobian matrix becomes a free vector-space presentation over its function field. A section zero on that dense open set has all its coefficients zero in that presentation, by the identity theorem on the branch. Equivalently its cyclic coherent submodule is supported on an analytic set containing no irreducible component, and its annihilator therefore avoids each minimal prime. Prime avoidance selects a nonzerodivisor in the annihilator. Thus the germ maps to zero in U^{-1}M and is torsion.

These two inclusions are inclusions of subsheaves of Omega_S, commute with restriction, and give the exact asserted kernel equality with j_*Omega_{S_reg}; no isomorphism between arbitrary quotients is presumed. The Cartier hypothesis is compatible with the local presentation; the proof actually uses reducedness and generic smoothness in characteristic zero, without strengthening the manuscript statement. No numerical program is invoked.

## Bound inputs

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03IF_statement_inputs.tex SHA256 ffe1699b2e155773016746e3653e6a20379cdefc774d16418e0b3c98fa020735
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03IF_cited_input_supplement.tex SHA256 972c60da33dce001d4022ed4a0ee6188dce5863b9a6619291e468b33e6de38fe
