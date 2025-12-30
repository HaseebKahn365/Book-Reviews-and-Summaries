# Plugin-Driven Graphics Framework

## Overview

Demonstrates namespace packages, dynamic loading, and relative imports.

## Directory Structure

```
10.module and packages/
├── engine-base/
│   └── graphics/              # NO __init__.py (Namespace Package)
│       └── engine.py          # Core engine with load_plugin()
│
├── plugin-svg/
│   └── graphics/              # NO __init__.py (Namespace Package)
│       └── plugins/
│           ├── __init__.py    # Makes plugins a proper package
│           └── svg.py         # SVG plugin with relative imports
│
└── demo_graphics.py           # Demo script
```

## Key Concepts

### 1. Namespace Packages (10.5)

- `graphics/` directories have **NO `__init__.py`**
- Multiple directories merge into single `graphics` namespace
- Allows plugins from different locations to coexist

### 2. Dynamic Loading (10.10)

- `load_plugin(name)` uses `importlib.import_module()`
- Loads plugins at runtime by string name
- Example: `load_plugin("svg")` → imports `graphics.plugins.svg`

### 3. Relative Imports (10.3)

- `svg.py` uses `from ...engine import register_format`
- Goes up 2 levels: `plugins` → `graphics` → imports `engine`
- Requires proper package structure with `__init__.py` in `plugins/`

## Usage

```python
# Add both namespace roots to sys.path
sys.path.extend(["engine-base", "plugin-svg"])

# Import and use
from graphics.engine import load_plugin

svg = load_plugin("svg")
decoder = svg.SVGDecoder()
decoder.decode("<svg>...</svg>")
```

## Run Demo

```bash
python demo_graphics.py
```

## Adding New Plugins

1. Create new directory: `plugin-xyz/graphics/plugins/`
2. Add `__init__.py` in `plugins/`
3. Create `xyz.py` with relative imports: `from ...engine import ...`
4. Add to `sys.path` and load: `load_plugin("xyz")`
