import csv
import os

data = []


def init():
    # __file__ : is variable that contains the path to the module that is currently being imported.
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            # prints a ordered dictionary
            #print(f"Row -> {row}")
            print(f"max -> {row.get('record_max_temp')}")
            print(f"min -> {row.get('record_min_temp')}")


