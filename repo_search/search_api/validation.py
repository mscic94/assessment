from functools import wraps
from http import HTTPStatus

from flask import request, make_response, jsonify

from repo_search.search_api.exceptions import ValidationError


"""
    Validation methods to check the requests payload based on project logic.
"""


def validate_search_repo_data(payload, **kwargs):
    keys = {
        "provider",
        "keyword",
        "page_no",
    }

    key_types = {
        "provider": str,
        "keyword": str,
        "page_no": int,
    }
    validate_data_keys(payload, keys)
    validate_content_keys(payload, keys)
    validate_data_types(payload, key_types)


"""
    Validation helper methods to check the payload data.
"""


def validate_data_keys(data: dict, keys: set):
    if not data:
        raise ValidationError(message="Data not found", fields=list(keys))

    # Check if all the data is present
    if not keys.issubset(data.keys()):
        raise ValidationError(
            message="Missing fields", fields=list(keys - set(data.keys()))
        )


def validate_content_keys(data: dict, keys: set):
    if not data:
        raise ValidationError(message="Data not found", fields=list(keys))

    # Check that all keys are not empty
    for key in keys:
        value = data.get(key)
        if value is None or value == "":
            raise ValidationError(message="Field empty", fields=[key])


def validate_data_types(data: dict, validation_format: dict):
    if not data:
        raise ValidationError(message="Data not found", fields=list(validation_format))

    # Check if all keys has the correct datatype
    for key, expected_type in validation_format.items():
        if key in data:
            value = data.get(key)
            if type(value) is not expected_type:
                raise ValidationError(
                    message=f"Wrong data type. Expected {expected_type.__name__}",
                    fields=[key],
                )


"""
    Validation helpers in charge of running the specific validation.py function for each endpoint and raising the 
    correct error in case validation.py fails.
"""


def validate(validation_function):
    def decorator(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            try:
                payload = request.json
                query_params = request.args
                view_args = request.view_args or {}
                validation_function(
                    payload=payload, query_params=query_params, **view_args
                )
            except ValidationError as e:
                return make_response(
                    jsonify(status=e.message, fields=e.fields),
                    HTTPStatus.BAD_REQUEST,
                )

            response = view(*args, **kwargs)
            return response

        return wrapper

    return decorator
