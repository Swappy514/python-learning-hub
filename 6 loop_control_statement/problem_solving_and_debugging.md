# Problem-Solving and Debugging: Loop Control Statements

Loop control bugs often come from:

- Missing increments, causing infinite loops.
- Incorrect loop conditions.

### Example bug: Infinite Loop

count = 0
while count < 5:
print(count)

# Missing count += 1 leads to infinite loop

### Fixed:

count = 0
while count < 5:
print(count)
count += 1

Always check your loop exit conditions to avoid these issues.
