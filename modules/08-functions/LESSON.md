# Module 08 — Functions

## School-student idea

A **function** is a named mini-recipe: inputs go in, result comes out.

## Where this shows up at work

| Role | Example functions |
|------|-------------------|
| SRE | `check_health(url)`, `restart_if_needed(service)` |
| Observability | `parse_log_line(line)`, `emit_counter(name, labels)` |
| AI Engineer | `chunk_text(doc)`, `call_model(prompt)`, `postprocess(output)` |
| FastAPI | `create_item(payload)`, route functions under `@app.get` |
| Enterprise | `calculate_invoice(order)`, `apply_discount(user, cart)` |

## Why pros create functions (not giant scripts)

1. **Reuse** — call from CLI, API, and tests
2. **Testing** — assert `check_health` without starting the whole app
3. **Clarity** — the main program reads like a story of steps
4. **Change safety** — fix the rule in one place

## Return vs print

- **return** → reusable (APIs, libraries, automation frameworks)
- **print** → fine for learning; later prefer **logging**

## Exercises (role flavored)

1. Write `is_healthy(status_code)` → True if code is 200–299.
2. Write `error_rate(errors, total)` with a zero-total guard.
3. Write `build_alert(service, severity)` returning an f-string.
4. Write `clamp(value, low, high)` used for metric bounds / AI temperature.

## Next

Run `functions_demo.py`, build Checkpoint A, then **Module 09**.
