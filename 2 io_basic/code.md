Industry Example: User Registration Input and Output
In many real-world applications, gathering user input and validating it is fundamental.

This example simulates:

Asking for a username and age.

Converting age input to an integer.

Handling invalid input with basic error checking.

Displaying the collected data.

Code:
user_name = input("Enter username: ")
user_age = input("Enter age: ")

try:
user_age = int(user_age)
except ValueError:
print("Invalid age entered. Setting age to 0.")
user_age = 0

print("Username:", user_name)
print("Age:", user_age)
Possible Output:
code
Enter username: alice
Enter age: twenty
Invalid age entered. Setting age to 0.

User Profile:
Username: alice
Age: 0
