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

    def test_check_file(self):
        self.assertEqual(check_file(path="example.txt"), "Все найденные пароли: ['aA!12345']")

    def test_check_url(self):
        example_html = "<li>Valid password:<strong> StrongP@ss1 </strong><rd:<strong> Test@123A </strong></li>"
        self.assertEqual(check_string(password=example_html),
                         "Все найденные пароли: ['StrongP@ss1', 'Test@123A']")


if __name__ == "__main__":
    unittest.main()