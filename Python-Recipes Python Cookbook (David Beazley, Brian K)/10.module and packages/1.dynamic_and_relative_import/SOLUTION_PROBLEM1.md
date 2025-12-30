# Problem 1: Plugin-Driven Graphics Framework - SOLUTION

## ✅ Implementation Complete

### Structure Created

```
10.module and packages/
├── engine-base/
│   └── graphics/              # NO __init__.py → Namespace Package
│       └── engine.py          # Core engine with load_plugin()
│
├── plugin-svg/
│   └── graphics/              # NO __init__.py → Namespace Package
│       └── plugins/
│           ├── __init__.py    # Makes plugins a proper package
│           └── svg.py         # SVG plugin
│
├── demo_graphics.py           # Working demo
├── relative_imports_explained.py
└── README_GRAPHICS.md
```

## Key Concepts Demonstrated

### ✅ 1. Namespace Packages (10.5)

- **No `__init__.py`** in `graphics/` directories
- Multiple directories (`engine-base/graphics` + `plugin-svg/graphics`) **merge** into single namespace
- Allows plugins from different developers/locations to coexist
- View merged paths: `graphics.__path__` shows both directories

### ✅ 2. Dynamic Loading (10.10)

```python
def load_plugin(plugin_name):
    module_path = f"graphics.plugins.{plugin_name}"
    return importlib.import_module(module_path)
```

- Runtime loading by string name
- No need to know plugins at compile time

### ✅ 3. Imports in Namespace Packages (10.3)

**Important Discovery:**

- **Namespace packages** → Use **absolute imports**
  ```python
  from graphics.engine import register_format  # ✅ Works
  ```
- **Regular packages** → Can use **relative imports**
  ```python
  from ..engine import register_format  # ✅ Works only with __init__.py
  ```

## Why Absolute Imports for Namespace Packages?

Relative imports like `from ...engine` require a clear parent package hierarchy. With namespace packages:

- `graphics/` has NO `__init__.py`
- Python can't establish a fixed parent-child relationship
- Multiple `graphics/` directories exist in different locations

**Solution:** Use absolute imports since both directories are in `sys.path` and merge into the `graphics` namespace.

## Demo Output

```bash
$ python3 demo_graphics.py

============================================================
Plugin-Driven Graphics Framework Demo
============================================================

1. Loading SVG plugin dynamically...
   Loaded module: <module 'graphics.plugins.svg' from '...'>

2. Creating SVG decoder instance...
[Engine] Registered format: SVG

3. Plugin information:
   name: SVG Decoder
   version: 1.0
   formats: ['svg', 'svgz']

4. Decoding SVG data...
[SVG Plugin] Decoding SVG data...
[Engine] Rendering SVG data...
   Result: Rendered: <svg><circle cx="50" cy="50" r="40"/></svg>

6. Namespace package structure:
   graphics.__path__ = _NamespacePath(['.../plugin-svg/graphics',
                                       '.../engine-base/graphics'])
```

## Adding New Plugins

1. Create: `plugin-xyz/graphics/plugins/xyz.py`
2. Add `__init__.py` in `plugins/`
3. Use absolute imports: `from graphics.engine import ...`
4. Add to `sys.path` and load: `load_plugin("xyz")`

## Concepts Checklist

- ✅ Hierarchical Packages (10.1) - `graphics.plugins.svg`
- ✅ Relative vs Absolute Imports (10.3) - Explained both approaches
- ✅ Namespace Packages (10.5) - Multiple directories merge
- ✅ Dynamic Loading (10.10) - `importlib.import_module()`

**Difficulty: Medium** ✅ Completed
