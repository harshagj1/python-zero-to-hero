# Module 04 — Control Flow
# Run: python control_flow_demo.py
#
# SCHOOL: if = choose a path. for/while = repeat work.
# WORK: This is the brain of runbooks, alert routers, FastAPI handlers, ETL/AI batch jobs.

score = 82
# SCHOOL: Check top band first, then next, else fail.
# WORK: Map HTTP codes → severity; map model scores → accept/review/reject.
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print(f"Score {score} => grade {grade}")

print("\nFor each fruit:")
fruits = ["apple", "banana", "cherry", "date"]
# SCHOOL: for each item in the list, do the same action.
# WORK: for host in hosts: check_health(host)
#       for doc in documents: embed(doc)   (AI batch)
#       for target in scrape_targets: collect(target)  (observability)
for fruit in fruits:
    print(f"I like {fruit}.")

print("\nRange loop:")
# SCHOOL: range(1,6) → 1,2,3,4,5.
# WORK: retry loops for i in range(max_retries); page numbers.
for i in range(1, 6):
    print("Step", i)

print("\nWhile countdown:")
count = 3
# SCHOOL: while keeps going until the condition is false.
# WORK: while not healthy and attempts < 10: sleep; recheck  (SRE wait-for-ready)
while count > 0:
    print(count)
    count -= 1  # WHY: without this, infinite loop — like a stuck cron job
print("Lift off!")

print("\nbreak / continue:")
# SCHOOL: continue = skip this round; break = leave the loop.
# WORK: continue past known-noisy hosts; break when first critical failure found.
for n in range(1, 10):
    if n == 4:
        continue
    if n == 8:
        break
    print(n)

total = 0
# SCHOOL: start at 0, add each number — classic totaling pattern.
# WORK: sum latencies, count 5xx responses, total tokens billed.
for n in range(1, 11):
    total += n
print("\nSum 1..10 =", total)
