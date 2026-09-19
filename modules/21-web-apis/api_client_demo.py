# Module 21 — Talking to REST APIs (client side)
# pip install requests
# python api_client_demo.py
#
# SCHOOL: Your program asks a website/API for data (GET) or sends data (POST).
#         The answer is often JSON (nested dicts/lists) — exactly Module 07 skills.
# WORK:
#   SRE            → hit /health, /metrics; automation against cloud APIs
#   Observability  → pull Prometheus/Datadog/Grafana APIs; push events
#   AI Engineer    → call model HTTP endpoints; send prompts; read completions
#   Enterprise     → integrate billing, CRM, internal microservices
# FASTAPI LINK: this file is the CLIENT; fastapi_sketch.py is the SERVER.

from __future__ import annotations

import sys


def main() -> None:
    try:
        import requests
    except ImportError:
        # SCHOOL: friendly message if the library isn't installed.
        # WORK: fail fast with a clear operator message (good SRE UX).
        print("Install requests first: pip install requests")
        sys.exit(1)

    url = "https://httpbin.org/json"
    try:
        # SCHOOL: GET = "please give me data from this address."
        # WORK: always set timeout — hanging forever is an incident.
        response = requests.get(url, timeout=10)
        # SCHOOL: raise if status is 4xx/5xx so we don't pretend success.
        # WORK: surface failures to retries/alerts instead of silent bad data.
        response.raise_for_status()
    except requests.RequestException as err:
        print("Network/API error:", err)
        sys.exit(1)

    # SCHOOL: .json() turns the text body into Python dict/list.
    # WORK: every REST integration starts here — then you .get() fields safely.
    data = response.json()
    print("Status:", response.status_code)
    print("Keys:", list(data.keys()))
    print("Sample JSON:", data)

    # SCHOOL: POST = "here is some JSON for you to accept."
    # WORK: create resources; submit AI inference jobs; push metric batches.
    post = requests.post(
        "https://httpbin.org/post",
        json={"course": "zero-to-hero", "module": 21},
        timeout=10,
    )
    post.raise_for_status()
    echoed = post.json()["json"]
    print("Echoed POST body:", echoed)


if __name__ == "__main__":
    main()
