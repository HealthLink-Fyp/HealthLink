# Rest Framework Imports
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


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


##------------- Custom Exceptions --------------##


class CustomCommonException(APIException):
    default_detail = "Something went wrong."
    code = "custom_common_exception"
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail=None, code=None):
        self.detail = self.default_detail if detail is None else detail + self.detail
        self.code = self.code if code is None else code

        super().__init__(self.detail, self.code)


##------------- Common Exceptions --------------##


class NotFound(CustomCommonException):
    detail = " not found."
    code = "not_found"
    status_code = status.HTTP_404_NOT_FOUND


class URLKwargNotFound(CustomCommonException):
    detail = " keyword arguments not found in the URL."
    code = "url_kwarg_not_found"
    status_code = status.HTTP_400_BAD_REQUEST


class AlreadyExists(CustomCommonException):
    detail = " already exists."
    code = "already_exists"
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidData(CustomCommonException):
    detail = " invalid, make sure it's valid."
    code = "invalid_data"
    status_code = status.HTTP_400_BAD_REQUEST


##------------- User Authentication Exceptions --------------##


class InvalidToken(APIException):
    default_detail = "Your token is invalid or expired. Please login again."
    code = "invalid_token"
    status_code = status.HTTP_401_UNAUTHORIZED


class TokenExpired(APIException):
    default_detail = "Your token has expired. Please login again."
    code = "token_expired"
    status_code = status.HTTP_401_UNAUTHORIZED


class NoTokenProvided(APIException):
    default_detail = "No token provided."
    code = "no_token_provided"
    status_code = status.HTTP_401_UNAUTHORIZED


##------------- Profile Exceptions --------------##


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


class NotHealthcareProvider(APIException):
    default_detail = "You are not a healthcare provider."
    code = "not_healthcare_provider"
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


##------------- Availability Exceptions --------------##


class InvalidAvailabilityData(APIException):
    default_detail = "Invalid availability data, make sure it is a valid dictionary."
    code = "invalid_availability_data"
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidAvailabilityTime(APIException):
    default_detail = (
        "Invalid availability time, make sure start time is before end time."
    )
    code = "invalid_availability_time"
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidAvailabilityDay(APIException):
    default_detail = "Invalid availability day, make sure it is a valid list of days."
    code = "invalid_availability_day"
    status_code = status.HTTP_400_BAD_REQUEST
