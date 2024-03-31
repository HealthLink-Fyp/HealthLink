# HealthLink Profile API Documentation

This documentation outlines the usage of the Django API provided for user profiles.

## Endpoints

### 1. User Profile Information (Doctor or Patient)

- **URL:** `api/v1/auth/profile/`
- **Method:** `GET`
- **Description:** Retrieve the user's profile.
- **Authentication:** `JWT token required`.
- **Permissions:** User must be authenticated.
- **Responses:**

     `200 OK`: Profile retrieved successfully.

     `404 Not Found`: User or profile not found.

     `403 Forbidden`: Not allowed.


### 2. Create User Profile (Doctor or Patient)

- **Method:** `POST`
- **Description:** Create the user's profile.
- **Authentication:** `JWT token required`.
- **Permissions:** User must be authenticated.
- **Request Body:**

     `user` (integer, required): ID of the user.


- **Profile data (varies based on user role):**
    - For doctors: See [Doctor Profile Serializer](#doctor-profile-serializer)
    - For patients: See [Patient Profile Serializer](#patient-profile-serializer)

- **Responses:**

     `201 Created`: Profile created successfully.

     `400 Bad Request`: Invalid request parameters.

     `403 Forbidden`: Not allowed.


## Serializers

### Doctor Profile Serializer

Serializer for doctor profile data.

```json
{
  "id": integer,
  "user": integer,
  "full_name": string,
  "city": string,
  "specialization": string,
  "qualification": string,
  "experience_years": integer,
  "consultation_fees": integer,
  "summary": string,
  "wait_time": integer,
  "recommendation_percent": integer,
  "patients_count": integer,
  "reviews_count": integer,
  "profile_photo_url": string,
  "created": datetime
}
```

### Patient Profile Serializer

Serializer for patient profile data.

```json
{
  "id": integer,
  "user": integer,
  "full_name": string,
  "city": string,
  "age": integer,
  "sex": boolean,
  "blood_group": string,
  "weight": integer,
  "height": integer,
  "bmi": float,
  "created": datetime
}
```

