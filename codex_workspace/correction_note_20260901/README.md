# Independent arXiv-oriented draft

This directory is a separate, local preprint draft. It does not modify,
replace, unpublish, or reorganize the canonical Overleaf project or the
published Zenodo record
([10.5281/zenodo.22235524](https://doi.org/10.5281/zenodo.22235524)).
That DOI is a versioned record; if this draft is deposited, it belongs as a
new version of that record, not as a new DOI.

## Why this is not a duplicate of Alpöge's source manuscript

Levent Alpöge's supplied source manuscript already states and proves, for its proposed
non-normal fibre, the normalization--conductor sequence, the
conductor-supported differential, and the split-extension coinvariant
calculation (Section 10, Lemmas 10.2--10.3 and 10.7). It also contains the
proposed construction and its headline \(S^6\), topology, and Picard claims.
Those results are credited as prior material here; no priority is claimed for
them and they are not repackaged as new theorems.

The independent material retained in this shorter note is:

1. an explicit two-step cotangent filtration and its connecting-map formula;
2. a proper morphism over a disc with smooth total space whose central fibre
   is a nodal cubic times \(\mathbb P^1\), together with a non-torsion gluing bundle for which the two
   endpoint groups vanish but the ambient twisted cotangent group does not;
3. an explicit extension of that gluing bundle over the displayed total space;
4. a local calculation of ordinary relative \(\Omega^1\) in the bare
   double/triple-crossing and cyclic multiple-fibre charts; and
5. a derived reformulation of the sufficient global vanishing criterion in
   CDP20, stated without a priority claim.

The test family refutes only the unrestricted endpoint implication for an
arbitrary fibre line bundle. It is not a counterexample to CDP20 Theorem 2.2:
the family is not a compact threefold with that theorem's global hypotheses,
and the local calculation does not settle the proposed \(S^6\) construction.
The local correction is specifically about ordinary relative \(\Omega^1\)
on those displayed charts. A quotient chart needs a separate invariant-module
calculation, and no assertion about \(\bigwedge^2\Omega^1\) or
\(\bigwedge^3\Omega^1\) is made.

The bounded literature/source audit found no occurrence of this specific
equation together with this proper-family endpoint test. That is a search
scope statement, not an absolute novelty claim.

The likely publication-sized contribution is therefore a short correction
note centered on the exact connecting-map obstruction and the proper test
family. The filtration itself is elementary homological algebra, the local
module calculation is a useful correction rather than a major theorem, and
the global criterion is a transparent sufficient condition. Whether that
package clears an arXiv novelty threshold is a judgment for a human author and
subject moderator; this directory does not claim that it does.

## Status and authorship

This is a mathematical draft for human review, not an arXiv submission. The
author field is intentionally a placeholder. Before submission, a human
author must verify every proof, replace the author field, check rights and
references, and accept responsibility for the final version. Generative-AI
systems assisted transcription, exact calculations, literature searching, and
drafting; no AI system is an author. The local audit used OpenAI Codex
gpt-5.6-sol.

## Build

Run the following in this directory (or use `latexmk -pdf main.tex`):

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

For an arXiv source upload, use `main.tex` and `references.bib` only. The
generated PDF is retained for inspection; machine-specific auxiliary build
files are intentionally omitted from this clean source package.

## Public sources

* CDP20: <https://doi.org/10.1112/S0010437X19007802>
* CDP20 arXiv record: <https://arxiv.org/abs/1904.11179>
* CDP98: <https://doi.org/10.1023/A:1000313214795>
* Levent Alpöge, supplied source manuscript (unrefereed): <https://alpo.ge/s6.pdf>
* Public context page for the supplied manuscript: <https://zeli.app/story/49412947>
* Public audit/reconstruction record: <https://doi.org/10.5281/zenodo.22235524>
* Related extension record: <https://doi.org/10.5281/zenodo.22085272>
* arXiv submission guidance: <https://info.arxiv.org/help/submit/index.html>
* arXiv moderation and AI policy: <https://info.arxiv.org/help/moderation/index.html>
