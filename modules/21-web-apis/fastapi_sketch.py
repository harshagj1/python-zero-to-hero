# Module 21 — Minimal FastAPI server (enterprise-shaped hello service)
# pip install fastapi uvicorn
# uvicorn fastapi_sketch:app --reload
# Then open: http://127.0.0.1:8000/health
# Docs UI:   http://127.0.0.1:8000/docs
#
# SCHOOL: FastAPI lets you turn Python functions into a website API.
#         Browser/other programs call URLs; your functions return JSON.
# WORK:
#   AI Engineer     → /v1/complete that wraps a model call
#   Observability   → /v1/events receiver for logs/metrics payloads
#   SRE             → internal control APIs; health/readiness endpoints
#   Enterprise apps → CRUD microservices (items, orders, users)

from fastapi import FastAPI
from pydantic import BaseModel

# SCHOOL: create the app object — the front door of your API.
# WORK: one app per service in microservice architectures.
app = FastAPI(title="Zero to Hero API")


class Item(BaseModel):
    """SCHOOL: describes the shape of JSON we accept (name + price).
    WORK: Pydantic validation = free request checking (enterprise must-have).
    AI: define PromptRequest(prompt: str, max_tokens: int) the same way.
    """

    name: str
    price: float


# SCHOOL: pretend database in memory (resets when server restarts).
# WORK: replace with SQLite/Postgres (Module 22) for real services.
ITEMS: list[Item] = []


@app.get("/health")
def health() -> dict[str, bool]:
    # SCHOOL: simple "I'm alive" endpoint.
    # WORK: Kubernetes/load balancers probe /health or /ready (SRE bread-and-butter).
    return {"ok": True}


@app.get("/items")
def list_items() -> list[Item]:
    # SCHOOL: return all items as JSON list.
    # WORK: GET collection endpoints; list recent incidents / datasets / jobs.
    return ITEMS


@app.post("/items")
def add_item(item: Item) -> Item:
    # SCHOOL: take JSON body → validated Item → store → return it.
    # WORK: POST create pattern used across enterprise REST APIs.
    ITEMS.append(item)
    return item
