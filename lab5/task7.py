import re

def snakeToCamel(str):
    words = str.split('_')
    CamelString= words[0]
    for char in words[1:]:
        CamelString += char.capitalize()
    return CamelString

str = str(input())
print(snakeToCamel(str))

