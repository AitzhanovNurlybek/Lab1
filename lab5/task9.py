import re

def insert_spaces(input_str):
    spaced_str = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_str)
    return spaced_str

input_string = str(input())
result = insert_spaces(input_string)
print(result)
