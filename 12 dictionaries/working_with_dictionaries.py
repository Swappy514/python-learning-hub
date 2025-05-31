# Working with Dictionaries: Common methods

person = {"name": "Alice", "age": 28, "city": "Boston"}

# Get keys, values, and items
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Remove element with pop()
age = person.pop("age")
print("Removed age:", age)
print("Updated dict:", person)
