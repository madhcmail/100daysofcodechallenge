import logging
import day34_logging_in_python

logger = logging.getLogger(__name__) # this will take the re
logger.setLevel(logging.DEBUG) # setting the loglevel

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# define the log file name
file_handler = logging.FileHandler('employee.log')
# add the formatter to the file handler
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def add(x,y):
    """ Add Function"""
    return x + y


def sub(x, y):
    """ Subtract function"""
    return x - y


def mul(x, y):
    """ Multiplication function"""
    return x * y


def div(x, y):
    """Division function"""
    return x/y


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logger.debug(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = sub(num_1, num_2)
logger.debug(f"Sub: {num_1} - {num_2} = {sub_result}")

mul_result = mul(num_1, num_2)
logger.debug(f"Mul: {num_1} * {num_2} = {mul_result}")

div_result = div(num_1, num_2)
logger.debug(f"Div: {num_1} / {num_2} = {div_result}")
