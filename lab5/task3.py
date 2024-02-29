import re 


def find_sequence(str):
    pattern = re.compile(r"[a-z]+_[a-z]+")
    sequence = re.findall(pattern,str)
    return sequence

str = str(input())
print(find_sequence(str))