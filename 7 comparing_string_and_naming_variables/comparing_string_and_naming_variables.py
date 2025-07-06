# Comparing Strings and Naming Variables in Python

# Example 1: String comparison (case-sensitive)
str1 = "Hello"
str2 = "hello"

print("str1 == str2:", str1 == str2)  # False because case differs

# Example 2: Case-insensitive comparison
print("str1.lower() == str2.lower():", str1.lower() == str2.lower())  # True

# Example 3: Naming variables correctly
my_variable = 10
_myVariable2 = 20
variable3 = 30

print(my_variable, _myVariable2, variable3)

# Invalid variable names (commented out because they cause errors):
# 3variable = 10   # Error: can't start with number
# my variable = 5  # Error: spaces not allowed
