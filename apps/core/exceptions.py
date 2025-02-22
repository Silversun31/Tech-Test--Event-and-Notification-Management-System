from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    Custom error handler to return a unified format.
    """
    response = exception_handler(exc, context)

    if response is not None:
        formatted_response = {
            "status_code": response.status_code,
            "error": "Validation Error" if response.status_code == 400 else "Error",
            "message": response.data,
        }
        return Response(formatted_response, status=response.status_code)

    return Response(
        {"status_code": 500, "error": "Internal Server Error", "message": "An unexpected error occurred."},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
