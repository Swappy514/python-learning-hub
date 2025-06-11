# Handling Errors and Exceptions in Python

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is", result)
except ValueError:
    print("That was not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution completed.")
