# Function Call Stack & Recursion

Recursion is a technique where a function calls itself to solve smaller instances of a problem.

### Function Call Stack

Each function call is placed on a call stack until a base case stops recursion.

### Example: Factorial Calculation

The factorial of a number n (written n!) is the product of all positive integers up to n.

- Base case: factorial(0) = 1
- Recursive case: factorial(n) = n × factorial(n-1)

def factorial(n):
if n == 0:
return 1
else:
return n \* factorial(n - 1)

print(factorial(5)) # Output: 120

Each recursive call waits for the result of the next until the base case is reached.

---
