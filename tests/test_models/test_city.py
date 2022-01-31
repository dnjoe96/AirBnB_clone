#!/usr/bin/python3
"""Unit test for class city"""

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
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for class city"""

    def setUp(self):
        """ Initialization """
        self.city = City()
        self.city_2 = City()
        self.city.name = "name"
        self.city.state_id = "state id"""

    def test_city_is_subclass(self):
        """Test city is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attr(self):
        """ Test attribut City class """
        self.assertEqual(self.city.name, "name")
        self.assertEqual(self.city.state_id, "state id")

    def test_no_arg(self):
        """Test no arguments"""
        self.assertEqual(self.city_2.name, "")

    def test_type_attribute(self):
        """Test attribute type"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city_2.name), str)


if __name__ == "__main__":
    unittest.main()
