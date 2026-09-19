# Module 07 — Dicts and Sets
# Run: python dicts_sets_demo.py
#
# SCHOOL: dict = labeled drawers (key → value). set = bag of unique things.
# WORK: JSON request/response bodies ARE dicts. Labels on metrics are dicts.
#       Sets = unique failing hosts, unique user ids, vocabulary tokens.

person = {
    "name": "Ada",
    "age": 36,
    "skills": ["python", "math", "writing"],
}
# SCHOOL: person["name"] opens the drawer labeled name.
# WORK: payload["model"]; log_record["level"]; span["trace_id"]
print(person["name"])

# SCHOOL: .get avoids crashing if the key is missing — returns default instead.
# WORK: Essential for REST/JSON — clients omit fields. Observability parsers must be safe.
print(person.get("email", "no email yet"))

person["email"] = "ada@example.com"  # SCHOOL: add/update a drawer
person["age"] += 1
print(person)

print("\nLoop items:")
# SCHOOL: loop key and value together.
# WORK: for label, value in metric_labels.items(): ...
for key, value in person.items():
    print(f"  {key}: {value}")

# SCHOOL: dicts inside dicts/lists — nested like real JSON from APIs.
# WORK: Kubernetes API objects; OpenAI-style responses; Grafana datasource JSON.
company = {
    "name": "Analytic Engines",
    "employees": [
        {"name": "Ada", "role": "engineer"},
        {"name": "Alan", "role": "researcher"},
    ],
}
print("\nFirst employee role:", company["employees"][0]["role"])

python_devs = {"Ada", "Guido", "Alice"}
ml_devs = {"Ada", "Andrew", "Alice"}
# SCHOOL: & shared, - only left, | everyone.
# WORK: hosts_down & pageable; new_errors - known_noise; union of scrape targets.
print("\nboth python and ml:", python_devs & ml_devs)
print("python only:", python_devs - ml_devs)
print("all:", python_devs | ml_devs)

nums = [1, 2, 2, 3, 3, 3, 4]
# SCHOOL: set drops duplicates.
# WORK: unique trace ids in a window; unique failing endpoints for an alert.
print("unique sorted:", sorted(set(nums)))
