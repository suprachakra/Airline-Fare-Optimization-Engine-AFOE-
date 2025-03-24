"""
User.py
Shared User Model

This model represents basic user information used for authentication, audit logs,
and personalization across multiple services.
"""

class User:
    def __init__(self, user_id, username, email, role):
        self.user_id = user_id  # Unique identifier for the user
        self.username = username
        self.email = email
        self.role = role  # e.g., "admin", "analyst", "user"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }

# Example usage:
# user = User("1", "johndoe", "john@example.com", "admin")
# print(user.to_dict())
