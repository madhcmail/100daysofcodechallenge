"""
Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is .

Input Format

The first line of input is the integer , the number of email addresses.
 lines follow, each containing a string.

Constraints

Each line is a non-empty string.

Output Format

Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""

import re


def fun(s):
    # return True if s is a valid email, else return False
    check = re.match("^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s)
    return check


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)