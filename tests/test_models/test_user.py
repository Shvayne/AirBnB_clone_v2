#!/usr/bin/python3
"""tests for the user class model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import os


class TestUser(test_basemodel):
    """User class tests"""

    def __init__(self, *args, **kwargs):
        """initilaization..."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_first_name(self):
        """test user first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_last_name(self):
        """tests user lastname"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_email(self):
        """test user email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_password(self):
        """tets for the user password"""
        new = self.value()
        self.assertEqual(type(new.password), str)