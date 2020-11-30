from unittest import TestCase

from repo_search.search_api.response import Response
from repo_search import app


class TestResponse(TestCase):
    def test_successful_response_with_empty_data(self):
        response = Response()
        result = response.successful_response()

        self.assertEqual(200, result.get("code"))
        self.assertEqual("success", result.get("body").get("message"))
        self.assertEqual(1, len(result.get("body")))

    def test_successful_response_with_data_should_return_valid_dict(self):
        current_app = app()
        current_app.config["PER_PAGE"] = 10

        with current_app.app_context():
            response = Response()
            result = response.successful_response(data={"provider": "gitlab"})

            self.assertEqual(200, result.get("code"))
            self.assertEqual("success", result.get("body").get("message"))
            self.assertTrue("data" in result.get("body").keys())
            self.assertEqual(4, len(result.get("body")))
            self.assertEqual("gitlab", result.get("body").get("data").get("provider"))
