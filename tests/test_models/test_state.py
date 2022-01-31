#!/usr/bin/python3
""" Unit tests class state"""

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
from models.state import State


class TestState(unittest.TestCase):
    """Tests for State class"""

    def setUp(self):
        """Set up class method"""
        self.state = State()
        self.state.name = "Hawaii"

    def test_type_args(self):
        """Test attribute type"""
        self.assertEqual(type(self.state.name), str)

    def test_attr(self):
        """Test attribute"""
        self.assertEqual(self.state.name, "Hawaii")

    def test_basemode_attributes(self):
        """Test attributes of BaseModel"""
        self.assertIsNotNone(self.state.id)
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)

    def test_subclass_state(self):
        """Test State is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))


if __name__ == '__main__':
    unittest.main()
