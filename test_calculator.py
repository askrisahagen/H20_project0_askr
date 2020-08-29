import calculator

def test_add_integer():
    assert calculator.add(1,2) == 3

def test_add_float():
    from math import isclose

    assert isclose(calculator.add(0.1,0.2), 0.3)

def test_add_string():
    assert calculator.add("Hello ","World") == "Hello World"