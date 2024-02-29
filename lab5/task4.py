import re

def pattern(str):
    pattern = "[A-Z]{1}[a-z]+"
    sequence = re.findall(pattern,str)
    return sequence

str = str(input())
print(pattern(str))