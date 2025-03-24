## User Management Service
The User Management Service handles authentication, user registration, and role-based access control for internal users (e.g., admins, analysts). It is responsible for secure user credential management, JWT token generation, and enforcing role permissions.

### Responsibilities
- **AuthService:** Provides authentication logic including credential verification, password hashing, and token generation.
- **UserController:** Exposes API endpoints for user registration, login, and role assignment.
- **UserModel:** Defines the data model for user profiles, including username, hashed password, and roles/permissions.

### Setup and Running
- Configure using `config.yaml` (password policies, token expiration, OAuth provider settings).
- Containerize with the provided `Dockerfile`.
- Run tests using the test suite in the `tests/` directory.
