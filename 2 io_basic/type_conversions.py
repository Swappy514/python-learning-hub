# Type Conversions in Python

# Example 1: Converting string to integer
num_str = "123"
num_int = int(num_str)
print(num_int, type(num_int))  # Output: 123 <class 'int'>

# Example 2: Converting integer to string
num = 456
num_str = str(num)
print(num_str, type(num_str))  # Output: '456' <class 'str'>

# Example 3: Converting float to integer (truncates decimal)
price = 9.99
price_int = int(price)
print(price_int)  # Output: 9

# Example 4: Converting between different numeric types
val = float(num_int)  # Converts int to float
print(val, type(val))  # Output: 123.0 <class 'float'>
