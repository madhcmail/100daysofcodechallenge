"""
Turn the following unix pipeline into Python code using generators
$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""
import os
import fnmatch
import glob
import re
from collections import Counter

def gen_files(pat):
    for file in glob.glob(pat):
        yield file


def gen_lines(files):
    with open(files, 'r') as f:
        data = [line for line in f.readlines()if line.startswith('import')]
        yield data


def gen_grep(lines, pattern):
    new_list = []

    for line in lines:
        new_list.append(line.split()[1].rstrip('\n'))
    yield new_list


def gen_count(new_list):
    pass


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    for _ in range(29):
        f = next(files)
        lines = gen_lines(f)
        l = next(lines)
        if len(l) > 0:
            g = gen_grep(l)
        else:
            continue

        print(Counter(sorted(next(g))))
   # greps = gen_grep(next(lines), 'import')
   # next(greps)









