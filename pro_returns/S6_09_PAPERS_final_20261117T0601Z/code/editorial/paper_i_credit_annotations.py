"""Exact, qualified source credits found in the final original-source pass."""
import re

ANNOTATIONS={
 'inv:D1.1':r'''The root-curve Picard group and graded cohomology are
\citet[Lemma~6.1]{DuEtAl2026v1}. We re-derive them and retain the explicit
coarse invariant-descent function $d(n)$ in the same calculation.''',
 'inv:D1.2':r'''The root lift, vertical splitting, logarithmic quotient and
structure direct images are re-derived after reading
\citet[Lemmas~6.2 and 6.7; Propositions~6.6 and 6.10]{DuEtAl2026v1}.
The complete root and ordinary-sheaf arguments are retained below.''',
 'inv:A3.1':r'''The vanishing of holomorphic forms and the Hodge-diamond
pattern with one undetermined integer are due to
\citet[Proposition~9.20, p.~80; Theorem~9.1(vi), p.~65]{AC2026}.
The value of that integer is determined here by the nonzero direct-image
scalar. The full calculations of both the pattern and its value are retained.''',
 'mapsI:hodge:line':r'''The Hodge line and finite determinant characters
are known from \citet[Lemma~9.10 and Proposition~9.11, pp.~70--71]{AC2026}.
The complete modular-frame and root-character re-derivation follows.''',
 'wb:ffcert:thm:normal-trivialization':r'''The exact normal-line orders are
\citet[Theorem~5.4(iii), p.~32; flat-character proof, p.~35]{AC2026}.
We retain the full primitive-character calculation as a re-derivation.'''
}

def add_credits(text):
    for label,annotation in ANNOTATIONS.items():
        token='\\label{'+label+'}'
        assert text.count(token)==1,(label,'nonunique or absent')
        pos=text.index(token)
        starts=list(re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|remark)\}',text[:pos]))
        env=starts[-1][1]
        end=text.index('\\end{'+env+'}',pos)+len('\\end{'+env+'}')
        text=text[:end]+'\n\n'+annotation+'\n'+text[end:]
    return text
