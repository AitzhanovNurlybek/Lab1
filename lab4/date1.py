import datetime
def days():
    x= datetime.datetime.now()
    return x.day - 5

print(days())