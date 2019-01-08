import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())


#Greedy and non-greedy matching
greedyHaRegex = re.compile(r'(ha){3,5}') #greedy meaning that it will match the longest string
mo2 = greedyHaRegex.search('hahahahaha')
print(mo2.group())

nongreedyHaRegex = re.compile(r'(ha){3,5}?') #non-greedy matches the smallest string as a result of the optional matching (?)
mo3 = nongreedyHaRegex.search('hahahahaha')
print(mo3.group())
