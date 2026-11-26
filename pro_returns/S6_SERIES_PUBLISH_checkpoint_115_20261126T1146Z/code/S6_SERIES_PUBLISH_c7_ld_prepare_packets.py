#!/usr/bin/env python3
"""Prepare LD's exact local comparison proposals; no canonical/global mutations."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import io
import re

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
BASE="S6_SERIES_PUBLISH_III_02LD_"
ID="maps:src:D.2.37"
canonical=ROOT/"S6_SERIES_PUBLISH_III.tex"
canonical_bytes=canonical.read_bytes()
assert sha256(canonical_bytes).hexdigest()=="9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0"
source=canonical_bytes.decode()
frozen={
"fresh_derivation.md":"8b72bf89e09ce2750b192c7216d94b1b63b436f50554f9a446374a9057ee0284",
"fresh_exterior_data.json":"083818ab7e52eaa416fedca4f9676340f2adbd2a90798bc2eb1f14e7b5dbbecc",
"fresh_finite_data.json":"9d921e7c7e379ce973a38eba7443022600fc10f6c3e9256b74daea3806b63bb5",
"fresh_global_data.json":"43f56cbabb43cdb34276d8df48b2aaf303268398765045d00ec514c987a17c61",
"fresh_patterns.json":"db9fdc33cacd22c4b3e00ce854757f8c593d2d1f4d2cedb92a99aa8beb726590",
"pre_exposure_example_supplement.md":"07dc879b94fb5676308c8c7e0385a00adf6ae76cc2eba4368b3a0743a2309561",
"primitive_examples_data.json":"fdf158b072e8d3407ba79ceadf8e7d3d930572935ebaea6b96b256427c141b0c",
}
for suffix,digest in frozen.items():
    assert sha256((LANE/(BASE+suffix)).read_bytes()).hexdigest()==digest,suffix
frozen_code={
"exterior.py":"3a12576b0d98b3cfe5ca4cfab0def92fc0097aa2b3f2359e3e7ac833ccb4a307",
"exterior.out":"da21963355323874f345c6fb8c4b3d5d63ed8410e540b01b97b6b5e998938528",
"finite.py":"a7a5a4117ad7764ee1a3dc6169761f4dc98e8e9b848f6be6b29e89baa437edd5",
"finite.out":"f6f491f82c5cc2deb66626192bb4e1eb336f5b312442353633a6621bccdab3b6",
"catalogue.py":"a54d43e83cbb37a1e2fb0f0ee316b8a2a475256c392d6056be2cac9a9a629f54",
"catalogue.out":"2f583d364422184e0bc06866bb927a0a75b9b688a262f3b1e41ed0ecc782b7cb",
"format_check.py":"a2ec42c9d8aabbe60c216e5ee19762741e3383549c6f3b5d6870c8c323b20f46",
"format_check.out":"e0c7602e0ce4c3b02e322261a38da5a00e1d6ad64529972bfdec3a7a0a6ccf7c",
"primitive_examples.py":"a76c59f7d66418309864fe46eef501eb3538a7d9ccc21eba3d89d9626b8c187d",
"primitive_examples.out":"06897e7627a90f2f33a95471cc4e77345d9cb3e3b7f608c6a45d91ddae6a4a84",
}
for suffix,digest in frozen_code.items():
    assert sha256((ROOT/"code"/("S6_SERIES_PUBLISH_c7_ld_"+suffix)).read_bytes()).hexdigest()==digest,suffix
print("PASS all 17 frozen fresh proof/supplement/data/program/output files unchanged.")

def released(kind,environment,expected_span,expected_hash):
    lines=(LANE/(BASE+"released_"+kind+".tex")).read_text().splitlines()
    assert len(lines)>5 and all(x.startswith("%") for x in lines[:5])
    text="\n".join(lines[5:]).rstrip("\n")
    assert text.startswith("\\begin{"+environment+"}") and text.endswith("\\end{"+environment+"}")
    assert source.count(text)==1
    first=source[:source.index(text)].count("\n")+1
    span=(first,first+text.count("\n"))
    assert span==expected_span
    assert sha256(text.encode()).hexdigest()==expected_hash
    return text,span

sold,sspan=released("statement","theorem",(15830,15976),
                   "d17a7a503c52f37a45e1f34f60ed0715b121c59d9bd20bd1ab89dac35b258e2b")
pold,pspan=released("proof","proof",(15979,16237),
                   "0a874668ebf1d1b43130bd5f7d31c521be1f604a3c8a9cab94431528fd03e327")
new=(LANE/(BASE+"receiving.tex")).read_text().rstrip("\n")
assert sha256((new+"\n").encode()).hexdigest()=="7335b8346e3e8258e0b194bc8ecae9301bb91a0e28d9d3ba96a3b01942954246"
snew,pnew=new.split(r"\begin{proof}",1)
snew=snew.rstrip("\n")
pnew=r"\begin{proof}"+pnew
assert snew.endswith(r"\end{theorem}") and pnew.endswith(r"\end{proof}")

def identities(text):
    return tuple(sorted(re.findall(pattern,text)) for pattern in (
        r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\tag\{([^}]+)\}"))
assert identities(sold)==identities(snew)
assert identities(pold)==identities(pnew)
assert len(identities(new)[0])==13 and len(identities(new)[2])==12
print("PASS exact separate theorem guard 15830-15976 and proof guard 15979-16237.")
print("PASS all 13 permanent labels/targets and 12 equation tags preserved by their separate guards.")

def write_tsv(suffix,fields,rows):
    stream=io.StringIO(newline="")
    writer=csv.DictWriter(stream,fields,delimiter="\t",lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    (LANE/(BASE+suffix+".tsv")).write_text(stream.getvalue(),newline="\n")

reason=(
"Full fresh main frozen 02:04:14 UTC with separate example supplement completed "
"02:21:18 UTC, fully root-reviewed before individual LD release "
"2026-11-25T02:23:46.236890Z. Whole original theorem and all fifteen auxiliary "
"proof items compared. All homology, group and all-parameter formulas stand. "
"D26 makes the broad 495 finite-good scope and all-star-original 459 subset "
"explicit through their exact inclusion/retraction and all 36 changed patterns. "
"Supply actual period-cover, primitive exterior, original/Mumford, projected "
"finite, normal Thom, fundamental-group and relative maps with inverses. "
"Prove original 436-factor and D=0 certificate claims anew, including the full "
"weighted cusp H2 quotient and finite-first D.WP11/D.WP12 sequences. "
"Historical exact program/certificate bytes are absent; no historical execution "
"or bytewise comparison claimed. Preserve every permanent identity. "
"Root record admission and canonical/unit/build/page stages remain separate."
)
replacements=[]
for kind,before,after,span in (("theorem",sold,snew,sspan),("proof",pold,pnew,pspan)):
    replacements.append(dict(statement_id=ID,old_text=before,new_text=after,
                             reason=f"Separate exact {kind} guard at lines {span[0]}-{span[1]}. "+reason))
write_tsv("replacements",["statement_id","old_text","new_text","reason"],replacements)
trial=source
for row in replacements:
    assert trial.count(row["old_text"])==1
    trial=trial.replace(row["old_text"],row["new_text"],1)
assert canonical.read_bytes()==canonical_bytes
print("PASS both exact replacements apply once in memory; canonical bytes unchanged.")

def between(text,start,end):
    assert text.count(start)==1,(start,text.count(start))
    i=text.index(start)
    j=text.index(end,i+len(start))
    return text[i:j].rstrip("\n")

defects=[]
def defect(suffix,kind,before,after,why):
    matches=[(text,span) for text,span in ((sold,sspan),(pold,pspan)) if before in text]
    assert len(matches)==1,(suffix,"old excerpt absent or spans both guards")
    old,span=matches[0]
    assert old.count(before)==1,(suffix,"old excerpt is not unique within its guard")
    assert new.count(after)==1,(suffix,"new excerpt absent or ambiguous",new.count(after))
    old_line=span[0]+old[:old.index(before)].count("\n")
    new_line=1+new[:new.index(after)].count("\n")
    assert span[0]<=old_line<=span[1]
    defects.append(dict(
        change_id="c7-III-02LD-"+suffix,type=kind,statement_id=ID,
        old_location=f"S6_SERIES_PUBLISH_III.tex:{old_line}",old_page="",
        new_location=str((LANE/(BASE+"receiving.tex")).relative_to(ROOT))+f":{new_line}",
        new_page="",old_text=before,new_text=after,reason=why,
        review_status="proposed; root mathematical reading complete; record admission, canonical application and final page review pending"))

defect("title","D16",sold.splitlines()[0],snew.splitlines()[0],
       "Use the short capitalized mathematical title, preserving the theorem target and label.")
defect("header","D10",next(x for x in sold.splitlines() if x.startswith(r"\StatementRecord")),
       r"\textup{\small(tag 02LD)}",
       "Move machine dependency/status apparatus out of the theorem while keeping the permanent printed tag.")
defect("starred-scope","D26",
       between(sold,"Every original/Mumford choice represented", "Write $A_i$"),
       between(snew,"The $495$ initial presentation patterns","Use the lattice"),
       "The full original leaves the finite-good III*/IV* scope ambiguous while naming 495 patterns. State the proved broad 495 set and all-star-original 459 subset with their exact inclusion/retraction; all 36 omitted patterns and local kernel changes are proved. No displayed formula is refuted.")
defect("iteration-wording","D08",
       between(sold,"Iterate its actual contracting translation","Every original/Mumford"),
       between(snew,"Take the $d$th iterate","The $495$"),
       "State the contracting norm iterate and period-subgroup fan directly.")
defect("marked-matrix-notation","D20",
       "Write $A_i$ for the recorded four-dimensional\nmonodromies in the basis $(e_1,e_2,\\delta,\\gamma)$.",
       "Use the lattice\n$\\Lambda=\\mathbb Z\\langle e_1,e_2,\\delta,\\gamma\\rangle$.\nFor the initial monodromies $A_i$ set",
       "Declare the integral marking used by the cover and all subsequent fixed/projected lattice maps.")
defect("wedge-notation","D20",
       r"\omega_d=a e_1^*e_2^*-db\,\delta^*\gamma^*.",
       r"\omega_d=a e_1^*\wedge e_2^*"+"\n"+r"                  -db\,\delta^*\wedge\gamma^*.",
       "Write the alternating functional with explicit exterior products.")
defect("seifert-in-statement","D14",
       between(sold,"The full fundamental group is","Then\n\\["),
       between(snew,"For the logarithms other than","The Betti numbers are"),
       "Place the complete group presentation and gamma-power convention in the theorem before its homology consequences.")
defect("historical-executable","D09",
       between(sold,"The executable",r"\end{theorem}"),
       between(snew,"The two Smith calculations,",r"\end{theorem}"),
       "Replace the unverified historical implementation claim by the exact two integer calculations. The attached metadata lists the historical path but the executable bytes are absent; new programs and their full outputs are disclosed in the comparison.")
defect("machine-enumeration","D10",
       r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
       r"\emph{The cover and its marked period map.}",
       "Use connected mathematical proof paragraphs instead of machine-prefixed enumeration.")
defect("norm-defense","D02",
       "It need not be a whole fibre. This is the prescribed\nnorm linearization, so no unsupported line-bundle\nmodification is being introduced.",
       "Its divisor is\n"+r"\(\sum_{j=0}^{d-1}t_{-jQ}^{\,*}\operatorname{div}(u)\), with"+"\nall orbit repetitions included.",
       "Give the exact divisor morphism of the norm product, including repetitions, instead of defensive line-bundle language.")
defect("cover-inverses","D22",
       between(pold,"Outside the finite replacements","\\item At the unique rank-two zero"),
       between(pnew,r"The inclusion of groups",r"\emph{Raw matrices"),
       "Supply the group quotient, coset inverse sheets, period injection and extension through the unchanged toric charts with their inverse coordinates.")
defect("cusp-period-reason","D22",
       "At the unique rank-two zero the old valuation\nlattice was the full short lattice. Multiplying\none long period by $d$ gives index $d$. The same\nsmooth triangular fan therefore has $d$ copies\nof the old normalized $dP_6$ in its quotient.",
       between(pnew,r"At the selected fibre \(I_{n_*}\)",r"The normalization complex"),
       "Give the determinant-one short-column matrix and actual d-period subgroup that produce the d normalized components.")
defect("rankone-certificate","D09",
       between(pold,"The exact factorization certificate","Thus the respective component counts"),
       between(pnew,r"\emph{Zero-Chern multiplicative caps",r"\emph{Every finite-good"),
       "Replace the absent historical certificate dependency by explicit primitive factors, full period changes and inverses; the new program recomputes all 436 factors and weighted content identities.")
defect("relative-diffeomorphism-disclaimer","D11",
       "Zero-degree original multiplicative caps\nhave the same component count and the same global\nkernel image; no relative diffeomorphism is asserted.",
       "Thus\nthe original and Mumford alternatives have the same\nmarked boundary kernel and the same primitive cap\nimage, through those explicit maps.",
       "State the positive marked homology-diagram maps used by the algorithm.")
defect("central-core-map","D20",
       "An original zero-degree additive cap is\n$S^1_\\delta$ times the mapping torus of the Kodaira\ntree under $Q^d$.",
       between(pnew,r"Let \(K_0\subset N\)",r"Let \(U_j\)"),
       "Use the Kodaira neighbourhood in the geometric cap model and identify the central-core homology through its translation-compatible inclusion and Wang map, with inverse component coordinates.")
defect("primitive-original-components","D22",
       between(pold,"At a nonzero-Chern original, $Q$","All these caps have"),
       between(pnew,r"\emph{Nonzero-Chern original additive caps.}",r"\emph{Multiplicative caps"),
       "Supply the original line-bundle isotopy, product map and inverse, primitive Chern-kernel basis, fibre generator and full normal/fibre columns at every weight.")
defect("zero-certificate","D09",
       between(pold,"There is a finite exact certificate","\\item Here is why"),
       between(pnew,r"\emph{The constant specialization.}",r"\emph{The integral graph splitting.}"),
       "Replace the absent constant-matrix JSON by exact image and quotient maps. Newly computed Smith lists are (1,1,a) and (1,1,1,1,a) on all 172 rows; retain the original prime-support claim in the full comparison.")
defect("unbounded-integer-coordinates","D20",
       "The two common coinvariants are therefore free\nof ranks one and one for every allowed $d$.\nMoreover \\eqref{maps:eq:D.WP3} is primitive since\n$\\gcd(a,db)=1$, so it is their actual integral\ndegree-two functional.",
       between(pnew,r"Let \(G_d\) be the first three rows",r"\emph{The constant specialization.}"),
       "Give all-d degree-one right inverses and complete wedge-kernel coordinates with inverse maps. The original local-prime argument is separately rederived and remains valid.")
defect("integral-class-input","D14",
       between(pold,"On the\noriginal regular piece","Primitivity of"),
       between(pnew,"We use the integral exterior fibre class","The edge projection"),
       "Use the admitted all-172-row exterior class at its proven scope and construct the integral UCT class before pulling it through the actual cover.")
defect("form-descent-defense","D02",
       "This is a pullback of an\nalready marked class, not an assumption that\nan invariant differential form descends integrally.",
       r"\(\xi_d=p_d^*\xi_1\), with fibre restriction \(\omega_d\). A marked"+"\nweight-d fixed sweep maps to the weight-one sweep with period\n"+r"\(S_d\lambda\); hence its \(\xi_d\) value is zero.",
       "State the pullback map and its evaluations directly.")
defect("projected-lattice-inverses","D20",
       between(pold,"For a finite-good matrix","\\item The full normal Thom image"),
       between(pnew,r"Let \(A=A_i(d)\)",r"\emph{The torsion and the normal character.}"),
       "Give the fixed/projection coordinates, their section, the actual affine and holomorphic conjugacies, every-power fixed-point inverse and the all-d primitive finite examples.")
defect("thom-root-inverse","D20",
       between(pold,"The full normal Thom image","These are complete integral coordinates"),
       between(pnew,r"\emph{Full normal Thom columns",r"\emph{Regular logarithms"),
       "Specify the root boundary map, sector decomposition and inverse, root torus, primitive relation, core torsion and full Thom kernel.")
defect("torsion-defense","D02",
       "These are complete integral coordinates\nin the free target \\eqref{maps:eq:D.WP10}, so a local torsion\nambiguity cannot be lost by this computation.",
       between(pnew,r"The boundary \(H_2\) is free",r"\emph{Regular logarithms"),
       "Explain the actual torsion generator, its zero Thom image and the surjective boundary map to the full core H2.")
defect("quotient-form-defense","D02",
       "In particular no claim of integral form descent\non the finite quotient is needed.",
       "Its Bockstein is the integral normal Chern class;\ntherefore that class has exact order t and no free\ncomponent.",
       "State the normal character and integral Chern-order computation positively.")
defect("weighted-cusp-boundary","D22",
       between(pold,"At the rank-two zero, the two primitive","At a\nrank-one cap"),
       between(pnew,r"Write \(S_{\mathrm{bas}}=(u,\delta)\)",r"Put \(W_d=V_d\cup N_d\)"),
       "Prove H2(boundary)=Z^6 with complete wedge relations, quotient, section and inverse; retain H1's Z/d and use the primitive angular kernel plus relative rank bound.")
defect("additive-specialization","D20",
       "At an original zero-degree additive cap the\nKodaira-tree permutation model supplies the whole\nfibre and the transverse area, the full two\ndimensional coinvariant.",
       between(pnew,r"Let \(U_j\)",r"For \(\mathrm{III}^*\)"),
       "Give the primitive orbit-fibre vector, complete integral fibre map, Bezout section, component complement and both fixed-normal bounding chains.")
defect("logarithm-marking","D20",
       "For a nonzero-Chern original, the marked logarithm\nvectors scale by $d$.",
       "Here \\(dbz\\) is integral and \\(g_0=1\\). Use the unimodular\nperiod matrix \\(R_d=(e_1,e_2,\\delta,\\ell_d)\\), whose inverse\nadds \\(dbz\\) times the last coordinate to the elliptic part.",
       "Distinguish the elliptic logarithm d*z_Q from the full marked period ell_d; the exact relation is S_d ell_d=d ell_1, with the integral H_d inverse. Kernel values scale by d as claimed.")
defect("multiplicative-rim-scope","D20",
       "Their complete fixed normal projections still\nbound, and the third multiplicative correction\nis still annihilated by $\\omega_d$.",
       between(pnew,"The marked geometric normal torus of u","Thus the complete global kernel"),
       "Keep the geometric normal section's rim correction, bounding projection and zero long coordinate, with the inverse shear and exact zero omega_d value; arbitrary Wang sections require their additional displayed shears.")
defect("finite-first-relative-map","D22",
       between(pold,"First attach only the finite","\\item Now attach all the remaining"),
       between(pnew,"Attach the k finite","For each remaining original"),
       "Supply the full m_i x_i-chi(v_i)gamma relative columns, independent base coordinates and inverse, retaining the intermediate H1 torsion.")
defect("relative-sequence-section","D22",
       between(pold,"Now attach all the remaining","\\item If there are $s$"),
       between(pnew,"For each remaining original","Denote the component-disc"),
       "Give every H4 component rank, actual multiplicity-disc boundary, the full relative kernel, and the integer [M,-P] algorithm with a geometric splitting and inverse.")
defect("unfilled-count-notation","D20",
       between(pold,"If there are $s$ unfilled caps","\\item Over the rationals"),
       between(pnew,"Denote the component-disc",r"\emph{The full group"),
       "Distinguish the unfilled-cap count s_unf from the fibre generator s and retain exact torsion-index coordinates in the free relative kernel of rank d-1+beta+L+r.")
defect("rational-graph-coordinate-map","D20",
       between(pold,"Over the rationals \\eqref{maps:eq:D.WP2}","\\item The fundamental-group"),
       between(pnew,r"\emph{The free rank of the full boundary cokernel.}",r"\emph{Euler characteristic"),
       "Give the explicit blockwise S_d rational isomorphism, identity-site inverse, single delta relation and exact Euler coefficient after the integral torsion calculation.")
defect("vertical-and-star-words","D22",
       between(pold,"The fundamental-group argument","Finally $\\chi=2d$"),
       between(pnew,r"\emph{The nonabelian vertical quotient.}",r"\emph{The free rank"),
       "Give every vertical quotient and reverse map, the two retained-star exceptional words, deck-path normal forms, norm-lift changes and complete Seifert presentation.")
defect("duality-coordinates","D22",
       "Finally $\\chi=2d$ and integral duality give\nthe remainder of \\eqref{maps:eq:D.WP8}--\\eqref{maps:eq:D.WP9}.",
       between(pnew,r"\emph{Euler characteristic and integral duality.}",r"\emph{Enumeration"),
       "Give Euler additivity, the free ranks and the torsion-character/Bockstein maps with inverse evaluation, including the d=1 identity specialization.")
defect("neron-accent","D23",
       "Equivalently\nuse the same toric or Neron-logarithm section\ndisc and its actual invariant circle actions.",
       "The fixed sweeps of \\(\\delta\\) and \\(\\ell_d\\) bound respectively the\nextending line-circle tube and the q-fold orbit tube closed\nby the identity-component translation logarithm.",
       "Use the explicit extending logarithm tube and its boundary period; remove the unaccented bare Neron name.")
fields=["change_id","type","statement_id","old_location","old_page","new_location","new_page",
        "old_text","new_text","reason","review_status"]
write_tsv("defects",fields,defects)
assert len(defects)==35,len(defects)
assert sum(x["type"]=="D26" for x in defects)==1
assert not any(x["type"] in ("D25","D27") for x in defects)
print("PASS 35 complete correction rows; one D26 scope clarification; no D25 or D27.")
for d in defects:
    print("DEFECT",d["type"],d["change_id"],d["old_location"],"->",d["new_location"])

fresh_where=[str((LANE/(BASE+x)).relative_to(ROOT)) for x in frozen]
fresh_where+=[
    str((LANE/(BASE+"fresh_source_scope.md")).relative_to(ROOT)),
    "agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02LD_fresh_root_review.md",
]
fresh_where += ["code/S6_SERIES_PUBLISH_c7_ld_"+x for x in frozen_code]
post_where=[str((LANE/(BASE+x)).relative_to(ROOT)) for x in (
"released_statement.tex","released_proof.tex","post_exposure_derivation.md",
"post_exposure_data.json","comparison.md","receiving.tex","replacements.tsv","defects.tsv")]
post_where += ["code/S6_SERIES_PUBLISH_c7_ld_"+x for x in (
"post_exposure.py","post_exposure.out","receiver.py","receiver.out",
"receiver_check.py","receiver_check.out")]
assert all((ROOT/p).exists() for p in fresh_where+post_where)
now=datetime.now(timezone.utc).isoformat()
common=dict(statement_id=ID,date="2026-11-25",
    who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed",
    source_file="S6_SERIES_PUBLISH_III.tex",source_row=sspan[0],
    evidence_group="publish:c7:III:02LD:check-sequence",
    publish_input_file=str((LANE/(BASE+"comparison.md")).relative_to(ROOT)),
    publish_input_row=1,date_utc=now)
events=[
dict(common,type="targeted proof check",
    event_id="publish:c7:III:02LD:fresh-complete-derivation",
    phase="before whole original LD exposure",source_event_type="targeted proof check",
    where="; ".join(fresh_where),
    outcome=(
    "Complete LD statement-only derivation from the disclosed defining profile fixture and "
    "admitted dependencies. Main proof frozen 02:04:14 UTC; separate projected-example "
    "supplement completed 02:21:18 UTC and fully reviewed before individual LD release "
    "2026-11-25T02:23:46.236890Z. Proved actual d-period cover and pullback class, complete "
    "primitive all-d exterior maps, component permutation inverse exponents, every original/"
    "Mumford map, finite projected lattice and every-power freeness, all five Thom columns, "
    "full Seifert inverses, global torsion and every homology group. Derived 172 rows, 495 "
    "patterns and exact 459 subset with 36 projection records, 1728 representatives and "
    "4242 complete group/matrix cases. The supplement proves delta+ell projected primitivity "
    "for every allowed d from both signs at all 102 weight-one positions. Whole new sources "
    "and complete outputs read. LD original and historical weighted target computation "
    "remained closed during this derivation. Post-exposure auxiliary calculations receive "
    "no pre-exposure credit.")),
dict(common,type="used and rechecked in this run",
    event_id="publish:c7:III:02LD:whole-original-comparison",
    phase="after whole original LD exposure",source_event_type="used and rechecked in this run",
    where="; ".join(fresh_where+post_where),
    outcome=(
    "After individual release, read the entire original theorem and all fifteen proof items, "
    "all twelve displays and every auxiliary/computation assertion. Whole receiver and "
    "comparison are complete. Recomputed all 436 primitive rank-one factors, all 172 full "
    "D=0 matrix pairs with exact Smith lists (1,1,a)/(1,1,1,1,a), and all-d cusp Wang "
    "quotient/section identities. Derived the finite-first relative sequence D.WP11 and "
    "free kernel D.WP12 with exact component-disc, power and inverse splitting maps; "
    "retained boundary and finite-core torsion. The original prime argument, central-core "
    "inclusion, logarithm/period scaling, geometric rim scope and all group claims are "
    "settled. D26 makes the broad 495 finite-good family and all-star-original 459 subset "
    "explicit by inclusion/retraction; all formulas stand. No unambiguous false mathematical "
    "assertion or D25/D27 identified. Historical program/certificate bytes absent, with "
    "no historical execution or bytewise comparison claimed. All new source/output read. "
    "Two exact separate guards, 35 correction rows, 13 labels/targets and 12 equation tags "
    "verified. Syntax/data checks give no TeX/PDF/build, unit or page credit. Root record "
    "admission and canonical application remain separate. No extra independent-blind credit.")),
]
event_fields=["statement_id","date","who","type","outcome","event_id","phase","source_file",
              "source_row","source_event_type","evidence_group","publish_input_file",
              "publish_input_row","date_utc","where"]
write_tsv("CHECK_EVENTS",event_fields,events)
assert len({x["evidence_group"] for x in events})==1
assert canonical.read_bytes()==canonical_bytes
print("PASS two narrowly typed event proposals share one evidence group; no extra blind credit.")
print("PASS all proposal writes confined to the LD lane; no canonical/global mutation.")
print("RECEIVER_SHA256",sha256((LANE/(BASE+"receiving.tex")).read_bytes()).hexdigest())
print("COMPARISON_SHA256",sha256((LANE/(BASE+"comparison.md")).read_bytes()).hexdigest())
print("PACKET_COMPLETE_UTC",now)

