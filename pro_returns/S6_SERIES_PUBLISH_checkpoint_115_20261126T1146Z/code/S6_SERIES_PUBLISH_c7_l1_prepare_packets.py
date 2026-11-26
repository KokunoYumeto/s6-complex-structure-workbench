#!/usr/bin/env python3
"""Prepare the L1 comparison proposal; no canonical or global writes.

Only the individually released theorem/proof are inspected in the canonical
source. All outputs are in the owning agent folder. No historical topology
program is imported or executed.
"""
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_nonstar"
BASE="S6_SERIES_PUBLISH_III_02L1_"
ID="maps:src:D.2.26"
TAG="02L1"
canonical=ROOT/"S6_SERIES_PUBLISH_III.tex"
canonical_bytes=canonical.read_bytes()
canonical_hash=sha256(canonical_bytes).hexdigest()
assert canonical_hash=="9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
source=canonical_bytes.decode()
release_time="2026-11-24T22:51:21.424447+00:00"

frozen={
 "fresh_derivation.md":"172c439477e26f58c07171b635786f488f7084707bb00b1c1d9f92827a09da2a",
 "fresh_graph_maps.md":"ce12561fabebef5ed591a0754ba8dbb42580271b2d856d233bfe77320fc39e44",
 "fresh_cap_rank.md":"0d6f6250135b4f923e91a46cc569d5f2104a1b279c31a36917dbdc8354981912",
 "fresh_catalogue.json":"e7815e81b19c8c18d29192565ef1528ba37629271093df00c1ca0ad15831aa14",
 "fresh_sphere_patterns.csv":"01750de85b3f4f0113da8a01f3ec2210458b1e97e653156c11ba915deb1c9b4a",
 "fresh_inverse_checks.json":"705add94aee847cfe6fe1198303cbdc2bf914f7bfe880ed2132388a9b5ea6a4e",
}
for suffix,digest in frozen.items():
    assert sha256((LANE/(BASE+suffix)).read_bytes()).hexdigest()==digest,suffix
print("PASS six frozen L1 proof/data files unchanged.")

def read_released(kind,env):
    text=(LANE/(BASE+"released_"+kind+".tex")).read_text()
    lines=text.splitlines()
    assert len(lines)>5 and all(x.startswith("%") for x in lines[:5])
    result="\n".join(lines[5:]).rstrip("\n")
    assert result.startswith("\\begin{"+env+"}") and result.endswith("\\end{"+env+"}")
    assert source.count(result)==1
    start=source.index(result)
    span=(source[:start].count("\n")+1,source[:start].count("\n")+1+result.count("\n"))
    return result,span

old_statement,statement_span=read_released("statement","theorem")
old_proof,proof_span=read_released("proof","proof")
assert statement_span==(12740,12835)
assert proof_span==(12838,13019)
assert sha256(old_proof.encode()).hexdigest()=="30420dc0844488d3d5200d2e20cb45f9533a3cac47f29c306f9ad94a739b1be7"
receiver_path=LANE/(BASE+"receiving.tex")
new=receiver_path.read_text().rstrip("\n")
assert new.count(r"\begin{proof}")==new.count(r"\end{proof}")==1
new_statement,new_proof=new.split(r"\begin{proof}",1)
new_statement=new_statement.rstrip("\n")
new_proof=r"\begin{proof}"+new_proof
assert new_statement.startswith(r"\begin{theorem}") and new_statement.endswith(r"\end{theorem}")
assert new_proof.endswith(r"\end{proof}")

def identities(text):
    return tuple(sorted(re.findall(pattern,text)) for pattern in (
        r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\tag\{([^}]+)\}"))
assert identities(old_statement)==identities(new_statement)
assert identities(old_proof)==identities(new_proof)
assert len(identities(new)[0])==8
print("PASS separate exact source guards:",statement_span,proof_span)
print("PASS separate theorem/proof permanent identities unchanged.")

def write_tsv(name,fields,rows):
    buf=io.StringIO(newline="")
    w=csv.DictWriter(buf,fields,delimiter="\t",lineterminator="\n")
    w.writeheader();w.writerows(rows)
    (LANE/(BASE+name+".tsv")).write_text(buf.getvalue(),newline="\n")

replacement_rows=[]
for kind,before,after,span in (
    ("statement",old_statement,new_statement,statement_span),
    ("proof",old_proof,new_proof,proof_span)):
    replacement_rows.append(dict(
        statement_id=ID,old_text=before,new_text=after,
        reason=(
          f"Separate exact {kind} guard, canonical lines {span[0]}--{span[1]}, "
          f"individually released {release_time}. Complete fresh derivation was frozen "
          "and fully reviewed before release; entire original and every auxiliary assertion "
          "have now been compared. All theorem conclusions and parameter scopes stand. "
          "Repair the false physical-delta fan/semifree intermediate assertion by the "
          "explicit finite Farey word, Thom induction and oriented relative-ball maps. "
          "The post-exposure scope clarification gives a global diffeomorphism fixing "
          "the chosen ball's outer boundary; the filling construction uses unchanged "
          "other cap data, while the diffeomorphism need not fix those caps. "
          "Give all cap/graph/affine/CRT inverses, all homology, complete new 59-row table "
          "and exact oriented framed reconstruction. The original 68 count is the all-172 "
          "scope and includes the theorem's 62 primitive positions. No count D26 or smooth D27. "
          "The exact historical CSV is absent; no bytewise-table or historical-execution claim. "
          "All permanent labels, equation tags and hypertargets preserved. Root admission, "
          "canonical application, unit/build/page work remain separate.")))
write_tsv("replacements",["statement_id","old_text","new_text","reason"],replacement_rows)
trial=source
for row in replacement_rows:
    assert trial.count(row["old_text"])==1
    trial=trial.replace(row["old_text"],row["new_text"],1)
assert canonical.read_bytes()==canonical_bytes
print("PASS two in-memory replacements apply once; canonical bytes unchanged.")

def between(text,start,end):
    i=text.index(start);j=text.index(end,i+len(start))
    return text[i:j].rstrip("\n")

headings=[
 r"\emph{Natural rows and necessary cap choices.}",
 r"\emph{The period bundle and integral graph.}",
 r"\emph{Integral maps for the reduced caps.}",
 r"\emph{Finite affine lifts and their full kernel.}",
 r"\emph{Regular logs and Mayer--Vietoris.}",
 r"\emph{Integral reduction for the simply connected members.}",
 r"\emph{The complete list and its parameters.}",
 r"\emph{Transporting the cusp fan when $c=1$.}",
 r"\emph{The circle quotient and oriented reconstruction.}",
 r"\end{proof}",
]
sections=[between(new,a,b) for a,b in zip(headings,headings[1:])]
items=old_proof.split(r"\item ")[1:]
assert len(items)==11
items[-1]=items[-1].split(r"\end{enumerate}")[0]
items=[x.rstrip("\n") for x in items]

defects=[]
def defect(suffix,kind,before,after,reason):
    assert before
    candidates=[(old_statement,statement_span),(old_proof,proof_span)]
    candidates=[(part,span) for part,span in candidates if before in part]
    assert len(candidates)==1,(suffix,"old quote ambiguous or absent")
    part,span=candidates[0]
    assert part.count(before)==1,(suffix,"old quote repeated")
    assert not after or after in new,(suffix,"new quote absent")
    old_line=span[0]+part[:part.index(before)].count("\n")
    new_line=1+new[:new.index(after)].count("\n") if after else ""
    defects.append(dict(
        change_id="c7-III-02L1-"+suffix,type=kind,statement_id=ID,
        old_location=f"S6_SERIES_PUBLISH_III.tex:{old_line}",old_page="",
        new_location=str(receiver_path.relative_to(ROOT))+(f":{new_line}" if new_line else ""),
        new_page="",old_text=before,new_text=after,reason=reason,
        review_status="complete checker comparison; proposed for root review and admission; canonical/unit/build/page work pending"))

defect("header","D10",next(x for x in old_statement.splitlines() if x.startswith(r"\StatementRecord")),
       r"\textup{\small(tag 02L1)}",
       "Replace the machine record by the small permanent printed tag; mathematical references occur at their applications.")
defect("title","D23",old_statement.splitlines()[0],new_statement.splitlines()[0],
       "Use a short capitalized mathematical title while preserving the theorem label, hypertarget and full sixteen-profile scope.")
defect("external-table","D09",
       "They lie on $50$ distinct initial rows. The complete table,\nincluding the section pair, zero component, marked fibre positions,\nand every additive original/log choice, is\n"+r"\path{records/manifolds_nonstar_sphere_patterns.csv}.",
       between(new,"The following table lists them.","There are $50$ distinct"),
       "The exact historical CSV is absent from the attached tree and named indexes, as checked by root. Print the complete independently derived 59-row table with all marked choices. No bytewise comparison with the missing file is claimed.")
defect("defensive-parameters","D02",
       "These are parameter families, not multiplicity samples. The exact\nunrestricted parameter conditions for every row follow below.",
       "For one finite log every positive multiple of its monodromy order\noccurs.",
       "State the all-order parameter conclusion directly and prove it by explicit numerator constructions, with no multiplicity cutoff.")
defect("generator-notation","D20",
       "Here is their full integral degree-two presentation. For each finite\nlog retain a generator $d_i$; for each regular log retain its four\nsweeps $t_j("+r"\Lambda"+")$; retain the fibre generator $s$. Impose",
       "Define $C$ by a generator $s$, one generator $D_i$ at each finite\nlog and a homomorphism $t_j:"+r"\Lambda"+"\\to C$ at each regular log,\nwith relations",
       "Use D_i for the delta-sweep and d_i for the monodromy order. The old finite generator d_i maps identically to D_i; the inverse restores the old symbol. The relations are unchanged.")
defect("finite-scope","D11",
       "Thus this is also an all-order integral algorithm\nfor the nonsimply-connected members satisfying the stated finite\ncoprimality condition. No conclusion for the omitted noncoprime\nfinite twists is silently inferred.",
       "These formulas apply to every member with the stated finite\ncoprimality, including those with nontrivial fundamental group.",
       "State the positive finite scope once. The excluded noncoprime range is not added, and no new D26 endpoint is found.")
defect("smooth-scope","D11",
       "For $c>1$ the groups "+r"\eqref{maps:eq:D.HY4}"+"\nare exact, but a general smooth identification of these remaining\ntorsion types is not asserted by this theorem.",
       "For every simply connected member with $c=1$, the oriented smooth\ntype is",
       "Give the full simply connected group formula and the c=1 smooth assertion at their positive scopes; remove the repeated negative closing clause.")
defect("enumeration","D10",
       r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]","",
       "Replace the generated numbered hierarchy by a connected proof with mathematical subheadings; all eleven original items are individually compared.")

repairs=[
 ("original-obstruction",0,0,
  "Give the fixed-lattice component index and actual original-cap rank obstruction, including the global free bridge which excludes nonzero-Chern III and I2 even when their local defect is zero."),
 ("graph-inverse",1,1,
  "Give the complete based Fox injections, primitive fixed bases, Smith inverse, fibre detector with section, swept global delta chain and induction for arbitrarily many regular sites. Post-exposure exact arithmetic checks the exposed all 172 auxiliary scope."),
 ("original-integral-map",2,2,
  "Use the four-dimensional neighbourhood N and its actual roof/line/logarithm maps; the central core computes homology by its inclusion. Give the integral component specialization, explicit Bezout section, complete local wedge quotient and both bounding sweeps, including III/IV saturation."),
 ("finite-vertical",3,3,
  "Derive the full fixed and vertical lattices, inverse quotient row, norm and signed pairing. State both exact scopes 62/94 nonstar and 68/102 all, with their six-position primitive inclusion. The original 68 count is correct in its all-172 context."),
 ("affine-averaging",4,3,
  "Construct the holomorphic finite averaging translation and its inverse on the whole root disc, including varying affine terms; identify the integral power class by the cyclic resolution and use the full norm law for finite lift changes."),
 ("finite-thom-and-groups",5,4,
  "Give the actual central Bezout basis and inverse, normal-line trivialization, full Thom transfers, coefficient-one elimination for every r, all regular root relations, the exact Mayer--Vietoris quotient and free extension, and complete integral duality maps."),
 ("all-primary-inverse",6,5,
  "Prove the finite and regular CRT reductions by explicit integer inverse substitutions, preserve every extra root row and handle empty sets/order-one sites. The unimodular two-row elimination proves cs=0 at all primes simultaneously."),
 ("smith-factors",7,5,
  "Give the exact three-generator matrix and its determinantal divisors g,Rg,cR^2, together with the inverse elimination of the contracting sweep and the full weighted X,Y coordinates."),
 ("complete-patterns",8,6,
  "Give the exhaustive selection rule, the two explicit unavoidable base-order obstructions, all 164/162/59 counts, complete 59-row table and unbounded numerator constructions. No absent historical table or unverified program execution supplies evidence."),
 ("other-stabilizers",9,8,
  "Prove freeness on every original, primitive rank-one, regular and finite cap using its literal period and contracting coordinate. Use the physical-edge representative only after the separate complete fan transport."),
 ("framed-smooth-map",10,8,
  "Give the integral quotient homology inverse, even-R spin calculation, fixed-sphere nullhomotopy and framed Hopf maps. Construct the unstabilized oriented twisted-suspension map and inverse; also prove the surgery/projectable-spin auxiliary and integral ring/p1 data."),
]
for suffix,item,section,reason in repairs:
    # The finite-kernel row spans the finite and regular sections.
    replacement=sections[section]
    if suffix=="finite-thom-and-groups":
        replacement=between(new,"Write $v=n"+r"\ell"+"+r"+r"\delta"+"$ and choose",headings[5])
    defect(suffix,"D22",items[item],replacement,reason)

defect("cusp-circle","D25",
       "At the zero its lattice is the full original\nshort lattice, retaining $"+r"\delta"+"$ as the second coordinate, so its\nsingle fixed sphere and normal weights are those of "+r"\ref{maps:src:D.2.14}.",
       sections[7],
       "False intermediate assertion. In the stated sphere pattern OS49/default, a=1, b=3, selected I2, the specified short matrix is C=[[2,3],[-1,-1]], C^{-1}delta=(-3,2); the chart (q/(XY),Y,X) has weights (1,2,-3), an isolated fixed point and stabilizers of orders 2 and 3. The theorem remains true: prove s=0, carry the actual fan and units through a finite Euclidean/Farey word, preserve integral specialization by the codimension-four Thom isomorphisms, and use the explicit relative-ball diffeomorphisms. This is D25; the smooth conclusion is not refuted and no D27 is added.")
defect("historical-fixed-program","D09",
       "These are exact fixed-lattice\ncalculations, included for all $172$ initial rows in\n"+r"\texttt{manifolds\_sphere\_normal\_lattices.py}.","",
       "Remove the historical program path and execution attribution from the proof. The new raw-derived computation checks every stated lattice assertion; historical executions are not verified.")
defect("historical-graph-program","D09",
       "That program also computes the complete boundary fixed-sweep map",
       "With $N$ singular places let",
       "State the actual graph matrix and exact quotient result; the explicit inverse and new finite computation support the claim.")
defect("saved-bases","D08",
       "The table "+r"\eqref{maps:eq:D.HY2}"+" follows either from the component group or the\nsaved primitive Smith bases. The code verifies all $68$ such slots.",
       "The finite matrix has exact order $d$ as in\n"+r"\eqref{maps:eq:D.HY2}"+". Its average projects $"+r"\beta"+"$\nto $"+r"\delta"+"/q$, while fixing $"+r"\ell"+"$.",
       "Replace saved-code wording by the invariant row and exact norm proof; both 62/68 scopes are stated explicitly with the inclusion.")
defect("saved-enumeration","D09",
       "Their complete data are saved in the CSV and JSON tables.",
       "The following table lists them.",
       "Print the complete mathematical enumeration in the proof. The unavailable historical table and any unexamined JSON output are not treated as evidence.")
defect("defensive-original","D02",
       "rather than merely a rational homology\ncomparison.","",
       "Remove the defensive clause; the receiver supplies the neighbourhood diffeomorphism, fibre maps and integral right inverses directly.")
defect("defensive-kernel","D02",
       "not a sublattice of finite index.","",
       "Remove the defensive clause; the displayed central basis and full Thom sequence prove the exact integral kernel.")
defect("cancellation-invocation","D18",
       "The fixed sphere is nullhomotopic, and the equivariant surgery,\nprojectable spin quotient, Smale--Barden classification, twisted\nsuspension formula and full Zhubr cancellation from "+r"\ref{maps:src:D.2.14}"+" apply\nwith $H_2=("+r"\mathbb Z"+"/R)^2$. They give precisely\n$X"+r"\cong\widetilde\Sigma_0N_R"+"$.",
       sections[8],
       "The generic complete-cancellation invocation has no stated primary theorem or invariant comparison. Give the direct unstabilized oriented framed reconstruction with its inverse, precise Barden applications and all auxiliary surgery/spin/product data. No assertion that no cancellation theorem can apply is made.")
defect("poincare-accent","D23","Poincare--Lefschetz duality",
       r"Poincar\'e--Lefschetz duality",
       "Restore the accent in the duality name; its mathematical application is separately proved by the complete cap maps.")
defect("neron-accent","D23","Neron logarithm",
       r"N\'eron logarithm",
       "Restore the accent in the local logarithm's name; the actual section and line maps remain as derived.")
defect("bezout-accent","D23","Bezout numerators",
       "B\\'ezout\nnumerators",
       "Restore the accent in the numerator construction and use the same spelling throughout the receiving proof.")

write_tsv("defects",
          ["change_id","type","statement_id","old_location","old_page","new_location","new_page","old_text","new_text","reason","review_status"],
          defects)
print("PASS",len(defects),"defect rows have exact old and receiving quotations.")
print("DEFECT TYPES",dict(sorted(__import__("collections").Counter(d["type"] for d in defects).items())))
print("PASS sole mathematical refutation is the D25 intermediate cusp-circle assertion; no D26/D27 added.")

now=datetime.now(timezone.utc)
event_id="publish:c7:III:02L1:check-sequence"
where=[
 LANE/(BASE+"fresh_derivation.md"),LANE/(BASE+"fresh_graph_maps.md"),
 LANE/(BASE+"fresh_cap_rank.md"),LANE/(BASE+"fresh_catalogue.json"),
 LANE/(BASE+"fresh_sphere_patterns.csv"),LANE/(BASE+"fresh_inverse_checks.json"),
 ROOT/"agents/continuation7_iii_root"/(BASE+"fresh_root_review.md"),
 LANE/(BASE+"released_statement.tex"),LANE/(BASE+"released_proof.tex"),
 LANE/(BASE+"post_exposure_derivation.md"),LANE/(BASE+"comparison.md"),
 receiver_path,LANE/(BASE+"replacements.tsv"),LANE/(BASE+"defects.tsv"),
]
for code in ("catalogue","inverse_checks","post_exposure","receiver_check"):
    where.extend(ROOT/"code"/f"S6_SERIES_PUBLISH_c7_l1_{code}.{suffix}" for suffix in ("py","out"))
assert all(p.exists() for p in where)
event=dict(
 statement_id=ID,date=now.date().isoformat(),
 who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed",
 type="targeted proof check",
 outcome=(
 "Complete pre-exposure fresh derivation frozen 2026-11-24T22:48:18Z and fully read by root "
 "before individual original release 2026-11-24T22:51:21.424447Z. Whole released theorem "
 "and all 11 proof items, every auxiliary lattice/cap/affine/primary/count/smooth assertion "
 "and historical execution claim compared. All stated conclusions stand for the sixteen "
 "profiles, 148 initial rows, 164 minimal patterns, 59 sphere patterns on 50 rows; exact finite "
 "coprimality and unrestricted regular parameters preserved. New all 172 graph/fibre and "
 "all 102 finite-position calculation confirms the exposed auxiliaries; 62 nonstar primitive "
 "positions embed in 68 all-catalogue positions, so no count D26. D25 false physical-delta "
 "semifree assertion refuted by the OS49 I2 chart weights (1,2,-3) and repaired by actual "
 "Farey flips, Thom transport and relative-ball maps. Full integral inverse maps, all-order "
 "CRT/root rows, complete homology, even-R spin, p1/ring and oriented unstabilized "
 "reconstruction proved. Missing historical CSV recorded; new full 59-row table printed; "
 "Post-exposure clarification corrects the fresh support sentence: the flop comparison "
 "is a global oriented diffeomorphism with its own outer-ball map; the physical-fan "
 "construction uses unchanged other cap data, without a pointwise preservation claim. "
 "no bytewise historical-table or historical-program execution claim. Complete receiver "
 "and separate exact theorem/proof guards prepared; root final admission review pending. "
 "Syntax checks only; no canonical application, unit closure, TeX/PDF/build or page credit."),
 event_id=event_id,phase="complete fresh derivation before individual release; full post-exposure comparison",
 source_file="S6_SERIES_PUBLISH_III.tex",source_row="12740",
 source_event_type="targeted proof check",evidence_group=event_id,
 publish_input_file=str((LANE/(BASE+"comparison.md")).relative_to(ROOT)),
 publish_input_row="1",date_utc=now.isoformat(),
 where="; ".join(str(p.relative_to(ROOT)) for p in where))
event_fields=["statement_id","date","who","type","outcome","event_id","phase","source_file","source_row",
              "source_event_type","evidence_group","publish_input_file","publish_input_row","date_utc","where"]
fresh_event=dict(event)
fresh_event.update(
 type="targeted proof check",source_event_type="targeted proof check",
 event_id="publish:c7:III:02L1:fresh-complete-derivation",
 phase="before whole original L1 exposure",
 outcome=(
  "Before individual original release, derived the full sixteen-profile theorem from "
  "the statement-only packet and permitted constructions. Frozen at "
  "2026-11-24T22:48:18Z and fully read by root before release at "
  "2026-11-24T22:51:21.424447Z. Derived all 172 natural rows and the 148-row nonstar "
  "restriction, primitive graph/fibre quotient on those148 rows, exact original-cap "
  "integral maps, every permitted finite/regular Thom relation, all-order Mayer--Vietoris "
  "groups, complete Seifert tests, finite/regular CRT inverses including root rows, "
  "cs=0 and all59 sphere patterns on50 initial rows. Constructed actual fan flips, "
  "Thom transport, global oriented reconstruction, even-R spin and linking maps. "
  "Complete fresh programs and outputs were read by checker and root. A stronger "
  "support sentence in the fresh fan argument is narrowed in the separately recorded "
  "post-exposure comparison; this event credits the actual relative-ball/global maps "
  "and does not claim pointwise preservation of every other cap. One fresh derivation; "
  "no post-exposure or historical-execution work receives independent-blind credit."),
 where="; ".join(str(p.relative_to(ROOT)) for p in where if
                 "fresh_" in p.name or p.name in {
                  "S6_SERIES_PUBLISH_c7_l1_catalogue.py","S6_SERIES_PUBLISH_c7_l1_catalogue.out",
                  "S6_SERIES_PUBLISH_c7_l1_inverse_checks.py","S6_SERIES_PUBLISH_c7_l1_inverse_checks.out"}))
refuted_event=dict(event)
refuted_event.update(
 type="refuted, with the refined statement's id",
 source_event_type="refuted, with the refined statement's id",
 event_id="publish:c7:III:02L1:physical-fan-assertion-corrected",
 phase="after whole original L1 exposure",
 outcome=(
  "Refined identity remains maps:src:D.2.26. Refuted precisely the original proof's "
  "assertion that the physical delta circle is the second short coordinate of the "
  "specified cusp fan and hence has the semifree fixed sphere of02KO. In the allowed "
  "OS49/default sphere pattern (a,b)=(1,3), selected I2, C=[[2,3],[-1,-1]] and "
  "C^{-1}delta=(-3,2); the chart(q/(XY),Y,X) has weights(1,2,-3), an isolated fixed "
  "point and stabilizers of orders2 and3. The exact inverse period map and chart "
  "characters prove this D25 counterexample. The complete actual fan change, Thom "
  "induction and global oriented ball comparison repair the inference. All theorem "
  "conclusions remain proved, with no count D26 or smooth D27 and no refutation of "
  "a general cancellation theorem."),
 source_row="13006",
 where="; ".join(str(p.relative_to(ROOT)) for p in (
        LANE/(BASE+"released_proof.tex"),LANE/(BASE+"post_exposure_derivation.md"),
        LANE/(BASE+"comparison.md"),receiver_path,LANE/(BASE+"defects.tsv"))))
rechecked_event=dict(event)
rechecked_event.update(
 type="used and rechecked in this run",source_event_type="used and rechecked in this run",
 event_id="publish:c7:III:02L1:whole-original-comparison",
 phase="after whole original L1 exposure",
 outcome=(
  "After individual release at2026-11-24T22:51:21.424447Z, read the entire original "
  "theorem and all11 proof items, every labelled formula, historical computation "
  "assertion, original-cap and affine auxiliary, primary Smith calculation and smooth "
  "paragraph. Compared every clause with the frozen derivation and complete receiver. "
  "New post-exposure arithmetic checks the full172 graph/fibre scope and all102 finite "
  "positions; the correct all-catalogue68 includes the nonstar62, so no count D26. "
  "The whole-disc holomorphic averaging map, normal-kernel inverse, complete primary "
  "comparison and surgery/projectable-spin/ring/p1 auxiliaries are supplied. The "
  "cited full-invariant cancellation was unproved at the invoked02KO scope; direct "
  "unstabilized oriented reconstruction repairs that gap, without a general "
  "cancellation-theorem refutation. Root identified an overstrong fresh auxiliary "
  "support sentence: the nullhomotopy can use other caps, so each flop map fixes its "
  "own outer-ball boundary and their composition is global. The receiving proof "
  "and post-exposure note now state that exact scope; the physical-fan construction "
  "keeps the same other cap data, and the common-complement Thom maps preserve fibre "
  "specialization. Frozen bytes remain unchanged. The exact historical CSV is absent, "
  "with no bytewise-table or old-program execution claim; all59 new rows are printed. "
  "Separate exact theorem/proof guards,30 correction rows and all permanent labels "
  "are checked. Syntax checking gives no TeX/PDF/build, unit or page credit. Root "
  "admission and canonical application remain pending. This row adds no independent-blind credit."))
for row in (fresh_event,refuted_event,rechecked_event):
    row["outcome"]=row["outcome"].replace("those148","those 148").replace("all59","all 59").replace("on50","on 50")
    row["outcome"]=row["outcome"].replace("of02KO","of 02KO").replace("chart(q","chart (q").replace("weights(1","weights (1")
    row["outcome"]=row["outcome"].replace("orders2 and3","orders 2 and 3").replace("at2026","at 2026").replace("all11","all 11")
    row["outcome"]=row["outcome"].replace("full172","full 172").replace("all102","all 102").replace("catalogue68","catalogue 68")
    row["outcome"]=row["outcome"].replace("nonstar62","nonstar 62").replace("invoked02KO","invoked 02KO").replace("guards,30","guards, 30")
write_tsv("CHECK_EVENTS",event_fields,[fresh_event,refuted_event,rechecked_event])
print("PASS three event proposals: targeted fresh derivation, exact D25 refutation, and used/rechecked whole comparison.")
print("PASS one shared evidence group; one pre-exposure derivation, no extra independent-blind credit.")
for suffix in ("receiving.tex","comparison.md","post_exposure_derivation.md",
               "replacements.tsv","defects.tsv","CHECK_EVENTS.tsv"):
    path=LANE/(BASE+suffix)
    raw=path.read_bytes()
    assert all(x>=32 or x in (9,10) for x in raw),suffix
    assert raw.endswith(b"\n"),suffix
    print("PACKET",path.name,"SHA256",sha256(raw).hexdigest())
assert canonical.read_bytes()==canonical_bytes
print("PASS only owning-lane proposal files written; canonical source and global tables untouched.")
