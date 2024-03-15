import os

f = open(r"/Users/Aitzh/OneDrive/Рабочий стол/lab6/dir-and-files.md/4.txt")
cnt = 0
for lines in f:
    cnt += 1
print(f"file has {cnt} lines")