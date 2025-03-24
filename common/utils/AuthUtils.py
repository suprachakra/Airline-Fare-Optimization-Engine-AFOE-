"""
AuthUtils.py
Common Authentication and Authorization Utilities

Provides functions to:
- Verify JWT tokens.
- Check permissions based on user roles.
- Perform other common authentication-related tasks.
"""

import jwt
import os
from datetime import datetime

# Securely load secret key from environment variables (in production, use secret management)
JWT_SECRET = os.getenv("JWT_SECRET", "default_secret_key")

def verify_token(token):
    """
    Verifies a JWT token and returns its decoded payload.
    Raises an exception if verification fails.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired.")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token.")

def check_permission(user_payload, required_role):
    """
    Checks whether the user (from the token payload) has the required role.
    Raises an exception if the permission is insufficient.
    """
    user_role = user_payload.get("role")
    if user_role != required_role:
        raise Exception(f"Insufficient permissions. Required role: {required_role}.")
    return True

# Example usage:
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
# payload = verify_token(token)
# check_permission(payload, "admin")
