# Scope and Namespaces

### Scope

- **Local scope:** Variables inside a function; accessible only within it.
- **Global scope:** Variables defined outside functions; accessible anywhere.

### Namespaces

- Namespaces keep variable names unique in different scopes.
- Python looks for variable names in local, enclosing, global, and built-in scopes (LEGB rule).

### Example:

message = "Hello, World!" # Global

def greet():
message = "Hi from inside function" # Local
print(message)

greet() # Output: Hi from inside function
print(message) # Output: Hello, World!

def change_global():
global message
message = "Changed globally!"

change_global()
print(message) # Output: Changed globally!

Understanding scope avoids bugs caused by variable shadowing.
