import csv
import os
import collections


data = []
Record = collections.namedtuple(
    'Record',
    'date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,'
    'average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,'
    'record_max_temp_year,actual_precipitation,average_precipitation,'
    'record_precipitation')


def init():
    # __file__ : is variable that contains the path to the module that is currently being imported.
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear() # just incase if run twice, it should get clear the data in the list and rerun the loop
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])

    record = Record(
        **row  # set each column value to the value of the dictionary
    )
    return record

init()

print(data)