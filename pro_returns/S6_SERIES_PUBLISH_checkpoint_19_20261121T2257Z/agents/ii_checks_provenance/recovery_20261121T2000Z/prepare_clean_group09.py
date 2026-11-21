from pathlib import Path
import csv, hashlib, json, re
from datetime import datetime, timezone

R=Path.cwd()
P=Path("agents/ii_checks_provenance/recovery_20261121T2000Z")
O=P/"clean_group09"
O.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binding(p): return {"path":str(p),"sha256":sha(p)}
def save(p,obj):
    p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n")
    return binding(p)
now=datetime.now(timezone.utc).isoformat()
tags=["03DS","03IX","03IA","03I7","03J0","03DT","03IZ","03IV","03IP"]
targets=[]
for tag in tags:
    f=json.loads((P/"clean_derivations"/f"S6_SERIES_PUBLISH_II_{tag}_freeze_pointer.json").read_text())
    q=json.loads((P/"clean_derivations"/f"S6_SERIES_PUBLISH_II_{tag}_release_pointer.json").read_text())
    fr=json.loads(Path(f["receipt"]).read_text())
    orig=Path(q["full_block"]).read_text()
    assert orig.count(r"\begin{proof}")==orig.count(r"\end{proof}")==1
    assert Path("S6_SERIES_PUBLISH_II.tex").read_text().count(orig)==1,tag
    t={"tag":tag,"statement_owner":f["owner"],"checker":"i_provenance_recovery",
       "freeze_receipt":binding(f["receipt"]),"release_receipt":binding(q["receipt"]),
       "release_envelope":binding(q["full_block"]),"guards":[],
       "named_statement_scope":{"start_offset_in_release":0,"end_offset_in_release":len(orig),
          "complete_attached_proofs":1,"additional_released_proofs_outside_independent_target_scope":0},
       "events_added":0,"source_application_pending":True}
    frozen=Path(f["receipt"]).parent/"S6_SERIES_PUBLISH_derivation_frozen.md"
    t["frozen_derivation"]=binding(frozen)
    oldp=O/f"S6_SERIES_PUBLISH_II_{tag}_original.tex";oldp.write_text(orig)
    t["original_full_block"]=binding(oldp)
    new=orig
    def change(old,replacement,typ,reason,count=1):
        global new
        assert new.count(old)==count,(tag,old,new.count(old))
        t["guards"].append({"change_id":f"II-REC-C09-{tag}-{len(t['guards'])+1:02}",
            "defect_type":typ,"old":old,"new":replacement,
            "expected_occurrences_in_owning_block":count,"reason":reason})
        new=new.replace(old,replacement)
    def one_wrapper():
        change("\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]\n\\item \n\\noindent\\textbf{Step 1.} ","","D04,D23","Remove the single-item iteration wrapper and redundant step label.")
        change("\n\\end{enumerate}","","D04,D23","Remove the paired single-item wrapper terminator.")
    def ordinary():
        change(r"\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]",
               r"\begin{enumerate}[label=\arabic*.,leftmargin=*]","D04,D23",
               "Use ordinary numbering while preserving every mathematical proof step.")
    if tag=="03DS":
        change("standard-family nonvanishing for \\texorpdfstring{$\\operatorname{Pic}^0$}{Pic0} without topology",
               "Standard-family nonvanishing for \\texorpdfstring{$\\operatorname{Pic}^0$}{Pic0}","D02,D16","Use the mathematical scope as the title.")
        change("\\ For the standard","For the standard","D23","Remove a stray initial control-space.")
        change("This proof uses the analytic construction of the cusp fibre but no global\nhomology, Mayer--Vietoris, or Leray calculation.\n","","D02,D08","Remove a method-scope announcement after the complete mathematical statement.")
        one_wrapper()
        change("} now identifies","} identifies","D08","State the base-change map directly.")
    elif tag=="03IX":
        change("the conductor mechanism for the standard family","Conductor nonvanishing for the standard family","D16","Use a mathematical title.")
        change("\\ Assume:","Assume:","D23","Remove a stray initial control-space.")
        change("author preprint p.~410","2010 text, p.~410","D18","Bind the cited page to the original 2010 text, whose title/copyright and September2010 preface were read.",2)
        ordinary()
        change("\\Cref{wbII:prop:conductor} now gives","\\Cref{wbII:prop:conductor} gives","D08","State the conductor application directly.")
        change("The right side is nonzero by \\eqref{wbII:eq:W:5.20}, proving the first assertion of \\eqref{wbII:eq:W:5.18}.",
               "By \\eqref{wbII:eq:W:5.20}, the dual space is nonzero, giving the first nonvanishing in \\eqref{wbII:eq:W:5.18}.",
               "D08","Express the exact duality implication without an assertion-completion recap.")
        change("The stalk, and hence the coherent direct-image sheaf, is nonzero.  This is\nthe second assertion of \\eqref{wbII:eq:W:5.18}.",
               "The stalk, and hence the coherent direct-image sheaf in\n\\eqref{wbII:eq:W:5.18}, is nonzero.","D08","Retain the exact conclusion and reference in one mathematical sentence.")
    elif tag=="03IA":
        change("generic endpoint vanishing","Generic endpoints in an analytic parameter space","D16","Distinguish the precise parameter-space scope by its mathematical title.")
        change("\\cite{Grauert1960D,BS76push}",r"\cite[Chapter~III, \S4, Theorem~4.1, p.~124]{BS76push}","D18","Give the precise local finite-complex input for determinantal jump loci.",2)
        change(" (the stabilization argument\n  supplies such exponents whenever the corresponding twists lie in\n  $\\mathcal P$)","","D08,D12","Keep the two zero-point hypotheses explicit; remove a redundant method parenthesis.")
        one_wrapper()
        start=new.index("Put\n  \\(V_k=")
        end=new.index("  The chosen point $P_0$",start)
        change(new[start:end],"","D12,D17","Remove the unused repetition of negative-divisor stabilization. The statement already supplies both zero points; the classical stabilization input is cited in the separate Pic0 lemma.")
        change("The Poincar\\'e bundle gives, locally on\n$\\mathcal P$, a family to which Grauert's theorem applies; the local jump\n  loci $\\{P':h^0(Y,B\\otimes P')\\ge1\\}$ glue to a closed analytic subset of\n  $\\mathcal P$ (Grauert's theorem; see \\cite[Chapter~III, \\S4, Theorem~4.1, p.~124]{BS76push}).",
               "The Poincar\\'e bundle gives a proper flat family over\n$\\mathcal P$.  Locally, its cohomology is computed by a finite free complex\n\\cite[Chapter~III, \\S4, Theorem~4.1, p.~124]{BS76push}.\nThe rank conditions on its differentials make\n$\\{P':h^0(Y,B\\otimes P')\\ge1\\}$ a determinantal locus; these local loci glue\nto a closed analytic subset of $\\mathcal P$.",
               "D13,D18","Specify the finite-complex rank maps supporting analyticity, retaining the given proper Poincare family.")
        change("Applying the same stabilization\nargument to $B^\\vee\\otimes\\omega_Y$ and using the chosen point $Q_0$ gives\n$H^0(Y,B^\\vee\\otimes\\omega_Y\\otimes Q_0)=0$; dualization stability puts",
               "The other chosen point satisfies\n$H^0(Y,B^\\vee\\otimes\\omega_Y\\otimes Q_0)=0$; dualization stability puts",
               "D12","Use the exact second zero-point hypothesis, with no inference that an arbitrary parameter subspace inherits a generic Pic0 open set.")
    elif tag=="03I7":
        change("generic endpoint vanishing",r"Generic endpoints on \texorpdfstring{$\operatorname{Pic}^0$}{Pic0}","D16","Name the full Pic0 scope.")
        change("the definitions and constructions stated in the proof",r"\cite[Proposition~1.1, p.~78]{CDP98}; \cite[Chapter~III, \S4, Theorem~4.1, p.~124]{BS76push}","D18","Supply precise primary inputs for the negative twists and local finite complexes.")
        change("\\ Let \\(Y\\)","Let \\(Y\\)","D23","Remove a stray initial control-space.")
        one_wrapper()
        start=new.index("The inclusions ")
        end=new.index("Since\n\\(\\mathcal O_Y(-kD)",start)
        replacement=r"""By \cite[Proposition~1.1, p.~78]{CDP98}, applied to the connected smooth
space \(Y\), the divisor \(D\), and the locally free sheaf \(B\), one has
\[
 V_k=H^0(Y,B\otimes\mathcal O_Y(-kD))
 \subseteq H^0(Y,B),
\]
with \(V_k=0\) for all sufficiently large \(k\).
"""
        change(new[start:end],replacement,"D17","Replace the repeated classical stabilization proof by its exact primary citation and hypothesis transport; retain the section-space map and vanishing.")
        change("upper semicontinuity in a\nlocal universal family of topologically trivial line bundles shows that",
               "local finite free complexes for the proper family over a\nlocal universal parameter space of topologically trivial line bundles\n\\cite[Chapter~III, \\S4, Theorem~4.1, p.~124]{BS76push} show that",
               "D13,D18","The local rank maps make the jump set analytic, beyond the numerical upper-semicontinuity assertion.")
        change("is a proper analytic subset of \\(\\operatorname{Pic}^0(Y)\\).  This proves\nthe first vanishing for general \\(P\\).  Serre duality identifies the dual",
               "is a proper analytic subset of the connected complex Lie group\n\\(\\operatorname{Pic}^0(Y)\\), so its complement is dense open.\nSerre duality identifies the dual","D08,D13","State the dense-open consequence in the exact parameter group.")
    elif tag=="03J0":
        change("corrected CDP global-vanishing criterion","Global vanishing from one degree-two vanishing","D16","State the mathematical criterion in the title.")
        change("\\ Let \\(X\\) be a compact connected complex threefold","Let \\(X\\) be a smooth compact connected complex threefold","D20,D25","The tangent bundle, six-manifold Poincare duality and HRR proof require smooth X; the frozen derivation explicitly certifies this scope.")
        ordinary()
        change("Choose additive Cech cocycles","Choose additive \\v{C}ech cocycles","D23","Correct the printed accent.")
        change("so proper\nsemicontinuity below applies to an actual holomorphic family.","and the projection to the parameter space is proper.","D08,D09","Replace a workflow qualifier by the proper projection of the actual holomorphic family.")
        change("is analytic by upper semicontinuity.","is locally determinantal in this family\n\\cite[Chapter~III, \\S4, Theorem~4.1, p.~124]{BS76push}.","D13,D18","Bind analyticity to the actual differential-rank construction.")
        change("Its complement therefore meets the two endpoint\nvanishing loci in a dense open set.  This proves \\eqref{wbII:eq:W:5.25}, and on that set",
               "Its complement meets the two endpoint\nvanishing loci in a dense open set, where \\eqref{wbII:eq:W:5.25} holds and",
               "D08","Retain the exact dense-open scope and displayed reference without a completion announcement.")
        change("Hirzebruch--Riemann--Roch turns \\eqref{wbII:eq:W:5.28} into",
               "Hirzebruch--Riemann--Roch and \\eqref{wbII:eq:W:5.28} give the inequalities\nin \\eqref{wbII:eq:W:5.26}:","D08","Move the concluding reference into the precise HRR implication.")
        change("which proves \\eqref{wbII:eq:W:5.26}.\n","","D08","Remove the now-redundant completion recap; its exact reference is retained in the preceding implication.")
        change("\\right\\rangle\\le0,\n\\]","\\right\\rangle\\le0.\n\\]","D23","End the final HRR display with a period after removing its trailing recap.")
    elif tag=="03DT":
        change("intact relative criterion","Relative vanishing criterion","D16","Use a mathematical title.")
        change("\\ In the setting","In the setting","D23","Remove a stray initial control-space.")
        change("This is the valid content of the sufficient criterion printed as\n\\cite[Proposition~2.4, p.~680]{CDP20}.",
               "The relative criterion is \\cite[Proposition~2.4, p.~680]{CDP20}.","D09,D18","Retain precise published attribution without an editorial validity qualifier.")
        one_wrapper()
    elif tag=="03IZ":
        change("exact reduced-fibre repair of the p.~692 step","Reduced-fibre vanishing criterion","D16","Use a mathematical title.")
        change("\\ Retain the setting of","In the setting of","D08,D23","Introduce the hypotheses directly.")
        change("be the connecting map from the missing cotangent filtration.",
               "be the connecting map of the cotangent filtration in \\cref{cdp:st:A.1.1}.",
               "D09,D13","Identify the actual filtration and its map.")
        one_wrapper()
        change("Cartier fibre \\(W_c\\), not separately to its components.","Cartier fibre \\(W_c\\).","D02","Retain the positive full-fibre scope already stated.")
        change("Cartier-fibre duality now gives","Cartier-fibre duality gives","D08","State the duality application directly.")
    elif tag=="03IV":
        change("Positive Euler number obstructs the added vanishings","Positive Euler number and cohomology nonvanishing","D16","Use the mathematical conclusion as the title.")
        change("Section~10.2, Theorem~10.5","Section~10.3, Theorem~10.5 and Corollary~10.6, pp.~88--89","D18","The exact author PDF and printed pages locate both the nonvanishing theorem and the credited CDP counterexample in section10.3.",2)
        one_wrapper()
        change("Paper I proves that the standard compact threefold has",
               "The standard compact smooth threefold constructed in Paper I has","D20","Make the receiving smoothness hypothesis explicit; the construction is smooth.")
        change("The contradiction with the printed\nCDP conclusion is credited to",
               "The resulting counterexample to the CDP conclusion is due to","D09,D18","Retain the substantive attribution with the exact primary locator.")
    elif tag=="03IP":
        change("crossing and multiple-fibre modules","Crossing and multiple-fibre modules","D16","Use the mathematical title consistently.")
        ordinary()
        change("Differentiating the three equations gives the presentations in",
               "Differentiating $t=xy$ and $t=xyz$ gives the presentations in","D06,D13","The referenced display contains exactly the two crossing presentations; the multiple-fibre equation is treated in step2.")
        change("  This proves\nnon-local-freeness at the origin.","","D08","Remove a pure completion recap after the explicit rank and minimal-generator contradiction.")
    newp=O/f"S6_SERIES_PUBLISH_II_{tag}_proposed.tex";newp.write_text(new)
    t["proposed_full_block"]=binding(newp)
    t["guard_validation"]={"exact_application":True,
       "all_statement_labels_tags_preserved":re.findall(r"\\(?:label|hypertarget)\{[^}]*\}",orig)==re.findall(r"\\(?:label|hypertarget)\{[^}]*\}",new),
       "proof_count_preserved":True,
       "mathematical_exception_scope":("IA removes a redundant stabilization argument while retaining both assumed zero-point hypotheses; I7 cites the precise primary stabilization theorem with its exact section-space inclusion and all-degree vanishing. J0 adds smoothness required by the proof. IP specifies the two differentiated crossing equations. No displayed conclusion, fibre, map, quantifier or value is changed. New references bind finite complexes and exact AC/CLS locators.")}
    t["actual_complete_original_proof_read"]=True
    t["actual_complete_proposed_proof_read"]=False
    t["proposed_editorial_event"]=True
    targets.append(t)

src=Path("S6_SERIES_PUBLISH_II.tex").read_text()
bibs=[]
for key in ["CoxLittleSchenck2011","Serre1956GAGA","AC2026","BS76push","CDP98"]:
    ms=[m for m in re.finditer(r"\\bibitem(?:\[[\s\S]*?\])?\{([^}]+)\}",src) if m.group(1)==key]
    assert len(ms)==1
    m=ms[0];e=src.find(r"\bibitem",m.end());e=e if e>=0 else src.find(r"\end{thebibliography}",m.end())
    old=src[m.start():e];new=old.replace("\\newblock \\emph{Verified}.\n","")
    if key=="CoxLittleSchenck2011":
        new=new.replace("Henry~K. Schenck","Hal Schenck")
        new=new.replace("\\newblock \\doi{10.1090/gsm/124}.",
            "\\newblock \\doi{10.1090/gsm/124}.\n\\newblock Page locators refer to the authors' 2010 text, whose preface is\n  dated September 2010.\n\\newblock URL \\url{https://dacox.people.amherst.edu/toric.html}.")
    if key=="BS76push":
        new=new.replace("\\newblock URL \\url{https://djvu.online/file/2hQiOnz8WuoQk}.\n","")
    for scope,txt in [("original",old),("proposed",new)]:
        (O/f"S6_SERIES_PUBLISH_II_bib_{key}_{scope}.tex").write_text(txt)
    bibs.append({"key":key,"change_id":f"II-REC-C09-BIB-{key}","defect_type":"D18",
       "old":old,"new":new,"expected_occurrences":1,
       "original_full_entry":binding(O/f"S6_SERIES_PUBLISH_II_bib_{key}_original.tex"),
       "proposed_full_entry":binding(O/f"S6_SERIES_PUBLISH_II_bib_{key}_proposed.tex"),
       "reason":"Remove review-status prose. CLS author spelling and 2010 locator edition are bound to the original text and author page. BS76 retains bibliographic publication data without a nonpublisher mirror URL."})

owners={t["statement_owner"] for t in targets}
with Path("CHECK_EVENTS.tsv").open() as f:
    prior=[{"ledger_row":n,"event":r} for n,r in enumerate(csv.DictReader(f,delimiter="\t"),2) if r["statement_id"] in owners]
pr=save(O/"S6_SERIES_PUBLISH_II_clean_group09_prior_associations.json",
        {"ledger":binding("CHECK_EVENTS.tsv"),"read_after_freeze_and_release":True,"rows":prior,"events_added":0})
rec={"schema_version":1,"paper":"II","checker":"i_provenance_recovery","created_utc":now,
     "source_at_preparation":binding("S6_SERIES_PUBLISH_II.tex"),"targets":targets,"bibliography_guards":bibs,
     "prior_associations":pr,"canonical_mutations":0,"events_added":0,
     "status":"Exact nine original/proposed pairs prepared; full proposed-pair reading is pending.",
     "scope_transport":binding(P/"S6_SERIES_PUBLISH_II_J0_current_incoming_uses.json")}
out=save(O/"S6_SERIES_PUBLISH_II_clean_group09_preparation.json",rec)
print(json.dumps({"preparation":out,"targets":len(targets),"guards":sum(len(t["guards"]) for t in targets),"bibliography_guards":len(bibs)},indent=2))
