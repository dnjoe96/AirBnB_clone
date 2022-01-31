#!/usr/bin/python3
"""Unit test for class review"""

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
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests for class review"""

    def setUp(self):
        """Set up class method"""
        self.review = Review()
        self.review.place_id = "place_id"
        self.review.user_id = "user.id"
        self.review.text = "review"

    def test_type_arg(self):
        """Test type argument"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_review_subclass(self):
        """Test review is subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.review.id)
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)


if __name__ == '__main__':
    unittest.main()
