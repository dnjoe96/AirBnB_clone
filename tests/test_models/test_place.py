#!/usr/bin/python3
"""Unit test for class Place"""
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
from models.place import Place
from models.amenity import Amenity

class TestClassPlace(unittest.TestCase):
    """Tests for class Place"""

    def setUp(self):
        """Set up class method"""
        self.place = Place()
        self.amenity = Amenity()
        self.place.name = "name"
        self.place.city_id = "city id"
        self.place.user_id = "user id"
        self.place.description = "description"
        self.place.number_bathrooms = 10
        self.place.max_guest = 20
        self.place.number_rooms = 100
        self.place.price_by_night = 200
        self.place.latitude = 67.8
        self.place.longitude = 200.7
        self.place.amenity_ids = [self.amenity]
        self.place_2 = Place()

    def test_type_attribute(self):
        """Test class type  attribute"""
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_no_arg(self):
        """Test no args added"""
        self.assertEqual(self.place_2.name, "")
        self.assertEqual(self.place_2.description, "")
        self.assertEqual(self.place_2.city_id, "")
        self.assertEqual(self.place_2.user_id, "")
        self.assertEqual(self.place_2.number_rooms, 0)
        self.assertEqual(self.place_2.number_bathrooms, 0)
        self.assertEqual(self.place_2.max_guest, 0)
        self.assertEqual(self.place_2.price_by_night, 0)
        self.assertEqual(self.place_2.latitude, 0.0)
        self.assertEqual(self.place_2.longitude, 0.0)
        self.assertEqual(self.place_2.amenity_ids, [])

    def test_subclass_place(self):
        """Test Place is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attr_base(self):
        """Test BaseModel attributes"""
        self.assertIsNotNone(self.place.id)
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)


if __name__ == '__main__':
    unittest.main()
