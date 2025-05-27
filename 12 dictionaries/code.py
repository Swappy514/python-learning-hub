# Industry Example: Student Grades Management

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Update a grade
students["Bob"] = 95

# Add a new student
students["David"] = 88

# Print all student grades
for student, grade in students.items():
    print(f"{student}: {grade}")
