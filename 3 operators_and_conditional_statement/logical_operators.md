Logical Operators
Logical operators combine or invert boolean values:

Operator Description Example Result
and True if both are True a and b True or False
or True if at least one is True a or b True or False
not Inverts True/False not a False or True

How they work:
and: Returns True only if both conditions are True.

or: Returns True if any one condition is True.

not: Reverses the truth value.

Example:
python
x = 5
y = 10
print(x < y and y < 20) # True
print(not(x > y)) # True
Logical operators are essential for complex decision making.
