"""
test_auth_service.py
Unit tests for the AuthService and UserController modules.
Tests include:
- User registration
- Login and token generation
- Role assignment
"""

import unittest
import json
from src.AuthService import hash_password, verify_password, generate_token
from src.UserController import register_user, login_user, assign_role

# A dummy user database (for testing)
dummy_db = {}

class TestAuthService(unittest.TestCase):
    def test_hash_and_verify_password(self):
        password = "securepassword"
        hashed = hash_password(password)
        from src.AuthService import verify_password
        self.assertTrue(verify_password(password, hashed))
        self.assertFalse(verify_password("wrongpassword", hashed))

    def test_generate_token(self):
        token = generate_token("1", "admin")
        self.assertIsInstance(token, str)

class TestUserController(unittest.TestCase):
    def test_register_and_login(self):
        # Test registration
        request = {"username": "alice", "password": "alice123", "role": "analyst"}
        reg_response = json.loads(register_user(request))
        self.assertEqual(reg_response["status"], "success")
        
        # Test login
        login_req = {"username": "alice", "password": "alice123"}
        login_response = json.loads(login_user(login_req))
        self.assertIn("token", login_response)

    def test_assign_role(self):
        # First, register a user
        register_user({"username": "bob", "password": "bob123", "role": "user"})
        # Now, update the role
        assign_req = {"username": "bob", "new_role": "admin"}
        response = json.loads(assign_role(assign_req))
        self.assertEqual(response["user"]["role"], "admin")

if __name__ == '__main__':
    unittest.main()
