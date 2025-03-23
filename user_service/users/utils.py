

from rest_framework.views import exception_handler
from rest_framework.response import Response


def standardized_response(data=None, errors=None, status=200, extra_meta=None):
    response_format = {
        "success": errors is None,
        "data": data,
        "errors": errors or {},
        "meta": extra_meta or {}
    }
    return Response(data=response_format, status=status)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        return standardized_response(data=None, errors=response.data, status=response.status_code)
    return response
