import unittest
import company


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.dan = company.Employee("Michael", "Jordan", 10000)

# 4 Test should pass

    def test_give_raise_default_works(self):
        self.assertEqual(self.dan.give_raise(), "After a raise of 5000, you have 15000.")

    def test_give_raise_works_with_positive_integer(self):
        self.assertEqual(self.dan.give_raise(10000), "After a raise of 10000, you have 20000.")

    def test_give_raise_negative_raise_error(self):
        self.assertEqual(self.dan.give_raise(-100), "-100 is NOT a raise!")

    def test_give_raise_non_integer_error(self):
        self.assertEqual(self.dan.give_raise("hundred"), "You need to enter a positive integer!")

# This is the failed test.

    def test_give_raise_zero_message(self):
        self.assertEqual(self.dan.give_raise(0), "There is no raise!")


if __name__ == '__main__':
    unittest.main()




