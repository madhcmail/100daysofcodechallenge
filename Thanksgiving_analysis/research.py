import os
import csv
import collections

Record = collections.namedtuple('Record', 'region, income_range, main_dish,sides')
data = []


# parse the CSV data and create a list of named tuples with the required fields
def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'thanksgiving_data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_data(row)
            data.append(record)


# Below function creates a named tuple
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


regions = set()  # get unique regions
income = set()  # get unique income

us_regions = {}  # dictionary for user to pick the region key and validate the user input
us_income_range = {}  # dictionary for user to pick the income_range key and validate the user input

main_dishes = []  # list to count the most common main dishes
side_dishes = []  # list to count the most common side dishes


# get the available regions and income ranges from the data set for the user to choose
def get_regions_and_income():
    for row in data:
        if row.region != '':
            regions.add(row.region)
        if row.income_range != '' and row.income_range != 'Prefer not to answer':
            income.add(row.income_range)

    for idx, each_region in enumerate(list(sorted(regions)), 1):
        us_regions[str(idx)] = each_region
    for idx, income_r in enumerate(list(sorted(income)), 1):
        us_income_range[str(idx)] = income_r

    return us_regions, us_income_range


# function to return the main dish and sides dishes for the user input region and income_range
def get_menu(user_input_region, user_input_income):
    for row in data:
        if row.region == user_input_region and row.income_range == user_input_income:
            main_dishes.append(row.main_dish)
            for dish in row.sides:
                side_dishes.append(dish)
    cnt_main = collections.Counter(main_dishes)
    cnt_sides = collections.Counter(side_dishes)
    return cnt_main.most_common(1), cnt_sides.most_common(5)

