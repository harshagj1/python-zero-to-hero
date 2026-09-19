# Module 19 — Concurrency and Async

## Layman idea

Sometimes you wait on the network/disk a lot. Your CPU is idle while waiting.

Three tools:

| Tool | Metaphor | Best for |
|------|----------|----------|
| Threads | Multiple cooks sharing one kitchen | I/O waits, some libraries |
| Processes | Multiple kitchens | Heavy CPU work |
| asyncio | One cook juggling many pots | Many network requests |

## Threads (high level)

```python
from concurrent.futures import ThreadPoolExecutor

def fetch(url): ...

with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, urls))
```

Watch out: threads share memory — use locks if mutating shared data.

## Processes

```python
from concurrent.futures import ProcessPoolExecutor
```

Use for CPU-bound tasks (image processing, heavy math). Higher overhead.

## asyncio — modern Python networking style

```python
import asyncio

async def work(name):
    print("start", name)
    await asyncio.sleep(1)  # non-blocking wait
    print("end", name)

async def main():
    await asyncio.gather(work("a"), work("b"), work("c"))

asyncio.run(main())
```

Key words:

- `async def` = coroutine function
- `await` = pause here until that wait finishes, let others run
- `asyncio.gather` = run many concurrently

## Choosing wisely (senior judgment)

- Lots of HTTP calls → asyncio or thread pool
- Heavy CPU → processes / native extensions
- Simple script → plain sync code first
- Don't make everything async “because it's cool”

## GIL (plain English)

CPython has a Global Interpreter Lock: threads don't speed up pure-Python CPU math much. They still help with I/O waiting.

## Exercises

1. Run three `asyncio.sleep` tasks concurrently and sequentially; compare time.
2. Use `ThreadPoolExecutor` to run a blocking `time.sleep` fake download.
3. Write down one CPU-bound and one I/O-bound example from your life.
4. Read an async FastAPI handler later in Module 21.

## Next

Run `async_demo.py`, then **Module 20**.
