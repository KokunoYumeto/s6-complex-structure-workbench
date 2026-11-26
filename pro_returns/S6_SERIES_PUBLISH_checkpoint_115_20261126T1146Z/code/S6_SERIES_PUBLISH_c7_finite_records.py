"""Exact individual L4/L6 replacement guards and proposed checking records."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from collections import Counter
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
F = ROOT / "agents/continuation7_iii_finite_general"
FRESH = {
    "S6_SERIES_PUBLISH_III_finite_fresh_local_derivation.md":
        "d87421677b7784e848c5b4b37e6bbecc40ef42c6b3042dc4e6ce56c874b8196a",
    "S6_SERIES_PUBLISH_III_one_finite_fresh_smith.md":
        "179b3aac45d763fb37335257c4bdca4c9110913cd1c8b39ce6cd6aa93ab2c8ef",
    "S6_SERIES_PUBLISH_III_finite_fresh_global_derivation.md":
        "853475804f1890f30c45fda30e4cf61afa951bc12b9e37dab353e0d1899c9794",
}
META = {
    "02L4": ("maps:src:D.2.29", "13529",
        "4b3ce6186cba9a306141000a3c209f6de92ec0afe81c9de8e576cc3b90baa1c4",
        "22:56:00.036851"),
    "02L6": ("maps:src:D.2.30", "13821",
        "d265f86917d9b28bbee21fd7cd382c8e6e299dda15bbab5fcbecad6178398ea1",
        "22:56:00.548989"),
}


def block(text, env):
    a, b = "\\begin{" + env + "}", "\\end{" + env + "}"
    assert text.count(a) == text.count(b) == 1
    return text[text.index(a):text.index(b) + len(b)]


def write(path, fields, rows):
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    with path.open(newline="") as f:
        assert list(csv.DictReader(f, delimiter="\t")) == rows


for filename, digest in FRESH.items():
    assert sha256((F / filename).read_bytes()).hexdigest() == digest
print("PASS all three frozen fresh derivations unchanged.")

for tag, (sid, source_row, old_hash, release_time) in META.items():
    stem = "S6_SERIES_PUBLISH_III_" + tag + "_"
    old_s = block((F / (stem + "released_statement.tex")).read_text(), "theorem")
    old_p = block((F / (stem + "released_proof.tex")).read_text(), "proof")
    assert sha256(old_p.encode()).hexdigest() == old_hash
    item_count = len(re.findall(r"\\item\b", old_p))
    assert item_count == {"02L4": 10, "02L6": 7}[tag]
    print(tag, "original proof items", item_count)
    receiver = F / (stem + "receiving.tex")
    new = receiver.read_text()
    new_s, new_p = block(new, "theorem"), block(new, "proof")
    assert new.rstrip("\n") == new_s + "\n\n" + new_p
    for original, replacement in [(old_s, new_s), (old_p, new_p)]:
        for kind in ["label", "hypertarget", "tag"]:
            pat = r"\\" + kind + r"\{([^{}]+)\}"
            assert Counter(re.findall(pat, original)) == Counter(re.findall(pat, replacement))
    for kind in ["label", "hypertarget", "tag"]:
        found = Counter(re.findall(r"\\" + kind + r"\{([^{}]+)\}", new))
        assert all(v == 1 for v in found.values())
        print(tag, kind, dict(found))
    assert not any(x in new for x in
                   ["\\StatementRecord", "\\SeriesRef", "code/", "records/", ".json", "SHA256"])
    stack = []
    for action, env in re.findall(r"\\(begin|end)\{([^{}]+)\}", new):
        if action == "begin":
            stack.append(env)
        else:
            assert stack and stack.pop() == env
    assert not stack
    depth = 0
    for brace in re.findall(r"(?<!\\)[{}]", new):
        depth += 1 if brace == "{" else -1
        assert depth >= 0
    assert depth == 0
    for p in [receiver, F / (stem + "comparison.md"),
              F / "S6_SERIES_PUBLISH_III_02L4_02L6_post_exposure_derivation.md"]:
        assert b"\r" not in p.read_bytes()

    guards = [
        dict(statement_id=sid, old_text=o, new_text=n,
             reason="Complete fresh derivation and full original/receiver comparison; preserve every identity and supply the marked integral maps and inverses.")
        for o, n in [(old_s, new_s), (old_p, new_p)]
    ]
    guard_path = F / (stem + "replacements.tsv")
    write(guard_path, ["statement_id", "old_text", "new_text", "reason"], guards)
    replay = old_s + "\n\n" + old_p
    for guard in guards:
        assert replay.count(guard["old_text"]) == 1
        replay = replay.replace(guard["old_text"], guard["new_text"], 1)
    assert replay == new.rstrip("\n")
    for guard in reversed(guards):
        assert replay.count(guard["new_text"]) == 1
        replay = replay.replace(guard["new_text"], guard["old_text"], 1)
    assert replay == old_s + "\n\n" + old_p

    common = [
        ("header", "D10", next(x for x in old_s.splitlines() if x.startswith("\\StatementRecord")),
         r"\textnormal{\small tag " + tag + ".}",
         "Remove production header while preserving the permanent theorem and equation identities."),
        ("proof-order", "D10", r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
         r"\begin{proof}",
         "Replace the production-style proof item labels by connected mathematical paragraphs."),
    ]
    if tag == "02L4":
        specs = common + [
            ("local-global-scope", "D26", "These are the $68$ marked finite positions",
             "Their restriction to the nonstar initial rows consists of $62$",
             "State all 68 local primitive-gamma positions and their 62-position nonstar restriction explicitly. The exact marked-tuple inclusion has the six positions listed in the proof as complement."),
            ("retrospective-opening", "D01", r"The restriction $\gcd(m_i,n_i)=1$",
             "Consider the natural initial data",
             "State the complete free-action result directly with its fixed local and global scopes."),
            ("integral-lattice-maps", "D22", "The integral certificates",
             "Here the quotient map is integral:",
             "Give the actual integer quotient, section, inverse and fixed-position inclusion."),
            ("whole-disc-conjugacy", "D22", "the averaging solution is holomorphic on the disc.",
             r"s_0=-\frac1m\sum_{j=0}^{m-1}jR^j b_0",
             "Supply the holomorphic contracting sum, conjugacy and inverse over the entire root disc, with period and normal-unit changes."),
            ("complete-thom-map", "D22", "On the boundary mapping cylinder, their",
             "The marked boundary identification is",
             "Write the boundary map and inverse, all three parametrized Thom tori, complete source, primitive relation, index and inverse Bezout reduction."),
            ("global-cokernel-and-bridge", "D22", "Thus its extension",
             r"(c,k)\longmapsto c+\sum k_i Z_i",
             "Give the exterior/cap quotient and inverse and the integral two-chain section of the free Mayer--Vietoris bridge; retain every torsion group at both Euler ranks."),
        ]
        disposition = (
            "All finite-cap and global homology conclusions stand at explicit scopes. "
            "D26 clarifies 68 primitive-gamma positions on all172 rows versus62 on148 nonstar rows, with exact tuple inclusion and six-position complement. "
            "The complete target was derived before exposure; every original auxiliary assertion was compared, including the whole-disc holomorphic averaging, all172 graph/fibre assertion, all boundary groups, full Thom image, normal index, coprime reduction and zero-Euler bridge. "
        )
    else:
        specs = common + [
            ("retrospective-opening", "D01", "The fixed-$\\gamma$ restriction",
             "Consider all $102$ finite additive positions",
             "State the full local lattice and global filling scopes directly."),
            ("record-path", "D09", r"\path{records/manifolds_all_finite_logs.json}",
             "The minimal original/log choices on the $148$ nonstar rows give",
             "Remove the record path from the theorem and give the mathematical choice rule and all sixteen profile counts in the proof; the independent program belongs in the later program table."),
            ("fixed-coinvariant-inverses", "D22", "These assertions are checked by unimodular Smith operations",
             "Multiplying the quotient map by $C^{-1}$ gives",
             "Supply the literal period matrix, primitive fixed basis and inverse, integral coinvariant quotient and inverse, both norms and all pairings."),
            ("full-normal-kernel", "D22", "their normal-projection index is still $(m/q)t$.",
             "Their projected minors are",
             "Give the complete three-column Thom image, primitive relation, exact projected minor gcd and degree-two surjectivity with cap torsion."),
            ("all-patterns", "D22", "Enumerating these choices gives $198$ patterns",
             "Taking the product of the permitted original/log",
             "State the component/multidegree choice rule, free vector at every order, all sixteen profile counts and the exact inclusion of164 patterns with34-pattern complement."),
            ("one-site-integral-maps", "D22", "Changing $n$ by $(m/g)e$ is exactly a peripheral lift change",
             r"The lift change $c'=c\eta^{-e}$",
             "Give the actual norm-based lift isomorphism and inverse, complete integer elimination, unbounded Bezout/minor proof, zero-Euler coprimality and both quotient inverse maps."),
        ]
        disposition = (
            "All theorem and original auxiliary conclusions stand: all102 finite lattices,68/34 fixed indices, all198 patterns on148 nonstar rows, every free twist and order, all homology degrees, both one-site Euler cases and the full-group obstruction at g>1. "
            "Every original proof item was compared, including all34 literal delta/gamma bases, both boundary Smith assertions, eta/ell pairing, normal index, primitive free vector at every order, norm-based peripheral change and r prime to m at n'=0. No D25/D26/D27 is alleged. "
        )
    defects = []
    for name, kind, old, replacement, why in specs:
        assert old in old_s + old_p, (tag, name, "old")
        assert replacement in new, (tag, name, "new")
        defects.append(dict(
            change_id="c7-III-" + tag + "-" + name, type=kind, statement_id=sid,
            old_location="S6_SERIES_PUBLISH_III.tex; " + sid, old_page="",
            new_location=str(receiver.relative_to(ROOT)), new_page="",
            old_text=old, new_text=replacement, reason=why,
            review_status="whole comparison submitted to root; admission pending"))
    defect_path = F / (stem + "defects.tsv")
    write(defect_path,
          ["change_id", "type", "statement_id", "old_location", "old_page",
           "new_location", "new_page", "old_text", "new_text", "reason", "review_status"],
          defects)
    now = datetime.now(timezone.utc).isoformat()
    event_id = "publish:c7:III:" + tag + ":targeted"
    evidence = [str((F / filename).relative_to(ROOT)) for filename in FRESH]
    evidence += [str((F / (stem + suffix)).relative_to(ROOT)) for suffix in
                 ["released_statement.tex", "released_proof.tex", "receiving.tex",
                  "comparison.md", "replacements.tsv", "defects.tsv"]]
    evidence.append(str((F / "S6_SERIES_PUBLISH_III_02L4_02L6_post_exposure_derivation.md").relative_to(ROOT)))
    evidence += ["code/S6_SERIES_PUBLISH_c7_" + name + ext
                 for name in ["finite_lattices", "one_finite_minors", "finite_patterns",
                              "finite_auxiliary", "l1_post_exposure", "finite_records"]
                 for ext in [".py", ".out"]]
    event = dict(
        statement_id=sid, date=now[:10],
        who="GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; seventh continuation",
        type="targeted proof check",
        outcome=(
            "Complete three-part fresh target derivation frozen22:55:15 UTC before individual release" + release_time + " UTC. "
            + disposition +
            "Frozen fresh auxiliary v+m lambda sentence is explicitly restricted post-exposure to regular/invariant periods; the general finite law v+N_m lambda is proved with inverse. Directly derived target kernels/clutch/minors do not depend on that illustration; frozen bytes unchanged, no extra independent credit. "
            "All new mathematical programs and every output line read, including163200 direct-minor one-site cases,646 boundary checks and2448 auxiliary index examples; universal conclusions have full algebraic/geometric proofs. Historical target algorithms remain unopened/uncredited. "
            "Full original and receiving proof read; exact separate statement/proof guards preserve every permanent identity. One targeted event, no new independent-family count, canonical application, unit, build, page or paper-gate credit; root admission pending."),
        event_id=event_id,
        phase="complete fresh proof, individual release, full original and receiving comparison",
        source_file="S6_SERIES_PUBLISH_III.tex", source_row=source_row,
        source_event_type="targeted proof check", evidence_group=event_id,
        publish_input_file=str((F / (stem + "CHECK_EVENTS.tsv")).relative_to(ROOT)),
        publish_input_row="2", date_utc=now, where="; ".join(evidence))
    event_path = F / (stem + "CHECK_EVENTS.tsv")
    write(event_path,
          ["statement_id", "date", "who", "type", "outcome", "event_id", "phase",
           "source_file", "source_row", "source_event_type", "evidence_group",
           "publish_input_file", "publish_input_row", "date_utc", "where"],
          [event])
    print(tag, "PASS exact reversible two-block guards, identities, environment/brace structure and LF.")
    print(tag, "UTC", now, "defects", len(defects), "targeted_events", 1)
    for p in [receiver, F / (stem + "comparison.md"), guard_path, defect_path, event_path]:
        print("SHA256", sha256(p.read_bytes()).hexdigest(), p.relative_to(ROOT))
print("No canonical source, required row or global check-event file changed.")
