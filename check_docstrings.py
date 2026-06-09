# scripts/check_docstrings.py

import ast
import pathlib
import sys

failed = False

for file in pathlib.Path(".").rglob("*.py"):

    with open(file) as f:
        tree = ast.parse(f.read())

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            if ast.get_docstring(node) is None:

                print(
                    f"{file}: function '{node.name}' "
                    "missing docstring"
                )

                failed = True

if failed:
    sys.exit(1)

print("All functions have docstrings")
