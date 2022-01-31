#!/usr/bin/python3
"""Unittest for the Console class"""

import unittest
import sys
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from io import StringIO
import re

class ConsoleTest(unittest.TestCase):
    """Test for console"""

    def setUp(self):
        """Set up methods"""
        pass

    def test_01_quit(self):
        """Test quit"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_01_EOF(self):
        """Test EOF"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
