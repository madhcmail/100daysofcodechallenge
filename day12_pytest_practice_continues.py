import pytest
import json
from math_func import StudentDB
# How to run a specific test case. Use the below format to run it
# pytest <test file name>::<testcase function name> -v

# -k is used to run test cases based on the substrings that you add in " "
#Eg: python -v <test file name> -k "add"

# -m is used for markers. Suppose if you want to group few tests you can mark them with decorators
#as @pytest.mark.number  or @pytest.mark.strings


def add(x, y=2):
    return x + y


def product(x, y=2):
    return x * y

@pytest.mark.number1
def test_add():
    assert add(2, 3) == 5
    assert add(2) == 4

@pytest.mark.number1
def test_product():
    assert product(2,3) == 6
    assert product(2) == 4


@pytest.mark.strings1
def test_add_strings():
    result = add("Hello","Python")
    assert result == "HelloPython"
    assert type(result) is str


def test_add_without_parameterize():
    assert add(7,3) == 10
    assert add('Hello',' World') == 'Hello World'
    assert add(3.6, 6.4) == 10


@pytest.mark.parametrize('num1, num2, result',
                         [
                            (7, 3, 10),
                            ('Hello', ' World', 'Hello World'),
                            (10.5, 25.5, 36)
                         ]
                         )
def test_add_with_parameterize(num1, num2, result):
    assert add(num1, num2) == result


def test_scott_data():
    db = StudentDB()
    db.connect('data.json')
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data():
    db = StudentDB()
    db.connect('data.json')
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'


# Results
============================================================================== test session starts ==============================================================================
platform darwin -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/xxxx/PycharmProjects/100daysofcode
plugins: arraydiff-0.3, remotedata-0.3.2, doctestplus-0.4.0, openfiles-0.4.0, cov-2.8.1
collected 9 items

day12_pytest_practice_continues.py::test_add PASSED                                                                                                                       [ 11%]
day12_pytest_practice_continues.py::test_product PASSED                                                                                                                   [ 22%]
day12_pytest_practice_continues.py::test_add_strings PASSED                                                                                                               [ 33%]
day12_pytest_practice_continues.py::test_add_without_parameterize PASSED                                                                                                  [ 44%]
day12_pytest_practice_continues.py::test_add_with_parameterize[7-3-10] PASSED                                                                                             [ 55%]
day12_pytest_practice_continues.py::test_add_with_parameterize[Hello- World-Hello World] PASSED                                                                           [ 66%]
day12_pytest_practice_continues.py::test_add_with_parameterize[10.5-25.5-36] PASSED                                                                                       [ 77%]
day12_pytest_practice_continues.py::test_scott_data PASSED                                                                                                                [ 88%]
day12_pytest_practice_continues.py::test_mark_data PASSED                                                                