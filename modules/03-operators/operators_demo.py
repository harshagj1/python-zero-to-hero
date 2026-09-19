# Module 03 — Operators
# Run: python operators_demo.py
#
# SCHOOL: Operators are symbols that calculate or compare (+ - * / == and ...).
# WORK: Alert rules, SLO math, token billing, FastAPI validation, automation thresholds.

print("Arithmetic")
print(10 + 3)    # SCHOOL: add. WORK: total errors across pods
print(10 - 3)    # SCHOOL: subtract. WORK: remaining quota
print(10 * 3)    # SCHOOL: multiply. WORK: price * seats; tokens * cost
print(10 / 3)    # SCHOOL: divide → decimal. WORK: error_rate = errors / requests
print(10 // 3)   # SCHOOL: whole groups only. WORK: shard index, page numbers
print(10 % 3)    # SCHOOL: leftover. WORK: even/odd worker id; round-robin
print(2 ** 8)    # SCHOOL: power. WORK: backoff 2**attempt seconds (SRE retries)

print("\nEven or odd?")
number = 17
# SCHOOL: % 2 == 0 means even.
# WORK: split work across even/odd workers; sample every 2nd trace.
print(number, "is even?", number % 2 == 0)

print("\nComparisons")
score = 85
# SCHOOL: comparisons answer True/False.
# WORK: if latency_ms >= 500: page on-call; if confidence < 0.7: reject AI answer.
print("pass?", score >= 50)
print("distinction?", score >= 75)

print("\nLogic")
has_ticket = True
has_id = True
is_banned = False
# SCHOOL: and = all must be true; not = flip.
# WORK: can_deploy = tests_passed and not freeze_window
#       FastAPI: if not user.is_active: raise 403
can_enter = has_ticket and has_id and not is_banned
print("can enter?", can_enter)

print("\nNone check")
email = None
# SCHOOL: "is None" asks "is this empty on purpose?"
# WORK: if api_key is None: fail fast before calling the model/vendor API.
print("missing email?", email is None)

price = 100
discount = 0.1
tax = 0.05
# SCHOOL: parentheses make the order obvious.
# WORK: billing services; also: success_rate = (ok / total) * 100
total = (price * (1 - discount)) * (1 + tax)
print("\nTotal after discount + tax:", round(total, 2))
