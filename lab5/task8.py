import re

str = str(input())
word = re.findall(r'[A-Z][^A-Z]*',str)
print(word)