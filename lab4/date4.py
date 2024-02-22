import datetime

def date_difference_in_seconds(date1, date2):
    
    difference = date2 - date1
    return difference.total_seconds()

date1 = datetime.datetime(2024, 2, 21, 12, 0, 0)  
date2 = datetime.datetime(2024, 2, 22, 12, 0, 0)  

difference_seconds = date_difference_in_seconds(date1, date2)

print("Difference in seconds:", difference_seconds)
