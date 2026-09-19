# Capstone 3 — Async Job Fetcher

## Goal

Fetch many URLs concurrently with `asyncio` + `httpx`/`aiohttp`, save results, summarize timing.

## Skills proven

asyncio, HTTP client, error handling, pathlib, logging, performance awareness

## Requirements

- Read URLs from a text file (one per line)
- Fetch concurrently with a concurrency limit (e.g. 10)
- Save each response body or status to `out/`
- Write a summary JSON: success count, fail count, total seconds
- Timeouts and clear error logs for failures
- Compare sync vs async timing in README

## Stretch

- Retry failed requests twice
- Parse HTML titles
- Progress bar

## Acceptance checklist

- [ ] Handles dead URLs without crashing
- [ ] Concurrency limit respected
- [ ] Summary file generated
- [ ] README explains sync vs async results
