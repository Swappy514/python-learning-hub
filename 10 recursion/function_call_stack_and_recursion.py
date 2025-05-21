# Function Call Stack & Recursion in Python

# Example: Factorial using recursion

def factorial(n):
    if n == 0:
        return 1  # Base case to stop recursion
    else:
        return n * factorial(n - 1)  # Recursive call

num = 5
print(f"Factorial of {num} is {factorial(num)}")
