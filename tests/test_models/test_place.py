#!/usr/bin/python3
"""Tests for the place model"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest
import os


class TestPlace(test_basemodel):
    """Tests for an instance of the place model"""

    def __init__(self, *args, **kwargs):
        """iitialization..."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_city_id(self):
        """test the city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_user_id(self):
        """Test the user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_name(self):
        """test name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_description(self):
        """test desciptionof place model"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_number_rooms(self):
        """test the number of rooms of place mthd"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_number_bathrooms(self):
        """test the number of bathrooms method"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_max_guest(self):
        """test the maximum guests method"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_price_by_night(self):
        """Test price by night mthd"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_latitude(self):
        """test latitude method"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_longitude(self):
        """test longitude mthd"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_amenity_ids(self):
        """test amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
