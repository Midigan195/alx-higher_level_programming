import os
import sys
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_base(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_id_with_arg(self):
        b1 = Base(6)
        self.assertEqual(b1.id, 6)

    def test_id_as_zero(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_id_as_negative(self):
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_id_with_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_with_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_json_string_empty_list(self):
        res = Base.to_json_string([])
        self.assertEqual(res, "[]")

    def test_json_string_list_dict(self):
        th_list = [{"id": 10,
                    "width": 5,
                    "height": 10,
                    "x": 0,
                    "y": 0
                    }]
        res = Base.to_json_string(th_list)
        expect = json.dumps(th_list)
        self.assertEqual(res, expect)

    def test_json_string_list_dict(self):
        th_list = [
                {
                    "id": 10,
                    "width": 5,
                    "height": 10,
                    "x": 0,
                    "y": 0
                },
                {
                    "id": 10,
                    "width": 5,
                    "height": 10,
                    "x": 0,
                    "y": 0
                }
        ]
        res = Base.to_json_string(th_list)
        expect = json.dumps(th_list)
        self.assertEqual(res, expect)

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_save_to_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as fle:
            self.assertEqual("[]", fle.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as fle:
            self.assertEqual("[]", fle.read())

    def test_save_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as fle:
            self.assertEqual("[]", fle.read())

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as fle:
            self.assertEqual("[]", fle.read())

    def test_from_json_string_normal(self):
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, ' \
                      '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        result = Rectangle.from_json_string(json_string)
        expected_result = [
                {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        ]
        self.assertEqual(result, expected_result)

    def test_from_json_string_empty(self):
        json_string = ''
        result = Rectangle.from_json_string(json_string)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_from_json_string_none(self):
        json_string = None
        result = Rectangle.from_json_string(json_string)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_create_with_dictionary(self):
        obj_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        obj = Rectangle.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_create_with_default_values(self):
        obj_dict = {}
        obj = Rectangle.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_create_with_partial_attributes(self):
        obj_dict = {'id': 1, 'width': 2}
        obj = Rectangle.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_create_with_dictionary_square(self):
        obj_dict = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
        obj = Square.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_create_with_default_values_square(self):
        obj_dict = {}
        obj = Square.create(**obj_dict)

        self.assertEqual(obj.id, 2)
        self.assertEqual(obj.size, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_create_with_partial_attributes_square(self):
        obj_dict = {'id': 1, 'size': 2}
        obj = Square.create(**obj_dict)

        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.size, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_load_from_file_empty(self):
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_empty_square(self):
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_with_rectangles(self):
        r1 = Rectangle(3, 5, 7, 8, 8)
        r2 = Rectangle(9, 6)
        Rectangle.save_to_file([r1, r2])

        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))

    def test_load_from_file_with_Squares(self):
        r1 = Square(3, 7, 8, 8)
        r2 = Square(9)
        Square.save_to_file([r1, r2])

        result = Square.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(str(result[0]), str(r1))
        self.assertEqual(str(result[1]), str(r2))
