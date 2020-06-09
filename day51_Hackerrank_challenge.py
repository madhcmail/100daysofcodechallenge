'''

Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

'''

from itertools import groupby
values = []
for key, count in groupby(input()):
    values.append((len(list(count)), int(key)))
print(*values) # unpacking list values


if __name__ == '__main__':
    site = pull_site()
    scrape(site)
