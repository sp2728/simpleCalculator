
from simpleCalculator import calculator
import pytest
import unittest


class test_PythonSimpleCalc(unittest.TestCase):
    def test_calc(self):
        assert calculator

    def test_calc_add(self):

        assert calculator.add(3, 2) == 5

    def test_calc_subtract(self):
        assert calculator.subtraction(0, 10) == -10

    def test_calc_multiply(self):
        assert calculator.multiply(2, 2) == 4

    def test_calc_divide(self):
        assert calculator.divide(10, 5) == 2

    def test_calc_square(self):
        assert calculator.square(5)== 25

    def test_calc_squareroot(self):
        assert calculator.squareRoot(25) == 5