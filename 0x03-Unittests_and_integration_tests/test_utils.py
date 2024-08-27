#!/usr/bin/env python3
"""
Unit tests for the utils.py module.
"""

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for the access_nested_map function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str], expected: Union[int, Dict]
    ) -> None:
        """
        Test access_nested_map with valid inputs.

        Args:
            nested_map (Dict): The nested dictionary to access.
            path (Tuple[str]): The sequence of keys to access the nested value.
            expected (Union[int, Dict]):
            The expected value from the nested map.

        Returns:
            None
        """
        self.assertEqual(expected, access_nested_map(nested_map, path))

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str]
    ) -> None:
        """
        Test access_nested_map raises KeyError for invalid paths.

        Args:
            nested_map (Dict): The nested dictionary to access.
            path (Tuple[str]): The sequence of keys to access the nested value.

        Returns:
            None
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function.
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        Test get_json returns the correct JSON payload.

        Args:
            test_url (str): The URL to send the GET request to.
            test_payload (Dict[str, bool]):
            The expected JSON payload from the response.

        Returns:
            None
        """
        config = {"return_value.json.return_value": test_payload}
        with patch("requests.get", autospec=True, **config) as mockRequestGet:
            self.assertEqual(get_json(test_url), test_payload)
            mockRequestGet.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Test memoize caches the result of a method.

        Returns:
            None
        """

        class TestClass:
            """
            A test class with a method and a memoized property.
            """

            def a_method(self):
                """
                A method that returns a constant value.

                Returns:
                    int: The constant value 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that calls a_method.

                Returns:
                    int: The result of a_method.
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mockMethod:
            test = TestClass()
            self.assertEqual(test.a_property, mockMethod.return_value)
            self.assertEqual(test.a_property, mockMethod.return_value)
            mockMethod.assert_called_once()
