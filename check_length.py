# scripts/check_length.py

import pathlib
import sys

for file in pathlib.Path(".").rglob("*.py"):

    with open(file) as f:
        lines = len(f.readlines())

    if lines > 100:
        print(f"{file} has {lines} lines (limit: 100)")
        sys.exit(1)

print("All Python files under 100 lines")
