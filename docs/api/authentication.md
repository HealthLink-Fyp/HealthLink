# HealthLink Authentication API Documentation

This documentation outlines the usage of the Django API provided for user authentication and management.

## Endpoints

### 1. Register User

- **URL:** `/api/v1/auth/register/`
- **Method:** `POST`
- **Description:** Register a new user.

- **Request Body:**
    
    `email` (string, required): Email of the user.

    `password` (string, required): Password of the user.

    `role` (string, optional): Role of the user (Note: Only non-admin roles are allowed.)

- **Responses:**

    `200 OK`: User registered successfully.

    `400 Bad Request`: Invalid request parameters.

    `403 Forbidden`: Not allowed (for admin role).

### 2. User Login

- **URL:** `/api/v1/auth/login/`
- **Method:** `POST`
- **Description:** Log in an existing user.
- **Request Body:**

    `email` (string, required): Email of the user.

    `password` (string, required): Password of the user.

- **Responses:**

    `200 OK`: User logged in successfully.

    `400 Bad Request`: Invalid request parameters.

    `401 Unauthorized`: Invalid credentials or authentication failed.

    `404 Not Found`: User not found.

    `403 Forbidden`: Not allowed (for admin role).

### 3. User Information

- **URL:** `/api/v1/auth/user/`
- **Method:** `GET`
- **Description:** Retrieve information about the logged-in user.
- **Authentication:** JWT token required.
- **Responses:**

    `200 OK`: User information retrieved successfully.

    `401 Unauthorized`: Not authenticated.

### 4. Refresh Access Token

- **URL:** `/api/v1/auth/refresh/`
- **Method:** `POST`
- **Description:** Refresh the access token using the refresh token.
- **Request Header:**

    `Cookie`: `refresh_token` (string, required): Refresh token.

- **Responses:**

    `200 OK`: Access token refreshed successfully.

    `400 Bad Request`: Invalid refresh token.

    `401 Unauthorized`: Not authenticated.

    `404 Not Found`: User not found.

### 5. User Logout

- **URL:** `/api/v1/auth/logout/`
- **Method:** `POST`
- **Description:** Log out the user by deleting the refresh token.
- **Request Header:**

    `Cookie`: `refresh_token` (string, required): Refresh token.

- **Responses:**

    `200 OK`: User logged out successfully.

    `401 Unauthorized`: Not authenticated.

### 6. Forgot Password

- **URL:** `/api/v1/auth/forgot/`
- **Method:** `POST`
- **Description:** Send an email to the user to reset their password.
- **Request Body:**

    `email` (string, required): Email of the user.

- **Responses:**

    `200 OK`: Email sent successfully with reset instructions.

    `404 Not Found`: User not found.

### 7. Reset Password

- **URL:** `/api/v1/auth/reset/`
- **Method:** `POST`
- **Description:** Reset the user's password using the reset token.
- **Request Body:**

    `token` (string, required): Reset token received via email.

    `password` (string, required): New password for the user.

- **Responses:**

    `200 OK`: Password reset successfully.

    `400 Bad Request`: Invalid request parameters.
    
    `404 Not Found`: Invalid token or user not found.
