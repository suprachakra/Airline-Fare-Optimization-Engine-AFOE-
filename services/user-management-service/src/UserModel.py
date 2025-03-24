"""
UserModel.py
Defines the data model for user profiles.
Contains attributes such as username, hashed password, and roles/permissions.
"""

class User:
    def __init__(self, user_id, username, password_hash, role):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        }

# Example usage:
# user = User("1", "johndoe", "hashedpassword123", "admin")
