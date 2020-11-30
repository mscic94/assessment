from unittest import TestCase

from repo_search.search_api.exceptions import ValidationError
from repo_search.search_api.validation import validate_search_repo_data


class TestValidation(TestCase):
    def test_validate_search_repo_data_correct_fields_in_payload(self):
        payload = {"provider": "gitlab", "keyword": "python", "page_no": 1}

        self.assertIsNone(validate_search_repo_data(payload=payload))

    def test_validate_search_repo_data_wrong_fields_in_payload(self):
        payload = {"providers": "gitlab", "keyword": "python"}

        with self.assertRaises(ValidationError):
            validate_search_repo_data(payload=payload)

    def test_validate_search_repo_data_wrong_datatype_in_payload(self):
        payload = {"provider": 123, "keyword": "python", "page_no": 1}

        with self.assertRaises(ValidationError):
            validate_search_repo_data(payload=payload)

    def test_validate_search_repo_data_missing_fields_in_payload(self):
        payload = {"keyword": "python", "page_no": 1}

        with self.assertRaises(ValidationError):
            validate_search_repo_data(payload=payload)

    def test_validate_search_repo_data_empty_fields_in_payload(self):
        payload = {
            "keyword": "",
            "providers": "gitlab",
            "page_no": 1
        }

        with self.assertRaises(ValidationError):
            validate_search_repo_data(payload=payload)
