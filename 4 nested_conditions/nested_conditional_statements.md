# Nested Conditional Statements

You can place `if` (or `else`) blocks inside one another to check multiple, sequential conditions.

**Example:**  
Event entry depends on age and ticket possession.

age = 17
has_ticket = True

if age >= 18:
if has_ticket:
print("Entry allowed.")
else:
print("Ticket required.")
else:
if has_ticket:
print("Too young, even with ticket.")
else:
print("Too young and no ticket.")

**Output with age=17, has_ticket=True:**
Too young, even with ticket.

**Output with age=20, has_ticket=False:**
Ticket required.
undefined
