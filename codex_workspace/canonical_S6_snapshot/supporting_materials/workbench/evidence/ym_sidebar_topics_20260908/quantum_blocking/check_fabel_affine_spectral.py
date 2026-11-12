"""Run the full independent geometry/coefficient diagnostic for this map."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("check_fabel_tensor_transfer.py")),run_name="__main__")
