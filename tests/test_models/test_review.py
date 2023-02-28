#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review(self):
        rv = Review()
        self.assertEqual(rv.text, "")
