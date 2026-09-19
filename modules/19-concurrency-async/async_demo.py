# Module 19 — Async demo (fan-out like real collectors)
# Run: python async_demo.py
#
# SCHOOL: async lets one program juggle many waiting tasks (network/sleep)
#         without standing idle doing nothing.
# WORK:
#   SRE / Observability → check or scrape many endpoints concurrently
#   AI Engineer         → parallel model/tool calls (with limits)
#   Enterprise          → fan-out to many microservices, then gather results

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


async def boil(name: str, seconds: float) -> str:
    # SCHOOL: await sleep = "wait without blocking the whole program."
    # WORK: await client.get(url) while other requests continue (async HTTP).
    print(f"start {name}")
    await asyncio.sleep(seconds)
    print(f"end {name}")
    return name


async def async_main() -> None:
    start = time.perf_counter()
    # SCHOOL: gather runs these waits together — total time ≈ slowest, not sum.
    # WORK: collect() many targets; gather health of all regions.
    await asyncio.gather(
        boil("pasta", 0.3),
        boil("sauce", 0.2),
        boil("garlic", 0.1),
    )
    print(f"async total: {time.perf_counter() - start:.2f}s")


def fake_download(n: int) -> str:
    # SCHOOL: time.sleep blocks THIS thread (pretend slow download).
    # WORK: older libraries that aren't async — wrap with threads.
    time.sleep(0.2)
    return f"file-{n}"


def thread_main() -> None:
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as pool:
        print(list(pool.map(fake_download, range(3))))
    print(f"threads total: {time.perf_counter() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(async_main())
    thread_main()
