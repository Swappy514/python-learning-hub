# Industry Example: Managing User Roles with Sets

In many applications, managing user permissions benefits from sets:

- Roles are unique, no duplicates.
- You can quickly add or remove roles.
- Membership checks for access control.

## Example:

roles = {"admin", "editor", "viewer", "editor"} # duplicates ignored

roles.add("contributor")
roles.discard("viewer")

if "admin" in roles:
print("User has admin access.")

**Expected Output:**

Unique user roles: {'admin', 'viewer', 'editor'}
Updated roles: {'admin', 'contributor', 'editor'}
User has admin access.

Using sets simplifies managing permissions and groups.
