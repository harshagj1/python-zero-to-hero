# Module 24 — Performance, Debugging, and Professional Quality

## Layman idea

Writing code that works is level 1.  
Writing code you can **fix**, **speed up**, and **operate in production** is engineer level.

## Debugging toolkit

1. **Read the traceback** bottom-up: last line is often the real failure site
2. **Reproduce** with the smallest example
3. **Print/log** strategic values (then remove noise)
4. **Debugger**: breakpoints in Cursor/VS Code
5. **Bisect**: comment half the code to find the guilty section

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("user_id=%s", user_id)
```

## Timing code

```python
import time
start = time.perf_counter()
# ... work ...
print(time.perf_counter() - start)
```

Or use `cProfile`:

```powershell
python -m cProfile -s cumtime your_script.py
```

## Common performance wins (in order)

1. Choose better algorithms / data structures (`set`/`dict` for membership)
2. Avoid repeated work (cache, precompute)
3. Batch I/O (don't open files in a tight loop)
4. Use generators for large streams
5. Only then: concurrency, Cython, etc.

**Premature optimization** wastes time — measure first.

## Code quality habits of strong engineers

- Clear names
- Small functions
- Types on public APIs
- Tests for core logic
- Logging over mystery prints
- Handle errors near the boundary (I/O, user input)
- Keep secrets out of git
- Write README for future-you

## Security basics (must know)

- Parameterized SQL
- Validate/sanitize inputs
- Don't `eval` user strings
- Use HTTPS and timeouts for HTTP
- Hash passwords properly (never store plain text)

## Exercises

1. Compare list membership vs set membership for 50k items.
2. Profile a slow function with `cProfile`.
3. Turn a noisy script into structured logging.
4. Find a quadratic loop in your own practice code and fix it.

## Next

Run `perf_debug_demo.py`, then start **Module 25 Capstones**.
