# Module 05 — Strings
# Run: python strings_demo.py
#
# SCHOOL: Strings are text. Users, files, and websites mostly speak in text.
# WORK: Log lines, metric names, REST JSON fields, prompts, Kubernetes labels — all strings.

text = "  Python Zero to Hero  "
# SCHOOL: strip() cuts extra spaces on the edges.
# WORK: Clean env vars, form fields, Slack commands before parsing.
clean = text.strip()
print(clean)
print(clean.lower())   # SCHOOL: all small. WORK: case-insensitive error_code match
print(clean.upper())   # SCHOOL: all caps. WORK: severity banners CRITICAL
print(clean.title())

word = "Python"
print("first:", word[0])       # SCHOOL: first character. WORK: parse short codes
print("slice:", word[0:3])     # SCHOOL: take a piece. WORK: truncate trace ids for UI
print("reverse:", word[::-1])

sentence = "learn python, love python"
print("count 'python':", sentence.count("python"))
# WORK: count "ERROR" in a log buffer (simple observability before full parsers)
print("replaced:", sentence.replace("python", "coding"))
# WORK: redact secrets: replace(api_key, "***") before logging (SRE safety!)

email = "ada@example.com"
# SCHOOL: split breaks text at a marker.
# WORK: split host:port; parse "key=value"; separate service.method in traces.
user, domain = email.split("@")
print("user:", user, "domain:", domain)

items = ["milk", "eggs", "bread"]
# SCHOOL: join glues a list into one string.
# WORK: ",".join(failed_hosts) for one alert line; prompt bullet lists for AI.
print("shopping:", ", ".join(items))

name = "Ada"
price = 12.5
# SCHOOL: f-string inserts values; :.2f = two decimals.
# WORK: f"latency_ms={ms:.1f}"; FastAPI detail=f"user {id} not found"
print(f"{name} paid ${price:.2f}")

code = "A42"
print("isdigit?", code.isdigit())           # WORK: validate numeric ids
print("startswith A?", code.startswith("A"))  # WORK: filter log lines / metric prefixes
