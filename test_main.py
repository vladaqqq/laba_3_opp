import unittest
from main import *

class TestCheckAll(unittest.TestCase):
    def setUp(self):
        self.valid_data = ["abcdef1A!", "!!!!@@@@aB1", "09876543Ab!"]
        self.invalid_data = ["Aa!1234", "Aa!12345678bcfdt", "AaBbCcDd!"]

    def test_check_string(self):
        for i in self.valid_data:
            with self.subTest(i=i):
                self.assertEqual(check_string(password=i), f"Все найденные пароли: ['{i}']")

    def test_check_string1(self):
        for i in self.invalid_data:
            with self.subTest(i=i):
                self.assertEqual(check_string(password=i), f"Пароли не найдены")


