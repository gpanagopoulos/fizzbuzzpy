import unittest
import fizzbuzz

class FizzbuzzTests(unittest.TestCase):

    def test_check_fizz(self):
        result = fizzbuzz.check_fizz(3)
        self.assertEqual(result, "Fizz")

    def test_check_buzz(self):
        result = fizzbuzz.check_buzz(5)
        self.assertEqual(result, "Buzz")

    def test_check_fizzbuzz(self):
        result = fizzbuzz.check_fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")

    def test_check_notfizzbuzz(self):
        result = fizzbuzz.check_fizzbuzz(1)
        self.assertEqual(result, "1")

    def test_check_notfizz(self):
        result = fizzbuzz.check_fizz(4)
        self.assertEqual(result, "")

    def test_check_notbuzz(self):
        result = fizzbuzz.check_buzz(2)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
