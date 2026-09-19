# Module 17 — Standard Library Essentials

## Layman idea

Before installing packages, learn the **batteries included** with Python. Pros reach for the stdlib first.

## Must-know modules

### `pathlib` — files and folders
```python
from pathlib import Path
p = Path("data") / "file.txt"
p.write_text("hi", encoding="utf-8")
```

### `datetime` — time
```python
from datetime import datetime, timedelta, timezone
now = datetime.now(timezone.utc)
tomorrow = now + timedelta(days=1)
```

### `json` — data interchange
```python
import json
json.dumps({"ok": True})
json.loads('{"ok": true}')
```

### `collections` — better containers
```python
from collections import Counter, defaultdict, deque

Counter("banana")                 # counts letters
defaultdict(list)                 # auto-make missing keys
deque([1,2,3], maxlen=3)          # fast queue
```

### `itertools` — iterator algebra
```python
from itertools import chain, islice, groupby
```

### `re` — regular expressions (text patterns)
```python
import re
re.findall(r"\d+", "a1 b23")  # ['1', '23']
```

Learn regex gradually; don't force it when `.split` / `.replace` is enough.

### `logging` — pro output (better than endless prints)
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("started")
```

### `argparse` — CLI arguments (also Module 20)
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name")
args = parser.parse_args()
```

### `urllib` / prefer `http.client` carefully
For real apps you'll often use `httpx`/`requests` (Module 21), but know stdlib exists.

## Exercises

1. Create a folder `out/` and write a timestamped file with pathlib + datetime.
2. Count word frequencies in a sentence with `Counter`.
3. Parse a simple phone-like pattern with `re`.
4. Replace `print` debugging in a small script with `logging`.

## Next

Run `stdlib_demo.py`, then **Module 18**.
