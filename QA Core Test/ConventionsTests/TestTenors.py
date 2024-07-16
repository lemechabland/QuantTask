import unittest
from QA_Core.Conventions.Tenors import Tenor


class TestTenorConstructors(unittest.TestCase):
    def setUp(self):
        self.tenor3M = Tenor("3M")
        self.another_tenor3M = Tenor.tenor(0, 0, 3, 0)
        self.tenor1Y3M = Tenor.tenor(0, 0, 3, 1)

    def test_default_constructor(self):
        self.assertEqual(self.tenor3M.Months, 3)

    def test_tenor_can_construct(self):
        self.assertEqual(self.tenor1Y3M.Days, 0)
        self.assertEqual(self.tenor1Y3M.Months, 3)
        self.assertEqual(self.tenor1Y3M.Years, 1)

    def test_incorrect_tenor_string_throws_error(self):
        with self.assertRaises(Exception) as assert_error:
            Tenor("2D1Y")
        self.assertEqual(assert_error.exception.args[0], "2D1Y is not OK.")

    def test_tenor_can_be_represented_as_string(self):
        self.assertEqual(str(self.tenor1Y3M), "1Y3M")
        self.assertEqual(str(self.tenor3M), "3M")

    def test_tenors_are_not_equal(self):
        self.assertTrue(self.tenor1Y3M != self.tenor3M)

    def test_tenors_are_equal(self):
        self.assertTrue(self.tenor3M == self.another_tenor3M)

    def test_tenor_can_be_constructed_from__(self):
        self.assertTrue(Tenor.from_years(1), Tenor("1Y"))
        self.assertTrue(Tenor.from_days(1), Tenor("1D"))
        self.assertTrue(self.tenor3M, Tenor.from_months(3))


if __name__ == '__main__':
    unittest.main()
