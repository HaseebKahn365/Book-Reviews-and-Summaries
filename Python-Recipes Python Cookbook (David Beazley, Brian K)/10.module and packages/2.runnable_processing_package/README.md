# Problem 2: Runnable Data-Processing Package

## Structure

```
processor/
├── __init__.py       # Package exports
├── __main__.py       # Runnable entry point
├── core.py           # Core logic with __all__
└── config.json       # Configuration data
```

## Key Concepts

### 1. Runnable Package (10.7)

Execute with: `python -m processor`

- `__main__.py` makes package executable
- Entry point for command-line usage

### 2. Resource Loading (10.8)

```python
pkgutil.get_data(__package__, 'config.json')
```

- Works even if package is zipped
- Portable across installations

### 3. Controlled Exports (10.2)

```python
__all__ = ['run_process']
```

- `_internal_helper()` hidden from `import *`
- Only `run_process` exported

## Usage

### Run as module

```bash
python3 -m processor
```

### Import and use

```python
from processor import run_process
run_process()
```

### Test exports

```python
from processor.core import *
# Only run_process available
# _internal_helper not accessible
```

## Demo

```bash
python3 demo_processor.py
```
