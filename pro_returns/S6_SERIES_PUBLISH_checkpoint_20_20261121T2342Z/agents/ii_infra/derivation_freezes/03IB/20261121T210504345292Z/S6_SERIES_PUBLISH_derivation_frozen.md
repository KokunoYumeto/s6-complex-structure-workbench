# Independent derivation before target-proof release

Checker: i_provenance_recovery. Created: 2026-11-21T21:04:53.862060+00:00. The target printed proof, its historical check outcomes, and other agents’ argument records have not been opened. Related Paper I mathematics and already released Paper II inputs were previously read; those exposures do not include this target proof. Inputs below are exact statement-only packets and their supplements. The proofs here are my own current derivations. No source, event ledger or canonical defect record is changed.

Owner: wbII:lem:gluing-bundle.

The exact cited nodal curve construction is also included in the statement-only packet03I9, whose input Proposition B1 defines C0 and its normalization/gluing convention. At the node the analytic local ring is R={(a,b) in C{z} directsum C{w}:a(0)=b(0)}. The gluing module M_lambda={(f,g):f(0)=lambda*g(0)} is invertible: R -> M_lambda sends(a,b) to(lambda*a,b), and its inverse sends(f,g) to(lambda^{-1}f,g). These maps are R-linear inverse maps, so the construction is a line bundle. Pullback to each normalization branch is freely generated, and these trivializations glue to the prescribed trivial line bundle on P1.

A global section pulls back to a holomorphic function on P1 and hence a constant c. Its descent condition is c=lambda*c. Since lambda is not a root of unity, lambda is not1 and c=0. Injectivity of pullback for a locally free sheaf on a reduced curve gives H0=0.

Multiplication on the two normalized components maps M_lambda tensor M_mu -> M_{lambda*mu}; it sends the free generators(lambda,1) tensor(mu,1) to(lambda*mu,1), so is a local isomorphism and respects the fixed trivializations globally. Consequently A_lambda^{tensor m}=A_{lambda^m} through this explicit tensor map. For every m>=1 the scalar lambda^m is not1; the same H0 argument gives no nonzero sections. The trivial line bundle has its section1, so this proves each stated power nontrivial. No finite enumeration is substituted for this all-m argument.

## Bound inputs

- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03IB_statement_inputs.tex SHA256 02b1d83f8a145d4f62909ebb23739a895267b7789954b0a584a7d95576b8c343
- agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03IB_cited_input_supplement.tex SHA256 21bb34ccabfec70149e33a9eff245a0c8af82b37ef76c4a7220e13e341e583c4
- agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03I9_statement_inputs.tex SHA256 b33187161932b65cf6a328a87ba0f2be211f0d5333795b7dae42fff8e6c603b8
