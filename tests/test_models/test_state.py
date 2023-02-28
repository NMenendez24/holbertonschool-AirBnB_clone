#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state(self):
        st = State()
        self.assertEqual(st.name, "")
