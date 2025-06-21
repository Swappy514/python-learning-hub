# Logical Operators in Python
# Used to combine multiple boolean expressions

x = 5
y = 10
z = 15

# Example 1: and operator - True if both conditions are True
print("x < y and y < z:", x < y and y < z)  # True and True => True

# Example 2: or operator - True if at least one condition is True
print("x > y or y < z:", x > y or y < z)    # False or True => True

# Example 3: not operator - negates boolean value
print("not(x < y):", not(x < y))  # not(True) => False
