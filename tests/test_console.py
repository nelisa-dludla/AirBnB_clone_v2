#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import pep8
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test Suite for the console"""

    @classmethod
    def setUpClass(cls):
        """set up for the tests"""
        cls.console = HBNBCommand()

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def teardown(cls):
        """tear down at the end"""
        del cls.console

    def test_docstrings_in_console(self):
        """check for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_emptyline(self):
        """Test if line is empty"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()
