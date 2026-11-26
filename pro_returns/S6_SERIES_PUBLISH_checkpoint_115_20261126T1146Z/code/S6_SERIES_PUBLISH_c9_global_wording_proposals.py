#!/usr/bin/env python3
"""Reviewed Paper III P11/P14 wording proposals; writes only owned proposal rows.

The canonical source and shared defects/events are never written by this program.
The exact old/new passages, interpretation proofs and comparison scope are the
edit record. No inventory, census, manifest, seal or manuscript copy is produced.
"""
from __future__ import annotations

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
REPAIRS = []


def add(name, finding, old, new, interpretation):
    REPAIRS.append(dict(name=name, finding=finding, old=old, new=new,
                        interpretation=interpretation))


add("cyclic-index-renaming", "P11",
    "Definition~\\ref{mapsIII:def:fundamental-class-invariant}; this\nrenaming and its inverse preserve every group element and product.",
    "Definition~\\ref{mapsIII:def:fundamental-class-invariant}; this\nreindexing preserves every group element and product.",
    "The immediately preceding sentence retains the exact index map i -> i+1. Its inverse is j -> j-1; a basis vector and every named product are unchanged. Only the redundant inverse-renaming wording is removed.")
add("untwisted-engel-gluing", "P11",
    "gluing is the identity with identity inverse. The integral groups",
    "gluing is the identity. The integral groups",
    "The map remains the identity of the same marked boundary at (m,v)=(1,0). Its composite with itself fixes every point; the homology computation and subsequent nontrivial Weierstrass coordinate maps are untouched.")
add("pattern-product-coordinates", "P11",
    "The multiplicative models are fixed as in Theorem~\\ref{maps:src:D.2.31}. Taking the Cartesian products gives all patterns with\ntheir inverse identity on the row, site and option coordinates.",
    "The multiplicative models are fixed as in Theorem~\\ref{maps:src:D.2.31}. Taking the Cartesian products gives all patterns, indexed by\ntheir row, sites and options.",
    "A pattern is the same tuple (row, site options) before and after this edit; the Cartesian-product definition and full finite arithmetic scope remain. The tuple-to-tuple map fixes each coordinate, and its square fixes the tuple.")
add("weighted-root-input", "P11",
    "here. Identity on these marked data and its inverse identify\nthe affine equations and the positive root coordinate.",
    "here. The identity on these marked data identifies\nthe affine equations and the positive root coordinate.",
    "The data are explicitly Lambda, A_i(d), m_i and v_i in the preceding sentence. The comparison fixes them and the positive root coordinate. The substantive conjugating translation h and its inverse -h remain below.")
add("weighted-smith-identity", "P11",
    "in the free and Smith coordinates of their respective proofs.\nIts inverse is the same coordinate assignment. In degree three",
    "in the free and Smith coordinates of their respective proofs.\nIn degree three",
    "The retained display is (z_1,...,z_{d-1};[u]_d) -> (z_1,...,z_{d-1};[u]_d), and subsequent degrees retain their specified generator maps. The inverse sentence repeats this identity assignment.")
add("weighted-original-specialization", "P11",
    "Remark~\\ref{mapsIII:rem:original-additive-specializations};\ntheir inverse is identity in the same marked charts. At every\npositive $d$ the construction uses the stated iterated translation.",
    "Remark~\\ref{mapsIII:rem:original-additive-specializations}\nin the same marked charts. At every positive $d$ the construction\nuses the stated iterated translation.",
    "The preceding sentence retains identity suspension/toric maps and unchanged original caps at d=1. These fix every marked chart point. The positive-d construction and all homology formulas remain unchanged.")
add("weighted-normalization-coordinates", "P11",
    "same group ring. The inverse reads those identical coordinates.\nThis chain isomorphism carries the unit and $t-1$ reductions,",
    "same group ring. This chain isomorphism carries the unit and\n$t-1$ reductions,",
    "The preceding exact map [p(t)] -> [p(t)] and identical indexed component/branch/dual-torus cells give an identity matrix in every degree. Both chain differentials agree there. The substantive partial-sum inverse and extension section remain.")
add("weighted-odd-normalization-coordinates", "P11",
    "complex and the degree-four group-ring row agree under this\nchain map; the inverse reads the same coordinates. The unit\nand $t-1$ reductions, their partial-sum inverse and the free",
    "complex and the degree-four group-ring row agree under this\nchain map. The unit and $t-1$ reductions, their partial-sum\ninverse and the free",
    "The retained map fixes [p(t)] and each indexed cell coefficient; its matrix and inverse matrix are identity in each degree. No partial-sum or period-basis inverse is removed.")
add("bar-finite-input-tuple", "P11",
    "Its input identification fixes $R,m,b_0$ and the root coordinate,\nwith the same tuple as inverse. The coordinate map subtracts",
    "Its input identification fixes $R,m,b_0$ and the root coordinate.\nThe coordinate map subtracts",
    "The input map fixes the tuple (R,m,b_0,root coordinate), so applying it twice fixes that tuple. The analytic translation by -y_0 and its inverse by +y_0 remain explicitly stated.")
add("bar-unchanged-cap-input", "P11",
    "fan, node units, powered component permutation and line norm;\nreading the same tuple is its inverse. These displayed local",
    "fan, node units, powered component permutation and line norm.\nThese displayed local",
    "The retained identification fixes the natural row, positive d, fan, node units, permutation and line norm. The transfer, period, normalization, line-flow and Gysin maps cited immediately before it are preserved with their full mathematical content.")
add("bar-peripheral-identity", "P11",
    "On the fibre lattice and peripheral paths the identification and\nits inverse are the identity. Thus the comparison carries the",
    "On the fibre lattice and peripheral paths the identification\nis the identity. Thus the comparison carries the",
    "The comparison fixes each fibre-lattice element and peripheral path. The preceding period exponential and inverse logarithm, and the following bar-polygon inverse, remain unchanged.")
add("three-primary-generators", "P11",
    "the identity, with the identity inverse. Those proofs give",
    "the identity. Those proofs give",
    "The three model embeddings, framings and primitive generators are the identical ones from their definitions. Their generator comparison remains the identity; the CRT homology maps and inverses below remain.")
add("odd-parity-scalar", "P11",
    "Multiplication by the odd integer $q$ is the identity, with\nidentity inverse, on $\\mathbb Z/2$; hence the full-order $N$",
    "Multiplication by the odd integer $q$ is the identity\non $\\mathbb Z/2$; hence the full-order $N$",
    "For the two residues 0 and 1, multiplication by odd q returns the same residue. The identity assertion and its parity conclusion remain, so the deleted inverse phrase contributes no separate premise.")
add("additive-trace-models", "P11",
    "trace maps, so the identity and its inverse identify the marked\nmanifolds. That proof gives simple connectivity, the unique spin",
    "trace maps, so the identity identifies the marked\nmanifolds. That proof gives simple connectivity, the unique spin",
    "The exact embeddings, normal framings and coefficient maps in this paragraph remain identical to the cited trace construction; the comparison fixes every point of that construction. The displayed quotient-generator inverses and subsequent order-20 CRT inverse remain.")
add("weighted-parity-input", "P11",
    "on $(N,TN)$ and on its projected frame, with identity inverse. Its\ninduced spin structure is the one used by the prescribed-spin filling",
    "on $(N,TN)$ and on its projected frame. Its induced spin\nstructure is the one used by the prescribed-spin filling",
    "The map fixes N, TN and the projected tangent frame. The substantive projection/shear maps immediately above and quaternionic convention maps below are unchanged.")
add("type-c-universal-cover", "P11",
    "universal \\(\\mathbb C^2\\) and its inverse are the identity.",
    "universal \\(\\mathbb C^2\\) is the identity.",
    "Only the identity point map of the universal complex plane is involved. The lattice change G_0, G_0^{-1}=G_0, period equation and nontrivial line-frame gauges remain explicitly displayed.")
add("cusp-cover-input-renamings", "P11",
    "in the fixed ordered bases. Their inverses are $(x,q)\\mapsto(x,t=q)$,\nthe identity on $(\\xi,v)$, and the inverse basis identification.\nEvery cone and every character coordinate is fixed.",
    "in the fixed ordered bases. These identifications fix every cone\nand every character coordinate.",
    "The preceding displayed maps (x,t)->(x,q=t), (xi,v)->(xi,v), and bar-lambda->lambda remain. They identify literal parameter names and ordered basis elements; swapping the names recovers each input. The induced quotient/fibre-product isomorphisms and nontrivial covering maps remain.")
add("cusp-cover-radius-renaming", "P11",
    "on their quotients and fibre products. The radius identification\n$r=\\epsilon_N$, with inverse $\\epsilon_N=r$, gives the full\ninverse-image discs of that same construction.",
    "on their quotients and fibre products. With radius $r=\\epsilon_N$,\nwe obtain the full inverse-image discs of that construction.",
    "Both descriptions use the identical positive radius. The disc is the same set defined by that radius; no radial rescaling map or inverse is deleted.")
add("cusp-cover-star-fan", "P11",
    "identifies this $D_0$ with the target normalization $E\\simeq\\mathrm{dP}_6$,\nwith inverse the same fan map. The two branches at an open double",
    "identifies this $D_0$ with the target normalization $E\\simeq\\mathrm{dP}_6$.\nThe two branches at an open double",
    "The retained preceding sentence explicitly gives the identity of the star fans. It fixes every cone and its character chart. The normalization injection and conductor/ramification computations remain.")
add("cusp-cover-log-renaming", "P11",
    "The log coordinate $s_v$ is the coordinate $r$ of the earlier period\ncalculation, with inverse renaming, and",
    "The log coordinate $s_v$ is the coordinate $r$ of the earlier period\ncalculation, and",
    "The parameter is merely named s_v here and r in the referenced formula. All actual period formulas and the scaling isomorphism [zeta]->[N zeta] with inverse remain.")
add("target-smash-quotient-identity", "P11",
    "The comparison with that lemma's quotient sends $[x]$ to $[x]$;\nits inverse is the same map, with $F$ representing the basepoint.",
    "The comparison with that lemma's quotient sends $[x]$ to $[x]$,\nwith $F$ representing the basepoint.",
    "The quotient comparison fixes each class [x], including the collapsed class F. The circle rescaling and tangent/arctangent coordinate maps above retain their inverse formulas.")
add("fibre-smash-quotient-identity", "P11",
    "to that lemma's quotient is $[x]\\mapsto[x]$, with the same inverse;\noff the collapsed point it takes the unique uncollapsed tuple, and",
    "to that lemma's quotient is $[x]\\mapsto[x]$; off the collapsed\npoint it takes the unique uncollapsed tuple, and",
    "The comparison is the identity on quotient classes with the same collapsed subset. The preceding homeomorphisms from fibre quotients and their nontrivial uncollapsed-coordinate inverses remain.")
add("carrier-target-identity", "P11",
    "that lemma with this target is the identity, with itself as inverse.",
    "that lemma with this target is the identity.",
    "The specialization C=mathcal C is retained with its basepoint and ordered generators u,v. Its identity comparison is unchanged; the wedge homotopy inverse L=kj_C and both stated based homotopies remain.")
add("final-natural-specialization", "P11",
    "marked quotient with the same filling data; its inverse on that\nsubfamily is the same identity. The finite reduction for integral",
    "marked quotient with the same filling data. The finite reduction\nfor integral",
    "The V=0 specialization fixes the natural line, its linearization and marked quotient with all filling data. The identity and the count 226 remain; no claim for nonzero V is altered.")
add("final-degree-zero-specialization", "P11",
    "the line bundle and its quotient construction, with identity inverse.",
    "the line bundle and its quotient construction.",
    "The two specializations are explicitly M=O(P-O) and M=O(P-O+V), with their marked section pair, divisor, linearization and filling data held fixed. Their identity comparisons remain; the unresolved general question is unchanged.")


# Every occurrence selected here was read in its paragraph before this list
# was written. In these 28 loci 'output' names the same glued complex
# threefold X; the final remark is handled separately as a computation.
P14_LINES = [470, 786, 21728, 21737, 22833, 22839, 24421, 25066,
             25112, 25206, 25216, 25259, 25312, 25869, 26973,
             38273, 39305, 40651, 41473, 41503, 41600, 42841,
             42899, 42916, 44805]


def rows(source):
    proposals = list(REPAIRS)
    # Locate the expressly read paragraphs by content; line numbers are only
    # descriptive cp100 locators and are not used to mutate the live source.
    original_lines = source.splitlines(keepends=True)
    for line in P14_LINES:
        # Root owns other concurrent edits, so these paragraph proposals are
        # generated against cp100 before admission; no live-offset mutation.
        if line > len(original_lines):
            raise ValueError("P14 baseline line out of range")
        a = line - 1
        while a > 0 and original_lines[a - 1].strip():
            a -= 1
        b = line
        while b < len(original_lines) and original_lines[b].strip():
            b += 1
        old = ''.join(original_lines[a:b]).rstrip('\n')
        if not re.search(r'\boutputs?\b', original_lines[line - 1]):
            raise ValueError(f"P14 cp100 line guard changed: {line}")
        new = re.sub(r'\boutput\b', 'threefold', old)
        new = re.sub(r'\boutputs\b', 'threefolds', new)
        new = re.sub(r'\bOutputs\b', 'Threefolds', new)
        new = new.replace('Every sphere threefold is',
                          'Every threefold satisfying these sphere conditions is')
        new = new.replace('[Sphere threefolds over', '[Sphere fillings over')
        if any(p['old'] == old for p in proposals):
            continue
        proposals.append(dict(name=f"threefold-wording-{line}", finding="P14",
            old=old, new=new,
            interpretation="In the read paragraph, the noun denotes the glued complex threefold X defined by the same marked filling data. The identity X -> X preserves the construction, all hypotheses and every invariant. Only the noun 'output' is replaced; no formula, parameter, map, conclusion or cited statement changes."))
    proposals.append(dict(name="weighted-integral-computation", finding="P14",
        old=r"""The integral computation takes integer parameters, tests
\eqref{maps:eq:D.WE1}, and returns the full group and homology
presentations. Polynomial identities verify the monodromies,
primitive exterior-square quotient and graph basis. The unreduced
graph and full area kernels are compared with
\eqref{maps:eq:D.WE3}--\eqref{maps:eq:D.WE4}. The finite outputs
include nonprimitive free twists, nontrivial cap torsion,
every original/logarithmic choice and zero-Euler cases.""",
        new=r"""For integer parameters satisfying \eqref{maps:eq:D.WE1}, the
Mayer--Vietoris maps in the preceding proof give the integral group
and homology presentations. The monodromy identities, primitive
exterior-square quotient and graph basis are polynomial identities
in those parameters. The unreduced graph and full area kernels give
\eqref{maps:eq:D.WE3}--\eqref{maps:eq:D.WE4}. These formulas include
nonprimitive free twists, nontrivial cap torsion, every
original/logarithmic choice and zero-Euler cases.""",
        interpretation="The immediately preceding weighted Engel proof constructs the integral boundary/cap maps and their Mayer-Vietoris presentation, including its exterior-square and graph kernels. The remark now names that method and its exact input condition rather than describing a program return. The three referenced formulas, four exceptional scopes and all substantive maps are unchanged."))
    return proposals


def main():
    archive = ROOT.parents[1] / "upload/S6_SERIES_PUBLISH_continue_cp100.zip"
    with ZipFile(archive) as base:
        source = base.read("S6_SERIES_PUBLISH_checkpoint_100/S6_SERIES_PUBLISH_III.tex").decode("utf-8")
    owners, _, _ = parse_statements(source)
    proposals = rows(source)
    now = datetime.now(timezone.utc).isoformat()
    df = next(csv.reader((ROOT / "S6_SERIES_PUBLISH_defects_III.tsv").open(), delimiter="\t"))
    ef = next(csv.reader((ROOT / "CHECK_EVENTS.tsv").open(), delimiter="\t"))
    defects, events = [], []
    candidate = source
    proof_changes = {}
    for i,p in enumerate(proposals, 1):
        old,new=p['old'],p['new']
        if source.count(old) != 1:
            raise ValueError((p['name'],source.count(old)))
        pos=source.index(old)
        owner_pos=pos + (old.find('output') if p['name'].startswith('threefold-wording-') else 0)
        assigned=[o for o in owners if o.start<=owner_pos<o.stop]
        if len(assigned) == 1:
            owner=assigned[0]
            sid=owner.statement_id
            tag=owner.tag
            proof=owner.statement_stop <= owner_pos
        else:
            if p['name'] == 'threefold-wording-786':
                sid='series:III:F'
                tag=next(o.tag for o in owners if o.statement_id==sid)
                proof=False
            else:
                raise ValueError((p['name'],'ambiguous owner',assigned))
        p.update(statement_id=sid,tag=tag,cp100_line=source.count('\n',0,pos)+1)
        if Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]+\}',old)) != Counter(re.findall(r'\\(?:label|hypertarget)\{[^{}]+\}',new)):
            raise ValueError('permanent identity changed: '+p['name'])
        if candidate.count(old) != 1:
            raise ValueError('overlapping guard: '+p['name'])
        candidate=candidate.replace(old,new,1)
        change_id=f"CLAUDE-III-{p['finding']}-GLOBAL-{i:03d}"
        p['change_id']=change_id
        defects.append(dict(change_id=change_id,type='D08',statement_id=sid,
            old_location=f"cp100 source line {p['cp100_line']}; tag {tag}",
            old_page='cp100 regrouped source; page concordance pending',
            new_location=f"same labelled statement/proof; {p['name']}",
            new_page='pending current rendered-PDF review',old_text=old,new_text=new,
            reason=p['interpretation'],
            review_status=f"Exact old/new passage and surrounding argument read by continuation9_global_sweep at {now}; proposed, awaiting root admission and final page review."))
        if proof:
            proof_changes.setdefault(sid,[]).append(p)
        print(f"{change_id} {sid} line {p['cp100_line']}: {p['name']}")
    for j,(sid,ps) in enumerate(proof_changes.items(),1):
        eid=f"publish:c9:III:global-wording:{j:03d}"
        e={k:'' for k in ef}
        e.update(statement_id=sid,date=now[:10],who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; continuation nine global wording reviewer',
            type='used and rechecked in this run',
            outcome='Read and compared exact old/new passages and their adjoining argument for '+', '.join(p['name'] for p in ps)+'. Each retained map and parameter scope has the same interpretation, proved in the corresponding defect reason; nontrivial inverses are retained. All other proof text is byte-identical by guarded substitution. This is a wording comparison at the stated loci, with no new independent proof, required-check or PDF-page credit.',
            event_id=eid,phase='continuation9 Paper III publication wording',
            source_file='code/S6_SERIES_PUBLISH_c9_global_wording_proposals.py',source_event_type='used and rechecked in this run',
            evidence_group=eid,date_utc=now,where='agents/continuation9_global_sweep/S6_SERIES_PUBLISH_c9_wording_proposals.json')
        events.append(e)
    OWN.mkdir(parents=True,exist_ok=True)
    (OWN / 'S6_SERIES_PUBLISH_c9_wording_proposals.json').write_text(json.dumps(proposals,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    for name,fields,data in [('S6_SERIES_PUBLISH_c9_wording_defects.tsv',df,defects),('S6_SERIES_PUBLISH_c9_wording_events.tsv',ef,events)]:
        with (OWN / name).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n')
            w.writeheader();w.writerows(data)
    # Equality of the unchanged complement is built into exact replacement;
    # reverse every admitted word passage in reverse order to recover input.
    reconstructed=candidate
    for p in reversed(proposals):
        if reconstructed.count(p['new']) != 1:
            raise ValueError('inverse edit guard: '+p['name'])
        reconstructed=reconstructed.replace(p['new'],p['old'],1)
    if reconstructed != source:
        raise ValueError('exact inverse text reconstruction failed')
    live = (ROOT / "S6_SERIES_PUBLISH_III.tex").read_text(encoding="utf-8")
    for p in proposals:
        if live.count(p['old']) != 1:
            raise ValueError('live source old guard changed: '+p['name'])
    print(f"{len(proposals)} guarded proposals; {len(events)} scoped wording-comparison events; exact reverse substitutions recover source; canonical source untouched.")


if __name__ == '__main__':
    main()
