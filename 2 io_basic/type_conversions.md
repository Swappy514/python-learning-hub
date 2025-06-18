Type Conversions
Python provides built-in functions to change data types:

Common type conversions:
int(x): converts x to an integer (truncates floats)

float(x): converts x to a floating-point number

str(x): converts x to a string

Examples:
Code
num_str = "123"
num_int = int(num_str) # '123' -> 123

num = 456
num_str = str(num) # 456 -> '456'

price = 9.99
price_int = int(price) # 9.99 -> 9 (drops decimal part)

val = float(num_int) # 123 -> 123.0
Important notes:
Conversion must be valid or it raises an error:

Code
int("abc") # Raises ValueError
Always validate or handle exceptions when dealing with user input.
