How to Debug Your Code
When you write code, errors (bugs) are natural. Debugging means finding and fixing these errors.

Common error types:
Syntax errors: Mistakes in the code format. E.g., missing colons or parentheses.

Logical errors: Code runs but gives incorrect results due to wrong logic or assumptions.

Example 1: Syntax error
code
print("Hello World"

# This raises a SyntaxError because the closing parenthesis is missing.

Example 2: Logical error
code
a = 10
b = 5
result = a + b # Intended difference but addition was used!
print(result) # Prints 15 instead of expected 5
Tips to debug:
Read error messages carefully.

Use print statements to check variable values.

Use an IDE debugger or tools like pdb for step-by-step execution.
