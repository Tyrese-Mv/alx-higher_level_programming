#!/usr/bin/python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 3, 4, 6)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 6)

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        
        s2 = Square(3)
        self.assertEqual(s2.area(), 9)

    def test_display(self):
        s1 = Square(2, 1, 1)
        expected_output = "\n" + " " * 1 + "##\n" + " " * 1 + "##\n"
        self.assertEqual(expected_output, s1.display())

        s2 = Square(3, 2, 0)
        expected_output = "##\n" + "##\n" + "##\n"
        self.assertEqual(expected_output, s2.display())

    def test_str(self):
        s1 = Square(4, 2, 1, 7)
        self.assertEqual(str(s1), "[Square] (7) 2/1 - 4")

    def test_update(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(10, 20)
        self.assertEqual(s1.width, 20)
        self.assertEqual(s1.height, 20)

        s1.update(10, 20, 30)
        self.assertEqual(s1.x, 30)

        s1.update(10, 20, 30, 40)
        self.assertEqual(s1.y, 40)

    def test_to_dictionary(self):
        s1 = Square(5)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 5, 'x': 0, 'y': 0})

        s2 = Square(3, 2, 1, 7)
        self.assertEqual(s2.to_dictionary(), {'id': 7, 'size': 3, 'x': 2, 'y': 1})

if __name__ == '__main__':
    unittest.main()