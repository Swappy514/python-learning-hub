# Approach for Hollow Pattern

This example creates a hollow square using nested loops.

- Outer loop runs through each row.
- Inner loop runs through each column.
- Stars (`*`) are printed on borders; spaces inside.

size = 5

for i in range(size):
for j in range(size):
if i == 0 or i == size - 1 or j == 0 or j == size - 1:
print("\*", end=" ")
else:
print(" ", end=" ")
print()

**Output:**

-
-
-

Nested loops are useful for creating complex patterns like this.
