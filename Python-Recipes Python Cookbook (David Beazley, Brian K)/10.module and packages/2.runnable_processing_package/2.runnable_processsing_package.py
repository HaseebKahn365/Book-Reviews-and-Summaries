#!/usr/bin/env python3

import sys
from pathlib import Path

base_dir = Path(__file__).parent
sys.path.insert(0, str(base_dir))

print("=" * 60)
print("Testing Runnable Data-Processing Package")
print("=" * 60)

print("\n1. Running package with python -m processor")
print("-" * 60)

import subprocess
result = subprocess.run(
    [sys.executable, "-m", "processor"],
    cwd=base_dir,
    capture_output=True,
    text=True
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)

print("\n2. Testing __all__ exports")
print("-" * 60)
from processor.core import *

print(f"Exported functions: {[name for name in dir() if not name.startswith('_')]}")

try:
    _internal_helper()
    print("ERROR: _internal_helper should not be accessible!")
except NameError:
    print("✓ _internal_helper is correctly hidden by __all__")

print("\n3. Direct import and execution")
print("-" * 60)
from processor import run_process
config = run_process()

print("\n" + "=" * 60)
print("All tests completed!")
print("=" * 60)
