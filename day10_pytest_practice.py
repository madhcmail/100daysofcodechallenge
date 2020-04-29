import pytest


def hello(name):
    return f"Hello {name}"

def func(x):
    return x + 5


def test_fun():
    assert func(3) == 8


def test_fun2():
    assert func(0) == 5


# grouping by test sub-strings match. You can run pytest -k method1 -v; pytest -k method2 -v;
# -k : matches the substring

def test_method1():
    x = 10
    y = 10
    assert x == y

def test_method2():
    a = 15
    b = 20
    assert a+5 == b

def test_hello():
    assert hello('Python') == 'Hello Python'
