Industry Example: User Access Level Determination
This example mimics permission checks common in applications:

Different user roles get different access rights.

Additional conditions (like activity count) influence access.

Code:
python
user_role = "admin" # roles: admin, editor, viewer
activity_count = 15

if user_role == "admin":
access_level = "Full Access"
elif user_role == "editor" and activity_count > 10:
access_level = "Limited Edit Access"
elif user_role == "viewer":
access_level = "Read-Only Access"
else:
access_level = "No Access"

print(f"User Role: {user_role}")
print(f"Access Level: {access_level}")
Expected Output:
text
User Role: admin
Access Level: Full Access
This approach is commonly used in role-based access control (RBAC) systems.
