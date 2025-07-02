# Loop Control Statements

Python provides statements to control the flow inside loops.

- **break:** Exit the loop immediately.
- **continue:** Skip the rest of the current iteration and move to the next.
- **pass:** Do nothing (used as a placeholder).

### Example:

for i in range(1, 6):
if i == 3:
continue # Skip printing 3
if i == 5:
break # Exit loop at 5
print(i)

**Output:**

1
2
Skipping 3
4
Breaking at 5

The `else` after a loop executes only if the loop completes without hitting a `break`.

### pass statement

Used when syntax requires a statement but no action is needed.

for i in range(3):
pass
undefined
