# Independent derivation of01GW before target-proof release

Owner: cdp:st:E7. Checker: i_provenance_recovery. Written 2026-11-21T21:11:10.684688+00:00.

The Paper II E7 proof, C’s notes/snippet and all old E7 check outcomes remain unopened. Related Paper I construction and its previously completed checks are disclosed prior exposure. I have now read the exact primary construction inputs listed below, including the comb paper’s logarithmic period/Hodge-frame construction. Those are declared inputs; no E7 manuscript argument has been supplied.

## Exact Kodaira–Spencer map for the marked periods

On a simply connected piece of the regular base take the constructed torus T_q=C^2/(Z^2+Z(q)Z^2), with the first two lattice generators a_i=e_i constant and b_j=Z(q)e_j. A constant complex-valued lattice1-cocycle has values(a,b) on these two pairs. Its image in H1(T_q,O) is the quotient by holomorphic linear functions on C2, whose values are(a,aZ). The quotient map is explicitly(a,b)->b-aZ. Its kernel is exactly those holomorphic linear functions. This identification also follows from the flat Kähler metric: harmonic1-forms are constant and the H^{0,1} projection has kernel the complex-linear forms. Thus the two classes eta_j with a-values0 and b-values the jth unit row form a basis of H1(O); a cocycle with those a-values and zero class would have a complex-linear functional vanishing on e1,e2 and hence would be zero.

The torus tangent bundle is O tensor C2 by translation. On local covering charts the transition for b_j is z_j=z_i+Z(q)e_j. A lift of the base vector partial_q with z_j held constant differs from the lift with z_i constant by -Z'(q)e_j in the tangent space. With the Čech boundary lift_j-lift_i, its class is therefore

 kappa(partial_q)=-sum_{i,j} Z'_{ij}(q) e_i tensor eta_j.

This is the connecting class of the relative tangent exact sequence, the same Kodaira–Spencer tensor used in input E5. It has rank equal to the2x2 matrix -Z'(q), through the displayed isomorphisms on both tensor factors; its determinant equals det Z' because the dimension is two. A change of local origin is translation by a holomorphic section and changes the local lifts by a Čech coboundary, so this exact class and rank persist for the affine torus family.

## The actual construction data for each listed family

For the period family X_c, Paper I equation label wb:pshift:eq:cusp-periods gives Z_c(q)=sB0+C_c(q), s=log(q)/(2*pi*i), B0=((0,1),(-1,0)), with C_c holomorphic on the cusp disc. The regular torus marking is[Z_c|I]; permuting its two pairs of columns gives precisely the(a,b) marking above, without changing the lattice or the fibre. The maps are the identity on C2 and the displayed permutation on Z4. Every finite affine twist changes finite caps/origins, with the same cusp lattice. On a regular local disc a translation identifies the torsor with its Jacobian, by z->z+sigma(q), and the preceding coboundary calculation applies. This includes |p|>1. The higher multiplicity construction X_{3k,4l} pulls back only the finite root models by s->s^k and s->s^l; Paper I’s common cusp charts and integral dictionary retain this same cusp lattice. The finite root charts lie over0 and1, whereas the cusp disc is at infinity; their replacement leaves this punctured cusp map unchanged. Thus all these actual constructions have the stated invertible residue matrix B0.

For Viaclovsky’s two-parameter family, the primary source equations(periods) at the distinguished p3 have generators(q*alpha(q),beta(q)) and(gamma(q),lambda*q*delta(q)), with all four functions holomorphic units and lambda fixed nonzero. In the coordinatewise exponential covering exp(2*pi*i*z), the angular loops give e1,e2, and the other two additive periods are the columns of

 Z(q)=log(q)/(2*pi*i)*I + (2*pi*i)^{-1}[[log alpha,log gamma],[log beta,log(lambda*delta)]].

Each unit has a holomorphic logarithm on the disc; changing its logarithm adds an integral lattice column, whose derivative is zero. This gives the exact map from the stated multiplicative quotient to the additive lattice quotient and an invertible residue matrix I for each admitted member.

For the comb construction, the primary local models equation(tau) and Proposition(hexfill) give Z_s(q)=log(q)/(2*pi*i)*I+H_s(q) for every admissible smoothed period section, with H_s holomorphic across q=0. The exponential map and period generators are explicitly the same ones in its equations(g1),(g2). The comb deformation fixes the marked plane at the hexagonal fibre, so this local graph model is among the supplied construction inputs. The original handle and the resulting smooth family members all retain this exact local form.

For Liu–Rollenske, the proof of their Proposition(compactification X) gives near infinity the multiplicative generators(c1(q)*q,c2(q)),(c3(q),c4(q)*q), all ci units. Taking the same coordinatewise exponential covering yields Z=log(q)/(2*pi*i)*I+H(q). Their finite logarithmic transformations at0 and1 leave this infinity neighbourhood unchanged. This supplies the same local map for every admitted nonzero quotient parameter.

## Invertibility and the stated conclusions

For each actual model just listed, put B=B0 or I and H=C_c or the explicitly written holomorphic logarithm matrix. Then

 Z'(q)=(2*pi*i*q)^{-1}(B+2*pi*i*q*H'(q)).

The determinant of the matrix in parentheses tends to det B=1 as q->0. Its determinant is holomorphic on the disc and has value1 at0, so it stays nonzero on a smaller disc. Hence there are regular values q!=0 at which kappa has rank two. The new exact polynomial program certifies det(B+uM)=det B+u*tr(adj(B)M)+u^2 det(M) and det B=1 for both residue matrices. The analytic extension/value argument, rather than finite samples, supplies the full punctured-disc conclusion.

The primary constructions and current Paper I furnish proper connected torus fibrations from smooth compact threefolds, so all hypotheses of the supplied input E6 are met. Its conclusion gives the retained map to P1 for every sufficiently small deformation, including its stated analytic-germ scope. For each member with b2=0, E6’s final clause gives algebraic dimension one throughout the small deformation family. Equivalently smooth proper deformation preserves b2 by the differentiable bundle theorem and E1 identifies the meromorphic function field via the retained torus map. These are applications of the explicitly supplied E6/E1 statements, not additional unsupported deformation assertions. The comb-paper Section10(1) asks precisely this retention question for its constructed members, so this establishes the target’s answer.

## Exact input and code bindings

{
  "inputs": [
    {
      "path": "agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_01GW_statement_inputs.tex",
      "sha256": "7de1302cc10320af12596382cc7af2648667fbf78481051ff80a8133f4ff93b0"
    },
    {
      "path": "agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_01GW_cited_input_supplement.tex",
      "sha256": "c2c3f1e928161fa578f6cbdef6ba2e12509b13add1347fbb8f676d8e84b5975b"
    },
    {
      "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_01GW_primary_locator_inputs.json",
      "sha256": "ee8d33c8f35c0d56371d30dc492507b9e445fb23ae3846363fa70f1f706db969"
    },
    {
      "path": "agents/ii_infra/S6_SERIES_PUBLISH_II_front_main_statements_conventions.tex",
      "sha256": "7d5afda78d4bdcc4e158ef40457a8f609b32b7df96eb51769f196531564a4bae"
    },
    {
      "path": "S6_SERIES_PUBLISH_I.tex",
      "sha256": "179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74"
    },
    {
      "path": "/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH_work/S6_GRIND_6_literature/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex",
      "sha256": "11cb218c0d67fae857c2538cd259bb10988eb9bd6c65475fe616c2929845cd9c"
    },
    {
      "path": "/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH_work/S6_GRIND_6_literature/papers/arXiv_2610.10451_Viaclovsky_combs_src/Viaclovsky_Comb_S6_Draft_October_7_2026.tex",
      "sha256": "42dea62b023dfb75a009a8c83c15349ddc8f853162f753e3547ca583d07b74d5"
    },
    {
      "path": "/workspace/scratch/08a92fb2355d/S6_SERIES_PUBLISH_work/S6_GRIND_6_literature/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex",
      "sha256": "d3cdd5ffbd84d03ea0180988a92e4c0627b76cc47dc9375365e61c8dcc4d377e"
    }
  ],
  "program": {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_01GW_preproof_determinant.py",
    "sha256": "3513f0759dfaf2ea59309f82a1612970e2611ad421322339f12f1f1061de548d"
  },
  "program_output": {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_01GW_preproof_determinant.output.json",
    "sha256": "901a84cb46b327ac5ecf8a5fcfa34eb76af1bb6cea31b0630b2bce00b4d25c49"
  },
  "primary_loci_read": {
    "ViaclovskyTwo": "equations(periods) and Proposition(mum), source lines501–548, including the explicit p3 orders",
    "ViaclovskyCombs": "local model lines787–861, periodextension construction lines884–1015, Proposition(hexfill) and its period/generator construction lines1515–1603",
    "LiuRollenske": "open construction lines319–406 and compactification Proposition/proof lines412–449",
    "PaperI": "common conventions; wb:pshift:eq:cusp-periods lines8542–8548; cusp chart matrix PD9 lines8386–8395; higher-multiplicity marking and root replacements lines9045–9068 and9188–9219"
  },
  "no_target_proof_read": true,
  "events_added": 0
}

The primary comb Questions item1, source lines2693–2699, was read before freezing. The last sentence asks retention of a torus fibration. Only that part is answered here; its preceding questions asking exact h1 and Kuranishi dimension receive no new claim.
