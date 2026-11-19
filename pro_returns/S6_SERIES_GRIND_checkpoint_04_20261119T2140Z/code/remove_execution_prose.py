"""Move execution history out of research prose; retain full before/after receipts."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];changes=[]
def patch(paper,old,new,reason):
 p=R/f'parts/{paper}.body.linked.tex';s=p.read_text()
 n=s.count(old)
 if not n:
  if new and new not in s:raise ValueError((paper,old[:80]))
  i=s.find(new) if new else -1;status='already applied'
 else:
  if n>1 and old!=r'\medskip\noindent\textbf{Completed proof and retained submission history.}':raise ValueError(('nonunique',paper,old[:80],n))
  i=s.index(old);status='applied'
 prior=re.findall(r'\\StatementRecord\{([^}]+)\}',s[:i]) if i>=0 else []
 label=prior[-1] if prior else ''
 if n:p.write_text(s.replace(old,new))
 changes.append(dict(paper=paper,label=label,old=old,new=new,reason=reason,status=status,occurrences=n))
 (R/'analysis/execution_prose_changes.json').write_text(json.dumps(changes,indent=2))
patch('I',r'''This identifier recorded an open step at the earlier checkpoint:
the minimum principle in \ref{push:src:D.4.2} did not exclude additional maxima,
and the exact crossing in \ref{push:src:D.4.5} did not classify all levels. That
open status is superseded by \ref{push:src:D.4.7}--\ref{push:src:D.4.8} below. We retain the
record of the unsuccessful reduction.''',r'''The minimum principle in \ref{push:src:D.4.2} and the crossing
in \ref{push:src:D.4.5} enter the complete level classification through
the nonvanishing and boundary estimates of
\ref{push:src:D.4.7}--\ref{push:src:D.4.8}.''','Replace chronology by the actual dependency.')
patch('III',r'''Root independently read the full proof and replayed all
$12$ actual marked bases, $95$ normalization comparisons
and $1638$ global Smith calculations successfully.
An independent adversarial review by the fourfolds
agent also checked \eqref{maps:eq:D.SL17}--\eqref{maps:eq:D.SL24}, including the
nonzero order-two correction and the integer phase lift.
''','', 'Move retained proof/computation provenance to the statement checks.')
patch('III','The checkpoint follows the slice $s=0$ and varies\n$u$ towards zero; the present construction fixes $u\\ne0$ and varies\n$s$.','The first slice has $s=0$ and varies\n$u$ towards zero; the second fixes $u\\ne0$ and varies\n$s$.','State the two actual parameter slices.')
patch('IV',r'''\item The first clipped-polygon attempt failed because some parent triangle columns were clockwise; its source and failure output are preserved. The next ordered-factor overlay was interrupted after thousands of subdivisions; it remains a documented incomplete attempt. The present calculation uses the explicit alternative zero-end fan and the finite residue search above. A peer audit identified the missing native height unit \(R=pP\) in the preliminary output; that preliminary output is preserved, and CFg is in the current certificate.''',r'''\item The zero-end fan and finite residue calculation retain the
native height unit \(R=pP\) in the source map CFg. The oriented parent
triangle columns and the height-one source charts therefore use the
same prescribed marking.''','Keep the geometric correction and move failed executions to provenance.')
patch('IV',r'''Local calculation sent to checks before checkpoint24, with the full
common 510-cone extension completed below. The executed refinement has
558 regular four-dimensional cones and retains the complete source,
point-line and period morphisms.''',r'''The common refinement below has 558 regular four-dimensional cones;
it extends the 510-cone comparison with the complete source,
point-line and period morphisms.''','State the exact cone counts and maps without execution chronology.')
patch('IV',r'''Working calculation owned by blind\_control, complementary to
\path{part3_e6_selected_infinity_working.md} (the source/Miller/collar calculation).
The maps below have been derived on their displayed charts. The complementary
root corner, the full Cartier graph there, and its completed suspension
attachment are still being calculated. The actual ordinary quotient,
point-line chain and cap-domain overlaps are written below. No return
or compact global boundary is assigned by this note.''',r'''This argument gives the ordinary quotient, point-line chain,
cap-domain overlaps and their full annular groupoid. The complementary
source/Miller/collar maps and root-corner Cartier graph enter at their
specified interfaces in the completed suspension construction below.''','Replace ownership and intermediate readiness by the actual interfaces.')
patch('IV',r'''Working exact-map audit, owned by blind\_control. The source, Cartier
and root inputs are EI.1-\/-9 and EIR.1-\/-10. This note constructs the
selected \(T_0\) toric patch and its source-graph refinements, with
the full period and line maps. It assigns no characteristic number
or source return. The original finite cap stays on the domain in
EIR.9 and retains the EIR.28 annular map.''',r'''The source, Cartier and root inputs are EI.1--9 and EIR.1--10.
They give the selected \(T_0\) toric patch and its source-graph
refinements with the full period and line maps. The original finite
cap stays on the domain in EIR.9 and retains the EIR.28 annular map.''','Retain the explicit source and cap maps; move reviewer attribution out.')
patch('IV',r'''Working ledger owned by blind\_control, saved before checkpoint24.
The full finite quotient resolution is owned by root. Fourfold owns
the source/Miller/point-line atlas EI.1-\/-12. The detailed root and
annular maps are EIR.1-\/-11; the independently checked local toric
maps are SIT.1-\/-5. No numerical return is assigned here.''',r'''The source/Miller/point-line atlas is EI.1--12. The root and annular
maps are EIR.1--11, and the local toric maps are SIT.1--5. The finite
quotient resolution uses these exact domain and overlap arrows.''','Replace working assignments by the actual mathematical references.')
patch('IV','ASI.4. Completed local interfaces after checkpoint24','ASI.4. The complete local interfaces','Remove execution timing from a proof heading.')
patch('IV',"\\(\\mathcal C\\) is the positive generator in this run's convention.","\\(\\mathcal C\\) is the positive generator in the fixed orientation.",'State the orientation as mathematical data.')
patch('IV',r'''The checkpoint36 source reports the additional completed sectors in
\cref{night:P3K.109}, \cref{night:P3K.110}, \cref{night:P3K.111}, \cref{night:P3K.112}, \cref{night:P3K.113}, \cref{night:P3K.114}, \cref{night:P3K.115}, \cref{night:P3K.116}, \cref{night:P3K.117}, \cref{night:P3K.118}, \cref{night:P3K.119}. Their complete supplied
arguments are retained below with their receiving check scopes.
The current receiving review of those arguments remains explicit in
each record; the source's proof status is preserved separately.
''',r'''The further endpoint, selected-cusp and ordinary-cap constructions
are stated with their full arguments in
\cref{night:P3K.109,night:P3K.110,night:P3K.111,night:P3K.112,night:P3K.113,night:P3K.114,night:P3K.115,night:P3K.116,night:P3K.117,night:P3K.118,night:P3K.119}.
''','Replace intake history by exact theorem locations; statuses stay in headers.')
patch('IV',r'''The continuation also
retains the pending whole-proof, new-computation and credit gates on
the newly received results.''','', 'Retain review gates in check files.')
patch('IV',r'''\item The checkpoint36 intake places the eleven further source results
named above in this paper with their complete arguments and receiving
review records. Its exact source comparison finds the preceding
287 theorem/proof blocks unchanged and this reduction record enlarged.
The source's remaining mathematical boundary is the OS45 \(I_9\),
handle and infinity sectors, additional ordinary clutch slots with
nonzero total norm, and endpoint loci outside the completed domains.
The new receiving proof checks remain separately recorded, with no
promotion from source status alone.''',r'''\item The remaining source-moduli constructions are the OS45
\(I_9\), handle and infinity sectors, additional ordinary clutch
slots with nonzero total norm, and endpoint loci outside the stated
domains. They require their full source, line, root, annular and
closing comparisons.''','Keep the exact mathematical open gate and move the intake counts out.')
patch('IV',r'''\subsection{Checkpoint36 source results with continuation review pending}

The following source statements and their complete supplied arguments are
retained here while their continuation checks are completed. Their source
records report proofs by GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6\_06\_BLIND, 16--18 November 2026. Each receiving status records the
current scope below; importing the source does not add a proof check.
The separate event ledger records the algebraic substeps already checked
with new code and every later mathematical comparison.
''',r'''\subsection{Further marked endpoints and source-moduli loops}
The following statements retain the original source section, point line,
finite roots, affine characters, ordinary reference and specified fan.
Their separate construction maps and exact parameter domains are given
with each statement.
''','Put model/effort/check attribution in methodology and check files.')
patch('IV',r'''\medskip\noindent\textbf{Completed proof and retained submission history.}''',r'''\medskip\noindent\textbf{The complete source and cap construction.}''','Use a mathematical proof heading.')
patch('IV','The original pending-review notice is retained below. The complete C45.1-\\/-8 proof has now passed both full independent geometric audits reproduced afterward. Its primary readiness and all preceding attempts remain preserved.\n\n','', 'Move submission/check history to the exact statement record.')
patch('IV','The original preparation-stage readiness record remains preserved.\n','', 'Move readiness history to checks.')
p=R/'parts/IV.body.linked.tex';s=p.read_text()
for m in list(re.finditer(r'\[Source result P3K\.(\d+) under continuation review\]',s))[::-1]:
 changes.append(dict(paper='IV',label='night:P3K.'+m.group(1),old=m.group(),new='',reason='Keep one-word status in the statement header; no workflow title.'))
 s=s[:m.start()]+s[m.end():]
p.write_text(s)
q=R/'analysis/execution_prose_changes.json';q.write_text(json.dumps(changes,indent=2))
print(json.dumps({'changed_spans':len(changes)}))
