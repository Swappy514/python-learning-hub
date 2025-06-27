# Industry Example: Input Collection with Loops

This example mimics collecting and processing user inputs in a loop until a sentinel value ('quit') is entered.

### Code:

usernames = []

while True:
user_input = input("Enter username (or 'quit' to stop): ")
if user_input.lower() == 'quit':
break
usernames.append(user_input)

print("\nUsernames collected:")
for user in usernames:
print("-", user)

### Sample Interaction:

Enter username (or 'quit' to stop): alice
Enter username (or 'quit' to stop): bob
Enter username (or 'quit' to stop): quit

Usernames collected:

- alice

- bob

This demonstrates practical use of loops, user interaction, and list processing.
