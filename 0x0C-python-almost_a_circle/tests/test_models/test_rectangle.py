#!/usr/bin/python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 3, 4, 6, 8)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 8)

    def test_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)
        
        r2 = Rectangle(3, 5)
        self.assertEqual(r2.area(), 15)

    def test_display(self):
        r1 = Rectangle(2, 3)
        expected_output = "##\n" + "##\n" + "##\n"
        self.assertEqual(expected_output, r1.display())

        r2 = Rectangle(3, 2, 1, 1)
        expected_output = "\n" + "\n" + " ###\n" + " ###\n"
        self.assertEqual(expected_output, r2.display())

    def test_str(self):
        r1 = Rectangle(4, 2, 1, 1, 7)
        self.assertEqual(str(r1), "[Rectangle] (7) 1/1 - 4/2")

    def test_update(self):
        r1 = Rectangle(5, 10)
        r1.update(10)
        self.assertEqual(r1.id, 10)

        r1.update(10, 20)
        self.assertEqual(r1.width, 20)

        r1.update(10, 20, 30)
        self.assertEqual(r1.height, 30)

        r1.update(10, 20, 30, 40)
        self.assertEqual(r1.x, 40)

        r1.update(10, 20, 30, 40, 50)
        self.assertEqual(r1.y, 50)

    def test_to_dictionary(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.to_dictionary(), {'id': 1, 'width': 5, 'height': 10, 'x': 0, 'y': 0})

        r2 = Rectangle(3, 2, 1, 1, 7)
        self.assertEqual(r2.to_dictionary(), {'id': 7, 'width': 3, 'height': 2, 'x': 1, 'y': 1})

if __name__ == '__main__':
    unittest.main()