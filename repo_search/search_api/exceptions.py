from http import HTTPStatus

from flask import make_response, jsonify


class BaseError(BaseException):
    """Base Error in which all the Error of the service are placed"""

    status_code = HTTPStatus.BAD_REQUEST
    message = ""

    def __repr__(self):
        return {"status_code": self.status_code, "message": self.message}


class InternalServerError(BaseError):
    """ Generic stack error """

    def __init__(
        self,
        message: str,
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        fields: list = (),
    ):
        self.message = message
        self.status_code = status_code
        self.fields = fields

    def get_response(self):
        return make_response(
            jsonify(status="fail", message=f"{self.message}.", fields=self.fields),
            self.status_code,
        )


class ValidationError(BaseError):
    def __init__(
        self, message: str, status_code=HTTPStatus.BAD_REQUEST, fields: list = ()
    ):
        self.message = message
        self.fields = fields
        self.status_code = status_code

    def get_response(self):
        return make_response(
            jsonify(status="fail", message=f"{self.message}.", fields=self.fields),
            self.status_code,
        )


class ProviderNotValidError(BaseError):
    def __init__(self, message: str, status_code=HTTPStatus.BAD_REQUEST):
        self.message = message
        self.fields = ["provider"]
        self.status_code = status_code

    def get_response(self):
        return make_response(
            jsonify(status="fail", message=f"{self.message}.", fields=self.fields),
            self.status_code,
        )
