# Module 06 — Lists and Tuples
# Run: python lists_tuples_demo.py
#
# SCHOOL: A list is a shopping list — ordered, changeable. A tuple is a sealed pack — fixed.
# WORK: Lists = hosts to check, documents to embed, spans in a trace.
#       Tuples = (lat, lon), (status_code, body), fixed CSV row shapes.

fruits = ["apple", "banana", "cherry"]
# SCHOOL: [0] is the first item (computers count from 0).
# WORK: targets[0] = primary region; messages[0] in a chat prompt.
print(fruits[0])

fruits[0] = "avocado"   # SCHOOL: lists can change. WORK: update queue item status in memory
fruits.append("date")   # SCHOOL: add at end. WORK: append failed_host during a probe loop
fruits.insert(1, "blueberry")  # SCHOOL: insert at position. WORK: inject canary target first
print(fruits)

removed = fruits.pop()  # SCHOOL: remove last and give it back. WORK: pop job from queue
print("removed:", removed)
print("after pop:", fruits)

ages = [25, 30, 18, 40, 22]
print("before sort:", ages)
ages.sort()  # SCHOOL: sort in place. WORK: sort latencies before computing p95
print("after sort:", ages)
print("length:", len(ages))           # WORK: queue depth metric
print("30 in ages?", 30 in ages)      # WORK: membership checks (better as set when huge)

# SCHOOL: b = a does NOT copy — both names point to the SAME list (surprise bug!).
# WORK: Mutating a shared list in async/threaded collectors corrupts metrics. Copy when needed.
a = [1, 2, 3]
b = a
c = a.copy()
b.append(99)
print("a (changed via b):", a)
print("c (independent copy):", c)

grid = [[1, 2, 3], [4, 5, 6]]
# SCHOOL: list inside list — like a table.
# WORK: batches of vectors; rows of CSV; matrix of health[region][service]
print("center-ish:", grid[1][1])

point = (4, 9)
x, y = point  # SCHOOL: unpack fixed parts into names. WORK: status, body = call_api()
print(f"point x={x}, y={y}")

rgb = (255, 200, 50)
# SCHOOL: tuples should not be edited — that stability is the feature.
# WORK: dict keys; return pairs; immutable config records.
print("rgb:", rgb)
