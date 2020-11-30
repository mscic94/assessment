from flask import current_app as app

from repo_search.search_api.providers.GitlabSearchRepo import GitlabSearchRepo
from repo_search.search_api.exceptions import ProviderNotValidError

"""
    The controller class holds all the logic that a specific endpoint should expect
"""


class Controller:
    def __init__(self, response):
        # passing the response to have consistency when returning responses
        self.response = response

    def search_repos(self, provider: str, keyword: str, current_page: int = 1):
        """
        This will read the provider from the request's payload, and if the provider is valid it redirects to the correct
        provider search

        return: JSON response with a list of repositories found
        """
        projects = []

        if provider not in app.config["ACCEPTED_PROVIDERS"]:
            raise ProviderNotValidError(
                message=f"Invalid provider. Please choose from: {app.config['ACCEPTED_PROVIDERS']}"
            )

        if provider == "gitlab":
            projects = GitlabSearchRepo().get_repositories_by_keyword(
                keyword=keyword, current_page=current_page
            )

        return self.response.successful_response(data=projects, page_no=current_page)
