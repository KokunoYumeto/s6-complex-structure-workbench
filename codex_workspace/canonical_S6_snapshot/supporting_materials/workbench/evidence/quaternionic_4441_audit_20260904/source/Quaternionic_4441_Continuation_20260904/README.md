# Quaternionic 4+4+4+1 continuation packet

This packet develops the next exact rung after the marked `9=4+4+1` Lorentz observation theorem.

## Files

- `quaternionic_4441_continuation.pdf` - 12-page theorem/proof note.
- `quaternionic_4441_continuation.tex` - standalone LaTeX source.
- `quaternionic_4441_continuation.md` - machine-readable mathematical handoff.
- `verify_quaternionic_4441.py` - exact symbolic replay.
- `verification_output.txt` - human-readable check transcript.
- `verification_results.json` - machine-readable check summary.
- `MANIFEST.sha256` - checksums for packet files.

## Central construction

The same marked map `P` is extended from `Herm_3(C)` to `Herm_3(H)`, and the preimage of `Herm_2(C)` is retained:

```
J_13,P = (O_P^H)^{-1}(Herm_2(C)).
```

It has the exact real decomposition

```
Herm_2(C) + C^2 + C^2 + R = 4+4+4+1.
```

Its cubic is

```
N_13 = lambda det(G) - z* adj(G) z - w* adj(G) w.
```

The old nine-dimensional object is the slice `w=0`. The new rank-defect boundary compactifies to `S^12`, with the old `S^8` as an unknotted fixed set and linking sphere `S^3`.
