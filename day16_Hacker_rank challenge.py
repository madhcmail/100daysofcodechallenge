# https://www.hackerrank.com/challenges/word-order/problem

# Problem Statement:You are given  words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
'''
Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1
'''


from collections import OrderedDict

occurances = OrderedDict()
for _ in range(int(input())): # _ in for loop is used when you do not want to use the iterator values
    word = input()
    occurances[word] = occurances.get(word, 0) + 1

# print(occurances)
print(len(occurances))
print(*occurances.values())