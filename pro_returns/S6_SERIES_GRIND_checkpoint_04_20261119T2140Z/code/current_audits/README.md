# Current audit programs and outputs

These are exact copies of the fresh audit programs and their derivations,
outputs and receipts. `manifest.json` maps every copy to its canonical
working path in the package and records its size and SHA-256.

Run a relative-path program from its listed canonical path. Both that
program and its inputs remain in the package. For example:

```sh
python audit_paper_i/iv_os45/code/k119_afterreading_exact.py
```

Copying and packaging do not count as another execution or proof check.
The original typed events state which programs were actually run, which
were newly written, and whether their derivation preceded proof reading.
Primary-source PDFs and large source transcriptions remain in the
corresponding `audit_*/primary_sources` directories.
