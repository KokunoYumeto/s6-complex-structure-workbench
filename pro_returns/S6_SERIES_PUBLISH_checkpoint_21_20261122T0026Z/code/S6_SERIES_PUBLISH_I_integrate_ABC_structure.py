from pathlib import Path
import json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_analytic/S6_SERIES_PUBLISH_I_global_ABC_guards.json'
for x in json.loads(p.read_text())['guards']:
 ed.replace(x['old'],x['new'],'D11' if x['id'].startswith('IA-ELLIPTIC') else 'D07',x['reason'],x['scope'],x['expected_count'])

def move_section(start,end,before,reason,label):
 a=ed.text.index(start);b=ed.text.index(end,a);old=ed.text[a:b]
 assert before not in old
 ed.replace(old,'','D15',reason+' Remove the sole complete block from its former position.',label)
 ed.replace(before,old+before,'D15',reason+' Insert the identical block in its dependency position.',label)
 return {'label':label,'bytes':len(old.encode()),'sha256':hashlib.sha256(old.encode()).hexdigest(),'reason':reason}

moves=[]
moves.append(move_section(r'\section{Global coefficient representatives}',r'\section{Arithmetic periods and compact subgroups}',r'\section{Twisted tangent cohomology}',
 'Place the full new coefficient construction after its Hodge and Picard inputs, before the twisted-cohomology application. The credited appendix retains its specified classification and deformation proofs.','inv:section:coefficient-atlas'))
moves.append(move_section(r'\section{The cotangent direct images and the decisive period scalar}',r'\section{Other logarithmic transformations and finite covers}',r'\section{The integral circle quotient and its cusp replacement}',
 'Place the cohomology and coefficient construction together before the real structures and the two boundary problems; preserve every proof and formula verbatim.','series:I:D; series:I:E'))
moves.append(move_section(r'\section{Arithmetic periods and compact subgroups}',r'\part{Results not yet established}',r'\clearpage\appendix',
 'Place the additional arithmetic results in the main body, leaving the appendix to the credited parameter, tangent and automorphism re-derivations.','I:algebraic-period-coordinates'))
ed.replace('\\clearpage\\appendix\n\n\\appendix\n','\\clearpage\\appendix\n',
 'D15','Apply the appendix counter transition once, after the full main body.','I:appendix-transition')

labels={
 'The cotangent direct images and the decisive period scalar':'pub:I:cotangent',
 'Fr\\"olicher, Bott--Chern, Aeppli, and Hermitian metrics':'pub:I:hodge',
 'Twisted tangent cohomology':'pub:I:twists',
 'Other logarithmic transformations and finite covers':'pub:I:other-multiplicities',
 'Global heights and the eleven rational CM fibres':'pub:I:cm-height',
 'Critical points and the global level curves':'pub:I:critical',
 'Arithmetic periods and compact subgroups':'pub:I:arithmetic',
 'Parameter equivalence and deformations':'pub:I:parameter-appendix',
 'Tangent cohomology and deformations':'pub:I:deformation-appendix',
 'The integral parameter comparison':'pub:I:torsor-appendix',
}
for title,lab in labels.items():
 old=r'\section{'+title+'}'
 ed.replace(old,old+r'\label{'+lab+'}','D16','Provide a permanent section anchor for the description of the actual body order.',lab)
a=ed.text.index(r'\subsection{How the paper is organized}');b=ed.text.index(r'\begin{figure}',a)
old=ed.text[a:b]
new=r'''\subsection{How the paper is organized}
The marked period and quotient coordinates lead to the exact norm,
its admissible domain, and the proper family. The intrinsic
classification is followed by discrete logarithmic data, the monodromy
quotient and the exceptional fibres. Sections~\ref{pub:I:cotangent}--\ref{pub:I:twists}
compute the cotangent, Bott--Chern and tangent cohomology; the complete
coefficient construction precedes its use in the Picard family.
The integral circle quotient and the real structures then lead to
the puncture and outer-boundary problems. Their local models,
component obstructions and topology are developed with the specified
marked comparison maps.

The remaining main-body sections treat other multiplicities and finite
covers, rational CM heights, the critical level curves, and arithmetic
periods. Appendices~\ref{pub:I:parameter-appendix}--\ref{pub:I:torsor-appendix}
contain the credited proofs of parameter equivalence, tangent
cohomology, local deformations and automorphisms.
The final part states the unresolved arithmetic questions.
Each arrow in the diagram identifies a particular supplying and
receiving body argument in the table below it.
'''
ed.replace(old,new,'D07','Describe the actual reordered body and credited appendix; remove the obsolete statement-header navigation claim.','sec:results')
ed.replace(r'\item \Cref{ari:C.6.3,ari:C.6.T2}: local heights give the rational CM factors and the stated central derivative calculation.',
 r'\item \Cref{ari:C.6.3,ari:C.6.T2}: local heights give the rational CM factors, and two-isogeny descent determines the stated rank over $\mathbb Q(\sqrt3)$.',
 'D07','Match the further-result description to the actual rank theorem rather than a different derivative result.','sec:results')
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_ABC_structure_integration.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'guard_path':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'moves':moves,'scope':'Root read every guard and both original elliptic statements. The cited-source quotient/scaling proof was compared in full by the analytic owner; root read the entire merged proof. Whole-section moves are byte-identical and carry no new proof-check event. All labels and permanent tags are preserved.'},indent=2)+'\n')
