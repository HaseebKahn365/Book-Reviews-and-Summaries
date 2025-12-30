"""
Alternative: Using Relative Imports with Namespace Packages

This example shows how to structure code to use relative imports.
The key is to have a common parent package that IS a regular package.
"""

# Create an alternative structure:
# plugin-png/
#   graphics/
#     plugins/
#       __init__.py
#       png/
#         __init__.py
#         decoder.py  <-- Can use: from ....engine import ...

# For this example, we'll demonstrate with a simpler approach:
# Put both engine and plugins in the same namespace directory

import sys
from pathlib import Path

# Alternative structure where relative imports work:
print("Alternative Structure for Relative Imports:")
print("""
unified-graphics/
  graphics/
    __init__.py          <-- Makes graphics a REGULAR package
    engine.py
    plugins/
      __init__.py
      svg.py             <-- Can use: from ..engine import ...
      png.py
""")

print("\nKey Differences:")
print("1. Namespace Package (current): NO __init__.py in graphics/")
print("   - Multiple separate directories merge")
print("   - Use absolute imports: from graphics.engine import ...")
print("")
print("2. Regular Package: HAS __init__.py in graphics/")
print("   - Single directory structure")
print("   - Can use relative imports: from ..engine import ...")
print("")
print("Both approaches are valid! Choose based on your needs:")
print("- Namespace: For distributed plugins from different sources")
print("- Regular: For a single cohesive package with relative imports")
