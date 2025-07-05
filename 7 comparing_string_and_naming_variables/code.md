# Industry Example: Username Validation and Comparison

This example shows a common scenario in applications:

- Accept a username input from the user
- Compare it with a stored username regardless of case

stored_username = "AdminUser"
input_username = input("Enter your username: ")

if input_username.lower() == stored_username.lower():
print("Welcome,", stored_username)
else:
print("Username not recognized.")

**Sample interaction:**

Enter your username: adminuser
Welcome, AdminUser

Case-insensitive comparison improves user experience by preventing minor input mistakes.

---
