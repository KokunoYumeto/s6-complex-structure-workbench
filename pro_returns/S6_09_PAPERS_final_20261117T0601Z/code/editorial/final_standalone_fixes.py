"""Exact final source/command locators; no argument is replaced or omitted."""
from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parents[2]
FIXES={
 'I':[
  ('coincide with the family in this prompt; the normalization differs',
   r'coincide with the marked family $X_c$; the normalization differs',
   'Replace an unavailable prompt referent by the explicitly defined marked family.'),
  ('Every equality, the division-polynomial noncancellation, and the four\nlattice images are checked by exact arithmetic in the supplied code.',
   r'''The program \path{cd_torsion_independent.py} checks the displayed
division polynomials and four lattice images by exact arithmetic; its
command and retained output are in Appendix~\ref{app:I:programs}.
The admissibility inequality is proved analytically above.''',
   'The complete original program and its actual successful output were opened: they certify the stated polynomial/lattice calculations. The stronger unspecific every-equality claim is narrowed to the actual finite output; the full analytic admissibility proof remains.'),
 ],
 'III':[
  (r'''We also read the finite semistable
models in the supplied checkpoint, B.1--B.3 of
\texttt{S6\_02\_PUSH\_AB\_push.tex}. Their component monodromy''',
   r'''The finite semistable models are treated in
\cref{push:src:B.1.1,push:src:B.1.2,push:src:B.2.1,push:src:B.3.1}.
Their component monodromy''',
   'Replace the old own-work filename/part pointer by the complete numbered companion model and obstruction proofs.'),
  ('These are the maps in the supplied workbench, not choices\nof arbitrary sphere quotients of the same targets.',
   'These formulas specify the marked maps, including the retained coordinates\nand quotient identifications; arbitrary sphere quotients of the same targets\nare not substituted for them.',
   'State the mathematical marking scope directly; the complete formulas immediately precede this sentence.'),
  ('The local assertions in the supplied workbench are valid, with their\ntwo different degrees.',
   'The local cover constructions have the two different degrees just computed.',
   'Replace historical provenance by the actual immediately proved local degree statement.'),
  (r'''The presentation of the fundamental group in the supplied
\textup{[AC26, Theorem 7.17]} sends''',
   r'''The presentation of the fundamental group in
\cite[Theorem~7.17]{AC26} sends''',
   'Use the verified original-source citation with its exact theorem locator.'),
  ('no case from the prompt.','no case from the specified input class.',
   'Identify the exact input class defined by the preceding numbered statement.'),
 ]}

def transform(text,paper):
    changes=[]
    for before,after,reason in FIXES[paper]:
        if before in text:
            assert text.count(before)==1,(paper,before,text.count(before))
            text=text.replace(before,after)
        else:assert after in text,(paper,'neither source nor replacement found',before)
        changes.append({'before':before,'after':after,'reason':reason,
                        'mathematical_argument_removed':False})
    (D/'records'/f'{paper}_final_standalone_fixes.json').write_text(json.dumps({
        'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),17November2026,/root',
        'changes':changes},ensure_ascii=False,indent=2)+'\n')
    return text

if __name__=='__main__':
    p=D/'S6_09_PAPERS_I.tex';p.write_text(transform(p.read_text(),'I'))
