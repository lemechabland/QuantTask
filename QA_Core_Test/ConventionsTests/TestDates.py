import unittest
from QA_Core.Conventions.Dates import Date


class TestDateConstructors(unittest.TestCase):
    def setUp(self):
        self.testDate = Date(2024, 7, 1)
        self.testDate2 = Date.from_string("2024-07-01")

    def test_default_constructor(self):
        self.assertEqual(self.testDate.year, 2024)
        self.assertEqual(self.testDate.month, 7)
        self.assertEqual(self.testDate.day, 1)

    def test_construct_date_from_string(self):
        self.assertEqual(self.testDate2.year, 2024)
        self.assertEqual(self.testDate2.month, 7)
        self.assertEqual(self.testDate2.day, 1)


class TestDateRepresentation(unittest.TestCase):
    def setUp(self):
        self.testDate = Date(2024, 7, 1)

    def test_representation(self):
        self.assertEqual(self.testDate.__repr__(), "Date(2024, 7, 1)")


class TestDateOperators(unittest.TestCase):
    def setUp(self):
        self.testDate1 = Date(2024, 7, 1)
        self.testDate2 = Date(2024, 7, 2)
        self.testDate3 = Date(2023, 7, 1)
        self.testDate4 = Date(2024, 6, 1)

    def test_greaterThan(self):
        self.assertTrue(self.testDate2 > self.testDate1)
        self.assertTrue(self.testDate2 > self.testDate3)
        self.assertTrue(self.testDate2 > self.testDate4)

    def test_lessThan(self):
        self.assertTrue(self.testDate3 < self.testDate1)
        self.assertFalse(self.testDate4 < self.testDate3)

    def test_equal(self):
        self.assertTrue(self.testDate1 == self.testDate1)

    def test_neq(self):
        self.assertTrue(self.testDate1 != self.testDate2)


class TestIncorrectDateThrowsAnError(unittest.TestCase):

    def test_incorrect_date_throws_error(self):
        with self.assertRaises(Exception) as assert_error:
            Date(2024, 2, 30)
        self.assertEqual(assert_error.exception.args[0], "Date(2024, 2, 30) cannot be constructed.")
        with self.assertRaises(Exception) as assert_error:
            Date(2024, 13, 2)
        self.assertEqual(assert_error.exception.args[0], "Date(2024, 13, 2) cannot be constructed.")


if __name__ == '__main__':
    unittest.main()
