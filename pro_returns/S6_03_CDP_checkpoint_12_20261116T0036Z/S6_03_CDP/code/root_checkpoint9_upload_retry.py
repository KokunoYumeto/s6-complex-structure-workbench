"""Retry the known failed preparation through the unchanged upload workflow."""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root.parent / 'library_helpers_current'))
from library_upload import (LibraryUploadWorkflow, HostedAppsClient,
                            LibraryFileMaterializer, SignedUrlUploader)
from library_hosted_apps import HostedAppsToolError

request = {'uploads': [{
    'local_path': str(root.parent / 'S6_03_CDP_checkpoint_09.zip'),
    'purpose': 'create_library_file', 'library_artifact_type': 'other'}]}
try:
    result = LibraryUploadWorkflow(apps_client=HostedAppsClient(),
        materializer=LibraryFileMaterializer(),
        uploader=SignedUrlUploader()).run(request)
    (root / 'records/checkpoint_09_library.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print('Upload workflow completed; ordered receipt saved.')
except HostedAppsToolError as exc:
    safe = {'error': str(exc)}
    texts = []
    for block in exc.result.get('content', []):
        if block.get('type') == 'text':
            txt = block.get('text', '')
            txt = re.sub(r'https?://\S+', '[URL REDACTED]', txt)
            texts.append(txt[:2000])
    safe['error_text'] = texts
    (root / 'records/checkpoint_09_upload_error.json').write_text(
        json.dumps(safe, indent=2) + '\n')
    print(json.dumps(safe, indent=2))
    raise SystemExit(1)
