"""
AuthService.py
Handles user authentication.
- Verifies user credentials.
- Hashes passwords using secure algorithms.
- Generates JWT tokens for authenticated sessions.
"""

import hashlib
import jwt
import time
import logging
from . import config

logger = logging.getLogger(__name__)

def hash_password(password):
    """
    Hashes a password using SHA-256.
    In production, consider using bcrypt or argon2 for enhanced security.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(input_password, stored_hash):
    """
    Verifies that the input password, when hashed, matches the stored hash.
    """
    return hash_password(input_password) == stored_hash

def generate_token(user_id, role):
    """
    Generates a JWT token containing the user's ID and role.
    Uses a secret key from configuration.
    """
    payload = {
        "user_id": user_id,
        "role": role,
        "iat": int(time.time()),
        "exp": int(time.time()) + config.TOKEN_EXPIRY_SECONDS
    }
    token = jwt.encode(payload, config.JWT_SECRET, algorithm="HS256")
    return token

def authenticate_user(username, password, user_db):
    """
    Authenticates a user by verifying credentials against the user_db.
    user_db: A dictionary mapping usernames to user records (including hashed passwords).
    
    Returns:
        JWT token if successful, otherwise raises an error.
    """
    try:
        user = user_db.get(username)
        if not user:
            raise ValueError("User not found.")
        if not verify_password(password, user["password_hash"]):
            raise ValueError("Invalid password.")
        token = generate_token(user["id"], user["role"])
        logger.info(f"User {username} authenticated successfully.")
        return token
    except Exception as e:
        logger.error("Authentication error: " + str(e))
        raise e
