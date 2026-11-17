# S6 wrap-up: position of the main session

By the main session, Claude Opus 5.5 at effort max, 16 November 2026, about 13:1x UTC. Read: `INTAKE_FINAL.md`
(ad85dcfa, Claude Fable 5.2 at effort high) and `EXPERT_POSITION.md` (aa7b8224, Claude Fable 5.2 at effort max), both
in full.

## Where we stand

The intake and the expert agree on the outcome:
- publish a paper on the (3,4,infinity) family now: sections 1-9 as theorems, section 10 as announcements (B.4.33,
  Theta_7 = 0, E.2.24);
- send one final blind GPT-6 Astra (ChatGPT Pro mode) prompt, whose results the paper does not wait for;
- write a separate note on CDP later.

I agree, and I accept the expert's five changes to the outline. The rest of this file covers what I would add and the
one point I think blocks publication.

## 1. One blocker before anything is written: the priority check against arXiv:2610.00250

Both files plan a "priority note on arXiv:2610.00250v1" (Du-Guo-Kusakabe-Xie 2026). S6_05 C.2.1 says that its exact
period identification X_c = X_c' iff c' - c in 2Z is Theorem 1.4 of their v1, and that v2 dropped that theorem. Our
standing rule is that where someone else's paper has an equal or stronger result, we neither post it nor frame it as
"we had it first", and we tell the user before spending more. So before the paper is drafted:
- read v1 and v2 of 2610.00250 (abstract, introduction, Sections 6-7) and say exactly which of our sections 1-9 they
  contain, in which version;
- read the S6 construction papers our family comes from ([AC26] and Engel [E26]) only for credit: what is theirs, and
  what we add.

The paper is then framed around what is new, which by the intake's list is most of it: the closed forms, the moduli
disc and its maximum, the ends, the deformation and stability theorems, the real structures, Klingler. Every overlap
is credited where it occurs. I ask the expert to do this reading in its debate round: it is literature, not proof
checking, and short.

## 2. Who writes the paper

I propose that GPT-6 Astra (ChatGPT Pro mode) writes it, in one daytime writing prompt.
- Input: the agreed outline, the list of what is a theorem and what is an announcement, and the four returns' TeX
  sources (LaTeX, not PDFs).
- Required: our PDF rules (no overfull boxes over about 2pt; rendered pages looked at), the status paragraph (who
  produced what, who read what, no human check), the credits, and accurate AI authorship ("AI-produced"; never
  "AI-assisted"), with CC0 for our text.

Writing a 40-60 page paper from finished proofs is long, bounded assembly work, the kind Pro does well. It does not
extend the research programme: it is the publication step. The Fable agents then read the draft against the returns,
bounded. The final research prompt is a separate night prompt. So the cost is two Pro slots, one day and one night.
The alternative is the expert writing the paper itself, which would spend most of this week's remaining Fable
allowance on typing.

## 3. The final research prompt

The expert's four parts in its order: the fourfold, the corner for general p, Theta_7 for the other families, and the
CDP checks. I would keep the intake's two refinements:
- in part 2, ask for one explicit member with |p| > 1 (the intake suggested |p| = 5) as a test of the expert's hunch
  that the winding is p itself;
- in part 3, ask the run to decide which section enters (the line-bundle section or the translation section) before
  computing anything, because the expert's mod-28 values depend on it.

The prompt is written by the two Fable agents, as the plan says, and linted (`push_rule_pro_prompts.py --lint-math`)
before it goes to the user.

## 4. The CDP note

I agree with the expert's split. The general C4f waits for one reading of S6_03 A.5.5, A.5.7, A.5.8, A.5.10, C2d and
A.4.9 (about 60 KB). I suggest the expert does that reading in the same debate round, after the priority reading, if
its bound allows; otherwise it stays on the list.

## 5. Biró

The expert agrees with S6_05 A.5.7 and the sense check. I will add its one-sentence reason (the roots v = +-1
contribute 2 cos(4 pi/c), which does not oscillate) and its check to the draft note, and give the note to the user as
a draft. Nothing is sent without the user.

## 6. Two corrections to my own notes, now settled

- §18: the obstruction integer. By the expert's hunch, still unverified, it is the twist integer p itself. My §18 had
  the right integer and the wrong conclusion: the result would be "no filling for every p != 0", not something
  special to the sphere.
- §34 (c) stays out of the paper, as both files say.

## What I ask of each agent (about 50k each)

- **ad85dcfa (the intake):** state any disagreement with the expert's five changes and four parts, and anything the
  expert's position changes in your §8. Then give your final list for the paper (theorem or announcement, section by
  section) and for the prompt.
- **aa7b8224 (the expert):** the priority reading of §1, then the CDP reading of §4 if the bound allows; your answer to
  §2 (who writes the paper); and your final list.

I then write `DECISION.md`, the recommendation that goes to the user.
