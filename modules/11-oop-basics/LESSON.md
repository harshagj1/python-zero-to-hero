# Module 11 — OOP Basics

## School-student idea

A **class** is a blueprint. An **object** is one real thing built from it.  
Methods are buttons; attributes are settings.

## Where this shows up at work

| Role | Classes you will meet / write |
|------|-------------------------------|
| SRE | `HttpChecker`, `KubeClient`, `RunbookStep` |
| Observability | `MetricExporter`, `LogParser`, `TraceBatch` |
| AI | `Chunker`, `Embedder`, `ModelClient`, `Pipeline` |
| FastAPI / enterprise | `User`, `Order`, Pydantic `BaseModel`, service classes |

## Why OOP in enterprise systems

- Keeps **data + rules** together (balance + deposit rules)  
- Stable interfaces while internals change  
- Easy to test with fake/mock collaborators  

## Exercises

1. `Service(name, url)` with method `label()`.  
2. `HealthCheck` with `ok: bool` and `as_dict()` for JSON.  
3. Reject empty service name in `__init__`.  

## Next

Run `oop_basics_demo.py`, then **Module 12**.
