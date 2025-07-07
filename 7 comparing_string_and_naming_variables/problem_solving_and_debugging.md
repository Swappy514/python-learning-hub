# Problem-Solving and Debugging: Comparing Strings and Naming Variables

### Bug Example: String Comparison Case Sensitivity

user_input = "Yes"
if user_input == "yes":
print("User agreed.")
else:
print("User did not agree.")

- Prints "User did not agree." because `"Yes" != "yes"`

### Fix: Use `lower()` or `upper()` for case-insensitive comparison

if user_input.lower() == "yes":
print("User agreed.")
else:
print("User did not agree.")

### Key Tips:

- Remember string comparisons are case-sensitive by default.
- Use consistent naming styles and valid variable names to avoid syntax errors.
