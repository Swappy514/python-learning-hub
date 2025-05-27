# Industry Example: Student Grades Management

This example simulates managing student grades using a dictionary:

- Adding new students and grades.
- Updating existing grades.
- Iterating and printing all records.

students = {
"Alice": 85,
"Bob": 92,
"Charlie": 78
}

students["Bob"] = 95
students["David"] = 88

for student, grade in students.items():
print(f"{student}: {grade}")

### Expected Output:

Alice: 85
Bob: 95
Charlie: 78
David: 88

Dictionaries provide fast access and easy updates for such data.

---
