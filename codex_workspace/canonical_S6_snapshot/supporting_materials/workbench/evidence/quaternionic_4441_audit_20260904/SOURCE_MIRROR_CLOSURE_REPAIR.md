# Same-project source-closure repair

4 September 2026. After the quantum delta was synchronized, a full
comparison of the AI bundle's 77 TeX/Bib sources against the Overleaf
checkout found fourteen earlier differences, including four absent
Koide modules. These were not newline-only differences.

The missing inputs are `koide_exact_parametrization.tex`,
`koide_exact_census.tex`, `koide_quaternion_bridge.tex`, and
`koide_effective_literature_audit.tex`, all below the workbench research
directory. The current canonical `koide_counting_repair.tex` includes
them. The existing local cumulative workbench compiles with all four.

The other differences concern the Koide root and counting extension,
crosswalks, mathematical summary, two higher-rung passages, citations,
and formatting packages in the worldline root. The repair copies the
already-existing current canonical sources; it does not claim that the
quantum audit has independently re-proved the earlier arithmetic or
global geometric results.

The synchronization script now obtains its source list from the current
AI bundle's complete dependency receipt, instead of relying on a manually
maintained changed-file list. Existing canonical companion PDF previews
are mirrored as well. Only the new quantum draft, cumulative workbench,
and overview were built and reviewed in this delta. Other companion
previews remain their existing local versions, not newly certified PDFs.
The historical annotated and clean principal sources are preserved;
their local-only PDF assets are not added or altered by this repair.

The same canonical Overleaf project is used. The script checks a clean
checkout and unchanged remote head before copying or pushing. It deletes
no file and changes neither sharing nor the selected main document.
