# Rest Framework Imports
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status

# Python Imports
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler that converts exceptions to dictionary format, if they are instances of APIException.
    """

    response = exception_handler(exc, context)

    if response is not None and hasattr(exc, "code") and isinstance(exc, APIException):
        response.data = {
            "detail": exc.detail,
            "code": exc.code,
            "status_code": exc.status_code,
        }

    return response


##------------- Common Exceptions --------------##


class NotFound(APIException):
    default_detail = "Not found."
    code = "not_found"
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, detail=None, code=None):
        if detail is not None and code is not None:
            self.detail = detail + self.default_detail
            self.code = code

        super().__init__(self.detail, self.code)


class URLKwargNotFound(APIException):
    default_detail = " keyword arguments not found in the URL."
    code = "url_kwarg_not_found"
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail=None, code=None):
        if detail is not None and code is not None:
            self.detail = detail + self.default_detail
            self.code = code

        super().__init__(self.detail, self.code)


##------------- User Authentication Exceptions --------------##


class InvalidToken(APIException):
    default_detail = "Your token is invalid or expired. Please login again."
    code = "invalid_token"
    status_code = status.HTTP_401_UNAUTHORIZED


class TokenExpired(APIException):
    default_detail = "Your token has expired. Please login again."
    code = "token_expired"
    status_code = status.HTTP_401_UNAUTHORIZED


class UserNotFound(APIException):
    default_detail = "User not found."
    code = "user_not_found"
    status_code = status.HTTP_404_NOT_FOUND


##------------- Profile Exceptions --------------##


class ProfileAlreadyExists(APIException):
    default_detail = "Doctor or Patient profile already exists."
    code = "profile_already_exists"
    status_code = status.HTTP_403_FORBIDDEN


class ProfileNotFound(APIException):
    default_detail = "Create a patient or doctor profile to access this feature."
    code = "profile_not_found"
    status_code = status.HTTP_404_NOT_FOUND


class AdminNotAllowed(APIException):
    default_detail = "Admin actions are disabled temporarily."
    code = "admin_not_allowed"
    status_code = status.HTTP_403_FORBIDDEN


class DoctorNotAllowed(APIException):
    default_detail = "Doctors are not allowed to access this feature."
    code = "doctor_not_allowed"
    status_code = status.HTTP_403_FORBIDDEN


##------------- Appointment Exceptions --------------##


class DoctorNotAvailable(APIException):
    default_detail = "Doctor is not available on the selected date and time."
    code = "doctor_not_available"
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidAppointment(APIException):
    default_detail = "Invalid appointment or appointment not found."
    code = "invalid_appointment"
    status_code = status.HTTP_400_BAD_REQUEST


class PastAppointment(APIException):
    default_detail = "You cannot book an appointment in the past."
    code = "past_appointment"
    status_code = status.HTTP_400_BAD_REQUEST


class DoctorAvailabilityNotFound(APIException):
    default_detail = "Doctor has not set their availability."
    code = "doctor_availability_not_found"
    status_code = status.HTTP_404_NOT_FOUND


class UnableToDestroyPastAppointment(APIException):
    default_detail = "You cannot delete a past appointment."
    code = "unable_to_destroy_past_appointment"
    status_code = status.HTTP_400_BAD_REQUEST
