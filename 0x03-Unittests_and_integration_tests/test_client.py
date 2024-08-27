#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class methods.
"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from typing import Dict, List

import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class.
    """

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org: str, get_json_mock: MagicMock) -> None:
        """
        Test the `org` property of the GithubOrgClient class.

        Args:
            org (str): The organization name.
            get_json_mock (MagicMock): Mock object for the `get_json` function.

        Returns:
            None
        """
        git_client = GithubOrgClient(org)
        self.assertEqual(git_client.org, get_json_mock.return_value)
        get_json_mock.\
            assert_called_once_with(git_client.ORG_URL.format(org=org))

    def test_public_repos_url(self) -> None:
        """
        Test the `_public_repos_url` property of the GithubOrgClient class.

        Returns:
            None
        """
        config = \
            {"return_value.repos_url": "https://api.github.com/orgs/alx/repos"}
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock, **config
        ) as mock_org:
            test_client = GithubOrgClient("alx")
            self.assertEqual(
                test_client._public_repos_url,
                mock_org.return_value["repos_url"]
            )

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock: MagicMock) -> None:
        """
        Test the `public_repos` method of the GithubOrgClient class.

        Args:
            get_json_mock (MagicMock): Mock object for the `get_json` function.

        Returns:
            None
        """
        get_json_mock.return_value = [
            {"name": "cpp-netlib", "license": {"key": "bsl-1.0"}},
            {"name": "dagger", "license": {"key": "apache-2.0"}},
            {"name": "dot-net", "license": {"key": "bsl-1.0"}},
        ]
        prop_value = \
            {"return_value": "https://api.github.com/orgs/google/repos"}
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
            **prop_value
        ) as mock_public_repos_url:
            test_client = GithubOrgClient("google")
            self.assertEqual(
                test_client.public_repos(), ["cpp-netlib", "dagger", "dot-net"]
            )
            mock_public_repos_url.assert_called_once()
        get_json_mock.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self,
                         license: Dict,
                         key: str,
                         expected: bool) -> None:
        """
        Test the `has_license` method of the GithubOrgClient class.

        Args:
            license (Dict): Dictionary containing license information.
            key (str): License key to check.
            expected (bool): Expected result of the license check.

        Returns:
            None
        """
        self.assertEqual(GithubOrgClient.has_license(license, key), expected)


@parameterized_class(
    (
        "org_payload",
        "repos_payload",
        "expected_repos",
        "apache2_repos"
    ),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class method to start patchers.

        Returns:
            None
        """

        def response(url):
            """
            Mock response for requests.get(url).json().

            Args:
                url (str): The URL to mock the response for.

            Returns:
                MagicMock: Mocked response object.
            """
            config = {"json.return_value": []}
            for payload in TEST_PAYLOAD:
                if url == payload[0]["repos_url"]:
                    config = {"json.return_value": payload[1]}
                    break
            return MagicMock(**config)

        cls.get_patcher = patch("requests.get", side_effect=response)
        cls.org_patcher = patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
            **{"return_value": cls.org_payload}
        )
        cls.get_patcher.start()
        cls.org_patcher.start()

    def test_public_repos(self) -> None:
        """
        Test the `public_repos` method without specifying a license.

        Returns:
            None
        """
        test_client = GithubOrgClient("google/repos")
        self.assertEqual(self.expected_repos,
                         test_client.public_repos(license=None))

    def test_public_repos_with_license(self) -> None:
        """
        Test the `public_repos` method with a specified license.

        Returns:
            None
        """
        test_client = GithubOrgClient("google/repos")
        self.assertEqual(
            self.apache2_repos, test_client.public_repos(license="apache-2.0")
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tear down class method to stop patchers.

        Returns:
            None
        """
        cls.get_patcher.stop()
        cls.org_patcher.stop()
