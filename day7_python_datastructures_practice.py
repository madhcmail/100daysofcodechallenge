lst = [1,2,3,4,5]
print(lst)

for num in lst:
    print(num)

lst.reverse()  # reverse the list
print(lst)

lst.sort()  # sort the list
print(lst)

last_element = lst.pop()  #  pop the last element
print(last_element)

print(lst)

lst.insert(5,5)  # insert an element in to list a specified position
print(lst)

lst.insert(3,7)
print(lst)

lst = [1, 2, 3, 4, 5]
l_item = lst[4]
print(l_item)

lst.insert(-1,5)

mystring ="Hello Python"
lst2= list(mystring)   # converting string to list
print(lst2)  # prints as ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']

#get the position of the space
print(lst2.index(' ')) #  prints 5

# now replace with -
lst2.remove(' ')
print(lst2)  #  ['H', 'e', 'l', 'l', 'o', 'P', 'y', 't', 'h', 'o', 'n']

lst2.insert(5,'-')

# convert list to string
mystring_back = ""
for char in lst2:
    mystring_back += char
print(mystring_back)

# *************tuples are immutable ************

t = ('p','y','t','h','o','o','n')
print(t[0])

print(t.count('o'))  # gives count

#t[0] = 't'
print(t)  # TypeError: 'tuple' object does not support item assignment

t2 = ('carrots','vegetable')
t3 = ('kiwi','fruit')
print(t3[1])

from collections import namedtuple

Food = namedtuple('Food','food type')
t2 = Food('carrots','vegetable')
t3 = Food('kiwi','fruit')
print(t3.food)
print(t3.type)

# ************** Dictionaries ************


people = {}
people['julian'] = 30
people['bob'] = 50
people['scott'] = 25

print(people)
print(f"age of scott: {people['scott']}")
#print(f"age of tiger: {people['tiger']}")  # you get KeyError: 'tiger'

# to overcome this key error you can define defaultDict
from collections import defaultdict
people_dict = defaultdict(int)
people_dict['julian'] = 30
people_dict['bob'] = 45
print(people_dict)  #  prints {'julian': 30, 'bob': 45})

print(f"age of scott: {people_dict['scott']}")  #  prints 0 instead of key error becuase we defined default dict with type value as int
print(f"age of tiger: {people_dict['tiger']}")  # prints 0


people = {'julian': 30, 'bob': 50, 'scott': 25}

for keys in people.keys():
    print(keys)

for values in people.values():
    print(values)

for keys, values in people.items():
    print(f"{keys} is of age {values}")

print(people)
print(people.keys())
print(people.values())
print(people.items())