import re

phonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
cell = phonenumber.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(cell)

xmas = re.compile(r'\d+\s\w+')
jolly = xmas.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partraige')
print(jolly)

vowel = re.compile(r'[aeiouAEIOU]') #the brackets find all characters found inside of the brackets
words = vowel.findall('Artificial amateurs arent at all amazing')
print(words)

consinant = re.compile(r'[^aeiouAEIOU]') #inverse because of ^
morewords = consinant.findall('Artificial amateurs arent at all amazing')
print(morewords)

atRegex = re.compile(r'.at')
at = atRegex.findall('The cat on the mat with a hat looked fat')
cat = print(at)