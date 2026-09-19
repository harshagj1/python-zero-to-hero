# Module 08 — Functions
# Run: python functions_demo.py
#
# SCHOOL: A function is a mini-recipe with a name. Write once, use many times.
# WORK: Enterprise services, FastAPI route handlers, SRE checks, AI steps —
#       all are functions (or methods) with clear inputs and outputs.

def greet(name, greeting="Hello"):
    """Build a greeting string.

    SCHOOL: return sends an answer back to the caller (better than only printing).
    WORK: FastAPI handlers return dict/JSON; SRE functions return True/False health;
          AI helpers return cleaned text. Callers decide to log, store, or respond.
    WHY default greeting: most calls share one default; override only when needed.
    """
    return f"{greeting}, {name}!"


def is_even(n):
    # SCHOOL: tiny yes/no helper so the main code reads like English.
    # WORK: prefer named checks: is_retryable(status), is_slo_breach(rate)
    return n % 2 == 0


def average(numbers):
    # SCHOOL: one place for the averaging rule.
    # WORK: average latency, mean token length, mean confidence — test this once in CI.
    if not numbers:
        # WHY guard: empty list → division by zero. Same as "no samples yet" in metrics.
        return 0
    return sum(numbers) / len(numbers)


def minmax(numbers):
    # SCHOOL: return two answers together (a tuple).
    # WORK: (p0, p100) latency bounds; (min_score, max_score) for AI eval reports.
    return min(numbers), max(numbers)


def add_item(item, bucket=None):
    # SCHOOL: add something to a list and return the list.
    # WORK: collect failing hosts; append citations; build batch payloads.
    # WHY bucket=None (not []): mutable defaults are a famous production foot-gun.
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def total(*nums):
    # SCHOOL: *nums means "accept any number of inputs."
    # WORK: flexible helpers: sum_latency(*samples); merge_tags(*tag_sets)
    return sum(nums)


print(greet("Ada"))
print(greet("Ada", greeting="Hi"))
print("42 even?", is_even(42))
print("average:", average([10, 20, 30]))

lo, hi = minmax([4, 9, 1, 7])
print(f"min={lo}, max={hi}")

print(add_item("milk"))
print(add_item("eggs"))
print("total:", total(1, 2, 3, 4))


def letter_grade(score):
    # SCHOOL: map a number to a category with clear rules.
    # WORK: map HTTP status → class; map anomaly_score → severity;
    #       map model confidence → auto-answer vs human-review (AI).
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 50:
        return "C"
    return "F"


for s in [95, 80, 60, 40]:
    print(s, "->", letter_grade(s))
