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
        self.city_1 = City()
        self.city_1.name = "London"

    def test_city_is_subclass(self):
        """Test city is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attr(self):
        """ Test attribut City class """
        self.assertEqual(self.city_1.name, "London")
        self.assertEqual(self.city_1.state_id, self.state.id)

if __name__ == "__main__":
    unittest.main()
