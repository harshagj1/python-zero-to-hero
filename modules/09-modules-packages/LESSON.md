# Module 09 — Modules and Packages

## Layman idea

One giant file becomes a mess. Pros split code into **modules** (`.py` files) and **packages** (folders of modules).

- **Module** = one toolbox file (`math_utils.py`)
- **Package** = a drawer of toolboxes (a folder with `__init__.py`)

## Importing

```python
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.pi)
```

### Your own module

`greeter.py`:
```python
def hello(name):
    return f"Hi {name}"
```

`app.py` (same folder):
```python
from greeter import hello
print(hello("Ada"))
```

## `if __name__ == "__main__"`

This line means: “Only run this part when I execute THIS file directly — not when someone imports it.”

```python
def main():
    print("Running as a program")

if __name__ == "__main__":
    main()
```

Pros put reusable functions at the top, and the “script behavior” under that guard.

## Packages (folder layout)

```
myapp/
  __init__.py
  utils.py
  services/
    __init__.py
    billing.py
```

```python
from myapp.utils import helper
from myapp.services.billing import charge
```

`__init__.py` can be empty; it marks a package (and can re-export names).

## PYTHONPATH / running as module

From project root:

```powershell
python -m projects.something
```

Prefer package-style imports as projects grow.

## Standard library vs third-party vs your code

| Kind | Example | Install? |
|------|---------|----------|
| Stdlib | `json`, `pathlib` | Built-in |
| Third-party | `requests`, `pytest` | `pip install` |
| Your code | `myapp/...` | Your files |

Never name your file `random.py` or `json.py` — you'll shadow the real modules.

## Exercises

1. Create `helpers.py` with `double(n)` and import it from another file.
2. Add `if __name__ == "__main__"` demo that prints a message only when run directly.
3. Explain in one sentence what a package is.

## Next

Explore `demo_package/`, run `run_me.py`, then **Module 10**.
