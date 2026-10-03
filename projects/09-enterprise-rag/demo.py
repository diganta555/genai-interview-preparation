"""Runnable offline learning reference for Enterprise Knowledge Assistant. See README scope."""
import runpy
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
if __name__=='__main__':
    runpy.run_module('examples.security',run_name='__main__')
