from http import HTTPStatus
from flask import current_app as app

""""
Helper method to display JSON responses.
"""


class Response:
    success_message = "success"

    def successful_response(self, data=None, page_no=1):
        response = {"body": {"message": self.success_message}, "code": HTTPStatus.OK}

        if data:
            response["body"]["data"] = data
            response["body"]["current_page"] = str(page_no)
            response["body"]["per_page"] = str(app.config["PER_PAGE"])

        return response
