import re 
def pattern(str):
    p = r'ab*' #to find pattern a,ab,abbb,abbbbb.....a
    if re.match(p,str):
        return True 
    else:
        return False 

str = str(input())
print(pattern(str))