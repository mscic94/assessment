from unittest import TestCase
from unittest.mock import patch

from repo_search.search_api.controller import Controller


@patch("repo_search.search_api.response.Response")
class TestController(TestCase):
    @patch("repo_search.search_api.providers.GitlabSearchRepo.GitlabSearchRepo")
    def test_search_repo_valid_data_should_return_200(
        self, mock_response, mock_gitlab_search_repo
    ):
        from repo_search import app

        current_app = app()
        current_app.config["PER_PAGE"] = 10
        current_app.config["ACCEPTED_PROVIDERS"] = ["gitlab"]

        with current_app.app_context():
            mock_response.successful_response.return_value = {"code": 200}
            mock_gitlab_search_repo.get_repositories_by_keyword = [
                {"id": 1, "name": "python1"},
                {"id": 2, "name": "python2"},
            ]

            controller = Controller(response=mock_response)
            result = controller.search_repos(provider="gitlab", keyword="python")

            self.assertTrue(type(result) is dict)
            self.assertEqual(200, result.get("code"))

    def test_search_repo_invalid_provider_should_raise_provider_not_found_error(
        self, mock_response
    ):
        from repo_search import app

        current_app = app()
        current_app.config["PER_PAGE"] = 10
        current_app.config["ACCEPTED_PROVIDERS"] = ["gitlab"]

        with current_app.app_context():

            controller = Controller(response=mock_response)
            from repo_search.search_api.exceptions import ProviderNotValidError

            with self.assertRaises(ProviderNotValidError):
                controller.search_repos(provider="git", keyword="python")
