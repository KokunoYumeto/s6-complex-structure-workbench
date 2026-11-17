"""Run the unchanged bundled save workflow and retain a precise error receipt.

This retries a preparation failure only, not an uncertain finalization.
It neither bypasses size/permission checks nor calls preparation separately.
"""
from pathlib import Path
import json, sys
D=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(D.parent/'.library_current'))
from library_upload import LibraryUploadWorkflow, HostedAppsClient, LibraryFileMaterializer, SignedUrlUploader
from library_hosted_apps import HostedAppsToolError
request=json.load(sys.stdin)
try:
    result=LibraryUploadWorkflow(apps_client=HostedAppsClient(),materializer=LibraryFileMaterializer(),uploader=SignedUrlUploader()).run(request)
except HostedAppsToolError as error:
    result={'status':'failed_before_transfer','message':str(error),'returned_error':error.result}
    print(json.dumps(result,ensure_ascii=False))
    raise SystemExit(1)
print(json.dumps(result,ensure_ascii=False))
