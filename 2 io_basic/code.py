# Industry Example: Simple User Registration Input and Output

# This simulates a registration system gathering user data.

user_name = input("Enter username: ")
user_age = input("Enter age: ")

# Convert age to integer with basic validation
try:
    user_age = int(user_age)
except ValueError:
    print("Invalid age entered. Setting age to 0.")
    user_age = 0

print("\nUser Profile:")
print("Username:", user_name)
print("Age:", user_age)
