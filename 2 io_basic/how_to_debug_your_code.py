# How to Debug Your Code in Python

# Example 1: Simple syntax error and fix
# Uncomment the line below and see the error:
# print("Hello World"   # SyntaxError: missing closing parenthesis

# Fixed code:
print("Hello World")

# Example 2: Logical error demonstrating wrong result
a = 10
b = 5
# Intended to calculate difference, but sum is used by mistake
result = a + b  # Logical error if you wanted difference
print("Result:", result)  # Output will be 15, not 5

# Correct logical error:
correct_result = a - b
print("Correct Result:", correct_result)
