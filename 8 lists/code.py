# Industry Example: Manage a To-Do List

tasks = ["Email client", "Write report", "Fix bug"]

# Add new task
tasks.append("Prepare presentation")

# Complete and remove first task
completed_task = tasks.pop(0)
print(f"Completed: {completed_task}")

print("Remaining tasks:")
for task in tasks:
    print("-", task)
