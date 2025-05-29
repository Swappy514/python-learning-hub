# Nested Lists & String Formatting

## Example: List of dictionaries

You may encounter data structures like lists containing dictionaries:

students = [
{"name": "Alice", "grade": 85},
{"name": "Bob", "grade": 92},
{"name": "Charlie", "grade": 78}
]

### Accessing and displaying data with string formatting:

for student in students:
print(f"Student: {student['name']}, Grade: {student['grade']}")

### Output:

Student: Alice, Grade: 85
Student: Bob, Grade: 92
Student: Charlie, Grade: 78

Such structures are common in datasets and APIs.
