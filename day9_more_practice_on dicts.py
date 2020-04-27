lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
    print(f"student name:{student['name']}")
    print(f"student homework: {student['homework']}")
    print(f"student quizzes:{student['quizzes']}")
    print(f"student tests:{student['tests']}")


def average(numbers):
    return float(sum(numbers))/len(numbers)


def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    student_avg=(0.1 * homework + 0.3 * quizzes + 0.6 * tests)
    return student_avg


def get_class_average(students):
    results = []
    for student in students:
        r = get_average(student)
        results.append(r)
    return average(results)


students = [lloyd,alice,tyler]
print (get_class_average(students))

# *******************Example 2*********************************
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


states_list = ['Oklahoma',
               'Kansas',
               'North Carolina',
               'Georgia',
               'Oregon',
               'Mississippi',
               'Minnesota',
               'Colorado',
               'Alabama',
               'Massachusetts',
               'Arizona',
               'Connecticut',
               'Montana',
               'West Virginia',
               'Nebraska',
               'New York',
               'Nevada',
               'Idaho',
               'New Jersey',
               'Missouri',
               'South Carolina',
               'Pennsylvania',
               'Rhode Island',
               'New Mexico',
               'Alaska',
               'New Hampshire',
               'Tennessee',
               'Washington',
               'Indiana',
               'Hawaii',
               'Kentucky',
               'Virginia',
               'Ohio',
               'Wisconsin',
               'Maryland',
               'Florida',
               'Utah',
               'Maine',
               'California',
               'Vermont',
               'Arkansas',
               'Wyoming',
               'Louisiana',
               'North Dakota',
               'South Dakota',
               'Texas',
               'Illinois',
               'Iowa',
               'Michigan',
               'Delaware']
count = 0

for keys,values in us_state_abbrev.items():
    count = count + 1
    if count == 27:
        print(f"value at 27th position {values} ")
    if count == 45:
        print(f"Key at 45th position: {keys}")
        break
    if count == 10:
        print(f"items at 10th position {keys}:{values}")
        print(count)








