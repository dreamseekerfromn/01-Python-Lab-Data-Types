import unittest
from numbers_1 import safe_divide, factorial, sum_of_digits
from booleans import is_divisible, complex_check
from strings import count_vowels, replace_char, format_name, is_valid_email
from mixed_operators import combine_and_convert, mixed_operations, compare_types

class TestNumbers(unittest.TestCase):

    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertEqual(safe_divide(10, 0), "Error: Division by zero")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(0), 0)

class TestBooleans(unittest.TestCase):

    def test_is_divisible(self):
        self.assertTrue(is_divisible(10, 2))
        self.assertFalse(is_divisible(10, 3))

    def test_complex_check(self):
        self.assertTrue(complex_check(6))
        self.assertFalse(complex_check(-5))
        self.assertTrue(complex_check(-9))

class TestStrings(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Octopocalypse"), 6)
        self.assertEqual(count_vowels("Python"), 1)

    def test_replace_char(self):
        self.assertEqual(replace_char("Hello World", "l", "z"), "Hezzo Worzd")
        self.assertEqual(replace_char("abcdef", "a", "A"), "Abcdef")

    def test_format_name(self):
        self.assertEqual(format_name("John", "Doe"), "Doe, John")
        self.assertEqual(format_name("John"), "Unknown, John")
        self.assertEqual(format_name(), "Unknown, Unknown")

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("test@example"))
        self.assertFalse(is_valid_email("test@.com"))
        self.assertFalse(is_valid_email("test@com"))

class TestMixedOperations(unittest.TestCase):

    def test_combine_and_convert(self):
        self.assertEqual(combine_and_convert(10, "25"), "3525")
        self.assertEqual(combine_and_convert(100, "50"), "15050")

    def test_mixed_operations(self):
        self.assertEqual(mixed_operations(9, True), 81)
        self.assertEqual(mixed_operations(9, False), 3.0)

    def test_compare_types(self):
        self.assertTrue(compare_types(10, 5))
        self.assertFalse(compare_types(10, "10"))
        self.assertTrue(compare_types("string", "another string"))

if __name__ == "__main__":
    unittest.main()
