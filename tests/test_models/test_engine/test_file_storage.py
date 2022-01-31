#!/usr/bin/python3
"""Module tests for FileStorage class"""
import unittest
import json
import os
import uuid
import os
import time
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Sets up test methods"""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass

    def test_class_attributes(self):
        """Test attributes of FileStorage"""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_private_class_attribute(self):
        """Test private attributes of FileStorage"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_all_method(self):
        """Test all()"""
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)

        dictionary = storage.all()
        self.assertEqual(type(dictionary), dict)
        self.assertFalse(dictionary == {})
        self.assertTrue("BaseModel.{}".format(obj1.id) in dictionary)
        self.assertTrue("BaseModel.{}".format(obj2.id) in dictionary)
        self.assertTrue("BaseModel.{}".format(obj3.id) in dictionary)

    def test_new_method(self):
        """Test new()"""
        pass


if __name__ == "__main__":
    unittest.main()
