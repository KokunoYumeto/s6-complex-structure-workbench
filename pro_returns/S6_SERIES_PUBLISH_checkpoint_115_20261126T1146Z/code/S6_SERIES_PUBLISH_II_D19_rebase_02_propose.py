#!/usr/bin/env python3
"""Reversible section-numbering proposal. Canonical files are read, never written."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import bisect
import collections
import csv
import difflib
import hashlib
import importlib.util
import json
import re

ROOT=Path(__file__).resolve().parents[1]
BDIR=ROOT/"agents/continuation2_B/D19"
OLDPRE="S6_SERIES_PUBLISH_II_B2_D19_"
OUT=ROOT/"records/S6_SERIES_PUBLISH_II_D19_rebase_02"
PRE="S6_SERIES_PUBLISH_II_D19_rebase_02_"
spec=importlib.util.spec_from_file_location("d19refs",BDIR/(OLDPRE+"reference_scan.py"))
refsmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(refsmod)
scan=refsmod.scan

def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()

def apply_edits(s,edits):
    edits=sorted(edits,key=lambda e:(e["start"],e["end"]))
    out=[];cursor=0
    for e in edits:
        assert e["start"]>=cursor,("overlapping edits",e)
        assert s[e["start"]:e["end"]]==e["old"],e
        out.extend([s[cursor:e["start"]],e["new"]]);cursor=e["end"]
    out.append(s[cursor:])
    return "".join(out)

def invert_edits(s,edits,proposed):
    delta=0;inverse=[]
    for e in sorted(edits,key=lambda e:(e["start"],e["end"])):
        a=e["start"]+delta;b=a+len(e["new"])
        inverse.append(dict(start=a,end=b,old=e["new"],new=e["old"]))
        delta+=len(e["new"])-len(e["old"])
    assert apply_edits(proposed,inverse)==s
    return inverse

def transform(s,include_scope=True):
    assert digest(s)=="6ebaca4da9c7533800d8054bb63d8b4521c11e59b401c8ec02a425a34cd3d181"
    data,blocks=scan.inventory(s)
    assert len(data["numbered_equations"])==1817
    assert len(data["displays"])==3013
    assert sum(bool(x["old_tag"]) for x in data["numbered_equations"])==1764
    baseline_single=[x for x in json.loads((BDIR/(OLDPRE+"v1_literal_reference_transport.json")).read_text()) if x.get("treatment")=="single-letter text reference replaced by eqref"]
    assert len(baseline_single)==9
    refs=refsmod.collect(s,data)
    math_ranges=refsmod.math_ranges(s,data["displays"])
    math_starts=[x[0] for x in math_ranges]
    def in_math(a,b):
        i=bisect.bisect_right(math_starts,a)-1
        return i>=0 and math_ranges[i][1]>=b
    all_labels=collections.Counter(re.findall(r"\\label\{([^{}]+)\}",s))
    all_anchors=collections.Counter(re.findall(r"\\hypertarget\{([^{}]+)\}",s))
    edits=[];new_labels=[];reference_changes=[];non_equation_collisions=[]
    def add(a,b,new,kind,reason,**extra):
        edits.append(dict(start=a,end=b,old=s[a:b],new=new,kind=kind,
                          reason=reason,**extra))
    # The numerical sequence includes every existing numbered equation.
    for e in data["numbered_equations"]:
        if e["labels"]:
            e["target_label"]=e["labels"][0]
        else:
            assert e["old_tag"] and re.fullmatch(r"[A-Za-z0-9.]+",e["old_tag"])
            label="eq:II:manual:"+e["old_tag"]
            assert label not in all_labels and label not in new_labels
            new_labels.append(label);e["target_label"]=label
        e["new_labels_added"]=[] if e["labels"] else [e["target_label"]]
    by_tag={e["old_tag"]:e for e in data["numbered_equations"] if e["old_tag"]}
    by_label={l:e for e in data["numbered_equations"] for l in e["labels"]}
    for b in blocks:
        if not b["tags"]:continue
        assert len(b["tags"])==1
        tag=b["tags"][0];e=by_tag[tag["value"]];env=b["environment"]
        if env=="bracket":
            add(b["start"],b["begin_end"],r"\begin{equation}","display_environment",
                "Replace the tagged bracket display by the ordinary equation counter.",old_tag=e["old_tag"])
            add(b["end_start"],b["end"],r"\end{equation}","display_environment",
                "Close the same numbered display.",old_tag=e["old_tag"])
        elif env=="align*":
            assert tag["row"]==b["row"],"A nonfinal tagged align row needs explicit review"
            assert not b["row_controls"]
            add(b["start"],b["begin_end"],r"\begin{align}","display_environment",
                "Keep the same aligned rows and number only the original tagged row.",old_tag=e["old_tag"])
            add(b["end_start"],b["end"],r"\end{align}","display_environment",
                "Close the same aligned display.",old_tag=e["old_tag"])
            for row in b["row_breaks"]:
                assert row["row"]<tag["row"]
                add(row["start"],row["start"],r"\notag","row_number_suppression",
                    "Preserve the originally unnumbered earlier alignment row.",old_tag=e["old_tag"])
        else:
            assert env in {"multline","equation","align"},env
        replacement="" if e["labels"] else r"\label{"+e["target_label"]+"}"
        add(tag["start"],tag["end"],replacement,"manual_tag",
            "Use section-based appearance-order numbering and preserve or supply the exact equation label.",
            old_tag=e["old_tag"],new_number=e["new_number"],target_label=e["target_label"])
    counter_anchor=r"\allowdisplaybreaks[2]"
    assert s.count(counter_anchor)==1
    assert r"\numberwithin{equation}{section}" not in s
    a=s.index(counter_anchor)+len(counter_anchor)
    add(a,a,"\n"+r"\numberwithin{equation}{section}","section_counter",
        "Reset the equation counter at each numbered section.")
    scope_guard=json.loads((BDIR/(OLDPRE+"CIR_scope_guard.json")).read_text())["guard"]
    scope_interval=None;scope_status="not requested"
    if include_scope:
        if s.count(scope_guard["old"])==1:
            a=s.index(scope_guard["old"]);b=a+len(scope_guard["old"])
            add(a,b,scope_guard["new"],"CIR_scope_correction",scope_guard["reason"],
                defect_type=scope_guard["defect_type"])
            scope_interval=(a,b);scope_status="exact separate D22/D23 guard applied in the proposal"
        else:
            assert s.count(scope_guard["new"])==1,"The CIR scope paragraph changed; review before rebinding"
            scope_status="already corrected exactly"
    def covered_by_scope(a,b):
        return scope_interval is not None and a>=scope_interval[0] and b<=scope_interval[1]
    for x in refs["literal_candidates"]:
        a,b=x["start"],x["end"];tag=x["old_tag"]
        if covered_by_scope(a,b):
            reference_changes.append(dict(**x,treatment="transported by the separately proved CIR scope correction"))
            continue
        if s[a-1:a]=="(" and s[b:b+1]==")":
            e=by_tag[tag];old=s[a-1:b+1];new=r"\eqref{"+e["target_label"]+"}"
            add(a-1,b+1,new,"literal_equation_reference",
                "Bind the literal equation citation to the same displayed formula through its exact label.",
                old_tag=tag,new_number=e["new_number"],target_label=e["target_label"])
            reference_changes.append(dict(**x,old=old,new=new,target_label=e["target_label"],
                                          treatment="literal replaced by eqref"))
        else:
            # These seven contexts were actually read and are subsection/program-outline identifiers.
            assert tag in {"C.3","A.3","A.5","C.1","E.5","C.2"},x
            non_equation_collisions.append(dict(**x,
                treatment="unchanged; this occurrence names an inherited subsection or range of subsections",
                reason="The actual sentence/heading concerns the full section topic rather than the unique displayed equation with the same characters."))
    single_math=[];single_text=[]
    for x in refs["single_letter_candidates"]:
        a,b=x["start"],x["end"]
        if in_math(a,b):
            single_math.append(dict(start=a,end=b,line=x["line"],token=s[a:b],
                                   prefix=s[max(0,a-24):a],suffix=s[b:b+24],
                                   treatment="unchanged mathematical argument or principal ideal inside a math delimiter"))
        else:
            tag=x["old_tag"];e=by_tag[tag]
            assert any((x["old_tag"],x["context"])==(v["old_tag"],v["context"]) for v in baseline_single),"A changed single-letter citation context needs review"
            new=r"\eqref{"+e["target_label"]+"}"
            add(a,b,new,"literal_equation_reference",
                "Resolve this text citation of the original lettered equation, preserving all mathematical uses of the same letter.",
                old_tag=tag,new_number=e["new_number"],target_label=e["target_label"])
            single_text.append(dict(**x,old=s[a:b],new=new,target_label=e["target_label"]))
            reference_changes.append(single_text[-1]|dict(treatment="single-letter text reference replaced by eqref"))
    assert [(x["old_tag"],x["context"]) for x in single_text]==[(x["old_tag"],x["context"]) for x in baseline_single]
    assert len(single_text)==9
    assert len(non_equation_collisions)==7
    assert all(x["already_dynamic"] for x in refs["seriesref_definitions"])
    # Record exact dynamic owners without changing the already correct SeriesRef definitions.
    for x in refs["dynamic_body_references"]:
        x["treatment"]=("changed only inside the separately justified scope paragraph"
                        if covered_by_scope(x["start"],x["end"])
                        else "unchanged reference command to the same equation label")
    # Prove that each literal numeric range still names exactly the same contiguous formula set.
    ranges=[]
    literal_spans={e["start"]:e for e in edits if e["kind"]=="literal_equation_reference"}
    for a,e in sorted(literal_spans.items()):
        tail=s[e["end"]:]
        m=re.match(r"\s*--\s*",tail)
        if not m:continue
        nexta=e["end"]+m.end()
        if nexta not in literal_spans:continue
        f=literal_spans[nexta];x,y=e["old_tag"],f["old_tag"]
        mx=re.fullmatch(r"(.*?)(\d+)",x);my=re.fullmatch(r"(.*?)(\d+)",y)
        if mx and my and mx.group(1)==my.group(1):
            lo,hi=int(mx.group(2)),int(my.group(2));assert lo<=hi
            old_tags=[mx.group(1)+str(i) for i in range(lo,hi+1)]
        else:
            mx=re.fullmatch(r"(.*?)([A-Za-z])",x);my=re.fullmatch(r"(.*?)([A-Za-z])",y)
            assert mx and my and mx.group(1)==my.group(1),(x,y)
            lo,hi=ord(mx.group(2)),ord(my.group(2));assert lo<=hi
            old_tags=[mx.group(1)+chr(i) for i in range(lo,hi+1)]
        assert all(t in by_tag for t in old_tags),(x,y,"missing range member")
        es=[by_tag[t] for t in old_tags]
        numbers=[z["new_number"] for z in es]
        contiguous=len({z["section"] for z in es})==1 and [z["ordinal"] for z in es]==list(range(es[0]["ordinal"],es[-1]["ordinal"]+1))
        assert contiguous,(x,y,numbers,"range needs explicit expansion")
        ranges.append(dict(old_start=x,old_end=y,old_tags=old_tags,new_numbers=numbers,
                           labels=[z["target_label"] for z in es],same_contiguous_formula_set=True))
    proposed=apply_edits(s,edits)
    inverse=invert_edits(s,edits,proposed)
    after,after_blocks=scan.inventory(proposed)
    assert len(data["displays"])==len(after["displays"])
    assert len(data["numbered_equations"])==len(after["numbered_equations"])==1817
    assert not re.search(r"\\tag\*?\{",proposed)
    old_statement_records=re.findall(r"\\StatementRecord\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}",s)
    new_statement_records=re.findall(r"\\StatementRecord\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}",proposed)
    assert old_statement_records==new_statement_records
    new_all_labels=collections.Counter(re.findall(r"\\label\{([^{}]+)\}",proposed))
    assert new_all_labels==all_labels+collections.Counter(new_labels)
    assert collections.Counter(re.findall(r"\\hypertarget\{([^{}]+)\}",proposed))==all_anchors
    after_labels={l:e for e in after["numbered_equations"] for l in e["labels"]}
    for e in data["numbered_equations"]:
        assert after_labels[e["target_label"]]["new_number"]==e["new_number"]
    # Per-display mathematical payload identity, with only the enumerated presentation maps removed.
    display_comparison=[]
    for before_b,after_b in zip(blocks,after_blocks):
        oldbody=s[before_b["begin_end"]:before_b["end_start"]]
        newbody=proposed[after_b["begin_end"]:after_b["end_start"]]
        oldbody=re.sub(r"\\tag\{[^{}]+\}","",oldbody)
        for label in new_labels:
            newbody=newbody.replace(r"\label{"+label+"}","")
        if before_b["environment"]=="align*" and before_b["tags"]:
            newbody=newbody.replace(r"\notag","")
        # Literal references inside math have their exact inverse citation map.
        for e in edits:
            if e["kind"]=="literal_equation_reference" and before_b["begin_end"]<=e["start"]<before_b["end_start"]:
                assert newbody.count(e["new"])>=1
                newbody=newbody.replace(e["new"],e["old"],1)
        assert oldbody==newbody,("mathematical payload changed",before_b["line"])
        display_comparison.append(dict(
            old_line=before_b["line"],old_environment=before_b["environment"],
            new_environment=after_b["environment"],old_tags=[t["value"] for t in before_b["tags"]],
            old_display_sha256=before_b["sha256"],new_display_sha256=after_b["sha256"],
            mathematical_payload_sha256=digest(oldbody),payload_byte_identical=True,
            originally_numbered=bool(before_b["tags"]) or before_b["environment"] in {"equation","align","multline"}))
    after_refs=refsmod.collect(proposed,after,legacy_tag_map=by_tag)
    assert [x["old"] for x in refs["seriesref_definitions"]]==[x["old"] for x in after_refs["seriesref_definitions"]]
    # No numbered-equation citation is left as an old literal. The seven section identifiers remain.
    assert len(after_refs["literal_candidates"])==7,after_refs["literal_candidates"]
    assert all(not (proposed[x["start"]-1:x["start"]]=="(" and proposed[x["end"]:x["end"]+1]==")")
               for x in after_refs["literal_candidates"])
    assert "(C.IR.7)" not in proposed and "(C.IR.8)" not in proposed
    return proposed,dict(
        source_sha256=digest(s),proposed_source_sha256=digest(proposed),
        source_bytes=len(s.encode()),proposed_source_bytes=len(proposed.encode()),
        equation_map=data["numbered_equations"],section_counts=data["section_numbered_counts"],
        original_display_census=data["displays"],display_comparison=display_comparison,
        added_labels=new_labels,atomic_edits=edits,inverse_edits=inverse,
        literal_reference_transport=reference_changes,
        dynamic_reference_transport=refs["dynamic_body_references"],
        seriesref_transport=refs["seriesref_definitions"],
        literal_range_transport=ranges,unchanged_section_collisions=non_equation_collisions,
        unchanged_single_letter_math=single_math,CIR_scope_status=scope_status,
        verification=dict(
            numbered_equations=1817,old_manual_tags=1764,
            all_displays=len(blocks),unnumbered_displays=sum(not x["numbered"] for x in data["displays"]),
            all_display_payloads_byte_identical=True,
            all_existing_labels_preserved=True,all_hypertargets_preserved=True,
            all_statement_record_owners_statuses_tags_preserved=True,
            added_equation_labels=len(new_labels),
            seriesref_definitions_byte_identical=len(refs["seriesref_definitions"]),
            literal_equation_references_replaced=sum(e["kind"]=="literal_equation_reference" for e in edits),
            inverse_transform_exact=True,canonical_mutations=0))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=Path,default=ROOT/"S6_SERIES_PUBLISH_II.tex")
    ap.add_argument("--stem",default="v1")
    ap.add_argument("--emit-temporary",type=Path)
    args=ap.parse_args()
    assert re.fullmatch(r"[A-Za-z0-9_]+",args.stem)
    index=OUT/(PRE+args.stem+"_proposal_index.json")
    assert not index.exists(),"Existing proposal versions are immutable"
    s=args.source.read_text()
    proposed,meta=transform(s)
    now=datetime.now(timezone.utc).isoformat()
    outputs=[]
    def write(suffix,text):
        p=OUT/(PRE+args.stem+"_"+suffix)
        assert not p.exists()
        p.write_text(text)
        outputs.append(dict(path=str(p.relative_to(ROOT)),sha256=digest(text),bytes=len(text.encode())))
        return p
    def js(suffix,value):
        return write(suffix+".json",json.dumps(value,ensure_ascii=False,indent=2)+"\n")
    for key in ["atomic_edits","inverse_edits","literal_reference_transport","dynamic_reference_transport",
                "seriesref_transport","literal_range_transport","unchanged_section_collisions",
                "unchanged_single_letter_math","display_comparison"]:
        js(key,meta[key])
    # Full mathematical source is represented by a reversible diff, not a checkpoint copy.
    write("source_diff.patch","".join(difflib.unified_diff(
        s.splitlines(True),proposed.splitlines(True),
        fromfile=str(args.source),tofile="proposed/Paper_II_D19.tex")))
    rows=meta["equation_map"]
    header=["old_tag","new_number","target_label","section","ordinal","line","environment","row","labels","hypertargets","new_labels_added"]
    import io
    buffer=io.StringIO();writer=csv.DictWriter(buffer,fieldnames=header,delimiter="\t",lineterminator="\n")
    writer.writeheader()
    for e in rows:
        writer.writerow({k:(";".join(e[k]) if isinstance(e.get(k),list) else e.get(k,"")) for k in header})
    write("equation_map.tsv",buffer.getvalue())
    js("source_and_verification",dict(
        created_utc=now,source_path=str(args.source),
        source_sha256=meta["source_sha256"],proposed_source_sha256=meta["proposed_source_sha256"],
        source_bytes=meta["source_bytes"],proposed_source_bytes=meta["proposed_source_bytes"],
        section_counts=meta["section_counts"],verification=meta["verification"],
        CIR_scope_status=meta["CIR_scope_status"],
        manual_tag_policy="Every literal tag is replaced by the ordinary equation counter. All existing automatic equation rows share the same section counter.",
        unnumbered_display_policy="Every originally unnumbered display remains unnumbered and has a byte-identical mathematical payload.",
        rebind_policy="Run this read-only-source proposal builder against the later canonical source with a new stem; it rescans all sections/displays/references and rejects unsupported or unresolved cases. Never replace a later canonical file by the temporary proposed whole source."))
    if args.emit_temporary:
        temp=args.emit_temporary.resolve()
        assert not temp.is_relative_to(ROOT),"Full temporary source must stay outside the checkpoint tree"
        temp.mkdir(parents=True,exist_ok=True)
        (temp/"S6_SERIES_PUBLISH_II_D19_before.tex").write_text(s)
        (temp/"S6_SERIES_PUBLISH_II_D19_proposed.tex").write_text(proposed)
    result=dict(created_utc=now,immutable=True,status="reversible proposal; canonical source not written",
                source_sha256=meta["source_sha256"],proposed_source_sha256=meta["proposed_source_sha256"],
                verification=meta["verification"],files=outputs)
    index.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(dict(index=str(index.relative_to(ROOT)),index_sha256=hashlib.sha256(index.read_bytes()).hexdigest(),
                         source_sha256=meta["source_sha256"],proposed_source_sha256=meta["proposed_source_sha256"],
                         verification=meta["verification"],outputs=len(outputs)),indent=2))

if __name__=="__main__":main()
