# Local LuaLaTeX runtime

Status: verified with a successful LuaHBTeX/LuaLaTeX compilation and embedded
outline text and mathematical fonts. This is runtime verification, not the
paper's final content or typography review.

## Reproduce

From `S6_02_PUSH`, run:

```sh
python code/tex_runtime_setup.py
python code/build_paper.py final
```

The setup helper builds its state in the sibling `tex_runtime` directory and
writes the exact environment to `code/tex_runtime_environment.json`.
`build_paper.py` loads that JSON before invoking LuaLaTeX and BibTeX. If the
package is relocated, rerun setup to regenerate the absolute paths. The
workspace must already provide the installed LuaHBTeX binary and the TeX Live
base/LaTeX trees; this helper repairs this image's missing local runtime pieces.

## Repairs

The installed binary is LuaHBTeX 1.18.0, TeX Live 2025/dev/Debian. The installed
TeX trees had dangling format, filename-database and font-map configuration
links into the absent `/var/lib/texmf`, and no `luaotfload`/`lualibs` package.

The helper extracts the distribution-matched Debian package locally:

- URL: https://deb.debian.org/debian/pool/main/t/texlive-base/texlive-luatex_2024.20250309-1_all.deb
- Bytes: 29,141,396.
- SHA-256: `c6601d6856af0b9cd25c64fcdab4a219a6ce7fd7a37724f532305add28fc72ff`.

It searches the local and existing system TeX trees without database-only `!!`
restrictions, generates a genuine `lualatex.fmt` using `luahbtex --ini`, and
creates local outline-font maps using `updmap --user` with explicit local
configuration. No global TeX files or `/usr` files were modified.

The existing `openout_any=p` policy remains in force. The intended font-cache
directory is declared through `TEXMFOUTPUT` as well as `TEXMFCACHE`; this allows
LuaTeX's cache writes without relaxing the existing output-path policy.

## Verification evidence

`code/tex_runtime_setup.out` records successful extraction, local font-map
generation, format generation, package resolution, and compilation of the
one-page `tex_runtime/runtime_check.pdf`. The check loads `fontspec`, Latin
Modern Roman, and the paper's principal mathematical, bibliography, table,
and hyperlink packages.

`code/tex_runtime_fonts.out` records `pdffonts` confirmation that the output
embeds Latin Modern as CID Type 0C and Computer Modern mathematics as Type 1;
no bitmap fonts occur in that check.

The first full-paper runtime check (`build_logs/runtime_ready_1.txt`) reached
the E.4 source after 36 pages and stopped at a missing display delimiter. That
source location was reported to the integrating author. The runtime helper
does not edit mathematical content, bibliography entries, or page layout.
