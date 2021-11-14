#!/usr/bin/env python

"""Tests for `cipher_hek2125` package."""


import unittest
from click.testing import CliRunner

from cipher_hek2125 import cipher_hek2125
from cipher_hek2125 import cli


class TestCipher_hek2125(unittest.TestCase):
    """Tests for `cipher_hek2125` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'cipher_hek2125.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
