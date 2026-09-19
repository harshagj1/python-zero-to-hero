# Module 02 — Variables and Types
# Run: python variables_demo.py
#
# SCHOOL: A variable is a labeled box that remembers a value (like writing a name on a jar).
# WORK: Enterprise apps, FastAPI handlers, SRE scripts, and AI pipelines all store
#       config, request data, thresholds, and model parameters in variables.
# WHY: Without variables you rewrite the same value everywhere → bugs when it changes.

# SCHOOL: "Asha" is text. Quotes mean "these are letters," not code commands.
# WORK: service_name, user_id, model_name, trace_id — almost always strings at the edge.
name = "Asha"

# SCHOOL: 28 is a whole number (int). Good for counting.
# WORK: port numbers, retry counts, HTTP status codes (200, 500), batch sizes.
age = 28

# SCHOOL: 1.65 has a decimal (float). Good for measurements.
# WORK: CPU percent, latency seconds, temperature, model confidence scores.
height_m = 1.65

# SCHOOL: True/False is a yes/no switch (bool).
# WORK: is_healthy, feature_enabled, paid, dry_run=True in automation CLIs.
likes_python = True

# SCHOOL: None means "empty on purpose / not set yet."
# WORK: optional email, missing metric, no API key loaded — use None, not fake "".
nickname = None

# SCHOOL: Print labels so a person can read the output.
# WORK: Same habit as structured logs: field=value (later: JSON logs for observability).
print("Name:", name)
print("Age:", age)
print("Height (m):", height_m)
print("Likes Python:", likes_python)
print("Nickname:", nickname)

# SCHOOL: type() tells you what kind of thing is in the box.
# WORK: Huge class of production bugs = treating JSON text "42" like a number.
#       AI pipelines and REST APIs break when types are wrong. Check early.
print("--- types ---")
print(type(name))          # str
print(type(age))           # int
print(type(height_m))      # float
print(type(likes_python))  # bool
print(type(nickname))      # NoneType

# SCHOOL: Update the box: take old age, add 1, store again.
# WORK: counters (requests_served += 1), circuit-breaker state, epoch ticks in collectors.
age = age + 1
print("Next birthday age:", age)

# SCHOOL: "10" looks like a number but is still TEXT until you convert it.
# WORK: Environment variables, CSV cells, HTTP query params arrive as strings.
#       SRE scripts: int(os.environ["TIMEOUT_SECONDS"]). AI: int(batch_size_text).
years_text = "10"
years = int(years_text)  # WHY int(): unlocks real math / comparisons
print("Years as number + 5 =", years + 5)

# SCHOOL: f-string builds a readable sentence from variables.
# WORK: Alert messages, Slack/PagerDuty text, FastAPI error detail, prompt templates.
print(f"{name} is {age} years old and {height_m}m tall.")
