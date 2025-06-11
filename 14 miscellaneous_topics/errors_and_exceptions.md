# Errors and Exceptions

Exceptions are runtime errors that disrupt normal flow.

### Common Exception Types:

- `ValueError`: Wrong type or invalid value input.
- `ZeroDivisionError`: Division by zero.
- `Exception`: Base class for all exceptions.

### Handling Exceptions:

Use `try-except` blocks to catch and handle exceptions gracefully:

try:
num = int(input("Enter a number: "))
result = 10 / num
print(result)
except ValueError:
print("Invalid input.")
except ZeroDivisionError:
print("Divide by zero error.")
except Exception as e:
print("Other error:", e)
finally:
print("Finished.")

`finally` block runs regardless of exceptions, ideal for cleanup.
