#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place()
        self.assertEqual(place.name, "")
