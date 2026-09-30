import pytest
from src.calculator import add, subtract, multiply, divide, evaluate_expression


def test_basic_operations():
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_evaluate_expression():
    assert evaluate_expression("2+3*4") == "14"
    assert evaluate_expression("10/2") == "5"
    assert evaluate_expression("5/0") == "Error"
    assert evaluate_expression("__import__('os')") == "Error"
