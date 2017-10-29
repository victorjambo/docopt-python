import unittest
from unittest import TestCase
from src.dojo import Dojo


class TestHello(TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_instance(self):
        self.assertIsInstance(self.dojo, Dojo)

    def test_command(self):
        text = self.dojo.getText('some text')
        self.assertEqual(text, 'some text')


if __name__ == '__main__':
    unittest.main(verbosity=2)
