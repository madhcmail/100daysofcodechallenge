import csv
from collections import namedtuple

# with cvs.reader and csv.writer
count = 0
with open('movie_metadata.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open("new_movies.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter=';')

        for line in csv_reader:
            count = count + 1
            if count <=3:
                csv_writer.writerow(line)


# with csv.DictReader and csv.DictWriter
# more readable and accessible way
Movie = namedtuple('Movie','director movie')
with open('movie_metadata.csv' ,'r') as new_dict_file:
    csv_reader = csv.DictReader(new_dict_file)
    for line in csv_reader:
        if 'title_year' > '2017' and 'num_user_reviews' > '75':
            director = line['director_name']
            movie = line['movie_title']

            m = Movie(director,movie)
            print(m.director,m.movie)






