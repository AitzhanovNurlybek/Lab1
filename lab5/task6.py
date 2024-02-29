import re

str = str(input())
newstr = re.sub(r'[ ,.]',':',str)
print(newstr)