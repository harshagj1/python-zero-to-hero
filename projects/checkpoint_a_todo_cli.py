# Checkpoint A — Mini Todo CLI  (training wheels for real operator tools)
# Run from python-zero-to-hero folder:
#   python projects/checkpoint_a_todo_cli.py
#
# SCHOOL: A menu program that stores tasks in a list while it runs.
# WORK: Same shape as SRE CLIs and internal admin tools:
#       show menu → read input → call a function → loop until quit.
#       Later: swap "tasks" for "services to restart" or "silence alert windows".
# FASTAPI LINK: each menu action ≈ an API endpoint (add/list/delete).

def show_menu():
    # SCHOOL: tell the human what keys do what.
    # WORK: argparse/click help text for automation CLIs does the same job.
    print("\n=== TODO LIST ===")
    print("1) Add task")
    print("2) View tasks")
    print("3) Mark done (remove)")
    print("4) Quit")


def add_task(tasks):
    # SCHOOL: ask the user, clean spaces, append if not empty.
    # WORK: validate input at the edge (empty ticket id, blank host name).
    task = input("New task: ").strip()
    if task:
        tasks.append(task)
        print("Added.")
    else:
        print("Empty task ignored.")


def view_tasks(tasks):
    # SCHOOL: if nothing there, say so; else number each line.
    # WORK: empty-state messaging in CLIs/APIs prevents "is it broken?" confusion.
    if not tasks:
        print("(no tasks yet)")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task(tasks):
    # SCHOOL: show list, ask for a number, remove that item safely.
    # WORK: delete-by-id patterns in REST (DELETE /items/{id}) need the same checks.
    view_tasks(tasks)
    if not tasks:
        return
    raw = input("Number to remove: ").strip()
    if not raw.isdigit():
        print("Please enter a number.")
        return
    idx = int(raw) - 1  # SCHOOL: humans count from 1; lists from 0
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"Removed: {removed}")
    else:
        print("Invalid number.")


def main():
    # SCHOOL: tasks list lives here for the whole session (memory only).
    # WORK: later persist to JSON/SQLite (Module 10/22) like real tools.
    tasks = []
    while True:
        show_menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Bye!")
            break
        else:
            # SCHOOL: unknown input should not crash — say so and continue.
            # WORK: same as HTTP 400 Bad Request instead of a 500 stack trace.
            print("Unknown option.")


if __name__ == "__main__":
    main()
