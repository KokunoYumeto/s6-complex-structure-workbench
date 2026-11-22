# Prerelease independent derivation

Checker: i_provenance_recovery. Written 2026-11-21T21:24:19.177179+00:00. Both IK and DU own printed proofs remain closed. Prior exposures are disclosed: Paper I, the safe statement packets, the now independently frozen/released named torsion lemma03IF, and the unnumbered W.4/W.5 coordinate proofs displayed by the broader03IF release. The I9 ancillary proof’s final invocation of IK’s stated section was also seen post-I9-freeze; it did not expose IK’s own proof. The W.4/W.5 exact statements and source-bound nonproof global setup are declared inputs. This derivation proves the target conclusions anew from those inputs.

## Exact notation transport

The existing nonproof definitions give T=ker(Omega_S->j_*Omega_{S_reg}), Q=Omega_S/T and the explicit existing equality Q=tildeOmega_S. The proved03IF input identifies T with Tor(Omega_S). The map from Q to j_*Omega_{S_reg} is [omega]->omega|reg. Its kernel is zero by that exact kernel definition, and its image is the image of restriction; its inverse on that image takes a local restricted differential to the class of any local lift, independent of the lift because differences lie in T. This constructs the quotient/image identification, without imposing a new meaning on tildeOmega. The map Omega_S->tildeOmega is the quotient map omega->[omega].

Owner: wbII:cor:normal-crossing-kernel, tag03DU.

Use the supplied conductor-section theorem statement as a prior input and its exact construction just independently written for03IK, still before either target proof is released. It supplies nonzero s in H0(V tensor A) whose image in Q tensor A=tildeOmega tensor A is zero. Thus s lies in H0(K tensor A) by the actual kernel map K=ker(V->Q). In the exact sequence0->N* tensor A->K tensor A->T tensor A->0, let v be the image of s. The assumed H0(N* tensor A)=0 makes the map H0(K tensor A)->H0(T tensor A) injective, so v is nonzero. Since v has the global lift s, its connecting class delta_A(v) is zero: in a Čech construction one takes that same global lift on every open set, and every pairwise difference is zero. Consequently delta_A has the nonzero kernel element v.

The second assumed vanishing H0(Q tensor A)=0 makes H0(V tensor A)=H0(K tensor A) by the other exact sequence. Combining the two exact maps identifies H0(V tensor A) with ker delta_A exactly as stated in input A.1.1, through s->rho(s)=v. This is the section-kernel map in the target. The local names scriptK and scriptT correspond by these same kernel/quotient maps, not an assumed equality of unrelated objects. The statement and all its hypotheses are proved, with no numerical computation invoked.

## Bound inputs

[
  {
    "path": "agents/ii_infra/statement_packets_v2/S6_SERIES_PUBLISH_II_03DU_statement_inputs.tex",
    "sha256": "ab6e396a420d8357aac59677b71209249d0f053722df5a93852244a7b073d0a9"
  },
  {
    "path": "agents/ii_infra/statement_supplements_v1/S6_SERIES_PUBLISH_II_03DU_cited_input_supplement.tex",
    "sha256": "57e31e36eeafdeb103e019e84f8e59956a78358bd476163a53ea99608d673443"
  },
  {
    "path": "agents/ii_infra/recovery_20261121/S6_SERIES_PUBLISH_II_03IK_03DU_setup_inputs.tex",
    "sha256": "2e9029fb1adf51dfd0ebb87048afb0db065d75dad065314e9155d1d3c89d5387"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/S6_SERIES_PUBLISH_II_IK_DU_existing_notation_inputs.json",
    "sha256": "b1d05935395d5ae5eeebd159b9f2eb536be6efa82e8ea7fd48dbe9694bc8ccf5"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_03IF_freeze_pointer.json",
    "sha256": "14e3dc7ac32666602d7d27b3e4a0f87ec0e44eab578307899daf5636f282efcf"
  },
  {
    "path": "agents/ii_checks_provenance/recovery_20261121T2000Z/clean_derivations/S6_SERIES_PUBLISH_II_03IF_release_pointer.json",
    "sha256": "7857e12464a4c84168433ac79848d930f442d25f01a4bbe616a3a51a749f7fd8"
  }
]
