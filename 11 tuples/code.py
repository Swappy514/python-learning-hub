# Industry Example: Managing User Roles with Sets

# Roles assigned to users (some duplicates possible)

user_roles = {"admin", "editor", "viewer", "editor"}

print("Unique user roles:", user_roles)

# Adding a new role
user_roles.add("contributor")

# Removing a role
user_roles.discard("viewer")

print("Updated roles:", user_roles)

# Check if user has a certain role
if "admin" in user_roles:
    print("User has admin access.")
