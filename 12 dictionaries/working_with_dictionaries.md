# Working with Dictionaries

Useful dictionary methods:

- `.keys()`: Returns all keys.
- `.values()`: Returns all values.
- `.items()`: Returns key-value pairs.

### Looping through dictionary:

for key, value in person.items():
print(f"{key}: {value}")

### Removing items:

Use `.pop(key)` to remove and return a value:

age = person.pop("age")
print(age) # 28

Dictionaries are flexible and powerful for many data manipulation tasks.
