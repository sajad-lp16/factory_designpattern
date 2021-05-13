import pytest
from simple_factory_pattern2 import *


class TestOperations:

    @pytest.fixture
    def set_up(self):
        pass

    def test_add(self):
        assert AddOperation(4, 5).execute() == 9
        assert AddOperation(-5, 4).execute() == -1

    def test_subtraction(self):
        assert Subtraction(0, -5).execute() == 5
        assert Subtraction(-4, 1).execute() == -5

    def test_division(self):
        assert Division(4, 2).execute() == 2
        with pytest.raises(ZeroDivisionError):
            Division(10, 0).execute()

    def test_multiply(self):
        assert Multiply(0, 200).execute() == 0
        assert Multiply(7, 8).execute() == 56
