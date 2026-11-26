#!/usr/bin/env python3
"""Write the local LE completion/input and execution-account supplements."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT / "agents/continuation7_iii_mixed_torsion"
INPUT = LANE / "S6_SERIES_PUBLISH_III_02LE_inputs_and_primary_reading.md"
NOTE = LANE / "S6_SERIES_PUBLISH_III_02LE_execution_reading.md"
assert not NOTE.exists()
old = INPUT.read_text()
assert "## Completion supplement" not in old
now = datetime.now(timezone.utc).isoformat()
b = chr(96)
supplement = f"""

## Completion supplement, {now}

The future-tense statements above record intake. The new computation and
the complete mathematical derivation are now finished; the LE original
and all held target material remain unopened. The source and every one
of its 333 stdout lines were read. Its separate stderr exists and is
zero bytes. The complete fresh proof was reread through its final line,
followed by the exact final notation changes and rank-one parity sentence.
The final local input/execution notes are to receive their final reading
before the completion time and hashes are sent to root.

The new program {b}code/S6_SERIES_PUBLISH_c7_le_mixed_v001.py{b}
contains 477 lines and reads only the raw fixture named above. It
recomputes all 172 natural rows, all twelve LE patterns on ten rows,
every actual period matrix and inverse, the angular and wedge-chain
integer sections, every rank-one basis, prescribed-fan character and
degree, finite fixed vector, full CRT invariant, and model map with its
inverse. All 34 printed marked pair maps were inspected. The written
proof treats every allowed finite order and affine twist algebraically;
the displayed parameter choices establish realization.

The complete result retains the twelve-pattern catalogue. It proves
three oriented types at order ten and two at order fourteen, with the
full primitive-fibre invariant and connected-sum maps in proof Sections
10--13. This is a fresh result submitted for root review; no required
row is closed here and no claim about an unseen original auxiliary is
made. The exact target's uniform conic factor and two/one type counts
are contradicted by the exhibited preserved cubic and refined class.

For full admitted-input provenance, this intake also consulted lines
1--280 of {b}code/S6_SERIES_PUBLISH_c7_lc_odd_cubic.py{b}, the
already admitted LC computation, to confirm the raw period formulas and
fixture scope. This is disclosed admitted-code exposure, not an LE
historical algorithm. The new LE computation enumerates the raw criterion
afresh and constructs its integer sections by the saved Euclidean
procedure. No LC target table is loaded. The L1 graph note was revisited
at lines 1--140 and 397 through its end after its earlier complete reading.
The actual raw matrices and cocycles used for LE are all printed and
read in the new output.

The LF conversion and presentation repair history are recorded in
{b}S6_SERIES_PUBLISH_III_02LE_execution_reading.md{b}. The executed
v001 source/output are preserved. The corrected v002 source is saved
but was not run. All publications remain outside the working tree.
No LE original release or original-comparison credit is asserted.
"""
INPUT.write_text(old + supplement)

execution = f"""# III 02LE: actual execution and final-reading account

Checker: ChatGPT Pro mode; numerical effort is not separately exposed.
Written at {now}. This is a human-readable account of the new programs
and their retained streams, including the exact line-ending conversion
and the observed presentation-repair failure. It gives no additional
independent theorem-check credit.

## The one executed catalogue calculation

The complete source is
{b}code/S6_SERIES_PUBLISH_c7_le_mixed_v001.py{b}, 477 lines,
SHA256 {b}9f86482aca7952719c5fd34037a411d7675e091896cf3f176d5c10bb68c68a42{b}.
It was executed once with explicit separate stdout and stderr redirection,
under shell noclobber. It began at
2026-11-25T03:32:17.051108+00:00 and printed completion at
2026-11-25T03:32:17.599060+00:00. That process exited zero.
No failed version of this mathematical catalogue program was run.

Its retained files are
{b}code/S6_SERIES_PUBLISH_c7_le_mixed_v001.out{b} and
{b}code/S6_SERIES_PUBLISH_c7_le_mixed_v001.err{b}.
The stdout has 333 lines and SHA256
{b}0ea6a63da32f30f54d05bce170fd09f61c6c6fc10f1248f4b747c79f498d7b55{b}.
The stderr is an actual retained zero-byte file; its SHA256 is
{b}e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855{b}.
The full source and all stdout were read, including every one of the
twelve patterns and 34 marked pair maps. No execution of a historical
LE program or output is asserted.

The JSON contains the same complete exact matrices and coordinates
printed in stdout. Its SHA256 is
{b}8816e5af8593ed9758496217fe14a553fc8e4a2ee48ea7069d27d990ac9f9bf0{b}.
The proof explains separately the algebraic, unbounded parameter scope.
The program's all_parameter_scope field records that proof scope; it
does not claim an infinite numerical enumeration.

## Exact TSV conversion after the successful run

The executed v001 writer used the CSV library's default CRLF terminator.
Its original table had 533 bytes and SHA256
{b}96c676f1c82c7b1681723b7c1cfb6891f054be567baaef349a03bc31d044c9a5{b}.
At root's checkpoint request, the separately saved program
{b}code/S6_SERIES_PUBLISH_c7_le_lf_conversion.py{b}
ran successfully at 2026-11-25T03:46:08.213870+00:00.
Its matching .out and .err files are retained; the source and complete
output were read and the actual stderr is zero bytes.

The conversion stdout retains the exact original table bytes in base64.
Decoding that string recovers the 533-byte file without reconstruction
from mathematical values. The program verifies that changing LF back
to CRLF gives byte equality and that parsed fields are unchanged.
The current table has 520 bytes and SHA256
{b}383bb8e3cd9956b6c917e0f1ac1fb5b094439c68c286bdf261e9ea857f5524a2{b}.
This is the converted file's hash, not the original run's table hash.

The conversion also saved
{b}code/S6_SERIES_PUBLISH_c7_le_mixed_v002.py{b},
SHA256 {b}2a9c95dbdecd968a3d67a0fa50d40093d96c1a06c4359be49e64af2fb9687cb3{b}.
It adds explicit LF output and changes version/output suffixes to v002.
The complete diff was read. This source was not run; no v002 computation
output or verification credit is claimed. The executed v001 source and
its streams were not changed.

## Presentation-repair attempts and their exact limits

An initial code-mode invocation attempting to create the presentation
repair source failed at the JavaScript parser because literal backticks
inside its Python text closed the surrounding JavaScript template.
No nested tool or Python process ran in that invocation.
The available exact invocation text and actual parser result are retained
in {b}code/S6_SERIES_PUBLISH_c7_le_text_repairs_orchestration_attempt001.js{b}
and its matching .out. They were retained from the available current
tool-call text after the failure and were wholly read. The result was
“SyntaxError: missing ) after argument list”. There was no Python
stdout/stderr for that parser failure. This account does not invent
streams for a process that never began.

The successful source
{b}code/S6_SERIES_PUBLISH_c7_le_text_repairs_v001.py{b}
uses chr(96) for those character comparisons. It ran at
2026-11-25T03:54:20.782212+00:00 with separately retained .out/.err.
The complete source and all 510 output lines were read. The actual
stderr is zero bytes. Its output records every restored control/command
sequence and each of 495 inline-delimiter repairs. Displayed equations
and equation-number references were retained.

The subsequent complete proof reread identified three thin-space
expressions, two numerical inline delimiters, a stray escape, and the
Phi/mu commands. The bounded source
{b}code/S6_SERIES_PUBLISH_c7_le_final_text_v001.py{b}
repairs those literal strings, adds the explicit odd first-period
content argument for rank-one support integrality, and appends the
conversion account to the proof. It ran successfully at
2026-11-25T04:01:58.479094+00:00. Its full source and complete matching
.out were read; the separately retained .err is zero bytes.
The exact changed passages were reread after the whole-proof reading.
There was no catalogue rerun during these presentation repairs.

## Reading and scope

The complete mathematical source, all new numerical output, all twelve
patterns, every retained inverse and invariant coordinate, the complete
fresh proof, and the exact final changes have been inspected. The
conversion source/output and repair source/output were also wholly read.
An earlier combined read was truncated by the tool; its missing source
and output ranges were then read in smaller complete calls and receive
credit only from those later reads.

The local notes are produced by
{b}code/S6_SERIES_PUBLISH_c7_le_completion_notes_v001.py{b},
with its own separate .out/.err. Their final full reading and the
completion time are reported to root after this write. The original LE
proof, outline and historical target programs/tables remain closed.
No global file or canonical manuscript was edited, and no build,
whole-PDF or publication-completion credit is claimed.
"""
NOTE.write_text(execution)
print("Notes written UTC", now)
for p in (INPUT, NOTE):
    print(p.relative_to(ROOT), "lines", len(p.read_text().splitlines()), "SHA256", sha256(p.read_bytes()).hexdigest())
print("PASS: local factual completion/input and execution-account notes only")
