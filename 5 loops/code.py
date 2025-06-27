# Industry Example: Processing User Inputs with Loop

# Collect usernames until 'quit' is entered

usernames = []

while True:
    user_input = input("Enter username (or 'quit' to stop): ")
    if user_input.lower() == 'quit':
        break
    usernames.append(user_input)

print("\nUsernames collected:")
for user in usernames:
    print("-", user)
