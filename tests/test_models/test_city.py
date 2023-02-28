#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city(self):
        city = City()
        self.assertEqual(city.name, "")
