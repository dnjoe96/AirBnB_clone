#!/usr/bin/python3
"""Unit test for Basemodel"""

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



class TestBaseModel(unittest.TestCase):

    """Tests for BaseModel class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}

        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init_function(self):
        pass

    def test_creating_object(self):
        """Test the object is correctly created"""

        pass

    def test_unique_uuid(self):
        """Test uuid is unique"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_id_is_string(self):
        """Test id is string"""
        obj = BaseModel()
        self.assertTrue(type(obj.id), str)

    def test_init_no_args(self):
        """Test init function has no args"""
        pass

    def test_attriutes(self):
        obj = BaseModel()
        obj.name = "Name"
        obj.number = 11

        self.assertEqual(obj.name, "Name")
        self.assertEqual(obj.number, 11)

    def test_date_time(self):
        """Test created at and updated are datetime"""
        obj = BaseModel()
        self.assertTrue(type(obj.created_at), datetime)
        self.assertTrue(type(obj.updated_at), datetime)

    def test_to_dict(self):
        """Test the method to_dict()"""
        obj = BaseModel()
        dic = obj.to_dict()

        self.assertEqual(dic["created_at"], obj.created_at)
        self.assertEqual(dic["updated_at"], obj.updated_at)
        self.assertEqual(dic["__class__"], type(obj).__name__)

    def test_to_dict_returns_dict(self):
        """Test to_dict() returns a dictionary"""
        obj = BaseModel()
        self.assertTrue(type(obj.to_dict), dict)

    def test_str(self):
        """Test str() returns a string"""
        obj = BaseModel()
        string = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))


    def test_save(self):
        """Test save() that updates created/updated at
        and calles strorage"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        old_created_at = obj.created_at

        obj.save()
        new_created_at = obj.created_at
        new_updated_at = obj.updated_at

        self.assertEqual(old_created_at, new_created_at)
        self.assertNotEqual(new_created_at, new_updated_at)

if __name__ == '__main__':
    unittest.main()
