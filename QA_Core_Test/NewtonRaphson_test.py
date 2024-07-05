import unittest
from unittest import TestCase
from QA_Core.Math.NewtonRaphsonOneDim import NewtonRaphsonOneDim
import math


def f(x):
    return x ** 2 - 4 * x + 2


def g(x):
    return math.cos(x) - x ** 3


class TestNewtonRaphson(TestCase):
    def setUp(self):
        self.NR = NewtonRaphsonOneDim(f, 3)

    def test_initialization(self):
        self.assertTrue(hasattr(self.NR.func, '__call__'))
        self.assertEqual(self.NR.x0, 3)

    def test_newton_raphson(self):
        result = self.NR.newton_raphson(diff_method='central')
        self.assertAlmostEqual(result, 3.4142135624)


class TestGettingResultBeforeReachingMaxIter(TestCase):
    def setUp(self):
        self.NR = NewtonRaphsonOneDim(g, 0.5)

    def test_newton_raphson(self):
        result = self.NR.newton_raphson(diff_method='central')
        self.assertAlmostEqual(result, 0.87, places=2)


if __name__ == "__main__":
    unittest.main()
