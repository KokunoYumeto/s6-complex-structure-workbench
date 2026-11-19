# S6 wrap-up: decision of the debate, for the user (16 Nov 2026, ~13:3x UTC)

Written by the main session (Claude Opus 5.5 at effort max) from:
- `INTAKE_FINAL.md` and `RESPONSE_INTAKE.md`: ad85dcfa, Claude Fable 5.2 at effort high;
- `EXPERT_POSITION.md` and `RESPONSE_EXPERT.md`: aa7b8224, Claude Fable 5.2 at effort max;
- `MAIN_POSITION.md`: the main session.

The three agree on everything below. Where they differed, the stricter reading won.

## 1. Publish a paper now: a period-and-moduli paper, not a classification paper

**Priority.** arXiv:2610.00250 v1 (Du, Guo, Kusakabe and Xie, 23 Sep 2026) already contains, for the standard twist
data, the three results a reader would call the classification:
- X_a = X_a' iff a' - a is in 2Z;
- h^q(T) = (1,1,1,0), with a smooth miniversal Kuranishi line;
- Aut = C*.

v1 also has the fibration f = |-2K| and the moduli as a punctured disc, without the radius. v2 (23 Oct) drops all of
this and keeps only the Oka theorems. Under our rule, these results are stated as theirs, with our proofs in an
appendix, and with no date comparison and no "first" anywhere.

**New, and the substance of the paper** (in neither version):
- the periods in closed form;
- the radius 216;
- all the discrete data;
- the real structures;
- the monodromy group and Klingler's question;
- the special fibres;
- the two ends of the disc.

**Proposed title:** "The (3,4,infinity) family of complex structures on S^6: periods, moduli and the ends of the disc".

**What goes in as what:** the section-by-section table in `RESPONSE_INTAKE.md` decides, with the expert's credit rows
and splits (`RESPONSE_EXPERT.md`).
- **Theorems:** the closed forms and the division formula with N^12 on the torsion locus; the maximum (the interval
  certificates are the proof of record, and the duplication ladder is printed beside them); no extension across
  |w| = 216; Engel's Conjecture 8.2 false as worded, with the corrected form.
- **Announcements** (proofs in the repository): B.4.33 (no filling at w = 0), Theta_7 = 0 (two runs, two methods),
  and E.2.24 (the families as components).
- **Left out:** the CM height table, the fourfold, everything on CDP, the stability theorem beyond first order (it
  moves to the CDP note), and §34 (c) of my notes.

## 2. Who writes it: GPT-6 Astra (ChatGPT Pro mode), in one daytime writing prompt

Then the two Fable agents check the draft against the sources, bounded.

The prompt binds the writer to nine conditions:
1. a binding status table (theorem, known, announcement);
2. one notation;
3. a stated selection of proofs;
4. every printed statement checked word for word against its source;
5. a status paragraph: the same model produced the results and wrote the paper, who read what, and no human check;
6. a binding credit table (Du-Guo-Kusakabe-Xie, [AC26], Engel), section by section;
7. a source row for every statement;
8. no statement that is not in the sources;
9. the reviews' label corrections as input.

Our standing rules also apply: LaTeX sources in the zip (not PDFs), the PDF check (no overfull boxes over about 2pt;
rendered pages looked at), accurate AI authorship ("AI-produced"), and CC0 for our text.

## 3. One final blind research prompt, sent at night

The paper does not wait for it. The run gets statements and data only, no proof text from the earlier runs, and
reports every disagreement with a stated value. Four parts, in order:
1. **The fourfold (S6_04 F.4.1).** Verification first (integral homology with every differential, the rank-three cusp
   filling, the two free quotients, the diffeomorphism type). Then the family in c: the exact range of c,
   classification, and limits at the ends.
2. **The corner for general twists.** From the period matrix and the deck transformations alone: the two origins,
   their comparison F carried through the collar term, and the winding. Test the hunch that the winding is the twist
   integer p on the member p = -5, with the untwisted family as the control.
3. **Theta_7 for every sphere family,** through the height formula (mP).O = m^2 - 1 on the page surface. This is the
   intake's correction; the expert's earlier mod-28 list is withdrawn. Decide whether any family has nonzero class.
4. **The CDP checks:** the gluing and integral Mayer-Vietoris of D.2.7, and C.2.G.1 for irreducible and
   normal-crossings fibres as one self-contained proof.

Not in the prompt: a = 0 (no constructive route).

## 4. Later, and smaller

- **The CDP note.** Ready for normal-crossings and irreducible fibres. The general C4f waits for one reading, which
  needs no Astra run: the proof of S6_03 A.5.5, A.4.7-A.4.8, D.1.8-D.1.9, A.2.4 and the triple-point case of C2d.
  The general stability theorem goes in this note.
- **Biró.** The note is ready for you (`A57_sense_check/NOTE_TO_BIRO_DRAFT.md`).
- **Engel.** Send our note together with the paper (`grant_evidence/OUTREACH_DRAFTS_20261116.md`).

## What the user decides

1. Go for the writing prompt and the night prompt. Both are drafted by the two Fable agents (the expert is at about
   700k of context, the intake at about 830k) and linted before they come to you. Fable this week: about 45 % used.
2. The title.

## The user's answers

- 16 Nov ~13:3x UTC: the title is approved ("Title sounds fine"). The go for the two prompts is still open; the user asked first for the CDP note in more detail and for any stated reason for the v2 cut.
- The v2 cut: no reason is stated. Neither abstract page has a Comments line, and the v2 text gives none (RESPONSE_EXPERT.md). v1 (23 Sep, 138 KB) is "Oka Geometry and Deformations of Torus-Fibred Complex Six-Spheres"; v2 (23 Oct, 42 KB) is "Oka Geometry of Complex Six-Spheres", and its source file is named submited-tams.tex (v1: v5oka_maps_modifications_deformations.tex). So v2 looks like a cut-down journal submission (TAMS). That is an inference, not a stated reason.
- 16 Nov ~13:3x UTC: how independent our derivation was (checked for the user). It was not independent discovery. Our first run, S6_02_FAMILY (GPT-6 Astra, ChatGPT Pro mode, 12 Nov), found 2610.00250 v1 by its own literature search (the prompt did not cite it). It read and audited v1 Section 6 in full (Lemmas 6.1-6.3 through Proposition 6.16) and reported no error. It then wrote its own proofs: A.5.2, with an independent calculation of the root-line cohomology checked by ab_deformation.py, and A.2.1 for the 2Z classification, with a second generic proof through the two Albanese invariants (A.4.1). The paper therefore says that these results are theirs, and that our proofs re-derive and confirm them (Appendix). It does not say "independently found".
- 16 Nov ~13:3x UTC: the user agrees that CDP gets its own note ([the user's words, omitted]). The paper's introduction states Alpöge's counterexample to CDP20 Corollary 2.3 as his (AC26) and points to the CDP note for where the argument fails. This becomes binding condition 10 of the writing prompt.
- 16 Nov ~13:5x UTC: correction to the line above, at the user's prompting to look further back. The 2Z classification WAS obtained independently, in the September workbench: period_shift_classification.tex, with the theorem and its proof, is in the working-edition package downloaded 8 Sep 2026 21:17 UTC; DGKX v1 dates from 23 Sep. (1,1,1,0) and Aut = C* stay "re-derived". The paper says so plainly, with no priority claim and no date comparison, and its appendix prints the workbench's own proof.
- 16 Nov ~14:0x UTC: the S6_01 intake (INTAKE_S6_01.md) adds section 5 of the paper, "The cohomology of X". The Hodge table, Frölicher, Bott-Chern and Aeppli go in as theorems; N^2 = 0 and the (3k,4l) Hodge numbers as announcements. Two refutations of published statements are candidates for plain author notes after the paper: A4.2 (Remark 9.21 of [AC26], the cusp torsion) and E2.4 (the Huckleberry-Kebekus-Peternell bound h0(T) <= 2; it goes with the CDP note).
- 16 Nov ~14:2x UTC: the user confirmed both. Engel's Conjecture 8.2 is filed as a counterexample ("a counterexample is what happens to a conjecture"). The [AC26] PDF stays in the night zip beside our transcription, because the transcription may contain errors. The user: [the user's words, omitted] The S6_01 A1.1-A1.2 reading goes to the Fable check of the draft, and sections 5.1-5.2 stay theorems unless that reading finds a gap. Both prompts are ready in TO_SEND folder 8: the writing prompt by day, the night prompt at bedtime.

## Precedence, for the draft check (main session, 16 Nov ~16:4x UTC)

The user's priority rule (memory priority-heuristic): precedence is recorded for whoever was first, an AI included, and a later human discoverer does not inherit priority. Public dated records of our S6 work exist beside the deleted Zenodo record (removed because the work was made with AI). First, the user's Reddit post: its 29 Aug update states h^{1,1} = 2 and h^{1,2} = 1. Second, the public Overleaf working edition. When the writing return comes back, the draft check asks the user for the Overleaf history date of the 2Z classification file. If that date is before 23 Sep, the paper must not say "first published in DGKX v1". It should say "posted publicly in our working edition on <date>; obtained independently by DGKX (v1, 23 Sep)". The same check applies to the Hodge numbers, with the Reddit post of 29 Aug, after confirming what [AC26] and DGKX state about them.
