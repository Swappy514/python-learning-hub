# Industry Example: Username Validation and Comparison

# Simulates checking if a username entered matches a stored username (case-insensitive)

stored_username = "AdminUser"
input_username = input("Enter your username: ")

if input_username.lower() == stored_username.lower():
    print("Welcome,", stored_username)
else:
    print("Username not recognized.")
