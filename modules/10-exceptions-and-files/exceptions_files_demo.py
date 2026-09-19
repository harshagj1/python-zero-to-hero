# Module 10 — Exceptions and Files
# Run: python exceptions_files_demo.py
#
# SCHOOL: Things go wrong; programs must not explode silently.
#         Files let programs remember data after they close.
# WORK:
#   SRE → catch probe failures; write reports; non-zero exit codes
#   Observability → parse files/logs; skip corrupt lines without dying
#   AI → load datasets; save outputs; handle API/json errors
#   Enterprise/FastAPI → validate input; persist JSON; map errors to HTTP codes

import json
from pathlib import Path


def safe_int(text):
    # SCHOOL: try to turn text into a number; if it fails, return None.
    # WORK: parse env vars / form fields / log fields safely.
    try:
        return int(text)
    except ValueError:
        return None


def load_or_create(path: Path):
    # SCHOOL: if missing, create empty list JSON; if corrupt, start fresh.
    # WORK: resilient config/state loading — never crash the whole agent on one bad file.
    if not path.exists():
        path.write_text("[]", encoding="utf-8")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("Corrupt JSON — starting fresh.")
        return []


def main():
    print("safe_int('42') ->", safe_int("42"))
    print("safe_int('nope') ->", safe_int("nope"))

    notes = Path(__file__).parent / "sample_notes.txt"
    # SCHOOL: write text to disk, then read it back.
    # WORK: export runbooks output; cache; AI batch results; metric dumps.
    notes.write_text("line 1\nline 2\nline 3\n", encoding="utf-8")
    print("\nFile contents:")
    print(notes.read_text(encoding="utf-8"))

    data_path = Path(__file__).parent / "sample_data.json"
    payload = {"app": "zero-to-hero", "version": 1, "ok": True}
    # SCHOOL: JSON is the common language of APIs and config files.
    # WORK: REST bodies, model configs, Grafana dashboards, service manifests.
    data_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    loaded = json.loads(data_path.read_text(encoding="utf-8"))
    print("Loaded JSON:", loaded)

    def set_age(age):
        # SCHOOL: raise = deliberately shout when a rule breaks.
        # WORK: raise ValueError/HTTPException early — better than corrupt data later.
        if age < 0:
            raise ValueError("age cannot be negative")
        return age

    try:
        set_age(-3)
    except ValueError as err:
        print("Caught:", err)


if __name__ == "__main__":
    main()
