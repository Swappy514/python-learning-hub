# Industry Example: Manage a To-Do List

This simple program demonstrates task management using a list:

- Adding new tasks
- Completing (removing) tasks
- Displaying remaining tasks

tasks = ["Email client", "Write report", "Fix bug"]

tasks.append("Prepare presentation")
completed_task = tasks.pop(0)
print(f"Completed: {completed_task}")

print("Remaining tasks:")
for task in tasks:
print("-", task)

### Sample Output:

Completed: Email client
Remaining tasks:
Write report
Fix bug
Prepare presentation
