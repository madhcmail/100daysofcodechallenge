import os
import csv
import collections


Record = collections.namedtuple('Record', 'region, income_range, main_dish,sides')
data = []


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'thanksgiving_data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_data(row)
            data.append(record)


def parse_data(row):
    sides = []
    for k, v in row.items():
        if 'side' in k and v != '':
            sides.append(v)
    record = Record(
        region=row['US Region'],
        income_range=row['How much total combined money did all members of your HOUSEHOLD earn last year?'],
        main_dish=row['What is typically the main dish at your Thanksgiving dinner?'],
        sides=sides
        )
    return record


regions = set()
income = set()
main_dishes = []
side_dishes = []


def get_regions():
    for row in data:
        if row.region != '':
            regions.add(row.region)
    return list(sorted(regions))


def get_income_ranges():
    for i in data:
        if i.income_range != '' and i.income_range != 'Prefer not to answer':
            income.add(i.income_range)

    return list(sorted(income))


def get_menu(user_input_region, user_input_income):
    for row in data:
        if row.region == user_input_region and row.income_range == user_input_income:
            main_dishes.append(row.main_dish)
    cnt_main = collections.Counter(main_dishes)
    return cnt_main.most_common(1)


def get_sides(user_input_region, user_input_income):
    for row in data:
        if row.region == user_input_region and row.income_range == user_input_income:
            for dish in row.sides:
                side_dishes.append(dish)
    #print(side_dishes)
    cnt_sides = collections.Counter(side_dishes)
    return cnt_sides.most_common(5)
