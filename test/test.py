import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main.main import JsonChecker


checker = JsonChecker()


class TestCheckPolicyResource(unittest.TestCase):
    checker = JsonChecker()

    def test_check_policy_resource_with_asterisk(self):
        data = checker.check_policy_resource("resources/resource_with_asterisk.json")
        self.assertFalse(data)

    def test_check_policy_resource_without_asterisk(self):
        data = checker.check_policy_resource("resources/resource_without_asterisk.json")
        self.assertTrue(data)

    def test_check_policy_resource_mixed_string(self):
        data = checker.check_policy_resource("resources/resource_with_mixed_format.json")
        self.assertTrue(data)

    def test_check_policy_resource_appears_two_times(self):
        data = checker.check_policy_resource("resources/policy_file_with_2_resource_fields.json")
        self.assertFalse(data)

    def test_is_file_present(self):
        with self.assertRaises(FileNotFoundError):
            checker.check_policy_resource("resources/nonexistent_file.json")

    def test_check_if_valid_json1(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/empty_file.json")

    def test_check_if_valid_json2(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/file_is_not_dict.json")

    def test_check_if_file_is_json(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/text_file.txt")

    def test_policy_document_is_present(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/file_without_policy_document.json")

    def test_policy_document_is_dict(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_document_as_string.json")

    def test_policy_name_is_present(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/file_without_policy_name.json")

    def test_policy_name_is_string(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_name_as_int.json")

    def test_policy_name_valid_pattern(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_name_invalid_pattern.json")

    def test_if_policy_name_too_short(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_name_too_short.json")

    def test_if_policy_name_too_long(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_name_too_long.json")

    def test_statement_field_is_present(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_document_without_statement.json")

    def test_resource_field_is_present(self):
        with self.assertRaises(ValueError):
            checker.check_policy_resource("resources/policy_document_without_resource.json")
