#!/usr/bin/python3
"""tests for the review model"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import os


class TestReview(test_basemodel):
    """set up test review class"""

    def __init__(self, *args, **kwargs):
        """intitialization..."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_place_id(self):
        """test place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_user_id(self):
        """test uID"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_text(self):
        """test test method"""
        new = self.value()
        self.assertEqual(type(new.text), str)