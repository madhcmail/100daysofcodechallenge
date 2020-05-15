from itertools import cycle
from time import sleep
import random

colors = "Red Green Amber".split()
rotation = cycle(colors)


def rd_timer():
    return random.randint(3, 7)


def traffic_lights():
    for color in rotation:

        if color == 'Amber':
            print(f"Slow Down! The light is {color}")
            sleep(3)
        elif color == 'Red':
            print(f"STOP! The light is {color}")
            sleep(rd_timer())
        else:
            print(f"Go! The light is green {color}")
            sleep(rd_timer())


if __name__  == '__main__' :
    traffic_lights()
