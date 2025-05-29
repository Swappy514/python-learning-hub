# Nested Lists & String Formatting

# Example: List of dictionaries representing students

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Access nested data and print formatted output
for student in students:
    print(f"Student: {student['name']}, Grade: {student['grade']}")
