#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import json
import os
import uuid
import time
import uuid
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
from models.user import User


class TestClassUser(unittest.TestCase):

    """Tests for class user"""

    def setUp(self):
        """Sets up test methods."""
        self.user_1 = User()
        self.user_1.email = "cat@gmail.com"
        self.user_1.password = "111"
        self.user_1.first_name = "first name"
        self.user_1.last_name = "last name"
        self.user_2 = User()

    def test_attribute_type(self):
        """Test type of attributes"""
        self.assertEqual(type(self.user_1.email), str)
        self.assertEqual(type(self.user_1.password), str)
        self.assertEqual(type(self.user_1.first_name), str)
        self.assertEqual(type(self.user_1.last_name), str)

    def test_user_is_subclass(self):
        """Test user is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.user_1), BaseModel))

    def test_attribute_is_attribute(self):
        """Test attributes are User class attributes"""
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def test_attribute_of_basemodel(self):
        """Test the attributes of BaseModel are not empty"""
        self.assertIsNotNone(self.user_1.id)
        self.assertIsNotNone(self.user_1.created_at)
        self.assertIsNotNone(self.user_1.updated_at)

    def test_no_arg(self):
        """ Test User class with no attribut """
        self.assertEqual(self.user_2.first_name, "")
        self.assertEqual(self.user_2.last_name, "")
        self.assertEqual(self.user_2.email, "")
        self.assertEqual(self.user_2.password, "")


if __name__ == '__main__':
    unittest.main()
