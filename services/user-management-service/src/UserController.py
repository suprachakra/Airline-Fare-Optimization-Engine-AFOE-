"""
UserController.py
Provides API endpoints for user registration, login, and role management.
"""

import json
import logging
from AuthService import authenticate_user, hash_password, generate_token

logger = logging.getLogger(__name__)

# In-memory storage for demonstration; replace with a persistent database in production.
USER_DB = {}

def register_user(request):
    """
    Registers a new user.
    Expects request to contain 'username', 'password', and 'role'.
    """
    try:
        username = request.get("username")
        password = request.get("password")
        role = request.get("role", "user")
        if not username or not password:
            raise ValueError("Username and password are required.")
        if username in USER_DB:
            raise ValueError("Username already exists.")
        user_id = str(len(USER_DB) + 1)
        USER_DB[username] = {
            "id": user_id,
            "username": username,
            "password_hash": hash_password(password),
            "role": role
        }
        logger.info(f"User {username} registered successfully.")
        return json.dumps({"status": "success", "user": USER_DB[username]})
    except Exception as e:
        logger.error("Error in register_user: " + str(e))
        return json.dumps({"error": str(e)})

def login_user(request):
    """
    Authenticates a user and returns a JWT token.
    Expects request to contain 'username' and 'password'.
    """
    try:
        username = request.get("username")
        password = request.get("password")
        if not username or not password:
            raise ValueError("Username and password are required.")
        token = authenticate_user(username, password, USER_DB)
        return json.dumps({"status": "success", "token": token})
    except Exception as e:
        logger.error("Error in login_user: " + str(e))
        return json.dumps({"error": str(e)})

def assign_role(request):
    """
    Assigns a new role to an existing user.
    Expects request to contain 'username' and 'new_role'.
    """
    try:
        username = request.get("username")
        new_role = request.get("new_role")
        if not username or not new_role:
            raise ValueError("Username and new_role are required.")
        if username not in USER_DB:
            raise ValueError("User not found.")
        USER_DB[username]["role"] = new_role
        logger.info(f"User {username} role updated to {new_role}.")
        return json.dumps({"status": "success", "user": USER_DB[username]})
    except Exception as e:
        logger.error("Error in assign_role: " + str(e))
        return json.dumps({"error": str(e)})
