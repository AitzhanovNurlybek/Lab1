import time
import math

def my(num, miliseconds):
    time.sleep(miliseconds / 1000)
    res = math.sqrt(num)
    return res

num = int(input())
miliseconds = int(input())
output = my(num, miliseconds)
print(f"Square root of {num} after {miliseconds} miliseconds is", output)
