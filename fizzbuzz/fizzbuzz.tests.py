import unittest
import fizzbuzz

class FizzbuzzTests(unittest.TestCase):

    def test_checkfizz(self):
        result = fizzbuzz.checkfizz(3)
        self.assertEqual(result, "Fizz")

    def test_checkbuzz(self):
        result = fizzbuzz.checkbuzz(5)
        self.assertEqual(result, "Buzz")

    def test_checknotfizz(self):
        result = fizzbuzz.checkfizz(4)
        self.assertEqual(result, "")

    def test_checknotbuzz(self):
        result = fizzbuzz.checkbuzz(2)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
