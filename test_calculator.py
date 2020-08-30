import calculator
import pytest
import math

@pytest.mark.parametrize("arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]])
def test_add_integer(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(-1.1, -1.2), -2.3], [(1.4, 1.5), 2.9], [(1.0, 0.1), 1.1]])
def test_add_float(arg, expected_output):
    assert math.isclose(calculator.add(arg[0], arg[1]), expected_output)

@pytest.mark.parametrize("arg, expected_output", [[("Hello ", "world"), "Hello world"], [("To ", "you"), "To you"], [("Git", "Hub"), "GitHub"]])
def test_add_string(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [(4, 24), (0, 1), (3,6), (-1, "This factorial only works with integers")])
def test_factorial_integer(arg, expected_output):
    assert calculator.factorial(arg) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(math.pi/3, 5), 3**0.5/2], [(math.pi/6, 4), 0.5], [(math.pi/2, 6), 1]])
def test_sin(arg, expected_output):
    assert math.isclose(calculator.sin(arg[0], arg[1]), expected_output)

@pytest.mark.parametrize("arg, expected_output",[[(-1, -1), 1], [(1, 1), 1], [(6, 2), 3]])
def test_divide_integers(arg, expected_output):
    assert calculator.divide(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output",[[(-1.2, -1.2), 1.0], [(1.5, 3), 0.5], [(6.9, 3), 2.3]])
def test_divide_floats(arg, expected_output):
    assert math.isclose(calculator.divide(arg[0], arg[1]), expected_output)

@pytest.mark.parametrize("arg, expected_output",[(-3,3), (2,2), (-5,5)])
def test_abs_integer(arg, expected_output):
    assert calculator.abs(arg) == expected_output

@pytest.mark.parametrize("arg, expected_output",[(-3.3,3.3), (2.4,2.4), (-5.6,5.6)])
def test_abs_float(arg, expected_output):
    assert math.isclose(calculator.abs(arg), expected_output)

@pytest.mark.parametrize("arg, expected_output",[[(27, 3), 3], [(4, 2), 2], [(125, 3), 5]])
def test_nthroot(arg, expected_output):
    assert calculator.nthroot(27,3) == 3 

@pytest.mark.parametrize("arg",[[2, "you"], ["Pie ", 3], [2, "me"]])
def test_add_raises_TypeError(arg):
    with pytest.raises(TypeError):
        calculator.add(arg[0],arg[1])

@pytest.mark.parametrize("arg",[[2, 0], [12392781, 0], [23467, 0]])
def test_divide_raises_ZeroDivision_Error(arg):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(arg[0],arg[1])
