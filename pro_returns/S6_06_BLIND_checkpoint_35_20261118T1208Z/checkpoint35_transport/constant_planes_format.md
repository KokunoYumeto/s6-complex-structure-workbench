# Checkpoint35: exact constant-plane outer dictionary representation

This candidate changes only the transport representation of the retained RGB-row dictionary. The original dictionary stream, row order, integer row IDs and every PNG-codec byte remain the required output. The candidate remains provisional until the full closed-stream inverse and whole-archive size gates pass.

## Format and exact inverse

The input is the already verified stream with magic `S6RGBROW1\0`. It consists of ordered records `(n,row)`, where `n` is an unsigned four-byte big-endian integer and `row` contains exactly `n` bytes. Write `s=n mod3` and `k=(n-s)/3`. The original row has the literal ordered decomposition

`prefix[s] | plane0[k] | plane1[k] | plane2[k]`.

These are precisely the three planes of the inherited RGB/difference representation; the prefix is retained exactly. The new stream begins with the twelve-byte magic `S6RGBCONST1\0`. Each record keeps the same four-byte original length `n`, followed by the same prefix, one flag byte, and three payloads in their original plane order.

For plane number `j`, bit `j` of the flag is set exactly when `k>0` and every byte in that plane is equal to its first byte. In that case the payload is that one original byte. Otherwise the flag bit is zero and the payload consists of all `k` original bytes. The flag has no other bits. Empty planes have their bits zero and carry no bytes.

The inverse reads `n`, derives the same `s,k`, copies the prefix, and visits the three flags in order. A set flag consumes one byte `b` and writes exactly `k` copies of `b`. A zero flag consumes and writes exactly `k` bytes. It then emits the unchanged original length and recovered row. For a set flag, the forward test states that each original byte was `b`, so the recovered plane is byte-for-byte equal to the original plane. For a zero flag the bytes were copied directly. This proves the inverse equation for every row, including all three remainder classes of `n` and the empty-plane case. Concatenating these equalities in the original order recovers the entire prior RGB dictionary stream.

No permutation is used. Thus row number `i` in the recovered dictionary is exactly the prior row number `i`; every existing PNG row-reference index keeps its original meaning.

## Composition with the retained original-dictionary inverse

The existing `checkpoint_png_rgb_dictionary.py` inverse is retained byte-for-byte. It interprets the recovered RGB row as the original prefix, the original middle-channel bytes, and the two original byte differences. Its displayed additions modulo256 reconstruct the exact interleaved original row bytes. The new decoder composes the constant-plane inverse with that existing inverse.

The implementation `RGBReader` provides the recovered RGB stream through `read(n)`. Its buffer invariant is that the buffer is exactly the not-yet-returned suffix of already recovered rows; further complete records are decoded only as necessary to supply the requested prefix. On end of input it returns only the remaining suffix, then the empty byte string. The whole closed-candidate check passes this reader into the unchanged original-dictionary decoder and checks all three streams separately.

The exact required identities for the current retained dictionary are:

| Stream | Bytes | SHA-256 |
|---|---:|---|
| Prior RGB dictionary | 5,533,013,867 | `5cfaf1bbcd269b6210b7708aaa72939a9658c4f8e8d22b24755a042eb964e8aa` |
| Original row dictionary | 5,533,013,871 | `a1c39525e573980a1cc3b8e593f9d887ddf49997f338c4c4a70140bb7180daa1` |

The original row count is1,901,249. The candidate encoder records its own exact encoded length and SHA only after the full stream is closed.

## Full measurement and evidence gates

`code/checkpoint35_constant_planes_complete.py` first rehashes the exact retained source bundle and scans every member. It computes the new dictionary length from the complete original rows, while checking the complete prior RGB hash. It then writes one candidate bundle, preserving every one of the other3,600 member byte streams and their hashes.

After closing that bundle, the program independently opens it, checks every unchanged member, executes the complete new streaming inverse, checks the intermediate RGB length/SHA, and executes the retained inverse to check the final original dictionary length/SHA and row count. It also rehashes the original source bundle. The measured candidate saving is the difference between the two complete compressed bundle sizes. This is a measurement, not an extrapolation from a prefix.

The tiny fixtures cover arbitrary byte data, constant0/255 data and irregular lengths. The bounded prefix trial covers complete actual dictionary records and verifies their entire recovered byte stream. The complete candidate's result is written only after all full-stream gates pass. A subsequent standalone restore of the entire checkpoint remains required before delivery. No original mathematical file, frozen snapshot, prior archive, row index or existing closed bundle is changed by this candidate program.
