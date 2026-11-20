"""Serialize assembly and compilation of the shared current paper sources."""
from contextlib import contextmanager
from pathlib import Path
import fcntl

@contextmanager
def pipeline_lock(root):
    path=Path(root)/'analysis/series_pipeline.lock'
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('a') as lock:
        fcntl.flock(lock.fileno(),fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock.fileno(),fcntl.LOCK_UN)
