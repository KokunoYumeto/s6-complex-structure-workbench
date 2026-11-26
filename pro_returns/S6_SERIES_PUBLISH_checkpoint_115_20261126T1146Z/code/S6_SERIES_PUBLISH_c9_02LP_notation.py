#!/usr/bin/env python3
"""Stage scoped 02LP names after complete source reading; no master writes."""
from pathlib import Path
import csv
from datetime import datetime, timezone
import difflib
import hashlib
import io
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "S6_SERIES_PUBLISH_III.tex"
OUT = ROOT / "agents/continuation9_02LP_notation"
SID = "maps:src:D.2.48"
EXPECTED = "cc40b15bd43061116aa029ac5d64bc22f2698f77e816c497c1227275bc96c72c"


def main():
    original_bytes = SOURCE.read_bytes()
    source = original_bytes.decode()
    t = source.index(r"\label{" + SID + "}")
    a = source.rfind(r"\begin{theorem}", 0, t)
    b = source.index(r"\end{proof}", t) + len(r"\end{proof}")
    baseline = source[a:b]
    assert hashlib.sha256(baseline.encode()).hexdigest() == EXPECTED
    candidate = baseline
    history = []
    substitutions = []

    def literal(text, old, new):
        n = text.count(old)
        assert n, old
        substitutions.append((old, new, n))
        return text.replace(old, new)

    def literals(pairs):
        def transform(text):
            for old, new in pairs:
                text = literal(text, old, new)
            return text
        return transform

    def symbols(pairs):
        replacements = dict(pairs)
        pattern = re.compile(r"(?<![A-Za-z\\])(?:" + "|".join(map(re.escape, replacements)) + r")(?![A-Za-z_])")
        def transform(text):
            protected = r"(\\(?:label|hypertarget|[Cc]ref|[Ee]qref|ref|cite)(?:\[[^]]*\])?\{[^{}]+\})"
            pieces = re.split(protected, text)
            editable = pieces[::2]
            for old, new in pairs:
                n = sum(len(re.findall(r"(?<![A-Za-z\\])" + re.escape(old) + r"(?![A-Za-z_])", part)) for part in editable)
                assert n, old
                substitutions.append((old, new, n))
            pieces[::2] = [pattern.sub(lambda m: replacements[m[0]], part) for part in editable]
            return "".join(pieces)
        return transform

    def operation(name, begin, end, transform, reason, kind="D20"):
        nonlocal candidate
        left = candidate.index(begin)
        right = candidate.index(end, left) if end else len(candidate)
        before = candidate[left:right]
        first_sub = len(substitutions)
        after = transform(before)
        assert before != after, name
        assert candidate.count(before) == 1
        line_start = candidate.count("\n", 0, left) + 1
        baseline_lines = baseline.splitlines()
        current_lines = candidate.splitlines()
        origins = {}
        for action, i1, i2, j1, j2 in difflib.SequenceMatcher(a=baseline_lines,b=current_lines,autojunk=False).get_opcodes():
            for j in range(j1,j2):
                origins[j+1] = {i1+j-j1+1} if action == "equal" else set(range(i1+1,max(i2,i1+1)+1))
        changed = set()
        for action, i1, i2, _, _ in difflib.SequenceMatcher(a=before.splitlines(), b=after.splitlines(), autojunk=False).get_opcodes():
            if action != "equal":
                for line in range(line_start+i1, line_start+max(i2, i1+1)):
                    changed.update(origins.get(line,{len(baseline_lines)}))
        candidate = candidate[:left] + after + candidate[right:]
        history.append(dict(name=name, before=before, after=after, reason=reason,
                            kind=kind, changed_lines=changed, substitutions=substitutions[first_sub:]))

    operation("normal-columns", "the six relation columns", "Every common divisor",
              literals([(f"C_{{{i}{j}}}", f"C^{{\\rm nor}}_{{{i}{j}}}") for i in (0,1) for j in (1,2,3)]),
              "C^nor_ij is the same one of the six displayed columns in the ordered target (s,t,t'_0,t'_1), with every integer entry unchanged. The identity on the six source basis vectors and four target coordinates gives both comparison directions. The final incidence scalars have their own name below.")
    operation("normal-matrix", "Let $B$ be the six-column", "Let $E$ be the exterior",
              literals([(r"Let $B$", r"Let $B_{\rm nor}$"), (r"BR_d", r"B_{\rm nor}R_d"),
                        (r"BR_t", r"B_{\rm nor}R_t"), (r"of $B$", r"of $B_{\rm nor}$"),
                        (r"\operatorname{coker}B", r"\operatorname{coker}B_{\rm nor}")]),
              "B_nor=B is the unchanged four-by-six normal-column matrix. Its images of R_d,R_t, first-coordinate divisibility and cokernel map all retain exactly that matrix. The comparison fixes source and target bases.")
    def normal_bezout(text):
        text = literal(text, "B_0", r"b_{\rm nor}")
        text = literal(text, "A", r"a_{\rm nor}")
        text = literal(text, "$q=", r"$q_{\rm nor}=")
        return literal(text, "+qR_d", r"+q_{\rm nor}R_d")
    operation("normal-bezout-coefficients", "Choose $A,B_0$", "Then $B_{\\rm nor}R_t",
              normal_bezout,
              "a_nor=A and b_nor=B_0 are the original two Bezout integers satisfying -kA+2ell B_0=1; q_nor=q is their stated integer 2A n_0+3B_0 n_1. All products in R_t change names together; the scalar identities and relation preimage are unchanged.")
    operation("exceptional-basis-names", "The notation in the statement is", "In the toric chain construction",
              literals([("$E_1=E_B,E_2=E_C,E_3=E_A$, with inverse\n$E_A=E_3,E_B=E_1,E_C=E_2$.",
                         "$E_1=E_B,E_2=E_C,E_3=E_A$.")]),
              "The retained ordered-basis assignment (E_1,E_2,E_3)=(E_B,E_C,E_A) is the same cyclic permutation. Its inverse sends (E_A,E_B,E_C) to (E_3,E_1,E_2), and both composites fix each exceptional class. Only the redundant prose repeating the inverse names is removed; the subsequent nontrivial toric chain/period maps and their inverses remain.", "D08")
    operation("nilpotent-return", "In the positive period basis", "Since $\\xi_d$",
              symbols([("N", r"N_{\rm mon}")]),
              "N_mon=N is the same nilpotent period return with N_mon b=a and N_mon gamma_d=d delta. The three occurrences retain those lattice maps. The finite subgroup order N and later detector N_det have separate domains.")
    operation("core-base-loop", "Let $W$ consist", "For the core monodromies",
              literals([(r"\langle\gamma,x\mid[\gamma,x]=1\rangle", r"\langle\gamma,x_{\rm bas}\mid[\gamma,x_{\rm bas}]=1\rangle"),
                        (r"\gamma^ux^v", r"\gamma^ux_{\rm bas}^v")]),
              "x_bas=x is the same second generator of pi_1(W)=Z². The presentation, exponent map and inverse reading of exponents are unchanged.")
    operation("quadratic-refinement", "For the core monodromies", "For the cusp write",
              literals([(r"q(\lambda)", r"q_\xi(\lambda)")]),
              "q_xi=q is the stated quadratic refinement Lambda→Z/2 whose polarization is xi mod2. Its formula and occurrence in the line cocycle use the identical function, with no change to the invariant polynomial check.")
    def real_period(text):
        text = literal(text, r"A_ix", r"A_i x_{\rm per}")
        text = literal(text, r"dx)", r"d x_{\rm per})")
        return symbols([("x", r"x_{\rm per}")])(text)
    operation("real-period-point", "For the core monodromies", "Use $\\phi(r,s)", real_period,
              "x_per=x is the real universal-cover point in the lattice line cocycle, its connection and the cusp real-period decomposition. The map is identity on that real vector space; all lattice translations, scalar lifts and connection arguments, including dx_per, change together.")
    def cusp_matrices(text):
        for old,new in [("U",r"u_{\rm per}"),("V",r"v_{\rm per}"),("K",r"K_{\rm pol}"),("B",r"B_{\rm hol}")]:
            text = literal(text,old,new)
        return text
    operation("cusp-period-coordinates", "For the cusp write", "Use $\\phi(r,s)", cusp_matrices,
              "u_per=U and v_per=V are the same two real coordinate columns; K_pol=K=diag(1,-6d) is the same polarization matrix; B_hol=B(q_base) is the same holomorphic matrix of period units. The expressions x_per=(a,delta)u_per+(b,gamma)v_per, Z=u_per+Omega v_per, Gaussian, symmetry and base-return substitution change names in every occurrence. The coordinate identity and its inverse fix both columns and both matrices.")
    def support(text):
        pairs=[("(r,s)",r"(r_{\rm tor},s_{\rm tor})"),
               ("-r(r-1)/2+3s^2",r"-r_{\rm tor}(r_{\rm tor}-1)/2+3s_{\rm tor}^2"),
               ("(r+1,s)",r"(r_{\rm tor}+1,s_{\rm tor})"),
               ("=-r$",r"=-r_{\rm tor}$"),
               ("(r,s+d)",r"(r_{\rm tor},s_{\rm tor}+d)"),
               ("=6ds+3d^2",r"=6d s_{\rm tor}+3d^2"),
               (r"-\frac{r(r-1)}2+3s(s-1)",r"-\frac{r_{\rm tor}(r_{\rm tor}-1)}2+3s_{\rm tor}(s_{\rm tor}-1)"),
               ("-3s.",r"-3s_{\rm tor}."), (r"\lambda_s",r"\lambda_2")]
        text = literals(pairs)(text)
        return literal(text,
                       r" \psi(r_{\rm tor},s_{\rm tor})=-\frac{r_{\rm tor}(r_{\rm tor}-1)}2+3s_{\rm tor}(s_{\rm tor}-1)=\phi(r_{\rm tor},s_{\rm tor})-3s_{\rm tor}.",
                       " \\begin{aligned}\n \\psi(r_{\\rm tor},s_{\\rm tor})&=-\\frac{r_{\\rm tor}(r_{\\rm tor}-1)}2+3s_{\\rm tor}(s_{\\rm tor}-1)\\\\\n &=\\phi(r_{\\rm tor},s_{\\rm tor})-3s_{\\rm tor}.\n \\end{aligned}")
    operation("toric-support-coordinates", "Use $\\phi(r,s)", "The weight-$d$ core", support,
              "(r_tor,s_tor)=(r,s) is identity on the same integral fan lattice. Both support functions and each period difference retain exactly the original values; lambda_2 is the same exponent of q_base in the z_2 period. The generator s of Tor H_2 and rank r=d-1 remain unchanged. The monomial line map zeta_psi=z_2^-3 zeta_phi and its reciprocal are preserved.")
    operation("universal-quadratic-map", "The quadratic generator has relations", "For the degree-six generator",
              literals([("q(",r"q_{\rm quad}(")]),
              "q_quad is the same universal quadratic coordinate used in the two defining relations and j↦j² mod D_2 detector. The identity substitution fixes its generator and values, while q_xi names the earlier lattice refinement.")
    operation("magnetic-real-point", "For every $N\\mid6d$", "Its commutator with",
              symbols([("x",r"x_{\rm per}")]),
              "The magnetic lift acts on the same real cover point x_per as the line cocycle. Its translation by delta/N and phase xi(delta/N,x_per) are unchanged.")
    operation("support-reprise", "Thus the global finite class", "The degree on every vertical",
              literals([("(r,s)",r"(r_{\rm tor},s_{\rm tor})"), ("-3s.",r"-3s_{\rm tor}.")]),
              "This repeated support identity uses the same renamed fan coordinates as WI17; its common linear character and restriction of u are unchanged.")
    operation("curve-generator", r"\item \emph{The common Borel character.}", r"\item \emph{The full third-power operation.}",
              symbols([("x",r"x_C")]),
              "x_C=x is the positive degree-two generator on a fixed curve, with evaluation one. Its Borel restriction uses the same class and character; the real period point is separately x_per.")
    operation("curve-euler-class", r"\item \emph{Localization at the full third-power modulus.}", r"\item \emph{The pure cyclic coordinate.}",
              symbols([("x",r"x_C")]),
              "The normal Euler calculation uses the same fixed-curve class x_C and x_C²=0; the factors (-x_C+t)(-x_C-t), sign and localization result are unchanged.")
    def detector_name(text):
        text = literal(text, "TN", r"TN_{\rm det}")
        return symbols([("N",r"N_{\rm det}")])(text)
    operation("detector-three-manifold", "Its connected fibre $N$", r"\item \emph{Complete marked oriented recognition.}", detector_name,
              "N_det=N is the same connected fibre of the primitive character chi in the finite cap. Every tangent projection, homology/spin/parity calculation, orientation, linking, odd multiple, surgery comparison and bounding-chain order refers to this detector under identity. The finite subgroup order N and nilpotent N_mon are outside this scope; the embedded surgery sphere remains described as the surgery image, with no new identification asserted.")
    def base_kernel(text):
        text = literal(text, r"\eta", r"\eta_{\rm bas}")
        text = symbols([("q",r"q_{\rm ker}"),("h",r"h_{\rm ker}"),("t",r"t_{\rm ker}"),("K",r"b_{\rm ker}")])(text)
        # Adjacent scalar-vector products are distinct literal targets.
        for old,new in [(r"Kh",r"b_{\rm ker}h_{\rm ker}"),
                        (r"Kn_1",r"b_{\rm ker}n_1")]:
            if old in text:
                text = literal(text,old,new)
        return text
    operation("detector-base-kernel", "order-four elliptic monodromy", "The elliptic\nmonodromy", base_kernel,
              "eta_bas=eta is the finite-cap base direction [u_1], distinct in name from the earlier component class eta=-5H+6E_1-E_3. q_ker=eta_bas-b_chi beta and h_ker=g-c_chi beta are the same base-kernel vectors; t_ker=a_ker q_ker+b_ker h_ker is the same primitive generator and b_ker=K the same Bezout integer/root exponent. All forward and inverse base coordinates retain the displayed integer relation m_1h_ker=n_1q_ker.")
    operation("detector-smith-matrices", "An affine translation in this return", "Every determinant is one",
              symbols([("A",r"A_{\rm ell}"),("U",r"U_{\rm snf}"),("V",r"V_{\rm snf}")]),
              "A_ell is the same order-four elliptic return (or its inverse). U_snf,V_snf are the unchanged determinant-one Smith row/column matrices, with the same adjugate inverses and diag(1,2) reduction. Their entries and the affine conjugating map are unchanged.")
    def spin_degrees(text):
        return literals([("A",r"d_L"),("B",r"d_R")])(text)
    operation("spin-factor-degrees", "Evaluation on $[N_{\\rm det}]$ gives", "These are precisely the first-column", spin_degrees,
              "d_L=A and d_R=B are the two integer degrees of the SU(2)_L and SU(2)_R maps. The collapse construction, first-column degree d_L-d_R and stable parity d_L+d_R are the identical integer maps; neither degree is a matrix or a Bezout coefficient.")
    operation("detector-parity", r"\item \emph{The tangent-parallelization parity.}", r"\item \emph{Complete marked oriented recognition.}",
              literals([(r"\epsilon",r"\epsilon_{\rm det}")]),
              "epsilon_det=epsilon is the same detector's stable framing parity in Z/2. Its value one, frame-degree congruence and linking half all change names together. The earlier epsilon=±1 describing circle orientation is unchanged.")
    operation("quaternion-sphere-coordinates", "For $q=a+xi+yj+zk$", "is the nontrivial class relative",
              literals([("For $q=a+xi+yj+zk$ and $t_1=qi,t_2=qj,t_3=qk$, the frame",
                         "For $q_{\\mathbb H}=a_{\\mathbb H}+x_{\\mathbb H}i+y_{\\mathbb H}j+z_{\\mathbb H}k$, put\n\\[\n t_{{\\mathbb H},1}=q_{\\mathbb H}i,\\qquad t_{{\\mathbb H},2}=q_{\\mathbb H}j,\\qquad t_{{\\mathbb H},3}=q_{\\mathbb H}k.\n\\]\nThe frame"),
                        ("(-a e_3-x t_1-y t_2-z t_3,e_1,e_2)",r"(-a_{\mathbb H} e_3-x_{\mathbb H} t_{{\mathbb H},1}-y_{\mathbb H} t_{{\mathbb H},2}-z_{\mathbb H} t_{{\mathbb H},3},e_1,e_2)")]),
              "q_H=q is the same unit quaternion, with (a_H,x_H,y_H,z_H)=(a,x,y,z) identity on R⁴ and t_H,j the same three tangent products qi,qj,qk. The coefficient map and displayed three-frame retain all signs and terms; the degree and extension assertions are unchanged.")
    operation("complement-obstruction", "Thus $\\sigma/\\rho$", r"\item \emph{Complete marked oriented recognition.}",
              literals([(r"q_0",r"d_\rho"),("2q+",r"2q_{\rm ref}+"),("Here $q$",r"Here $q_{\rm ref}$"),(r"$q/\operatorname",r"$q_{\rm ref}/\operatorname")]),
              "d_rho=q_0 is the integral Spin(6) comparison degree, and q_ref=q is the complementary obstruction cochain evaluation. Their obstruction equality, parity and linking quotient use the same integers and the same Poincare-duality map; base, quaternion and quadratic uses of q are separately named.")
    operation("classifying-map", r"\item \emph{Complete marked oriented recognition.}", None,
              literals([(r"f_X",r"f_{\rm cls}")]),
              "f_cls is the same classifying map X→K(A_d,2) for the inverse marking. Its refined invariant P(f_cls) is unchanged. The original holomorphic fibration f_X and its differential/point pullback retain their name in the preceding proof.")
    operation("incidence-coefficients", r"\item \emph{Complete marked oriented recognition.}", None,
              literals([(r"C_{ij}",r"c^{\rm inc}_{ij}")]),
              "c^inc_ij=C_ij is exactly the cyclic incidence scalar from WI3, including both directed incidences at d=2. The coefficient of gamma_ij(e)g in mu_d is unchanged, while the six normal columns are C^nor_ij.")

    inverse = candidate
    for item in reversed(history):
        assert inverse.count(item["after"]) == 1, item["name"]
        inverse = inverse.replace(item["after"],item["before"],1)
    assert inverse == baseline
    for pattern in [r"\\(?:label|hypertarget)\{[^{}]+\}",r"\\(?:[Cc]ref|[Ee]qref|ref|cite)(?:\[[^]]*\])?\{[^{}]+\}"]:
        assert re.findall(pattern,baseline) == re.findall(pattern,candidate)
    assert "\r" not in candidate
    old_lines,new_lines=baseline.splitlines(keepends=True),candidate.splitlines(keepends=True)
    matcher=difflib.SequenceMatcher(a=old_lines,b=new_lines,autojunk=False)
    for context in range(1,9):
        groups=list(matcher.get_grouped_opcodes(context))
        fragments=[("".join(old_lines[g[0][1]:g[-1][2]]),"".join(new_lines[g[0][3]:g[-1][4]])) for g in groups]
        if all(source.count(old)==1 for old,new in fragments):break
    else:raise AssertionError("No unique exact fragments")
    fields=next(csv.reader(io.StringIO((ROOT/"S6_SERIES_PUBLISH_defects_III.tsv").read_text()),delimiter="\t"))
    rows=[];rebuilt=source
    for i,((old,new),group) in enumerate(zip(fragments,groups),1):
        assert rebuilt.count(old)==1
        rebuilt=rebuilt.replace(old,new,1)
        lines=set(range(group[0][1]+1,group[-1][2]+1))
        applies=[x for x in history if x["changed_lines"] & lines]
        rows.append(dict(change_id=f"CLAUDE-III-C9-PDF-02LP-{i:03d}",type=";".join(sorted(set(x["kind"] for x in applies))) or "D20",
                         statement_id=SID,old_location="02LP complete statement/proof; exact pre-edit fragment",old_page="candidate02 physical 523–533 (root images); own full source read",
                         new_location="same statement/proof and permanent labels",new_page="pending rebuilt image review",old_text=old,new_text=new,
                         reason=" ".join(dict.fromkeys(x["reason"] for x in applies)) or "Exact bounded name substitution from the complete reversible map table.",
                         review_status="Complete 935-line theorem/proof read; exact inverse restores baseline; source/matrix coefficients and labels preserved. Root admission and rebuilt PDF reading pending."))
    assert rebuilt==source[:a]+candidate+source[b:]
    assert SOURCE.read_bytes()==original_bytes
    OUT.mkdir(parents=True,exist_ok=True)
    p=OUT/"S6_SERIES_PUBLISH_c9_02LP_notation_defects.tsv"
    with p.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)
    (OUT/"S6_SERIES_PUBLISH_c9_02LP_notation.diff").write_text("".join(difflib.unified_diff(old_lines,new_lines,fromfile="02LP before",tofile="02LP proposed",n=3)),encoding="utf-8",newline="\n")
    # Full candidate is a temporary review intermediate outside the checkpoint.
    tmp=ROOT.parents[1]/"tmp/c9_02LP_notation"
    tmp.mkdir(parents=True,exist_ok=True)
    (tmp/"S6_SERIES_PUBLISH_c9_02LP_proposed.tex").write_text(candidate,encoding="utf-8",newline="\n")
    event_fields=next(csv.reader(io.StringIO((ROOT/"CHECK_EVENTS.tsv").read_text()),delimiter="\t"))
    event={k:"" for k in event_fields}
    event.update(statement_id=SID,date="2026-11-26",who="GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; continuation nine",type="used and rechecked in this run",
                 event_id="publish:c9:III:02LP:full-notation-context",phase="publication continuation 9",source_file=str(SOURCE.relative_to(ROOT)),source_row="complete 02LP theorem/proof",
                 source_event_type="used and rechecked in this run",evidence_group="publish:c9:III:02LP:full-notation-context",publish_input_file="../CLAUDE_READING_LOG_PAPER_III.md",publish_input_row="P11/P15; candidate02 image findings from root",
                 date_utc=datetime.now(timezone.utc).isoformat(),where="code/S6_SERIES_PUBLISH_c9_02LP_notation.py; agents/continuation9_02LP_notation/",
                 outcome="Read the entire 935-line 02LP statement/proof after exposure to root's candidate02 physical 523–533 image findings. Traced each overloaded normal-matrix, Bezout, period, fan, quadratic, fixed-curve, detector, Smith, quaternion, obstruction and classifying-map name through its complete semantic scope and later uses. Prepared reversible identity substitutions and removed only the redundant inverse exceptional-class renaming. Exact reverse application recovers every baseline byte; labels, tags, references, matrix entries, mathematical maps and assertions are preserved. This exposed proof-context repair adds no independent re-proof or page-reading credit; root admission and rebuilt image review remain pending.")
    with (OUT/"S6_SERIES_PUBLISH_c9_02LP_notation_CHECK_EVENTS.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,event_fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerow(event)
    print("Baseline",len(old_lines),EXPECTED)
    print("Proposed",len(new_lines),hashlib.sha256(candidate.encode()).hexdigest())
    print("Scoped operations",len(history),"unique fragments",len(rows),"context",context)
    for item in history:
        print(item["name"],"|",item["kind"],"|",item["reason"])
        for old,new,n in item["substitutions"]:print("  exact target count",n,repr(old),"→",repr(new))
    print("Complete inverse comparison passed; all labels/tags/references unchanged; canonical bytes unchanged.")
    print("Candidate for full readback:",tmp/"S6_SERIES_PUBLISH_c9_02LP_proposed.tex")
    print("Staged defects:",p.relative_to(ROOT))


if __name__=="__main__":main()
