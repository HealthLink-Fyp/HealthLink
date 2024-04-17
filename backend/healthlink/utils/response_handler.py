from enum import Enum
import logging

from rest_framework.response import Response

logger = logging.getLogger(__name__)


rest_framework_status_codes = {
    "Successful": {
        200: "OK - Your request was successful",
        201: "Created - Your request was successful and a new resource was created",
        202: "Accepted - Your request was accepted but not yet processed",
        204: "No Content - Your request was successful but no content was returned",
    },
    "Client Error": {
        400: "Bad Request - Your request was invalid",
        401: "Unauthorized - You are not authenticated",
        403: "Forbidden - You are not allowed to access this resource",
        404: "Not Found - The resource you are looking for does not exist",
        405: "Method Not Allowed - The method you are trying to use is not allowed",
        406: "Not Acceptable - The response is not acceptable",
        409: "Conflict - There was a conflict with the current state of the resource",
        415: "Unsupported Media Type - The media type is not supported",
        422: "Unprocessable Entity - The request was well-formed but was unable to be followed due to semantic errors",
    },
    "Server Error": {
        500: "Internal Server Error - There was an error on the server",
        501: "Not Implemented - The server does not support the functionality required to fulfill the request",
        502: "Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server",
        503: "Service Unavailable - The server is not ready to handle the request",
    },
}

successful_response = rest_framework_status_codes.get("Successful")
client_error = rest_framework_status_codes.get("Client Error")
server_error = rest_framework_status_codes.get("Server Error")


class StatusCode(Enum):
    SUCCESSFUL = "Successful"
    CLIENT_ERROR = "Client Error"
    SERVER_ERROR = "Server Error"


def log_and_create_response(
    message: str, status_code: int, status_type: str
) -> Response:
    status_message = rest_framework_status_codes.get(status_type).get(status_code)
    message = {"detail": message, "message": status_message}
    if status_type == StatusCode.SUCCESSFUL.value:
        logger.info(message)
    else:
        logger.error(message)
    return Response(message, status=status_code)


def send_response(message: str, status_code: int) -> Response:
    if status_code in successful_response:
        return log_and_create_response(
            message, status_code, StatusCode.SUCCESSFUL.value
        )
    elif status_code in client_error:
        return log_and_create_response(
            message, status_code, StatusCode.CLIENT_ERROR.value
        )
    elif status_code in server_error:
        return log_and_create_response(
            message, status_code, StatusCode.SERVER_ERROR.value
        )
    else:
        return Response({"message": "An error occurred"}, status=server_error.get(500))
