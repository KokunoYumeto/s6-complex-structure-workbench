#!/usr/bin/env python3
"""Archive candidate16 D08 proposals without changing canonical or reading files."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "agents/i_cont_edits"
SOURCE_SHA = "61ffa2e316814c140fc69723e080b4414ea4016ba27e0ac84bd2d9347fbc93fc"
PDF_SHA = "4a1633d9e19a82e3df92a0e3c31ada306b3e801f3051b0c1b7f0018d873f51a2"
READING_SHA = "77bc19c01d1de57578583b29396fe9dce802222405a8adc7a019ec40108f5183"
sha = lambda b: hashlib.sha256(b).hexdigest()

PROPOSALS = [
    (290, "We prove the following four coefficient bounds. ", "",
     "Delete the announcement. The immediately following analytic power-series norm definition and all four inequalities remain, with their complete recurrence, finite sums, rational enclosures and tail proof."),
    (290, "The following recurrences and tails determine the coefficient\nbounds. ", "",
     "Delete the second announcement of that same calculation. The text proceeds directly from the four bounds to the displayed differential system and coefficient recurrences, and retains every finite input, cutoff, tail and comparison."),
    (296, " The polarization calculation below identifies these groups\nfor the point and extension data in this paper.", "",
     "Delete the closing roadmap of the numbered input remark. Its exact published construction, dimension formula, bracket locator and corrected-table value remain. The following proposition already states the point and lift data and proves the group calculation."),
    (297, " This\ndescription computes the group even when the lift contributes\na Kummer factor.", "",
     "Delete the closing recap. The proposition explicitly defines the quotient-torus torsion criterion for e; the proof retains the Rosati slope, lift contribution, extra central Tate line for e=1, and the dimension formula proving each table entry."),
    (303, " This argument uses the period vector.", "",
     "Delete the recap after the transcendence conclusion. The preceding two proof steps retain the explicit period vector, its algebraic differential coordinates, division to a nonzero torsion point, analytic-subgroup theorem and isogeny contradiction. The compact-point argument remains a separate following step."),
    (305, "This computes the antisymmetric compact lift with the stated normalization.\n", "",
     "Delete the closing recap of the completed lift calculation. The exact theta/sigma ratio, rational trivialization, logarithm, differentiated CM identity and zero compactness character remain; the same normalization is fixed by those unchanged equations."),
    (305, "The following period comparison determines $dB$ in the algebraic coordinates. Its torus\nblock is", "In the algebraic coordinates, the torus block of $dB$ is",
     "Replace the announcement by the same positive coordinate statement. The symbol dB is retained, followed by its unchanged torus block, first column, B-squared relation, period vectors, integer comparison and matrix conclusion."),
    (306, " The construction isolates the Gaussian in\na Lie eigencoordinate.", "",
     "Delete the recap after the toric-slope contradiction. The theorem and proof retain the exact Gaussian projection, algebraic-subtorus slope argument and transcendence conclusion; no mathematical map or scope is changed."),
    (306, "The spectral comparison with the ordinary prime $5$ is\nexplicit. The CM number", "At the ordinary prime $5$, the CM number",
     "State the comparison's existing ordinary-prime context directly. The prime 5, CM number, polynomial, two archimedean absolute values, two valuations, reduction and comparison with the proved spectral gap remain in their existing order."),
    (306, "The following polynomial identities determine these values.\n", "",
     "Delete the announcement before the exact witness calculation. The stated constants, polynomials, coprimality identities, degree-19 endomorphism, differential pullback, kernel count, sign choice and evaluations giving those constants remain."),
    (307, "The following complexification uses the curve and conjugation of\n\\cref{I:CM-enlargement-coordinates}. Its diagonal values,\nCM translates and normalized second derivatives are computed explicitly.", "Use the curve and conjugation of\n\\cref{I:CM-enlargement-coordinates}.",
     "Retain the exact curve/conjugation convention and its numbered reference positively; delete the section roadmap. The following proposition and complete proof retain the diagonal identity, CM translates, first and second derivatives, fixed-field formulas and numerical rank criterion."),
]


def block_for(s, position):
    if s.startswith("The following complexification", position):
        start = s.rfind(r"\subsection{", 0, position)
        statement = s.index(r"\begin{proposition}", position)
        end_statement = s.index(r"\end{proposition}", statement) + len(r"\end{proposition}")
        end = s.index(r"\end{proof}", end_statement) + len(r"\end{proof}")
        return "ari:C.7.11", start, end, (statement-start, end_statement-start)
    head = list(re.finditer(r"\\begin\{(theorem|proposition|lemma|corollary|remark|definition)\}", s[:position]))[-1]
    end_statement = s.index(r"\end{" + head[1] + "}", head.end()) + len(r"\end{" + head[1] + "}")
    end = end_statement
    if re.match(r"\s*\\begin\{proof\}", s[end:]):
        end = s.index(r"\end{proof}", end) + len(r"\end{proof}")
    assert head.start() <= position < end
    label = re.search(r"\\label\{([^}]+)\}", s[head.start():end])[1]
    return label, head.start(), end, (0, end_statement-head.start())


def math_segments(s):
    patterns = [r"\\\[[\s\S]*?\\\]", r"\\\([\s\S]*?\\\)",
                r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$",
                r"(?<!\\)\$(?:\\.|[^$\\])*(?<!\\)\$",
                r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}[\s\S]*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?)\}"]
    return [re.findall(p, s) for p in patterns]


def main():
    paths = {"source": ROOT / "S6_SERIES_PUBLISH_I.tex",
             "log": ROOT / "S6_SERIES_PUBLISH_defects_I.tsv",
             "events": ROOT / "CHECK_EVENTS.tsv",
             "reading": OUT / "S6_SERIES_PUBLISH_I_final_candidate16_reading_edits.json"}
    frozen = {k:p.read_bytes() for k,p in paths.items()}
    assert sha(frozen["source"]) == SOURCE_SHA
    assert sha(frozen["reading"]) == READING_SHA
    assert sha((ROOT / "build/I_candidate16/S6_SERIES_PUBLISH_I.pdf").read_bytes()) == PDF_SHA
    s = frozen["source"].decode()
    blocks, guards = {}, []
    for i, (page, before, after, reason) in enumerate(PROPOSALS, 1):
        assert s.count(before) == 1, (i, s.count(before))
        pos = s.index(before)
        label, start, end, statement_span = block_for(s, pos)
        block = blocks.setdefault(label, {"start":start,"end":end,"original":s[start:end],"proposed":s[start:end],"statement_span":statement_span,"guards":[]})
        assert block["proposed"].count(before) == 1
        block["proposed"] = block["proposed"].replace(before,after,1)
        assert math_segments(before) == math_segments(after)
        assert re.findall(r"\\[A-Za-z@]+\*?|\\.",before) == re.findall(r"\\[A-Za-z@]+\*?|\\.",after)
        gid = f"I16-edits-{i:02d}"
        block["guards"].append(gid)
        guards.append({"id":gid,"type":"D08","page":page,"statement_id":label,"source_line":s[:pos].count("\n")+1,
                       "before":before,"after":after,"reason":reason,"source_sha256":SOURCE_SHA,"pdf_sha256":PDF_SHA,
                       "all_mathematical_segments_and_commands_identical":True,
                       "inline_math_mentions_removed":[],"inline_math_mentions_added":[],
                       "status":"proposed for root review; not applied","mathematical_events_added":0})
    archives = []
    for i,(label,b) in enumerate(blocks.items(),1):
        a,c = b["original"],b["proposed"]
        assert math_segments(a) == math_segments(c)
        assert re.findall(r"\\[A-Za-z@]+\*?|\\.",a) == re.findall(r"\\[A-Za-z@]+\*?|\\.",c)
        for p in [r"\\label\{([^}]+)\}",r"\\hypertarget\{([^}]+)\}",r"\\(?:eqref|ref|cref|Cref|cite|citet|citep)(?:\[[^\]]*\])?\{([^}]+)\}"]:
            assert re.findall(p,a) == re.findall(p,c)
        stem = OUT / f"S6_SERIES_PUBLISH_I_candidate16_edits_block_{i:02d}"
        pa,pb,pd = [Path(str(stem)+suffix) for suffix in ["_original.tex","_proposed.tex",".diff"]]
        pa.write_text(a);pb.write_text(c)
        pd.write_text("".join(difflib.unified_diff(a.splitlines(True),c.splitlines(True),fromfile=label+"/candidate16",tofile=label+"/proposed")))
        stat_a=a[slice(*b['statement_span'])]
        stat_identical=stat_a in c
        archive={"statement_id":label,"original":str(pa.relative_to(ROOT)),"original_sha256":sha(pa.read_bytes()),
                 "proposed":str(pb.relative_to(ROOT)),"proposed_sha256":sha(pb.read_bytes()),"diff":str(pd.relative_to(ROOT)),"diff_sha256":sha(pd.read_bytes()),
                 "guards":b["guards"],"all_mathematical_segments_and_commands_identical":True,
                 "all_labels_targets_and_citation_reference_sequences_identical":True,
                 "full_statement_byte_identical":stat_identical,
                 "complete_owning_source_block_read":True,
                 "all_content_outside_exact_guards_byte_identical":True}
        archives.append(archive)
        for g in guards:
            if g["statement_id"]==label:g["full_block_archive"]=archive
    proposed=s;maps=[]
    for g in guards:
        p=proposed.index(g["before"]);maps.append((p,g['before'],g['after']))
        proposed=proposed[:p]+g['after']+proposed[p+len(g['before']):]
    reverse=proposed
    for p,a,b in reversed(maps):
        assert reverse[p:p+len(b)]==b
        reverse=reverse[:p]+a+reverse[p+len(b):]
    assert reverse==s
    for k,p in paths.items():assert p.read_bytes()==frozen[k]
    result={"paper":"I","candidate":16,"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "source_sha256":SOURCE_SHA,"pdf_sha256":PDF_SHA,"defect_log_sha256":sha(frozen['log']),
            "reading_record":str(paths['reading'].relative_to(ROOT)),"reading_record_sha256":READING_SHA,
            "guards":guards,"full_blocks":archives,"guard_count":len(guards),"source_modified":False,
            "exact_forward_and_inverse_reconstruction_verified":True,"all_mathematical_segments_and_commands_identical":True,
            "mathematical_events_added":0,"additional_full_page_credit":0,
            "scope":"All 18 assigned candidate16 complete images actually viewed and read in the immutable reading receipt. Six complete source blocks (including the Section 26.6 headnote and owning proposition/proof) were then read; exact replacements compared against those blocks. These proposals remove only announcements and recaps or restate the existing coordinate/prime convention positively. Every mathematical segment, TeX command, label, target and citation/reference sequence is identical. No canonical source, log, event or completed reading record is changed.",
            "ordinary_mathematics_retained":["The branch and C-nonvanishing estimates justify definitions and analytic quotients.","Recurrence/tail inputs, finite bounds and Bernstein positivity are retained in full.","The quotient-torus torsion criterion and extra central line determine the Kummer contribution.","Algebraic Hom and subtorus obstructions, spectral-gap nonapproximation, and ordinary-prime valuations retain their exact maps and inequalities.","The existing final-part norm question and its graph-closure pointer are retained."]}
    p=OUT / "S6_SERIES_PUBLISH_I_candidate16_edits_guards.json"
    p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    md=["# Paper I candidate16 — D08 guarded proposals","",f"Source: `{SOURCE_SHA}`", "",f"PDF: `{PDF_SHA}`","",f"Immutable reading: `{READING_SHA}`","","Eleven proposals in six complete source blocks; canonical source and log unchanged. No added mathematical events or page credit.","","| Guard | Page | Statement | Exact change |","|---|---:|---|---|"]
    for g in guards:md.append(f"| {g['id']} | {g['page']} | `{g['statement_id']}` | {g['reason']} |")
    p.with_suffix('.md').write_text('\n'.join(md)+'\n')
    print(json.dumps({"guards":len(guards),"blocks":len(blocks),"guard_file":str(p.relative_to(ROOT)),"sha256":sha(p.read_bytes()),"proposed_source_sha256":sha(proposed.encode()),"source_modified":False,"reading_unchanged":True,"mathematical_events_added":0},indent=2))


if __name__ == "__main__":main()
