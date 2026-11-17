#!/usr/bin/env python3
"""Independently exercise the unchanged archive restoration helper in isolation.

The canonical workspace and checkpoint are read only.  The temporary archive
tree contains hardlinks to the 717 retained PNGs and copies of the manifest and
helper.  Missing duplicate paths are created only in that temporary tree.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

HERE = Path(__file__).resolve().parent
D = HERE.parents[2]
ROOT = D.parent
MANIFEST = D / "records/visual_asset_deduplication.json"
HELPER = D / "code/editorial/restore_duplicate_visual_assets.py"
CHECKPOINT = ROOT / "S6_09_PAPERS_checkpoint_06.zip"
CODE_NAMES = ["plan_visual_asset_deduplication.py", "restore_duplicate_visual_assets.py",
              "repack_checkpoint_losslessly.py", "package_final.py"]


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def write_json(name, obj):
    (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def safe_relative(name):
    p = PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts and p.suffix == ".png", name
    return Path(*p.parts)


def run_helper(tree, name, restore, expected_exit=0):
    command = [sys.executable, str(tree / "code/editorial/restore_duplicate_visual_assets.py")]
    if restore: command.append("--restore")
    start = time.monotonic()
    result = subprocess.run(command, cwd=tree, capture_output=True, text=True)
    (HERE / (name + ".stdout.txt")).write_text(result.stdout)
    (HERE / (name + ".stderr.txt")).write_text(result.stderr)
    record = {"name": name, "command": command, "working_directory": str(tree),
              "returncode": result.returncode, "expected_returncode": expected_exit,
              "elapsed_seconds": time.monotonic()-start,
              "stdout": name + ".stdout.txt", "stderr": name + ".stderr.txt",
              "stdout_sha256": sha_bytes(result.stdout.encode()), "stderr_sha256": sha_bytes(result.stderr.encode())}
    assert result.returncode == expected_exit, record
    if expected_exit == 0:
        record["parsed_output"] = json.loads(result.stdout)
        assert record["parsed_output"]["passed"] is True
    else:
        assert "AssertionError" in result.stderr and not result.stdout.strip(), record
        record["expected_refusal_confirmed"] = True
    return record


def verify_logical(tree, unique, aliases, special=None):
    special = special or {}
    rows = []
    for item in unique + aliases:
        name = item.get("original_path", item.get("path"))
        p = tree / safe_relative(name)
        assert p.is_file() and not p.is_symlink(), name
        expected_bytes, expected_sha = special.get(name, (item["bytes"], item["sha256"]))
        actual_sha = sha_file(p)
        actual_bytes = p.stat().st_size
        assert (actual_bytes, actual_sha) == (expected_bytes, expected_sha), name
        rows.append({"path": name, "retained_path": item.get("retained_path", name),
                     "bytes": actual_bytes, "sha256": actual_sha,
                     "matches_original_manifest": name not in special})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep-tree", action="store_true", help="Keep the independently restored temporary tree for inspection")
    args = parser.parse_args()
    manifest_bytes = MANIFEST.read_bytes()
    helper_bytes = HELPER.read_bytes()
    plan = json.loads(manifest_bytes)
    unique, aliases = plan["unique_payloads"], plan["aliases"]
    assert (len(unique), len(aliases), plan["source_png_paths"]) == (717, 1015, 1732)
    assert plan["unique_png_payloads"] == 717 and plan["duplicate_png_paths"] == 1015
    by_unique = {x["path"]: x for x in unique}
    alias_names = [x["original_path"] for x in aliases]
    assert len(by_unique) == 717 and len(set(alias_names)) == 1015
    assert not set(by_unique).intersection(alias_names)
    assert len({x["sha256"] for x in unique}) == 717
    for item in unique:
        safe_relative(item["path"])
    for item in aliases:
        safe_relative(item["original_path"]); safe_relative(item["retained_path"])
        retained = by_unique[item["retained_path"]]
        assert (item["bytes"], item["sha256"]) == (retained["bytes"], retained["sha256"])
    declared_paths = set(by_unique).union(alias_names)
    actual_png_paths = {str(p.relative_to(D)) for p in D.rglob("*.png") if p.is_file()}
    assert declared_paths == actual_png_paths, "The plan does not cover the exact current PNG path set"
    before_codes = {name: sha_file(D / "code/editorial" / name) for name in CODE_NAMES}
    checkpoint_before = sha_file(CHECKPOINT)
    assert checkpoint_before == "13d04426c8832adf4fa4bdc5d198851f45afaeb2abcaff1e4aafa3ef21d800d0"
    with zipfile.ZipFile(CHECKPOINT) as archive:
        member_list = archive.namelist()
        assert len(member_list) == len(set(member_list)) == 7296
        assert not any(x.is_dir() for x in archive.infolist())
        assert declared_paths.issubset(set(member_list))
        assert "READ_THIS_CHECKPOINT.txt" not in member_list
    print("Manifest partition and immutable checkpoint identity verified.", flush=True)

    temp_parent = Path(tempfile.mkdtemp(prefix="s6_archive_restore_validation_", dir=ROOT))
    tree = temp_parent / "archive"
    tree.mkdir()
    assert not tree.resolve().is_relative_to(D.resolve())
    (tree / "code/editorial").mkdir(parents=True)
    (tree / "records").mkdir()
    (tree / "code/editorial/restore_duplicate_visual_assets.py").write_bytes(helper_bytes)
    (tree / "records/visual_asset_deduplication.json").write_bytes(manifest_bytes)
    linked = []
    for item in unique:
        rel = safe_relative(item["path"])
        source, target = D / rel, tree / rel
        assert source.is_file() and not source.is_symlink()
        assert source.stat().st_size == item["bytes"] and sha_file(source) == item["sha256"]
        target.parent.mkdir(parents=True, exist_ok=True)
        os.link(source, target)
        a, b = source.stat(), target.stat()
        assert (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)
        linked.append({"path": item["path"], "bytes": item["bytes"], "sha256": item["sha256"],
                       "hardlink_device": a.st_dev, "hardlink_inode": a.st_ino})
    assert all(not (tree / name).exists() for name in alias_names)
    write_json("unique_payload_hardlinks.json", linked)
    commands = []
    r = run_helper(tree, "01_verify_before_restoration", False)
    assert r["parsed_output"] == {"passed": True, "unique_payloads_verified": 717,
                                 "duplicate_paths_restored": 0, "duplicate_paths_available_to_restore": 1015,
                                 "all_original_bytes_preserved": True}
    commands.append(r)
    r = run_helper(tree, "02_restore_all_aliases", True)
    assert r["parsed_output"] == {"passed": True, "unique_payloads_verified": 717,
                                 "duplicate_paths_restored": 1015, "duplicate_paths_available_to_restore": 0,
                                 "all_original_bytes_preserved": True}
    commands.append(r)
    restored_rows = verify_logical(tree, unique, aliases)
    write_json("all_1732_restored_payloads.json", restored_rows)
    print("All 1015 aliases restored; all 1732 full payload SHA256 values independently matched.", flush=True)

    r = run_helper(tree, "03_idempotent_restore", True)
    assert r["parsed_output"]["duplicate_paths_restored"] == 0
    assert r["parsed_output"]["duplicate_paths_available_to_restore"] == 0
    commands.append(r)

    # The first alias is deliberately a copied restored file, never a retained
    # hardlink. Changing it therefore cannot change a canonical source payload.
    conflict = aliases[0]
    target = tree / conflict["original_path"]
    retained = tree / conflict["retained_path"]
    assert (target.stat().st_dev, target.stat().st_ino) != (retained.stat().st_dev, retained.stat().st_ino)
    sentinel = b"Deliberately different existing file: isolated archive overwrite-refusal test.\n"
    target.write_bytes(sentinel)
    conflict_before = target.stat()
    r = run_helper(tree, "04_refuse_different_existing_alias", True, expected_exit=1)
    assert target.read_bytes() == sentinel
    conflict_after = target.stat()
    assert (conflict_before.st_ino, conflict_before.st_mtime_ns, conflict_before.st_size) == (conflict_after.st_ino, conflict_after.st_mtime_ns, conflict_after.st_size)
    commands.append(r)
    conflict_rows = verify_logical(tree, unique, aliases,
                                  {conflict["original_path"]: (len(sentinel), sha_bytes(sentinel))})
    write_json("overwrite_refusal_check.json", {
        "passed": True, "original_alias": conflict["original_path"], "retained_path": conflict["retained_path"],
        "sentinel_bytes": len(sentinel), "sentinel_sha256": sha_bytes(sentinel),
        "exit_code": 1, "expected_assertion_refusal": True,
        "different_existing_bytes_inode_and_mtime_unchanged": True,
        "all_other_original_payloads_unchanged": len(conflict_rows)-1,
        "canonical_retained_source_untouched": sha_file(D / conflict["retained_path"]) == conflict["sha256"]})
    print("Different existing alias refused with exit1; sentinel and the other 1731 payloads unchanged.", flush=True)

    target.unlink()
    r = run_helper(tree, "05_restore_removed_test_alias", True)
    assert r["parsed_output"]["duplicate_paths_restored"] == 1
    assert r["parsed_output"]["duplicate_paths_available_to_restore"] == 0
    commands.append(r)
    final_rows = verify_logical(tree, unique, aliases)
    assert final_rows == restored_rows

    # Recheck all canonical image files, not only the retained hardlinked ones.
    canonical_rows = verify_logical(D, unique, aliases)
    assert canonical_rows == restored_rows
    after_codes = {name: sha_file(D / "code/editorial" / name) for name in CODE_NAMES}
    assert after_codes == before_codes and MANIFEST.read_bytes() == manifest_bytes
    assert HELPER.read_bytes() == helper_bytes
    checkpoint_after = sha_file(CHECKPOINT)
    assert checkpoint_after == checkpoint_before
    write_json("execution_manifest.json", commands)
    if not args.keep_tree:
        shutil.rmtree(temp_parent)
        assert not temp_parent.exists()
    report = {"passed": True, "gate_passed": True,
              "reader": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)", "effort": "Pro", "date_utc": "2026-11-17",
              "manifest_sha256": sha_bytes(manifest_bytes), "reviewed_code_sha256": before_codes,
              "original_checkpoint_sha256_before": checkpoint_before, "original_checkpoint_sha256_after": checkpoint_after,
              "original_checkpoint_bytes": CHECKPOINT.stat().st_size, "original_checkpoint_members": len(member_list),
              "retained_unique_pngs_hardlinked": len(linked), "duplicate_aliases_restored": len(aliases),
              "complete_logical_png_paths_verified": len(restored_rows),
              "complete_logical_png_bytes_verified": sum(x["bytes"] for x in restored_rows),
              "all_logical_full_sha256_match": True, "idempotent_repeat_passed": True,
              "different_existing_file_refused": True, "different_existing_file_unchanged": True,
              "all_other_paths_unchanged_after_refusal": True, "conflict_recovery_restore_count": 1,
              "canonical_all_1732_pngs_unchanged": True, "canonical_code_and_manifest_unchanged": True,
              "original_checkpoint_unchanged": True, "temporary_tree": str(tree),
              "temporary_tree_retained": args.keep_tree,
              "temporary_tree_cleanup_did_not_touch_canonical_hardlink_targets": not args.keep_tree,
              "execution_manifest": "execution_manifest.json", "full_payload_hash_record": "all_1732_restored_payloads.json",
              "refusal_record": "overwrite_refusal_check.json",
              "scope": "Actual unchanged production helper run on the full actual717-payload/1015-alias manifest in an isolated tree. Every original logical image path and full SHA256 is verified; canonical papers, code and original checkpoint are not edited."}
    write_json("validation_report.json", report)
    print(json.dumps({k:report[k] for k in ["passed","retained_unique_pngs_hardlinked","duplicate_aliases_restored","complete_logical_png_paths_verified","different_existing_file_refused","original_checkpoint_unchanged","temporary_tree_retained"]}), flush=True)


if __name__ == "__main__":
    main()
