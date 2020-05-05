
# List comprehensions provides a concise way to write lists
# It consists of brackets containing an expression followed by a for clause, then zero or more if clauses
# The list comprehension always returns a result list.

from collections import Counter
import string
import requests
import re

names = "harry bob scott emily katie sassy cassy"
names = names.split()
print (names)

for name in names:
    print (name.title())

names_list = [name.title() for name in names]
print(names_list)

# print only the names in A-M

first_half_alphabet = list(string.ascii_lowercase)[:13]
print(first_half_alphabet)

names_new_list = []
for name in names:
    if name[0] in first_half_alphabet:
        names_new_list.append(name.title())
print(sorted(names_new_list))

# The above 4 lines of code can be rewritten in to single line. This is called list compreshension

names_new_list2 = sorted([name.title() for name in names if name[0] in first_half_alphabet])
print(names_new_list2)

# The below, a most common word count on Harry Potter.
# Use some list comprehensions to clean up the words before counting them

resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
print (words[:5])

# find the most common words

cnt = Counter(words)
print(cnt.most_common(5))

# clean up the stopwords like the, and, so, to, -

print('-' in words)

# Let's first clean up any non-alphabetic characters using regex
# we use re.sub (search and replace)
# re.sub(pattern, repl, string, max=0)
# \W : Mateches non word characters; + matches one ore more preceeding characters

words = [re.sub(r'\W+', r'', word) for word in words]
print('-' in words)  # returns false now which means non word characters are cleaned.

# Let's filter the stop words

resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
print(stopwords[:5])

words = [word for word in words if word.strip() and word not in stopwords]
print(words[:5]) # gives the words list by cleaning the stopwords


cnt = Counter(words)
print(cnt.most_common(5))

word1 = 'Madhuri '
print(word1.strip())