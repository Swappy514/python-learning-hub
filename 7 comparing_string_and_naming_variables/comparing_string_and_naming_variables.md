# Comparing Strings and Naming Variables

## String Comparison

- String comparison in Python is case-sensitive:
  "Hello" == "hello" # False
- To compare ignoring case, convert both strings to lowercase or uppercase:
  str1.lower() == str2.lower() # True

## Naming Variables

- Variable names:
- Must start with a letter (a-z, A-Z) or underscore (\_)
- Can contain letters, digits (0-9), and underscores
- Are case-sensitive (`myVar` and `myvar` are different)
- Cannot contain spaces or special characters
- Cannot be a Python keyword (like `if`, `for`, etc.)

### Valid examples:

my_variable = 10
\_myVariable2 = 20
variable3 = 30

### Invalid examples:

3variable = 10 # starts with a digit
my variable = 5 # contains space

Following these rules helps prevent syntax errors and improves code readability.
