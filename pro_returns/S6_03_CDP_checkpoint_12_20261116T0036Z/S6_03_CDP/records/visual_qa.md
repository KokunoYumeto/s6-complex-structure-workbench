# Visual QA

15 November 2026, 14:35 UTC: 110-page LuaLaTeX build; zero TeX errors, zero unresolved references, zero overfull boxes. Rendered 31 pages using PyMuPDF at 1.45 scale. Inspected pages 1, 8, 21, 33, 57, 58, 60 and 75 as full-page images. These include the repaired character-count/path passages and C5 definition/display passages. All inspected margins, formula tags, line breaks, fonts and page numbers are legible; no clipping or overlap observed. The remaining distributed samples will be inspected after checkpoint 02.

The source of the first overflow list remains in the build logs; former substantive sizes were 46.9542pt, 24.50348pt and 2.76465pt. The current count above 2pt is zero. Further builds after mathematical additions require a renewed log check and changed-page rendering.

15 November 2026, 15:16 UTC: inspected full-page PNGs 10, 44, 73, 90, 105, 117 and 128 of the 128-page build. The former character-count and long C5 displays now remain within the margins; conductor comparison displays, D2 sign theorem, root-stack formulas, E4 proof and bibliography are legible with no clipping or overlaps. This build has zero TeX errors, unresolved references, overfull boxes and missing glyphs. Subsequent mathematical additions require a fresh build and changed-page sample.

2026-11-15 15:43 UTC: clean 141-page build (118 statements). Rendered 33 pages; inspected full-page images 1,45,69,81,104,129,141. No clipped text, overlapping material, broken formulas or margin overflow observed. First-page convention additions will be checked after the next build.

## 16:34 UTC build audit

The 127-statement manuscript has 170 pages. All four build passes succeeded, with zero TeX errors, overfull boxes, unresolved references or missing glyphs. The generic renderer produced 42 distributed page images; additional targeted images cover the new proofs. Full-page images 1, 48, 56, 57, 79, 85, 90 and 91 were independently viewed. The first-page conventions and signed dictionary fit on page one; the new incidence, non-lci discriminant, minimality, class VII equality and rational cusp calculations have no clipping or overlapping text/equations. The legacy inclusion arrow was replaced by the same Unicode-math hook arrow after its old font command triggered a bitmap-font failure. The erroneous unbraced C subscript was corrected. Both failed build logs are retained.

## 17:36 UTC build and inspection

The build begun at 17:34 compiled 150 numbered statements into 213 pages. All four compilation stages exited zero. The final log has zero TeX errors, zero unresolved references, zero overfull boxes and zero missing glyphs. Distributed and newly targeted pages were rendered by the saved script. The root visually inspected pages 130 and 132 (weighted cyclic-cover formulas and the new parity proof) in this version; both are contained within the margins and readable. The earlier 205-page version was additionally inspected at pages 93, 105 and 117. No overflow repair was required in these builds.

## 17:57 UTC build and subsequent inspection

The build recorded in `build/root_build_1803.out` compiled 157 statements into 224 pages. All four stages exited zero, with zero TeX errors, unresolved references, overfull boxes and missing glyphs. The renderer saved distributed and newly targeted page images. The root visually inspected pages 86, 107, 110, 112 and 142 in this version. The mixed-Hodge comparisons, global Euler statement and new unrestricted-fillings passages fit their margins without clipping or overlap. Mathematical additions UN5–10 require another build and inspection before checkpoint 06.

## 18:24 UTC build and inspection

The build `root_build_1824.out` compiled 162 statements into 235 pages. All four stages exited zero, with zero TeX errors, overfull boxes, unresolved references and missing glyphs. The root inspected rendered pages 107, 110, 129, 131 and 132, covering the new cusp-product statement and source comparison, properly elliptic example, node transport, contracted-genus comparison and normal-support classification. The split cusp-product display fits; all inspected pages are legible without clipped or overlapping material. UN7, UN11 and UN12 will be rendered after their final integration.

## Six-hour manuscript inspection

UTC 2026-11-15T18:38:15.392087+00:00; 251-page manuscript, 166 numbered statements. Build root_build_1835.out: four successful passes; TeX errors 0; overfull boxes 0; boxes above 2pt 0; unresolved references 0; missing glyph warnings 0. Renderer manifest regenerated for this exact PDF. Root visually opened pages 128, 134, 138, and 163: the UN7 statement, UN12 conductor table, UN13 cohomology displays, and complete UN11 signature table all fit within the text area, with no clipped or overlapping content. Earlier distributed visual inspections remain recorded above.

## Root inspection at 2026-11-15T19:38:32.688407+00:00

PDF:283pages,177statements, build/root_build_1932.out, through UN24. Root opened and visually inspected page_149.png, page_165.png and page_188.png. The K3 statement opening, rank-two period argument, and secondary-Kodaira integral-cohomology table are legible and inside the page margins, with no visible clipping or overlap. The prior six-image tool return was truncated and is not counted as inspection. Zero overfull boxes and zero overflow above2pt in the clean compile. UN25/26 await compilation.

## Root inspection at 2026-11-15T20:15:39.901039+00:00

PDF289pages,179statements, build/root_build_1942.out throughUN26. Actual images page_121.png,page_125.png,page_128.png were opened and inspected. Page125 is the sole1.22974pt overflow passage C.EN.S2; it is readable with no clipping, and its source has now been split into a gathered two-line display. Statement openings, incidence table, displayed equalities and prose on the three pages fit clearly. Final build haszeroerrors/undefinedrefs/missingglyphs andzerooverflowabove2pt.

## Root inspection of the 320-page build — 2026-11-15T20:29:03.186169+00:00

Build/root_build_2028.out contains188statements throughUN35, with four successful compilation passes, zero TeX errors, zero overfull boxes, zero unresolved references and zero missing glyphs. The earlier failed2023build is retained: four alignment errors in C.ET.2 and overflows14.19334pt and6.45247pt. The source repairs replace the erroneous split alignment by a three-line aligned display, split C.EN.R1, and break the paired-root support heading. Literal quad text in C.EN.G2 was also corrected.

Root opened and inspected the actual current rendered pages89,122,126,135,141,183,195,223. These cover UN28 compact-core maps, the repaired UN27 and UN30 canonical displays, UN33 Weierstrass/branch tables, the UN35 opening and preceding support cohomology, the K3 translation-lattice quotient, the UN29 normal-return statement, and the UN34 occurrence statement. All displayed text, equation tags, tables and page boundaries fit clearly with no clipping or overlap. Only these pages are claimed as visually inspected; other render samples are available in build/visual_qa.

## Root inspection at 2026-11-15T20:36:08.209339+00:00

Current327-page191-statement PDF throughUN38, build/root_build_2033.out: all four passes successful; zero errors, overflows, unresolved references or missing glyphs. Root opened page_107.png,page_132.png,page_163.png from the current render and inspected their table, formulas, proof text and page boundaries. All are readable and within margins, with no clipping or overlap. Other rendered samples are available but are not claimed as inspected.

## Root inspection at 2026-11-15T21:23:48.787850+00:00

Current356-page200-statement PDF throughUN47: all four passes successful; zero errors, overflows, undefined references or missing glyphs. Previous overflows8.02008pt and14.71288pt were repaired in C.DH.14a and C.HC.2. Root opened and visually inspected current pages98,131,167,180,215,252; formulas, text and page boundaries are readable with no clipping or overlap.

## Root inspection at 2026-11-15T21:33:52.037940+00:00

Current360-page201-statement PDF throughUN48: four successful passes, zero errors, overflows, undefined references and missing glyphs. Root opened and inspected current pages180,182,183. All displayed formulas and proof text fit within the page boundaries with no clipping or overlap.

## Root actual visual inspection at 2026-11-15T22:11:01.763248+00:00

The367-page203-statement PDF from root_build_2146.out was rendered and root opened current pages222,225,266. These cover the exact primary boundary matrix, twistor period frame and weighted map, and the secondary coarse inverse and primitive boundary matrix. All text and formulas fit with no clipping or overlap. The build had four successful passes and zero errors, overflows, undefined references or missing glyphs.
The first207-statement build (root_build_2210.out, filename label chosen before its actual finish) exposed sixteen TeX errors caused solely by unbraced math-letter macro subscripts in UN51/52. All six source subscripts were braced. The replacement build root_build_2209.out completes all four passes with zero errors, overflows, unresolved references and missing glyphs. Actual inspection of that new PDF is recorded separately after rendering.

## Root actual inspection of the385-page PDF — 2026-11-15T22:19:17.411248+00:00

The clean207-statement PDF throughUN54 from root_build_2209.out was rendered. Root actually opened pages83,86,194,226,297: the full Hopf character classification, mixed-star weighted map and proper gluing, coherent incidence and residue sequence, separate ruled moving frame, and weighted finite transport/invariant quotient. All text, matrices, equation labels and displayed maps fit within the pages, with no clipping or overlap. The build has four successful passes and zero errors, overflows, unresolved references and missing glyphs. Future builds preserve the previous root PDF and its exact rendering manifest before replacement.

## Root actual inspection of the397-page PDF — 2026-11-15T22:22:30.537212+00:00

The211-statement PDF throughUN58, built by root_build_2220.out with four successful passes and zero errors, overflows, unresolved references and missing glyphs, was rendered. Root actually opened pages83,84,201,202,277,309. They cover the global twistor-log period and conjugate Hopf frames, the exact root and canonical-height equations, common nonlinear core periods, the all-ruled infinity filling, and the finite ruled root-cover power map. Text, formulas and labels fit cleanly with no clipping or overlap.

## Root actual inspection of the402-page PDF — 2026-11-15T22:29:05.684552+00:00

The212-statement PDF throughUN59, from root_build_2228.out, was rendered after four successful passes with zero errors, overflows, unresolved references and missing glyphs. Root actually opened pages92,93,94,95. These cover the full affine descent relation and positive equivariant period determinant, target-frame transport and global partial-sum finite action, exact Reynolds coordinates and invariant quotient, and the conjugate infinity action and explicit order2/3/4/6 examples. Every displayed formula, label and paragraph fits with no clipping or overlap.

## Root inspections after checkpoint10

The clean root_build_2307.out compiled217 statements through UN64/65 in426 pages. The subsequent root_build_2309.out compiled218 statements through UN65, now including UN63, in436 pages. Both final logs have zero errors, overfull boxes, unresolved references and missing glyphs. The436-page PDF was rendered, and root actually inspected pages173,176,324,326,336,338,340. The invariant-ring, finite-action, extension and volume displays fit without clipping or overlap.

The next clean root_build_2325.out compiled221 statements through UN68 in449 pages. Every compiler/bibliography pass succeeded, and the final log again has zero errors, zero overfull boxes, zero unresolved references and zero missing glyph warnings. render_qa_2327.out records the raster renders. Root actually viewed pages180,181,182,248,251,254,295,297, including the charge equalities, intrinsic Euler formula, all-elliptic extension and repaired etale root argument. There is no clipping, overlap or truncated formula. The previous PDFs, manifests and pass logs remain in build/history.


