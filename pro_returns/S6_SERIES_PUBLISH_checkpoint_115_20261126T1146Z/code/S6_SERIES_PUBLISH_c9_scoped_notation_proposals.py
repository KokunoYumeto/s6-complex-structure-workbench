#!/usr/bin/env python3
"""Further context-read P15 corrections; writes only guarded agent proposals.

Every replacement is a reversible name map on a specifically read proof block.
Displayed environments as well as inline math are handled; targets and citations
are preserved. Shared manuscript and tables are left for root admission.
"""
from collections import Counter
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from zipfile import ZipFile

from S6_SERIES_PUBLISH_c8_III_check_counts import parse_statements

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / "agents/continuation9_global_sweep"
SOURCE = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text(encoding="utf-8")
OWNERS, _, _ = parse_statements(SOURCE)
PROPOSALS = []


def statement(sid):
    o = next(o for o in OWNERS if o.statement_id == sid)
    return SOURCE[o.start:o.stop]


def between(t, start, end, include_end=False):
    pattern = lambda q: r"\s+".join(re.escape(w) for w in q.split())
    starts = list(re.finditer(pattern(start), t))
    assert len(starts) == 1, (start, len(starts))
    a = starts[0].start()
    stop = re.search(pattern(end), t[starts[0].end():])
    assert stop is not None, end
    b = starts[0].end() + (stop.end() if include_end else stop.start())
    return t[a:b]


def brace_end(s, i):
    depth = 1
    j = i + 1
    while depth:
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
        j += 1
    return j


def rename_math(t, mapping, skip_subscript=False):
    literal = {"label", "hypertarget", "ref", "eqref", "cref", "Cref", "SeriesRef", "cite",
               "begin", "end", "text", "textrm", "textit", "textbf", "hbox", "mbox",
               "mathrm", "operatorname", "mathbb", "mathcal", "mathsf", "mathbf", "mathfrak", "mathit"}
    out = []
    i = 0
    while i < len(t):
        if t[i] == "\\":
            token = re.match(r"\\[A-Za-z]+|\\.", t[i:], re.S).group()
            out.append(token); i += len(token)
            name = token[1:]
            if name in literal:
                while i < len(t) and t[i].isspace():
                    out.append(t[i]); i += 1
                if i < len(t) and t[i] == "{":
                    j = brace_end(t, i); out.append(t[i:j]); i = j
                elif name.startswith("math") and i < len(t):
                    out.append(t[i]); i += 1
            continue
        c = t[i]
        if c in mapping and not (skip_subscript and i+1 < len(t) and t[i+1] == "_"):
            out.append("{" + mapping[c] + "}")
        else:
            out.append(c)
        i += 1
    return "".join(out)


MATH = re.compile(r"\$[^$]*\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}", re.S)


def add(name, sid, old, new, reason, inverse):
    assert SOURCE.count(old) == 1 and old != new, (name, SOURCE.count(old))
    assert inverse(new) == old, (name, "reverse name map")
    p = SOURCE.index(old)
    owners = [o for o in OWNERS if o.start <= p and p+len(old) <= o.stop]
    assert len(owners) == 1 and owners[0].statement_id == sid, (name, "formal owner")
    controls = r"\\(?:label|hypertarget|ref|eqref|cref|Cref|SeriesRef|cite)\s*(?:\[[^]]*\])?\{[^{}]*\}"
    assert Counter(re.findall(controls, old)) == Counter(re.findall(controls, new)), (name, "target/reference change")
    PROPOSALS.append(dict(name=name, finding="P15", statement_id=sid, tag=owners[0].tag,
        source_line=SOURCE.count("\n", 0, p)+1, old=old, new=new, reason=reason))


def names(name, sid, old, mapping, reason, skip_subscript=False, protected=(), extra=()):
    t = old
    holds = {}
    for i, word in enumerate(protected):
        assert word in t, (name, word)
        hold = r"\operatorname{SsixHold" + str(i) + "}"
        assert hold not in t
        holds[word] = hold
        t = t.replace(word, hold)
    new = MATH.sub(lambda m: rename_math(m.group(), mapping, skip_subscript), t)
    for word, hold in holds.items():
        new = new.replace(hold, word)
    for a, b in extra:
        assert a in new, (name, a)
        new = new.replace(a, b)
    def inverse(s):
        for a, b in reversed(extra):
            s = s.replace(b, a)
        for a, b in mapping.items():
            s = s.replace("{" + b + "}", a)
        return s
    add(name, sid, old, new, reason, inverse)


def prepare():
    sid = "maps:src:D.2.13"; t = statement(sid)
    old = between(t, "At a type-$II$ point put $d=H_0'(a)$", "Thus the point splits into two $I_1$ fibres.", True)
    names("02KN-discriminant-derivative", sid, old, {"d": r"d_{\rm disc}"},
        "The proof later uses d=gcd(m,a,b) in its integral splitting and a bound d in a Smith summand. The local derivative H_0'(a) receives d_disc, with the same three numerical values and the identical polynomial 1-27 d_disc^2 z^2. The analytic splitting argument is unchanged; the reverse name map fixes each germ and coefficient.")

    sid = "maps:src:D.2.25"; t = statement(sid)
    old = between(t, "Let $S$ be the Seifert relation matrix", "Form an integral presentation")
    names("02L0-Seifert-matrix-statement", sid, old, {"S": r"\mathsf S_{\rm Sei}"},
        "S is also the persistent primitive short basis (u,delta) in this proof. The Seifert relation matrix is now mathsf S_Sei; it has exactly the same rows, cokernel and rank r. This name is propagated to both proof references in the following two proposals.")
    old = "Call this matrix \\(S\\), and write its Smith cokernel as"
    names("02L0-Seifert-matrix-proof", sid, old, {"S": r"\mathsf S_{\rm Sei}"},
        "This defines the same Seifert matrix as the statement: rows (-n_i,0,...,m_i,...,0) and (-e,1,...,1). The reverse matrix-name map recovers the original declaration, and the short basis S remains unchanged.")
    old = "It is the transpose of the row convention for \\(S\\)."
    names("02L0-Seifert-matrix-relative-reference", sid, old, {"S": r"\mathsf S_{\rm Sei}"},
        "The reduced normal-disc matrix is the transpose of that same Seifert relation matrix. Only its name is updated to the declaration above; every row, orientation and unit elimination remains unchanged.")
    old = between(t, "For each row of the displayed complete list, integer elimination gives matrices", "For an arbitrary number $s_\\mathrm{reg}$") if "For an arbitrary number $s_\\mathrm{reg}$" in t else between(t, "For each row of the displayed complete list, integer elimination gives matrices", r"For an arbitrary number \(s_\mathrm{reg}\)")
    names("02L0-integral-graph-left-inverse", sid, old, {"L": "L_K"},
        "L already denotes the complementary period basis (r,gamma); the graph coordinate left inverse is now L_K. The map is the same integer matrix V_K P_17 U_K. Every occurrence in L_K K=I, K L_K(I-C_0D_0)=I-C_0D_0, L_K j_0 delta and the inverse sweep projection is renamed together. Exact reversal recovers the entire block, including every Smith construction and geometric splitting.")
    old = between(t, r"For \(E\ne0\) the kernel is zero.", "Its \\(\\chi\\) coordinate vanishes")
    names("02L0-multiplicity-lcm", sid, old, {"L": r"\ell_{\rm mult}"},
        "The least common multiple of the positive multiplicities is now ell_mult, separating it from the complementary basis L and graph inverse L_K. Its value, the empty-site convention 1, the primitive kernel vector and the residual fibre loop are unchanged. Multiplication, division and prime valuations are identical under the reversible scalar-name map.")

    sid = "maps:src:D.2.31"; t = statement(sid)
    old = between(t, "For the finite sites put", "In particular, \\(s=0\\) is an equality")
    names("02L7-CRT-aggregate-names", sid, old,
        {"F": "F_f", "V": r"v_{\rm reg}", "T": r"t_{\rm reg}",
         "X": r"x_{\rm reg}", "Y": r"y_{\rm reg}", "Z": r"z_{\rm reg}", "N": r"n_{\rm reg}"},
        "The proof uses F for the elliptic fibre, V for the exterior, T for the torsion subgroup, X for the threefold and N for a neighbourhood. In this arithmetic block F_f is the finite product, v_reg is the aggregate regular vector, t_reg its aggregate sweep homomorphism, and x_reg,y_reg,z_reg,n_reg its four coordinates. Each new symbol denotes the identical integer, vector or homomorphism. N_f, D_f, all indexed terms and the actual H_2(X) are protected. The two CRT inverse formulas, determinant identity, Bezout reduction, torsion group and empty-set cases are carried term by term by this exact reversible name map.",
        skip_subscript=True, protected=("H_2(X)",))
    old = "The fixed lattice is\n\\[\n \\operatorname{Fix}(T)=\\mathbb Z\\delta\\oplus\\mathbb Z\\ell,"
    new = "For the marked boundary monodromy $\\mathsf T$, the fixed lattice is\n\\[\n \\operatorname{Fix}(\\mathsf T)=\\mathbb Z\\delta\\oplus\\mathbb Z\\ell,"
    add("02L7-boundary-monodromy-name", sid, old, new,
        "The theorem's T is the torsion group, whereas Fix(T) here means the marked boundary monodromy. Writing mathsf T names that same monodromy matrix explicitly and keeps its fixed vectors unchanged. The identity matrix-coordinate map mathsf T<-T and its reverse transport Fix exactly. Two later bare matrix uses are updated below; the mapping-torus notation T^+ and torsion group T remain.", lambda s: s.replace(new, old))
    old = between(t, "For finite order, \\(N_m\\) is self-adjoint", "These identities show")
    names("02L7-boundary-monodromy-norm", sid, old, {"T": r"\mathsf T"},
        "Both sums are powers of the same boundary monodromy matrix renamed mathsf T. Their equality and the self-adjointness of N_m are unchanged. T for the torsion group elsewhere is untouched.")
    old = between(t, "The selected cusp has the Jordan fan of", "The identity on the punctured rank-one matrix cone")
    names("02L7-cusp-monodromy-reference", sid, old, {"T": r"\mathsf T"},
        "The cusp period equation and H_E^{-1} T H_E conjugacy use the boundary monodromy matrix. That matrix now has the consistent mathsf T name, while T continues to denote the torsion group. The bases S,L, integral C, the fan example and all chart/inverse maps are fixed by the exact matrix-name map.")

    sid = "maps:src:D.2.41"; t = statement(sid)
    old = between(t, "The affine freeness criterion is", "The fixed-plane condition")
    names("02LI-fixed-basis-matrix", sid, old, {"F": r"F_{\rm fix}"},
        "F already names the fibre bar-chain map used in the integral splitting. The later primitive fixed-basis matrix is now F_fix. Its columns, inverse on its image, projected lattice F_fix(H/h)Z^2 and coordinates v=F_fix z remain identical. The analytic freeness argument and its actual affine conjugacy inverses are unchanged.")

    sid = "maps:src:D.2.50"; t = statement(sid)
    old = between(t, "Put $g=\\gcd(n,q)$", "For the other types, the component orders")
    names("02LS-component-orbit-gcd", sid, old, {"g": r"g_{\rm comp}"},
        "The proof subsequently uses g for the marked section cocycle. The earlier orbit-count integer gcd(n,q) is now g_comp. The residue classes, orbit length n/g_comp, augmentation equation, invariant multidegree vector and integral solution all retain their exact values under the reverse scalar-name map.")
    old = between(t, "Write $J$ for this ambient graph map.", "\\item \\emph{The relative map and full fundamental group.}")
    names("02LS-graph-comparison-matrices", sid, old,
        {"J": r"\mathsf J_{\Gamma}", "Q": r"\mathsf Q_{\Gamma}", "M": r"\mathsf M_{\Gamma}"},
        "J already denotes the symplectic matrix, Q the elliptic section, and M the section line. In this graph comparison, mathsf J_Gamma is the ambient word-change matrix, mathsf Q_Gamma its induced kernel-basis matrix, and mathsf M_Gamma the 23-generator row map. The three displayed matrix formulas, all inverse matrices, BC_r=M_Gamma B_o and B_oD_r=M_Gamma^{-1}B are renamed consistently. Their entries, domains, codomains and quotient maps are unchanged. Indexed J_o is retained.", skip_subscript=True)

    sid = "maps:src:D.2.39"; t = statement(sid)
    old = between(t, "Choose $qA+qz_{Q,2}B-qz_{Q,1}C=1$.", "Component transiti")
    new = old.replace("qA+qz_{Q,2}B-qz_{Q,1}C", "qa_0+qz_{Q,2}b_0-qz_{Q,1}c_0").replace("(Ae_{12}+Be_{14}+Ce_{24})", "(a_0e_{12}+b_0e_{14}+c_0e_{24})")
    add("02LF-Bezout-coefficients", sid, old, new,
        "A denotes the monodromy and [C] the component class in this very paragraph; the unindexed Bezout coefficients A,B,C therefore overlap active objects. They become a_0,b_0,c_0 only in the Bezout equation and its section vector. The component class [C], line-frame map S_P and coefficient identities are unchanged. The coefficient map (A,B,C)<->(a_0,b_0,c_0) is coordinatewise identity, so the section and its composites are the identical maps.",
        lambda s: s.replace("qa_0+qz_{Q,2}b_0-qz_{Q,1}c_0", "qA+qz_{Q,2}B-qz_{Q,1}C").replace("(a_0e_{12}+b_0e_{14}+c_0e_{24})", "(Ae_{12}+Be_{14}+Ce_{24})"))
    old = between(t, "Put $A=a(\\nu-k)$", "\\item \\emph{The coefficient-one detector")
    names("02LF-edge-coefficient", sid, old, {"A": r"a_{\rm edge}"},
        "A is the monodromy/linear deck map earlier in this proof. The coefficient a(nu-k) multiplying the fixed-curve class is now a_edge. Its value, mod-three invertibility, the restriction rho_3(a_edge z_C) and inverse class change alpha=a_edge u are unchanged. The same scalar is propagated in the localization terms below.")
    old = between(t, "e_C=\\nu(k-\\nu)T^2", "The action on the elliptic")
    # Include the opening display delimiter so that every A is in a math span.
    a = t.index(old)
    display = t.rfind(r"\[", 0, a)
    assert display >= 0 and t[display:a].strip() == r"\["
    old = t[display:a+len(old)]
    names("02LF-edge-localization-reference", sid, old, {"A": r"a_{\rm edge}"},
        "The localization numerator uses the same coefficient a(nu-k), renamed a_edge in its definition. Its cube, the denominator nu(k-nu), the mod-nine zero value and all weights are unchanged. The genuine equivariant restrictions and Thom localization maps remain.")

    sid = "maps:src:D.3.1"; t = statement(sid)
    old = between(t, "For fixed $u\\ne0$ set", "The punctured\nperiod generators")
    names("02M0-local-node-coordinate", sid, old, {"X": r"\widehat x"},
        "X(u) already denotes the total threefold family. Its local coordinate x/u is now widehat x. The equation, gradient, singular ideal, Hessian, two small-resolution charts, overlaps and toric character cones use the identical scalar coordinate under x/u<->widehat x. The local inverse x=u widehat x is immediate from the defining nonzero u; the geometric family X(u) is unchanged.")

    sid = "wb:cusp-spec-globalization-obstruction"; t = statement(sid)
    old = between(t, "let $p=h_0(x_0)$", "In dimension $d$, let $b$ denote")
    names("039U-sphere-basepoint", sid, old, {"p": r"p_{\rm sph}"},
        "p is already the covering projection in this proof. The later point h_0(x_0) on the sphere is now p_sph. Its coordinates, inner product c, orthogonal vector w, rotation R, exceptional pole cases and based diffeomorphism are the same under the identity map on S^6. The full rotation block was compared with the original; the covering projection retains p.")

    sid = "wb:sphere-metric-tangent-scope"; t = statement(sid)
    old = between(t, "We specify a boundary collar for this product.", "At a point with \\(k\\) boundary factors")
    names("03DF-collar-function", sid, old, {"d": r"d_{\rm col}"},
        "The proof later uses d=dim L in its cone volume calculation. The collar function is now d_col, with the identical values u on the collar and 1 outside. Its superlevel set, minimum on product coordinates, collar map H_t and explicit inverse u=(u'-t)/(1-t) are unchanged. The reverse function-name map recovers every displayed relation; the dimension d retains its meaning.")


def main():
    prepare()
    with ZipFile(ROOT.parents[1] / "upload/S6_SERIES_PUBLISH_continue_cp100.zip") as z:
        original = z.read("S6_SERIES_PUBLISH_checkpoint_100/S6_SERIES_PUBLISH_III.tex").decode("utf-8")
    now = datetime.now(timezone.utc).isoformat()
    df = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
    ef = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
    candidate = SOURCE
    defects, events = [], []
    for i, p in enumerate(PROPOSALS, 1):
        assert candidate.count(p["old"]) == 1, (p["name"], "overlap")
        base_pattern = r"\s+".join(re.escape(w) for w in p["old"].split())
        base_matches = list(re.finditer(base_pattern, original))
        assert len(base_matches) == 1, (p["name"], "original cp100 comparison modulo whitespace", len(base_matches))
        candidate = candidate.replace(p["old"], p["new"], 1)
        cid = f"CLAUDE-III-P15-SCOPED-{i:03d}"
        p["change_id"] = cid
        p["cp100_line"] = original.count("\n", 0, base_matches[0].start())+1
        defects.append(dict(change_id=cid, type="D20", statement_id=p["statement_id"],
            old_location=f"cp100 source line {p['cp100_line']}; tag {p['tag']}",
            old_page="current page concordance pending", new_location="same scoped proof block; "+p["name"],
            new_page="pending current rendered-PDF review", old_text=p["old"], new_text=p["new"], reason=p["reason"],
            review_status="Exact old/new block and relevant surrounding definitions read "+now+"; proposed for root admission; no whole-proof independent-check or PDF-page credit."))
        print(cid, p["statement_id"], p["name"])
    for j, sid in enumerate(dict.fromkeys(p["statement_id"] for p in PROPOSALS), 1):
        names_here = [p["name"] for p in PROPOSALS if p["statement_id"] == sid]
        eid = f"publish:c9:III:scoped-notation:{j:03d}"
        row = {k: "" for k in ef}
        row.update(statement_id=sid, date=now[:10], who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global notation reviewer",
            type="used and rechecked in this run", outcome="Read the original cp100 and current mathematical blocks, their defining contexts and every changed expression for "+", ".join(names_here)+". The symbol maps and their exact inverses are documented in the D20 rows. Every target and citation is preserved, and reversing the guarded substitutions recovers the pre-edit source exactly. This is a scoped comparison, with no claim of an independent proof, whole-proof rereading or PDF-page review.",
            event_id=eid, phase="continuation9 Paper III scoped notation", source_file="code/S6_SERIES_PUBLISH_c9_scoped_notation_proposals.py",
            source_event_type="used and rechecked in this run", evidence_group=eid, date_utc=now,
            where="agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_scoped_notation_proposals.json")
        events.append(row)
    restored = candidate
    for p in reversed(PROPOSALS):
        assert restored.count(p["new"]) == 1, (p["name"], "reverse guard")
        restored = restored.replace(p["new"], p["old"], 1)
    assert restored == SOURCE
    targets = lambda s: Counter(re.findall(r"\\(?:label|hypertarget)\{[^{}]+\}", s))
    assert targets(SOURCE) == targets(candidate)
    (OWN / "S6_SERIES_PUBLISH_c9_scoped_notation_proposals.json").write_text(json.dumps(PROPOSALS, ensure_ascii=False, indent=2)+"\n", encoding="utf-8", newline="\n")
    for name, fields, rows in [("S6_SERIES_PUBLISH_c9_scoped_notation_defects.tsv", df, defects), ("S6_SERIES_PUBLISH_c9_scoped_notation_events.tsv", ef, events)]:
        with (OWN / name).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader(); writer.writerows(rows)
    print(f"Prepared {len(PROPOSALS)} exact notation proposals and {len(events)} scoped events; original guards, formal owners, permanent targets and reverse maps pass.")


if __name__ == "__main__":
    main()
