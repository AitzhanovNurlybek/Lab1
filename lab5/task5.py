import re 

pattern = re.compile(r'a.*b$')
str = str(input())
print(pattern.findall(str))