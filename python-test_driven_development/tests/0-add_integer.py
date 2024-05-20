import unittest
from add_integer import add_integer

class TestAddInteger(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(-1, 1), 0)
        self.assertEqual(add_integer(0, 0), 0)
        self.assertEqual(add_integer(100, 200), 300)

    def test_floats(self):
        self.assertEqual(add_integer(1.5, 2.5), 3)
        self.assertEqual(add_integer(-1.7, 1.2), -1)
        self.assertEqual(add_integer(0.0, 0.0), 0)
        self.assertEqual(add_integer(100.9, 200.1), 300)

    def test_default_argument(self):
        self.assertEqual(add_integer(2), 100)
        self.assertEqual(add_integer(0), 98)
        self.assertEqual(add_integer(-2), 96)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            add_integer("a", 2)
        with self.assertRaises(TypeError):
            add_integer(2, "b")
        with self.assertRaises(TypeError):
            add_integer(None, 2)
        with self.assertRaises(TypeError):
            add_integer(2, None)

    def test_large_numbers(self):
        self.assertEqual(add_integer(1e10, 1e10), 20000000000)

    def test_special_values(self):
        with self.assertRaises(TypeError):
            add_integer(float('inf'), 1)
        with self.assertRaises(TypeError):
            add_integer(1, float('inf'))
        with self.assertRaises(TypeError):
            add_integer(float('nan'), 1)
        with self.assertRaises(TypeError):
            add_integer(1, float('nan'))

if __name__ == '__main__':
    unittest.main()
