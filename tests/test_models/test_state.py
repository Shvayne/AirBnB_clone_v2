#!/usr/bin/python3
"""test cases for the state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import os


class TestState(test_basemodel):
    """Tests for the state model"""

    def __init__(self, *args, **kwargs):
        """initializaton..."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_name3(self):
        """Test name of states"""
        new = self.value()
        self.assertEqual(type(new.name), str)
