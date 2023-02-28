#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
