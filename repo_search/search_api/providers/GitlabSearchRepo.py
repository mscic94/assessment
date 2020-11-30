from gitlab import Gitlab
from flask import current_app as app

from repo_search.search_api.access_tokens import GITLAB_AT
from repo_search.search_api.exceptions import InternalServerError
from repo_search.search_api.providers.ISearchRepo import ISearchRepo


"""
    An implementation class of ISearchRepo for Gitlab integration
"""


class GitlabSearchRepo(ISearchRepo):
    def __init__(self):
        # Instantiating Gitlab server connection using a private access token
        # in order to use the Search API functionality
        self.gl = Gitlab("https://gitlab.com", private_token=GITLAB_AT)
        self.per_page = app.config["PER_PAGE"]

    def get_repositories_by_keyword(self, keyword: str = "", current_page: int = 1):
        """
        Gets all the Gitlab projects based on the specified keyword and page no
        """
        try:
            return self.gl.search(
                scope="projects",
                search=keyword,
                page=current_page,
                per_page=self.per_page,
            )
        except Exception as e:
            return InternalServerError(
                f"Something went wrong when searching for Gitlab repositories. \n {e}"
            )
