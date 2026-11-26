#!/usr/bin/env python3
"""Prepare local LK proposals; apply no canonical or global mutation."""
import csv
from datetime import datetime, timezone
from hashlib import sha256
from itertools import islice
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT/"agents/continuation7_iii_general_cusp"
LANE = ROOT/"agents/continuation7_iii_general_cusp_receiving"
P = "S6_SERIES_PUBLISH_III_02LK_"
ID = "maps:src:D.2.43"
CANON = ROOT/"S6_SERIES_PUBLISH_III.tex"
SOURCE_SHA = "9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
SPANS = {"statement":(17544,17611),"proof":(17614,17862),"auxiliary":(17864,17873)}
OLD_SHA = {
    "statement":"1e6e598d0222dd6c553927a9ce0ce359290098c9179197aa533ac7f3d5783535",
    "proof":"05d19cfb6e15cd90bc84a51dbab2d3f487c094abb37d3a77f3bc29bb33d1e960",
    "auxiliary":"c58b4ed4cd08126e89401cb3ea8b0279ead8c456cdfe810cbaee900fb6ce09d9",
}

def digest(path):
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()

frozen = {
    FRESH/(P+"fresh_derivation.md"):"83191425a6141af9e3e125622493df5c44dfb909ff77c65af6f1ea6d90995f90",
    FRESH/(P+"fresh_source_scope.md"):"1b31a5efa818aaa247390b3a42b7481df3ea34bd412008f0b2fdeebd5a6ca058",
    FRESH/(P+"fresh_calculation_readout.md"):"89f2a381880981c2a669b757e241b6b81f589a80cdb55e196ad35a274ef27383",
    FRESH/(P+"fresh_lattice_data.json"):"0141c55f7ec26c20d6a76baa64f4ce9be67a84a524f8a095c906756cf4c6428e",
    LANE/(P+"receiving.tex"):"05449b31014711d8305e0e5e0ea4706698ab2a191e40ad2078e13aaa1bf996db",
    LANE/(P+"post_exposure_derivation.md"):"245140dd93858573d3f5f03da72acf390cdd5be18e1ebcb25ad0afbdda1bc03c",
}
assert digest(CANON) == SOURCE_SHA
for path,expected in frozen.items():
    assert digest(path) == expected, path

def environment(text,name):
    start = text.index("\\begin{"+name+"}")
    end = text.index("\\end{"+name+"}",start)+len("\\end{"+name+"}")
    return text[start:end]

old = {}
for kind in SPANS:
    source = FRESH if kind != "auxiliary" else LANE
    text = (source/(P+"released_"+kind+".tex")).read_text()
    old[kind] = (environment(text,"theorem" if kind=="statement" else "proof")
                 if kind != "auxiliary" else text.rstrip("\n"))
    lo,hi = SPANS[kind]
    with CANON.open() as f:
        bounded = "".join(islice(f,lo-1,hi)).rstrip("\n")
    assert bounded == old[kind]
    assert len(bounded.splitlines()) == hi-lo+1
    assert sha256(bounded.encode()).hexdigest() == OLD_SHA[kind]
    print("PASS exact",kind,"guard",lo,hi,OLD_SHA[kind])
for lo,hi in ((17612,17613),(17863,17863),(17874,17875)):
    with CANON.open() as f:
        blank = "".join(islice(f,lo-1,hi))
    assert blank == "\n"*(hi-lo+1)
print("PASS only the five specified intervening lines are blank; no next statement opened")

receiver_path = LANE/(P+"receiving.tex")
receiver = receiver_path.read_text()
new = {"statement":environment(receiver,"theorem"),
       "proof":environment(receiver,"proof"),"auxiliary":""}
assert old["proof"].count(r"\item ") == 12
for kind in ("statement","proof"):
    for pattern in (r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}"):
        assert re.findall(pattern,old[kind]) == re.findall(pattern,new[kind])
assert len(re.findall(r"\\label\{",receiver)) == 15
assert len(re.findall(r"\\hypertarget\{",receiver)) == 15
assert len(re.findall(r"\\tag\{D\.GC\d+\}",old["statement"]+old["proof"])) == 14
assert r"\tag{" not in receiver
assert not re.findall(r"\\(?:label|hypertarget)\{",old["auxiliary"])
print("PASS twelve original items, fourteen formulas and all fifteen identity partitions")

def write_tsv(name,fields,records):
    path = LANE/(P+name+".tsv")
    previous = {
        "replacements":"a29a3eb0f94267223df86f4d658e1c33e602a061cff551bb602dfb3965719a12",
        "defects":"237c96b149d6d8d85f7cd393084c8516925cf83acfb23ed2b1257ad719d80767",
        "CHECK_EVENTS":"bef2c72bc42c0e52ec2fc5f287ed9d4fe1044e65a9ca7d1c88ddb0107e48280a",
    }
    assert path.exists() and digest(path) == previous[name], path
    with path.open("w",encoding="utf-8",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)
    raw = path.read_bytes()
    assert b"\r" not in raw and raw.endswith(b"\n")
    with path.open(newline="") as f:
        reread = list(csv.DictReader(f,delimiter="\t"))
    assert reread == [{key:str(row[key]) for key in fields} for row in records]
    return path

replacements = [
    dict(statement_id=ID,old_text=old[kind],new_text=new[kind],
         reason=("Complete LK "+kind+" proposal after whole-original and following-auxiliary comparison. "
                 "All mathematical statements stand. Preserve every permanent identity; "
                 "use one coherent receiving proof and automatic equation numbers. "
                 "The following auxiliary's endpoint maps occur in that proof; its pinned "
                 "program, exact replay and exhaustive comparison are retained in the check files. "
                 "This row applies nothing to canonical III."))
    for kind in ("statement","proof","auxiliary")
]
write_tsv("replacements",["statement_id","old_text","new_text","reason"],replacements)

def between(text,first,last=None):
    assert text.count(first) == 1,(first,text.count(first))
    start = text.index(first)
    return (text[start:] if last is None else text[start:text.index(last,start)]).strip()

def new_between(first,last=None):
    return between(receiver,first,last)

def location(text,snippet,base,filename):
    assert snippet and text.count(snippet) == 1,(snippet[:100],text.count(snippet))
    start = text.index(snippet)
    lo = base+text[:start].count("\n")
    return f"{filename}:lines {lo}--{lo+snippet.count(chr(10))}"

defects = []
def defect(slug,kind,part,before,after,reason):
    defects.append(dict(
        change_id=f"III-c7-02LK-{len(defects)+1:02d}-{slug}",
        type=kind,statement_id=ID,
        old_location=location(old[part],before,SPANS[part][0],
                              "S6_SERIES_PUBLISH_III.tex ("+part+" guard)"),
        old_page="not asserted; exact released source interval",
        new_location=location(receiver,after,1,str(receiver_path.relative_to(ROOT))),
        new_page="pending final III PDF build and page review",
        old_text=before,new_text=after,reason=reason,
        review_status="local whole comparison complete; root admission and final page review pending"))

s,p,a = old["statement"],old["proof"],old["auxiliary"]
defect("machine-header","D10","statement","\n".join(s.splitlines()[:2]),
       "\n".join(new["statement"].splitlines()[:2]),
       "Replace machine uses/status apparatus by the mathematical heading and small printed tag; preserve label and hypertarget.")
defect("machine-proof-prefix","D10","proof",
       r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
       r"\noindent\emph{Fan charts, covers and units.}",
       "Use mathematical proof paragraphs in the single receiving proof; all twelve original items are compared.")
tags = {1:"01YY",2:"01Z4",3:"01Z5",4:"01Z6",5:"01Z7",6:"01Z8",7:"01Z9",
        8:"01ZA",9:"01ZB",10:"01YZ",11:"01Z0",12:"01Z1",13:"01Z2",14:"01Z3"}
for n,tag in tags.items():
    tail = r"\hypertarget{tag-"+tag+r"}{}\label{maps:eq:D.GC"+str(n)+"}"
    defect("gc"+str(n)+"-number","D19","statement" if n<=4 else "proof",
           r"\tag{D.GC"+str(n)+"}"+tail,
           r"\begin{equation}"+tail,
           "Use section-based equation numbering while preserving the exact permanent equation label and hypertarget. "
           "For GC6 the identical matrix is denoted mathcal F to distinguish the fixed lattice F; its entries and maps are unchanged.")
defect("fixed-normal-wording","D08","statement",
       "The two actual fixed angular normal tori bound\nand give the entire fixed-normal projection.",
       "The two fixed angular normal tori bound and project to a basis of\n\\(F\\) in the Wang sequence.",
       "State the primitive Wang projection in mathematical terms.")
defect("cap-torsion-wording","D08","statement",
       "the actual cap torsion.","isomorphically to the cap torsion.",
       "Remove workflow vocabulary from the integral torsion assertion.")
defect("cover-heading","D08","proof",
       r"\emph{The actual covering and its two-variable normalization.}",
       r"\emph{Fan charts, covers and units.}",
       "Use a mathematical heading; the covering, units and normalization are proved explicitly.")
defect("boundary-heading","D08","proof",
       r"\emph{The actual boundary map and the nonsaturated kernel.}",
       r"\emph{Boundary coordinates.}",
       "Use a mathematical heading; retain the nonsaturated kernel and its exact inverse maps.")
defect("normal-sweep-wording","D08","proof",
       "tori have actual section-disc bounding sweeps.",
       new_between("Acting on that disc by a short","Its normal"),
       "State the circle action on the transverse disc and its literal torus boundary.")
defect("normal-section-wording","D08","proof",
       "their actual classes split off\nthe full Wang projection $H_2(M_L)\\to F$.",
       new_between("The fixed tori","In degree one"),
       "Give the integral Wang section and its inverse by projected short coordinates.")
defect("positive-matrix-comparison","D02","proof",
       "For clarity there is an explicit Laurent-unimodular\ncomparison, not just equality of ranks or minors.",
       "These are chain maps and both inverse chain homotopies.",
       "Replace the defensive comparison by the complete morphisms and inverse homotopies.")
defect("positive-torsion-kernel","D02","proof",
       between(p,"There is no hidden free-to-torsion extension","\\item The two boundary"),
       new_between("Consequently, after subtracting","Since the nearby fibre"),
       "Replace the defensive paragraph by the full integral relative-group argument and exact boundary kernel.")
defect("positive-lattice-quotient","D02","proof",
       "This proves exactly\n\\eqref{maps:eq:D.GC2}, not its saturation, and gives all\nthe remaining assertions in \\eqref{maps:eq:D.GC3}.",
       new_between("In the Smith coordinates it is","In particular the fibre"),
       "Give the kernel coordinates, quotient and inverse representatives directly.")
defect("poincare-accent","D23","proof","Poincare--Lefschetz","Poincaré--Lefschetz",
       "Restore the accent in the duality name.")
defect("following-program-apparatus","D09","auxiliary",
       between(a,"The complete Laurent-unimodular operations,","When $s=1$"),
       new_between("The cancellation is","Set\n\\["),
       "Move the following file/execution apparatus to the complete following-auxiliary comparison. "
       "Pinned source and saved JSON were retrieved; exact-helper replay is bytewise equal and all 75 cases have a separate field/map validation. "
       "The receiver contains the mathematical operations and both endpoint consequences.")
defect("following-saturation-presentation","D02","auxiliary",
       between(a,"When $s>1$, replacing"),
       new_between("For \\(s>1\\), the displayed fibre kernel","\\medskip"),
       "State the exact lattice witness and both cases in the receiving proof. The following note proves the quotient map kills precisely Z/s; no false-statement or refinement credit.")
defect("following-cap-wording","D08","auxiliary",
       r"the actual cap torsion $\mathbb Z/s$.","the entire torsion of the cap.",
       "Use the cap's exact torsion subgroup and generator without workflow vocabulary.")
assert len(defects) == 29
assert not any(row["type"] in ("D25","D26","D27") for row in defects)
fields = ["change_id","type","statement_id","old_location","old_page","new_location",
          "new_page","old_text","new_text","reason","review_status"]
write_tsv("defects",fields,defects)
print("PASS 29 narrowly typed presentation rows; no D25, D26 or D27")
for row in defects:
    print("DEFECT",row["type"],row["change_id"],row["old_location"],"->",row["new_location"])

fresh_where = [str((FRESH/(P+suffix)).relative_to(ROOT))
               for suffix in ("fresh_derivation.md","fresh_source_scope.md",
                              "fresh_calculation_readout.md","fresh_lattice_data.json")]
fresh_where += ["agents/continuation4_iii_infra/S6_SERIES_PUBLISH_III_02LK_packet.tex",
               "agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LK_fresh_review.md"]
for stem in ("lattices_v1","saved_check_v1"):
    for ext in (".py",".out",".err"):
        fresh_where.append("code/S6_SERIES_PUBLISH_c7_lk_"+stem+ext)
fresh_where += ["code/S6_SERIES_PUBLISH_c7_lk_saved_check_v1_final."+ext for ext in ("out","err")]
post_where = [str((LANE/(P+suffix)).relative_to(ROOT)) for suffix in (
    "receiving.tex","post_exposure_derivation.md","comparison.md","following_auxiliary_comparison.md",
    "released_auxiliary.tex","post_laurent_data_v1.json","historical_manifolds_general_cusp.py",
    "historical_manifolds_general_cusp.json","historical_helper_wedge.py","historical_helper_group.py",
    "historical_replay_data.json","historical_validation_data.json","historical_replay_main.out",
    "historical_replay_main.err","replacements.tsv","defects.tsv")]
post_where += [str((FRESH/(P+"released_"+kind+".tex")).relative_to(ROOT))
               for kind in ("statement","proof")]
for stem in ("post_laurent_v1","post_tor_v1","receiver_v1","receiver_v2","receiver_v3",
             "receiver_v4","receiver_v5","receiver_v6","historical_cache_v1",
             "historical_replay_v1","historical_validate_v1","historical_validate_v2"):
    for ext in (".py",".out",".err"):
        post_where.append("code/S6_SERIES_PUBLISH_c7_lk_"+stem+ext)
for ext in (".js",".out",".err"):
    post_where.append("code/S6_SERIES_PUBLISH_c7_lk_historical_fetch_calls_v1"+ext)
assert all((ROOT/path).exists() for path in fresh_where+post_where)
now = datetime.now(timezone.utc).isoformat()
common = dict(
    statement_id=ID,date="2026-11-25",
    who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed",
    source_file="S6_SERIES_PUBLISH_III.tex",source_row=17544,
    evidence_group="publish:c7:III:02LK:check-sequence",
    publish_input_file=str((LANE/(P+"comparison.md")).relative_to(ROOT)),
    publish_input_row=1,date_utc=now)
events = [
    dict(common,type="targeted proof check",
         event_id="publish:c7:III:02LK:fresh-complete-derivation",
         phase="before whole original LK exposure",source_event_type="targeted proof check",
         where="; ".join(fresh_where),
         outcome=("Complete 858-line statement-only proof frozen 2026-11-25T06:20:04Z before "
                  "individual original release 06:36:44.351604 UTC. Proved every full short lattice "
                  "with all holomorphic units: literal charts, period action and full-lattice cover, "
                  "unit family/collar inverse, proper-tube normalized-gradient retraction, branch "
                  "chain maps, exact normalization torsion with generator/inverse, all cap groups, "
                  "fundamental group, nonsaturated fibre kernel, both boundary torsion coordinates, "
                  "all component discs and integral splitting/inverse. Two complete sources and "
                  "three observed successful execution streams read: 139 finite lattices, including "
                  "20 with nonprimitive short lattice, and exhaustive saved-data checks. Large JSON "
                  "fields were computationally validated, not all manually read. Generic integer "
                  "helper reuse and bounded abstract peer checks are disclosed and receive no extra "
                  "independent-blind credit. Held V input was not opened; its unit comparison was "
                  "proved directly. Original and historical target program remained closed. "
                  "All post-exposure Laurent/Tor and historical comparisons are excluded here.")),
    dict(common,type="used and rechecked in this run",
         event_id="publish:c7:III:02LK:whole-original-comparison",
         phase="after whole original LK exposure",source_event_type="used and rechecked in this run",
         where="; ".join(fresh_where+post_where),
         outcome=("Read and compared all 68 statement lines, all 249 proof lines/twelve items, "
                  "fourteen labelled formulas, every unlabelled auxiliary and the ten-line following "
                  "paragraph. All mathematical assertions stand. Derived the full original Laurent "
                  "cancellation, deck involution/reflection maps, ideal-square quotient, positive "
                  "alpha_L sign, beta/derivative inverse, Tor segment and free-kernel section. "
                  "Complete new 206/196-line sources and 13/10-line stdout plus empty stderr read. "
                  "The pinned 95-line historical main was read and executed with exact wedge/group/"
                  "PAIRS helper definitions; other helper-module bodies were not manually read or "
                  "executed. All 75 cases reproduced the pinned JSON byte for byte. Separate validator "
                  "checked ten symbolic fields and 750 finite fields, both fibre-kernel maps and full "
                  "component/disc inverses; its entire successful source and 82-line output were read. "
                  "The connector fetch .err is a cache-created placeholder, not captured shell stderr. "
                  "Literal-string failure v1 and both assembly failures are retained without success "
                  "credit. Large matrix JSON verification was exhaustive by code, not manual entrywise "
                  "reading. Complete 962-line receiver read, all fifteen identities preserved, three "
                  "separate exact guards and 29 presentation rows proposed. Both s=1 and s>1 endpoints "
                  "are proved with exact quotient maps. No D25/D26/D27, extra independent-blind credit, "
                  "canonical application, unit closure, PDF build or page-review credit is claimed."))
]
event_fields = ["statement_id","date","who","type","outcome","event_id","phase","source_file",
                "source_row","source_event_type","evidence_group","publish_input_file",
                "publish_input_row","date_utc","where"]
write_tsv("CHECK_EVENTS",event_fields,events)
assert len({row["evidence_group"] for row in events}) == 1
assert digest(CANON) == SOURCE_SHA
for path,expected in frozen.items():
    assert digest(path) == expected,path
print("PASS two scoped events in one evidence group; post-exposure work earns no extra blind credit")
print("PASS canonical/global files and all frozen fresh evidence unchanged")
for suffix in ("receiving.tex","post_exposure_derivation.md","following_auxiliary_comparison.md",
               "comparison.md","replacements.tsv","defects.tsv","CHECK_EVENTS.tsv"):
    print("FINAL_SHA256",P+suffix,digest(LANE/(P+suffix)))
print("PACKET_COMPLETE_UTC",now)
