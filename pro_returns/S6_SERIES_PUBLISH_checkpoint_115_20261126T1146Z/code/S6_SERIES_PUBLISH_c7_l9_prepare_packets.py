#!/usr/bin/env python3
"""Prepare exact L9 comparison proposals without canonical/global mutations.
Only the individually released target blocks are inspected semantically.
"""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import io
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_multiplicative"
BASE = "S6_SERIES_PUBLISH_III_02L9_"
ID = "maps:src:D.2.33"
canonical = ROOT/"S6_SERIES_PUBLISH_III.tex"
canonical_bytes = canonical.read_bytes()
assert sha256(canonical_bytes).hexdigest() == "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
source = canonical_bytes.decode()
frozen = {
    "fresh_derivation.md":"e5f8cc59e98d20ffe7b845824c369083b7e5246762ba52423aeeca7ea016f920",
    "fresh_data.json":"28654bdc28d985d7ccb8989182e3b42d2ea7b55626f5c3e1b8fffdcd2c183d4a",
    "fresh_patterns.tsv":"fb02752a2ad6eee0bf292a7f658264f29af994a8c14ab167d0a8fdc730c885b6",
}
for suffix,digest in frozen.items():
    assert sha256((LANE/(BASE+suffix)).read_bytes()).hexdigest() == digest
for suffix,digest in (
    ("catalogue.py","c6291e86e2e5815496d94d317e80f37c1e2cde93ffeed715803cd7403148e3a6"),
    ("catalogue.out","079aef4858fd75d40d608f6137d1efa995f59b73333ca37e6a59146b990f73b0"),
    ("mathcheck.py","922f564660f1849c9a43a4330e3943091df85326b4afd1ca0a51aff564480027"),
    ("mathcheck.out","a5286fa00ca04d098ac6a2813f6e5abb6f45b696dfb488b6f8c8690a1266c973"),
):
    assert sha256((ROOT/"code"/("S6_SERIES_PUBLISH_c7_l9_"+suffix)).read_bytes()).hexdigest() == digest
print("PASS all seven frozen fresh proof/data/program/output files unchanged.")

def released(kind,env):
    lines=(LANE/(BASE+"released_"+kind+".tex")).read_text().splitlines()
    assert all(line.startswith("%") for line in lines[:5])
    text="\n".join(lines[5:]).rstrip("\n")
    assert text.startswith("\\begin{"+env+"}") and text.endswith("\\end{"+env+"}")
    assert source.count(text) == 1
    first=source[:source.index(text)].count("\n")+1
    return text,(first,first+text.count("\n"))

old_statement,sspan=released("statement","theorem")
old_proof,pspan=released("proof","proof")
assert pspan == (14496,14691)
assert sha256(old_proof.encode()).hexdigest() == "f1a282786f334f4d47bcc9983a4e5cdb114a090ec1def84fcf25e0bdecc206cc"
new=(LANE/(BASE+"receiving.tex")).read_text().rstrip("\n")
new_statement,new_proof=new.split(r"\begin{proof}",1)
new_statement=new_statement.rstrip("\n")
new_proof=r"\begin{proof}"+new_proof
assert new_statement.endswith(r"\end{theorem}") and new_proof.endswith(r"\end{proof}")

def identities(text):
    return tuple(sorted(re.findall(pattern,text)) for pattern in (
        r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\tag\{([^}]+)\}"))

assert identities(old_statement)==identities(new_statement)
assert identities(old_proof)==identities(new_proof)
print("PASS exact separate guards: statement",sspan,"proof",pspan)
print("PASS all eleven permanent identities and ten equation tags preserved separately by guard.")

def write_tsv(suffix,fields,rows):
    stream=io.StringIO(newline="")
    writer=csv.DictWriter(stream,fields,delimiter="\t",lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    (LANE/(BASE+suffix+".tsv")).write_text(stream.getvalue(),newline="\n")

reason=(
    "Complete fresh proof frozen 2026-11-25T00:16:32Z and fully reviewed before "
    "individual release 2026-11-25T00:20:45.744670Z. Whole original and all twelve "
    "auxiliary proof items compared. All theorem conclusions and parameter scopes stand. "
    "Give exact original-germ, period, Gysin, Wang, normal-sector and global inverse maps; "
    "retain the original local rim correction by the explicit integral section shear "
    "and its zero exterior image. The fresh tube notation is scoped to its bounding "
    "section, with no claim that a separate Wang section has zero correction. "
    "Supply every finite/regular free parameter and all 495 pattern counts. "
    "Replace file/certificate dependence and process wording by the mathematical "
    "enumeration and complete proof. The historical exact JSON is absent; no old-byte "
    "comparison or historical execution claimed. All labels, targets and printed "
    "equation tags preserved. Root admission and canonical/unit/build/page steps remain separate."
)
replacements=[]
for kind,before,after,span in (
    ("statement",old_statement,new_statement,sspan),
    ("proof",old_proof,new_proof,pspan)):
    replacements.append(dict(statement_id=ID,old_text=before,new_text=after,
                             reason=f"Separate {kind} guard at canonical lines {span[0]}-{span[1]}. "+reason))
write_tsv("replacements",["statement_id","old_text","new_text","reason"],replacements)
trial=source
for row in replacements:
    assert trial.count(row["old_text"])==1
    trial=trial.replace(row["old_text"],row["new_text"],1)
assert canonical.read_bytes()==canonical_bytes
print("PASS two replacements apply once in memory; canonical bytes unchanged.")

def span_text(text,start,end):
    i=text.index(start)
    return text[i:text.index(end,i+len(start))].rstrip("\n")

defects=[]
def defect(suffix,kind,before,after,why):
    candidates=[(part,span) for part,span in ((old_statement,sspan),(old_proof,pspan))
                if before in part]
    assert len(candidates)==1,(suffix,"old quote absent or ambiguous")
    part,span=candidates[0]
    assert part.count(before)==1,(suffix,"repeated old quote")
    assert after in new,(suffix,"new quote absent")
    old_line=span[0]+part[:part.index(before)].count("\n")
    new_line=1+new[:new.index(after)].count("\n")
    defects.append(dict(
        change_id="c7-III-02L9-"+suffix,type=kind,statement_id=ID,
        old_location=f"S6_SERIES_PUBLISH_III.tex:{old_line}",old_page="",
        new_location=str((LANE/(BASE+"receiving.tex")).relative_to(ROOT))+f":{new_line}",
        new_page="",old_text=before,new_text=after,reason=why,
        review_status="proposed; root comparison, source application and final page review pending"))

header=next(line for line in old_statement.splitlines() if line.startswith(r"\StatementRecord"))
defect("header","D10",header,r"\textup{\small(tag 02L9)}",
       "Replace the machine record by the small permanent printed tag.")
defect("title","D16",old_statement.splitlines()[0],new_statement.splitlines()[0],
       "Use a short capitalized mathematical title; preserve label and target.")
defect("external-json","D09",
       "Every original/Mumford choice represented by such an\nagreement is also listed explicitly in\n\\path{records/manifolds_original_multiplicative.json}.",
       "The quotient map forgets the $z$ zero-Chern choices, and its\nsection chooses the primitive filling at those sites.",
       "Replace dependence on the absent historical JSON by the complete finite quotient rule, all 21 count rows and new complete representative data.")
defect("new-sites-wording","D08",
       "The new original caps occur at $120$ marked zero-free\n$I_n$ sites with nonzero component Chern vector.",
       "There are $120$ marked zero-free multiplicative positions with\nnonzero component Chern class.",
       "State the site count and geometric condition directly.")
defect("verbatim-transfer","D14",
       span_text(old_statement,"Consequently \\ref{maps:src:D.2.32}","In particular, when $L>0$,"),
       span_text(new_statement,"Let $L$ count all nonzero-Chern original fillings,","Write the Seifert abelianization"),
       "Give the complete additive and multiplicative defect definition at its use.")
defect("machine-enumeration","D10",
       r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
       "Write the multiplicative fibre as $I_\\nu$.",
       "Replace machine-prefixed enumeration by one connected proof ordered by its constructions.")
defect("homology-scope","D02",
       "It does not\nassert a relative diffeomorphism between their caps.",
       "If the maps\nare $f_O,f_M$ with the displayed sections, the target isomorphism\nis $f_M\\sigma_O$, with inverse $f_O\\sigma_M$.",
       "State the exact positive homology-diagram isomorphism used by the theorem.")
defect("line-scope","D02",
       "The lift preserves the line bundle with Chern\nvector $c$; this bundle is not replaced by a trivial one.",
       "The line class on the original neighbourhood $N$ is\n\\[\n                 c_1(M)=C_{\\bar p}^*-C_0^*,\\qquad \\bar p\\ne0.\n\\]",
       "Retain the actual nonzero line class as the input of the bundle and gauge construction.")
defect("internal-reference","D04",
       "There is one additional point compared with the tree\nargument of D.2.32: the dual graph of $I_n$ has a circle.",
       "The central fibre $K$ is a cycle of $\\nu$ rational curves.\nArcs between their nodes form a graph circle.",
       "Replace the internal source-number reference by the full local graph construction.")
defect("neron-accent","D23",
       "The local\nNeron logarithm of $Q$ contracts its translation to the\nidentity.",
       "Its remaining local N\\'eron logarithm is holomorphic\non the base disc.",
       "Restore the accent and state the exact local logarithm domain.")
defect("product-coordinate","D20",
       r"U\simeq Y_c\times S^1_\gamma,\qquad",
       r"U\simeq Y_c\times S^1_\ell,\qquad",
       "Identify the product circle through ell=gamma-(b*kappa/nu)r0, with the inverse physical-period map, instead of parallel coordinate names.")
defect("certificate-dependence","D09",
       "The certificate records the\nunimodular basis for each of the $120$ occurrences.",
       span_text(new_proof,"Choose $x,z\\in\\mathbb Z$","In exterior order"),
       "Supply the all-parameter unimodular basis and inverse in the proof; the new complete data separately verify every occurrence.")
defect("rational-disclaimer","D02",
       "These are equalities in the marked lattice, not only\na rational normal form.",
       "The inverse adds $B$ times the last coordinate to the $r_0$\ncoordinate.",
       "Give the integer inverse directly.")
defect("raw-wang-marking","D20",
       "The image of\n$\\bigwedge^2 A-I$ is a primitive rank-two sublattice\nof \\eqref{maps:eq:D.OM8}.",
       span_text(new_proof,"The basis change from the displayed","The normal sweeps"),
       "Display the exact determinant-one identification of the raw kernel with two Wang relations and the one surviving primitive kernel.")
defect("normal-section","D20",
       "Subtracting that multiple\nproduces an actual boundary-kernel cycle with normal\nprojection $u_1$.",
       span_text(new_proof,"The cycle\n\\[","For the exterior fibre functional,"),
       "Retain the original correction integer as the inverse Gysin rim coordinate and give the full unipotent section map and inverse; clarify the frozen fresh section scope.")
defect("local-correction-scope","D02",
       "This correction cannot be discarded at the local level.",
       "The exterior map commutes with $Q_j$.",
       "State the proved exact exterior compatibility after retaining the local section shear.")
defect("wedge-notation","D20",
       r"\omega=a e_1^*e_2^*-b\delta^*\gamma^*.",
       r"\omega=a e_1^*\wedge e_2^*-b\delta^*\wedge\gamma^*,",
       "Use explicit exterior products and the same physical angular/contracting marking.")
defect("old-matrix-wording","D08",
       "The preceding kernel calculation shows that the latter\nis exactly the old fixed-sweep matrix with the new\nrelation \\eqref{maps:eq:D.OM1}.",
       "At every original filling set its full fixed sweeps to zero\nand impose its fibre relation when its component Chern class\nis nonzero.",
       "Write the complete finite, regular, original and global relation maps instead of referring to an old matrix.")
defect("now-applies","D08",
       "The proof of \\eqref{maps:eq:D.OC3} now applies with the enlarged $L$\nand $\\beta$.",
       span_text(new_proof,"An integral basis of this kernel","Every original cap"),
       "Supply the integral bounding-chain section and the resulting H2 decomposition before duality.")
defect("count-reason","D22",
       span_text(old_proof,"Finally, choose original or marked Mumford independently",r"\end{enumerate}"),
       span_text(new_proof,r"\emph{Enumeration.}",r"\end{proof}"),
       "Give the exact factor/residue enumeration, quotient/section, distinct-kernel proof and exhaustive 21-profile counts.")
fields=["change_id","type","statement_id","old_location","old_page","new_location","new_page",
        "old_text","new_text","reason","review_status"]
write_tsv("defects",fields,defects)
assert len(defects)==20
assert all(d["type"] not in ("D25","D26","D27") for d in defects)
print("PASS",len(defects),"complete correction rows; all old locations confined to the released target blocks.")
print("PASS no original mathematical refutation or parameter/smooth-classification defect proposed.")

fresh_where=[
    BASE+"fresh_derivation.md",BASE+"fresh_data.json",BASE+"fresh_patterns.tsv"]
fresh_where=[str((LANE/p).relative_to(ROOT)) for p in fresh_where]+[
    "agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02L9_fresh_root_review.md",
    "code/S6_SERIES_PUBLISH_c7_l9_catalogue.py",
    "code/S6_SERIES_PUBLISH_c7_l9_catalogue.out",
    "code/S6_SERIES_PUBLISH_c7_l9_mathcheck.py",
    "code/S6_SERIES_PUBLISH_c7_l9_mathcheck.out"]
post_where=[str((LANE/(BASE+suffix)).relative_to(ROOT)) for suffix in (
    "released_statement.tex","released_proof.tex","post_exposure_derivation.md",
    "post_exposure_checks.json","comparison.md","receiving.tex","replacements.tsv","defects.tsv")]
post_where += ["code/S6_SERIES_PUBLISH_c7_l9_post_exposure.py",
               "code/S6_SERIES_PUBLISH_c7_l9_post_exposure.out",
               "code/S6_SERIES_PUBLISH_c7_l9_receiver_check.py",
               "code/S6_SERIES_PUBLISH_c7_l9_receiver_check.out"]
assert all((ROOT/p).exists() for p in fresh_where+post_where)
now=datetime.now(timezone.utc).isoformat()
common=dict(statement_id=ID,date="2026-11-25",
    who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed",
    source_file="S6_SERIES_PUBLISH_III.tex",source_row=sspan[0],
    evidence_group="publish:c7:III:02L9:check-sequence",
    publish_input_file=str((LANE/(BASE+"comparison.md")).relative_to(ROOT)),
    publish_input_row=1,date_utc=now)
events=[]
events.append(dict(common,type="targeted proof check",
    outcome=(
      "Before individual original release, derived the complete theorem from the statement-only "
      "packet and permitted construction inputs. Frozen 2026-11-25T00:16:32Z and fully read by root "
      "before release 2026-11-25T00:20:45.744670Z. Proved actual original-germ line/roof maps, "
      "graph winding, primitive rim, period and Wang inverses, all 120 h=b/n relations and "
      "local defects, 316 zero-Chern diagram agreements, 495 patterns and all 1728 representatives. "
      "Derived all free finite/regular parameters, full Thom kernels, exact Seifert maps, "
      "the integral L+r bridge and every homology degree at both Euler values. Entire new "
      "program/output read, including 990 complete matrix checks. The fresh t(u) notation is "
      "scoped to its geometrically bounding section; post-exposure comparison retains the marked "
      "geometric normal torus's rim correction with its exact inverse shear. No claim that that "
      "section has correction zero, and no post-exposure or historical execution receives blind credit."),
    event_id="publish:c7:III:02L9:fresh-complete-derivation",
    phase="before whole original L9 exposure",source_event_type="targeted proof check",
    where="; ".join(fresh_where)))
events.append(dict(common,type="used and rechecked in this run",
    outcome=(
      "After individual release, read the complete original theorem and all twelve proof items, "
      "every labelled formula and auxiliary, and all historical computation assertions. "
      "Compared them with the frozen proof and complete receiver. The nodal CW model, every "
      "local Gysin/Kunneth group, actual gamma-to-ell map, raw-to-Wang kernel inverse, exact "
      "rim-section shear O(j)Q_j=O(0) for the marked geometric normal torus with bounding "
      "projection and zero long coordinate, zero exterior correction, finite norm-lift law, "
      "full global extension and 282-to-495 exhaustion are supplied. New symbolic post-exposure "
      "calculation proves the section identities for every j and checks all 120 occurrences, "
      "282 additive patterns (54 nonzero) and 1728 representatives. All theorem conclusions "
      "stand; no original D25, parameter D26 or smooth D27. Exact historical JSON absent; "
      "no bytewise-table comparison or historical execution claimed. Two separate exact guards, "
      "20 correction rows and all permanent identities checked. Syntax checking gives no "
      "TeX/PDF/build, unit or page credit. Root admission and canonical application remain pending. "
      "This row adds no independent-blind credit."),
    event_id="publish:c7:III:02L9:whole-original-comparison",
    phase="after whole original L9 exposure",source_event_type="used and rechecked in this run",
    where="; ".join(fresh_where+post_where)))
event_fields=["statement_id","date","who","type","outcome","event_id","phase","source_file",
              "source_row","source_event_type","evidence_group","publish_input_file",
              "publish_input_row","date_utc","where"]
write_tsv("CHECK_EVENTS",event_fields,events)
assert len({e["evidence_group"] for e in events})==1
assert canonical.read_bytes()==canonical_bytes
print("PASS two correctly scoped event proposals share one evidence group; no extra blind credit.")
print("PASS all proposal writes confined to the owning lane; canonical/global tables unchanged.")
print("RECEIVER SHA256",sha256((LANE/(BASE+"receiving.tex")).read_bytes()).hexdigest())
print("PACKET COMPLETE UTC",now)
