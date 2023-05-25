import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_mult_positive(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_div_positive(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_zero_addition_positive(self):
        assert self.calc.adding(self, 10, 0) == 10

    def test_zero_subtraction_positive(self):
        assert self.calc.subtraction(self, 10, 0) == 10

    def teardown(self):
        print("teardown method executed")
