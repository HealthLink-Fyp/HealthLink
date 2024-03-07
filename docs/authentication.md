API Endpoints
============

### Register

* **Method**: POST
* **Endpoint**: `/api/v1/register/`
* **Description**: Creates a new user account
* **Request Body**:
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

* **Response**:
```json
{
  "success": true,
  "message": "Account created successfully"
}
```

### Login

* **Method**: POST
* **Endpoint**: `/api/v1/login/`
* **Description**: Logs in an existing user
* **Request Body**:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

* **Response**:

```json
{
  "success": true,
  "message": "Logged in successfully",
  "access_token": "eyJrZXkiOiAidmFsdWUiOlt7IlJlc29sdmFsImlzcyI6Imh0dHA6Ly9zdGF0aWMuY29tL3F1ZXN0aW9ucyIsInVzZXJfaWQiOiAifQ=="
}
```

### Get User

* **Method**: GET
* **Endpoint**: `/api/v1/users/me/`
* **Description**: Retrieves the current user's information
* **Auth**: Bearer Token
* **Response**:

```json
{
  "success": true,
  "data": {
    "id": 1,
    "email": "user@example.com",
    "username": "johndoe",
    "created_at": "2023-03-15T14:30:00.000000Z"
  }
}
```
### Update User

* **Method**: PATCH
* **Endpoint**: `/api/v1/users/me/`
* **Description**: Updates the current user's information
* **Auth**: Bearer Token
* **Request Body**:
```json
{
  "email": "new-email@example.com",
  "username": "new-username"
}
```
* **Response**:
```json
{
  "success": true,
  "message": "User updated successfully"
}
```
### Delete User

* **Method**: DELETE
* **Endpoint**: `/api/v1/users/me/`
* **Description**: Deletes the current user's account
* **Auth**: Bearer Token
* **Response**:
```json
{
  "success": true,
  "message": "User deleted successfully"
}
```
### Forgot Password

* **Method**: POST
* **Endpoint**: `/api/v1/forgot/`
* **Description**: Sends a password reset link to the user's email
* **Request Body**:
```json
{
  "email": "user@example.com"
}
```
* **Response**:
```json
{
  "success": true,
  "message": "Password reset link sent successfully"
}
```
### Reset Password

* **Method**: POST
* **Endpoint**: `/api/v1/reset/`
* **Description**: Resets the user's password
* **Request Body**:
```json
{
  "token": "reset-token",
  "password": "new-password"
}
```
* **Response**:
```json
{
  "success": true,
  "message": "Password reset successfully"
}
```
### Change Password

* **Method**: PATCH
* **Endpoint**: `/api/v1/users/me/password/`
* **Description**: Changes the current user's password
* **Auth**: Bearer Token
* **Request Body**:
```json
{
  "old_password": "old-password",
  "new_password": "new-password"
}
```
* **Response**:
```json
{
  "success": true,
  "message": "Password changed successfully"
}
```