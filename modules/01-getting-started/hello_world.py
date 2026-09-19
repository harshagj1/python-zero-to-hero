# Module 01 — Hello World
# Run: python hello_world.py
#
# SCHOOL: This is your first tiny program. You write instructions; Python runs them top to bottom.
# WORK: Every big system starts with a small script — SRE health pings, AI smoke tests,
#       FastAPI "hello" routes, automation that prints "job started".
# WHY THIS FILE: Train the loop write → run → see output. That loop is how pros debug forever.

# SCHOOL: Lines starting with # are notes for humans. Python skips them.
# WORK: In enterprise code, comments explain INTENT (why), not noise (what is obvious).
# WHY: Future-you (or a teammate on-call at 2am) needs the reason, not a novel.

# SCHOOL: print() shows text on the screen so you can see what happened.
# WORK: Early learning uses print; later SRE/Obs/AI use logging.info() the same way —
#       "tell me the program is alive." FastAPI still prints/logs on startup.
print("Hello, World!")

# SCHOOL: Second message = second line on screen.
# WORK: Real tools show a short banner: service name, version, environment (prod/stage).
print("Welcome to Python Zero to Hero.")

# SCHOOL: Commas let print show several pieces with spaces between them.
# WORK: Operators print "host=api-1 status=up" style lines during automation runs.
print("My name is", "Student")

# SCHOOL: 2 + 2 is math. No quotes → numbers, not letters.
# WORK: Scripts calculate error rates, latency totals, token counts, invoice sums.
print(2 + 2)

# SCHOOL: Mix a label with a calculation so the answer makes sense to a human.
# WORK: Dashboards and CLI tools never show a bare "4" — they show "retry_count=4".
print("2 + 2 =", 2 + 2)
