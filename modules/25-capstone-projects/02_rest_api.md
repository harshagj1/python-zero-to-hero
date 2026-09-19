# Capstone 2 — REST API + SQLite

## Goal

Build a small FastAPI service for notes or expenses with SQLite persistence.

## Skills proven

HTTP APIs, pydantic models, SQLite, testing, project layout, uvicorn

## Requirements

- Endpoints:
  - `GET /health`
  - `GET /items`
  - `POST /items`
  - `GET /items/{id}`
  - `DELETE /items/{id}`
- Validate input (empty titles rejected)
- Persist in SQLite
- Return proper status codes (404 when missing)
- Tests using FastAPI `TestClient`

## Stretch

- Pagination
- Filtering query params
- Simple API key header auth
- Dockerize

## Acceptance checklist

- [ ] API runs with uvicorn
- [ ] Data survives restart
- [ ] Tests pass
- [ ] README includes example `curl` commands
