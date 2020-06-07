import api
import webbrowser


def main():
    keyword = input('What keywords to search for; Enter Multiple keywords separate by "-"?:  ')
    results = api.search_talkpython_by_keyword('%s' % keyword)

    # Displays the matchings based on teh search
    print(f'There are {len(results)} matchings found')
    for idx, r in enumerate(results):
        print(f'{idx + 1}: {r.category}({r.id}) - "{r.title}" has url {r.url}')

    # get an index from the displayed results to show that in users default browser
    r_index = int(input("Enter the index from the results to view them: "))
    open_url = f'https://talkpython.fm{results[r_index -1].url}'
    # print(open_url)
    webbrowser.open(open_url)


if __name__ == '__main__':
    main()