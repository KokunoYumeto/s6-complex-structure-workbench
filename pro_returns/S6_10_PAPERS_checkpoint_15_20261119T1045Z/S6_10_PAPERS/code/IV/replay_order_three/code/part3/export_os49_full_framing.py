#!/usr/bin/env python3
"""Reproduce the corrected OC local proof, retaining its Refuted statement."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('export_post19_blind_recovery.py')),run_name='__main__')
