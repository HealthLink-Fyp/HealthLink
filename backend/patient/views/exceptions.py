from rest_framework.exceptions import APIException
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CustomAPIException(APIException):
    def __init__(self, status_code, detail, code):
        self.status_code = status_code
        self.default_detail = detail
        self.default_code = code
        logger.error(self.default_detail)


class InvalidAppointment(APIException):
    def __init__(self):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            "Invalid appointment date and time.",
            "invalid_appointment",
        )


class PastAppointment(APIException):
    def __init__(self):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            "Cannot create appointment in the past.",
            "past_appointment",
        )


class DoctorAvailabilityNotFound(APIException):
    def __init__(self):
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            "Doctor availability not found.",
            "doctor_availability_not_found",
        )


class DoctorNotAvailable(APIException):
    def __init__(self):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            "Doctor is not available at the specified date and time.",
            "doctor_not_available",
        )
