#!/usr/bin/python3
"""Test for the city module"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
import os


class TestCity(test_basemodel):
    """set up class to test city model"""

    def __init__(self, *args, **kwargs):
        """initializing..."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test'
    )

    def test_state_id(self):
        """Test a new state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test'
    )
    def test_name(self):
        """test the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
