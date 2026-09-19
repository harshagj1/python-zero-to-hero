# Module 04 — Control Flow (if / loops)

## School-student idea

- `if` = choose a road at a fork  
- `for` / `while` = repeat a chore  

Indentation (spaces at the start of a line) shows what belongs inside the decision/loop.

## Where this shows up at work

| Role | Example |
|------|---------|
| SRE | `if status != 200: alert()`; retry `while` not ready |
| Observability | `for line in log_file: parse(line)` |
| AI | `for doc in corpus: embed(doc)` with filters |
| FastAPI | `if item is None: raise HTTPException(404)` |

## Exercises (role flavored)

1. Given `latency_ms`, print OK / WARN / CRITICAL with thresholds.  
2. Loop hosts `["api", "db", "cache"]` and print `checking {host}`.  
3. Sum numbers 1..100 (pattern for totaling metrics).  
4. Skip host `"cache"` with `continue` (known noisy target).

## Next

Run `control_flow_demo.py`, then **Module 05**.
