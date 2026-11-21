#!/usr/bin/env python3
"""First structural pass: preserve all mathematical blocks and stable anchors."""
from S6_SERIES_PUBLISH_editing import Editor, block
import re

e=Editor('V')

def take(label):
    value=block(e.text,label)
    e.text=e.text.replace(value,'',1)
    return value

def before(anchor,value,kind,reason,label=''):
    if e.text.count(anchor)!=1: raise ValueError(anchor)
    e.text=e.text.replace(anchor,value+'\n\n'+anchor,1)
    e.record(kind,value,value,reason,label,new_location='before '+anchor[:100])

# Put the headline family first. The common cusp is moved below before either
# global construction, so this does not borrow a later construction.
resolved_start=e.text.index('\\part{The resolved fibre product}')
resolved_end=e.text.index('\\part{The marked rank-six construction and its family}')
resolved=e.text[resolved_start:resolved_end]
e.text=e.text[:resolved_start]+e.text[resolved_end:]
before('\\part{Shifted fibre products}',resolved,'D14',
       'The rank-six compact complex fourfold is the headline construction; the resolved fibre product follows it.',
       'maps:src:E.1.2')

# Move broad classification restrictions to the classification part. The
# primitive cusp normal form is a common local input and stays early.
prelim_start=e.text.index('\\section{The marked cusp and preliminary lattice restrictions}')
prelim_end=e.text.index('\\section{The integral eight-manifold}')
prelim=e.text[prelim_start:prelim_end]
normal=block(prelim,'maps:src:F.2.1')
prelim=prelim.replace(normal,'',1)
e.text=e.text[:prelim_start]+e.text[prelim_end:]
prelim=prelim.replace('\\section{The marked cusp and preliminary lattice restrictions}',
                     '\\part{Integral monodromy and marked gluings}\n\\section{Admissible data and local restrictions}')
before('\\section{The effective integral input classification}',prelim,'D14',
       'Separate the classification of all admissible inputs from the construction of the headline example.',
       'def:admissible')

# All matrices are defined before the monodromy, period and filling statements.
construction=block(e.text,'maps:src:F.2.5')
m=re.search(r'\\item We use the following matrices on the marked dual lattice:\s*(.*?)\nTheorem~\\ref\{night:P1\.1\}',construction,re.S)
if not m: raise ValueError('standard matrix definition')
data=m[1]
definition=(r'\begin{definition}[The marked rank-six datum]\hypertarget{tag-PV02}{}\label{pub:V:rank-six-data}'+'\n'
 r'\StatementRecord{pub:V:rank-six-data}{proved}{PV02}{}'+'\n'
 r'We use column vectors and the integral cohomology matrices'+'\n'+data+'\n'
 r'The affine orders are $(m_1,m_2)=(5,4)$, and $\tau_i(x)=M_ix+v_i/m_i$ on $\mathbb R^6/\mathbb Z^6$.'+'\n'
 r'Positive based meridians satisfy $g_1g_2g_0=1$. The exterior-square basis of $\bigwedge^2\mathbb Z^4$ is $(01,02,03,12,13,23)$.'+'\n'
 r'\end{definition}')
newconstruct=construction.replace(m[0],
 r'\item Use the matrices and affine vectors of \cref{pub:V:rank-six-data}.'+'\n'+r'Theorem~\ref{night:P1.1}',1)
e.replace(construction,newconstruct,'D13','Give the defining matrices their own numbered definition before any construction uses them.','maps:src:F.2.5')
monodromy=take('night:P1.1')
cusp=take('night:P1.9')
collapse=take('night:P1.11')
local=r'\section{The monodromy and the marked cusp}\label{pub:V:sec-local}'+'\n\n'+definition+'\n\n'+normal+'\n\n'+monodromy+'\n\n'+cusp+'\n\n'+collapse
before('\\section{The integral eight-manifold}',local,'D14',
       'Define the matrices, prove the local monodromy, and construct the common cusp before either global gluing.',
       'night:P1.1')

# The explanatory dual-convention paragraph has become part of the numbered
# datum. Its old section anchor remains an alias at that definition.
old=re.search(r'\\hypertarget\{tag-034O\}\{\}\\label\{sec:fourfold\}\s*We use column vectors\..*?without floating-point\s*arithmetic\.',e.text,re.S)
if not old: raise ValueError('dual convention paragraph')
e.replace(old[0],'','D13','The dual convention and exterior basis are now in the numbered datum.','sec:fourfold')
e.replace('\\label{pub:V:rank-six-data}',
          '\\label{pub:V:rank-six-data}\\hypertarget{tag-034O}{}\\label{sec:fourfold}',
          'D10','Keep the original convention anchor at its numbered definition.','sec:fourfold')

# Move the period construction before the global topological calculation.
start=e.text.index('\\section{The genus-two pencil and the lifted period planes}')
end=e.text.index('\\section{The oriented diffeomorphism type}')
periods=e.text[start:end]
e.text=e.text[:start]+e.text[end:]
before('\\section{The integral eight-manifold}',periods,'D14',
       'Construct the holomorphic period family before the topology of its global filling.',
       'night:P1.4')

# Define the algebraic splitting and height function before the lift uses them.
connection=take('night:P1.15')
height=take('def:hb')
before(block(e.text,'maps:src:F.3.6'),
       '\\subsection{The algebraic connection and its splitting}\n\n'+connection+'\n\n'+height+
       '\n\n\\subsection{The lifted periods and compactification}',
       'D14','Place the normalized algebraic splitting and the height definition before the global lift.',
       'night:P1.15')

# Keep the integral homology theorem single, preserving both historical targets.
homology=take('night:P1.12')
aliases='\\hypertarget{tag-02QL}{}\\label{night:P1.12}'
e.replace('\\label{maps:src:F.2.6}',
          '\\label{maps:src:F.2.6}'+aliases,
          'D12','The holomorphic realization has the same marked caps and clutch; its homology is the conclusion of this one theorem.',
          'night:P1.12')
e.record('D12',homology,
         'The label night:P1.12 and tag 02QL are aliases at maps:src:F.2.6.',
         'Remove the repeated integral homology statement and its cross-reference proof; the original independent check remains in the check file.',
         'night:P1.12')

# Readable thematic sections replace a single long classification section.
e.replace('\\section{The effective integral input classification}',
          '\\section{Finite spectra and rational extensions}\\label{pub:V:sec-spectra}',
          'D14','Divide the long input classification by its mathematical dependencies.','maps:src:F.2.7')
for lab,title,key in [
 ('maps:src:F.2.16','Integral lattices and extension classes','lattices'),
 ('maps:src:F.2.25','Three-connectivity and affine twists','connectivity'),
 ('maps:src:F.2.31','Fundamental groups and cellular models','cellular'),
 ('maps:src:F.2.36','Canonical representatives of integral monodromy','canonical')]:
    before(block(e.text,lab),'\\section{'+title+'}\\label{pub:V:sec-'+key+'}',
           'D14','Give a distinct mathematical stage its own section.',lab)

e.save()
