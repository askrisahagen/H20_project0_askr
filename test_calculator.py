import calculator

def test_add_integer():
    assert calculator.add(1,2) == 3

def test_add_float():
    from math import isclose

    assert isclose(calculator.add(0.1,0.2), 0.3)

def test_add_string():
    assert calculator.add("Hello ","World") == "Hello World"

def test_factorial_integer():
    assert calculator.factorial(4) == 24

def test_factorial_negativ():
    assert calculator.factorial(-1) == "This factorial only works with integers"

def test_factorial_zero():
    assert calculator.factorial(0) == 1

def test_sin():
    import math

    assert math.isclose(calculator.sin(math.pi/3,5), 3**0.5/2)

def test_divide_integers():
    assert calculator.divide(12,-3) == -4

def test_divide_floats():
    from math import isclose

    assert isclose(calculator.divide(0.4,0.1), 4.0)

def test_abs_integer():
    assert calculator.abs(-3) == 3

def test_abs_float():
    from math import isclose

    assert isclose(calculator.abs(20.2),20.2)

def test_nthroot():
    assert calculator.nthroot(27,3) == 3 

def test_add_raises_TypeError():
    import pytest

    with pytest.raises(TypeError):
        calculator.add(2,"you")

def test_divide_raises_ZeroDivision_Error():
    import pytest

    with pytest.raises(ZeroDivisionError):
        calculator.divide(4,0)

