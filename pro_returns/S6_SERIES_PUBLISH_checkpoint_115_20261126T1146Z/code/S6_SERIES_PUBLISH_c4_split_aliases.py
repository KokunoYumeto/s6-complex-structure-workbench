"""Resolve the actual missing split-display aliases and one measured overflow."""
from S6_SERIES_PUBLISH_c4_edit import *
from S6_SERIES_PUBLISH_c4_derive_II import braced
import re

source=SOURCE.read_text()
repairs=[]
for match in re.finditer(r'\\begin\{equation\}[\s\S]*?\\end\{equation\}',source):
    block=match[0]
    split=block.find(r'\begin{split}')
    alias=block.find(r'\SsixEquationAliases{')
    if split<0 or alias<split:
        continue
    _,end=braced(block,alias+len(r'\SsixEquationAliases'))
    invocation=block[alias:end]
    after=block[:alias]+block[end:]
    after=after.replace(r'\begin{equation}',r'\begin{equation}'+'\n'+invocation,1)
    labels=re.findall(r'\\label\{([^}]+)\}',invocation)
    repairs.append((block,after,labels))
assert len(repairs)==3
for n,(old,new,labels) in enumerate(repairs,1):
    apply_edit(old,new,f'II-C4-SPLIT-ALIASES-{n:02}',['D23'],labels[0],
        'Numbered split display, same primary equation and alias targets',
        'The three-pass build had eight undefined-reference occurrences. Comparing every actual body label with the auxiliary file found eight absent aliases, all in these three displays: amsmath split captures the label writer before the late alias call. The existing correctly built displays install their alias call before split; use that same placement here. All mathematical tokens, labels and tag targets are retained.',
        review='Root read all three complete old displays and the earlier correctly built alias/split examples. Only the macro installation position changes; exact identifier multiplicities are checked. No mathematical event is added. Final build and rendered images must verify the result.')
old=r'''\begin{equation}
 \chi(\OO_X)=2-P_g,\qquad
 q(X)=P_g-1\ (P_g>0),\qquad q(X)=0\ (P_g=0),
 \qquad q(X)=\max(P_g-1,0).
\hypertarget{tag-00YL}{}\hypertarget{tag-00E8}{}\SsixEquationAliases{\label{cdp:eq:C.D4.16}}\label{cdp:eq:C.RD.30}
\end{equation}'''
new=r'''\begin{equation}
\begin{gathered}
 \chi(\OO_X)=2-P_g,\qquad q(X)=P_g-1\ (P_g>0),\\
 q(X)=0\ (P_g=0),\qquad q(X)=\max(P_g-1,0).
\end{gathered}
\hypertarget{tag-00YL}{}\hypertarget{tag-00E8}{}\SsixEquationAliases{\label{cdp:eq:C.D4.16}}\label{cdp:eq:C.RD.30}
\end{equation}'''
apply_edit(old,new,'II-C4-DUALITY-DISPLAY-WIDTH',['D23'],
    'cdp:eq:C.RD.30','Cubic duality calculation, coherent Euler/irregularity display',
    'The completed three-pass log measured a 12.1012pt overfull display at this exact line. Break the same four identities across two gathered rows; all expressions, inequalities, labels and tags are retained.',
    review='Root read the complete display and its Serre-duality/Leray context. This adds only a line break and a gathered environment, with no proof or equation-value change. The corrected display must be visually inspected after the clean rebuild.')
print('Before repairs: 8 undefined-reference occurrences, 8 absent auxiliary aliases, one 12.1012pt overflow and one 0.89041pt box.')
print('Repaired three split alias placements and one display width; all final images remain unread.')
