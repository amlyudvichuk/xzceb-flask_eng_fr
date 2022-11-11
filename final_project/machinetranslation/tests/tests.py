import unittest
from translator import french_to_english, english_to_french

class test_english_to_french(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNotNone(english_to_french('Hello'))

    def test_french_to_english(self):
        self.assertIsNotNone(french_to_english('Bonjour'))

if __name__ == '__main__':
    unittest.main()

