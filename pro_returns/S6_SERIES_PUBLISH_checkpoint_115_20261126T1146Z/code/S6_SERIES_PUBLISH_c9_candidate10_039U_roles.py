#!/usr/bin/env python3
"""Prepare bounded 039U role guards; never write canonical manuscript/records."""
from pathlib import Path
import csv
import difflib
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "S6_SERIES_PUBLISH_III.tex"
EXPECTED = "5a95d62059fcaf7859df33f5793d9cd97462024d50a1f7ee59f9fae0b2704187"
STEM = "S6_SERIES_PUBLISH_c9_candidate10_039U_roles"
OUT = ROOT / "agents/continuation9_candidate10_039U_roles"
TMP = ROOT.parents[1] / "tmp/c9_candidate10_039U_roles"
OWNER = "wb:cusp-spec-globalization-obstruction"
UNIT = "mapsIII:sec:regular-quotients"
REVIEW = f"agents/continuation9_candidate10_039U_roles/{STEM}_review.md"
ROOT_FINDING = "agents/continuation9_root/S6_SERIES_PUBLISH_c9_candidate10_new_source_findings.md"
IMAGE_REVIEW = "agents/continuation9_reading_thirdquarter/S6_SERIES_PUBLISH_c9_candidate10_pages526_614_review.md"
DEFECT_FIELDS = ["change_id", "type", "statement_id", "old_location", "old_page",
                 "new_location", "new_page", "old_text", "new_text", "reason", "review_status"]
EVENT_FIELDS = ["statement_id", "date", "who", "type", "outcome", "event_id", "phase",
                "source_file", "source_row", "source_event_type", "evidence_group",
                "publish_input_file", "publish_input_row", "date_utc", "where"]
MATH = re.compile(r"\\begin\{equation\}.*?\\end\{equation\}|\\\(.*?\\\)|\\\[.*?\\\]|\$(?:\\.|[^$])*\$", re.S)


def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()


def tsv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: str(row[k]).replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")
                             if k in {"old_text", "new_text"} else row[k] for k in fields})


def main():
    src = SOURCE.read_text()
    assert sha(src) == EXPECTED and "\r" not in src
    start = src.index(r"\begin{theorem}[Global circle quotients and compactification obstructions]")
    stop = src.index(r"\end{proof}", start) + len(r"\end{proof}")
    baseline = src[start:stop] + "\n"
    assert len(baseline.splitlines()) == 952
    rows, checks = [], []

    def block(first, last):
        assert baseline.count(first) == 1 and baseline.count(last) == 1
        lo = baseline.index(first)
        hi = baseline.index(last, lo) + len(last)
        return baseline[lo:hi]

    def rename(fragment, names):
        """Rename declared TeX tokens only inside mathematical containers."""
        counts = {old: 0 for old, new in names}
        def convert(match):
            value = match.group(0)
            for old, new in names:
                pattern = r"(?<![A-Za-z\\])" + re.escape(old) + r"(?![A-Za-z_])"
                value, number = re.subn(pattern, lambda _: new, value)
                counts[old] += number
            return value
        changed = MATH.sub(convert, fragment)
        assert all(counts.values()), counts
        reverse = changed
        for old, new in reversed(names):
            reverse = reverse.replace(new, old)
        assert reverse == fragment
        return changed, counts

    def add(old, new, title, reason, names=(), clauses=(), prose=(), occurrences=None):
        assert old != new and src.count(old) == 1
        reverted = new
        for clause in clauses:
            assert reverted.count(clause) == 1
            reverted = reverted.replace(clause, "", 1)
        for before, after in reversed(prose):
            assert reverted.count(after) == 1
            reverted = reverted.replace(after, before, 1)
        for before, after in reversed(names):
            reverted = reverted.replace(after, before)
        assert reverted == old, title
        number = len(rows) + 1
        cid = f"III-C9-CURRENT10-039U-ROLE-{number:03d}"
        line = src[:src.index(old)].count("\n") + 1
        rows.append(dict(change_id=cid, type="D20", statement_id=OWNER,
            old_location=f"039U complete statement/proof, source {line}: {title}",
            old_page="Current10 image triggers614–617 (root); backend actually read614; this guard compared in the complete source owner",
            new_location=f"Same full owner and maps: {title}",
            new_page="pending successor build and actual changed-page reading",
            old_text=old, new_text=new,
            reason=reason + " Full typed occurrence/inverse and caller comparison: " + REVIEW,
            review_status="proposed; complete exposed original/proposed owner and actual caller comparison; no independent credit; root admission and changed-page gate pending"))
        checks.append(dict(change_id=cid, title=title, source_line=line,
            literal_name_inverse=True, role_maps=[dict(old=a,new=b) for a,b in names],
            occurrence_counts=occurrences or {}, added_binding_clauses=list(clauses),
            prose_bindings=[dict(old=a,new=b) for a,b in prose]))

    old = block("For $A_{\\rm tor}=(\\mathbb R/\\mathbb Z)^2$ or $\\mathbb R/\\mathbb Z$, the\n",
                "$S^1\\times A_{\\rm tor}$ recovers the fixed quotient coordinate and has no\n")
    names = [("a", r"a_{\rm cone}")]
    new, counts = rename(old, names)
    add(old, new, "Statement cone input",
        "The cone angular input is a_cone in A_tor. The coordinate rename is the identity on A_tor, with literal inverse to a. The projection [r,z,a_cone]->a_cone and the proof's fixed-slice section give exact coordinate recovery; no inverse of the whole projection is asserted. The same qualified input is propagated through the proof.", names, occurrences=counts)

    old = block("The fixed product-target trivialization does not extend over \\(X\\), even if\n",
                "of the regular character, even after changing its winding on the base.\n")
    names = [("n", r"n_{\rm att}"), ("a", r"a_{\rm att}"), ("b", r"b_{\rm att}")]
    new, counts = rename(old, names)
    add(old, new, "Selected attachment homomorphism coordinates",
        "For the chosen homomorphism, n_att is its value on gamma_hat, a_att and b_att are its values on rho_hat_1 and rho_hat_2, and the restriction to Lambda is n_att epsilon_gamma. The coordinate map (n,a,b)->(n_att,a_att,b_att) is the integer identity, with inverse forgetting the suffixes. The presentation reconstructs the homomorphism from this triple; all three relations, both substitutions and n_att/12=0 are retained exactly. This chosen attachment integer is thereby qualified against the formal product/exponent inputs.", names, occurrences=counts)

    old = block("For \\(a=(a_1,a_2)^{\\mathsf T}\\in\\mathbb R^2\\), take the point of the\n",
                " \\hypertarget{tag-0395}{}\\label{wb:cusp-spec-cusp-nonextension-character}\n\\end{equation}\n")
    names = [("a_1", r"a_{1,\rm tor}"), ("a_2", r"a_{2,\rm tor}"), ("a", r"a_{\rm tor}")]
    new, counts = rename(old, names)
    assert new.count("Z_Ta") == 2
    new = new.replace("Z_Ta", r"Z_Ta_{\rm tor}")
    counts["Z_Ta"] = 2
    add(old, new, "Toric path family and its component coordinates",
        "The parameter identity (a_1,a_2)->a_tor=(a_{1,tor},a_{2,tor}) has inverse extraction of those two ordered real coordinates. Its marked insertion is a_{1,tor} gamma_hat+a_{2,tor} u_hat with zero short coordinates. The same Z_T, exponential, logarithmic-position map and character evaluation are composed with this identity. The exponential itself is not claimed to have a global inverse.", names, occurrences=counts)

    old = block("The prescribed fan consists of the integer translates of\n",
                "point and hence to the same triple point of \\(W\\).\n")
    names = [("e_1", r"e_{1,\rm fan}"), ("e_2", r"e_{2,\rm fan}"), ("a", r"a_{\rm tor}")]
    new, counts = rename(old, names)
    replacements = [("sI", r"s_{\rm cusp}I"), ("sB_0", r"s_{\rm cusp}B_0")]
    for before, after in replacements:
        assert new.count(before) > 0
        new = new.replace(before, after)
    names += [("s", r"s_{\rm cusp}")]
    binding = ("Let \\(e_{1,\\rm fan},e_{2,\\rm fan}\\) be the ordered standard basis\n"
               "of this two-dimensional fan lattice \\(\\mathbb Z^2\\). Use the logarithmic\n"
               "base coordinate \\(s_{\\rm cusp}\\), with \\(t=e^{2\\pi i s_{\\rm cusp}}\\);\n"
               "on the positive radial ray choose \\(s_{\\rm cusp}=iT\\), so \\(t=t_c\\).\n")
    new = binding + new
    add(old, new, "Typed fan columns and native long-period transport",
        "The fan vectors e_{i,fan} are the same ordered standard columns of Z2, while the earlier physical e_1,e_3 remain in R4. Insertion (m_1,m_2)->m_1 gamma_hat+m_2 u_hat and extraction of the first two marked coefficients identify the long-period domain. The existing transport a_native=B_0 a_tor has inverse B_0^{-1}; the entire block-matrix identity keeps the physical complex coordinate fixed. The old logarithmic base input is s_cusp=s from Q019 and equation original-periods; t=exp(2pi i s_cusp), with chosen positive-ray lift iT. On that branch the inverse is Log(t)/(2pi i); no global inverse of the exponential is asserted. All fan cells, toric chart entries and limits are identical.", names, clauses=[binding], occurrences={**counts,"sI":2,"sB_0":1})

    old = block("Take\n\\[\n a=\\left(-\\frac14,\\frac14\\right),\\qquad\n",
                " \\chi_{\\gamma,T}(x_T(a'))=\\frac12.\n\\]\n")
    names = [("a", r"a_{\rm tor}")]
    new, counts = rename(old, names)
    new = new.replace("Take\n", "Evaluate the same path family at\n", 1)
    add(old, new, "The two actual parameter evaluations",
        "These are the same two displayed inputs to x_T, now explicitly evaluations of the preceding a_tor family. The identity sends the original a,a' to a_tor,a_tor' with identical four rational entries. B_0 sends them to the same two fan positions, and the character values remain 3/4 and1/2. The inverse returns the original input names; no path, limit or selected value changes.", names, prose=[("Take\n","Evaluate the same path family at\n")], occurrences=counts)

    old = block("The radial family of translations by \\(\\widehat u/2\\) in \\(\\mathcal H\\)\n",
                "no continuous extension to \\(N_0\\).\n")
    names = [("y", r"y_{\rm tr}"), ("e_1", r"e_{1,\rm fan}"), ("e_2", r"e_{2,\rm fan}")]
    new, counts = rename(old, names)
    add(old, new, "Translation-limit pair and all fan-column uses",
        "The selected y_tr,y_tr' are the unchanged limiting real position vectors (1/8,1/8) and (3/8,3/8). They are obtained from the existing path family by inputs B_0^{-1}y_tr and B_0^{-1}y_tr', so B_0 followed by B_0^{-1} is the explicit coordinate inverse. The half-u_hat displacement uses the same second long-period column e_{2,fan}; every triangle uses the same qualified fan basis. All translated pairs, cell barycentres and integral deck-translation comparison are retained.", names, occurrences=counts)

    old = block("diffeomorphism $h_0:X\\to S^6$. For a fixed fibre inclusion choose\n",
                "Thus $h=O_{\\rm rot}h_0$ is based, with inverse $h_0^{-1}O_{\\rm rot}^{\\mathsf T}$.\n")
    names = [("b", "b_6"), ("c", r"c_{\rm rot}"), ("s", r"s_{\rm rot}"), ("w", r"w_{\rm rot}")]
    new, counts = rename(old, names)
    assert new.count(r"\\s&") == 1
    new = new.replace(r"\\s&", r"\\s_{\rm rot}&")
    counts["matrix_row_s"] = 1
    binding = ("Write $b_d$ for the north pole of $S^d$, indexed by its sphere dimension $d$.\n")
    before = "diffeomorphism $h_0:X\\to S^6$. For a fixed fibre inclusion choose\n"
    after = "diffeomorphism $h_0:X\\to S^6$.\n" + binding + "For a fixed fibre inclusion choose\n"
    new = new.replace(before, after, 1)
    pole_before = "its zero $x_0$ as basepoint, and let ${p_{\\rm sph}}=h_0(x_0)$ and $b$ be the\n"
    pole_after = "its zero $x_0$ as basepoint, and let ${p_{\\rm sph}}=h_0(x_0)$. Use $b_6$, the\n"
    assert new.count(pole_before.replace("$b$", "$b_6$")) == 1
    new = new.replace(pole_before.replace("$b$", "$b_6$"), pole_after, 1)
    add(old, new, "Dimension-indexed pole and selected rotation coordinates",
        "The pole family b_d is indexed by the same sphere dimension; b_6 is its evaluation in the displayed S6. The selected rotation coordinates are c_rot=<p_sph,b_6>, s_rot=sqrt(1-c_rot^2), w_rot=(b_6-c_rot p_sph)/s_rot, with the original piecewise choices at the two poles. The coefficient identity and its inverse preserve the same plane matrix; c_rot p_sph+s_rot w_rot=b_6, the perpendicular action is the identity and the inverse is the transpose. Public h_0, O_rot and h=O_rot h_0 and their inverse remain literally named as before. This qualifies the pole, root-disc s and solid-torus w roles without changing any geometric map.", names, prose=[(before,after),(pole_before,pole_after)], occurrences=counts)

    old = block("In dimension $d$, let $b$ denote the north pole of $S^d$.\n",
                "the two displayed substitutions are inverse.\n")
    names = [("b", "b_d"), ("a", r"a_{\rm st}")]
    new, counts = rename(old, names)
    # The product ab is two adjacent TeX scalar tokens; qualify it explicitly.
    assert new.count("x=ab+v") == 1
    new = new.replace("x=ab+v", r"x=a_{\rm st}b_d+v")
    before = "In dimension $d$, let $b_d$ denote the north pole of $S^d$.\n"
    after = "In dimension $d$, use the same pole $b_d$.\n"
    assert new.count(before) == 1
    new = new.replace(before, after, 1)
    add(old, new, "Stereographic scalar and the same indexed pole family",
        "The scalar a_st is the formal coordinate <x,b_d> in x=a_st b_d+v, with v=x-a_st b_d perpendicular to b_d. Projection is v/(1-a_st); the unchanged inverse gives a_st=(||y||^2-1)/(1+||y||^2), v=2y/(1+||y||^2). Thus coordinate extraction and reconstruction are explicit; b_d corresponds to infinity. At d=6 this is the same pole b_6 used by h, and at d=4 it supplies the later target-cube compactification. The inverse qualification returns the original stereographic formulas exactly.", names,
        prose=[("In dimension $d$, let $b$ denote the north pole of $S^d$.\n", "In dimension $d$, use the same pole $b_d$.\n")], occurrences={**counts,"product_ab":1})

    old = block("For $A_{\\rm tor}=(\\mathbb R/\\mathbb Z)^2$ or $\\mathbb R/\\mathbb Z$, form\n",
                "that vertex is therefore impossible.\n")
    names = [("a", r"a_{\rm cone}")]
    new, counts = rename(old, names)
    add(old, new, "Cone projection, fixed-slice section and the selected pair",
        "The whole cone angular input family uses a_cone in A_tor, agreeing with the statement. For fixed admissible r_0,z_0 the section s(a_cone)=[r_0,z_0,a_cone] has p_cone o s=id, and s o p_cone is the identity on that fixed slice. The two selected inputs a_cone,a_cone' are the same original pair under the identity of A_tor. The radial paths, their common vertex and constant projections are unchanged, with the same literal inverse name map.", names, occurrences=counts)

    old = block("Over \\(t\\ne0\\), choose one root \\(s\\) of \\(t\\), adjust each representative\n",
                "action. This is its holomorphic inverse.\n")
    names = [("t", "t_j")]
    new, counts = rename(old, names)
    assert counts == {"t": 2}
    add(old, new, "The defined finite base coordinate in the normalization inverse",
        "Item(iv) already defines the base coordinate t_j=s^{m_j} on D_j. These two finite-normalization inputs are exactly that t_j, while the later t is the cusp base coordinate. The identity from the old finite-coordinate slot t to t_j, with inverse t_j->t on this power-map input, preserves s->s^{m_j}, every cyclic adjustment and the residual diagonal quotient. No root or covering choice is changed, and the inverse formula remains the same holomorphic map.", names, occurrences=counts)

    candidate = src
    for row in rows:
        assert candidate.count(row["old_text"]) == 1
        candidate = candidate.replace(row["old_text"], row["new_text"], 1)
        assert candidate.count(row["new_text"]) == 1
    reverse = candidate
    for row in reversed(rows):
        assert reverse.count(row["new_text"]) == 1
        reverse = reverse.replace(row["new_text"], row["old_text"], 1)
    assert reverse == src
    proposed = candidate[start:candidate.index(r"\end{proof}",start)+len(r"\end{proof}")] + "\n"
    target_re = r"\\(?:label|hypertarget|(?:c|eq|C|Series)?ref)\{[^}]+\}|\\(?:begin|end)\{[^}]+\}"
    assert re.findall(target_re, src) == re.findall(target_re, candidate)
    assert candidate[:start] == src[:start]
    assert candidate[candidate.index(r"\end{proof}",start)+len(r"\end{proof}"):] == src[stop:]
    assert sha(SOURCE.read_text()) == EXPECTED
    OUT.mkdir(parents=True,exist_ok=True)
    TMP.mkdir(parents=True,exist_ok=True)
    original_path = TMP / f"{STEM}_original.tex"
    proposed_path = TMP / f"{STEM}_proposed.tex"
    original_path.write_text(baseline,encoding="utf-8",newline="\n")
    proposed_path.write_text(proposed,encoding="utf-8",newline="\n")
    payload = dict(source_file=SOURCE.name, source_sha256=EXPECTED, proposed_source_sha256=sha(candidate),
        owner_scope=dict(statement_id=OWNER, containing_unit=UNIT, original_lines=len(baseline.splitlines()),
            proposed_lines=len(proposed.splitlines()), original_sha256=sha(baseline), proposed_sha256=sha(proposed),
            original_path=str(original_path), proposed_path=str(proposed_path)),
        proposals=rows, validation=checks)
    (OUT/f"{STEM}.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    (OUT/f"{STEM}.diff").write_text("".join(difflib.unified_diff(src.splitlines(keepends=True),candidate.splitlines(keepends=True),
        fromfile=SOURCE.name,tofile=SOURCE.name+".proposed",n=3)),encoding="utf-8",newline="\n")
    tsv(OUT/f"{STEM}_defects.tsv",rows,DEFECT_FIELDS)
    now = datetime.now(timezone.utc).isoformat()
    eid = "publish:c9:III:039U:full-proof-roles"
    event = dict(statement_id=OWNER,date=now[:10],who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine",
        type="used and rechecked in this run",
        outcome=f"Read the complete {len(baseline.splitlines())}-line current 039U statement/proof and its complete proposed scope, Q310/Q311, the exact period-input definitions, and all 22 external citation sites in their caller paragraphs. Rechecked the marked attachment evaluation/reconstruction, toric/native coordinate inverse, typed fan insertion/extraction, actual path evaluations, positive-ray logarithmic lift, rotation and transpose inverse, stereographic coordinates and inverse, cone projection/section, and the defined finite-base input of the normalization inverse. The complete role inventory documents retained formal inputs by exact domains, evaluation/coordinate-recovery and literal alpha-renaming maps. All public maps, labelled conclusions, numerical entries and caller interfaces are retained. This is exposed comparison following root's actual current10 pages614–617 and backend page614; no independent proof or additional image credit. Root admission and successor changed-page gates remain pending.",
        event_id=eid,phase="publication continuation9",source_file=SOURCE.name,
        source_row="039U complete statement/proof; " + "; ".join(r["change_id"] for r in rows),
        source_event_type="used and rechecked in this run",evidence_group=eid,
        publish_input_file="../CLAUDE_READING_LOG_PAPER_III.md",
        publish_input_row="P15; prompt0.8 complete proof scope; root current10 pages614–617",
        date_utc=now,where=f"code/{STEM}.py; code/{STEM}.out; {REVIEW}; agents/continuation9_candidate10_039U_roles/{STEM}_defects.tsv; {ROOT_FINDING}; {IMAGE_REVIEW}")
    with (OUT/f"{STEM}_events.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=EVENT_FIELDS,delimiter="\t",lineterminator="\n");w.writeheader();w.writerow(event)
    print(json.dumps({k:v for k,v in payload.items() if k not in {"proposals","validation"}},indent=2))
    print("Unique forward/reverse guards, complete source reversal, every declared role-name inverse, ordered targets and environment sequence PASS.")
    print("All source outside the complete 039U owner is byte-identical; canonical source/records/events/counts/statuses untouched.")
    print(f"D20 guards {len(rows)}; exposed owner associations1; caller guards0.")
    for check in checks:
        print(json.dumps(check,ensure_ascii=False))


if __name__ == "__main__":
    main()
