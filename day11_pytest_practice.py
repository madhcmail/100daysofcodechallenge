import day8_code_challenge_dicts as d8


def test_get_all_jeeps():
    expected = 'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    actual = d8.get_all_jeeps()
    assert type(actual) == str
    assert actual == expected

def test_first_model_each_manufacturer():
    expect = ['Falcon','Commodore','Maxima','Civic','Grand Cherokee']
    actual = d8.get_first_model_each_manufacturer()
    assert actual == expect


def test_get_all_matching_models():
    assert d8.get_all_matching_models(grep='trail') == ['Trailblazer', 'Trailhawk']
    assert d8.get_all_matching_models(grep = 'CO')  == ['Accord', 'Commodore', 'Falcon']

def test_sort_car_models():
    expected = {'Ford': ['Fairlane', 'Falcon', 'Festiva', 'Focus'],
                'Holden': ['Barina', 'Captiva', 'Commodore', 'Trailblazer'],
                'Nissan': ['350Z', 'Maxima', 'Navara', 'Pulsar'],
                'Honda': ['Accord', 'Civic', 'Jazz', 'Odyssey'],
                'Jeep': ['Cherokee', 'Grand Cherokee', 'Trackhawk', 'Trailhawk']}
    actual = d8.sort_car_models()
    assert actual == expected


============================================================================== test session starts ==============================================================================
platform darwin -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0 -- /opt/anaconda3/bin/python

collected 4 items

day11_pytest_practice.py::test_get_all_jeeps PASSED                                                                                                                       [ 25%]
day11_pytest_practice.py::test_first_model_each_manufacturer PASSED                                                                                                       [ 50%]
day11_pytest_practice.py::test_get_all_matching_models PASSED                                                                                                             [ 75%]
day11_pytest_practice.py::test_sort_car_models PASSED                                                                                                                     [100%]

=============================================================================== 4 passed in 0.02s ===============================================================================