# Problem-Solving and Debugging: Dictionaries

# Example: Common mistake - KeyError when accessing non-existent key

student_grades = {"Alice": 85, "Bob": 90}

# Uncommenting the next line will cause KeyError if key does not exist:
# print(student_grades["Charlie"])  # KeyError

# Fix: Use .get() with default value to avoid error
print(student_grades.get("Charlie", "No grade found"))

# Correct usage:
print("Alice's grade:", student_grades["Alice"])
