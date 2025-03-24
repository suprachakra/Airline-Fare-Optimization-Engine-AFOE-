"""
roles.py
Defines user roles and their permissions for Role-Based Access Control (RBAC).
Ensures consistent permission management across all services.
"""

ROLES = {
    "admin": {
        "permissions": ["create", "read", "update", "delete"]
    },
    "analyst": {
        "permissions": ["read", "update"]
    },
    "user": {
        "permissions": ["read"]
    }
}

# Example usage:
# if "update" in ROLES[user_role]["permissions"]:
#     allow_update_operation()
