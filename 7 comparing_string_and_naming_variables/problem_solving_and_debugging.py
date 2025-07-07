# Problem-Solving and Debugging: Comparing Strings and Naming Variables

# Debug example: common mistake in string comparison

user_input = "Yes"
if user_input == "yes":
    print("User agreed.")
else:
    print("User did not agree.")  # Will execute for "Yes" due to case mismatch

# Fix by using case-insensitive comparison
if user_input.lower() == "yes":
    print("User agreed.")
else:
    print("User did not agree.")
