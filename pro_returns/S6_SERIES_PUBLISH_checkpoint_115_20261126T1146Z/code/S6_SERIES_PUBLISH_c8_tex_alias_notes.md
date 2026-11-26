# Bounded AMS literal-label alias diagnostic

Attribution: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed.

This work tests only an isolated pdfLaTeX document. It does not edit Paper III, its preamble, shared records, or mathematical progress. The proposed source block is `code/S6_SERIES_PUBLISH_c8_tex_alias_proposal.tex`; root review and application remain separate.

## Observed defect

The installed AMS display handler stores one deferred label in `\df@label`. A second label raises `Package amsmath Error: Multiple \label's` and overwrites that first label. The baseline auxiliary file confirms the loss. This occurs for both `equation` and a numbered `align` row.

The expanded baseline includes these exact current manuscript displays, copied without editing their mathematical text, literal labels, or explicit targets:

- `units/root/retained_angle.tex`: the equation labelled `wb:h24:ret:eq:M` and `maps:eq:B.3.2`, with targets `tag-03AP` and `tag-01V0`.
- The same fragment's two-row normal-frame `align`: its second row has `wb:h24:ret:eq:normal-u` and `maps:eq:B.3.4`, with targets `tag-03B3` and `tag-01V2`; the first row's `wb:h24:ret:eq:normal-first` and `tag-03B2` remain present.
- `units/weighted/weighted_os45.tex`: the equation labelled `maps:eq:D.OF1` and `maps:eq:D.OL1`, with targets `tag-0217` and `tag-021Q`.

The actual expanded baseline exited **1**. Its `.aux` retained only `maps:eq:B.3.2`, `maps:eq:B.3.4`, and `maps:eq:D.OL1` from these three pairs. The actual error/output/aux are preserved under `code/S6_SERIES_PUBLISH_c8_tex_alias_baseline_adjacent.*`. An earlier smaller synthetic baseline and its actual source/output/log/aux remain under `..._baseline.*`; it also printed multiple-label errors. No claim about its interrupted tool-return exit value is needed for the observed expanded-baseline failure.

## Proposed mechanism and exact state preservation

Place the complete tested block after loading `amsmath`, `hyperref`, and `cleveref`. Its `\AtBeginDocument` code runs after the installed cleveref initialization. It checks that cleveref's AMS hook exists, saves the active `\ltx@label` writer, and changes the raw display-label setter to append already-parsed label payloads to the existing `\df@label`.

The existing AMS row/display completion still chooses when to flush `\df@label`. At that exact point the dispatcher calls the saved cleveref/hyperref writer once for each queued literal label. Thus every alias receives the same current `\@currentlabel`, `\@currentHref`, and cleveref equation state as the original single label. The block does not increment a counter or create a hyperlink target. The optional syntax `\label[equation]{...}` still passes through cleveref's own parser. Non-queue calls to `\ltx@label` go directly to the saved writer.

Using the existing deferred storage also preserves AMS's row reset and display push/pop ownership. In particular, a patch confined to `\make@display@tag` would miss the separate `equation` completion path; the tested dispatcher is reached by both. The source mechanisms were read directly in the installed `amsmath.sty` (the deferred setter/writer and `endmathdisplay@a`/fleqn paths) and `cleveref.sty` (the begin-document wrapper, measurement handler, and optional argument parser).

## Actual result

Patched passes 1, 2, and 3 each exited **0**, with empty stderr. Pass 1 wrote all aliases. Pass 2 resolved the references; the resulting text moved the retained `align` onto page 2, so the auxiliary file changed only in its page fields and LaTeX requested a further pass. Pass 3 had no reference, multiple-label, duplicate-destination, or rerun warning. Its `.aux` is byte-identical to pass 2's `.aux`.

The ordinary equation, all align rows, gather rows, multline, split equation, a later single-label equation, an optional typed alias, and a section-reset equation were included. The final text extraction prints the expected alias numbers and equation names. The counter sequence is 1.1 through 1.9, then 2.1, then the manuscript cases 3.1 through 3.4.

| Exact manuscript labels | Final number | PDF destination |
| --- | --- | --- |
| `wb:h24:ret:eq:M`, `maps:eq:B.3.2` | 3.1 | `equation.3.1` |
| `wb:h24:ret:eq:normal-first` | 3.2 | `equation.3.2` |
| `wb:h24:ret:eq:normal-u`, `maps:eq:B.3.4` | 3.3 | `equation.3.3` |
| `maps:eq:D.OF1`, `maps:eq:D.OL1` | 3.4 | `equation.3.4` |

The PDF name tree contains each of the seven manuscript explicit targets exactly once. Both retained equation targets have the same page/coordinates; both retained second-row targets have the same page/coordinates; both LV targets have the same page/coordinates. Their literal identities remain separate live destinations. All 28 literal labels in this bounded MWE have one auxiliary entry, all 12 explicit targets have one PDF destination, and all 53 internal GoTo annotations resolve to named destinations. The baseline and patched diagnostic bodies are byte-identical after `\begin{document}`. These are checks of this diagnostic only, not a refreshed manuscript inventory.

The final diagnostic has two remaining non-reference messages: the expected epstopdf notice that shell escape is disabled, and an overfull retained equation in the narrow default article text width (73.51752 pt). That same overfull display occurs in the unpatched expanded baseline. The MWE preserves the relevant actual package order, rather than applying Paper III's full page/font layout. No whole-manuscript layout or build criterion is closed by this check.

## Reproduction and actual evidence

Run from the series root, using the already-installed root-relative wrapper. The wrapper always adds `-no-shell-escape` and selects the project-local format/font configuration.

```sh
python code/S6_SERIES_PUBLISH_c8_tex_alias_mwe.py baseline baseline_adjacent
python code/S6_SERIES_PUBLISH_c8_tex_alias_mwe.py patched patched_1
python code/S6_SERIES_PUBLISH_c8_tex_alias_mwe.py patched patched_2
python code/S6_SERIES_PUBLISH_c8_tex_alias_mwe.py patched patched_3
python code/S6_SERIES_PUBLISH_c8_tex_alias_inspect.py
```

These are the explicit passes actually run, not a compilation loop. The third patched pass resolved the observed page-field change. Reproduction need not replace the retained evidence filenames.

The driver preserves actual `.tex`, `.out`, `.err`, `.log`, and `.aux` for each named pass. The complete initial baseline log, expanded-baseline changes, final patched log, relevant stdout, all auxiliary data, and final output differences were read. `..._patched_3.out/.err/.log/.aux` are the stable final evidence. `..._inspect.py/.out/.err` contain the bounded source/aux/PDF-link inspection; its actual exit was 0, all 45 stdout lines were read, and stderr is empty. `..._dests.out/.err` contain the actual `pdfinfo -dests` output; `..._text.out/.err` contain the actual `pdftotext -layout` output. Both commands exited 0 and their full outputs were read.

The final diagnostic PDF is `agents/continuation8_tex_runtime/aliases/S6_SERIES_PUBLISH_c8_tex_alias_patched.pdf`. Package versions in its actual log are pdfTeX 1.40.26, LaTeX2e 2024-11-01 patch level 2, amsmath 2.17t (2024/11/05), hyperref 7.01l (2024-11-05), cleveref 0.21.4 (2018/03/27), mathtools 1.31, and etoolbox 2.5l. The block is proposed for this tested environment and package order; broader engines/package combinations were not tested.

One earlier direct `kpsewhich` lookup outside the project wrapper returned exit 1 with no paths. The installed package files were then read at their actual `/usr/share/texlive/texmf-dist/tex/latex/...` paths. The successful compiler runs used the wrapper's explicit project environment. No format or runtime reinstall was performed in this diagnostic.
