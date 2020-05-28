import os
import csv
import collections

Record = collections.namedtuple('Record', 'region, income_range, main_dish,sides')
data = []

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data','thanksgiving_data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_data(row)
            data.append(record)


def parse_data(row):
    sides = []
    for k,v in row.items():
        if 'side' in k:
            sides.append(v)
    record = Record(
        region=row['US Region'],
        income_range=row['How much total combined money did all members of your HOUSEHOLD earn last year?'],
        main_dish=row['What is typically the main dish at your Thanksgiving dinner?'],
        sides=sides
        )
    return record


init()
print(data)