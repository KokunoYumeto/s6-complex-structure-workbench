"""Apply exact final-read findings in the cyclic-cover unit."""
from __future__ import annotations
from datetime import datetime, timezone
import S6_SERIES_PUBLISH_c8_integrate_units as u
import S6_SERIES_PUBLISH_c8_root_units as r

path=u.WORK / "root/cyclic_homology.tex"
before=path.read_text(encoding="utf-8")
after=before
fields,rows=r.table(r.DEFECTS)
changes=[]
items=[
 ("DELPEZZO-NAME","D05",
  r"$\widetilde W_p$ for the inverse image of the cusp $W$.",
  r"$\widetilde W_p$ for the inverse image of the cusp $W$."+"\n"+r"We write $dP_6$ for the blowup of $\mathbb P^2$ at its three coordinate points.",
  "Define the named component surface before the cusp theorem; its six-ray identification remains proved in KB."),
 ("PARAMETER-ONCE","D13",
  "Put $d=|12\\ell_0-4\\ell_1-3\\ell_2|$ for an admissible member $X_p$.\n",
  "For every admissible member $X_p$,\n",
  "Use the numbered shared parameter definition while retaining the theorem's full admissible scope."),
 ("REAL-INVERSE","D20",
  r"\eta_j=\Pi_c(s_j)^{-1}",
  r"\eta_j=\bigl(\Pi_c(s_j)|_{\mathbb R^4}\bigr)^{-1}",
  "Specify the inverse as the admissible real period isomorphism R4 to C2 used in the stated real marking. The complex 2-by-4 matrix notation alone did not specify that inverse's domain."),
 ("CONCLUSION-PROSE","D23",
  "Thus for $d>1$ the cover is also not a connected sum of copies of\n$S^2\\times S^4$. \\end{theorem}",
  "For $d>1$ the cover is not a connected sum of copies of\n$S^2\\times S^4$.\n\\end{theorem}",
  "Remove the unneeded also and restore a separate environment-ending line; the exact-order homology obstruction remains fully proved."),
 ("TAIL-REPETITION","D11",
  "inverse induced map. The exhibited subgroup $\\mathbb Z/d$ of $H_2$ also shows that\nthe torsion-free homology hypothesis fails for $d>1$.",
  "inverse induced map.",
  "End at the proved homology-isomorphism obstruction, removing its repeated formulation as an unnamed criterion's failed hypothesis."),
]
for key,kind,old,new,reason in items:
 ident="III-C8-CYCLIC-FINISH-"+key
 assert after.count(old)==1,key
 assert not any(x['change_id']==ident for x in rows)
 after=after.replace(old,new,1)
 changes.append(dict(change_id=ident,type=kind,statement_id="maps:src:D.1.1--D.1.4",old_location="complete cyclic-unit readback",old_page="pending page concordance",new_location="Cyclic covers and integral homology",new_page="pending final PDF",old_text=old,new_text=new,reason=reason,review_status="whole source reviewed; final PDF review open"))

ipath=u.WORK / "root/cyclic_invariants.tex"
ibefore=ipath.read_text(encoding="utf-8")
heading="\\subsection{Characteristic classes and smooth classifications of cyclic covers}\n"
assert not ibefore.startswith(heading)
iafter=heading+ibefore
changes.append(dict(change_id="III-C8-CYCLIC-INVARIANTS-BOUNDARY",type="D14",statement_id="maps:src:D.1.5",old_location="former common cyclic subsection",old_page="pending page concordance",new_location="Characteristic classes and smooth classifications of cyclic covers",new_page="pending final PDF",old_text="",new_text=heading,reason="The Euler/cusp/homology prerequisite has moved before the framing argument. Give the remaining characteristic/classification material its real subsection boundary. All 28 criteria in this separated unit remain open; no progress follows from the boundary.",review_status="boundary applied; complete unit review pending"))
source=u.repairs.SOURCE.read_text(encoding="utf-8")
first_line=ibefore.splitlines(keepends=True)[0]
assert source.count(before)==source.count(first_line)==1
# The original invariant statements are not yet one contiguous canonical
# fragment: K9 is still in its later received-application subsection. This
# boundary applies only at KE; the full invariant unit remains unreviewed.
candidate=source.replace(before,after,1).replace(first_line,heading+first_line,1)
u.check_permanent_identifiers(source,candidate)
path.write_text(after,encoding="utf-8",newline="\n")
ipath.write_text(iafter,encoding="utf-8",newline="\n")
u.repairs.SOURCE.write_text(candidate,encoding="utf-8",newline="\n")
r.write_table(r.DEFECTS,fields,rows+changes)
print("UTC",datetime.now(timezone.utc).isoformat())
print("EXACT_EDIT_ROWS",len(changes))
print("IDENTIFIERS_PRESERVED; NO_CREDIT_ASSIGNED")
