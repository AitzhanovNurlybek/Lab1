import math
def sphere_volume(radius):
    volume = (4/3)*3.14*(radius**3)
    return volume

radius = float(input())
volume = sphere_volume(radius)
print(volume)
