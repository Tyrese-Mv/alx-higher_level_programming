#!/usr/bin/python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), [])
        self.assertEqual(Base.to_json_string(None), [])
        self.assertEqual(Base.to_json_string([{"key": "value"}]), '[{"key": "value"}]')
    
    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')
        os.remove("Rectangle.json")

        s1 = Square(10, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 3, "size": 10, "x": 2, "y": 8}, {"id": 4, "size": 2, "x": 0, "y": 0}]')
        os.remove("Square.json")

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[{"key": "value"}]'), [{"key": "value"}])

    def test_create(self):
        r1 = Rectangle.create(**{"id": 89})
        self.assertEqual(r1.id, 89)
        r2 = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 1)
        r3 = Rectangle.create(**{"id": 89, "width": 1, "height": 3})
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 3)

        s1 = Square.create(**{"id": 89})
        self.assertEqual(s1.id, 89)
        s2 = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(s2.size, 1)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[1].width, 2)
        self.assertEqual(rectangles[1].height, 4)

        s1 = Square(10, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].id, 5)
        self.assertEqual(squares[1].size, 2)
        os.remove("Rectangle.json")
        os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()