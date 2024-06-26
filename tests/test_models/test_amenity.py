#!/usr/bin/python3
"""This module contains tests for amenity module """
from models.base_model import Basemodel
from models.amenity import Amenity
import unittest
import inspect

class TestAmenityDocs(unittest.TestCase):
    """Tests documentation and style of Amenity class"""
    @classmethod
    def setUp(cls):
        """setting up..."""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_amenity_docstrings(self):
        """Test presence of docstring in amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None, "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1, "{:s} method needs a docstring".format(func[0]))

class testAmenity(unittest.TestCase):
    """Tests for the amenity class"""
    def test_is_subClass(self):
        """Tests if amenity is a subclass of the base model"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Basemodel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_str(self):
        """Test the str method output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
