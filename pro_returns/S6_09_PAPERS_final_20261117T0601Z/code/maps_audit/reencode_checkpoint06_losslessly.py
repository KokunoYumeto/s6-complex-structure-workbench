"""Lossless transport encoding of the already frozen hour-six checkpoint.

The immutable input is never replaced. The output is newly created, and its
entire decompressed stream is checked against the frozen input byte hash.
This is an encoding retry of one checkpoint, not a new logical checkpoint.
"""
from pathlib import Path
import datetime
import hashlib
import json
import lzma
import resource
import subprocess
import time

D = Path(__file__).resolve().parents[2]
R = D.parent
original = R / "S6_09_PAPERS_checkpoint_06.zip"
output = R / "repacked_checkpoints/payload_06.zip.xz"
record = D / "work/maps_audit/checkpoint06_lossless_encoding.json"
stderr_path = D / "work/maps_audit/checkpoint06_xz.stderr.txt"
expected_sha = "13d04426c8832adf4fa4bdc5d198851f45afaeb2abcaff1e4aafa3ef21d800d0"
expected_bytes = 787828278

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(16 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

assert original.stat().st_size == expected_bytes
assert digest(original) == expected_sha
output.parent.mkdir(exist_ok=True)
command = [
    "xz", "--stdout", "--threads=1", "--check=sha256",
    "--lzma2=preset=1,dict=128MiB,mode=fast,mf=hc4,nice=32",
    str(original),
]
info = {
    "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro",
    "date_utc": "2026-11-17",
    "scope": "Lossless storage encoding retry of the exact already-frozen logical checkpoint06. The original ZIP and all earlier checkpoint files are preserved; no mathematical deliverable is edited by this script.",
    "original_file": str(original.relative_to(R)),
    "original_bytes": expected_bytes, "original_sha256": expected_sha,
    "transport_payload_file": str(output.relative_to(R)),
    "command": command, "cwd": str(R),
    "xz_version": subprocess.run(["xz", "--version"], capture_output=True, text=True, check=True).stdout.strip(),
    "started_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "compression running",
    "earlier_counter_only_trial": {
        "archive_written": False, "exit_code": 130,
        "reason": "Stopped on root instruction to produce the actual transport rather than continue a disposable counter-only measurement.",
        "last_reported_compressed_bytes": 67108864, "last_reported_seconds": 32.53,
    },
    "decoder": "Python standard-library lzma.open; no external decoder is required by the restoration helper.",
    "library_file_limit_bytes": 536870912,
    "wrapper_scope": "Root will create a standard ZIP wrapper with this payload, restoration helper and hash manifest, and will record the wrapper hash separately.",
}
record.write_text(json.dumps(info, indent=2) + "\n")
start = time.monotonic()
with output.open("xb") as stream, stderr_path.open("wb") as err:
    process = subprocess.run(command, cwd=R, stdout=stream, stderr=err)
info["compression_seconds"] = time.monotonic() - start
info["compression_exit_code"] = process.returncode
info["peak_child_rss_KiB"] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
info["stderr_record"] = str(stderr_path.relative_to(D))
info["compressed_bytes"] = output.stat().st_size
info["transport_payload_sha256"] = digest(output)
info["status"] = "compression complete; verifying decompression"
record.write_text(json.dumps(info, indent=2) + "\n")
if process.returncode:
    raise SystemExit(process.returncode)
start = time.monotonic()
restored_sha = hashlib.sha256()
restored_bytes = 0
with lzma.open(output, "rb") as stream:
    for chunk in iter(lambda: stream.read(16 * 1024 * 1024), b""):
        restored_sha.update(chunk)
        restored_bytes += len(chunk)
info["verification_seconds"] = time.monotonic() - start
info["decompressed_bytes"] = restored_bytes
info["decompressed_sha256"] = restored_sha.hexdigest()
info["original_still_unchanged"] = original.stat().st_size == expected_bytes and digest(original) == expected_sha
info["round_trip_passed"] = restored_bytes == expected_bytes and restored_sha.hexdigest() == expected_sha and info["original_still_unchanged"]
info["remaining_bytes_below_library_limit_before_wrapper"] = info["library_file_limit_bytes"] - info["compressed_bytes"]
info["finished_at_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
info["status"] = "verified exact lossless transport encoding" if info["round_trip_passed"] else "FAILED lossless verification"
record.write_text(json.dumps(info, indent=2) + "\n")
print(json.dumps(info, indent=2), flush=True)
assert info["round_trip_passed"]
assert info["compressed_bytes"] < info["library_file_limit_bytes"]
