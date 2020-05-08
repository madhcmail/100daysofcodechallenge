bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods'}
exclude_bites = (6,10)

print({key:value for (key,value) in bites.items() if key not in exclude_bites})
