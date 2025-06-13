# Scope and Namespaces in Python

# Global variable
message = "Hello, World!"

def greet():
    # Local variable
    message = "Hi from inside function"
    print(message)

greet()                  # Prints local message
print(message)           # Prints global message

# Using global keyword
def change_global():
    global message
    message = "Changed globally!"

change_global()
print(message)           # Prints changed global message
