# Module 20 — Packaging, Virtual Envs, and CLIs

## Layman idea

Pros isolate project dependencies and ship clear command-line tools.

## Virtual environments (do this always)

```powershell
cd your-project
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install requests pytest
```

`requirements.txt` example:

```
requests==2.32.3
pytest==8.3.0
```

Install: `pip install -r requirements.txt`

## Project layout (sane default)

```
mytool/
  pyproject.toml   # or setup.cfg / requirements
  README.md
  src/
    mytool/
      __init__.py
      cli.py
      core.py
  tests/
    test_core.py
```

## argparse CLI

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Greeter")
    parser.add_argument("name")
    parser.add_argument("--loud", action="store_true")
    args = parser.parse_args()
    msg = f"Hello, {args.name}"
    print(msg.upper() if args.loud else msg)

if __name__ == "__main__":
    main()
```

Run: `python greeter_cli.py Ada --loud`

## pyproject.toml (modern packaging)

You'll meet build backends (`setuptools`, `hatchling`, `poetry`). Start simple; grow as needed.

## Pro checklist before sharing code

- [ ] venv + pinned dependencies
- [ ] README with run instructions
- [ ] tests
- [ ] no secrets committed
- [ ] clear entrypoint / CLI

## Exercises

1. Create a venv and install pytest.
2. Extend `greeter_cli.py` with a `--times` argument.
3. Freeze packages: `pip freeze > requirements.txt`.
4. Sketch a folder layout for a “habit tracker” app.

## Next

Run the CLI demo, then **Module 21**.
