#!/usr/bin/env python3
"""Prepare only the local LE exact guards, defects and check-event proposals."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import csv,re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_mixed_torsion"
STEM="S6_SERIES_PUBLISH_III_02LE_"
SID="maps:src:D.2.38"
def digest(p):return sha256(p.read_bytes()).hexdigest()
frozen={
 LANE/(STEM+"fresh_derivation.md"):"06c310525ed34c167a7b5b8fad0e244ec0c5277b47683eb0dc968b15f0374a5a",
 LANE/(STEM+"inputs_and_primary_reading.md"):"58b9e50360ac608f2e9e08585b645c516c8b747ca8626d4433ca64897de2ae92",
 LANE/(STEM+"execution_reading.md"):"f5761653287f5232b3080fbf96611db496ca660ece66db5a67325b0f03e282b2",
 LANE/(STEM+"fresh_data_v001.json"):"8816e5af8593ed9758496217fe14a553fc8e4a2ee48ea7069d27d990ac9f9bf0",
 LANE/(STEM+"fresh_patterns_v001.tsv"):"383bb8e3cd9956b6c917e0f1ac1fb5b094439c68c286bdf261e9ea857f5524a2",
 ROOT/"code/S6_SERIES_PUBLISH_c7_le_mixed_v001.py":"9f86482aca7952719c5fd34037a411d7675e091896cf3f176d5c10bb68c68a42",
 ROOT/"code/S6_SERIES_PUBLISH_c7_le_mixed_v001.out":"0ea6a63da32f30f54d05bce170fd09f61c6c6fc10f1248f4b747c79f498d7b55",
 ROOT/"code/S6_SERIES_PUBLISH_c7_le_mixed_v001.err":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}
for p,h in frozen.items():assert digest(p)==h,(p,digest(p))

def block(s,env):
    a=r"\begin{"+env+"}";b=r"\end{"+env+"}"
    assert s.count(a)==s.count(b)==1
    i=s.index(a)
    return s[i:s.index(b,i)+len(b)]
old_statement=block((LANE/(STEM+"released_statement.tex")).read_text(),"theorem")
old_proof=block((LANE/(STEM+"released_proof.tex")).read_text(),"proof")
assert sha256(old_proof.encode()).hexdigest()=="8a174956c35210b254e48f20fb2b4aafd1275cb917645db07af911eb8a2b5c93"
assert len(old_proof.splitlines())==201
assert len(re.findall(r"^\\item",old_proof,re.M))==12
canonical=ROOT/"S6_SERIES_PUBLISH_III.tex"
canonical_hash="9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
assert digest(canonical)==canonical_hash
source=canonical.read_text()
assert source.count(old_statement)==source.count(old_proof)==1
assert source.count("\n",0,source.index(old_proof))+1==16294

receiver_path=LANE/(STEM+"receiving.tex")
assert digest(receiver_path)=="0460f70c1201c0212a95ebbc8bd4ae08eba1d9323d6be836e264cc72043c9a92"
receiver=receiver_path.read_text()
new_statement=block(receiver,"theorem");new_proof=block(receiver,"proof")
old=old_statement+"\n\n"+old_proof
new=new_statement+"\n\n"+new_proof
assert receiver.rstrip("\n")==new
assert len(re.findall(r"^\\item",new_proof,re.M))==13
for kind in ("label","hypertarget","tag"):
    pat=r"\\"+kind+r"\{([^{}]+)\}"
    before=Counter(re.findall(pat,old));after=Counter(re.findall(pat,new))
    assert before==after,(kind,before,after)
    print(kind,dict(after),flush=True)
assert len(re.findall(r"\\label\{",new))==11
assert r"\textnormal{\small tag02LE.}" in new_statement
for token in (r"\StatementRecord",r"\SeriesRef","records/",".json","code/",
              "SHA256","the program","admitted","fresh"):
    assert token not in receiver,token
assert not re.search(r"(?<!\\)\b(qquad|quad)\b",new)
assert not re.search(r"\\\\\s*\n\[",new)
stack=[]
for m in re.finditer(r"\\(begin|end)\{([^{}]+)\}",new):
    action,env=m.groups()
    if action=="begin":stack.append(env)
    else:assert stack and stack.pop()==env,m.group()
assert not stack
depth=0
for c in re.sub(r"\\[{}]","",new):
    if c=="{":depth+=1
    elif c=="}":
        depth-=1
        assert depth>=0
assert depth==0
for left,right in ((r"\[",r"\]"),(r"\(",r"\)")):
    assert len(re.findall(r"(?<!\\)"+re.escape(left),new))==len(re.findall(r"(?<!\\)"+re.escape(right),new))
assert new.count("$")%2==0
for m in re.finditer(r"\\\[([\s\S]*?)\\\]",new):assert "\n\n" not in m.group(1)

def write(name,fields,rows):
    p=LANE/(STEM+name+".tsv")
    if p.exists():
        with p.open(newline="") as f:assert list(csv.DictReader(f,delimiter="\t"))==rows
        assert b"\r" not in p.read_bytes()
        print("Retained byte-unchanged existing exact rows",str(p.relative_to(ROOT)),flush=True)
        return p
    assert not p.exists(),p
    with p.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        w.writeheader();w.writerows(rows)
    assert b"\r" not in p.read_bytes()
    with p.open(newline="") as f:assert list(csv.DictReader(f,delimiter="\t"))==rows
    return p

reason=("Complete pre-exposure proof and raw-only new computation reviewed before release; "
        "all statement clauses and twelve original proof items, including every auxiliary, compared. "
        "Retain maps:src:D.2.38 and all eleven label/hypertarget pairs and ten equation tags. "
        "Refine X=M_t#Z_(p,epsilon), t=1+kappa mod2, P_p=(b/p-a nu)/2 modp, "
        "P_(2p)=CRT(t,P_p), mu=p t gamma3(s), with three order-ten and two order-fourteen types. "
        "Retain all twelve patterns and every allowed finite parameter. "
        "Supply the actual fan/line/action morphisms, all generator inverses, full primary invariants, "
        "coprime CW and bordism maps and complete marked recognition scope.")
guards=[
 dict(statement_id=SID,old_text=old_statement,new_text=new_statement,reason=reason),
 dict(statement_id=SID,old_text=old_proof,new_text=new_proof,reason=reason),
]
guard_path=write("replacements",["statement_id","old_text","new_text","reason"],guards)
replay=old
for g in guards:
    assert replay.count(g["old_text"])==1
    replay=replay.replace(g["old_text"],g["new_text"],1)
assert replay==new
print("guard_replay PASS: two separate exact canonical-matching environments, roundtrip and replay.",flush=True)

def span(s,a,b):
    i=s.index(a);return s[i:s.index(b,i)+len(b)]
def defect(suffix,kind,location,oldtext,newtext,why,identity=SID):
    assert oldtext in old,(suffix,"old")
    assert newtext in new,(suffix,"new")
    return dict(change_id="c7-III-02LE-"+suffix,type=kind,statement_id=identity,
        old_location="S6_SERIES_PUBLISH_III.tex; "+location,old_page="",
        new_location=str(receiver_path.relative_to(ROOT)),new_page="",
        old_text=oldtext,new_text=newtext,reason=why,
        review_status="whole comparison submitted to root; admission pending")
defects=[
 defect("machine-header","D10",SID,
    next(x for x in old_statement.splitlines() if x.startswith(r"\StatementRecord")),
    r"\textnormal{\small tag02LE.}",
    "Remove the machine status/dependency header and print the small tag; preserve every permanent identity."),
 defect("smooth-types","D27","statement D.MP1--D.MP2 and final counts",
    span(old_statement,r"                  X\cong",r"one for $c=14$."),
    span(new_statement,r" H_2(X)=\mathbb Z/(2p)",r"with multiplicities $3,2$."),
    "Refine maps:src:D.2.38 under the same identity. OS56(3,10), zero4,e=1 has actual mod2 cube0 and integral mu0; "
    "the old conic connected sum has cube1 and mu5 gamma3(s), fixed under every unit action u^3. "
    "OS56(1,10),zero1,e=1 has odd p1 pairing -42=3 mod5 and refined coefficient2, whereas old epsilon is0. "
    "The complete replacement is X=M_(1+kappa mod2)#Z_(p,epsilon), P_p=(b/p-a nu)/2, "
    "P_(2p)=CRT(1+kappa,P_p), mu=p(1+kappa mod2)gamma3(s). "
    "All twelve patterns stand; mod2 assignments3,4,5,6,7,9,10 and odd assignments1,4,5 change. "
    "There are three order-ten types with multiplicities2,4,1 and two order-fourteen types with multiplicities3,2."),
 defect("physical-fan-cube","D25","proof items4 and7; D.MP4 and D.MP7",
    span(old_proof,"Its vertical slope has odd constant term",r"since its signed value is $-a(\rho-br)$."),
    span(new_proof,"In (18) the actual physical valuation matrix",r"No local or global flop is invoked."),
    "Retain the integral physical polynomial and both true period differences. "
    "The actual prescribed fan has short basis SC, with phi(Cv)=-psi(v)+L0 v and integral L0=(a row1(C)-epsilon)/2. "
    "The reciprocal monomials identify regular Cartier frames including all units. "
    "C^-1 delta=(-b kappa,nu), c_C=(b/2)(a kappa(b kappa-nu)-1)=1+kappa mod2, "
    "degree a(nu-b kappa). D.MP7 is therefore cube1+kappa, not uniformly1.",
    "maps:eq:D.MP4"),
 defect("common-action-normalization","D25","proof item8; D.MP8",
    "The weights are $(1,-1)$ and $(w,-w)$.",
    span(new_proof,"The action conversion retains every generator.",r"for every assignment in \eqref{maps:eq:D.MP2}."),
    "The physical action has cusp pair +/-nu and elliptic pair +/-w. The exponent nu^-1 with inverse nu "
    "changes both pairs to +/-1 and +/-w/nu. In z[C]=1 marking, z[Ep]=-w^2/nu^2 and "
    "z p1=-2(1-w^2/nu^2); its coefficient (w^2/nu^2-1)/2 converts by a nu to "
    "P_p=(b/p-a nu)/2. All physical w values stand; the old zero criterion omitted this common action map.",
    "maps:eq:D.MP8"),
 defect("line-comparison","D22","proof item3; global prequantum comparison",
    span(old_proof,"Their comparison with the marked prequantum family",r"including its zero swept values."),
    span(new_proof,"Here are the maps identifying this line",r"equality of period matrices alone is not used."),
    "Supply the actual theta, Gaussian and integral monomial gauges with reciprocal inverses, all h/F/J maps and units. "
    "The degree-one graph and primitive exterior maps prove torsion-free H^2(V); the exact global line has Omega and zero sweep values. "
    "The tensor-square/cap comparison proves the original two-torsion bound by the stronger exact Chern equality."),
 defect("borel-character-choice","D22","proof item7; simultaneous Borel adjustment",
    span(old_proof,"To justify a simultaneous choice","One base adjustment therefore gives\n"+r"exactly the restrictions \eqref{maps:eq:D.C216}."),
    span(new_proof,r"\item \emph{A single global Borel character comparison.}",
         r"unrelated lifts at its fixed curves."),
    "Give the whole-circle-fixed endpoint, split actual fundamental group, unique finite subgroup, complete degree-two kernel and common base shift with inverse. "
    "Retain the mixed integral degree-one term; its square vanishes. The shift comparison stands but its actual cusp character is 1+kappa."),
 defect("coefficient-inverses","D22","proof items10--11; D.MP9--D.MP10 and connected sum",
    span(old_proof,"Here the comparison to the product",r"of the corresponding primary automorphism groups."),
    span(new_proof,r"\item \emph{The full coprime homotopy and bordism maps.}",
         r"been determined under the actual maps and their inverses."),
    "The full CW homotopy equivalence stands. Give its cellular retraction q with qi=id and iq~id relative wedge; "
    "CRT inverse p x+(1-p)y; bordism inverse factor inclusions followed by inverse CRT; "
    "unit inverse p+(1-p)r^-1; connected-sum ball contraction, neck collapse and oriented spin one-handle map. "
    "The preceding Phi and Phi^-1 give the exact primitive second-homology marking."),
 defect("certificate-prose","D09","proof items3 and6",
    span(old_proof,"Their\nsemicharacter",r"Thus the rigidified factors patch."),
    span(new_proof,r"\item \emph{Exhaustion from the raw defining profiles.}",
         r"Use their ordered defining matrices and cocycles in the following period maps."),
    "Remove historical certificate/execution assertions. The proof states the complete factor, component and cap-option method and all resulting patterns. "
    "The new raw-only computation and post-exposure auxiliary checks are separately retained/read; no historical LE certificate was opened or credited."),
 defect("recognition-locus","D18","proof item11; Zhubr classification",
    span(old_proof,"Zhubr's Theorem~3","gives the required oriented\ndiffeomorphism."),
    span(new_proof,"Use the marked recognition theorem.",
         r"is an actual oriented identification with its prescribed homology map."),
    "Specify Theorem5 p796 injection, Theorem3 p795 and Section4.1 p809 marked zero-free-H3 construction and uniqueness. "
    "Both free H2 and H3 ranks vanish here; preserve the admitted K9 printed-rank correction. "
    "The diffeomorphism induces Phi and its inverse induces the stated inverse. No additional primary or whole-PDF reading is claimed."),
]
defect_path=write("defects",
 ["change_id","type","statement_id","old_location","old_page","new_location","new_page","old_text","new_text","reason","review_status"],defects)

timestamp=datetime.now(timezone.utc).isoformat()
group="publish:c7:III:02LE"
who="GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; seventh continuation"
evidence=[str(p.relative_to(ROOT)) for p in frozen]
evidence.extend(str((LANE/(STEM+name)).relative_to(ROOT)) for name in
 ("released_statement.tex","released_proof.tex","receiving.tex","comparison.md",
  "post_exposure_auxiliary.md","replacements.tsv","defects.tsv"))
for name in ("post_exposure_v001","receiver_v001","receiver_edits_v001","records_v001","records_v002"):
    evidence.extend("code/S6_SERIES_PUBLISH_c7_le_"+name+ext for ext in (".py",".out",".err"))
evidence.append("code/S6_SERIES_PUBLISH_c7_le_receiver_orchestration_attempt001.out")
common=(" All frozen fresh hashes remain unchanged. Exact admitted-input and primary reading scopes are disclosed. "
        "No historical LE execution, second independent-family count, canonical/global mutation, PDF/build/page-reading, "
        "unit closure or publication-gate credit. Manual proof-local numbering and enumerate style remain for the existing unit pass. "
        "The failed pre-write JavaScript submission's exact parser output is retained; its complete orchestration source "
        "was not saved and is not reconstructed. All successful Python sources and actual separate streams are retained. Root admission pending.")
common += (" The initial record writer stopped on a literal-newline text locator after writing only the valid exact guards. "
           "Its full v001 source/stdout/stderr are retained; v002 corrects only the locators and reuses those guard bytes unchanged.")
events=[]
def event(suffix,typ,outcome,phase):
    events.append(dict(statement_id=SID,date=timestamp[:10],who=who,type=typ,outcome=outcome,
        event_id=group+":"+suffix,phase=phase,source_file="S6_SERIES_PUBLISH_III.tex",
        source_row="16294",source_event_type=typ,evidence_group=group,
        publish_input_file=str((LANE/(STEM+"CHECK_EVENTS.tsv")).relative_to(ROOT)),
        publish_input_row=str(len(events)+2),date_utc=timestamp,where="; ".join(evidence)))
event("targeted","targeted proof check",
    "Complete fresh proof frozen2026-11-25T04:04:24Z, root fully reviewed before release. "
    "Raw-only new enumeration derives172 natural rows and all12 minimal c10/14 patterns on10 initial rows. "
    "Complete actual period/line/cap maps and inverses, all finite orders and affine twists, primitive exterior/Thom kernels, "
    "prescribed-fan C2/Cp fixed data, global equivariant line and common Borel shift, full integral mu and refined P, "
    "exact marking maps and oriented classification proved. New477-line program and all333 output lines read, "
    "including every raw input matrix, all primitive integer sections and34 marked model maps. "
    "Result X=M_t#Z_(p,epsilon), t=1+kappa mod2, P_p=(b/p-a nu)/2, P_(2p)=CRT(t,P_p), "
    "mu=p t gamma3(s), gives3 order-ten and2 order-fourteen types."+common,
    "complete pre-exposure derivation and new computation")
event("smooth-identification-refuted","refuted, with the refined statement's id",
    "D27: refutes the uniform conic factor, three odd assignments and old2/1 type counts in maps:src:D.2.38. "
    "Refined statement retains maps:src:D.2.38, D.MP1/D.MP2 and all permanent identities. "
    "Full formula H2=H3=Z/(2p), spin,b3=0, X=M_t#Z_(p,epsilon), t=1+kappa mod2, "
    "P_p=(b/p-a nu)/2, P_(2p)=CRT(t,P_p), mathfrak p=P_(2p)s, mu=p t gamma3(s), epsilon=0 iff P_p=0. "
    "OS56(3,10),zero4,e1 has cusp characters160,-170, degrees33,-5 and cube0/integral mu0; "
    "the claimed conic sum has cube1 and mu5 gamma3(s), fixed by every unit's cube. "
    "OS56(1,10),I3 zero1,e1 has p1 pairing-42=3 mod5, hence P_p=2 instead of0. "
    "Mod2 assignments3,4,5,6,7,9,10 and odd assignments1,4,5 change; all12 patterns and parameter ranges stand. "
    "Counts are3 order-ten types (multiplicities2,4,1) and2 order-fourteen types (3,2), all realized."+common,
    "refuted smooth identification and assignments with complete refined statement and proof")
event("fan-and-action-refuted","refuted, with the refined statement's id",
    "D25: narrow intermediate refutation under retained maps:eq:D.MP4,D.MP7,D.MP8. "
    "True original physical polynomial/period differences and physical Tate weights stand. "
    "The actual fan map C=[[nu,b kappa],[-a kappa,rho]] with inverse [[rho,-b kappa],[a kappa,nu]] "
    "gives phi(Cv)=-psi(v)+L0 v, reciprocal line-gauge maps and scalar vector(-b kappa,nu). "
    "Thus c_C=(b/2)(a kappa(b kappa-nu)-1)=1+kappa mod2 and positive degree a(nu-b kappa). "
    "The common physical action has normal pairs +/-nu,+/-w; exponent nu^-1, inverse nu, gives +/-1,+/-w/nu. "
    "In z[C]=1 marking the corrected pairing is-2(1-w^2/nu^2), and multiplication by a nu "
    "with its inverse recovers P_p=(b/p-a nu)/2. These corrections imply the displayed exact theorem refinement."+common,
    "intermediate fan and common-action assertions compared after whole-original release")
event("whole-original-used","used and rechecked in this run",
    "After individual release2026-11-25T04:13:26.115296+00:00, read the whole statement and all201 original proof lines, "
    "all12 items and every auxiliary, the full13-item1297-line receiver and final changed passages. "
    "Post-exposure note proves physical support/unit/gauge compatibility, both rank-one differences including nonprimitive periods, "
    "the complete coprime CW homotopy equivalence with cellular inverse, spin-bordism projections/inclusions, "
    "CRT/unit inverses, connected-sum coefficient maps and exact marked recognition scope. "
    "Complete new auxiliary source/output read: all12 support/generator conversions and864 semicharacter checks. "
    "Full comparison distinguishes the seven changed cubes, three changed odd assignments and retained raw weights. "
    "Two separate exact guards match canonical statement/proof; all11 labels/hypertargets and10 equation tags, "
    "local replay, TSV roundtrip and balanced structures verified. Historical certificate prose replaced without historical execution."+common,
    "whole original and receiver reading; disclosed post-exposure auxiliary derivation and computation")
event_path=write("CHECK_EVENTS",
 ["statement_id","date","who","type","outcome","event_id","phase","source_file","source_row","source_event_type",
  "evidence_group","publish_input_file","publish_input_row","date_utc","where"],events)

print("record_timestamp_utc",timestamp,flush=True)
print("original_items12 receiver_items13 receiver_lines",len(receiver.splitlines()),
      "defects",len(defects),"events",len(events),flush=True)
for d in defects:print("defect",d["change_id"],d["type"],d["statement_id"],d["reason"],flush=True)
for e in events:print("event",e["event_id"],e["type"],"group="+group,e["outcome"],flush=True)
paths=[receiver_path,LANE/(STEM+"comparison.md"),LANE/(STEM+"post_exposure_auxiliary.md"),
       guard_path,defect_path,event_path,Path(__file__)]
for name in ("post_exposure_v001","receiver_v001","receiver_edits_v001","records_v001"):
    paths.extend(ROOT/("code/S6_SERIES_PUBLISH_c7_le_"+name+ext) for ext in (".py",".out",".err"))
paths.append(ROOT/"code/S6_SERIES_PUBLISH_c7_le_receiver_orchestration_attempt001.out")
for p in paths:
    print("sha256",digest(p),str(p.relative_to(ROOT)),"bytes",p.stat().st_size,flush=True)
for p,h in frozen.items():assert digest(p)==h,p
assert digest(canonical)==canonical_hash
print("PASS: frozen inputs, canonical exact guards, identities, replay, structure and local records; no global writes.",flush=True)
