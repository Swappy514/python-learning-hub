# Industry Example: User Access Level Determination

# Given a user role and activity log, determine access permissions.

user_role = "admin"  # roles: admin, editor, viewer
activity_count = 15  # number of actions performed

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
