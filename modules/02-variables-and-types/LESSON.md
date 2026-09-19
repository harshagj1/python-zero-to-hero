# Module 02 — Variables and Types

## School-student idea

A **variable** is a jar with a label. You put something inside and use the label later.

## Where this shows up at work

| Role | Example variables |
|------|-------------------|
| SRE | `hostname`, `max_retries`, `dry_run` |
| Observability | `metric_name`, `label_map`, `scrape_interval_sec` |
| AI Engineer | `model_id`, `temperature`, `max_tokens` |
| FastAPI / REST | `user_id`, `payload`, `status_code` |
| Enterprise app | `order_total`, `customer_email`, `is_active` |

## Core types

| Type | School meaning | Work example |
|------|----------------|--------------|
| `str` | text | API path `"/health"` |
| `int` | whole number | HTTP `504`, retry `3` |
| `float` | decimal | latency `0.243` seconds |
| `bool` | yes/no | `is_healthy = True` |
| `None` | missing | no optional field yet |

## Assignment is updating the jar

```python
error_count = 0
error_count = error_count + 1  # one more failed scrape
error_count += 1               # same idea, shorter
```

## Casting (why pros obsess over this)

REST and env vars give **strings**. Convert before math:

```python
timeout = int("30")
threshold = float("0.95")
```

## Exercises (role flavored)

1. Create variables for a service: name, port, is_healthy, version.
2. Convert `"500"` to int and check if it means "server error" (>= 500).
3. Set `api_key = None` and print whether it is missing (`is None`).
4. Print an f-string alert: `f"service={name} healthy={is_healthy}"`.

## Next

Run `variables_demo.py` (read every SCHOOL/WORK comment), then **Module 03**.
