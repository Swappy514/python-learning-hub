# Problem-Solving and Debugging: Dictionaries

Dictionaries often cause errors like `KeyError` when you try to access keys that do not exist.

### Common Issue: Accessing non-existent key

student_grades = {"Alice": 85, "Bob": 90}
print(student_grades["Charlie"]) # Raises KeyError

### Safe Access: Using `.get()` method

print(student_grades.get("Charlie", "No grade found")) # Outputs default message instead of error

### Key Points:

- Always check if a key exists before accessing it.
- Use `.get()` method to provide a default value.
- Debug by reading error messages carefully.
