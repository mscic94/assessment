from http import HTTPStatus

from flask import Blueprint, request, make_response, jsonify

from repo_search.search_api.controller import Controller
from repo_search.search_api.response import Response
from repo_search.search_api.validation import validate, validate_search_repo_data
from repo_search.search_api.exceptions import ProviderNotValidError

search_repo_bp = Blueprint("search_repo_api", __name__)

"""
    The Router is where all the requests will be caught. 
"""


class Router:
    def __init__(self):
        self.response = Response()
        self.controller = Controller(self.response)

    def get_repositories_based_on_keyword(self, data):
        """
        Initial method for getting a list of repositories based on keyword.
        """
        try:
            result = self.controller.search_repos(
                provider=data.get("provider"), keyword=data.get("keyword"), current_page=data.get('page_no')
            ).get("body")
            return make_response(
                jsonify(
                    message=result.get("message"),
                    current_page=result.get("current_page"),
                    per_page=result.get("per_page"),
                    data=result.get("data"),
                )
            )
        except ProviderNotValidError as e:
            return make_response(
                jsonify(status=e.message, fields=e.fields),
                HTTPStatus.BAD_REQUEST,
            )


@search_repo_bp.route("/search/repo", methods=["POST"])
# validates the payload before reaching the Router class
@validate(validate_search_repo_data)
def search_gitlab_api():
    data = request.json
    return Router().get_repositories_based_on_keyword(data=data)
