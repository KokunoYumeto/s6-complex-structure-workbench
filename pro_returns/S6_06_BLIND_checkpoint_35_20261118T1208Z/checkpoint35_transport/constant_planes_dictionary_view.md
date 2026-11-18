# Exact dictionary view and complete checkpoint restoration

The input is the closed constant-plane candidate already verified in
`checkpoint35_constant_planes_complete/result.json`. The complete original
dictionary has 1,901,249 rows and 5,533,013,871 bytes. Its constant-plane
representation has 1,868,804,034 bytes. Both original and intermediate
identities remain the identities in the existing transform record.

## 1. Verification before the first row is used

`store_verified_dictionary` reads the entire delivered encoded member and
copies those same bytes to a new private temporary file. Its input wrapper
hashes and counts every byte it copies. The existing `RGBReader` produces
the entire prior RGB stream, which a second wrapper hashes and counts.
The unchanged `checkpoint_png_rgb_dictionary.decode_stream` then produces
the entire original dictionary into a counting hash sink. The function
checks all three complete byte counts and SHA-256 values, and both row
counts, before it constructs any dictionary view. The output file is
closed before that construction. The view freshly hashes the closed
encoded file and checks its original encoded identity again.

The verified original dictionary is therefore the complete inverse of
this actual stored file. The access adapter never replaces the original
dictionary identity by an identity of selected rows.

## 2. Original row IDs and the exact access map

Write the original row lengths as \(n_i\), in their original order. The
constant-plane file retains each four-byte length. Its row payload is the
retained prefix, the three-bit flag and the three exact plane payloads of
the already proved format. Scanning those lengths and flags gives the
payload offsets \(o_i\). Consecutive offsets satisfy
\[
o_{i+1}=o_i+b_i+4,
\]
where \(b_i\) is the encoded payload length and the four bytes belong to
the next original row length. The final sentinel is the file size plus
four, so the same equation gives the last payload length. The scan checks
every flag, each nonzero constant-plane length, the exact file end and
the full original row count.

For original row ID \(i\), the adapter reads exactly the interval
\([o_i,o_{i+1}-4)\). It applies the existing constant-plane inverse at
the retained \(n_i\), and then the existing RGB-row inverse. These are
the same two maps used in the complete verification in section 1.
Consequently the returned byte string is precisely row \(i\) of that
verified original dictionary. The original IDs, lengths, row order and
all index-member bytes are unchanged. The returned length is checked.

The view owns its descriptor and two compact arrays: the original
lengths and the encoded payload offsets, including the final sentinel.
It records device, inode, size and nanosecond modification time after
the closed-file hash. Every row-object decode checks that identity at
entry and exit. Its cache stores only already reconstructed row bytes,
with a limit of 32 MiB and 8,192 entries; the entry limit also bounds
zero-length rows. Cache eviction does not modify either representation.
`close` empties the cache and closes the descriptor, and is idempotent.

## 3. Literal original PNG-codec member

The retained PNG row-object stores its entire original header prefix,
the ordered original row IDs, and the expected original member size and
SHA-256 value. The access decoder retains each check and each write of
the existing row-object decoder. Its sole data-source change replaces
the original dictionary `pread` by the access map in section 2. For IDs
\(i_1,\ldots,i_k\) the output is therefore literally
\[
\text{retained prefix}\;D_{i_1}\cdots D_{i_k},
\]
where \(D_i\) is row \(i\) of the complete original dictionary. The
expected member size and hash are checked after this concatenation.
The inherited PNG codec then restores the original PNG bytes and
checks its recorded compressed IDAT and complete PNG identities. Its
code and zlib parameter handling are unchanged.

## 4. Restorer lifetime and all final byte gates

The restorer retains a view under the original dictionary name after
section 1 passes. Its existing `dict_verified` identity is the original
dictionary byte count and hash. A PNG row object becomes ready either
through this registered verified view or through the existing original
dictionary file route. The latter route is unchanged. Each row object
must match that same original dictionary identity before decoding.

The original `dict_left` count decreases once per completed row object.
At zero, the view is closed before its private encoded file is removed.
The old file-backed route retains its existing descriptor-close and
temporary-file removal. The final dictionary gate additionally requires
that no views remain open. No frozen file, delivered bundle or original
archive is removed by this procedure.

All inherited gzip, zlib, raw, PNG and copy/add paths remain in the
restorer. It checks every retained content object and predecessor object
and then restores and verifies every frozen research file. The view
changes the temporary representation of one dictionary, with the exact
original-byte map proved above. Complete standalone recovery remains a
separate required execution gate.

## 5. Space accounting

During the dictionary stage the file allocation changes from the
5,533,013,871-byte original dictionary to its 1,868,804,034-byte verified
encoded view, a difference of 3,664,209,837 logical bytes. The final
research-file and duplicate-copy allocations still occur. The transport
headroom model therefore follows every actual selected dependency group,
the view lifetime, every retained object and every final duplicate; it
also records the frozen-file allocated-byte census and archive extraction
size. The candidate is used only with measured headroom for the maximum
of these actual stages.
