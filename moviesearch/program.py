import api


def main():
    keyword = input('Enter Movie keyword: ')
    results = api.find_movie_by_title(keyword)
    print(f"There are {len(results)} movies found")
    for r in results:
        print(f"Title : {r.get('title')} has imdb score of {r.get('imdb_score')}")


if __name__ == '__main__':
    main()