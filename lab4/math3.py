import math 
sides = int(input("Input number of sides: "))
lenght = int(input("Input the lenght of sides: "))
area = sides * (lenght**2)* (math.tan(math.pi/sides)/4)
print(area)