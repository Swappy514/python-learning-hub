# Set Operations

Common set operations include:

| Operation                | Description                      | Example                     | Result          |
| ------------------------ | -------------------------------- | --------------------------- | --------------- |
| **Union**                | All items in either or both sets | `A.union(B)`                | `{1,2,3,4,5,6}` |
| **Intersection**         | Items common to both sets        | `A.intersection(B)`         | `{3,4}`         |
| **Difference**           | Items in A but not in B          | `A.difference(B)`           | `{1,2}`         |
| **Symmetric Difference** | Items in A or B but not both     | `A.symmetric_difference(B)` | `{1,2,5,6}`     |

### Example:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B)) # {1, 2, 3, 4, 5, 6}
print(A.intersection(B)) # {3, 4}
print(A.difference(B)) # {1, 2}
print(A.symmetric_difference(B)) # {1, 2, 5, 6}

Sets are very useful for membership testing and mathematical operations involving groups of items.
