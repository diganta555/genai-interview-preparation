"""Runnable offline learning reference for Document Intelligence System. See README scope."""
import runpy
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
if __name__=='__main__':
    runpy.run_module('examples.dataset',run_name='__main__')
