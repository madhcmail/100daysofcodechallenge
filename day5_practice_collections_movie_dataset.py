import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
MIN_MOVIES = 4

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data='movie_metadata.csv'):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors


# directors with most movies
def get_most_movies(directors):
    cnt = Counter()
    for director,movies in directors.items():
        cnt[director] += len(movies)
    return cnt.most_common(5)


def get_min_movies(directors):
    '''Filter directors with < MIN_MOVIES '''
    dir_min_movies_cnt = Counter()
    for director,movies in directors.items():
        if len(movies) < MIN_MOVIES:
            dir_min_movies_cnt [director] += len(movies)

    return dir_min_movies_cnt


def main():
    directors = get_movies_by_director()
    print(directors['Christopher Nolan'])
    top_most = get_most_movies(directors)
    print(top_most)
    min_movies = get_min_movies(directors)
    print(min_movies)


if __name__ == '__main__':
    main()
