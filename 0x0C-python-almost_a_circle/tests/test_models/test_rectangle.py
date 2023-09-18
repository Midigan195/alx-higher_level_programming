import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class Test_base(unittest.TestCase):

    def setUp(self):
        self.stdout_backup = sys.stdout
        sys.stdout = StringIO()

    def teardown(self):
        sys.stdout = self.stdout_backup

    def test_constructor(self):
        r1 = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def getter_and_setter(self):
        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.width = 3
        r2.height = 3
        r2.x = 3
        r2.y = 3
        self.assertEqual(r2.id, 10)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 3)

    def test_Rectangle_with_some_args(self):
        r3 = Rectangle(3, 3, 1, 3)
        r4 = Rectangle(3, 3, 1)
        r5 = Rectangle(3, 2)
        r3.id = 10
        r4.id = 10
        r5.id = 10
        self.assertEqual(r3.id, 10)
        self.assertEqual(r4.id, 10)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r5.id, 10)
        self.assertEqual(r5.y, 0)
        self.assertEqual(r5.x, 0)

    def test_width_non_integer(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r3 = Rectangle("r", 4, 1, 2, 50)

    def test_width_non_integer_setter(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r3 = Rectangle(3, 4, 1, 2, 50)
            r3.width = "J"

    def test_width_eqauls_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(0, 4, 1, 2, 50)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(7, 4, 1, 2, 50)
            r3.width = 0

    def test_height_eqauls_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r3 = Rectangle(9, 0, 1, 2, 50)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r3 = Rectangle(7, 4, 1, 2, 50)
            r3.height = 0

    def test_width_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(-9, 6, 1, 2, 50)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(7, 4, 1, 2, 50)
            r3.width = -6

    def test_height_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r3 = Rectangle(6, -6, 1, 2, 50)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r3 = Rectangle(7, 4, 1, 2, 50)
            r3.height = -2

    def test_x_eqauls_zero(self):
        r3 = Rectangle(7, 4, 0, 2, 50)
        self.assertEqual(r3.x, 0)

    def test_y_eqauls_zero(self):
        r3 = Rectangle(7, 4, 3, 0, 50)
        self.assertEqual(r3.y, 0)

    def test_x_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r3 = Rectangle(9, 6, -1, 2, 50)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r3 = Rectangle(7, 4, 1, 2, 50)
            r3.x = -6

    def test_y_smaller_than_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r3 = Rectangle(6, 7, 1, -2, 50)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r3 = Rectangle(7, 4, 1, 2, 50)
            r3.y = -2

    def test_height_non_integer(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r3 = Rectangle(3, "5", 1, 2, 50)

    def test_height_non_integer_setter(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r3 = Rectangle(3, 4, 1, 2, 50)
            r3.height = "J"

    def test_x_non_integer(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3 = Rectangle(5, 4, [5], 2, 50)

    def test_x_non_integer_setter(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3 = Rectangle(3, 4, 1, 2, 50)
            r3.x = {}

    def test_y_non_integer(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3 = Rectangle(3, 4, 1, 9.64, 50)

    def test_y_non_integer_setter(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3 = Rectangle(3, 4, 1, 2, 50)
            r3.y = "J"

    def test_normal_area(self):
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

    def test_area_modification(self):
        r6 = Rectangle(99, 99)
        r6.width = 4
        r6.height = 5
        self.assertEqual(r6.area(), 20)

    def test_eqaul_area(self):
        r4 = Rectangle(6, 6)
        self.assertEqual(r4.area(), 36)

    def test_normal_area(self):
        r7 = Rectangle(2, 3)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "##\n##\n##\n"
        self.assertEqual(printed, expected)

    def test_area_is_one(self):
        r7 = Rectangle(1, 1)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "#\n"
        self.assertEqual(printed, expected)

    def test_square_area(self):
        r7 = Rectangle(2, 2)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "##\n##\n"
        self.assertEqual(printed, expected)

    def test_normal_offset(self):
        r7 = Rectangle(2, 2, 1, 1)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "\n ##\n ##\n"
        self.assertEqual(printed, expected)

    def test_zero_offset(self):
        r7 = Rectangle(2, 2, 0, 0)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "##\n##\n"
        self.assertEqual(printed, expected)

    def test_no_yoffset(self):
        r7 = Rectangle(2, 2, 2)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "  ##\n  ##\n"
        self.assertEqual(printed, expected)

    def test_no_offset(self):
        r7 = Rectangle(2, 2)
        r7.display()
        printed = sys.stdout.getvalue()
        expected = "##\n##\n"
        self.assertEqual(printed, expected)

    def test_normal_rectangle_using_string(self):
        r8 = Rectangle(4, 4, 7, 2, 3)
        self.assertEqual(str(r8), "[Rectangle] (3) 7/2 - 4/4")

    def test_normal_rectangle_using_print(self):
        r8 = Rectangle(4, 4, 7, 2, 3)
        print(r8)
        printed = sys.stdout.getvalue()
        expected = "[Rectangle] (3) 7/2 - 4/4\n"
        self.assertEqual(printed, expected)

    def test_print_width_and_height_of_one(self):
        r8 = Rectangle(1, 1, 0, 0, 0)
        self.assertEqual(str(r8), "[Rectangle] (0) 0/0 - 1/1")

    def test_print_no_x_y_or_id(self):
        r8 = Rectangle(1, 1)
        self.assertEqual(str(r8), "[Rectangle] ({}) 0/0 - 1/1". format(r8.id))

    def test_some_args(self):
        r6 = Rectangle(1, 2, 3, 4)
        r7 = Rectangle(1, 2, 3)
        r8 = Rectangle(1, 2,)
        self.assertEqual(str(r6), "[Rectangle] ({}) 3/4 - 1/2". format(r6.id))
        self.assertEqual(str(r7), "[Rectangle] ({}) 3/0 - 1/2". format(r7.id))
        self.assertEqual(str(r8), "[Rectangle] ({}) 0/0 - 1/2". format(r8.id))

    def test_normal_update_using_args(self):
        r1 = Rectangle(1, 2, 3, 5, 7)
        r1.update(6, 7, 8, 2, 10)
        self.assertEqual(str(r1), "[Rectangle] (6) 2/10 - 7/8")

    def test_modify_after_update(self):
        r1 = Rectangle(1, 2, 3, 5, 7)
        r1.update(6, 7, 8, 2, 10)
        r1.id = 200
        self.assertEqual(str(r1), "[Rectangle] (200) 2/10 - 7/8")

    def test_update_somw_args(self):
        r1 = Rectangle(1, 2, 3, 5, 7)
        r2 = Rectangle(1, 2, 3, 5, 7)
        r3 = Rectangle(1, 2, 3, 5, 7)
        r1.update(4, 4, 4, 4)
        r2.update(3, 3, 3)
        r3.update(1, 1)
        self.assertEqual(str(r1), "[Rectangle] (4) 4/5 - 4/4")
        self.assertEqual(str(r2), "[Rectangle] (3) 3/5 - 3/3")
        self.assertEqual(str(r3), "[Rectangle] (1) 3/5 - 1/2")

    def test_update_id(self):
        r1 = Rectangle(6, 7, 8, 9, 10)
        r1.update(4)
        self.assertEqual(r1.id, 4)

    def test_no_args(self):
        r1 = Rectangle(6, 7, 8, 9, 10)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (10) 8/9 - 6/7")

    def test_extra_args(self):
        r1 = Rectangle(6, 7, 8, 9, 10)
        r1.update(5, 5, 5, 5, 5, 5, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 5/5 - 5/5")

    def test_non_integrs(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(6, "", 8, 8, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.update(6, 7, "", 8, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(6, 8, 8, {}, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(6, 6, 8, 8, [7])

    def test_smaller_than_zero(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(6, -34, 8, 8, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.update(6, 7, -56, 8, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2.update(6, 8, 8, -78, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2.update(6, 6, 8, 8, -1)

    def test_equals_zero(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(6, 0, 8, 8, 9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.update(6, 7, 0, 8, 9)

    def test_None(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(6, None, 8, 8, 9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.update(6, 7, None, 8, 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(6, 8, 8, None, 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(6, 6, 8, 8, None)

    def test_normal_update_using_kwargs(self):
        r1 = Rectangle(1, 2, 3, 5, 7)
        r1.update(id=6, width=7, height=8, x=2, y=10)
        self.assertEqual(str(r1), "[Rectangle] (6) 2/10 - 7/8")

    def test_unordered_arguments(self):
        r1 = Rectangle(1, 2, 3, 5, 7)
        r1.update(id=6, height=8, width=7, y=2, x=10)
        self.assertEqual(str(r1), "[Rectangle] (6) 10/2 - 7/8")

    def test_update_somw_kwargs(self):
        r1 = Rectangle(1, 2, 3, 5, 7)
        r2 = Rectangle(1, 2, 3, 5, 7)
        r3 = Rectangle(1, 2, 3, 5, 7)
        r1.update(id=4, width=4, height=4, x=4)
        r2.update(id=3, width=3, height=3)
        r3.update(id=1, width=1)
        self.assertEqual(str(r1), "[Rectangle] (4) 4/5 - 4/4")
        self.assertEqual(str(r2), "[Rectangle] (3) 3/5 - 3/3")
        self.assertEqual(str(r3), "[Rectangle] (1) 3/5 - 1/2")

    def test_update_id_kwarg(self):
        r1 = Rectangle(6, 7, 8, 9, 10)
        r1.update(height=4)
        self.assertEqual(r1.height, 4)

    def test_extra_args(self):
        r1 = Rectangle(6, 7, 8, 9, 10)
        r1.update(id=5, width=5, y=5, x=5, height=5, jam=5, update=5)
        self.assertEqual(str(r1), "[Rectangle] (5) 5/5 - 5/5")

    def test_non_integrs(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(id=6, width="", height=8, x=8, y=9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.update(id=6, width=7, height="", x=8, y=9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(id=6, width=8, height=8, x={}, y=9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(id=6, width=6, height=8, x=8, y=[7])

    def test_smaller_than_zero(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(id=6, width=-34, height=8, x=8, y=9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.update(id=6, width=7, height=-56, x=8, y=9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r2.update(id=6, width=8, height=8, x=-78, y=9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r2.update(id=6, width=6, height=8, x=8, y=-1)

    def test_equals_zero(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r2.update(id=6, width=0, height=8, x=8, y=9)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.update(id=6, width=7, height=0, x=8, y=9)

    def test_None(self):
        r2 = Rectangle(5, 7, 8, 4, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r2.update(id=6, width=None, height=8, x=8, y=9)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.update(id=6, width=7, height=None, x=8, y=9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r2.update(id=6, width=8, height=8, x=None, y=9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r2.update(id=6, width=6, height=8, x=8, y=None)

    def test_dictionary_normal(self):
        r2 = Rectangle(10, 2, 1, 1, 1)
        expected = {'id': 1, 'x': 1, 'width': 10, 'height': 2, 'y': 1}
        self.assertDictEqual(r2.to_dictionary(), expected)

    def test_dictionary_new_obj(self):
        r1 = Rectangle(10, 2, 1, 1, 1)
        r2 = Rectangle(10, 2, 1, 1, 1)
        expected = {'id': 1, 'x': 1, 'width': 10, 'height': 2, 'y': 1}
        self.assertDictEqual(r2.to_dictionary(), expected)

    def test_dictionary_normal(self):
        r2 = Rectangle(10, 2, 1, 1)
        expected = {'id': r2.id, 'x': 1, 'width': 10, 'height': 2, 'y': 1}
        self.assertDictEqual(r2.to_dictionary(), expected)
