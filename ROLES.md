# Who This Course Is For — Role Guides

Read this like a school student. Use it like a professional.

Every module teaches **plain Python first**, then shows how the same idea appears in real jobs:

| Role | What you build / care about |
|------|-----------------------------|
| **SRE (Site Reliability Engineer)** | Automation scripts, health checks, incident helpers, CLIs, retries, logging |
| **Observability Engineer** | Metrics/logs/traces pipelines, parsing JSON, APIs to Prometheus/Grafana/Datadog, async collectors |
| **AI Engineer** | Data cleaning, API clients to model endpoints, FastAPI services, batch jobs, typing + tests |
| **Backend / Platform** | REST APIs (FastAPI), databases, enterprise services |

You do **not** need three courses. One strong Python foundation powers all of these roles.

---

## How comments in this course are written

In every `.py` file you will see comments in this shape:

```text
# SCHOOL: ...     ← so a beginner understands the line
# WORK: ...       ← how SRE / Observability / AI / enterprise apps use the same idea
# WHY: ...        ← why we chose this approach (not a different one)
```

If a school student reads every `SCHOOL` line, they can follow the program.  
If you also read every `WORK` line, you start thinking like an engineer on the job.

---

## Role learning tracks (same modules, different emphasis)

### Track A — Aiming for SRE

Focus harder on: **04, 08, 09, 10, 17, 18, 19, 20, 21, 24** + Capstone 3 (async fetcher)

You will repeatedly practice:

- scripts that check “is the service up?”
- reading logs / JSON configs
- timeouts, retries, clear errors
- CLIs operators can run during incidents

### Track B — Aiming for Observability Engineer

Focus harder on: **05, 07, 10, 13, 17, 19, 21, 22, 24** + Capstones 2 & 3

You will repeatedly practice:

- parsing structured logs (JSON)
- aggregating counters / dicts / sets
- calling REST APIs for metrics backends
- async collection of many endpoints
- writing small FastAPI “receivers” for events

### Track C — Aiming for AI Engineer

Focus harder on: **06–08, 11–16, 18, 21, 22, 23** + Capstones 2 & 4

You will repeatedly practice:

- cleaning lists/dicts of data before models
- calling model HTTP APIs (REST)
- FastAPI wrappers around inference
- type hints + tests so pipelines don’t silently break
- packaging batch jobs and services

---

## Map: Python idea → enterprise / automation / FastAPI / REST

| Python idea | Enterprise app | Automation / SRE | FastAPI / REST | Observability | AI |
|-------------|----------------|------------------|----------------|---------------|-----|
| variables | config values | host name, threshold | request fields | metric labels | prompt params |
| if/else | business rules | alert if CPU > 90% | return 400 vs 200 | drop bad events | guardrails |
| loops | process orders | check every server | validate each item | scrape many targets | batch documents |
| functions | service methods | `check_health()` | route handlers | `emit_metric()` | `tokenize()` |
| dicts/JSON | domain objects | inventory records | request/response body | log fields | embeddings metadata |
| files | reports | cron script I/O | upload handling | export metrics | dataset files |
| exceptions | domain errors | fail loudly, exit code | HTTPException | parse errors | API timeouts |
| classes | Order, User | Client wrappers | Pydantic models | Exporter class | Pipeline stages |
| async | concurrent jobs | fan-out checks | async routes | collectors | parallel inference calls |
| tests | CI quality gate | prevent flaky runbooks | API contract tests | parser tests | eval harnesses |

---

## Suggested “job story” projects (after fundamentals)

1. **SRE:** CLI that hits `/health` on N services and prints a red/green table  
2. **Observability:** script that reads JSON logs → counts error codes → writes summary  
3. **AI:** FastAPI endpoint that accepts text → calls a model HTTP API → returns JSON  
4. **Enterprise:** expense/notes API + SQLite (Capstone 2) like a tiny internal tool

Start Module 01 either way — roles only change *what you emphasize*, not the order of learning.
