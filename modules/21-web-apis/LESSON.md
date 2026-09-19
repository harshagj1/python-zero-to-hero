# Module 21 — Web APIs (HTTP / REST / FastAPI)

## School-student idea

An **API** is a waiter between programs: you ask for something (request), you get a dish back (response), often as **JSON**.

**REST** is a common style of API using URLs + verbs:

| Verb | School meaning | Example |
|------|----------------|---------|
| GET | read | list items / fetch metrics |
| POST | create/submit | add item / send prompt to model |
| PUT/PATCH | update | edit a record |
| DELETE | remove | delete item |

**FastAPI** = popular Python toolkit to **build** REST APIs quickly.

## Where this shows up at work

| Role | Daily API work |
|------|----------------|
| SRE | call cloud APIs; expose `/health`; automate with HTTP |
| Observability | scrape/push metrics; query backends; event ingest APIs |
| AI Engineer | call model endpoints; wrap models in your own FastAPI |
| Enterprise | microservice CRUD; webhooks; integrations |

## Client vs server (both matter)

- **Client** (`api_client_demo.py`): *you call someone else’s API*  
- **Server** (`fastapi_sketch.py`): *others call yours*

## Pro habits (memorize)

- Always set **timeouts**
- Check failures (`raise_for_status` / status codes)
- Validate JSON shapes (`.get`, Pydantic)
- Never commit API keys — use environment variables

## Exercises

1. GET httpbin and print status code.  
2. POST a small JSON payload and inspect the echo.  
3. Run the FastAPI sketch; hit `/health` and `/docs`.  
4. Role stretch:  
   - SRE: script that fails (exit 1) if `/health` is not ok  
   - Obs: POST a fake log event JSON to a local FastAPI receiver  
   - AI: design `POST /v1/summarize` body with `text: str`

## Next

Run both demos when ready, then **Module 22** (databases behind APIs).
