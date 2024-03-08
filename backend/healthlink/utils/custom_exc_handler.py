from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        data = {
            'error': True,
            'detail': response.data,
            'status': response.status_code

        }
        response.data = data
    else:
        response = Response(
            {
                'error': True,
                'detail': f'Internal Server Error {exc}',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if isinstance(exc, ValueError):
        response.status_code = status.HTTP_400_BAD_REQUEST
        response.data = {
            'error': True,
            'detail': 'ValueError',
            'status': status.HTTP_400_BAD_REQUEST
        }

    return response
