#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

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
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for class Amenity"""

    def setUp(self):
        """Set up class method"""
        self.amenity = Amenity()
        self.amenity.name = "amenity"
        self.amenity_2 = Amenity()

    def test_type_args(self):
        """Test attribute type"""
        self.assertEqual(type(self.amenity.name), str)

    def test_attribute_amenity(self):
        """Test attribute"""
        self.assertEqual(self.amenity.name, "amenity")

    def test_no_arg(self):
        """Test no argument"""
        self.assertEqual(self.amenity_2.name, "")

    def test_attr_base(self):
        """Test attribute BaseModel"""
        self.assertIsNotNone(self.amenity.id)
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)

    def test_type_attr_base(self):
        """Test type attribute BaseModel"""
        self.assertEqual(type(self.amenity.id), str)

    def test_subclass_amenity(self):
        """Test amenity is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))


if __name__ == '__main__':
    unittest.main()
